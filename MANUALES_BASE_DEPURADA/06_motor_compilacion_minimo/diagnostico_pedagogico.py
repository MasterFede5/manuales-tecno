"""
Diagnostica cobertura pedagógica por unidad y por manual.

Reporta:
  - Tipos de actividad del catálogo §6 presentes en cada unidad
  - Presencia de bloques semánticos obligatorios (concepto, interioriza, pausa,
    practica, caso, albatros, investiga, fuentes, implementacion)
  - Aproximación de % práctico real (bytes de bloques prácticos / bytes totales)
  - Visuales por tipo
  - Pausas para pensar (mini-actividades) por unidad
  - Faltantes vs checklist de manual-spec §10

Salida: docs/diagnostico-pedagogico.json + docs/diagnostico-pedagogico.md
"""
from __future__ import annotations
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)

CATALOGO_ACT = [
    "act-fill", "act-table", "act-calc", "act-mcq", "act-match",
    "act-puzzle", "act-mindmap", "act-label", "act-case",
    "act-challenge", "act-tf", "act-order",
]

BLOQUES_TEORICOS = ["concepto", "interioriza"]
BLOQUES_PRACTICOS = [
    "practica",       # práctica resuelta
    "albatros",       # actividades Albatros (mediano alcance)
    "investiga",      # apartado de investigación
    "implementacion", # proyecto integrador
    "pausa",          # mini-actividad detonadora
] + CATALOGO_ACT
BLOQUES_OBLIGATORIOS = [
    "concepto", "interioriza", "pausa", "practica", "caso",
    "albatros", "investiga", "fuentes", "implementacion",
]

# Cada manual y sus unidades esperadas
MANUAL_UNIDADES = {
    1: ["u00","u01","u02","u03","u04","u05","u06"],
    2: ["u01","u02","u03","u04","u05","u06","u07","u08","u09"],
    3: ["u01","u02","u03","u04","u05","u06","u07","u08","u09"],
    4: ["u01","u02","u03","u04","u05","u06","u07","u08","u09","u10"],
    5: ["u01","u02","u03","u04","u05","u06","u07","u08"],
}

# Misma división semestres
SEMESTER_MAP = {
    1: {1: ["u00","u01","u02","u03"], 2: ["u04","u05","u06"]},
    2: {1: ["u01","u02","u03","u04","u05"], 2: ["u06","u07","u08","u09"]},
    3: {1: ["u01","u02","u03","u04","u05"], 2: ["u06","u07","u08","u09"]},
    4: {1: ["u01","u02","u03","u04","u05"], 2: ["u06","u07","u08","u09","u10"]},
    5: {1: ["u01","u02","u03","u04"], 2: ["u05","u06","u07","u08"]},
}

OPEN_RE = re.compile(r"^::(?P<tag>[\w-]+)(?:\{[^}]*\})?(?:::)?\s*$", re.MULTILINE)
BLOCK_PAIR_RE = re.compile(
    r"^::(?P<tag>[\w-]+)(?:\{[^}]*\})?(?:::)?\s*\n(?P<body>.*?)\n^::/(?P=tag)(?:::)?\s*$",
    re.DOTALL | re.MULTILINE,
)
VISUAL_RE = re.compile(r'::visual\{[^}]*tipo="(?P<tipo>[^"]+)"[^}]*\}')


def semestre_de(manual: int, unidad: str) -> int | None:
    for s, units in SEMESTER_MAP.get(manual, {}).items():
        if unidad in units:
            return s
    return None


def diag_unidad(unit_dir: Path, manual_n: int) -> dict:
    unidad = unit_dir.name
    archivos = sorted(unit_dir.glob("*.md"))
    total_chars = 0
    practico_chars = 0
    teorico_chars = 0
    bloques_count = defaultdict(int)
    visuales = defaultdict(int)
    archivos_presentes = {f.name for f in archivos}

    for f in archivos:
        txt = f.read_text(encoding="utf-8", errors="replace")
        total_chars += len(txt)
        # Bloques pareados
        for m in BLOCK_PAIR_RE.finditer(txt):
            tag = m.group("tag")
            body = m.group("body")
            bloques_count[tag] += 1
            if tag in BLOQUES_PRACTICOS:
                practico_chars += len(body)
            elif tag in BLOQUES_TEORICOS:
                teorico_chars += len(body)
        # Visuales
        for m in VISUAL_RE.finditer(txt):
            visuales[m.group("tipo")] += 1

    pct_practico = round(100 * practico_chars / total_chars, 1) if total_chars else 0.0
    pct_teorico = round(100 * teorico_chars / total_chars, 1) if total_chars else 0.0

    tipos_actividad_usados = [t for t in CATALOGO_ACT if bloques_count.get(t, 0) > 0]
    bloques_faltantes = [b for b in BLOQUES_OBLIGATORIOS if bloques_count.get(b, 0) == 0]

    return {
        "unidad": unidad,
        "manual": manual_n,
        "semestre": semestre_de(manual_n, unidad),
        "archivos_count": len(archivos),
        "archivos_presentes": sorted(archivos_presentes),
        "total_chars": total_chars,
        "pct_practico_aprox": pct_practico,
        "pct_teorico_aprox": pct_teorico,
        "bloques_count": dict(bloques_count),
        "bloques_obligatorios_faltantes": bloques_faltantes,
        "tipos_actividad_usados": tipos_actividad_usados,
        "tipos_actividad_faltantes": [
            t for t in CATALOGO_ACT if t not in tipos_actividad_usados
        ],
        "cobertura_catalogo": f"{len(tipos_actividad_usados)}/12",
        "visuales_por_tipo": dict(visuales),
        "pausas_count": bloques_count.get("pausa", 0),
    }


