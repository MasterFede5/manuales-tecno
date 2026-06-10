#!/usr/bin/env python3
"""
Manual Albatros — MD → HTML doc-as-code converter.

Toma todos los .md de un manual y genera un HTML imprimible tamaño carta
con las cajas semánticas y actividades del catálogo Albatros renderizadas.

Uso:
  python build/converter.py manuales/manual-1 dist/manual-1.html
  python build/converter.py manuales/manual-1 dist/manual-1-digital.html --mode digital
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

# Windows console: forzar UTF-8 para imprimir emojis y acentos
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import markdown
import yaml
from jinja2 import Template

# Resolver de iconografía Albatros
sys.path.insert(0, str(Path(__file__).parent))
import iconografia as ico


BLOCK_RE = re.compile(
    r"^::(?P<tag>[\w-]+)(?P<attrs>\{[^}]*\})?(?:::)?\s*\n"
    r"(?P<body>.*?)"
    r"\n^::/(?P=tag)(?:::)?\s*$",
    re.DOTALL | re.MULTILINE,
)
# Tags self-closing (sin body, una sola línea): ::visual{...}
SELF_CLOSING_RE = re.compile(
    r"^::(?P<tag>visual)(?P<attrs>\{[^}]*\})\s*$",
    re.MULTILINE,
)
ATTR_RE = re.compile(r'(\w+)\s*=\s*(?:"([^"]*)"|(\S+))')


def parse_attrs(attrs_str: str | None) -> dict:
    if not attrs_str:
        return {}
    s = attrs_str.strip("{}")
    return {m.group(1): (m.group(2) or m.group(3)) for m in ATTR_RE.finditer(s)}


_MD_EXT = ["extra", "sane_lists", "tables"]
_MD_EXT_CFG: dict = {}

# === LaTeX math protection ===
# Markdown rompe `_`, `\` y `*` dentro de fórmulas. Antes de pasar a markdown,
# extraemos cada $$...$$ y $...$ y los reemplazamos por placeholders. Después
# del render, los reinyectamos como \[...\] o \(...\) que KaTeX (cliente)
# reconoce vía auto-render.
_MATH_BLOCK_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_MATH_INLINE_RE = re.compile(r"(?<!\\)\$([^$\n]+?)\$")


def _protect_math(text: str) -> tuple[str, list[tuple[str, str]]]:
    placeholders: list[tuple[str, str]] = []

    def block_sub(m):
        placeholders.append(("display", m.group(1).strip()))
        return f"@@MATHB{len(placeholders) - 1}@@"

    def inline_sub(m):
        placeholders.append(("inline", m.group(1).strip()))
        return f"@@MATHI{len(placeholders) - 1}@@"

    text = _MATH_BLOCK_RE.sub(block_sub, text)
    text = _MATH_INLINE_RE.sub(inline_sub, text)
    return text, placeholders


# Render LaTeX → MathML en build time (server-side). Si falla, deja `\[...\]`
# para que KaTeX (cliente, en el template) intente renderizarlo. Esto evita
# que las fórmulas aparezcan como `\[...\]` literal en PDFs exportados antes
# de que el JS termine de cargar.
try:
    import latex2mathml.converter as _l2m
    _HAS_L2M = True
except ImportError:
    _HAS_L2M = False


def _latex_to_mathml(expr: str, display: bool) -> str | None:
    if not _HAS_L2M:
        return None
    try:
        return _l2m.convert(expr, display="block" if display else "inline")
    except Exception:
        return None


def _restore_math(html: str, placeholders: list[tuple[str, str]]) -> str:
    for i, (mode, expr) in enumerate(placeholders):
        is_display = mode == "display"
        mathml = _latex_to_mathml(expr, is_display)
        if mathml is not None:
            cls = "math-display" if is_display else "math-inline"
            tag = "div" if is_display else "span"
            replacement = f'<{tag} class="{cls}">{mathml}</{tag}>'
        else:
            # Fallback: que KaTeX (cliente) intente
            if is_display:
                replacement = f'<div class="math-display">\\[{expr}\\]</div>'
            else:
                replacement = f'<span class="math-inline">\\({expr}\\)</span>'
        ph = f"@@MATHB{i}@@" if is_display else f"@@MATHI{i}@@"
        html = html.replace(ph, replacement)
    return html


def md(text: str) -> str:
    text_protected, ph = _protect_math(text)
    html = markdown.markdown(
        text_protected, extensions=_MD_EXT, extension_configs=_MD_EXT_CFG
    )
    return _restore_math(html, ph)


def _icon_html(query: str, mode: str = "print", size: int = 20) -> str:
    """Helper: resuelve un ícono y devuelve HTML inline."""
    return ico.render_inline(query, size=size, mode=mode)


def _clean_heading(prefix: str, titulo: str) -> str:
    """Antepone `prefix` a `titulo`, salvo que `titulo` ya empiece por él."""
    if not titulo:
        return prefix
    if titulo.strip().lower().startswith(prefix.strip().lower()):
        return titulo
    return f"{prefix} - {titulo}"


# === Normalización del cuerpo de bloques semánticos ============================
# Markdown necesita una línea en blanco antes de tablas (`|`) y listas (`1.`,
# `- `, `* `) para reconocerlas. Dentro de bloques `::albatros::` los autores
# pegan estos elementos al texto (`**Rúbrica.**\n| ... |`). Sin la línea en
# blanco, salen como párrafos crudos llenos de pipes (lo que el usuario ve como
# "código suelto" al imprimir el PDF).
_LIST_LINE_RE = re.compile(r"^\s*(?:\d+\.|[-*+])\s+\S")
_TABLE_LINE_RE = re.compile(r"^\s*\|")
_BLANK_RE = re.compile(r"^\s*$")


_SEP_LINE_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")


def _count_pipe_columns(line: str) -> int:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return len(s.split("|"))


def _inject_table_separators(lines: list[str]) -> list[str]:
    """Si encuentra una secuencia de filas pipe sin separador `|---|`, lo inserta."""
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if _TABLE_LINE_RE.match(line):
            # Recolecta toda la racha de filas pipe consecutivas
            j = i
            block: list[str] = []
            while j < n and _TABLE_LINE_RE.match(lines[j]):
                block.append(lines[j])
                j += 1
            has_sep = any(_SEP_LINE_RE.match(b) for b in block)
            if not has_sep and len(block) >= 2:
                cols = _count_pipe_columns(block[0])
                sep = "| " + " | ".join(["---"] * cols) + " |"
                out.append(block[0])
                out.append(sep)
                out.extend(block[1:])
            else:
                out.extend(block)
            i = j
            continue
        out.append(line)
        i += 1
    return out


def _normalize_block_body(body: str) -> str:
    """Inserta línea en blanco antes de listas/tablas y un separador a tablas sin él."""
    lines = body.split("\n")
    out: list[str] = []
    for i, line in enumerate(lines):
        if i > 0:
            prev = lines[i - 1]
            is_list = bool(_LIST_LINE_RE.match(line))
            is_table = bool(_TABLE_LINE_RE.match(line))
            prev_blank = bool(_BLANK_RE.match(prev))
            prev_list = bool(_LIST_LINE_RE.match(prev))
            prev_table = bool(_TABLE_LINE_RE.match(prev))
            if is_list and not (prev_blank or prev_list):
                out.append("")
            elif is_table and not (prev_blank or prev_table):
                out.append("")
        out.append(line)
    return "\n".join(_inject_table_separators(out))


# === Generador de sopa de letras ==============================================
import random as _random
import unicodedata as _ud

_DIRS = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1)]


def _strip_accents(s: str) -> str:
    return "".join(c for c in _ud.normalize("NFD", s) if _ud.category(c) != "Mn")


def _extract_word_list(body: str) -> list[str]:
    """Extrae palabras a buscar de un cuerpo de sopa de letras."""
    text = body
    m = re.search(r"(?i)(?:encuentra|busca|palabras?)\s*:\s*(.+)", text)
    chunk = m.group(1) if m else text
    chunk = chunk.split("\n\n")[0]
    parts = re.split(r"[,\n;]+", chunk)
    seen: set[str] = set()
    words: list[str] = []
    for p in parts:
        p = re.sub(r"[\.\)\(]", " ", p)
        p = re.sub(r"^\s*[\d•\-*]+\s*", "", p).strip()
        clean = _strip_accents(p).upper()
        clean = re.sub(r"[^A-Z]", "", clean)
        if 3 <= len(clean) <= 18 and clean not in seen:
            seen.add(clean)
            words.append(clean)
    return words[:18]


def _generate_word_search(words: list[str], size: int, seed: int) -> tuple[list[list[str]], list[str]]:
    """Crea un grid NxN determinista con las palabras colocadas. Devuelve grid y palabras realmente colocadas."""
    rng = _random.Random(seed)
    grid: list[list[str]] = [["" for _ in range(size)] for _ in range(size)]
    placed: list[str] = []

    def fits(w: str, r: int, c: int, dr: int, dc: int) -> bool:
        for i, ch in enumerate(w):
            rr, cc = r + dr * i, c + dc * i
            if not (0 <= rr < size and 0 <= cc < size):
                return False
            if grid[rr][cc] not in ("", ch):
                return False
        return True

    def put(w: str, r: int, c: int, dr: int, dc: int) -> None:
        for i, ch in enumerate(w):
            grid[r + dr * i][c + dc * i] = ch

    for word in sorted(words, key=len, reverse=True):
        if len(word) > size:
            continue
        ok = False
        for _ in range(400):
            dr, dc = rng.choice(_DIRS)
            r = rng.randrange(size)
            c = rng.randrange(size)
            if fits(word, r, c, dr, dc):
                put(word, r, c, dr, dc)
                placed.append(word)
                ok = True
                break
        if not ok:
            # último intento: horizontal en la primera fila libre
            for r in range(size):
                for c in range(size - len(word) + 1):
                    if fits(word, r, c, 0, 1):
                        put(word, r, c, 0, 1)
                        placed.append(word)
                        ok = True
                        break
                if ok:
                    break

    for r in range(size):
        for c in range(size):
            if grid[r][c] == "":
                grid[r][c] = chr(rng.randint(ord("A"), ord("Z")))
    return grid, placed


def _render_word_search(words: list[str], size: int, seed: int) -> str:
    grid, placed = _generate_word_search(words, size, seed)
    rows = "".join(
        "<tr>" + "".join(f"<td>{ch}</td>" for ch in row) + "</tr>" for row in grid
    )
    chips = "".join(f'<li class="ws-word">{html.escape(w)}</li>' for w in placed)
    return (
        f'<div class="word-search" data-size="{size}">'
        f'<table class="ws-grid"><tbody>{rows}</tbody></table>'
        f'<ul class="ws-words">{chips}</ul>'
        f"</div>"
    )


# === Generador de crucigrama (auto-place greedy) ==============================
_CLUE_RE = re.compile(
    r"^\s*(\d+)\.\s*(.+?)(?:\s*\(palabra:\s*([A-Za-zÁÉÍÓÚÜÑáéíóúüñ\-]+)\s*\))?\s*$"
)


def _extract_crossword_clues(body: str) -> tuple[list[tuple[int, str, str]], list[tuple[int, str, str]]]:
    """Devuelve (horizontales, verticales) como lista de (numero, pista, palabra_o_vacio)."""
    horiz: list[tuple[int, str, str]] = []
    vert: list[tuple[int, str, str]] = []
    bucket: list[tuple[int, str, str]] | None = None
    for raw in body.split("\n"):
        line = raw.rstrip()
        low = line.strip().lower()
        if low.startswith("horizontal"):
            bucket = horiz
            continue
        if low.startswith("vertical"):
            bucket = vert
            continue
        if bucket is None:
            continue
        m = _CLUE_RE.match(line)
        if not m:
            continue
        num = int(m.group(1))
        pista = m.group(2).strip()
        palabra = m.group(3) or ""
        palabra = _strip_accents(palabra).upper()
        bucket.append((num, pista, palabra))
    return horiz, vert


def _try_place_crossword(
    horiz: list[tuple[int, str, str]],
    vert: list[tuple[int, str, str]],
    size: int,
) -> dict | None:
    """Coloca palabras con cruces. Devuelve {'cells':{(r,c):letra}, 'starts':{(r,c):num}, 'across':[...], 'down':[...]} o None."""
    h_words = [(n, p, w) for (n, p, w) in horiz if w]
    v_words = [(n, p, w) for (n, p, w) in vert if w]
    if not h_words and not v_words:
        return None

    cells: dict[tuple[int, int], str] = {}
    starts: dict[tuple[int, int], int] = {}
    placed_h: list[tuple[int, str, str, int, int]] = []  # (num, pista, palabra, r, c)
    placed_v: list[tuple[int, str, str, int, int]] = []

    def fits(word: str, r: int, c: int, dr: int, dc: int) -> bool:
        # No tocar palabras ortogonales pegadas
        before = (r - dr, c - dc)
        after = (r + dr * len(word), c + dc * len(word))
        if before in cells or after in cells:
            return False
        for i, ch in enumerate(word):
            rr, cc = r + dr * i, c + dc * i
            if not (0 <= rr < size and 0 <= cc < size):
                return False
            existing = cells.get((rr, cc))
            if existing is not None and existing != ch:
                return False
            if existing is None:
                # vecinos ortogonales no deben estar ocupados (paralelo cercano)
                if dr == 0:  # horizontal: revisar arriba y abajo
                    if (rr - 1, cc) in cells or (rr + 1, cc) in cells:
                        return False
                else:  # vertical: izquierda/derecha
                    if (rr, cc - 1) in cells or (rr, cc + 1) in cells:
                        return False
        return True

    def put(num: int, pista: str, word: str, r: int, c: int, dr: int, dc: int, bucket: list) -> None:
        for i, ch in enumerate(word):
            cells[(r + dr * i, c + dc * i)] = ch
        starts[(r, c)] = num
        bucket.append((num, pista, word, r, c))

    # Coloca la palabra horizontal más larga centrada
    all_words = sorted(h_words + v_words, key=lambda t: -len(t[2]))
    if not all_words:
        return None
    first = all_words[0]
    is_h = first in h_words
    word = first[2]
    r0 = size // 2
    c0 = max(0, (size - len(word)) // 2)
    if is_h:
        put(first[0], first[1], word, r0, c0, 0, 1, placed_h)
        h_words = [t for t in h_words if t != first]
    else:
        put(first[0], first[1], word, c0, r0, 1, 0, placed_v)
        v_words = [t for t in v_words if t != first]

    # Greedy: para cada palabra restante, busca un cruce
    remaining = sorted(h_words + v_words, key=lambda t: -len(t[2]))
    for tup in remaining:
        num, pista, word = tup
        is_h_target = tup in h_words
        best: tuple[int, int, int, int] | None = None
        for i, ch in enumerate(word):
            for (rr, cc), existing in list(cells.items()):
                if existing != ch:
                    continue
                if is_h_target:
                    r = rr
                    c = cc - i
                    if fits(word, r, c, 0, 1):
                        best = (r, c, 0, 1)
                        break
                else:
                    r = rr - i
                    c = cc
                    if fits(word, r, c, 1, 0):
                        best = (r, c, 1, 0)
                        break
            if best:
                break
        if best:
            r, c, dr, dc = best
            put(num, pista, word, r, c, dr, dc, placed_h if is_h_target else placed_v)

    if not (placed_h or placed_v):
        return None
    return {"cells": cells, "starts": starts, "across": placed_h, "down": placed_v}


def _render_crossword(body: str, size: int) -> str:
    horiz, vert = _extract_crossword_clues(body)
    layout = _try_place_crossword(horiz, vert, size)

    def _clue_list(items: list[tuple[int, str, str]] | list, with_pos: bool = False) -> str:
        if not items:
            return "<li><em>Sin pistas</em></li>"
        lis = []
        for it in items:
            if with_pos:
                num, pista, _w, _r, _c = it
            else:
                num, pista, _w = it
            lis.append(f"<li><strong>{num}.</strong> {html.escape(pista)}</li>")
        return "".join(lis)

    if layout is None:
        # Fallback: rejilla en blanco + pistas sin posiciones
        cells_html = "".join(
            f'<div class="cw-cell cw-blank"></div>' for _ in range(size * size)
        )
        return (
            f'<div class="crossword crossword-empty" style="--cw-size:{size};">'
            f'<div class="cw-grid">{cells_html}</div>'
            f'<div class="cw-clues">'
            f'<div class="cw-clue-col"><h5>Horizontales</h5><ol>{_clue_list(horiz)}</ol></div>'
            f'<div class="cw-clue-col"><h5>Verticales</h5><ol>{_clue_list(vert)}</ol></div>'
            f"</div>"
            f'<p class="cw-note">Las pistas no traen palabra explícita. Usa la rejilla como espacio de trabajo.</p>'
            f"</div>"
        )

    cells = layout["cells"]
    starts = layout["starts"]
    grid_html: list[str] = []
    for r in range(size):
        for c in range(size):
            if (r, c) in cells:
                num = starts.get((r, c))
                num_html = f'<span class="cw-num">{num}</span>' if num else ""
                grid_html.append(f'<div class="cw-cell cw-open">{num_html}</div>')
            else:
                grid_html.append('<div class="cw-cell cw-block"></div>')
    return (
        f'<div class="crossword" style="--cw-size:{size};">'
        f'<div class="cw-grid">{"".join(grid_html)}</div>'
        f'<div class="cw-clues">'
        f'<div class="cw-clue-col"><h5>Horizontales</h5><ol>{_clue_list(layout["across"], with_pos=True)}</ol></div>'
        f'<div class="cw-clue-col"><h5>Verticales</h5><ol>{_clue_list(layout["down"], with_pos=True)}</ol></div>'
        f"</div></div>"
    )


# === Mapa mental SVG ==========================================================
import math as _math


def _render_mindmap_svg(centro: str, n_primarios: int) -> str:
    n = max(3, min(12, int(n_primarios)))
    # Lienzo: 700x340 (ratio amigable a US letter en mm)
    W, H = 700, 340
    cx, cy = W / 2, H / 2
    rx_orbit, ry_orbit = 280, 130
    bubble_w, bubble_h = 110, 36
    nodes = []
    lines = []
    for i in range(n):
        angle = -_math.pi / 2 + i * 2 * _math.pi / n
        x = cx + rx_orbit * _math.cos(angle)
        y = cy + ry_orbit * _math.sin(angle)
        lines.append(
            f'<line x1="{cx:.0f}" y1="{cy:.0f}" x2="{x:.0f}" y2="{y:.0f}" '
            f'stroke="#94A3B8" stroke-width="1.2" stroke-dasharray="4 3"/>'
        )
        nodes.append(
            f'<g><rect x="{x - bubble_w/2:.0f}" y="{y - bubble_h/2:.0f}" '
            f'width="{bubble_w}" height="{bubble_h}" rx="14" ry="14" '
            f'fill="#FFFFFF" stroke="#0E3A8A" stroke-width="1.2"/>'
            f'<text x="{x:.0f}" y="{y + 4:.0f}" text-anchor="middle" '
            f'font-family="Inter, Arial, sans-serif" font-size="11" fill="#475569">'
            f"Idea {i + 1}</text></g>"
        )
    centro_safe = html.escape(centro or "TEMA CENTRAL")
    return (
        f'<svg class="mindmap-svg" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="Mapa mental para llenar">'
        f"{''.join(lines)}"
        f'<g><ellipse cx="{cx}" cy="{cy}" rx="95" ry="38" fill="#0E3A8A" stroke="#0E3A8A"/>'
        f'<text x="{cx}" y="{cy + 5:.0f}" text-anchor="middle" '
        f'font-family="Montserrat, Arial, sans-serif" font-weight="700" font-size="13" fill="#FFFFFF">'
        f"{centro_safe}</text></g>"
        f"{''.join(nodes)}"
        f"</svg>"
    )


# Tags semánticos donde el body es prosa con tablas/listas pegadas (necesitan
# normalización). Las actividades tienen su propio renderer y no se normalizan
# por defecto para no romper sintaxis específica (ej. checkboxes).
_SEMANTIC_TAGS = {
    "concepto", "interioriza", "pausa", "practica", "caso",
    "implementacion", "albatros", "tecno", "investiga", "fuentes",
    "act-case", "act-challenge", "act-table", "act-match", "act-calc",
    "act-fill", "act-mcq", "act-tf", "act-order", "act-label", "act-mindmap",
}


def render_block(tag: str, attrs: dict, body: str, mode: str = "print") -> str:
    titulo = attrs.get("titulo", "")
    # Normaliza tablas/listas pegadas a texto antes de pasar a markdown.
    if tag in _SEMANTIC_TAGS:
        body = _normalize_block_body(body)
    body_html = md(body)
    icon_override = attrs.get("icono")

    def block_icon(default_alias: str) -> str:
        return _icon_html(icon_override or default_alias, mode=mode, size=20)

    if tag == "concepto":
        return f'<aside class="box-concepto"><h4>{block_icon("bloque-concepto")} {_clean_heading("Concepto", titulo)}</h4>{body_html}</aside>'
    if tag == "interioriza":
        return f'<aside class="box-interioriza"><h4>{block_icon("bloque-interioriza")} {titulo or "Por que te importa"}</h4>{body_html}</aside>'
    if tag == "pausa":
        return f'<aside class="box-pausa"><h4>{block_icon("bloque-pausa")} {titulo or "Pausa para pensar"}</h4>{body_html}</aside>'
    if tag == "practica":
        return f'<section class="box-practica"><h4>{block_icon("bloque-practica")} {titulo or "Practica resuelta"}</h4>{body_html}</section>'
    if tag == "caso":
        ep = attrs.get("episodio", "")
        return f'<section class="box-caso" data-ep="{html.escape(ep, quote=True)}"><span class="caso-tag">{block_icon("bloque-caso")} Caso Albatros - Episodio {ep}</span>{body_html}</section>'
    if tag == "implementacion":
        return f'<section class="box-implementacion"><h3>{block_icon("bloque-implementacion")} {titulo or "Implementacion Albatros"}</h3>{body_html}</section>'
    if tag == "albatros":
        tipo = attrs.get("tipo", "reto")
        tiempo = attrs.get("tiempo", "")
        subtipo_icon = _icon_html(f"tipo-albatros-{tipo}", mode=mode, size=18)
        return (
            f'<section class="box-albatros" data-tipo="{html.escape(tipo, quote=True)}">'
            f'<h3>{block_icon("bloque-albatros")} {_clean_heading("Actividad Albatros", titulo)}</h3>'
            f'<span class="meta">{subtipo_icon} Tipo: <em>{tipo}</em> - Tiempo: {tiempo}</span>'
            f"{body_html}</section>"
        )
    if tag == "tecno":
        tipo = attrs.get("tipo", "maker")
        tiempo = attrs.get("tiempo", "")
        subtipo_icon = _icon_html(f"tipo-tecno-{tipo}", mode=mode, size=18)
        return (
            f'<section class="box-tecno" data-tipo="{html.escape(tipo, quote=True)}">'
            f'<h3>{block_icon("bloque-tecno")} {_clean_heading("Actividad Tecno", titulo)}</h3>'
            f'<span class="meta">{subtipo_icon} Tipo: <em>{tipo}</em> - Tiempo: {tiempo}</span>'
            f"{body_html}</section>"
        )
    if tag == "investiga":
        tiempo = attrs.get("tiempo", "")
        return (
            f'<section class="box-investiga"><h3>{block_icon("bloque-investiga")} {_clean_heading("Investigacion", titulo)}</h3>'
            f'<span class="meta">Tiempo estimado: {tiempo}</span>'
            f"{body_html}</section>"
        )
    if tag == "fuentes":
        return f'<aside class="box-fuentes"><h4>{block_icon("bloque-fuentes")} {titulo or "Fuentes recomendadas"}</h4>{body_html}</aside>'
    if tag == "visual":
        return render_visual(attrs, mode=mode)

    if tag == "act-fill":
        body_lines = re.sub(r"_{3,}", '<span class="blank"></span>', body)
        return f'<div class="act-fill"><h4>{_clean_heading("Completa", titulo)}</h4>{md(body_lines)}</div>'
    if tag == "act-mcq":
        h = body_html.replace("[ ]", '<span class="mcq mcq-empty"></span>')
        h = h.replace("[x]", '<span class="mcq mcq-correct"></span>')
        return f'<div class="act-mcq"><h4>{_clean_heading("Opcion multiple", titulo)}</h4>{h}</div>'
    if tag == "act-table":
        return f'<div class="act-table"><h4>{_clean_heading("Tabla", titulo)}</h4>{body_html}</div>'
    if tag == "act-calc":
        renglones = int(attrs.get("renglones", "8"))
        height = max(renglones * 6, 48)
        return (
            f'<div class="act-calc"><h4>{_clean_heading("Calculo", titulo)}</h4>{body_html}'
            f'<div class="grid-area" style="min-height: {height}mm;"></div></div>'
        )
    if tag == "act-match":
        return f'<div class="act-match"><h4>{_clean_heading("Relaciona", titulo)}</h4>{body_html}</div>'
    if tag == "act-tf":
        body_lines = re.sub(r"_{3,}", '<span class="blank"></span>', body)
        return f'<div class="act-tf"><h4>{_clean_heading("Verdadero/Falso", titulo)}</h4>{md(body_lines)}</div>'
    if tag == "act-order":
        return f'<div class="act-order"><h4>{_clean_heading("Ordena", titulo)}</h4>{body_html}</div>'
    if tag == "act-case":
        lineas = int(attrs.get("lineas", "8"))
        spaces = "".join('<div class="resp-line"></div>' for _ in range(lineas))
        return f'<section class="act-case"><h4>{_clean_heading("Caso", titulo)}</h4>{body_html}{spaces}</section>'
    if tag == "act-challenge":
        return f'<aside class="act-challenge"><h4>{_clean_heading("Reto", titulo)}</h4>{body_html}</aside>'
    if tag == "act-puzzle":
        tipo = attrs.get("tipo", "crucigrama").lower()
        tamano = attrs.get("tamano", "12x12")
        try:
            size = int(re.split(r"[x×]", tamano)[0])
        except (ValueError, IndexError):
            size = 12
        size = max(8, min(20, size))
        if tipo in ("sopa-letras", "sopa", "wordsearch", "word-search"):
            words = _extract_word_list(body)
            seed = abs(hash((tuple(words), size))) & 0xFFFFFFFF
            puzzle_html = _render_word_search(words, size, seed) if words else (
                '<p class="cw-note">No se encontraron palabras en el cuerpo del bloque.</p>'
            )
        elif tipo in ("crucigrama", "crossword"):
            puzzle_html = _render_crossword(body, size)
        else:
            puzzle_html = (
                f'<div class="puzzle-placeholder">Tipo de puzzle no soportado: {html.escape(tipo)}</div>'
            )
        return (
            f'<div class="act-puzzle act-puzzle-{html.escape(tipo, quote=True)}">'
            f'<h4>{_clean_heading("Puzzle", titulo)}</h4>{body_html}{puzzle_html}</div>'
        )
    if tag == "act-mindmap":
        centro = attrs.get("centro", "")
        n1 = int(attrs.get("nodos_primarios", "6") or 6)
        svg = _render_mindmap_svg(centro, n1)
        return (
            f'<div class="act-mindmap"><h4>{_clean_heading("Mapa mental", titulo)}</h4>{body_html}'
            f'<div class="mindmap-canvas">{svg}</div></div>'
        )
    if tag == "act-label":
        return f'<div class="act-label"><h4>{_clean_heading("Etiqueta", titulo)}</h4>{body_html}</div>'

    return f"<!-- bloque desconocido: {tag} -->"


# ============================================================================
# Generadores de ilustraciones reales a partir del briefing al ilustrador
# (atributo `descripcion=`). Para cada `tipo=` reconocido, se intenta parsear
# la descripción y producir un SVG/HTML que ocupe el espacio definido por
# `paginas=`. Si el parsing falla, cae al renderer genérico estructurado.
# ============================================================================

_PALETTE = [
    "#0E3A8A",  # azul Albatros
    "#0F766E",  # verde-azul
    "#C2410C",  # naranja oscuro
    "#6D28D9",  # violeta
    "#B45309",  # ámbar
    "#9D174D",  # rosa oscuro
    "#0E7490",  # cian
    "#15803D",  # verde
]


def _frame_dims(paginas: float) -> tuple[int, int, str]:
    """Dimensiones del SVG según `paginas`. Devuelve (W, H, css_height).
    Lienzos generosos: las fuentes en SVG están en unidades del viewBox; un lienzo
    con dimensiones grandes ofrece más holgura para distribuir contenido sin
    encimar. El `css_height` controla cuánto alto físico ocupa al imprimir.
    """
    if paginas >= 1.5:
        return 1100, 780, "22cm"
    if paginas >= 1.0:
        return 1080, 660, "18.5cm"
    if paginas >= 0.6:
        return 1000, 460, "12.5cm"
    return 920, 340, "9cm"


def _split_clauses(text: str) -> list[str]:
    """Divide por `;` primero. Si solo hay 1 cláusula larga, divide por puntos
    que separen oraciones (`.` seguido de espacio + mayúscula)."""
    text = text.strip().rstrip(".")
    parts = re.split(r"\s*[;]\s*", text)
    if len(parts) <= 1:
        # Fallback: dividir por punto-y-mayúscula
        parts = re.split(r"(?<=[a-z\)])\.\s+(?=[A-ZÁÉÍÓÚÜÑ0-9])", text)
    return [p.strip() for p in parts if p.strip()]


def _wrap_text(text: str, max_chars: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= max_chars:
            cur = f"{cur} {w}"
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _svg_text_lines(x: float, y: float, lines: list[str], font_size: int, fill: str = "#111827", weight: str = "400", anchor: str = "middle") -> str:
    line_h = font_size * 1.15
    # Centra verticalmente el bloque sobre y
    start = y - (len(lines) - 1) * line_h / 2
    spans = []
    for i, ln in enumerate(lines):
        ly = start + i * line_h
        spans.append(
            f'<text x="{x:.0f}" y="{ly:.1f}" text-anchor="{anchor}" '
            f'font-family="Inter, Arial, sans-serif" font-size="{font_size}" '
            f'font-weight="{weight}" fill="{fill}">{html.escape(ln)}</text>'
        )
    return "".join(spans)


# ---------- Mapa mental --------------------------------------------------------

_MM_CENTER_RE = re.compile(
    r"(?:nodo\s+)?central(?:\s+(?:es|=))?\s+[\"'']?"
    r"([A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 \-\+/\.]*?)"
    r"[\"'']?(?=\s+(?:en|y|con)\s+|[\.,;])",
    re.IGNORECASE,
)
_MM_NAME_RE = re.compile(
    r"^([A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 \-\+/\.]+?)"
    r"(?=\s+\(|\s+—\s+|\s+-\s+|\s+con\s+sub|[\.;:]|$)"
)
_MM_SUBS_PARENS_RE = re.compile(r"\(([^)]+)\)")
_MM_SUBS_NODOS_RE = re.compile(r"(?:con\s+sub-?nodos?|sub-?nodos?\s*:)\s*([^\.;]+)")
_MM_SUBS_DASH_RE = re.compile(r"[—–\-]\s*(?:tipos|sub-?nodos?\s*\w*)?\s*[\(:]?\s*([A-Za-z][^.;]+)")


def _parse_mindmap(desc: str) -> dict | None:
    if not desc:
        return None
    cm = _MM_CENTER_RE.search(desc)
    centro = cm.group(1).strip() if cm else None
    # Divide por puntos numerados "1)", "2)", ...
    segments = re.split(r"\s*\d+\)\s*", desc)
    branches: list[tuple[str, list[str]]] = []
    for seg in segments[1:]:
        seg = seg.strip().rstrip(".;,")
        if not seg:
            continue
        nm = _MM_NAME_RE.match(seg)
        if not nm:
            continue
        name = nm.group(1).strip(" -.")
        # Sub-nodos: paréntesis, "con sub-nodos", o tras "—" / ":"
        subs_raw = ""
        sm = _MM_SUBS_PARENS_RE.search(seg)
        if sm:
            subs_raw = sm.group(1)
            # Si el contenido del paréntesis empieza con "sub-nodos:", limpiar
            subs_raw = re.sub(r"^\s*sub-?nodos?\s*:\s*", "", subs_raw, flags=re.IGNORECASE)
        if not subs_raw:
            sm = _MM_SUBS_NODOS_RE.search(seg)
            if sm:
                subs_raw = sm.group(1)
        subs = [s.strip() for s in re.split(r"[,·•]", subs_raw) if s.strip()]
        subs = [s if len(s) <= 24 else s[:22] + "…" for s in subs[:6]]
        if name and len(name) >= 3:
            branches.append((name, subs))
    if not branches:
        return None
    if not centro:
        head = desc.split("1)")[0]
        m = re.search(r"([A-ZÁÉÍÓÚÜÑ][A-ZÁÉÍÓÚÜÑ0-9 ]{2,}?)(?=\s+(?:en|y|con)\s+|[\.,;])", head)
        centro = m.group(1).strip() if m else "TEMA CENTRAL"
    return {"centro": centro[:40], "branches": branches[:8]}


def _render_visual_mindmap(desc: str, paginas: float) -> str | None:
    """Mapa mental con layout adaptativo:
    - ≤6 ramas: distribución radial con sub-nodos APILADOS verticalmente al lado
      exterior de cada rama (sin solapamiento entre cuadrantes).
    - ≥7 ramas: las ramas se reparten en cuadrantes; cada rama tiene una columna
      pequeña de sub-nodos. Centro arriba para liberar espacio.
    Fuentes generosas (centro 20pt, ramas 15pt, subs 12pt) pensadas para PDF.
    """
    parsed = _parse_mindmap(desc)
    if not parsed:
        return None
    centro = parsed["centro"]
    branches = parsed["branches"]
    n = len(branches)
    # Asegura siempre lienzo grande para mindmap (es el visual con más densidad)
    pag = max(paginas, 1.0)
    W, H, _ = _frame_dims(pag)
    parts: list[str] = []

    # === Layout radial (n ≤ 6) ===
    if n <= 6:
        cx, cy = W / 2, H / 2
        # Tamaños generosos
        bub_w, bub_h = 200, 64
        sub_w, sub_h = 168, 32
        center_rx, center_ry = 150, 64
        # Orbita: alejada para no chocar con centro grande
        rx_orbit = W * 0.34
        ry_orbit = H * 0.30
        for i, (name, subs) in enumerate(branches):
            angle = -_math.pi / 2 + i * 2 * _math.pi / n
            bx = cx + rx_orbit * _math.cos(angle)
            by = cy + ry_orbit * _math.sin(angle)
            color = _PALETTE[i % len(_PALETTE)]
            # Conector centro → rama
            parts.append(
                f'<path d="M {cx:.0f} {cy:.0f} L {bx:.0f} {by:.0f}" '
                f'fill="none" stroke="{color}" stroke-width="2.5" opacity="0.55"/>'
            )
            # Burbuja rama
            name_lines = _wrap_text(name, 22)[:2]
            parts.append(
                f'<rect x="{bx - bub_w / 2:.0f}" y="{by - bub_h / 2:.0f}" '
                f'width="{bub_w}" height="{bub_h}" rx="14" ry="14" '
                f'fill="{color}" stroke="{color}"/>'
            )
            parts.append(
                _svg_text_lines(bx, by, name_lines, font_size=15, fill="#FFFFFF", weight="700")
            )
            # Sub-nodos APILADOS hacia el exterior de la rama (no en arco)
            if subs:
                # Dirección: lejos del centro
                dx = bx - cx
                dy = by - cy
                dist = max(1.0, _math.hypot(dx, dy))
                ux, uy = dx / dist, dy / dist
                # Punto base donde arrancan los subs (apenas fuera de la burbuja)
                base_x = bx + ux * (bub_w / 2 + 18)
                base_y = by + uy * (bub_h / 2 + 18)
                ns = min(len(subs), 5)
                step = sub_h + 6
                # Centra la columna de subs verticalmente
                col_height = (ns - 1) * step
                start_y = base_y - col_height / 2
                for j, sub in enumerate(subs[:ns]):
                    sx = base_x
                    sy = start_y + j * step
                    # Recorta dentro del lienzo
                    sx = max(sub_w / 2 + 6, min(W - sub_w / 2 - 6, sx))
                    sy = max(sub_h / 2 + 6, min(H - sub_h / 2 - 6, sy))
                    parts.append(
                        f'<rect x="{sx - sub_w / 2:.0f}" y="{sy - sub_h / 2:.0f}" '
                        f'width="{sub_w}" height="{sub_h}" rx="10" ry="10" '
                        f'fill="#FFFFFF" stroke="{color}" stroke-width="1.4"/>'
                    )
                    parts.append(
                        _svg_text_lines(sx, sy, [sub[:24]], font_size=12, fill=color, weight="600")
                    )
        # Centro al final
        centro_lines = _wrap_text(centro, 20)[:2]
        parts.append(
            f'<ellipse cx="{cx}" cy="{cy}" rx="{center_rx}" ry="{center_ry}" '
            f'fill="#0E3A8A" stroke="#0E3A8A"/>'
        )
        parts.append(
            _svg_text_lines(cx, cy, centro_lines, font_size=20, fill="#FFFFFF", weight="700")
        )
    # === Layout grilla (n ≥ 7) ===
    else:
        cols = 4 if n >= 7 else 3
        rows = (n + cols - 1) // cols
        # Centro en la esquina superior izquierda como tarjeta dedicada
        cell_w = W / cols
        cell_h = (H - 90) / rows  # reserva espacio arriba para centro
        center_x, center_y = W / 2, 50
        center_rx, center_ry = 220, 38
        bub_w, bub_h = min(cell_w * 0.85, 220), 46
        sub_w, sub_h = min(cell_w * 0.78, 200), 26
        for i, (name, subs) in enumerate(branches):
            row = i // cols
            col = i % cols
            cx_cell = cell_w * (col + 0.5)
            cy_cell = 110 + cell_h * row + 10
            color = _PALETTE[i % len(_PALETTE)]
            # Conector desde centro a la rama (curvo)
            parts.append(
                f'<path d="M {center_x:.0f} {center_y + center_ry:.0f} '
                f'Q {(center_x + cx_cell) / 2:.0f} {(center_y + cy_cell) / 2:.0f}, '
                f'{cx_cell:.0f} {cy_cell:.0f}" '
                f'fill="none" stroke="{color}" stroke-width="2" opacity="0.4"/>'
            )
            # Rama
            name_lines = _wrap_text(name, 24)[:2]
            parts.append(
                f'<rect x="{cx_cell - bub_w / 2:.0f}" y="{cy_cell:.0f}" '
                f'width="{bub_w}" height="{bub_h}" rx="12" ry="12" '
                f'fill="{color}" stroke="{color}"/>'
            )
            parts.append(
                _svg_text_lines(cx_cell, cy_cell + bub_h / 2, name_lines, font_size=13, fill="#FFFFFF", weight="700")
            )
            # Sub-nodos apilados debajo
            if subs:
                ns = min(len(subs), 4)
                step = sub_h + 4
                start_y = cy_cell + bub_h + 8 + sub_h / 2
                for j, sub in enumerate(subs[:ns]):
                    sx = cx_cell
                    sy = start_y + j * step
                    if sy + sub_h / 2 > H - 4:
                        break
                    parts.append(
                        f'<rect x="{sx - sub_w / 2:.0f}" y="{sy - sub_h / 2:.0f}" '
                        f'width="{sub_w}" height="{sub_h}" rx="8" ry="8" '
                        f'fill="#FFFFFF" stroke="{color}" stroke-width="1.2"/>'
                    )
                    parts.append(
                        _svg_text_lines(sx, sy, [sub[:22]], font_size=11, fill=color, weight="600")
                    )
        # Centro
        centro_lines = _wrap_text(centro, 30)[:1]
        parts.append(
            f'<ellipse cx="{center_x}" cy="{center_y}" rx="{center_rx}" ry="{center_ry}" '
            f'fill="#0E3A8A" stroke="#0E3A8A"/>'
        )
        parts.append(
            _svg_text_lines(center_x, center_y, centro_lines, font_size=18, fill="#FFFFFF", weight="700")
        )

    svg = (
        f'<svg class="visual-svg visual-svg-mindmap" viewBox="0 0 {W} {H}" '
        f'preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="Mapa mental: {html.escape(centro)}">{"".join(parts)}</svg>'
    )
    return svg


# ---------- Diagrama de flujo --------------------------------------------------

_FLOW_STEP_RE = re.compile(r"\s*(?:→|->|⇒|=>)\s*")


# Patrón secundario: enumeraciones tipo "5 cajas: X, Y, Z" o "tres estaciones (A X, B Y, C Z)"
_FLOW_ENUM_INTRO_RE = re.compile(
    r"(?:cinco|seis|siete|ocho|tres|cuatro|dos|\d+)\s+"
    r"(?:cajas?|etapas?|estaciones?|pasos?|fases?|bloques?|nodos?)"
    r"\s*(?:[:\(]|conectad)",
    re.IGNORECASE,
)
_FLOW_LETTER_ITEM_RE = re.compile(r"\b([A-E])\s+([A-Za-zÁÉÍÓÚÜÑáéíóúüñ][^,;\)]+)")
_FLOW_NUM_ITEM_RE = re.compile(r"\b(\d+)\)\s*([A-Za-zÁÉÍÓÚÜÑáéíóúüñ][^,;\.]+?)(?=,\s*\d+\)|[\.;]|$)")


def _parse_flowchart(desc: str) -> list[tuple[str, str]] | None:
    if not desc:
        return None
    # Caso 1: cadena con flechas explícitas (→ o ->)
    candidates = re.split(r"(?<=[\.])\s+", desc)
    chosen = None
    for cand in candidates:
        if "→" in cand or "->" in cand:
            chosen = cand
            break
    if chosen is not None:
        raw_steps = _FLOW_STEP_RE.split(chosen)
        steps: list[tuple[str, str]] = []
        for s in raw_steps:
            s = s.strip().strip(".,;")
            if not s:
                continue
            s = re.sub(r"^.*?:\s*", "", s, count=1)
            m = re.match(r"^([^(]+?)\s*(?:\(([^)]+)\))?\s*$", s)
            if not m:
                continue
            name = m.group(1).strip()
            detail = (m.group(2) or "").strip()
            if 1 <= len(name) <= 60:
                steps.append((name, detail))
        if len(steps) >= 2:
            return steps[:8]

    # Caso 2: enumeración numerada "1) X, 2) Y, 3) Z" en cualquier parte
    num_items = _FLOW_NUM_ITEM_RE.findall(desc)
    if len(num_items) >= 2:
        steps = []
        for num, body in num_items:
            body = body.strip().rstrip(".,;")
            m = re.match(r"^([^(]+?)\s*(?:\(([^)]+)\))?\s*$", body)
            if m:
                name = m.group(1).strip()
                detail = (m.group(2) or "").strip()
                if 1 <= len(name) <= 60:
                    steps.append((name, detail))
        if len(steps) >= 2:
            return steps[:8]

    # Caso 3: introducción "X estaciones/etapas/cajas (A foo, B bar, C baz)"
    intro = _FLOW_ENUM_INTRO_RE.search(desc)
    if intro:
        # Tomar la sustitución desde el inicio del intro hasta el siguiente `.` o `;`
        rest = desc[intro.end():]
        chunk = re.split(r"[\.;]", rest, maxsplit=1)[0]
        # Quitar paréntesis envolventes
        chunk = chunk.strip()
        if chunk.startswith("("):
            close = chunk.find(")")
            if close > 0:
                chunk = chunk[1:close]
        # Items separados por "," donde cada uno arranca con letra mayúscula opcional
        letter_items = _FLOW_LETTER_ITEM_RE.findall(chunk)
        if len(letter_items) >= 2:
            steps = []
            for letter, name in letter_items:
                name = name.strip().rstrip(",;.")
                if 1 <= len(name) <= 60:
                    steps.append((f"{letter}. {name}", ""))
            if len(steps) >= 2:
                return steps[:8]

    return None


def _render_visual_flowchart(desc: str, paginas: float) -> str | None:
    steps = _parse_flowchart(desc)
    if not steps:
        return None
    n = len(steps)
    rows = 1 if n <= 4 else 2
    cols = n if rows == 1 else (n + 1) // 2
    W, H, _ = _frame_dims(max(paginas, 0.7))
    box_w = min(240, (W - 80) / cols - 40)
    box_h = 96
    gap_x = (W - cols * box_w) / (cols + 1)
    gap_y = 110
    parts: list[str] = []
    positions: list[tuple[float, float]] = []
    for i, (name, detail) in enumerate(steps):
        row = i // cols if rows > 1 else 0
        col = (i % cols) if (row % 2 == 0) else (cols - 1 - (i % cols))
        x = gap_x + col * (box_w + gap_x) + box_w / 2
        y = 80 + row * (box_h + gap_y) + box_h / 2
        positions.append((x, y))
        color = _PALETTE[i % len(_PALETTE)]
        parts.append(
            f'<rect x="{x - box_w / 2:.0f}" y="{y - box_h / 2:.0f}" '
            f'width="{box_w:.0f}" height="{box_h}" rx="12" ry="12" '
            f'fill="#FFFFFF" stroke="{color}" stroke-width="2.5"/>'
        )
        parts.append(
            f'<rect x="{x - box_w / 2:.0f}" y="{y - box_h / 2:.0f}" '
            f'width="9" height="{box_h}" fill="{color}"/>'
        )
        name_lines = _wrap_text(name, 22)[:2]
        det_lines = _wrap_text(detail, 30)[:2] if detail else []
        # Si hay detalle, posiciona el nombre más arriba y el detalle abajo
        if det_lines:
            parts.append(_svg_text_lines(x, y - 18, name_lines, font_size=14, fill=color, weight="700"))
            parts.append(_svg_text_lines(x, y + 18, det_lines, font_size=11, fill="#475569"))
        else:
            parts.append(_svg_text_lines(x, y, name_lines, font_size=15, fill=color, weight="700"))
    # Flechas entre pasos consecutivos
    parts.insert(
        0,
        '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#94A3B8"/></marker></defs>',
    )
    for i in range(n - 1):
        x1, y1 = positions[i]
        x2, y2 = positions[i + 1]
        if abs(y1 - y2) < 1:  # misma fila
            sx = x1 + box_w / 2 + 2 if x2 > x1 else x1 - box_w / 2 - 2
            ex = x2 - box_w / 2 - 2 if x2 > x1 else x2 + box_w / 2 + 2
            parts.append(
                f'<line x1="{sx:.0f}" y1="{y1:.0f}" x2="{ex:.0f}" y2="{y2:.0f}" '
                f'stroke="#94A3B8" stroke-width="1.6" marker-end="url(#arr)"/>'
            )
        else:  # cambio de fila
            sy = y1 + box_h / 2 + 2
            ey = y2 - box_h / 2 - 2
            parts.append(
                f'<path d="M {x1:.0f} {sy:.0f} C {x1:.0f} {(sy + ey) / 2:.0f}, '
                f'{x2:.0f} {(sy + ey) / 2:.0f}, {x2:.0f} {ey:.0f}" '
                f'fill="none" stroke="#94A3B8" stroke-width="1.6" marker-end="url(#arr)"/>'
            )
    return (
        f'<svg class="visual-svg visual-svg-flow" viewBox="0 0 {W} {H}" '
        f'preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="Diagrama de flujo">{"".join(parts)}</svg>'
    )


# ---------- Línea de tiempo ----------------------------------------------------

_YEAR_RE = re.compile(
    r"(?:^|[\s\(])((?:19|20)\d{2}(?:\s*[-–]\s*(?:19|20)\d{2})?|18\d{2})\s+"
    r"([A-ZÁÉÍÓÚÜÑ][A-ZÁÉÍÓÚÜÑa-záéíóúüñ\-]+(?:\s+[A-ZÁÉÍÓÚÜÑa-záéíóúüñ\-]+){0,3})"
)
# Forma inversa: "NOMBRE AÑO" (Dalton 1803, Thomson 1897, Schrödinger 1926, etc.)
_YEAR_REVERSE_RE = re.compile(
    r"(?:^|[,;:\.\s])"
    r"([A-ZÁÉÍÓÚÜÑ][A-ZÁÉÍÓÚÜÑa-záéíóúüñ\-]+(?:[\s\-][A-ZÁÉÍÓÚÜÑ][A-ZÁÉÍÓÚÜÑa-záéíóúüñ\-]+){0,2})"
    r"\s+((?:19|20)\d{2}|18\d{2})(?:\s*[-–]\s*(?:19|20)\d{2})?"
)


def _parse_timeline(desc: str) -> list[tuple[str, str]] | None:
    if not desc:
        return None
    items: list[tuple[str, str]] = []
    seen: set[str] = set()
    # Primero "AÑO NOMBRE"
    for m in _YEAR_RE.finditer(desc):
        year = m.group(1).strip()
        name = m.group(2).strip()
        key = f"{year}|{name.lower()}"
        if key not in seen:
            seen.add(key)
            items.append((year, name))
    # Luego "NOMBRE AÑO" (no duplica si ya tenemos ese año)
    if len(items) < 2:
        for m in _YEAR_REVERSE_RE.finditer(desc):
            name = m.group(1).strip()
            year = m.group(2).strip()
            # Evita matches accidentales tipo "valor 2024" o "GDPR 2018" donde NOMBRE es trivial
            if len(name) < 3:
                continue
            # Filtra palabras genéricas que no son nombres propios
            generic = {"con", "del", "los", "las", "una", "uno", "para", "este", "esta", "año"}
            if name.lower() in generic:
                continue
            key = f"{year}|{name.lower()}"
            if key not in seen:
                seen.add(key)
                items.append((year, name))
    if len(items) < 2:
        return None
    # Ordena por año cronológicamente
    def sort_key(it):
        try:
            return int(it[0][:4])
        except Exception:
            return 9999
    items.sort(key=sort_key)
    return items[:8]


def _render_visual_timeline(desc: str, paginas: float) -> str | None:
    items = _parse_timeline(desc)
    if not items:
        return None
    n = len(items)
    W, H, _ = _frame_dims(max(paginas, 0.8))
    margin = 80
    line_y = H * 0.55
    step = (W - 2 * margin) / max(1, n - 1)
    parts: list[str] = []
    parts.append(
        f'<line x1="{margin}" y1="{line_y}" x2="{W - margin}" y2="{line_y}" '
        f'stroke="#94A3B8" stroke-width="3"/>'
    )
    for i, (year, name) in enumerate(items):
        x = margin + i * step
        color = _PALETTE[i % len(_PALETTE)]
        parts.append(
            f'<circle cx="{x:.0f}" cy="{line_y}" r="13" fill="{color}" stroke="#FFFFFF" stroke-width="3"/>'
        )
        above = (i % 2 == 0)
        stick_end = line_y - 60 if above else line_y + 50
        parts.append(
            f'<line x1="{x:.0f}" y1="{line_y + (-13 if above else 13)}" x2="{x:.0f}" '
            f'y2="{stick_end}" stroke="{color}" stroke-width="2"/>'
        )
        ty = line_y - 78 if above else line_y + 78
        parts.append(
            _svg_text_lines(x, ty, [year], font_size=16, fill=color, weight="700")
        )
        name_lines = _wrap_text(name, 18)[:2]
        ny = ty - 24 if above else ty + 24
        parts.append(_svg_text_lines(x, ny, name_lines, font_size=12, fill="#111827", weight="600"))
    return (
        f'<svg class="visual-svg visual-svg-timeline" viewBox="0 0 {W} {H}" '
        f'preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="Línea de tiempo">{"".join(parts)}</svg>'
    )


# ---------- Cuadro comparativo ------------------------------------------------

def _parse_compare(desc: str) -> list[tuple[str, list[str]]] | None:
    if not desc:
        return None
    # Extraer item: "X (a, b, c)" o "X: a, b, c"
    rows: list[tuple[str, list[str]]] = []
    # Quita preámbulo hasta los dos puntos
    body = desc
    if ":" in body:
        body = body.split(":", 1)[1]
    pattern = re.compile(r"([A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 \-\+/\.]*?)\s*\(([^)]+)\)")
    for m in pattern.finditer(body):
        name = m.group(1).strip(" ,;.-")
        attrs = [a.strip() for a in re.split(r"[,;]", m.group(2)) if a.strip()]
        if name and attrs:
            rows.append((name[:50], attrs))
    if len(rows) < 2:
        return None
    return rows[:10]


def _render_visual_compare(desc: str, paginas: float) -> str | None:
    rows = _parse_compare(desc)
    if not rows:
        return None
    max_attrs = max(len(a) for _, a in rows)
    if max_attrs == 0:
        return None
    headers_html = "".join(f"<th>Atributo {i + 1}</th>" for i in range(max_attrs))
    body_rows = []
    for name, attrs in rows:
        cells = [f"<th>{html.escape(name)}</th>"]
        for i in range(max_attrs):
            v = html.escape(attrs[i]) if i < len(attrs) else ""
            cells.append(f"<td>{v}</td>")
        body_rows.append("<tr>" + "".join(cells) + "</tr>")
    return (
        f'<table class="visual-compare">'
        f'<thead><tr><th>Elemento</th>{headers_html}</tr></thead>'
        f'<tbody>{"".join(body_rows)}</tbody>'
        f"</table>"
    )


# ---------- Biblioteca de iconos SVG vectoriales (escenas figurativas) --------
# Cada icono se posiciona con (x, y, s) — centro y escala — y se colorea con
# c (primario) y c2 (secundario / fondo). Diseñados para 100x100 nominal.

ICON_LIB: dict[str, str] = {
    "matraz": (
        '<g transform="translate({x},{y}) scale({s})" stroke-linecap="round" stroke-linejoin="round">'
        '<line x1="0" y1="-32" x2="0" y2="-14" stroke="{c}" stroke-width="3"/>'
        '<ellipse cx="0" cy="-32" rx="6" ry="2" fill="none" stroke="{c}" stroke-width="2"/>'
        '<path d="M -3 -14 L -22 18 A 22 22 0 0 0 22 18 L 3 -14 Z" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<path d="M -16 4 A 17 17 0 0 0 16 4 L 14 12 A 14 14 0 0 1 -14 12 Z" fill="{c}" opacity="0.35"/>'
        '<line x1="-22" y1="-2" x2="-19" y2="-2" stroke="{c}" stroke-width="1.4"/>'
        '<line x1="-22" y1="-7" x2="-19" y2="-7" stroke="{c}" stroke-width="1.4"/>'
        "</g>"
    ),
    "balanza": (
        '<g transform="translate({x},{y}) scale({s})" stroke-linecap="round">'
        '<line x1="0" y1="-26" x2="0" y2="22" stroke="{c}" stroke-width="3"/>'
        '<line x1="-26" y1="-26" x2="26" y2="-26" stroke="{c}" stroke-width="3"/>'
        '<line x1="-26" y1="-26" x2="-26" y2="-16" stroke="{c}" stroke-width="2"/>'
        '<line x1="26" y1="-26" x2="26" y2="-16" stroke="{c}" stroke-width="2"/>'
        '<ellipse cx="-26" cy="-13" rx="14" ry="4" fill="{c2}" stroke="{c}" stroke-width="2"/>'
        '<ellipse cx="26" cy="-13" rx="14" ry="4" fill="{c2}" stroke="{c}" stroke-width="2"/>'
        '<rect x="-12" y="22" width="24" height="6" fill="{c}"/>'
        "</g>"
    ),
    "atomo": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<ellipse cx="0" cy="0" rx="32" ry="12" fill="none" stroke="{c}" stroke-width="2"/>'
        '<ellipse cx="0" cy="0" rx="32" ry="12" fill="none" stroke="{c}" stroke-width="2" transform="rotate(60)"/>'
        '<ellipse cx="0" cy="0" rx="32" ry="12" fill="none" stroke="{c}" stroke-width="2" transform="rotate(-60)"/>'
        '<circle cx="0" cy="0" r="6" fill="{c}"/>'
        '<circle cx="32" cy="0" r="3" fill="{c}"/>'
        '<circle cx="-16" cy="-27" r="3" fill="{c}"/>'
        '<circle cx="-16" cy="27" r="3" fill="{c}"/>'
        "</g>"
    ),
    "molecula": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<line x1="-22" y1="14" x2="0" y2="-14" stroke="{c}" stroke-width="3"/>'
        '<line x1="22" y1="14" x2="0" y2="-14" stroke="{c}" stroke-width="3"/>'
        '<circle cx="0" cy="-14" r="11" fill="{c}"/>'
        '<circle cx="-22" cy="14" r="9" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<circle cx="22" cy="14" r="9" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        "</g>"
    ),
    "gota": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<path d="M 0 -30 C -18 -10 -18 14 0 24 C 18 14 18 -10 0 -30 Z" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<ellipse cx="-5" cy="2" rx="3" ry="6" fill="{c}" opacity="0.35"/>'
        "</g>"
    ),
    "llama": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<path d="M 0 26 C -16 18 -19 -1 -10 -11 C -8 -3 0 -9 -2 -23 C 9 -19 16 -5 13 9 C 19 15 13 22 0 26 Z" fill="{c}" opacity="0.85"/>'
        '<path d="M -2 19 C -8 14 -10 7 -5 -2 C -3 4 2 0 0 -10 C 5 -6 8 4 6 12 C 8 16 4 19 -2 19 Z" fill="{c2}" opacity="0.85"/>'
        "</g>"
    ),
    "termometro": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<rect x="-5" y="-28" width="10" height="42" rx="5" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<circle cx="0" cy="20" r="11" fill="{c}"/>'
        '<rect x="-3" y="0" width="6" height="14" fill="{c}"/>'
        '<line x1="-12" y1="-22" x2="-7" y2="-22" stroke="{c}" stroke-width="1.4"/>'
        '<line x1="-12" y1="-14" x2="-7" y2="-14" stroke="{c}" stroke-width="1.4"/>'
        '<line x1="-12" y1="-6" x2="-7" y2="-6" stroke="{c}" stroke-width="1.4"/>'
        "</g>"
    ),
    "lupa": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<circle cx="-8" cy="-8" r="16" fill="{c2}" stroke="{c}" stroke-width="3"/>'
        '<line x1="3" y1="3" x2="20" y2="20" stroke="{c}" stroke-width="4.5" stroke-linecap="round"/>'
        '<path d="M -16 -10 A 12 12 0 0 1 -8 -18" fill="none" stroke="{c}" stroke-width="1.5" opacity="0.5"/>'
        "</g>"
    ),
    "libro": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<path d="M -24 -20 H 0 V 24 H -24 Q -27 24 -27 20 V -16 Q -27 -20 -24 -20 Z" fill="{c}"/>'
        '<path d="M 24 -20 H 0 V 24 H 24 Q 27 24 27 20 V -16 Q 27 -20 24 -20 Z" fill="{c}"/>'
        '<line x1="-17" y1="-10" x2="-5" y2="-10" stroke="{c2}" stroke-width="1.6"/>'
        '<line x1="-17" y1="-2" x2="-5" y2="-2" stroke="{c2}" stroke-width="1.6"/>'
        '<line x1="5" y1="-10" x2="17" y2="-10" stroke="{c2}" stroke-width="1.6"/>'
        '<line x1="5" y1="-2" x2="17" y2="-2" stroke="{c2}" stroke-width="1.6"/>'
        "</g>"
    ),
    "laptop": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<rect x="-24" y="-20" width="48" height="32" rx="2.5" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<rect x="-20" y="-16" width="40" height="24" fill="{c}" opacity="0.18"/>'
        '<line x1="-28" y1="14" x2="28" y2="14" stroke="{c}" stroke-width="3"/>'
        '<ellipse cx="0" cy="14" rx="9" ry="2.4" fill="{c2}" stroke="{c}" stroke-width="2"/>'
        "</g>"
    ),
    "smartphone": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<rect x="-12" y="-28" width="24" height="52" rx="4" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<rect x="-9" y="-22" width="18" height="36" fill="{c}" opacity="0.16"/>'
        '<circle cx="0" cy="19" r="2" fill="{c}"/>'
        '<line x1="-3" y1="-25" x2="3" y2="-25" stroke="{c}" stroke-width="1.6"/>'
        "</g>"
    ),
    "robot": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<rect x="-18" y="-18" width="36" height="30" rx="6" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<circle cx="-7" cy="-6" r="3" fill="{c}"/>'
        '<circle cx="7" cy="-6" r="3" fill="{c}"/>'
        '<line x1="-7" y1="6" x2="7" y2="6" stroke="{c}" stroke-width="2"/>'
        '<line x1="0" y1="-22" x2="0" y2="-26" stroke="{c}" stroke-width="2"/>'
        '<circle cx="0" cy="-28" r="2.5" fill="{c}"/>'
        '<rect x="-14" y="14" width="28" height="10" rx="2" fill="{c2}" stroke="{c}" stroke-width="2"/>'
        "</g>"
    ),
    "engranaje": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<g fill="{c}">'
        '<rect x="-3" y="-30" width="6" height="9"/>'
        '<rect x="-3" y="21" width="6" height="9"/>'
        '<rect x="-30" y="-3" width="9" height="6"/>'
        '<rect x="21" y="-3" width="9" height="6"/>'
        '<rect x="-3" y="-30" width="6" height="9" transform="rotate(45)"/>'
        '<rect x="-3" y="21" width="6" height="9" transform="rotate(45)"/>'
        '<rect x="-30" y="-3" width="9" height="6" transform="rotate(45)"/>'
        '<rect x="21" y="-3" width="9" height="6" transform="rotate(45)"/>'
        "</g>"
        '<circle cx="0" cy="0" r="20" fill="{c}"/>'
        '<circle cx="0" cy="0" r="9" fill="{c2}"/>'
        "</g>"
    ),
    "persona": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<circle cx="0" cy="-22" r="9" fill="{c}"/>'
        '<path d="M -16 -8 Q -16 -14 -8 -14 H 8 Q 16 -14 16 -8 V 26 H -16 Z" fill="{c}"/>'
        '<path d="M -10 -10 L 0 4 L 10 -10" fill="none" stroke="{c2}" stroke-width="2.2"/>'
        "</g>"
    ),
    "alquimista": (
        '<g transform="translate({x},{y}) scale({s})" opacity="0.55">'
        '<path d="M -18 30 L -20 -8 Q -20 -30 0 -30 Q 20 -30 20 -8 L 18 30 Z" fill="{c}"/>'
        '<ellipse cx="0" cy="-12" rx="7" ry="10" fill="{c2}"/>'
        '<path d="M -16 -22 Q 0 -34 16 -22" fill="none" stroke="{c}" stroke-width="3"/>'
        "</g>"
    ),
    "hoja_papel": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<rect x="-15" y="-22" width="30" height="42" rx="1" fill="{c2}" stroke="{c}" stroke-width="2"/>'
        '<line x1="-10" y1="-12" x2="10" y2="-12" stroke="{c}" stroke-width="1.5"/>'
        '<line x1="-10" y1="-4" x2="10" y2="-4" stroke="{c}" stroke-width="1.5"/>'
        '<line x1="-10" y1="4" x2="10" y2="4" stroke="{c}" stroke-width="1.5"/>'
        '<line x1="-10" y1="12" x2="6" y2="12" stroke="{c}" stroke-width="1.5"/>'
        "</g>"
    ),
    "chip": (
        '<g transform="translate({x},{y}) scale({s})" stroke-linecap="round">'
        '<rect x="-15" y="-15" width="30" height="30" rx="2" fill="{c}"/>'
        '<rect x="-10" y="-10" width="20" height="20" rx="1.5" fill="{c2}"/>'
        '<g stroke="{c}" stroke-width="2">'
        '<line x1="-21" y1="-8" x2="-15" y2="-8"/>'
        '<line x1="-21" y1="0" x2="-15" y2="0"/>'
        '<line x1="-21" y1="8" x2="-15" y2="8"/>'
        '<line x1="21" y1="-8" x2="15" y2="-8"/>'
        '<line x1="21" y1="0" x2="15" y2="0"/>'
        '<line x1="21" y1="8" x2="15" y2="8"/>'
        '<line x1="-8" y1="-21" x2="-8" y2="-15"/>'
        '<line x1="0" y1="-21" x2="0" y2="-15"/>'
        '<line x1="8" y1="-21" x2="8" y2="-15"/>'
        '<line x1="-8" y1="21" x2="-8" y2="15"/>'
        '<line x1="0" y1="21" x2="0" y2="15"/>'
        '<line x1="8" y1="21" x2="8" y2="15"/>'
        "</g>"
        "</g>"
    ),
    "globo": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<circle cx="0" cy="0" r="24" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<ellipse cx="0" cy="0" rx="24" ry="11" fill="none" stroke="{c}" stroke-width="1.6"/>'
        '<line x1="0" y1="-24" x2="0" y2="24" stroke="{c}" stroke-width="1.6"/>'
        '<ellipse cx="0" cy="0" rx="11" ry="24" fill="none" stroke="{c}" stroke-width="1.6"/>'
        "</g>"
    ),
    "reloj": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<circle cx="0" cy="0" r="24" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<line x1="0" y1="0" x2="0" y2="-16" stroke="{c}" stroke-width="3"/>'
        '<line x1="0" y1="0" x2="11" y2="6" stroke="{c}" stroke-width="2.2"/>'
        '<circle cx="0" cy="0" r="2.5" fill="{c}"/>'
        "</g>"
    ),
    "ecuacion": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<text x="0" y="14" text-anchor="middle" font-family="Cambria Math, Times New Roman, serif" font-size="48" font-style="italic" font-weight="700" fill="{c}">f(x)</text>'
        "</g>"
    ),
    "burbuja_chat": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<path d="M -24 -20 Q -24 -26 -18 -26 H 18 Q 24 -26 24 -20 V 6 Q 24 12 18 12 H -2 L -10 22 L -8 12 H -18 Q -24 12 -24 6 Z" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<circle cx="-9" cy="-7" r="2.5" fill="{c}"/>'
        '<circle cx="0" cy="-7" r="2.5" fill="{c}"/>'
        '<circle cx="9" cy="-7" r="2.5" fill="{c}"/>'
        "</g>"
    ),
    "microscopio": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<path d="M -10 22 H 10 L 14 28 H -14 Z" fill="{c}"/>'
        '<rect x="-3" y="-2" width="6" height="22" fill="{c}"/>'
        '<rect x="-12" y="-10" width="24" height="8" rx="2" fill="{c}"/>'
        '<circle cx="0" cy="-22" r="9" fill="{c2}" stroke="{c}" stroke-width="3"/>'
        '<line x1="0" y1="-15" x2="0" y2="-10" stroke="{c}" stroke-width="3"/>'
        "</g>"
    ),
    "edificio": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<rect x="-18" y="-22" width="36" height="44" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<g fill="{c}" opacity="0.7">'
        '<rect x="-13" y="-17" width="6" height="6"/>'
        '<rect x="-3" y="-17" width="6" height="6"/>'
        '<rect x="7" y="-17" width="6" height="6"/>'
        '<rect x="-13" y="-7" width="6" height="6"/>'
        '<rect x="-3" y="-7" width="6" height="6"/>'
        '<rect x="7" y="-7" width="6" height="6"/>'
        '<rect x="-13" y="3" width="6" height="6"/>'
        '<rect x="7" y="3" width="6" height="6"/>'
        "</g>"
        '<rect x="-5" y="10" width="10" height="12" fill="{c}"/>'
        "</g>"
    ),
    "hoja_natural": (
        '<g transform="translate({x},{y}) scale({s})">'
        '<path d="M 0 -28 C 22 -22 22 14 0 26 C -22 14 -22 -22 0 -28 Z" fill="{c2}" stroke="{c}" stroke-width="2.5"/>'
        '<line x1="0" y1="-22" x2="0" y2="22" stroke="{c}" stroke-width="2"/>'
        '<path d="M 0 -10 Q 10 -8 14 0" fill="none" stroke="{c}" stroke-width="1.4"/>'
        '<path d="M 0 -10 Q -10 -8 -14 0" fill="none" stroke="{c}" stroke-width="1.4"/>'
        '<path d="M 0 6 Q 10 8 12 14" fill="none" stroke="{c}" stroke-width="1.4"/>'
        '<path d="M 0 6 Q -10 8 -12 14" fill="none" stroke="{c}" stroke-width="1.4"/>'
        "</g>"
    ),
}

# Conector entre 2 iconos: flecha curva en color acento
ICON_CONNECTOR = (
    '<defs><marker id="arr-{uid}" viewBox="0 0 10 10" refX="9" refY="5" '
    'markerWidth="7" markerHeight="7" orient="auto">'
    '<path d="M 0 0 L 10 5 L 0 10 z" fill="#F39C12"/></marker></defs>'
    '<path d="M {x1:.0f} {y1:.0f} Q {mx:.0f} {my:.0f} {x2:.0f} {y2:.0f}" '
    'fill="none" stroke="#F39C12" stroke-width="3" stroke-linecap="round" '
    'marker-end="url(#arr-{uid})"/>'
)


# Mapeo keyword (normalizado sin acentos, lowercase) → icono
ICON_KEYWORDS: dict[str, list[str]] = {
    "matraz": ["matraz", "frasco", "vaso de precipitad", "erlenmeyer", "balon", "recipiente quimic"],
    "balanza": ["balanza", "bascula", "pesar", "peso", "masa de"],
    "atomo": ["atomo", "atomic", "electron", "nucleo", "proton", "neutron", "isotopo", "configuracion electron"],
    "molecula": ["molecula", "molecul", "compuesto quimic", "enlace", "h2o", "co2"],
    "gota": ["gota", "agua", "liquido", "solucion", "disolucion", "hidrico"],
    "llama": ["llama", "fuego", "combustion", "calor", "ardor", "combustib"],
    "termometro": ["termometro", "temperatura", "kelvin", "celsius", "frio", "calor corp"],
    "lupa": ["lupa", "investigacion", "busqueda", "analisis", "examen", "auditoria", "inspeccion"],
    "libro": ["libro", "manual", "texto", "lectura", "biblioteca", "capitulo"],
    "laptop": ["laptop", "computadora", "ordenador", "codigo", "programacion", "software", "ide", "editor"],
    "smartphone": ["smartphone", "celular", "movil", "app", "aplicacion movil", "telefono"],
    "robot": ["robot", "androide"],
    "engranaje": ["engranaje", "mecanismo", "proceso", "sistema", "pipeline", "etapa", "flujo"],
    "persona": ["estudiante", "profesor", "alumno", "joven", "persona", "usuari", "quimic moder", "cientific"],
    "alquimista": ["alquimist", "historic", "antigu", "siglo xv", "siglo xvi", "siglo xvii", "siglo xviii", "medieval"],
    "hoja_papel": ["documento", "reporte", "informe", "papel", "hoja de", "ficha", "memorandum"],
    "chip": ["chip", "circuito", "transistor", "microchip", "hardware", "semiconductor"],
    "globo": ["mundo", "global", "planeta", "tierra", "internacional", "mapa mund"],
    "reloj": ["reloj", "tiempo", "hora", "minuto", "cronometro", "temporal"],
    "ecuacion": ["formula", "ecuacion", "matematic", "algebra", "calculo de"],
    "burbuja_chat": ["chat", "prompt", "dialogo", "conversacion", "chatbot", "llm", "claude", "chatgpt", "gpt", "gemini"],
    "microscopio": ["microscopio", "celula", "microorganism", "bacteria"],
    "edificio": ["edificio", "fabrica", "escuela", "planta de", "instalacion", "empresa"],
    "hoja_natural": ["hoja", "planta", "naturaleza", "ecosistema", "vegetal", "biolog"],
    "ia": ["ia ", "inteligencia artificial", "modelo de lenguaje", "machine learning", "aprendizaje automatico", "red neuronal"],
}

# Algunas keywords mapean a iconos compuestos (resueltos por _detect_icons)
ICON_ALIAS = {"ia": "robot"}


def _detect_icons(desc: str, max_n: int = 3) -> list[str]:
    if not desc:
        return []
    norm = _strip_accents(desc.lower())
    found: list[tuple[str, int]] = []
    for icon_id, kws in ICON_KEYWORDS.items():
        for kw in kws:
            kw_norm = _strip_accents(kw.lower())
            pos = norm.find(kw_norm)
            if pos >= 0:
                resolved = ICON_ALIAS.get(icon_id, icon_id)
                if resolved not in [i for i, _ in found]:
                    found.append((resolved, pos))
                break
    found.sort(key=lambda t: t[1])
    return [i for i, _ in found][:max_n]


def _render_icon_scene(desc: str, paginas: float, tipo: str) -> str | None:
    icons = _detect_icons(desc, max_n=3)
    if not icons:
        return None
    W, H, _ = _frame_dims(max(paginas, 0.7))
    # Layout adaptativo con escalas más generosas para impresión
    if len(icons) == 1:
        positions = [(W / 2, H * 0.40)]
        scale = 3.0
    elif len(icons) == 2:
        positions = [(W * 0.28, H * 0.42), (W * 0.72, H * 0.42)]
        scale = 2.4
    else:
        positions = [(W * 0.20, H * 0.46), (W * 0.50, H * 0.30), (W * 0.80, H * 0.46)]
        scale = 2.0
    parts: list[str] = []
    uid = abs(hash((desc, tipo, paginas))) & 0xFFFFFF
    parts.append(
        f'<defs><linearGradient id="bg-{uid}" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="#EFF6FF"/><stop offset="1" stop-color="#FFF7ED"/>'
        f"</linearGradient></defs>"
        f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bg-{uid})" rx="10"/>'
    )
    if len(icons) == 2:
        x1, y1 = positions[0]
        x2, y2 = positions[1]
        x1 += 60
        x2 -= 60
        mx = (x1 + x2) / 2
        my = min(y1, y2) - 80
        parts.append(
            ICON_CONNECTOR.format(uid=uid, x1=x1, y1=y1, x2=x2, y2=y2, mx=mx, my=my)
        )
    accent = "#F39C12"
    primary = "#0E3A8A"
    for i, ((x, y), icon_id) in enumerate(zip(positions, icons)):
        tpl = ICON_LIB.get(icon_id)
        if not tpl:
            continue
        c = accent if (len(icons) > 1 and i == len(icons) - 1) else primary
        c2 = "#FFFFFF"
        parts.append(tpl.format(x=x, y=y, s=scale, c=c, c2=c2))
    first = re.split(r"(?<=[\.\!\?])\s+", desc, maxsplit=1)[0] if desc else ""
    first = _STOP_PREFIX_RE.sub("", first).strip()
    short = first[:200]
    if short:
        lines = _wrap_text(short, 70)[:3]
        # Caja blanca con sombra sutil para la frase
        n_lines = len(lines)
        box_h = 18 + n_lines * 24
        box_y = H - box_h - 16
        parts.append(
            f'<rect x="40" y="{box_y}" width="{W - 80}" height="{box_h}" rx="8" '
            f'fill="#FFFFFF" stroke="#0E3A8A" stroke-width="1.5" opacity="0.95"/>'
        )
        ty = box_y + box_h / 2
        parts.append(_svg_text_lines(W / 2, ty, lines, font_size=17, fill="#0E3A8A", weight="600"))
    return (
        f'<svg class="visual-svg visual-svg-scene" viewBox="0 0 {W} {H}" '
        f'preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="Composición simbólica">{"".join(parts)}</svg>'
    )


# ---------- Genérico estructurado (sin briefing crudo) -------------------------

# Limita el prefijo a máximo 60 caracteres antes de `:` o `,`. Sin esta cota,
# si la oración entera empieza con "Diagrama..." y el único `.` está al final,
# el regex consumiría TODA la oración y dejaría la frase pie vacía.
_STOP_PREFIX_RE = re.compile(
    r"^\s*(?:Ilustración|Infografía|Diagrama|Cuadro|Captura|Línea|Tabla|Mapa|Gráfica|Esquema|Composición)"
    r"[^:,]{0,60}[:,]\s*",
    re.IGNORECASE,
)


def _render_visual_generic(desc: str, paginas: float, tipo_label: str) -> str:
    """Caja semánticamente estructurada: breve título + lista de elementos clave."""
    if not desc:
        return (
            f'<div class="visual-stub-empty"><p>Espacio para {html.escape(tipo_label.lower())}.</p></div>'
        )
    # Quita el prefijo descriptivo ("Ilustración: ...", "Infografía con ...")
    text = _STOP_PREFIX_RE.sub("", desc).strip()
    parts = _split_clauses(text)
    # Subdivide por comas internas si quedan claves muy largas
    items: list[str] = []
    for p in parts:
        if len(p) > 110 and "," in p:
            for sub in re.split(r"\s*,\s*", p):
                if sub:
                    items.append(sub.strip())
        else:
            items.append(p)
    items = [i for i in items if 3 <= len(i) <= 240][:8]
    if not items:
        return (
            f'<div class="visual-stub-empty"><p>Espacio para {html.escape(tipo_label.lower())}.</p></div>'
        )
    chips = "".join(
        f'<li><span class="chip-num">{i + 1}</span><span class="chip-text">{html.escape(it)}</span></li>'
        for i, it in enumerate(items)
    )
    return (
        f'<div class="visual-structured">'
        f'<p class="visual-structured-lead">Elementos clave del {html.escape(tipo_label.lower())}:</p>'
        f'<ol class="visual-chips">{chips}</ol>'
        f"</div>"
    )


# ---------- Dispatch principal -------------------------------------------------

def render_visual(attrs: dict, mode: str = "print") -> str:
    tipo = attrs.get("tipo", "ilustracion")
    desc = attrs.get("descripcion", "")
    nota = attrs.get("nota", "")
    paginas = float(attrs.get("paginas", "0.5"))
    src = attrs.get("src") or attrs.get("asset")
    visual_id = attrs.get("_id")  # asignado por build_manual

    # Auto-inyección: si no hay src explícito y existe imagen con el ID en
    # assets/visuales/manual-N/uXX/, usar esa ruta.
    if not src and visual_id:
        manual_n = attrs.get("_manual_n")
        unidad = attrs.get("_unidad")
        if manual_n and unidad:
            base = Path(__file__).resolve().parent.parent / "assets" / "visuales" / f"manual-{manual_n}" / unidad
            for ext in (".jpg", ".jpeg", ".png", ".webp", ".svg"):
                cand = base / f"{visual_id}{ext}"
                if cand.exists():
                    # ruta relativa al HTML de salida (dist/) — usamos absoluta file:// segura
                    src = cand.resolve().as_uri()
                    break

    safe_tipo_attr = html.escape(tipo, quote=True)
    safe_tipo_label = html.escape(tipo.replace("-", " ").title())
    nota_html = f'<p class="visual-nota">Nota: {html.escape(nota)}</p>' if nota else ""
    id_attr = f' id="{html.escape(visual_id, quote=True)}"' if visual_id else ""

    if src:
        safe_src = html.escape(src, quote=True)
        safe_desc_attr = html.escape(desc, quote=True)
        clean_visual = attrs.get("sin_marco") in {"1", "true", "si", "yes"}
        if clean_visual:
            height = "15.0cm" if paginas >= 1 else ("7.0cm" if paginas >= 0.5 else "6.0cm")
            return (
                f'<figure class="visual-placeholder visual-asset visual-clean" data-tipo="{safe_tipo_attr}" data-pages="{paginas}"{id_attr}>'
                f'<div class="visual-frame" style="height: {height};">'
                f'<img src="{safe_src}" alt="{safe_desc_attr}" class="visual-img" />'
                f"</div></figure>"
            )
        first_sentence = re.split(r"(?<=[\.;])\s+", desc, maxsplit=1)[0] if desc else ""
        caption = html.escape(first_sentence[:120])
        height = "15.0cm" if paginas >= 1 else "7.0cm"
        return (
            f'<figure class="visual-placeholder visual-asset" data-tipo="{safe_tipo_attr}" data-pages="{paginas}"{id_attr}>'
            f'<div class="visual-frame" style="height: {height};">'
            f'<span class="visual-tag">Visual - {safe_tipo_label}</span>'
            f'<img src="{safe_src}" alt="{safe_desc_attr}" class="visual-img" />'
            f'<p class="visual-desc">{caption}</p>{nota_html}'
            f"</div></figure>"
        )

    # Generadores específicos por tipo
    rendered: str | None = None
    if tipo == "mapa-mental":
        rendered = _render_visual_mindmap(desc, paginas)
    elif tipo == "diagrama-flujo":
        rendered = _render_visual_flowchart(desc, paginas)
    elif tipo == "linea-tiempo":
        rendered = _render_visual_timeline(desc, paginas)
    elif tipo in ("cuadro-comparativo", "tabla-grande"):
        rendered = _render_visual_compare(desc, paginas)

    # Para tipos figurativos (ilustracion, infografia, interfaz, grafica) y como
    # último recurso para los demás: composición simbólica con iconos vectoriales.
    if rendered is None and tipo in ("ilustracion", "infografia", "interfaz", "grafica"):
        rendered = _render_icon_scene(desc, paginas, tipo)

    if rendered is None:
        # Último intento: escena de iconos en cualquier tipo
        rendered = _render_icon_scene(desc, paginas, tipo)

    if rendered is None:
        rendered = _render_visual_generic(desc, paginas, tipo.replace("-", " "))

    _, _, css_h = _frame_dims(paginas)
    desc_comment = f"<!-- briefing: {html.escape(desc[:300])} -->" if desc else ""
    return (
        f'<figure class="visual-placeholder visual-generated" data-tipo="{safe_tipo_attr}" data-pages="{paginas}"{id_attr}>'
        f"{desc_comment}"
        f'<div class="visual-frame visual-frame-generated" style="min-height: {css_h};">'
        f'<span class="visual-tag">{safe_tipo_label}</span>'
        f'<div class="visual-render">{rendered}</div>'
        f"{nota_html}"
        f"</div></figure>"
    )


def process_md(text: str, mode: str = "print", visual_ctx: dict | None = None) -> str:
    """Sustituye bloques ::tipo::, expande {{ico:NAME}} y ejecuta markdown.

    `visual_ctx`, si se entrega, debe ser {'manual_n': int, 'unidad': str,
    'counter': [int]} — counter se incrementa por cada ::visual{} encontrado
    para asignar IDs estables M{n}-uXX-NN.
    """
    placeholders: list[str] = []

    def sub(m):
        tag = m.group("tag")
        attrs = parse_attrs(m.group("attrs"))
        body = m.group("body")
        html = render_block(tag, attrs, body, mode=mode)
        placeholders.append(html)
        return f"\n\n%%MDBLOCK{len(placeholders) - 1}%%\n\n"

    rest = BLOCK_RE.sub(sub, text)

    # Tags self-closing (visual)
    def sub_self(m):
        tag = m.group("tag")
        attrs = parse_attrs(m.group("attrs"))
        if visual_ctx is not None:
            visual_ctx["counter"][0] += 1
            n = visual_ctx["counter"][0]
            attrs["_id"] = f"M{visual_ctx['manual_n']}-{visual_ctx['unidad']}-{n:02d}"
            attrs["_manual_n"] = visual_ctx["manual_n"]
            attrs["_unidad"] = visual_ctx["unidad"]
        html = render_block(tag, attrs, "", mode=mode)
        placeholders.append(html)
        return f"\n\n%%MDBLOCK{len(placeholders) - 1}%%\n\n"

    rest = SELF_CLOSING_RE.sub(sub_self, rest)

    # Normaliza también el texto fuera de bloques: tablas/listas pegadas a un
    # párrafo aparecen como "código suelto" en el PDF.
    rest = _normalize_block_body(rest)

    # Expandir {{ico:NAME}} antes de markdown (resultado HTML inline)
    rest = ico.expand_inline(rest, mode=mode)
    rest, math_ph = _protect_math(rest)
    html = markdown.markdown(
        rest,
        extensions=_MD_EXT + ["toc"],
        extension_configs=_MD_EXT_CFG,
    )
    html = _restore_math(html, math_ph)
    for i, ph in enumerate(placeholders):
        html = html.replace(f"<p>%%MDBLOCK{i}%%</p>", ph)
        html = html.replace(f"%%MDBLOCK{i}%%", ph)
    return html


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            fm_text = text[3:end].strip()
            body = text[end + 4 :].lstrip()
            try:
                fm = yaml.safe_load(fm_text) or {}
            except Exception:
                fm = {}
            return fm, body
    return {}, text


def collect_files(src_dir: Path, semester: int | None = None) -> list[Path]:
    """Recolecta los .md del manual en orden de aparición.

    Si `semester` se entrega:
      1. Front matter del semestre: manuales/manual-N/semestre-X/00..89 (orden)
      2. Unidades del semestre (filtrado por SEMESTER_MAP, hecho fuera)
      3. Cierre del semestre: manuales/manual-N/semestre-X/90..99
    Si no:
      1. .md en raíz del manual (excluye manifest.md)
      2. Todas las unidades en orden alfabético
    """
    files: list[Path] = []

    if semester:
        sem_dir = src_dir / f"semestre-{semester}"
        if sem_dir.exists():
            # archivos 00-89 antes de las unidades
            for f in sorted(sem_dir.glob("*.md")):
                if f.name.startswith(("90-", "91-", "92-", "93-", "94-", "95-",
                                       "96-", "97-", "98-", "99-")):
                    continue
                if f.name == "README.md":
                    continue
                files.append(f)
    else:
        for f in sorted(src_dir.glob("*.md")):
            if f.name == "manifest.md":
                continue
            files.append(f)

    unidades = src_dir / "unidades"
    if unidades.exists():
        for u_dir in sorted(unidades.glob("u*")):
            for f in sorted(u_dir.glob("*.md")):
                files.append(f)

    if semester:
        sem_dir = src_dir / f"semestre-{semester}"
        if sem_dir.exists():
            # archivos 90-99 después de las unidades
            for f in sorted(sem_dir.glob("*.md")):
                if not f.name.startswith(("90-", "91-", "92-", "93-", "94-", "95-",
                                           "96-", "97-", "98-", "99-")):
                    continue
                files.append(f)

    return files


_PRINT_SYMBOL_TRANSLATION = str.maketrans(
    {
        "\u2610": "[ ]",
        "\u2611": "[x]",
        "\u2612": "[x]",
        "\u2705": "Si",
        "\u2713": "Si",
        "\u2714": "Si",
        "\u274c": "No",
        "\u2717": "No",
        "\u2718": "No",
        "\ufe0f": "",
        "\u00b7": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2192": "->",
        "\u2190": "<-",
        "\u2194": "<->",
    }
)


def sanitize_print_symbols(text: str) -> str:
    """Remove emoji/dingbat glyphs that can print as corrupt symbols in PDF."""
    text = text.translate(_PRINT_SYMBOL_TRANSLATION)
    cleaned: list[str] = []
    for ch in text:
        cp = ord(ch)
        if 0x1F000 <= cp <= 0x1FAFF:
            continue
        if 0x2600 <= cp <= 0x27BF:
            continue
        if 0xFE00 <= cp <= 0xFE0F:
            continue
        cleaned.append(ch)
    return "".join(cleaned)


SEMESTER_MAP = {
    1: {1: ["u00", "u01", "u02", "u03"],            2: ["u04", "u05", "u06"]},
    2: {1: ["u01", "u02", "u03", "u04", "u05"],      2: ["u06", "u07", "u08", "u09"]},
    3: {1: ["u01", "u02", "u03", "u04", "u05"],      2: ["u06", "u07", "u08", "u09"]},
    4: {1: ["u01", "u02", "u03", "u04", "u05"],      2: ["u06", "u07", "u08", "u09", "u10"]},
    5: {1: ["u01", "u02", "u03", "u04"],            2: ["u05", "u06", "u07", "u08"]},
}


def _unidad_de(path: Path) -> str:
    """Devuelve 'uXX' si vive en unidades/uXX/, 'sem1'/'sem2' si vive en semestre-N/,
    o 'intro' para archivos en raíz del manual."""
    parent = path.parent.name
    if parent.startswith("u") and parent[1:].isdigit():
        return parent
    if parent.startswith("semestre-"):
        return f"sem{parent.split('-')[-1]}"
    return "intro"


def build_manual(
    src_dir: str,
    out_html: str,
    mode: str = "print",
    semester: int | None = None,
    units: list[str] | None = None,
) -> None:
    src = Path(src_dir)
    manifest = {}
    mfp = src / "manifest.md"
    if mfp.exists():
        manifest, _ = parse_frontmatter(mfp.read_text(encoding="utf-8"))

    manual_n = int(manifest.get("manual", 0) or 0)

    # Resolución de --semester a lista de unidades
    if semester and not units:
        units = SEMESTER_MAP.get(manual_n, {}).get(semester)
        if not units:
            print(f"⚠ Sin mapa de semestre {semester} para manual {manual_n}", file=sys.stderr)
            sys.exit(2)

    files = collect_files(src, semester=semester)

    # Filtro por unidades (mantiene archivos de front matter del semestre y raíz)
    if units:
        units_set = set(units)
        keep = units_set | {"intro", f"sem{semester}" if semester else "sem1", f"sem{semester}" if semester else "sem2"}
        files = [f for f in files if _unidad_de(f) in keep]

    if not files:
        print(f"⚠ No se encontraron .md (excluyendo manifest) en {src}")

    sections: list[str] = []
    # Contadores por unidad para IDs estables M{n}-uXX-NN
    counters: dict[str, list[int]] = {}
    for f in files:
        unidad = _unidad_de(f)
        text = f.read_text(encoding="utf-8")
        _, body = parse_frontmatter(text)
        counter = counters.setdefault(unidad, [0])
        ctx = {"manual_n": manual_n, "unidad": unidad, "counter": counter} if manual_n else None
        sem_attr = ""
        if semester:
            sem_attr = f' data-semestre="{semester}"'
        sections.append(
            f'<section class="md-file" data-file="{f.name}" data-unidad="{unidad}"{sem_attr}>\n'
            f"{process_md(body, mode=mode, visual_ctx=ctx)}\n</section>"
        )

    body_html = "\n\n".join(sections)

    here = Path(__file__).parent
    base_css = (here / "print-letter.css").read_text(encoding="utf-8")
    css = base_css
    if mode == "digital":
        css += "\n\n" + (here / "digital.css").read_text(encoding="utf-8")
    template = Template((here / "template.html").read_text(encoding="utf-8"))

    out = Path(out_html)
    out.parent.mkdir(parents=True, exist_ok=True)
    titulo = manifest.get("titulo", "Manual Albatros")
    if semester:
        titulo = f"{titulo} — Semestre {semester}"
    rendered = template.render(
        titulo=titulo,
        subtitulo=manifest.get("subtitulo", ""),
        mode=mode,
        layout=manifest.get("layout", ""),
        css=css,
        body=body_html,
    )
    out.write_text(sanitize_print_symbols(rendered), encoding="utf-8")
    print(
        f"OK construido: {out}  (modo: {mode}, archivos: {len(files)}"
        + (f", semestre: {semester}" if semester else "")
        + ")"
    )


def main():
    p = argparse.ArgumentParser(description="Manual Albatros — MD → HTML")
    p.add_argument("src", help="Carpeta del manual (manuales/manual-N)")
    p.add_argument("out", help="HTML de salida (dist/manual-N.html)")
    p.add_argument("--mode", default="print", choices=["print", "digital"])
    p.add_argument("--semester", type=int, choices=[1, 2], default=None,
                   help="filtra unidades por semestre según SEMESTER_MAP")
    p.add_argument("--units", default=None,
                   help="lista de unidades a incluir, separadas por coma (u01,u02,...)")
    a = p.parse_args()
    units = [u.strip() for u in a.units.split(",")] if a.units else None
    build_manual(a.src, a.out, a.mode, semester=a.semester, units=units)


if __name__ == "__main__":
    main()
