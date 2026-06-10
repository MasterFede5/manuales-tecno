"""Resolver de íconos — usado por converter.py y por el CLI iconos.py.

Permite resolver íconos por:
  - clave del registro: bloque-concepto, act-mcq, tipo-albatros-experimento
  - alias: foco, lupa, brujula, lampara
  - id de archivo: ico-bloque-concepto
"""
from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Optional

_REGISTRY: Optional[dict] = None
_REG_PATH = Path(__file__).parent.parent / "assets" / "iconos" / "registry.json"

INLINE_RE = re.compile(r"\{\{ico:([\w/-]+)\}\}")


def load_registry(force: bool = False) -> dict:
    global _REGISTRY
    if _REGISTRY is None or force:
        if not _REG_PATH.exists():
            _REGISTRY = {"icons": {}, "total": 0}
        else:
            _REGISTRY = json.loads(_REG_PATH.read_text(encoding="utf-8"))
    return _REGISTRY


def resolve(query: str) -> Optional[dict]:
    """Devuelve el dict del ícono o None. Acepta clave, alias o id."""
    if not query:
        return None
    reg = load_registry()
    icons = reg.get("icons", {})

    # Match directo por clave
    if query in icons:
        return icons[query]

    # Match por id de archivo (ico-X o logo-X)
    for k, v in icons.items():
        if v.get("id") == query:
            return v

    # Match por alias
    for k, v in icons.items():
        aliases = v.get("alias", [])
        if query in aliases:
            return v

    # Match suave: probar variantes comunes
    candidates = [
        f"bloque-{query}",
        f"act-{query}",
        f"fuente-{query}",
        f"tipo-albatros-{query}",
        f"tipo-tecno-{query}",
        f"visual-{query}",
        f"flujo-{query}",
        f"decor-{query}",
        f"manual-{query}",
        f"logo-{query}",
    ]
    for c in candidates:
        if c in icons:
            return icons[c]
    return None


def for_block(block_tag: str) -> Optional[dict]:
    return resolve(f"bloque-{block_tag}") or resolve(block_tag)


def for_activity(act_tag: str) -> Optional[dict]:
    raw = act_tag.replace("act-", "", 1)
    return resolve(f"act-{raw}") or resolve(raw)


def for_albatros_subtipo(subtipo: str) -> Optional[dict]:
    return resolve(f"tipo-albatros-{subtipo}")


def for_tecno_subtipo(subtipo: str) -> Optional[dict]:
    return resolve(f"tipo-tecno-{subtipo}")


def for_fuente(medio: str) -> Optional[dict]:
    return resolve(f"fuente-{medio}")


def for_visual(tipo: str) -> Optional[dict]:
    return resolve(f"visual-{tipo}")


def render_html(icon: Optional[dict], size: int = 24, mode: str = "print",
                fallback_emoji: str = "") -> str:
    """Devuelve <img>; si el archivo no existe, omite el fallback visual."""
    if not icon:
        return ""
    if icon.get("estado") != "listo":
        return (f'<span class="icon-fallback" data-id="{icon["id"]}" '
                f'title="{icon["concepto"]}"></span>')
    # Preferir PNG (provisto por diseñador) sobre SVG si está disponible
    src = icon.get("png") or (icon["svg_mono"] if mode == "print" else icon["svg"])
    return (f'<img src="../assets/iconos/{src}" alt="{icon["concepto"]}" '
            f'width="{size}" height="{size}" class="icon" data-id="{icon["id"]}">')


def render_inline(query: str, size: int = 18, mode: str = "print") -> str:
    """Para sustituir {{ico:NAME}} en MD."""
    icon = resolve(query)
    if not icon:
        return f'<span class="icon-missing" title="ícono no resuelto: {query}">[?{query}]</span>'
    return render_html(icon, size=size, mode=mode)


def expand_inline(text: str, mode: str = "print") -> str:
    """Reemplaza todas las apariciones {{ico:NAME}} en un texto."""
    return INLINE_RE.sub(lambda m: render_inline(m.group(1), mode=mode), text)