def main():
    todas = []
    for n, unidades in MANUAL_UNIDADES.items():
        for u in unidades:
            ud = ROOT / "manuales" / f"manual-{n}" / "unidades" / u
            if not ud.exists():
                continue
            todas.append(diag_unidad(ud, n))

    # JSON
    (DOCS / "diagnostico-pedagogico.json").write_text(
        json.dumps(todas, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Markdown reporte
    lines = [
        "# Diagnóstico pedagógico — Manuales Albatros",
        "",
        "Generado por `diagnostico_pedagogico.py`. Mide cobertura vs `manual-spec` §6 §7 §10.",
        "",
        "## Resumen por manual",
        "",
        "| Manual | Unidades | Práctico avg | Bloq oblig. faltantes (suma) | Catálogo cobertura avg |",
        "|---|---:|---:|---:|---:|",
    ]
    por_manual = defaultdict(list)
    for d in todas:
        por_manual[d["manual"]].append(d)

    for n in sorted(por_manual.keys()):
        regs = por_manual[n]
        pct_avg = round(sum(d["pct_practico_aprox"] for d in regs) / len(regs), 1)
        falt = sum(len(d["bloques_obligatorios_faltantes"]) for d in regs)
        cat_avg = round(sum(len(d["tipos_actividad_usados"]) for d in regs) / len(regs), 1)
        lines.append(f"| M{n} | {len(regs)} | {pct_avg}% | {falt} | {cat_avg}/12 |")
    lines.append("")

    # Detalle por unidad agrupado por semestre
    for n in sorted(por_manual.keys()):
        lines.append(f"## Manual {n}")
        lines.append("")
        regs = sorted(por_manual[n], key=lambda d: (d["semestre"] or 9, d["unidad"]))
        for sem in (1, 2):
            sem_regs = [d for d in regs if d["semestre"] == sem]
            if not sem_regs:
                continue
            lines.append(f"### Semestre {sem}")
            lines.append("")
            lines.append("| Unidad | %P | %T | Pausas | Catálogo | Faltan oblig. | Visuales |")
            lines.append("|---|---:|---:|---:|---|---|---:|")
            for d in sem_regs:
                fal = ", ".join(d["bloques_obligatorios_faltantes"]) or "—"
                cat = f"{len(d['tipos_actividad_usados'])}/12"
                tot_vis = sum(d["visuales_por_tipo"].values())
                lines.append(
                    f"| `{d['unidad']}` | {d['pct_practico_aprox']}% | {d['pct_teorico_aprox']}% | "
                    f"{d['pausas_count']} | {cat} | {fal} | {tot_vis} |"
                )
            lines.append("")

    # Análisis para subir a 60%
    lines.append("## Brecha al 60% práctico (objetivo del autor)")
    lines.append("")
    lines.append("Para llevar cada unidad al 60% práctico mínimo: estimar páginas a añadir.")
    lines.append("Asumiendo ~40 pp/unidad y que cada punto porcentual ≈ 0.4 pp:")
    lines.append("")
    lines.append("| Manual | Unidad | %P actual | Brecha al 60% | Páginas a añadir aprox |")
    lines.append("|---|---|---:|---:|---:|")
    total_pp_add = 0
    for d in todas:
        brecha = max(0.0, 60.0 - d["pct_practico_aprox"])
        pp_add = round(brecha * 0.4, 1)
        total_pp_add += pp_add
        if brecha > 0:
            lines.append(f"| M{d['manual']} | `{d['unidad']}` | {d['pct_practico_aprox']}% | {brecha:.1f} pp | {pp_add} pp |")
    lines.append("")
    lines.append(f"**Total páginas prácticas a añadir aprox:** {total_pp_add:.0f} pp")
    lines.append("")
    lines.append("Esto significa redacción de contenido nuevo. NO se puede hacer mecánicamente.")
    lines.append("Plan recomendado: por cada unidad bajo 60%, añadir un nuevo `81-banco-extra.md`")
    lines.append("(banco adicional de 4–6 pp) o subir el peso del taller existente.")
    lines.append("")

    # Cobertura del catálogo
    lines.append("## Cobertura del catálogo de actividades (12 tipos)")
    lines.append("")
    lines.append("Cada unidad debe usar mínimo 3 tipos diferentes (manual-spec §6).")
    lines.append("")
    tipos_global = defaultdict(int)
    for d in todas:
        for t in d["tipos_actividad_usados"]:
            tipos_global[t] += 1
    lines.append("| Tipo | Unidades que lo usan |")
    lines.append("|---|---:|")
    for t in CATALOGO_ACT:
        lines.append(f"| `{t}` | {tipos_global.get(t,0)}/{len(todas)} |")
    lines.append("")

    (DOCS / "diagnostico-pedagogico.md").write_text("\n".join(lines), encoding="utf-8")

    # Reporte corto stdout
    print(f"OK — {len(todas)} unidades diagnosticadas")
    print(f"  -> {DOCS/'diagnostico-pedagogico.md'}")
    print(f"  -> {DOCS/'diagnostico-pedagogico.json'}")
    for n in sorted(por_manual.keys()):
        regs = por_manual[n]
        pct = round(sum(d["pct_practico_aprox"] for d in regs) / len(regs), 1)
        falt = sum(len(d["bloques_obligatorios_faltantes"]) for d in regs)
        print(f"  M{n}: práctico avg {pct}%  · bloq oblig faltantes (suma): {falt}")


if __name__ == "__main__":
    main()
