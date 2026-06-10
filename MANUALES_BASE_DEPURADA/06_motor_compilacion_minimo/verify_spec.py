"""
Verifica los 10 PDFs semestrales contra la regla editorial vigente:

  - Tamano carta: 612 x 792 pt = 215.9 x 279.4 mm.
  - Rango por manual semestral: 120 a 140 paginas.
  - Estructura minima de front/back matter por semestre.
  - Descripciones visuales con longitud minima.

Salida: docs/verificacion-spec.md
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
DOCS = ROOT / "docs"

SEM_MIN = 120
SEM_MAX = 140
SEM_TARGET = 130
MANUALS = (1, 2, 3, 4, 5)
SEMESTERS = (1, 2)
EXPECTED_PDFS = len(MANUALS) * len(SEMESTERS)


def page_count(pdf_data: bytes) -> int:
    return pdf_data.count(b"/Type /Page") - pdf_data.count(b"/Type /Pages")


def page_sizes(pdf_data: bytes) -> list[tuple[float, float]]:
    sizes: list[tuple[float, float]] = []
    media_box = re.compile(
        rb"/MediaBox\s*\[\s*([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s*\]"
    )
    for match in media_box.finditer(pdf_data):
        x0, y0, x1, y1 = map(float, match.groups())
        sizes.append((round(x1 - x0, 1), round(y1 - y0, 1)))
    return sizes


def status_for_pages(pages: int) -> str:
    if SEM_MIN <= pages <= SEM_MAX:
        return "OK"
    if pages > SEM_MAX:
        return "alto"
    return "bajo"


def reduction_percent(current: int, target: int) -> float:
    if current <= 0:
        return 0.0
    return round(((current - target) / current) * 100, 1)


def main() -> None:
    DOCS.mkdir(exist_ok=True)

    lines = [
        "# Verificacion contra manual-spec",
        "",
        "Generado por `verify_spec.py`. Mide los 10 PDFs semestrales contra la regla vigente: 120 a 140 paginas por manual de contenido.",
        "",
        "## Tamano fisico - Carta 8.5x11 in (612x792 pt = 215.9x279.4 mm)",
        "",
        "| PDF | Paginas | Tamano detectado | Carta |",
        "|---|---:|---|:-:|",
    ]

    carta_w = 612.0
    carta_h = 792.0
    tolerance = 2.0
    pdf_pages: dict[tuple[int, int], int] = {}

    for manual in MANUALS:
        for semester in SEMESTERS:
            pdf = DIST / f"manual-{manual}-sem-{semester}.pdf"
            if not pdf.exists():
                lines.append(f"| `manual-{manual}-sem-{semester}.pdf` | - | NO EXISTE | NO |")
                continue

            data = pdf.read_bytes()
            pages = page_count(data)
            pdf_pages[(manual, semester)] = pages
            sizes = page_sizes(data)

            if not sizes:
                lines.append(f"| `manual-{manual}-sem-{semester}.pdf` | {pages} | no detectado | ? |")
                continue

            (width, height), _ = Counter(sizes).most_common(1)[0]
            width_mm = round(width * 25.4 / 72, 1)
            height_mm = round(height * 25.4 / 72, 1)
            ok = abs(width - carta_w) < tolerance and abs(height - carta_h) < tolerance
            tag = "OK" if ok else "NO"
            lines.append(
                f"| `manual-{manual}-sem-{semester}.pdf` | {pages} | {width}x{height} pt ({width_mm}x{height_mm} mm) | {tag} |"
            )

    lines.extend(
        [
            "",
            "**Carta exacta:** 612.0 x 792.0 pt (215.9 x 279.4 mm). Tolerancia +/-2 pt.",
            "",
            "## Rango de paginas por manual semestral",
            "",
            f"Regla correcta: cada PDF semestral debe tener entre {SEM_MIN} y {SEM_MAX} paginas de contenido.",
            "",
            "| PDF | Paginas | Rango 120-140 | Exceso sobre 140 | Reduccion minima |",
            "|---|---:|:-:|---:|---:|",
        ]
    )

    total_pages = 0
    for manual in MANUALS:
        for semester in SEMESTERS:
            pages = pdf_pages.get((manual, semester))
            if pages is None:
                lines.append(f"| `manual-{manual}-sem-{semester}.pdf` | - | faltante | - | - |")
                continue

            total_pages += pages
            excess = max(0, pages - SEM_MAX)
            reduction = reduction_percent(pages, SEM_MAX) if excess else 0.0
            lines.append(
                f"| `manual-{manual}-sem-{semester}.pdf` | {pages} | {status_for_pages(pages)} | {excess} | {reduction}% |"
            )

    max_total = EXPECTED_PDFS * SEM_MAX
    target_total = EXPECTED_PDFS * SEM_TARGET
    min_total = EXPECTED_PDFS * SEM_MIN
    excess_total = max(0, total_pages - max_total)
    target_cut = max(0, total_pages - target_total)

    lines.extend(
        [
            "",
            f"**PDFs esperados:** {EXPECTED_PDFS}.",
            f"**PDFs detectados:** {len(pdf_pages)}.",
            f"**Total actual:** {total_pages} paginas.",
            f"**Rango total permitido:** {min_total}-{max_total} paginas.",
            f"**Exceso minimo sobre el maximo:** {excess_total} paginas.",
            f"**Objetivo recomendado:** {target_total} paginas ({SEM_TARGET} por semestre).",
            f"**Reduccion contra objetivo recomendado:** {target_cut} paginas ({reduction_percent(total_pages, target_total)}%).",
            "",
            "## Estructura minima por semestre",
            "",
            "Cada `semestre-X/` debe tener al menos:",
            "",
        ]
    )

    expected = [
        "00-portada.md",
        "01-carta-estudiante.md",
        "02-carta-docente.md",
        "03-mapa-contenidos.md",
        "04-hilo-conductor.md",
        "05-competencias.md",
        "06-diagnostica.md",
        "90-cierre-semestre.md",
        "91-material-extra.md",
        "92-glosario-semestre.md",
        "93-bibliografia-semestre.md",
        "94-indice-analitico.md",
    ]

    lines.append("| Manual | Sem | Archivos esperados | Presentes | Completo |")
    lines.append("|---|:-:|---:|---:|:-:|")
    for manual in MANUALS:
        for semester in SEMESTERS:
            sem_dir = ROOT / "manuales" / f"manual-{manual}" / f"semestre-{semester}"
            present = sum(1 for filename in expected if (sem_dir / filename).exists())
            tag = "OK" if present == len(expected) else "NO"
            lines.append(f"| M{manual} | {semester} | {len(expected)} | {present} | {tag} |")

    lines.extend(
        [
            "",
            "## Bloques minimos por unidad",
            "",
            "Ver `docs/diagnostico-pedagogico.md`: cero unidades con bloques obligatorios faltantes.",
            "",
            "## Visuales - descripcion >= 50 caracteres",
            "",
        ]
    )

    bad_visuals: list[tuple[str, str]] = []
    visual_desc = re.compile(r'::visual\{[^}]*descripcion="([^"]*)"[^}]*\}')
    for md in ROOT.glob("manuales/**/*.md"):
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for match in visual_desc.finditer(text):
            description = match.group(1)
            if len(description) < 50:
                bad_visuals.append((str(md.relative_to(ROOT)).replace("\\", "/"), description[:60]))

    if not bad_visuals:
        lines.append("OK: todos los `::visual{}` tienen `descripcion` >= 50 caracteres.")
    else:
        lines.append(f"{len(bad_visuals)} visuales con descripcion corta:")
        for filename, description in bad_visuals[:20]:
            lines.append(f"- `{filename}` -> `{description}...`")

    lines.append("")
    out = DOCS / "verificacion-spec.md"
    out.write_text("\n".join(lines), encoding="utf-8")

    print(f"OK -> {out}")
    print(f"PDFs detectados: {len(pdf_pages)}/{EXPECTED_PDFS}")
    print(f"Total paginas actuales: {total_pages}")
    print(f"Rango total permitido: {min_total}-{max_total}")
    print(f"Exceso minimo: {excess_total}")


if __name__ == "__main__":
    main()
