from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import re
import textwrap


ROOT = Path(__file__).resolve().parents[1]
MANUALES = ROOT / "01_fuente_principal_markdown" / "manuales"
VISUALES = ROOT / "05_assets_visuales_iconos" / "visuales"
DOCS = ROOT / "07_docs_pedagogicos"
IMG_REL_PREFIX = "../../../../05_assets_visuales_iconos/visuales"


def e(value: object) -> str:
    return escape(str(value), quote=True)


def wrap(value: str, width: int) -> list[str]:
    return textwrap.wrap(str(value), width=width, break_long_words=False, replace_whitespace=False)


def page(title: str, kicker: str, body: str, classes: str = "page") -> dict[str, str]:
    return {"title": title, "kicker": kicker, "body": body, "classes": classes}


@dataclass
class ModelLine:
    expr: str
    use: str
    elements: str


@dataclass
class Unit:
    id: str
    title: str
    episode: str
    history: str
    analogy: str
    questions: list[str]
    subtopics: list[str]
    concepts: list[tuple[str, str]]
    process: list[str]
    models: list[ModelLine]
    worked_problem: str
    worked_data: list[str]
    worked_steps: list[str]
    worked_result: str
    product: str
    practice: str
    reading: str
    code: str | None = None
    code_check: list[str] | None = None


CSS = """
@page { size: letter; margin: 0; }
@page landscape { size: letter landscape; margin: 0; }

:root {
  --blue: #0E3A8A;
  --teal: #0E7490;
  --green: #15803D;
  --amber: #B45309;
  --red: #B91C1C;
  --ink: #172033;
  --muted: #526070;
  --line: #D7DEE8;
  --soft: #F7FAFC;
  --theory: #EFF6FF;
  --practice: #ECFDF5;
  --warm: #FFF7ED;
}

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  background: #E6EBF2;
  color: var(--ink);
  font-family: Arial, "Segoe UI", sans-serif;
  line-height: 1.32;
}
.page {
  width: 216mm;
  height: 279mm;
  min-height: 279mm;
  margin: 0 auto 8mm;
  padding: 12mm 13mm 15mm;
  background: #FFFFFF;
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 4mm;
  break-after: page;
  page-break-after: always;
  box-shadow: 0 8px 28px rgba(15, 23, 42, 0.12);
}
.landscape {
  page: landscape;
  width: 279mm;
  height: 216mm;
  min-height: 216mm;
  padding: 8mm 10mm 12mm;
  gap: 2.6mm;
}
.cover {
  padding: 0;
  color: #FFFFFF;
  display: block;
}
.cover .visual {
  position: absolute;
  inset: 0;
  margin: 0;
}
.cover img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.cover figcaption {
  display: none;
}
.cover::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, rgba(14, 58, 138, 0.94), rgba(14, 116, 144, 0.42));
}
.cover-content {
  position: relative;
  z-index: 1;
  height: 100%;
  padding: 20mm 17mm 16mm;
  display: grid;
  grid-template-rows: auto 1fr auto;
}
.school {
  font-size: 16pt;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0;
}
.cover h1 {
  margin: 25mm 0 5mm;
  max-width: 150mm;
  color: #FFFFFF;
  font-size: 40pt;
  line-height: 0.98;
  letter-spacing: 0;
  border: 0;
  padding: 0;
}
.cover .lead {
  max-width: 150mm;
  color: rgba(255,255,255,0.94);
  font-size: 15pt;
  line-height: 1.25;
}
.cover-meta {
  display: grid;
  grid-template-columns: 1.2fr 1fr 1fr;
  gap: 5mm;
  padding-top: 6mm;
  border-top: 1px solid rgba(255,255,255,0.55);
  font-size: 11pt;
}
.kicker {
  margin: 0;
  color: var(--amber);
  font-size: 9.8pt;
  line-height: 1.15;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
h1, h2, h3 {
  margin: 0;
  color: var(--blue);
  line-height: 1.08;
  letter-spacing: 0;
}
h2 {
  font-size: 19.5pt;
  padding-bottom: 2mm;
  border-bottom: 2px solid var(--line);
}
h3 {
  font-size: 12.8pt;
  margin-bottom: 1.5mm;
}
p, li {
  font-size: 11.4pt;
  line-height: 1.32;
}
p { margin: 0 0 2.8mm; }
ul, ol {
  margin: 1mm 0 2.8mm 5mm;
  padding-left: 5mm;
}
li { margin: 1mm 0; }
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5mm 0 3mm;
  font-size: 10.2pt;
  break-inside: avoid;
}
th, td {
  border: 1px solid var(--line);
  padding: 2mm;
  vertical-align: top;
}
th {
  color: #FFFFFF;
  background: var(--blue);
  text-align: left;
}
.large-table {
  font-size: 10.8pt;
}
.mini-table {
  font-size: 9.8pt;
}
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4mm;
  align-items: start;
}
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 3mm;
  align-items: stretch;
}
.box, .concept, .formula-card, .route-card, .appendix-card {
  border: 1px solid var(--line);
  border-left: 5px solid var(--blue);
  background: var(--soft);
  padding: 3mm;
  break-inside: avoid;
}
.theory-box { background: var(--theory); }
.practice-box { background: var(--practice); border-left-color: var(--green); }
.question-box { background: var(--warm); border-left-color: var(--amber); }
.warning-box { background: #FEF2F2; border-left-color: var(--red); }
.concept strong, .formula-card strong, .route-card strong, .appendix-card strong {
  color: var(--blue);
}
.visual {
  margin: 0;
  border: 0;
  background: transparent;
  break-inside: avoid;
}
.visual img {
  display: block;
  width: 100%;
  height: auto;
  object-fit: contain;
}
.visual.full img { max-height: 205mm; }
.visual.page-fit img { max-height: 178mm; }
.landscape .visual.full img { max-height: 176mm; }
figcaption {
  color: var(--muted);
  font-size: 9.8pt;
  line-height: 1.25;
  padding-top: 2mm;
}
.formula {
  font-family: Consolas, "Courier New", monospace;
  font-size: 11.2pt;
  background: #FFFFFF;
  border: 1px solid var(--line);
  padding: 2mm;
}
.worked-example, .worked-step {
  border: 1px solid var(--line);
  background: #FFFFFF;
  padding: 2.5mm;
  break-inside: avoid;
}
.worked-step {
  margin-bottom: 2mm;
}
.exercise, .bank-item {
  border: 1px solid var(--line);
  background: #FFFFFF;
  padding: 2.3mm;
  margin: 0 0 2.3mm;
  font-size: 10.4pt;
  line-height: 1.28;
  break-inside: avoid;
}
.exercise strong, .bank-item strong { color: var(--blue); }
.operation-lines, .answer-lines {
  margin-top: 2mm;
}
.operation-lines span, .answer-lines span {
  display: block;
  border-bottom: 1px solid #AEB7C4;
  height: 6.4mm;
}
.match-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2mm;
  margin-top: 2mm;
}
.match-grid div {
  border: 1px solid var(--line);
  padding: 2mm;
  background: #F8FAFC;
  font-size: 9.6pt;
}
.code-block {
  background: #111827;
  color: #F8FAFC;
  border-radius: 0;
  padding: 3mm;
  font-family: Consolas, "Courier New", monospace;
  font-size: 8.3pt;
  line-height: 1.18;
  white-space: pre-wrap;
  overflow: hidden;
}
.footer {
  position: absolute;
  left: 13mm;
  right: 13mm;
  bottom: 6mm;
  display: flex;
  justify-content: space-between;
  border-top: 1px solid var(--line);
  padding-top: 2mm;
  color: var(--muted);
  font-size: 8.8pt;
}
.landscape .footer {
  left: 10mm;
  right: 10mm;
}
.toc-row {
  display: grid;
  grid-template-columns: 18mm 1.15fr 1.6fr;
  gap: 3mm;
  border-bottom: 1px solid var(--line);
  padding: 2mm 0;
  font-size: 10.6pt;
}
.badge-row {
  display: flex;
  gap: 2mm;
  flex-wrap: wrap;
}
.badge {
  border: 1px solid var(--line);
  background: #FFFFFF;
  padding: 1.5mm 2mm;
  font-size: 9.5pt;
  color: var(--blue);
  font-weight: 700;
}
.ratio {
  display: grid;
  grid-template-columns: 40fr 60fr;
  border: 1px solid var(--line);
}
.ratio div {
  padding: 3mm;
  color: #FFFFFF;
  font-weight: 800;
}
.ratio .theory { background: var(--blue); }
.ratio .practice { background: var(--green); }
@media print {
  body { background: #FFFFFF; }
  .page { margin: 0; box-shadow: none; }
}
"""


def svg_tspans(text: str, x: int, y: int, size: int, color: str = "#172033", weight: int = 500, width: int = 52) -> str:
    lines = wrap(text, width)
    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else int(size * 1.25)
        tspans.append(f'<tspan x="{x}" dy="{dy}">{e(line)}</tspan>')
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{"".join(tspans)}</text>'


def write_svg(path: Path, title: str, subtitle: str, blocks: list[tuple[str, str]], footer: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    colors = ["#DBEAFE", "#DCFCE7", "#FEF3C7", "#E0F2FE", "#FEE2E2", "#F5F5F4"]
    strokes = ["#0E3A8A", "#15803D", "#B45309", "#0E7490", "#B91C1C", "#57534E"]
    box_svg = []
    for idx, (head, text) in enumerate(blocks[:6]):
        col = idx % 3
        row = idx // 3
        x = 78 + col * 585
        y = 260 + row * 320
        box_svg.append(
            f'<rect x="{x}" y="{y}" width="520" height="250" rx="0" fill="{colors[idx]}" stroke="{strokes[idx]}" stroke-width="5"/>'
        )
        box_svg.append(svg_tspans(head, x + 28, y + 56, 34, strokes[idx], 800, 23))
        box_svg.append(svg_tspans(text, x + 28, y + 118, 28, "#172033", 500, 29))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1150" viewBox="0 0 1800 1150">
  <rect width="1800" height="1150" fill="#FFFFFF"/>
  <rect x="0" y="0" width="1800" height="150" fill="#0E3A8A"/>
  <rect x="0" y="150" width="1800" height="14" fill="#F59E0B"/>
  {svg_tspans(title, 76, 72, 48, "#FFFFFF", 850, 48)}
  {svg_tspans(subtitle, 78, 210, 30, "#334155", 600, 82)}
  {''.join(box_svg)}
  <rect x="72" y="1040" width="1656" height="4" fill="#D7DEE8"/>
  {svg_tspans(footer, 78, 1090, 28, "#526070", 600, 92)}
</svg>'''
    path.write_text(svg, encoding="utf-8", newline="\n")


def visual_rel(manual: int, unit_id: str, filename: str) -> str:
    return f"{IMG_REL_PREFIX}/manual-{manual}/{unit_id}/{filename}"


def figure(src: str, phrase: str, mode: str = "full", visual_id: str = "") -> str:
    return (
        f'<figure class="visual {mode}" data-visual-id="{e(visual_id)}">'
        f'<img src="{e(src)}" alt="{e(phrase)}">'
        f"<figcaption>{e(phrase)}</figcaption>"
        "</figure>"
    )


def bullets(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{e(item)}</li>" for item in items) + "</ul>"


def answer_lines(count: int = 3) -> str:
    return '<div class="answer-lines">' + "".join("<span></span>" for _ in range(count)) + "</div>"


def operations(count: int = 2) -> str:
    return '<div class="operation-lines"><em>Aquí deja tus operaciones, verificación o evidencia.</em>' + "".join("<span></span>" for _ in range(count)) + "</div>"


def concept_table(unit: Unit) -> str:
    rows = "".join(
        f"<tr><td><strong>{e(name)}</strong></td><td>{e(desc)}</td></tr>"
        for name, desc in unit.concepts
    )
    return f'<table class="large-table"><tr><th>Concepto</th><th>Explicación útil para resolver la unidad</th></tr>{rows}</table>'


def model_table(unit: Unit) -> str:
    rows = "".join(
        "<tr>"
        f'<td><div class="formula">{e(model.expr)}</div></td>'
        f"<td>{e(model.use)}</td>"
        f"<td>{e(model.elements)}</td>"
        "</tr>"
        for model in unit.models
    )
    return f'<table class="large-table"><tr><th>Modelo, fórmula o criterio</th><th>Cuándo se usa</th><th>Elementos, unidades o escala</th></tr>{rows}</table>'


def render_page(item: dict[str, str], manual_label: str, number: int) -> str:
    classes = item["classes"]
    if "cover" in classes:
        return f'<section class="{classes}">{item["body"]}</section>'
    footer = f'<div class="footer"><span>{e(manual_label)}</span><span>Semestre 1 / p. {number}</span></div>'
    return (
        f'<section class="{classes}">\n'
        f'<p class="kicker">{e(item["kicker"])}</p>\n'
        f'<h2>{e(item["title"])}</h2>\n'
        f'{item["body"]}\n'
        f'{footer}\n'
        '</section>'
    )


def render_html(title: str, pages: list[dict[str, str]], manual_label: str) -> str:
    body = "\n\n".join(render_page(item, manual_label, idx + 1) for idx, item in enumerate(pages))
    return (
        "<!doctype html>\n"
        '<html lang="es">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"  <title>{e(title)}</title>\n"
        f"  <style>{CSS}</style>\n"
        "</head>\n"
        "<body>\n"
        f"{body}\n"
        "</body>\n"
        "</html>\n"
    )


def make_visuals(manual: int, data: dict[str, object]) -> dict[str, dict[str, str]]:
    visual_map: dict[str, dict[str, str]] = {}
    sem_dir = VISUALES / f"manual-{manual}" / "sem1"
    sem_file = f"M{manual}-sem1-30.svg"
    write_svg(
        sem_dir / sem_file,
        str(data["title"]),
        "Primer semestre: historia, modelos, práctica y evidencia imprimible.",
        [
            ("Caso conductor", str(data["case"])),
            ("40% teoría", "Conceptos, historia, modelos, criterios y lenguaje técnico."),
            ("60% práctica", "Ejercicios, comparación, verificación, producto y defensa."),
            ("Revisión visual", "Infografías grandes, texto legible y sin marcos que reduzcan contenido."),
            ("Cierre", "Examen integrador, bibliografía, recursos, glosario e índice analítico."),
            ("Colegio", "Colegio Nuevo Tecno."),
        ],
        "La unidad no avanza por memoria: avanza cuando el estudiante deja evidencia revisable.",
    )
    visual_map["sem1"] = {"cover": visual_rel(manual, "sem1", sem_file)}

    for unit in data["units"]:  # type: ignore[index]
        assert isinstance(unit, Unit)
        unit_dir = VISUALES / f"manual-{manual}" / unit.id
        prefix = f"M{manual}-{unit.id}"
        files = {
            "cover": f"{prefix}-30.svg",
            "process": f"{prefix}-31.svg",
            "models": f"{prefix}-32.svg",
        }
        write_svg(
            unit_dir / files["cover"],
            unit.title,
            unit.episode,
            [
                ("Historia", unit.history[:150]),
                ("Analogía", unit.analogy),
                ("Producto", unit.product),
                ("Práctica", unit.practice),
                ("Primer dato", unit.worked_data[0]),
                ("Cierre", "Defender una decisión con evidencia, no con opinión."),
            ],
            "La imagen funciona como mapa de entrada: ubica historia, producto y criterio antes de resolver.",
        )
        write_svg(
            unit_dir / files["process"],
            f"Proceso de {unit.title}",
            "Lectura visual para conectar el caso conductor con la actividad.",
            [(f"Paso {idx + 1}", step) for idx, step in enumerate(unit.process[:6])],
            "Primero se entiende el flujo; después se calcula, compara o programa con intención.",
        )
        write_svg(
            unit_dir / files["models"],
            f"Modelos clave de {unit.title}",
            "Cada fórmula o criterio debe tener elementos claros y una escala de revisión.",
            [(model.expr, model.use) for model in unit.models[:6]],
            "Un resultado sin unidad, criterio o evidencia no está listo para defenderse.",
        )
        visual_map[unit.id] = {key: visual_rel(manual, unit.id, value) for key, value in files.items()}
    return visual_map


def front_pages(manual: int, data: dict[str, object], visuals: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    units: list[Unit] = data["units"]  # type: ignore[assignment]
    label = f"Manual {manual} / Semestre 1"
    toc = "".join(
        f'<div class="toc-row"><strong>{e(unit.id.upper())}</strong><span>{e(unit.title)}</span><span>{e(unit.product)}</span></div>'
        for unit in units
    )
    detail_chunks = [units[:3], units[3:]]
    pages = [
        page(
            "",
            "",
            (
                figure(visuals["sem1"]["cover"], "Una ruta de aprendizaje funciona cuando cada herramienta deja evidencia.", "full", f"M{manual}-sem1-30")
                + '<div class="cover-content">'
                + '<div class="school">Colegio Nuevo Tecno</div>'
                + '<div>'
                + f'<h1>{e(data["title"])}</h1>'
                + f'<p class="lead">{e(data["subtitle"])}</p>'
                + '</div>'
                + '<div class="cover-meta">'
                + f'<div><strong>Semestre 1</strong><br>{e(data["case"])}</div>'
                + '<div><strong>Distribución</strong><br>40% teoría / 60% práctica</div>'
                + '<div><strong>Salida</strong><br>HTML y PDF para hoja carta</div>'
                + '</div></div>'
            ),
            "page cover",
        ),
        page(
            "Temario completo del semestre",
            label,
            (
                f"<p>Este primer semestre funciona como un manual completo: inicia con las bases, desarrolla el caso conductor y cierra con evaluación, recursos, glosario, bibliografía e índice analítico. La continuidad del siguiente semestre amplía la misma ruta sin repetirla.</p>"
                f'<div class="toc-list">{toc}</div>'
                '<div class="ratio"><div class="theory">40% comprender modelos</div><div class="practice">60% practicar, verificar y producir evidencia</div></div>'
            ),
        ),
    ]
    for idx, chunk in enumerate(detail_chunks, start=1):
        if not chunk:
            continue
        rows = "".join(
            "<tr>"
            f"<td>{e(unit.id.upper())}</td>"
            f"<td>{e(unit.title)}<br><span>{e(unit.episode)}</span></td>"
            f"<td>{e('; '.join(unit.subtopics))}</td>"
            f"<td>{e(unit.product)}</td>"
            "</tr>"
            for unit in chunk
        )
        pages.append(
            page(
                f"Desglose del temario {idx}",
                label,
                f'<table class="mini-table"><tr><th>Unidad</th><th>Caso</th><th>Temas</th><th>Producto</th></tr>{rows}</table>',
            )
        )
    pages.extend(
        [
            page(
                "Cómo trabajar este manual",
                label,
                (
                    f"<p>{e(data['story'])}</p>"
                    '<div class="grid-3">'
                    '<div class="route-card"><strong>1. Historia</strong><br>Entrar por una situación real y preguntas introductorias.</div>'
                    '<div class="route-card"><strong>2. Modelo</strong><br>Nombrar conceptos, fórmulas, criterios, unidades o escalas.</div>'
                    '<div class="route-card"><strong>3. Evidencia</strong><br>Resolver, comparar, verificar y entregar un producto revisable.</div>'
                    '</div>'
                ),
            ),
            page(
                "Diagnóstico inicial",
                label,
                (
                    '<div class="exercise"><strong>1.</strong> Explica con tus palabras qué evidencia necesitarías para confiar en una respuesta generada por IA.' + answer_lines(3) + '</div>'
                    '<div class="exercise"><strong>2.</strong> Convierte una situación cotidiana del caso conductor en una pregunta verificable.' + answer_lines(3) + '</div>'
                    '<div class="exercise"><strong>3.</strong> Identifica una variable, una escala de revisión y un posible error de interpretación.' + answer_lines(3) + '</div>'
                ),
            ),
            page(
                "Contrato de precisión",
                label,
                (
                    '<div class="box warning-box"><h3>Regla de impresión</h3><p>Las infografías deben ocupar ancho completo o página horizontal cuando tengan texto. Ninguna imagen se encierra en un cuadro que reduzca su lectura.</p></div>'
                    '<div class="box theory-box"><h3>Regla de instrucción</h3><p>Cada actividad explica qué comparar, qué calcular, qué escribir y qué evidencia entregar. Si requiere investigación externa, lo dice de forma explícita.</p></div>'
                    '<div class="box practice-box"><h3>Regla de banco</h3><p>Antes del banco aparece un ejemplo resuelto de principio a fin. El banco usa los modelos de la unidad y varía entre cálculo, tabla, relación de columnas, explicación y decisión de caso.</p></div>'
                ),
            ),
        ]
    )
    return pages


def unit_toc(unit: Unit, label: str) -> dict[str, str]:
    rows = "".join(f"<tr><td>{idx + 1}</td><td>{e(topic)}</td></tr>" for idx, topic in enumerate(unit.subtopics))
    return page(
        "Ruta interna de la unidad",
        label,
        (
            f"<p>La unidad se organiza para que el estudiante pase de relato a procedimiento. No se pide resolver nada que no haya sido explicado o marcado como investigación propia.</p>"
            f'<table><tr><th>#</th><th>Subtema operativo</th></tr>{rows}</table>'
            f'<div class="box practice-box"><h3>Producto de unidad</h3><p>{e(unit.product)}</p></div>'
        ),
    )


def infographic_explanation(unit: Unit, label: str) -> dict[str, str]:
    cards = "".join(
        f'<div class="concept"><strong>{e(step.split(":", 1)[0])}</strong><br>{e(step)}</div>'
        for step in unit.process[:4]
    )
    return page(
        "Explicación de la infografía",
        label,
        (
            f"<p>La infografía anterior no es decorativa: ordena el camino del caso conductor. Primero ubica el problema, después selecciona el modelo, luego ejecuta una práctica y finalmente exige una evidencia que pueda revisarse.</p>"
            f'<div class="grid-2">{cards}</div>'
            f'<div class="box question-box"><h3>Conexión con el caso</h3><p>{e(unit.episode)} La imagen sirve para decidir qué dato, criterio o paso falta antes de entregar el producto.</p></div>'
        ),
    )


def mini_activity_page(unit: Unit, label: str) -> dict[str, str]:
    return page(
        "Mini actividad conectada con la imagen",
        label,
        (
            f"<p>Usa la imagen como ejemplo de organización. Tu tarea es construir una versión equivalente para una situación propia, no copiar los textos de la infografía.</p>"
            '<div class="exercise"><strong>Actividad.</strong> Elige un subtema de la unidad y diseña una mini infografía con cuatro partes: problema, datos o criterios, procedimiento y evidencia final.' + answer_lines(4) + '</div>'
            f'<div class="box practice-box"><h3>Entrega mínima</h3><p>Una hoja con título, cuatro bloques, una conclusión de tres líneas y una relación explícita con: {e(unit.product)}.</p></div>'
        ),
    )


def worked_pages(unit: Unit, label: str) -> list[dict[str, str]]:
    data_html = bullets(unit.worked_data)
    steps_a = unit.worked_steps[:3]
    steps_b = unit.worked_steps[3:]
    body_a = (
        f'<div class="worked-example"><h3>Problema</h3><p>{e(unit.worked_problem)}</p></div>'
        f'<div class="worked-example"><h3>Datos dados</h3>{data_html}</div>'
        + "".join(f'<div class="worked-step"><strong>Paso {idx + 1}.</strong> {e(step)}</div>' for idx, step in enumerate(steps_a))
    )
    body_b = (
        "".join(f'<div class="worked-step"><strong>Paso {idx + 4}.</strong> {e(step)}</div>' for idx, step in enumerate(steps_b))
        + f'<div class="box practice-box"><h3>Resultado interpretado</h3><p>{e(unit.worked_result)}</p></div>'
        + '<div class="box question-box"><h3>Antes de pasar al banco</h3><p>Subraya qué modelo usaste, qué dato fue más importante y qué límite debe mencionarse en la conclusión.</p></div>'
    )
    return [
        page("Ejemplo resuelto de principio a fin 1", label, body_a),
        page("Ejemplo resuelto de principio a fin 2", label, body_b),
    ]


def exercise_bank(unit: Unit) -> list[str]:
    model_names = [model.expr for model in unit.models]
    exercises = [
        f"Define {unit.title} en cinco líneas y señala cuál concepto de la tabla anterior es indispensable para resolver el caso.",
        f"Construye una tabla con tres filas: dato o criterio, modelo que lo usa y evidencia que se debe entregar.",
        f"Usa el modelo {model_names[0]} con valores o puntajes propuestos por ti. Indica la escala y justifica el resultado.",
        f"Usa el modelo {model_names[1]} para comparar dos alternativas del caso. Explica cuál conviene y por qué.",
        '<strong>Relación de columnas.</strong><div class="match-grid"><div>A. Criterio de calidad<br>B. Evidencia<br>C. Límite del modelo<br>D. Producto final</div><div>1. Lo que se entrega para revisión<br>2. Condición que impide exagerar la conclusión<br>3. Prueba visible de que la tarea se hizo<br>4. Regla para decidir si funciona</div></div>Escribe las parejas correctas.',
        f"Detecta un error posible al aplicar {model_names[2]}. Escribe el error, su consecuencia y la corrección.",
        f"Completa un cuadro comparativo entre una respuesta débil y una respuesta confiable para: {unit.episode}.",
        f"Calcula o puntúa un segundo escenario usando {model_names[3]}. Después compara el resultado con el ejercicio 3.",
        "Escribe una pregunta abierta que obligue a verificar una fuente, un dato, una salida o un procedimiento.",
        f"Usa {model_names[-1]} para cerrar una decisión. Debes mostrar datos, sustitución o criterio y conclusión.",
        "Diseña una rúbrica de cuatro criterios con escala 1 a 4 para evaluar el producto de la unidad.",
        "Redacta una explicación de seis líneas para un compañero que faltó a clase. No uses solo definiciones.",
        "Propón una mini práctica de 15 minutos. Debe incluir material, pasos, evidencia y criterio de éxito.",
        "Identifica una instrucción ambigua en el caso y reescríbela de forma precisa, medible y revisable.",
        "Construye una matriz de decisión con dos opciones, tres criterios y una conclusión final.",
        "Explica qué parte de la infografía usarías para defender tu procedimiento ante el docente.",
        "Señala una fuente externa que consultarías. Indica qué buscarías y cómo evitarías copiar sin entender.",
        "Escribe una conclusión técnica separando hecho, inferencia y acción siguiente.",
        "Cambia un dato del caso, predice el efecto y luego recalcula o repuntúa con el modelo correspondiente.",
        "Entrega una versión final de tu procedimiento con título, datos, modelo, evidencia y límite.",
    ]
    return exercises


def exercise_pages(unit: Unit, label: str) -> list[dict[str, str]]:
    pages: list[dict[str, str]] = []
    exercises = exercise_bank(unit)
    for page_index in range(0, len(exercises), 4):
        items = exercises[page_index:page_index + 4]
        body = ""
        for idx, item in enumerate(items, start=page_index + 1):
            body += f'<div class="exercise bank-item"><strong>{idx}.</strong> {item}{operations(2)}</div>'
        pages.append(page(f"Banco de ejercicios {page_index // 4 + 1}", label, body))
    return pages


def code_pages(unit: Unit, label: str) -> list[dict[str, str]]:
    if not unit.code:
        return []
    checks = bullets(unit.code_check or [])
    return [
        page(
            "Ejemplo guiado con código",
            label,
            (
                f"<p>La práctica de programación aparece después de los conceptos para que el código sea consecuencia del razonamiento, no una receta aislada.</p>"
                '<p><strong>[icono: Sección de código]</strong></p>'
                f'<pre class="code-block">{e(unit.code)}</pre>'
            ),
        ),
        page(
            "Explicación del código por bloques",
            label,
            (
                '<div class="grid-2">'
                '<div class="concept"><strong>Datos</strong><br>El bloque inicial crea o carga datos mínimos para que la práctica pueda ejecutarse sin depender de archivos externos.</div>'
                '<div class="concept"><strong>Procedimiento</strong><br>La parte central aplica el concepto de la unidad con nombres claros y pasos visibles.</div>'
                '<div class="concept"><strong>Salida</strong><br>El cierre imprime una tabla, valor, gráfica o interpretación que permite comprobar el resultado.</div>'
                '<div class="concept"><strong>Registro</strong><br>El estudiante anota qué cambió, qué funcionó y qué límite conserva el análisis.</div>'
                '</div>'
            ),
        ),
        page(
            "Comprobación y mini actividad controlada",
            label,
            (
                f'<div class="box practice-box"><h3>Comprobación del resultado</h3>{checks}</div>'
                '<div class="exercise"><strong>[icono: Mini Actividades]</strong> Cambia un solo dato del ejemplo, ejecuta de nuevo el procedimiento y compara la salida anterior con la nueva.' + answer_lines(3) + '</div>'
                '<div class="exercise"><strong>[icono: Reto Digital]</strong> Entrega una captura, tabla o frase de interpretación que demuestre que el código se ejecutó y que entendiste el cambio.' + answer_lines(3) + '</div>'
            ),
        ),
        page(
            "Variación práctica del código",
            label,
            (
                f"<p>Ahora conecta el código con el caso conductor: {e(unit.episode)}. La variación debe mantener la misma estructura, pero cambiar el dato, columna, gráfica o criterio principal.</p>"
                '<div class="exercise"><strong>1.</strong> Escribe qué parte del código modificarás y por qué.' + answer_lines(3) + '</div>'
                '<div class="exercise"><strong>2.</strong> Describe qué salida esperas antes de ejecutar.' + answer_lines(3) + '</div>'
                '<div class="exercise"><strong>3.</strong> Registra si la salida confirmó o contradijo tu predicción.' + answer_lines(3) + '</div>'
            ),
        ),
    ]


def unit_pages(manual: int, unit: Unit, visuals: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    label = f"Manual {manual} / {unit.id.upper()} / 40% teoría - 60% práctica"
    visual = visuals[unit.id]
    pages = [
        page(
            "",
            "",
            (
                figure(visual["cover"], "Antes de operar una herramienta, hay que entender qué evidencia se espera.", "full", f"M{manual}-{unit.id}-30")
                + '<div class="cover-content">'
                + f'<div class="school">Colegio Nuevo Tecno · {e(unit.id.upper())}</div>'
                + '<div>'
                + f'<h1>{e(unit.title)}</h1>'
                + f'<p class="lead">{e(unit.episode)}</p>'
                + '</div>'
                + '<div class="cover-meta">'
                + '<div><strong>Entrada</strong><br>Historia y preguntas</div>'
                + '<div><strong>Modelo</strong><br>Conceptos, fórmulas o criterios</div>'
                + '<div><strong>Salida</strong><br>Práctica y producto</div>'
                + '</div></div>'
            ),
            "page cover",
        ),
        page(
            "Historia, analogía y preguntas introductorias",
            label,
            (
                f"<p>{e(unit.history)}</p>"
                f'<div class="box theory-box"><h3>Analogía de entrada</h3><p>{e(unit.analogy)}</p></div>'
                + "".join(f'<div class="exercise"><strong>Pregunta {idx + 1}.</strong> {e(question)}{answer_lines(3)}</div>' for idx, question in enumerate(unit.questions))
            ),
        ),
        unit_toc(unit, label),
        page(
            "Infografía principal de la unidad",
            label,
            figure(visual["process"], "Cuando el proceso se ve completo, la práctica deja de sentirse como una lista suelta.", "full", f"M{manual}-{unit.id}-31"),
            "page landscape",
        ),
        infographic_explanation(unit, label),
        page(
            "Conceptos fundamentales",
            label,
            (
                "<p>Estos conceptos se presentan antes de cualquier actividad para que el estudiante tenga herramientas de resolución. Cuando una actividad requiera investigar, se indicará explícitamente.</p>"
                + concept_table(unit)
            ),
        ),
        page(
            "Modelos visuales de trabajo",
            label,
            figure(visual["models"], "Una fórmula, criterio o esquema solo ayuda si cada elemento se entiende y puede revisarse.", "full", f"M{manual}-{unit.id}-32"),
            "page landscape",
        ),
        mini_activity_page(unit, label),
        page(
            "Fórmulas, criterios y unidades",
            label,
            (
                "<p>Los modelos de esta unidad se usan en el ejemplo resuelto y en el banco de ejercicios. En IA algunos modelos son criterios de evaluación; en programación y estadística son fórmulas numéricas.</p>"
                + model_table(unit)
            ),
        ),
        page(
            "Cómo usar los modelos sin perder precisión",
            label,
            (
                '<div class="grid-2">'
                '<div class="formula-card"><strong>1. Nombrar datos</strong><br>Antes de sustituir, escribe qué representa cada dato y en qué escala se mide.</div>'
                '<div class="formula-card"><strong>2. Revisar unidad o escala</strong><br>Si el modelo usa conteos, porcentaje, puntos o segundos, no mezcles magnitudes.</div>'
                '<div class="formula-card"><strong>3. Interpretar</strong><br>El resultado necesita una frase: qué significa, qué permite decidir y qué no demuestra.</div>'
                '<div class="formula-card"><strong>4. Verificar</strong><br>Compara contra una fuente, una rúbrica, un segundo cálculo o una salida observable.</div>'
                '</div>'
            ),
        ),
    ]
    pages.extend(worked_pages(unit, label))
    pages.extend(exercise_pages(unit, label))
    pages.extend(code_pages(unit, label))
    pages.extend(
        [
            page(
                "Especificación de actividad y práctica",
                label,
                (
                    f'<table><tr><th>Fase</th><th>Acción precisa</th><th>Evidencia</th></tr>'
                    f'<tr><td>Preparar</td><td>Leer historia, conceptos y modelos de {e(unit.title)}.</td><td>Preguntas contestadas con tres líneas cada una.</td></tr>'
                    f'<tr><td>Aplicar</td><td>{e(unit.practice)}</td><td>Procedimiento visible con datos, criterio o código.</td></tr>'
                    f'<tr><td>Verificar</td><td>Comparar resultado con rúbrica, fuente o cálculo alterno.</td><td>Corrección o confirmación escrita.</td></tr>'
                    f'<tr><td>Entregar</td><td>{e(unit.product)}</td><td>Producto final y conclusión técnica.</td></tr></table>'
                    '<div class="box practice-box"><h3>Distribución sugerida</h3><p>20 minutos para recuperar conceptos, 50 minutos para práctica guiada, 30 minutos para banco y 20 minutos para defensa o corrección.</p></div>'
                ),
            ),
            page(
                "Rúbrica del producto",
                label,
                (
                    '<table class="large-table"><tr><th>Criterio</th><th>Excelente</th><th>Suficiente</th><th>Debe corregirse</th></tr>'
                    '<tr><td>Precisión conceptual</td><td>Usa términos y modelos sin confundirlos.</td><td>Hay una imprecisión menor.</td><td>Mezcla conceptos o no los explica.</td></tr>'
                    '<tr><td>Evidencia</td><td>El resultado puede revisarse o replicarse.</td><td>La evidencia existe pero falta detalle.</td><td>No se puede comprobar el proceso.</td></tr>'
                    '<tr><td>Producto</td><td>Responde directamente al caso.</td><td>Responde parcialmente.</td><td>No resuelve la tarea.</td></tr>'
                    '<tr><td>Comunicación</td><td>Separa dato, interpretación y límite.</td><td>Comunica con algunas ambigüedades.</td><td>Presenta conclusión sin soporte.</td></tr></table>'
                ),
            ),
            page(
                "Lectura complementaria breve",
                label,
                (
                    f"<p>{e(unit.reading)}</p>"
                    '<div class="exercise"><strong>Después de leer.</strong> Escribe una idea útil, una duda y una acción que aplicarías en el producto de la unidad.' + answer_lines(4) + '</div>'
                ),
            ),
            page(
                "Cierre de unidad",
                label,
                (
                    f"<p>Al cerrar {e(unit.title)}, el estudiante debe explicar cómo la historia inicial se transformó en un procedimiento revisable y en un producto concreto.</p>"
                    '<div class="grid-2">'
                    f'<div class="box theory-box"><h3>Debe poder explicar</h3>{bullets([name for name, _ in unit.concepts[:4]])}</div>'
                    f'<div class="box practice-box"><h3>Debe entregar</h3>{bullets(["Banco de ejercicios corregido", unit.product, "Conclusión con límite", "Evidencia visual o técnica"])}</div>'
                    '</div>'
                ),
            ),
        ]
    )
    return pages


def appendix_pages(manual: int, data: dict[str, object], visuals: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    label = f"Manual {manual} / Cierre semestre 1"
    units: list[Unit] = data["units"]  # type: ignore[assignment]
    tri = ["Trimestre 1", "Trimestre 2", "Trimestre 3"]
    pages: list[dict[str, str]] = []
    for idx, title in enumerate(tri, start=1):
        pages.append(
            page(
                "",
                "",
                (
                    figure(visuals["sem1"]["cover"], "Cada trimestre separa avances, evidencias y correcciones.", "full", f"M{manual}-tri-{idx}")
                    + '<div class="cover-content">'
                    + '<div class="school">Colegio Nuevo Tecno</div>'
                    + '<div>'
                    + f'<h1>{e(title)}</h1>'
                    + f'<p class="lead">{e(data["title"])} · separador imprimible para seguimiento de evidencias.</p>'
                    + '</div>'
                    + '<div class="cover-meta"><div><strong>Uso</strong><br>Separar avance</div><div><strong>Entrega</strong><br>Producto y banco</div><div><strong>Revisión</strong><br>Corrección docente</div></div>'
                    + '</div>'
                ),
                "page cover",
            )
        )
    pages.extend(
        [
            page(
                "Material extra de trabajo",
                label,
                (
                    '<table><tr><th>Material</th><th>Uso</th><th>Evidencia esperada</th></tr>'
                    '<tr><td>Bitácora</td><td>Registrar decisiones, cambios y errores.</td><td>Una entrada por práctica.</td></tr>'
                    '<tr><td>Hoja de cálculo</td><td>Verificar puntajes, métricas o datos.</td><td>Tabla con fórmulas visibles.</td></tr>'
                    '<tr><td>Capturas o salidas</td><td>Documentar herramienta, código o resultado.</td><td>Imagen con fecha o explicación.</td></tr>'
                    '<tr><td>Fuentes oficiales</td><td>Contrastar instrucciones y conceptos.</td><td>URL y nota de uso.</td></tr></table>'
                ),
            ),
            page(
                "Lecturas complementarias",
                label,
                bullets(data["readings"]),  # type: ignore[arg-type]
            ),
            page(
                "Bibliografía y recursos oficiales",
                label,
                '<table class="large-table"><tr><th>Recurso</th><th>Uso sugerido</th><th>Enlace</th></tr>'
                + "".join(
                    f'<tr><td>{e(name)}</td><td>{e(use)}</td><td><a href="{e(url)}">{e(url)}</a></td></tr>'
                    for name, use, url in data["links"]  # type: ignore[index]
                )
                + "</table>",
            ),
            page(
                "Glosario esencial 1",
                label,
                '<table><tr><th>Término</th><th>Uso dentro del manual</th></tr>'
                + "".join(f"<tr><td>{e(term)}</td><td>{e(desc)}</td></tr>" for term, desc in data["glossary"][:6])  # type: ignore[index]
                + "</table>",
            ),
            page(
                "Glosario esencial 2",
                label,
                '<table><tr><th>Término</th><th>Uso dentro del manual</th></tr>'
                + "".join(f"<tr><td>{e(term)}</td><td>{e(desc)}</td></tr>" for term, desc in data["glossary"][6:])  # type: ignore[index]
                + "</table>",
            ),
            page(
                "Evaluación integradora 1",
                label,
                (
                    f"<p>La evaluación retoma el caso conductor: {e(data['case'])}. El estudiante debe demostrar que comprende modelos y que puede producir evidencia.</p>"
                    '<div class="exercise"><strong>1.</strong> Selecciona una unidad y escribe el problema en formato dato, criterio, procedimiento y evidencia.' + answer_lines(4) + '</div>'
                    '<div class="exercise"><strong>2.</strong> Usa un modelo de esa unidad y muestra sustitución, escala o criterios de evaluación.' + operations(3) + '</div>'
                    '<div class="exercise"><strong>3.</strong> Explica qué parte del resultado requiere verificación externa.' + answer_lines(3) + '</div>'
                ),
            ),
            page(
                "Evaluación integradora 2",
                label,
                (
                    '<div class="exercise"><strong>4.</strong> Compara dos productos de unidades distintas y decide cuál tiene evidencia más fuerte.' + answer_lines(4) + '</div>'
                    '<div class="exercise"><strong>5.</strong> Diseña una mejora para el producto final del semestre sin introducir una herramienta nueva.' + answer_lines(4) + '</div>'
                    '<div class="exercise"><strong>6.</strong> Presenta una conclusión técnica en 90 palabras: hecho, inferencia, límite y siguiente acción.' + answer_lines(5) + '</div>'
                ),
            ),
            page(
                "Índice analítico 1",
                label,
                '<table><tr><th>Entrada</th><th>Unidad</th><th>Uso</th></tr>'
                + "".join(f"<tr><td>{e(name)}</td><td>{e(unit.id.upper())}</td><td>{e(unit.title)}</td></tr>" for unit in units for name, _ in unit.concepts[:2])
                + "</table>",
            ),
            page(
                "Índice analítico 2",
                label,
                '<table><tr><th>Modelo o criterio</th><th>Unidad</th><th>Dónde se aplica</th></tr>'
                + "".join(f"<tr><td>{e(unit.models[0].expr)}</td><td>{e(unit.id.upper())}</td><td>Ejemplo resuelto y banco de ejercicios.</td></tr>" for unit in units)
                + "</table>",
            ),
            page(
                "Plantilla de reporte final",
                label,
                (
                    '<table><tr><th>Sección</th><th>Contenido obligatorio</th><th>Extensión</th></tr>'
                    '<tr><td>Problema</td><td>Pregunta verificable del caso.</td><td>3 a 5 líneas</td></tr>'
                    '<tr><td>Datos o criterios</td><td>Tabla con unidades, escala o fuente.</td><td>1 tabla</td></tr>'
                    '<tr><td>Procedimiento</td><td>Pasos numerados y modelo usado.</td><td>6 a 10 pasos</td></tr>'
                    '<tr><td>Evidencia</td><td>Cálculo, salida, tabla, imagen, código o rúbrica.</td><td>1 evidencia principal</td></tr>'
                    '<tr><td>Conclusión</td><td>Hecho, inferencia, límite y acción.</td><td>80 a 100 palabras</td></tr></table>'
                ),
            ),
            page(
                "Lista de verificación antes de imprimir",
                label,
                (
                    '<div class="exercise"><strong>1.</strong> Revisa que cada imagen tenga texto legible en hoja carta.' + answer_lines(1) + '</div>'
                    '<div class="exercise"><strong>2.</strong> Confirma que cada banco use los modelos explicados antes.' + answer_lines(1) + '</div>'
                    '<div class="exercise"><strong>3.</strong> Verifica que las instrucciones digan qué entregar.' + answer_lines(1) + '</div>'
                    '<div class="exercise"><strong>4.</strong> Marca fuentes, enlaces y recursos que se usarán en clase.' + answer_lines(1) + '</div>'
                ),
            ),
        ]
    )
    return pages


def build_manual(manual: int, data: dict[str, object]) -> tuple[Path, dict[str, int]]:
    visuals = make_visuals(manual, data)
    pages: list[dict[str, str]] = []
    pages.extend(front_pages(manual, data, visuals))
    for unit in data["units"]:  # type: ignore[index]
        assert isinstance(unit, Unit)
        pages.extend(unit_pages(manual, unit, visuals))
    pages.extend(appendix_pages(manual, data, visuals))
    out_dir = MANUALES / f"manual-{manual}" / "semestre-1"
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = str(data["slug"])
    out = out_dir / f"manual-{manual}-{slug}-semestre-1-reintento.html"
    out.write_text(render_html(f"Manual {manual} - {data['title']} - Semestre 1", pages, f"Manual {manual}"), encoding="utf-8", newline="\n")
    stats = verify_html(out)
    return out, stats


def verify_html(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    pages = len(re.findall(r'<section class="[^"]*\bpage\b', text))
    images = re.findall(r'<img src="([^"]+)"', text)
    broken = 0
    for src in images:
        if src.startswith("http"):
            continue
        if not (path.parent / src).resolve().exists():
            broken += 1
    return {
        "pages": pages,
        "images": len(images),
        "brokenImages": broken,
        "links": len(re.findall(r'<a href="', text)),
        "chars": len(re.sub(r"<[^>]+>", " ", text)),
    }


def make_index(results: dict[int, tuple[Path, dict[str, int]]]) -> Path:
    rows = []
    for manual, (path, stats) in results.items():
        rel = path.relative_to(MANUALES).as_posix()
        rows.append(
            "<tr>"
            f"<td>Manual {manual}</td>"
            f"<td>{e(DATA[manual]['title'])}</td>"
            f"<td>{stats['pages']}</td>"
            f"<td>{stats['images']}</td>"
            f"<td>{stats['links']}</td>"
            f"<td>{stats['brokenImages']}</td>"
            f'<td><a href="{e(rel)}">Abrir HTML</a></td>'
            "</tr>"
        )
    body = (
        '<section class="page">'
        '<p class="kicker">Colegio Nuevo Tecno</p>'
        '<h2>Manuales restantes · Semestre 1 · Versión reintento</h2>'
        '<p>Índice de revisión para Manual 3, Manual 4 y Manual 5. Cada archivo conserva imágenes grandes en SVG, explicación posterior de infografías, ejemplo resuelto y banco variado alineado a modelos.</p>'
        '<table><tr><th>Manual</th><th>Título</th><th>Páginas</th><th>Imágenes</th><th>Links</th><th>Rotas</th><th>Archivo</th></tr>'
        + "".join(rows)
        + "</table>"
        '<div class="footer"><span>Serie Albatros</span><span>Revisión de manuales restantes</span></div>'
        "</section>"
    )
    out = MANUALES / "manuales-restantes-semestre-1-reintento-index.html"
    out.write_text(
        "<!doctype html><html lang=\"es\"><head><meta charset=\"utf-8\"><title>Manuales restantes</title>"
        f"<style>{CSS}</style></head><body>{body}</body></html>",
        encoding="utf-8",
        newline="\n",
    )
    return out


def write_report(results: dict[int, tuple[Path, dict[str, int]]], index: Path) -> Path:
    DOCS.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Reporte - Manuales restantes semestre 1 reintento",
        "",
        "Reglas aplicadas:",
        "- Portada completa para hoja carta con Colegio Nuevo Tecno.",
        "- Temario completo al inicio y desglose por unidad.",
        "- Infografías SVG con texto grande, sin marcos que reduzcan lectura.",
        "- Explicación posterior de cada infografía principal.",
        "- Conceptos antes de actividades, sin pedir cálculo o investigación no explicada.",
        "- Ejemplo completamente resuelto antes del banco.",
        "- Banco de 20 ejercicios por unidad con variedad: cálculo, tabla, relación de columnas, explicación, decisión y verificación.",
        "- Manual 5 incluye páginas de código completo, explicación, comprobación y mini actividad.",
        "",
        "| Manual | Archivo | Páginas | Imágenes | Links | Imágenes rotas |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for manual, (path, stats) in results.items():
        lines.append(
            f"| M{manual} | `{path.relative_to(ROOT).as_posix()}` | {stats['pages']} | {stats['images']} | {stats['links']} | {stats['brokenImages']} |"
        )
    lines.extend(["", f"Índice: `{index.relative_to(ROOT).as_posix()}`", ""])
    out = DOCS / "REPORTE_MANUALES_3_5_SEM1_REINTENTO.md"
    out.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return out


def ml(expr: str, use: str, elements: str) -> ModelLine:
    return ModelLine(expr, use, elements)


DATA: dict[int, dict[str, object]] = {
    3: {
        "slug": "ia-basica",
        "title": "Inteligencia Artificial Básica",
        "subtitle": "Alfabetización en IA generativa para construir un tutor personal",
        "case": "Mi tutor IA personal",
        "story": "El semestre construye un tutor IA por capas: comprender qué es la IA, conversar con asistentes, diseñar instrucciones claras, usar medios multimodales y estudiar con fuentes verificables.",
        "readings": [
            "Turing, Dartmouth y el origen de la pregunta por máquinas inteligentes.",
            "Modelos fundacionales, lenguaje natural y límites de los asistentes conversacionales.",
            "Evaluación de respuestas generadas con evidencia y rúbricas.",
            "Uso responsable de IA para estudiar sin sustituir el criterio propio.",
        ],
        "links": [
            ("NIST AI Risk Management Framework", "Gestión de riesgo y uso responsable de IA.", "https://www.nist.gov/itl/ai-risk-management-framework"),
            ("OpenAI API Reference", "Referencia oficial para APIs, streaming y uso de modelos.", "https://platform.openai.com/docs/api-reference"),
            ("Anthropic Docs", "Documentación oficial de Claude y herramientas asociadas.", "https://docs.anthropic.com/"),
            ("Google AI", "Panorama oficial de herramientas e investigación de IA de Google.", "https://ai.google/"),
        ],
        "glossary": [
            ("IA", "Sistema que realiza tareas asociadas con percepción, lenguaje, decisión o generación."),
            ("Modelo", "Sistema entrenado para producir predicciones, clasificaciones o respuestas."),
            ("Entrenamiento", "Proceso de ajuste a partir de datos y objetivos."),
            ("Contexto", "Información disponible para guiar una respuesta."),
            ("Token", "Unidad de texto procesada por un modelo de lenguaje."),
            ("Prompt", "Instrucción que guía la salida de un modelo."),
            ("Alucinación", "Respuesta plausible que no está verificada por evidencia."),
            ("Sesgo", "Patrón de error o preferencia causado por datos, diseño o uso."),
            ("Multimodal", "Capacidad de trabajar con texto, imagen, audio, video o documentos."),
            ("Fuente", "Documento, enlace o evidencia consultable para verificar una afirmación."),
        ],
        "units": [
            Unit(
                "u01",
                "Fundamentos e Historia de la IA",
                "Antes de construir el tutor, el equipo entiende qué hace posible a la IA y qué límites conserva.",
                "La historia de la inteligencia artificial no avanza como una línea recta. Pasa por preguntas filosóficas, laboratorios universitarios, inviernos de baja inversión, redes neuronales que resurgen con datos masivos y modelos generativos capaces de producir lenguaje. Esta historia ayuda a no tratar la IA como magia ni como amenaza inevitable.",
                "La IA se parece a un estudiante entrenado con muchos ejemplos: puede reconocer patrones, pero necesita una consigna clara y una revisión externa.",
                ["¿Qué significa que una máquina aprenda?", "¿Por qué un modelo no entiende como una persona?", "¿Qué cambió cuando aparecieron datos masivos?", "¿Qué evidencia necesitas antes de confiar en una respuesta?"],
                ["Definiciones operativas de IA", "Turing, Dartmouth e inviernos de IA", "Machine learning, deep learning y modelos fundacionales", "Cómo aprende un modelo sin entrar en matemáticas pesadas", "Limitaciones: error, sesgo y alucinación", "Primera evaluación de una respuesta generada"],
                [("IA", "Sistema que usa datos y reglas aprendidas para producir salidas útiles en una tarea."), ("Machine learning", "Forma de IA que aprende patrones a partir de ejemplos."), ("Deep learning", "Aprendizaje con redes de muchas capas que detectan representaciones complejas."), ("LLM", "Modelo de lenguaje grande entrenado para trabajar con texto y contexto."), ("Evaluación", "Comparación entre salida, criterio y evidencia verificable.")],
                ["Problema: definir qué hará el tutor y qué no debe prometer.", "Historia: ubicar hitos para evitar ideas mágicas o exageradas.", "Modelo: separar IA, ML, DL y LLM.", "Criterio: evaluar una salida con precisión y evidencia.", "Práctica: construir una línea de tiempo comentada.", "Evidencia: entregar una definición operativa y una rúbrica breve."],
                [ml("precisión = aciertos / total", "Evaluar respuestas simples del tutor.", "Aciertos y total son conteos; el resultado va de 0 a 1 o 0% a 100%."), ml("riesgo = probabilidad x impacto", "Priorizar fallas posibles de una respuesta.", "Probabilidad e impacto se califican de 1 a 5."), ml("salida = modelo(entrada + contexto)", "Entender el funcionamiento conceptual de un LLM.", "Entrada: instrucción; contexto: datos disponibles; salida: respuesta."), ml("confianza = evidencia + coherencia + límite", "Decidir si una respuesta se puede usar.", "Cada componente se puntúa de 1 a 4."), ml("mejora = puntaje final - puntaje inicial", "Medir si una segunda versión fue mejor.", "Puntajes en la misma escala.")],
                "El tutor responde una explicación sobre qué es IA, pero mezcla machine learning con ciencia ficción. Evalúa la respuesta y decide si puede usarse en clase.",
                ["La respuesta tiene 8 afirmaciones revisables.", "5 afirmaciones son correctas, 2 son ambiguas y 1 no tiene evidencia.", "La coherencia se califica con 3 de 4.", "El límite declarado recibe 2 de 4."],
                ["Se calcula precisión = 5 / 8 = 0.625, equivalente a 62.5%.", "Se identifica riesgo: probabilidad 3 e impacto 4, por lo tanto riesgo = 12.", "Se calcula confianza: evidencia 2 + coherencia 3 + límite 2 = 7 de 12.", "Se redacta una decisión: la respuesta sirve como borrador, pero no como explicación final.", "Se corrige pidiendo fuentes, ejemplos y separación entre IA, ML y DL."],
                "La respuesta no se descarta por completo, pero exige corrección. El producto final debe incluir línea de tiempo y definición operativa con límites explícitos.",
                "Línea de tiempo comentada y definición operativa del tutor IA.",
                "Evaluar una respuesta generada, corregirla y convertirla en una explicación verificable.",
                "Lee una nota histórica sobre Turing o Dartmouth y escribe qué pregunta sigue vigente al usar asistentes actuales.",
            ),
            Unit(
                "u02",
                "Tu Primer Asistente Conversacional",
                "El equipo compara asistentes para elegir la base del tutor IA personal.",
                "Los asistentes conversacionales hicieron que la IA dejara de sentirse reservada para laboratorios. Sin embargo, una conversación útil no depende solo del modelo: también depende del contexto, de la memoria disponible, de la forma de preguntar y de la verificación posterior.",
                "Un asistente conversacional es como entrevistar a una persona muy rápida: puede responder mucho, pero la calidad de la entrevista depende de tus preguntas.",
                ["¿Qué información mínima necesita el asistente?", "¿Qué datos personales no deben compartirse?", "¿Cómo detectas una respuesta débil?", "¿Cómo comparas dos herramientas sin dejarte llevar por apariencia?"],
                ["Anatomía de un chat", "Tokens, contexto y memoria", "Comparación entre asistentes", "Limitaciones y fecha de corte", "Verificación con fuentes", "Primera conversación útil del tutor"],
                [("Token", "Unidad de texto que el sistema procesa para leer o generar respuestas."), ("Contexto", "Información que el asistente puede usar durante la conversación."), ("Memoria", "Persistencia de datos entre interacciones, cuando la herramienta lo permite."), ("Verificación", "Proceso de contrastar afirmaciones con evidencia externa."), ("Privacidad", "Criterio para decidir qué información no debe enviarse a una herramienta.")],
                ["Problema: elegir un asistente para estudiar una materia.", "Entrada: escribir tarea, contexto, formato y límites.", "Comparación: probar la misma instrucción en dos asistentes.", "Verificación: revisar afirmaciones con fuente o criterio.", "Decisión: elegir herramienta según evidencia, no moda.", "Evidencia: tabla comparativa con corrección de respuesta."],
                [ml("costo estimado = tokens x tarifa", "Comprender consumo cuando una herramienta cobra por uso.", "Tokens como conteo; tarifa en costo por token o por millón de tokens."), ml("tasa de verificación = afirmaciones comprobadas / afirmaciones totales", "Medir qué tanto se pudo verificar una respuesta.", "Conteos; resultado de 0 a 1 o porcentaje."), ml("utilidad = claridad + contexto + verificabilidad", "Comparar dos respuestas con rúbrica.", "Cada criterio se califica de 1 a 4."), ml("privacidad = sensibilidad x exposición", "Valorar riesgo de compartir datos.", "Sensibilidad y exposición se puntúan de 1 a 5."), ml("mejora = respuesta revisada - respuesta inicial", "Medir iteración de conversación.", "Puntajes en escala común.")],
                "Dos asistentes responden a la misma pregunta de biología. El primero es claro pero no cita fuentes; el segundo es más largo y verificable. Decide cuál usar para el tutor.",
                ["Respuesta A: claridad 4, contexto 2, verificabilidad 1.", "Respuesta B: claridad 3, contexto 3, verificabilidad 4.", "Respuesta A tiene 6 afirmaciones y se comprueban 2.", "Respuesta B tiene 7 afirmaciones y se comprueban 5."],
                ["Utilidad A = 4 + 2 + 1 = 7.", "Utilidad B = 3 + 3 + 4 = 10.", "Tasa A = 2 / 6 = 0.333.", "Tasa B = 5 / 7 = 0.714.", "Se elige B para estudiar, aunque se resume para hacerlo más claro."],
                "La mejor respuesta no siempre es la más breve. Para el tutor se elige la que permita verificar más afirmaciones y luego se mejora su claridad.",
                "Tabla comparativa de asistentes y conversación inicial corregida.",
                "Ejecutar la misma tarea en dos asistentes, puntuar respuestas y justificar la elección.",
                "Lee una guía de uso de un asistente conversacional y localiza qué dice sobre privacidad, memoria o datos sensibles.",
            ),
            Unit(
                "u03",
                "Prompt Engineering Fundamental",
                "El tutor mejora cuando las instrucciones dejan de ser vagas.",
                "Diseñar instrucciones efectivas no es escribir frases largas. Es definir rol, tarea, contexto, formato, criterio de calidad y restricciones. La historia de esta unidad muestra cómo una petición confusa produce respuestas genéricas y cómo la iteración convierte una idea en una salida revisable.",
                "Un prompt es como una orden de trabajo: si no dice producto, alcance y criterio, cada persona imagina algo distinto.",
                ["¿Qué debe incluir una instrucción clara?", "¿Cuándo conviene dar ejemplos?", "¿Qué diferencia hay entre mejorar y repetir?", "¿Qué antipatrones hacen fallar una respuesta?"],
                ["Rol, tarea, contexto y formato", "Zero-shot y few-shot", "Estructura de salida", "Iteración y comparación", "Antipatrones frecuentes", "Banco de instrucciones personales"],
                [("Rol", "Papel que se asigna al modelo para orientar tono, nivel y perspectiva."), ("Tarea", "Acción concreta que debe realizarse."), ("Contexto", "Información que reduce ambigüedad."), ("Formato", "Estructura visible de la salida esperada."), ("Criterio", "Regla para decidir si la salida funciona.")],
                ["Problema: una instrucción vaga genera una respuesta genérica.", "Despiece: identificar rol, tarea, contexto, formato y criterio.", "Primera versión: pedir una salida simple.", "Evaluación: usar rúbrica para detectar fallas.", "Iteración: corregir una sola variable por vez.", "Evidencia: banco de instrucciones con comparación."],
                [ml("prompt = rol + tarea + contexto + formato + criterio", "Construir una instrucción completa.", "Cada componente se redacta en lenguaje claro."), ml("puntaje = contenido + formato + evidencia + seguridad", "Evaluar una salida generada.", "Cada criterio se califica de 1 a 4."), ml("delta = puntaje v2 - puntaje v1", "Medir mejora entre iteraciones.", "Puntajes en la misma escala."), ml("ambigüedad = partes faltantes / partes requeridas", "Diagnosticar una instrucción incompleta.", "Partes requeridas: rol, tarea, contexto, formato, criterio."), ml("calidad final = utilidad x verificabilidad", "Evitar respuestas bonitas pero no comprobables.", "Utilidad y verificabilidad en escala 1 a 4.")],
                "Una instrucción inicial dice: 'Explícame fotosíntesis'. Debes convertirla en una instrucción completa para el tutor y evaluar la mejora.",
                ["Versión 1 obtiene contenido 2, formato 1, evidencia 1, seguridad 3.", "Versión 2 incluye rol docente, público bachillerato, tabla, ejemplo y criterio.", "Versión 2 obtiene contenido 4, formato 4, evidencia 3, seguridad 4.", "Se requieren 5 partes en el prompt completo."],
                ["Puntaje v1 = 2 + 1 + 1 + 3 = 6.", "Puntaje v2 = 4 + 4 + 3 + 4 = 15.", "Delta = 15 - 6 = 9.", "Ambigüedad v1 = 4 / 5 = 0.8 porque solo tenía tarea.", "Se redacta conclusión: la mejora vino de contexto, formato y criterio."],
                "La versión corregida no es más útil por ser más larga, sino porque define salida, audiencia y criterio de revisión.",
                "Banco de 20 instrucciones personales para estudiar.",
                "Diseñar, probar, puntuar e iterar instrucciones con una rúbrica visible.",
                "Lee una recomendación oficial de documentación de IA sobre instrucciones o estructura de salida y tradúcela a una regla para clase.",
            ),
            Unit(
                "u04",
                "IA Generativa Multimodal",
                "El tutor cobra voz, imagen, video y lectura de documentos.",
                "La IA generativa dejó de operar solo con texto. Ahora puede analizar imágenes, producir audio, transformar documentos y apoyar videos educativos. La precisión consiste en elegir el medio correcto y verificar que la salida no invente información ni oculte fuentes.",
                "La multimodalidad es como cambiar de pizarrón: a veces texto alcanza, a veces una imagen o una voz reduce diez párrafos.",
                ["¿Cuándo conviene una imagen en vez de texto?", "¿Qué debe verificarse en un audio o video?", "¿Qué riesgo tiene una imagen falsa?", "¿Cómo decides el medio adecuado para enseñar?"],
                ["Texto, imagen, audio y video", "Instrucciones visuales", "Guion breve", "Verificación multimodal", "Riesgos de deepfake", "Cápsula educativa del tutor"],
                [("Modalidad", "Tipo de entrada o salida: texto, imagen, audio, video o documento."), ("Guion", "Secuencia de ideas para producir audio o video."), ("Restricción", "Límite que evita resultados imprecisos o inseguros."), ("Verificación visual", "Revisión de coherencia, legibilidad y correspondencia con el tema."), ("Consentimiento", "Condición ética para usar voz, rostro o datos personales.")],
                ["Problema: explicar un tema con un solo medio no siempre funciona.", "Selección: elegir texto, imagen, audio o video según objetivo.", "Diseño: escribir guion o instrucción visual.", "Producción: generar o editar una salida.", "Verificación: revisar legibilidad, coherencia y ética.", "Evidencia: cápsula educativa corta."],
                [ml("duración = escenas x segundos", "Planear un video breve.", "Escenas como conteo; segundos en s."), ml("calidad visual = legibilidad + coherencia + pertinencia", "Evaluar una imagen educativa.", "Cada criterio se califica de 1 a 4."), ml("riesgo = impacto x probabilidad", "Valorar un uso de voz, rostro o video.", "Escala 1 a 5 para cada componente."), ml("cobertura = conceptos incluidos / conceptos requeridos", "Revisar si la cápsula cubre el tema.", "Conteos; resultado en porcentaje."), ml("tiempo total = guion + producción + revisión", "Planear una práctica realista.", "Tiempo en minutos.")],
                "El tutor debe producir una cápsula de 60 segundos sobre caída libre. Diseña 4 escenas y evalúa si la imagen principal es legible.",
                ["4 escenas de 15 segundos.", "La imagen obtiene legibilidad 3, coherencia 4 y pertinencia 4.", "Se requieren 5 conceptos y aparecen 4.", "Riesgo ético: impacto 2, probabilidad 2."],
                ["Duración = 4 x 15 = 60 s.", "Calidad visual = 3 + 4 + 4 = 11 de 12.", "Cobertura = 4 / 5 = 80%.", "Riesgo = 2 x 2 = 4, bajo pero debe revisarse.", "Se decide agregar el concepto faltante antes de entregar."],
                "La cápsula puede usarse si se agrega el concepto faltante y se conserva la revisión de legibilidad.",
                "Cápsula educativa multimedia de 60 segundos.",
                "Diseñar guion, imagen, audio o video y revisar cobertura, legibilidad y riesgo.",
                "Lee una política de uso responsable de imágenes o voz sintética y resume dos condiciones éticas aplicables al aula.",
            ),
            Unit(
                "u05",
                "IA para Estudio e Investigación",
                "El tutor estudia un PDF contigo sin inventar citas.",
                "Investigar con IA no significa aceptar resúmenes automáticos. Significa preguntar mejor, comparar fuentes, verificar citas y distinguir idea central, evidencia y opinión. El tutor se vuelve útil cuando trabaja con documentos revisables.",
                "La IA para investigar es como un asistente de biblioteca: encuentra rutas, pero no reemplaza leer la fuente crítica.",
                ["¿Qué hace confiable una fuente?", "¿Cómo detectas una cita inventada?", "¿Qué diferencia hay entre resumen y evidencia?", "¿Cómo usas IA sin copiar sin entender?"],
                ["Fuentes y documentos", "Resumen con evidencia", "Mapas de lectura", "Búsqueda con citas", "Citación y uso responsable", "Notebook de estudio"],
                [("Fuente", "Documento o sitio que permite verificar una afirmación."), ("Cita", "Referencia a una parte concreta de una fuente."), ("Resumen", "Reducción de ideas sin cambiar el sentido."), ("Evidencia", "Dato o fragmento que sostiene una afirmación."), ("Paráfrasis", "Explicación propia de una idea consultada.")],
                ["Problema: estudiar rápido puede producir comprensión superficial.", "Selección: elegir fuente confiable.", "Lectura: separar idea, dato y límite.", "Síntesis: construir resumen o mapa.", "Verificación: comprobar citas y afirmaciones.", "Evidencia: notebook de estudio con fuentes."],
                [ml("confiabilidad = autoridad + actualidad + evidencia", "Evaluar una fuente.", "Cada criterio se puntúa de 1 a 4."), ml("cobertura = fuentes usadas / fuentes requeridas", "Revisar si una investigación es suficiente.", "Conteos; resultado como porcentaje."), ml("densidad = ideas clave / páginas", "Medir concentración de ideas en una lectura.", "Ideas como conteo; páginas como conteo."), ml("verificación = citas correctas / citas totales", "Detectar citas dudosas.", "Conteos; resultado de 0 a 1."), ml("síntesis = idea central + datos + límite", "Construir resumen útil.", "Estructura textual obligatoria.")],
                "El tutor resume un PDF de 10 páginas con 6 citas. Debes evaluar si el resumen puede usarse para estudiar.",
                ["La fuente tiene autoridad 4, actualidad 3 y evidencia 4.", "Se requerían 3 fuentes y se usaron 2.", "De 6 citas, 5 son correctas.", "El resumen contiene 8 ideas clave en 10 páginas."],
                ["Confiabilidad = 4 + 3 + 4 = 11 de 12.", "Cobertura = 2 / 3 = 66.7%.", "Verificación = 5 / 6 = 83.3%.", "Densidad = 8 / 10 = 0.8 ideas por página.", "Se decide usar el resumen como apoyo, pero buscar una tercera fuente."],
                "El resumen es útil, aunque incompleto. La decisión correcta es conservarlo como apoyo y completar cobertura con otra fuente.",
                "Notebook de estudio con fuentes, resumen, mapa y verificación.",
                "Analizar un documento, crear resumen verificable y construir mapa de estudio.",
                "Lee una guía de citación académica y escribe cómo mencionarías apoyo de IA sin sustituir la fuente original.",
            ),
        ],
    },
    4: {
        "slug": "ia-avanzada",
        "title": "Inteligencia Artificial Avanzada",
        "subtitle": "Especificaciones, artifacts, RAG, agentes básicos y workflows institucionales",
        "case": "Asistente Institucional Albatros",
        "story": "El semestre diseña un asistente institucional por capas: instrucciones versionadas, especificaciones, artifacts, base de conocimiento y automatizaciones no-code con control de riesgo.",
        "readings": [
            "De instrucción simple a sistema versionado de trabajo con IA.",
            "Especificaciones como puente entre idea, alcance y ejecución.",
            "RAG como forma de responder con documentos y trazabilidad.",
            "Automatización no-code con controles, aprobaciones y bitácora.",
        ],
        "links": [
            ("OpenAI API Reference", "Referencia oficial para APIs y uso de modelos.", "https://platform.openai.com/docs/api-reference"),
            ("Anthropic Docs", "Documentación oficial de Claude.", "https://docs.anthropic.com/"),
            ("Model Context Protocol", "Documentación oficial del protocolo MCP.", "https://modelcontextprotocol.io/"),
            ("n8n Docs", "Documentación oficial para workflows e integraciones.", "https://docs.n8n.io/"),
            ("Power Automate", "Documentación oficial de automatización de Microsoft.", "https://learn.microsoft.com/power-automate/"),
        ],
        "glossary": [
            ("Prompt avanzado", "Instrucción estructurada, evaluable y versionada."),
            ("Schema", "Estructura esperada de una salida, como JSON o tabla."),
            ("PRD", "Documento de requisitos de producto."),
            ("Definition of Done", "Criterios que indican que una tarea está terminada."),
            ("Artifact", "Salida editable, interactiva o reutilizable generada con IA."),
            ("Canvas", "Espacio de trabajo para editar e iterar contenido."),
            ("RAG", "Generación aumentada por recuperación de fuentes."),
            ("Embedding", "Representación numérica de significado."),
            ("Workflow", "Secuencia automatizada de pasos con disparadores y acciones."),
            ("Webhook", "Evento que envía datos de una herramienta a otra."),
        ],
        "units": [
            Unit(
                "u01",
                "Prompt Engineering Avanzado",
                "El equipo crea instrucciones versionadas para todo el asistente institucional.",
                "Cuando una institución usa IA, las instrucciones dejan de ser ocurrencias individuales y se convierten en activos de trabajo. Una instrucción avanzada debe delimitar contexto, salida, seguridad, pruebas y cambios de versión.",
                "Un prompt avanzado se parece a un protocolo de laboratorio: una línea mal definida puede cambiar todo el resultado.",
                ["¿Qué parte de una instrucción debe versionarse?", "¿Cuándo conviene usar delimitadores?", "¿Qué salida debe tener esquema?", "¿Cómo comparas dos versiones sin opinión?"],
                ["Delimitadores y estructura", "Meta-instrucciones", "Salida restringida", "Rúbricas y pruebas A/B", "Consistencia y seguridad", "Repositorio de instrucciones"],
                [("Delimitador", "Marca que separa instrucciones, contexto y datos."), ("Schema", "Forma obligatoria de la salida esperada."), ("Versión", "Registro de cambios entre instrucciones."), ("Prueba A/B", "Comparación controlada entre dos variantes."), ("Seguridad", "Restricciones para evitar datos sensibles o acciones riesgosas.")],
                ["Problema: los equipos improvisan instrucciones distintas.", "Estructura: separar rol, tarea, contexto y salida.", "Restricción: definir esquema y límites.", "Prueba: comparar dos versiones.", "Registro: guardar cambios y resultados.", "Evidencia: repositorio de instrucciones con rúbrica."],
                [ml("score = exactitud + formato + utilidad + seguridad", "Evaluar una instrucción avanzada.", "Cada criterio se califica de 1 a 5."), ml("cumplimiento = campos correctos / campos requeridos", "Medir salida con schema.", "Conteos; resultado porcentual."), ml("estabilidad = respuestas válidas / pruebas totales", "Comprobar consistencia.", "Conteos en la misma batería de pruebas."), ml("mejora = score B - score A", "Comparar dos versiones.", "Puntajes en escala común."), ml("riesgo = impacto x probabilidad", "Priorizar restricciones.", "Escala 1 a 5.")],
                "Dos versiones de una instrucción generan reportes institucionales. La versión A es clara pero no cumple JSON; la versión B cumple estructura y reduce riesgo.",
                ["A: exactitud 4, formato 2, utilidad 4, seguridad 3.", "B: exactitud 4, formato 5, utilidad 4, seguridad 5.", "B requiere 6 campos y entrega 5 correctos.", "Se hacen 10 pruebas y 8 son válidas."],
                ["Score A = 4 + 2 + 4 + 3 = 13.", "Score B = 4 + 5 + 4 + 5 = 18.", "Mejora = 18 - 13 = 5.", "Cumplimiento B = 5 / 6 = 83.3%.", "Estabilidad = 8 / 10 = 80%."],
                "La versión B se adopta como base, pero debe corregir el campo faltante antes de publicarse.",
                "Repositorio de instrucciones institucionales con versión y rúbrica.",
                "Diseñar dos versiones, probarlas con la misma tarea y justificar cuál queda vigente.",
                "Lee una documentación oficial sobre salidas estructuradas o buenas prácticas y convierte una recomendación en regla de equipo.",
            ),
            Unit(
                "u02",
                "Especificaciones de Tareas y Proyectos",
                "El asistente institucional necesita un PRD antes de operar.",
                "Muchos errores atribuidos a la IA nacen antes de usarla: objetivos vagos, alcance indefinido, criterios invisibles o riesgos ignorados. Una especificación convierte una idea en un contrato de trabajo revisable.",
                "Una especificación es como un plano: no construye sola, pero evita que todos imaginen edificios distintos.",
                ["¿Quién es el usuario principal?", "¿Qué queda fuera del alcance?", "¿Cómo se define terminado?", "¿Qué riesgo debe controlarse primero?"],
                ["PRD asistido por IA", "Brief y alcance", "Definition of Done", "Criterios de aceptación", "Trade-offs", "Especificación por capas"],
                [("Usuario", "Persona o grupo que usará la solución."), ("Alcance", "Límites de lo que se incluye y excluye."), ("DoD", "Criterios para considerar terminada una tarea."), ("Trade-off", "Decisión entre beneficios y costos."), ("Riesgo", "Evento posible que afecta calidad, costo o seguridad.")],
                ["Problema: una solicitud institucional es ambigua.", "Usuario: definir quién recibe valor.", "Alcance: separar incluido y excluido.", "Criterios: escribir aceptación y DoD.", "Riesgo: priorizar controles.", "Evidencia: PRD de una función del asistente."],
                [ml("DoD = criterios cumplidos / criterios totales", "Medir avance real.", "Conteos; resultado porcentual."), ml("prioridad = impacto / esfuerzo", "Ordenar tareas.", "Impacto y esfuerzo en escala 1 a 5."), ml("riesgo = impacto x probabilidad", "Priorizar controles.", "Escala 1 a 5."), ml("alcance = objetivo + límites + entregables", "Definir proyecto.", "Texto verificable."), ml("calidad = claridad + completitud + trazabilidad", "Evaluar especificación.", "Cada criterio de 1 a 4.")],
                "La dirección pide: 'hacer un asistente para alumnos'. Debes convertir la frase en una especificación mínima y priorizar una función.",
                ["Hay 8 criterios de DoD y se cumplen 5.", "Impacto de responder dudas frecuentes: 5.", "Esfuerzo estimado: 2.", "Riesgo de datos personales: impacto 5, probabilidad 3."],
                ["DoD = 5 / 8 = 62.5%.", "Prioridad = 5 / 2 = 2.5.", "Riesgo = 5 x 3 = 15, alto.", "Se limita alcance: responder dudas generales sin datos sensibles.", "Se define entregable: FAQ institucional con fuentes."],
                "La especificación aún no está lista para implementación completa, pero sí para un prototipo controlado de preguntas frecuentes.",
                "PRD completo de una función del asistente institucional.",
                "Transformar una solicitud ambigua en alcance, criterios, riesgo y entregable.",
                "Lee una plantilla de PRD o criterios de aceptación y adapta sus secciones al caso escolar.",
            ),
            Unit(
                "u03",
                "Artifacts y Canvases",
                "El asistente produce un tablero editable para seguimiento institucional.",
                "Artifacts y canvases cambian la relación con la IA: la salida deja de ser solo texto y se convierte en documento, tabla, código, visualización o mini aplicación que puede revisarse, probarse y versionarse.",
                "Un artifact es como una mesa de trabajo compartida: la respuesta no queda cerrada, se puede corregir encima.",
                ["¿Qué tipo de salida conviene editar?", "¿Cómo pruebas una mini aplicación?", "¿Qué cambio debe guardarse como versión?", "¿Cómo compartes sin perder control?"],
                ["Tipos de artifacts", "Canvas como espacio de iteración", "Mini aplicaciones HTML", "Pruebas de interfaz", "Versionado", "Compartir y revisar"],
                [("Artifact", "Salida editable o interactiva generada con IA."), ("Estado", "Información que una mini aplicación conserva o muestra."), ("Prueba", "Acción para comparar salida esperada contra salida observada."), ("Versión", "Registro de cambios realizados."), ("Publicación", "Forma controlada de compartir un resultado.")],
                ["Problema: un reporte textual no basta para seguimiento.", "Diseño: elegir tablero, tabla o miniapp.", "Construcción: generar primera versión.", "Prueba: revisar datos, botones o estructura.", "Iteración: corregir una falla por vez.", "Evidencia: tablero con checklist de prueba."],
                [ml("bug = resultado esperado - resultado observado", "Describir una falla.", "Comparación textual; no es resta numérica."), ml("cobertura = pruebas aprobadas / pruebas totales", "Medir revisión.", "Conteos; resultado porcentual."), ml("versión nueva = versión anterior + cambio probado", "Controlar iteraciones.", "Versiones numeradas."), ml("usabilidad = claridad + navegación + error visible", "Evaluar miniapp.", "Cada criterio de 1 a 4."), ml("riesgo de publicación = exposición x sensibilidad", "Decidir si se comparte.", "Escala 1 a 5.")],
                "Se genera un tablero para seguimiento de solicitudes. Tiene 6 pruebas, aprueba 4 y falla al filtrar por estado.",
                ["Pruebas totales: 6.", "Pruebas aprobadas: 4.", "Claridad 3, navegación 3, error visible 2.", "Exposición 2, sensibilidad 4."],
                ["Cobertura = 4 / 6 = 66.7%.", "Usabilidad = 3 + 3 + 2 = 8 de 12.", "Riesgo publicación = 2 x 4 = 8.", "Bug: se esperaba filtrar estado; se observa lista sin cambios.", "Se crea versión 1.1 corrigiendo filtro antes de compartir."],
                "El tablero no debe publicarse todavía. Puede revisarse internamente y pasar a versión 1.1 con filtro corregido.",
                "Dashboard HTML del asistente con checklist de pruebas.",
                "Diseñar un artifact, probarlo y documentar cambios de versión.",
                "Lee una guía de accesibilidad o pruebas de interfaz y extrae dos criterios aplicables a un artifact escolar.",
            ),
            Unit(
                "u04",
                "Bases de Conocimiento y RAG",
                "El asistente responde usando el reglamento institucional como fuente.",
                "RAG surge porque un modelo general no conoce necesariamente los documentos internos. Recuperar fragmentos relevantes y usarlos como contexto permite responder con trazabilidad, aunque no elimina la necesidad de revisar fuentes.",
                "RAG es como responder con el archivo abierto al lado: no garantiza verdad automática, pero obliga a mirar la fuente.",
                ["¿Qué documento entra a la base?", "¿Qué es un fragmento o chunk?", "¿Cómo se cita una fuente?", "¿Cuándo RAG no conviene?"],
                ["Concepto de RAG", "Embeddings y vectores", "Fragmentación de documentos", "Búsqueda y recuperación", "Citas y trazabilidad", "RAG vs fine-tuning"],
                [("RAG", "Generación aumentada por recuperación de documentos."), ("Embedding", "Vector que representa significado."), ("Chunk", "Fragmento de documento usado para búsqueda."), ("Recuperación", "Selección de fragmentos relevantes."), ("Trazabilidad", "Capacidad de volver a la fuente original.")],
                ["Problema: el asistente no debe inventar reglamento.", "Documento: elegir fuente oficial.", "Fragmentación: dividir sin romper sentido.", "Búsqueda: recuperar fragmentos relevantes.", "Generación: responder citando fuente.", "Evidencia: pregunta, fragmento usado y respuesta."],
                [ml("similitud coseno = A·B / (|A| |B|)", "Comparar vectores de consulta y documento.", "A y B son vectores; resultado entre -1 y 1."), ml("cobertura = fuentes usadas / fuentes necesarias", "Revisar base documental.", "Conteos; resultado porcentual."), ml("precisión de recuperación = fragmentos útiles / fragmentos recuperados", "Evaluar búsqueda.", "Conteos."), ml("tamaño de chunk = palabras por fragmento", "Controlar fragmentación.", "Palabras o tokens como conteo."), ml("alucinación = respuestas sin fuente / respuestas totales", "Medir fallas de trazabilidad.", "Conteos; buscar valor bajo.")],
                "El asistente responde 10 preguntas del reglamento. Recupera 30 fragmentos, 21 son útiles y 2 respuestas no tienen fuente.",
                ["Fragmentos recuperados: 30.", "Fragmentos útiles: 21.", "Respuestas totales: 10.", "Respuestas sin fuente: 2.", "Se usaron 3 fuentes de 4 necesarias."],
                ["Precisión de recuperación = 21 / 30 = 70%.", "Alucinación = 2 / 10 = 20%.", "Cobertura = 3 / 4 = 75%.", "Se identifica que falta una fuente sobre becas.", "Se bloquean respuestas sin cita hasta agregar documento faltante."],
                "El prototipo funciona parcialmente. Para uso institucional debe reducir respuestas sin fuente y completar cobertura documental.",
                "Prototipo RAG sin código con preguntas, fuentes y respuestas citadas.",
                "Construir una base de conocimiento mínima y evaluar recuperación, cobertura y trazabilidad.",
                "Lee la documentación oficial de MCP o RAG de una herramienta y localiza cómo recomienda manejar fuentes.",
            ),
            Unit(
                "u05",
                "Workflows e Integraciones No-Code",
                "El asistente automatiza solicitudes con un flujo revisable.",
                "Automatizar no significa soltar decisiones sin control. Un workflow útil define disparador, validación, acción, registro y excepción. La IA puede ayudar a clasificar, redactar o resumir, pero las decisiones sensibles requieren aprobación.",
                "Un workflow es como una receta con sensores: si entra un evento, sigue pasos, pero debe saber cuándo detenerse.",
                ["¿Qué evento inicia el flujo?", "¿Qué acción requiere aprobación?", "¿Dónde se registra el error?", "¿Qué dato no debe enviarse a IA?"],
                ["Triggers y webhooks", "Validación de datos", "Acciones con IA", "Aprobaciones humanas", "Logs y errores", "Patrones reutilizables"],
                [("Trigger", "Evento que inicia el flujo."), ("Webhook", "Señal que envía datos entre herramientas."), ("Validación", "Revisión antes de ejecutar una acción."), ("Aprobación", "Intervención humana requerida."), ("Log", "Registro de lo que ocurrió.")],
                ["Problema: solicitudes repetidas consumen tiempo.", "Entrada: formulario o correo.", "Validación: revisar datos mínimos.", "Acción: clasificar, responder o asignar.", "Control: aprobación y registro.", "Evidencia: diagrama del flujo y prueba."],
                [ml("SLA = tiempo resuelto / tiempo objetivo", "Medir cumplimiento de atención.", "Tiempos en minutos u horas."), ml("éxito = flujos correctos / flujos probados", "Evaluar automatización.", "Conteos; resultado porcentual."), ml("riesgo = impacto x probabilidad", "Priorizar controles.", "Escala 1 a 5."), ml("costo operativo = pasos x costo por paso", "Estimar consumo o esfuerzo.", "Pasos como conteo; costo en moneda o tiempo."), ml("error = casos fallidos / casos totales", "Medir fallas del flujo.", "Conteos; buscar valor bajo.")],
                "Se prueba un flujo para solicitudes de constancias. De 12 casos, 9 terminan bien, 2 requieren aprobación y 1 falla por dato faltante.",
                ["Casos probados: 12.", "Casos correctos: 9.", "Casos fallidos: 1.", "Tiempo resuelto: 18 min.", "Tiempo objetivo: 20 min.", "Pasos: 6; costo por paso: 0.5 unidades."],
                ["Éxito = 9 / 12 = 75%.", "Error = 1 / 12 = 8.3%.", "SLA = 18 / 20 = 0.9, dentro del objetivo.", "Costo operativo = 6 x 0.5 = 3 unidades.", "Se agrega validación de datos antes de ejecutar respuesta."],
                "El flujo puede usarse como piloto, pero no como automatización final hasta reducir fallas y formalizar aprobaciones.",
                "Workflow no-code para solicitudes estudiantiles con diagrama, prueba y log.",
                "Diseñar un flujo con trigger, validación, acción, aprobación, error y evidencia.",
                "Lee documentación de n8n, Make o Power Automate y registra qué recomienda para errores o credenciales.",
            ),
        ],
    },
    5: {
        "slug": "ia-programacion",
        "title": "Inteligencia Artificial con Programación",
        "subtitle": "De Python al análisis de datos y estadística inicial para IA",
        "case": "Predictor de rendimiento escolar",
        "story": "El semestre convierte un dataset escolar en código, limpieza, visualizaciones y análisis estadístico. La meta no es memorizar sintaxis: es construir evidencia con datos.",
        "readings": [
            "Python como lenguaje de automatización y análisis de datos.",
            "Datos tabulares, limpieza y bitácora de transformaciones.",
            "Visualizaciones para detectar patrones antes de modelar.",
            "Estadística descriptiva para decidir con cautela.",
        ],
        "links": [
            ("Python Docs", "Referencia oficial del lenguaje Python.", "https://docs.python.org/3/"),
            ("NumPy Docs", "Documentación oficial de NumPy.", "https://numpy.org/doc/"),
            ("Pandas Docs", "Documentación oficial de pandas.", "https://pandas.pydata.org/docs/"),
            ("Matplotlib Docs", "Documentación oficial de Matplotlib.", "https://matplotlib.org/stable/contents.html"),
            ("scikit-learn User Guide", "Guía oficial para machine learning clásico.", "https://scikit-learn.org/stable/user_guide"),
        ],
        "glossary": [
            ("Variable", "Nombre que guarda un valor."),
            ("Lista", "Colección ordenada de valores."),
            ("CSV", "Archivo de texto separado por comas."),
            ("Array", "Estructura numérica usada por NumPy."),
            ("DataFrame", "Tabla con filas y columnas en pandas."),
            ("Nulo", "Dato faltante o vacío."),
            ("Histograma", "Gráfica de distribución por intervalos."),
            ("Boxplot", "Gráfica de cuartiles y posibles valores atípicos."),
            ("Media", "Promedio aritmético."),
            ("Correlación", "Medida de relación entre dos variables."),
        ],
        "units": [
            Unit(
                "u01",
                "Tu Primer Python para IA",
                "El equipo carga una lista de calificaciones y obtiene un resumen inicial.",
                "Programar para IA empieza con acciones pequeñas: guardar valores, repetir pasos, leer datos y detectar errores. Python permite convertir una lista escolar en evidencia manipulable antes de hablar de modelos.",
                "Python es como una libreta que también sabe hacer cuentas: si escribes instrucciones claras, repite el procedimiento sin cansarse.",
                ["¿Qué es una variable?", "¿Cómo se calcula un promedio?", "¿Qué error aparece si falta un dato?", "¿Por qué conviene nombrar bien los datos?"],
                ["Entorno básico", "Variables y tipos", "Condicionales", "Ciclos", "Funciones", "Lectura de datos simples"],
                [("Variable", "Nombre que guarda un valor para reutilizarlo."), ("Tipo", "Categoría del dato: número, texto, booleano o lista."), ("Condicional", "Estructura que ejecuta una acción si una condición se cumple."), ("Ciclo", "Repetición controlada sobre datos."), ("Función", "Bloque reutilizable con entrada y salida.")],
                ["Problema: cargar calificaciones sin perder datos.", "Datos: crear lista o leer archivo simple.", "Proceso: calcular conteo, suma y promedio.", "Validación: revisar valores fuera de rango.", "Salida: imprimir resumen entendible.", "Evidencia: script y resultado esperado."],
                [ml("promedio = suma / n", "Calcular media simple.", "Suma en puntos; n como conteo de datos."), ml("if condición: acción", "Tomar decisiones.", "Condición booleana; acción indentada."), ml("for dato in lista", "Recorrer datos.", "dato es elemento actual; lista es colección."), ml("error = valor esperado - valor observado", "Comparar salida.", "Misma unidad o escala."), ml("porcentaje = parte / total x 100", "Expresar proporciones.", "Parte y total como conteos.")],
                "Se tienen cinco calificaciones: 8.0, 9.5, 7.0, 10.0 y 6.5. Calcula promedio y porcentaje de aprobados.",
                ["Lista: [8.0, 9.5, 7.0, 10.0, 6.5].", "Aprobado significa calificación mayor o igual a 6.", "Total de datos: 5.", "Suma: 35.0."],
                ["Promedio = 35.0 / 5 = 7.0.", "Aprobados: 5 porque todos son >= 6.", "Porcentaje = 5 / 5 x 100 = 100%.", "Se revisa si algún valor está fuera de 0 a 10.", "La conclusión incluye que el grupo pequeño no representa a toda la escuela."],
                "El resumen inicial funciona, pero debe ampliarse con más datos antes de tomar decisiones escolares.",
                "Script que calcula resumen básico de calificaciones.",
                "Crear datos, calcular promedio, validar rango y explicar la salida.",
                "Lee la introducción de la documentación de Python y anota dos reglas sobre nombres, listas o control de flujo.",
                code='''calificaciones = [8.0, 9.5, 7.0, 10.0, 6.5]

total = len(calificaciones)
suma = sum(calificaciones)
promedio = suma / total

aprobados = 0
for calificacion in calificaciones:
    if calificacion >= 6:
        aprobados += 1

porcentaje_aprobados = aprobados / total * 100

print("Total de estudiantes:", total)
print("Promedio:", promedio)
print("Aprobados:", aprobados)
print("Porcentaje de aprobados:", porcentaje_aprobados)''',
                code_check=["Verifica que el promedio impreso sea 7.0.", "Confirma que el total de estudiantes sea 5.", "Cambia una calificación a 5.0 y observa cómo baja el porcentaje de aprobados."],
            ),
            Unit(
                "u02",
                "Datos con NumPy y Pandas",
                "El equipo limpia un dataset escolar con valores faltantes y duplicados.",
                "Los modelos aprenden de datos, pero los datos reales suelen venir incompletos, repetidos o con tipos incorrectos. NumPy ayuda con operaciones numéricas; pandas permite trabajar con tablas, columnas y transformaciones documentadas.",
                "Limpiar datos es como preparar ingredientes: antes de cocinar, separas, lavas y revisas que no falte lo esencial.",
                ["¿Qué columna tiene datos faltantes?", "¿Cuándo se elimina un duplicado?", "¿Qué tipo de dato espera cada campo?", "¿Cómo documentas una transformación?"],
                ["Arrays y operaciones básicas", "Series y DataFrame", "Lectura de CSV", "Nulos y duplicados", "Filtrado y selección", "Agrupación y resumen"],
                [("Array", "Estructura numérica para cálculos eficientes."), ("DataFrame", "Tabla con filas y columnas."), ("Nulo", "Dato ausente que debe tratarse con regla explícita."), ("Duplicado", "Registro repetido que puede distorsionar resultados."), ("Groupby", "Agrupación para calcular resúmenes por categoría.")],
                ["Problema: un dataset escolar tiene faltantes.", "Carga: crear o leer tabla.", "Diagnóstico: contar nulos y duplicados.", "Limpieza: aplicar regla justificada.", "Resumen: agrupar o calcular métricas.", "Evidencia: tabla limpia y bitácora."],
                [ml("missing rate = nulos / total", "Medir datos faltantes.", "Nulos y total como conteos."), ml("duplicate rate = duplicados / total", "Medir registros repetidos.", "Conteos."), ml("media = sum(x) / n", "Resumir columna numérica.", "x como valores; n como conteo."), ml("normalizado = (x - mínimo) / (máximo - mínimo)", "Escalar valores entre 0 y 1.", "x, mínimo y máximo en la misma unidad."), ml("retención = filas limpias / filas originales", "Medir cuánto queda tras limpiar.", "Conteos; resultado porcentual.")],
                "Un dataset tiene 10 filas, 2 valores faltantes en asistencia y 1 registro duplicado. Limpia y calcula retención.",
                ["Filas originales: 10.", "Valores faltantes en asistencia: 2.", "Duplicados: 1.", "Después de eliminar duplicado quedan 9 filas."],
                ["Missing rate = 2 / 10 = 20%.", "Duplicate rate = 1 / 10 = 10%.", "Retención = 9 / 10 = 90%.", "Se decide no eliminar filas por nulos: se documenta revisión de asistencia.", "La bitácora separa duplicado eliminado y nulos pendientes."],
                "La limpieza es aceptable para exploración inicial, pero la asistencia faltante debe resolverse antes de modelar.",
                "Dataset escolar limpio con bitácora de transformaciones.",
                "Cargar tabla, diagnosticar nulos, eliminar duplicados y registrar la regla aplicada.",
                "Lee una página de pandas sobre DataFrame o manejo de nulos y resume una función útil.",
                code='''import pandas as pd

datos = {
    "estudiante": ["Ana", "Luis", "Luis", "Marta", "Sofía"],
    "asistencia": [95, 80, 80, None, 70],
    "calificacion": [9.0, 7.5, 7.5, 8.0, 6.5],
}

tabla = pd.DataFrame(datos)

duplicados = tabla.duplicated().sum()
nulos = tabla.isna().sum()
tabla_limpia = tabla.drop_duplicates()

print("Duplicados:", duplicados)
print("Nulos por columna:")
print(nulos)
print("Tabla limpia:")
print(tabla_limpia)''',
                code_check=["Confirma que se detecte 1 duplicado.", "Revisa que asistencia tenga 1 valor nulo.", "Verifica que la tabla limpia conserve 4 filas."],
            ),
            Unit(
                "u03",
                "Visualización de Datos",
                "El equipo visualiza distribución de calificaciones por materia.",
                "Una gráfica no es decoración. Permite detectar patrones, grupos, errores y valores extremos que una tabla puede ocultar. Antes de entrenar modelos, el equipo debe mirar los datos y explicar qué muestra cada eje.",
                "Una gráfica es como una ventana: muestra algo con claridad, pero también decide qué queda fuera.",
                ["¿Qué gráfica conviene para comparar materias?", "¿Qué muestra un histograma?", "¿Qué oculta un promedio?", "¿Cómo evitas una gráfica engañosa?"],
                ["Líneas, barras y dispersión", "Histogramas", "Boxplots", "Títulos y ejes", "Interpretación visual", "Storytelling con datos"],
                [("Eje x", "Variable horizontal, normalmente categoría o variable independiente."), ("Eje y", "Variable vertical, normalmente medida o variable dependiente."), ("Histograma", "Distribución de valores por intervalos."), ("Boxplot", "Resumen visual de mediana, cuartiles y posibles outliers."), ("Outlier", "Valor atípico que requiere revisión.")],
                ["Problema: la tabla no revela patrón.", "Selección: elegir gráfica según pregunta.", "Construcción: definir ejes y título.", "Lectura: describir patrón visible.", "Revisión: detectar sesgo o escala engañosa.", "Evidencia: gráfica con interpretación."],
                [ml("x = variable independiente", "Definir eje horizontal.", "Unidad del dato original."), ml("y = variable dependiente", "Definir eje vertical.", "Unidad del dato original."), ml("bins = número de intervalos", "Configurar histograma.", "Conteo de grupos."), ml("IQR = Q3 - Q1", "Medir rango intercuartil.", "Misma unidad del dato."), ml("outlier si x > Q3 + 1.5 IQR", "Detectar valor atípico alto.", "x, Q3 e IQR en misma unidad.")],
                "Una lista de calificaciones tiene Q1 = 6.5 y Q3 = 8.5. Decide si 10.0 es outlier alto.",
                ["Q1 = 6.5.", "Q3 = 8.5.", "Valor a revisar: 10.0.", "Regla: outlier alto si x > Q3 + 1.5 IQR."],
                ["IQR = 8.5 - 6.5 = 2.0.", "Límite alto = 8.5 + 1.5(2.0) = 11.5.", "10.0 no es mayor que 11.5.", "No se marca como outlier alto.", "Se interpreta como calificación alta dentro del rango esperado."],
                "La gráfica debe mostrar 10.0 como valor alto, pero no como dato atípico según esta regla.",
                "Dashboard de gráficas básicas del dataset escolar.",
                "Construir gráfica, explicar ejes y justificar qué patrón se observa.",
                "Lee documentación de Matplotlib sobre títulos o etiquetas de ejes y escribe dos reglas de claridad visual.",
                code='''import matplotlib.pyplot as plt

materias = ["Matemáticas", "Física", "Química", "Historia"]
promedios = [7.4, 8.1, 7.8, 8.6]

plt.bar(materias, promedios, color="#0E7490")
plt.title("Promedio por materia")
plt.xlabel("Materia")
plt.ylabel("Calificación promedio")
plt.ylim(0, 10)
plt.tight_layout()
plt.show()''',
                code_check=["Confirma que la gráfica tenga cuatro barras.", "Revisa que el eje y vaya de 0 a 10.", "Explica qué materia tiene mayor promedio y cuál requiere atención."],
            ),
            Unit(
                "u04",
                "Estadística para Entender Datos",
                "El equipo analiza si horas de estudio y calificación se relacionan.",
                "La estadística descriptiva permite distinguir patrón, variación y casualidad. Antes de afirmar que una variable causa otra, se revisan medias, dispersión, percentiles y correlación con cautela.",
                "La estadística es como una lupa con escala: acerca los datos, pero también muestra cuánto varían.",
                ["¿Qué diferencia hay entre media y mediana?", "¿Qué mide la desviación estándar?", "¿Cuándo correlación no implica causalidad?", "¿Cómo detectas outliers?"],
                ["Media y mediana", "Varianza y desviación estándar", "Percentiles", "Correlación de Pearson", "Correlación vs causalidad", "Detección de outliers"],
                [("Media", "Promedio aritmético."), ("Mediana", "Valor central al ordenar datos."), ("Varianza", "Medida de dispersión respecto a la media."), ("Desviación estándar", "Raíz de la varianza; vuelve a la unidad original."), ("Correlación", "Medida de relación entre dos variables, no prueba causalidad.")],
                ["Problema: se sospecha relación entre estudio y calificación.", "Resumen: calcular medidas centrales.", "Dispersión: estimar variabilidad.", "Relación: calcular correlación.", "Cautela: separar correlación y causalidad.", "Evidencia: informe con interpretación y límites."],
                [ml("media = sum(x) / n", "Calcular promedio.", "x como valores; n como conteo."), ml("varianza = sum((x - media)^2) / n", "Medir dispersión.", "Unidad original al cuadrado."), ml("desviación = raíz(varianza)", "Volver a unidad original.", "Misma unidad de x."), ml("r = cov(x,y) / (sigma_x sigma_y)", "Correlación de Pearson.", "r no tiene unidad y va de -1 a 1."), ml("z = (x - media) / desviación", "Comparar un valor con el grupo.", "z sin unidad.")],
                "Un grupo registra horas de estudio y calificaciones. Se obtiene r = 0.72. Interpreta el resultado y calcula z para una calificación de 9 si media = 7.5 y desviación = 1.",
                ["r = 0.72.", "Calificación del estudiante: 9.", "Media del grupo: 7.5.", "Desviación estándar: 1."],
                ["r = 0.72 indica relación positiva fuerte, no causalidad automática.", "z = (9 - 7.5) / 1 = 1.5.", "El estudiante está 1.5 desviaciones arriba de la media.", "Se revisan otros factores antes de afirmar causa.", "La conclusión debe mencionar límite de interpretación."],
                "Hay evidencia de relación positiva, pero no prueba de que estudiar más sea la única causa de la calificación.",
                "Informe estadístico de relación entre horas de estudio y calificación.",
                "Calcular medidas, interpretar correlación y redactar límites de causalidad.",
                "Lee una explicación de correlación en documentación o libro y escribe un ejemplo donde correlación no implique causa.",
                code='''import pandas as pd

tabla = pd.DataFrame({
    "horas_estudio": [1, 2, 3, 4, 5],
    "calificacion": [6.0, 6.8, 7.5, 8.4, 9.0],
})

media = tabla["calificacion"].mean()
desviacion = tabla["calificacion"].std()
correlacion = tabla["horas_estudio"].corr(tabla["calificacion"])

print("Media:", round(media, 2))
print("Desviación estándar:", round(desviacion, 2))
print("Correlación:", round(correlacion, 2))''',
                code_check=["Verifica que la correlación sea positiva.", "Explica por qué el resultado no prueba causalidad.", "Cambia una calificación y observa cómo cambia la correlación."],
            ),
        ],
    },
}


def main() -> None:
    results: dict[int, tuple[Path, dict[str, int]]] = {}
    for manual in (3, 4, 5):
        results[manual] = build_manual(manual, DATA[manual])
    index = make_index(results)
    report = write_report(results, index)
    for manual, (path, stats) in results.items():
        print(f"M{manual}: {stats['pages']} pages, {stats['images']} images, {stats['links']} links, {stats['brokenImages']} broken -> {path}")
    print(f"Index: {index}")
    print(f"Report: {report}")


if __name__ == "__main__":
    main()
