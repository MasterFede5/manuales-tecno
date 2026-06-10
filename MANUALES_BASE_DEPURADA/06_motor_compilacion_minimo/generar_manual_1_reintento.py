from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
MANUALES = ROOT / "01_fuente_principal_markdown" / "manuales"
VISUALES = ROOT / "05_assets_visuales_iconos" / "visuales" / "manual-1"
PROMPTS = ROOT / "05_assets_visuales_iconos" / "prompts-visuales" / "manual-1" / "sem-1"
U0_HTML = MANUALES / "manual-1" / "unidades" / "u00" / "unidad-0-quimica.html"
OUT = MANUALES / "manual-1" / "semestre-1" / "manual-1-quimica-semestre-1-reintento.html"
IMG_PREFIX = "../../../../05_assets_visuales_iconos/visuales/manual-1"

EXTRA_STYLE = """
    @page landscape {
      size: letter landscape;
      margin: 0;
    }

    .appendix-cover {
      display: grid;
      grid-template-rows: auto 1fr auto;
      gap: 8mm;
      background:
        linear-gradient(135deg, rgba(14, 58, 138, 0.94), rgba(14, 116, 144, 0.84)),
        #0E3A8A;
      color: #FFFFFF;
    }

    .appendix-cover h2,
    .appendix-cover h3 {
      color: #FFFFFF;
      border-color: rgba(255, 255, 255, 0.32);
    }

    .appendix-cover .kicker {
      color: #FFD28A;
    }

    .appendix-cover .subtitle {
      color: rgba(255, 255, 255, 0.88);
      max-width: 160mm;
    }

    .appendix-panel {
      border-left: 6px solid var(--orange);
      background: rgba(255, 255, 255, 0.12);
      padding: 5mm;
      font-size: 11pt;
    }

    .appendix-cover .footer {
      color: rgba(255, 255, 255, 0.88);
      border-top-color: rgba(255, 255, 255, 0.38);
    }

    .concept-list {
      gap: 2.2mm;
    }

    .concept {
      font-size: 11pt;
      line-height: 1.26;
      padding: 2.8mm;
    }

    .concept strong {
      font-size: 11.8pt;
      line-height: 1.12;
    }

    .development-card {
      padding: 3.6mm;
    }

    .development-card h3,
    .fundamental-card h3,
    .formula-card h3,
    .exercise-development h3 {
      font-size: 12.4pt;
      line-height: 1.15;
    }

    .development-card p,
    .development-card li,
    .fundamental-card p,
    .formula-card p,
    .formula-card li,
    .mini-activity p,
    .mini-activity li,
    .exercise-development p {
      font-size: 11pt;
      line-height: 1.28;
    }

    .bank-item {
      min-height: 45mm;
      padding: 3mm;
    }

    .bank-item p {
      font-size: 11pt;
      line-height: 1.26;
    }

    .bank-lines::before {
      font-size: 9.6pt;
    }

    .bank-lines span {
      height: 4mm;
    }

    .question p {
      font-size: 10.8pt;
      line-height: 1.25;
    }

    .answer-lines span {
      height: 4mm;
    }

    .mini-table {
      font-size: 10.7pt;
      line-height: 1.24;
    }

    .mini-table th,
    .mini-table td {
      padding: 2.4mm;
    }

    .step-box {
      min-height: 25mm;
      font-size: 10.5pt;
      line-height: 1.25;
    }

    .calc-bank {
      grid-template-columns: 1fr;
      gap: 4mm;
    }

    .calc-bank .bank-item {
      min-height: 72mm;
      padding: 4mm;
    }

    .calc-bank .bank-lines span {
      height: 5mm;
    }

    .periodic-visual-page,
    .dense-visual-page {
      padding: 9mm 12mm 14mm;
      grid-template-rows: auto auto 1fr auto;
      gap: 2.2mm;
    }

    .landscape-visual-page {
      page: landscape;
      width: 279mm;
      height: 216mm;
      min-height: 216mm;
      padding: 8mm 10mm 12mm;
      grid-template-rows: auto auto 1fr auto;
      gap: 1.8mm;
    }

    .periodic-visual-page h2,
    .dense-visual-page h2 {
      font-size: 18pt;
      margin-bottom: 1mm;
    }

    .periodic-visual-page .subtitle,
    .dense-visual-page .subtitle {
      font-size: 9.8pt;
      line-height: 1.22;
    }

    .periodic-visual-page .case-image img,
    .dense-visual-page .case-image img {
      width: auto;
      max-width: 100%;
      max-height: 226mm;
      margin: 0 auto;
    }

    .landscape-visual-page .case-image img,
    .landscape-visual-page .wide-image img {
      width: 100%;
      max-width: 255mm;
      max-height: 154mm;
      object-fit: contain;
      object-position: center;
      margin: 0 auto;
    }

    .landscape-visual-page .subtitle {
      max-width: 250mm;
      font-size: 9.6pt;
      line-height: 1.18;
    }

    .periodic-visual-page .image-frase,
    .dense-visual-page .image-frase {
      font-size: 9.6pt;
      padding: 0 4mm;
    }

    .landscape-visual-page .image-frase,
    .landscape-visual-page .calculation-phrase {
      font-size: 9.3pt;
      line-height: 1.18;
      padding: 0 8mm;
    }

    .landscape-visual-page .mini-activity {
      padding: 2.2mm;
    }

    .landscape-visual-page .mini-activity p,
    .landscape-visual-page .mini-activity li {
      font-size: 9.8pt;
      line-height: 1.2;
    }

    .appendix-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4mm;
      margin-top: 4mm;
    }

    .appendix-card {
      border: 1px solid var(--line);
      border-left: 5px solid var(--cyan);
      padding: 3mm;
      break-inside: avoid;
      min-height: 34mm;
    }

    .appendix-card h3 {
      margin-top: 0;
      font-size: 11.4pt;
    }

    .appendix-card p,
    .appendix-card li {
      font-size: 8.8pt;
      line-height: 1.3;
    }

    .reading-text {
      column-count: 2;
      column-gap: 6mm;
      font-size: 9.2pt;
      line-height: 1.36;
      margin-bottom: 4mm;
    }

    .reading-text p {
      break-inside: avoid;
      margin-bottom: 3mm;
    }

    .worksheet-lines {
      display: grid;
      gap: 2mm;
      margin-top: 2mm;
    }

    .worksheet-lines span {
      border-bottom: 1px solid #AAB4C3;
      height: 4mm;
      display: block;
    }

    .periodic-table {
      display: grid;
      grid-template-columns: repeat(18, 1fr);
      gap: 0.85mm;
      margin-top: 4mm;
    }

    .element {
      min-height: 10.2mm;
      border: 1px solid #C8D1DE;
      background: #F8FAFC;
      padding: 0.8mm;
      font-size: 5.7pt;
      line-height: 1.04;
      overflow: hidden;
    }

    .element strong {
      display: block;
      color: var(--blue);
      font-size: 8.4pt;
      line-height: 1;
    }

    .element .num {
      color: var(--muted);
      font-size: 5.6pt;
    }

    .element.alkali { background: #FFF7ED; }
    .element.alkaline { background: #ECFDF5; }
    .element.transition { background: #EFF6FF; }
    .element.metalloid { background: #F5F3FF; }
    .element.nonmetal { background: #F0FDFA; }
    .element.halogen { background: #FEFCE8; }
    .element.noble { background: #FDF2F8; }
    .element.lanth { background: #F7FEE7; }
    .element.act { background: #FAE8FF; }

    .mini-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 3mm;
      font-size: 10.7pt;
      line-height: 1.24;
    }

    .mini-table th,
    .mini-table td {
      border: 1px solid var(--line);
      padding: 2.4mm;
      vertical-align: top;
    }

    .mini-table th {
      background: var(--blue);
      color: #FFFFFF;
      text-align: left;
    }

    .classification-defs {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3mm;
      margin-top: 3mm;
    }

    .classification-defs .concept {
      min-height: 23mm;
    }

    .classification-task {
      margin-top: 4mm;
      border: 1px solid var(--line);
      border-left: 6px solid var(--green);
      padding: 3mm;
      break-inside: avoid;
    }

    .classification-task h3 {
      color: var(--green);
      margin-top: 0;
    }
"""


@dataclass
class Visual:
    id: str
    unit: str
    src: str
    desc: str


def e(text: str) -> str:
    return escape(text, quote=True).encode("ascii", "xmlcharrefreplace").decode("ascii")


SPANISH_TEXT_REPLACEMENTS = {
    "Quimica": "Química",
    "quimica": "química",
    "Quimico": "Químico",
    "quimico": "químico",
    "Basicos": "Básicos",
    "basicos": "básicos",
    "Basico": "Básico",
    "basico": "básico",
    "Atomico": "Atómico",
    "atomico": "atómico",
    "Atomica": "Atómica",
    "atomica": "atómica",
    "Atomos": "Átomos",
    "atomos": "átomos",
    "Atomo": "Átomo",
    "atomo": "átomo",
    "Isotopos": "Isótopos",
    "isotopos": "isótopos",
    "Numero": "Número",
    "numero": "número",
    "Numeros": "Números",
    "numeros": "números",
    "Formula": "Fórmula",
    "formula": "fórmula",
    "Formulas": "Fórmulas",
    "formulas": "fórmulas",
    "Calculo": "Cálculo",
    "calculo": "cálculo",
    "Calculos": "Cálculos",
    "calculos": "cálculos",
    "Periodica": "Periódica",
    "periodica": "periódica",
    "Periodico": "Periódico",
    "periodico": "periódico",
    "Electron": "Electrón",
    "electron": "electrón",
    "Ionico": "Iónico",
    "ionico": "iónico",
    "Molecula": "Molécula",
    "molecula": "molécula",
    "Moleculas": "Moléculas",
    "moleculas": "moléculas",
    "Solucion": "Solución",
    "solucion": "solución",
    "Dilucion": "Dilución",
    "dilucion": "dilución",
    "Concentracion": "Concentración",
    "concentracion": "concentración",
    "Contaminacion": "Contaminación",
    "contaminacion": "contaminación",
    "Combustion": "Combustión",
    "combustion": "combustión",
    "Reaccion": "Reacción",
    "reaccion": "reacción",
    "Oxigeno": "Oxígeno",
    "oxigeno": "oxígeno",
    "Oxidos": "Óxidos",
    "oxidos": "óxidos",
    "Acido": "Ácido",
    "acido": "ácido",
    "Acida": "Ácida",
    "acida": "ácida",
    "Basica": "Básica",
    "basica": "básica",
    "Interpretacion": "Interpretación",
    "interpretacion": "interpretación",
    "Conclusion": "Conclusión",
    "conclusion": "conclusión",
    "Explicacion": "Explicación",
    "explicacion": "explicación",
    "Observacion": "Observación",
    "observacion": "observación",
    "Clasificacion": "Clasificación",
    "clasificacion": "clasificación",
    "Homogenea": "Homogénea",
    "homogenea": "homogénea",
    "Heterogenea": "Heterogénea",
    "heterogenea": "heterogénea",
    "Composicion": "Composición",
    "composicion": "composición",
    "Medicion": "Medición",
    "medicion": "medición",
    "Precision": "Precisión",
    "precision": "precisión",
    "Decision": "Decisión",
    "decision": "decisión",
    "Investigacion": "Investigación",
    "investigacion": "investigación",
    "Analisis": "Análisis",
    "analisis": "análisis",
    "Hipotesis": "Hipótesis",
    "hipotesis": "hipótesis",
    "Metodo": "Método",
    "metodo": "método",
    "Cientifico": "Científico",
    "cientifico": "científico",
    "Fisicas": "Físicas",
    "fisicas": "físicas",
    "Energia": "Energía",
    "energia": "energía",
    "Ionizacion": "Ionización",
    "ionizacion": "ionización",
    "Biogeoquimicos": "Biogeoquímicos",
    "biogeoquimicos": "biogeoquímicos",
    "Configuracion": "Configuración",
    "configuracion": "configuración",
    "Masico": "Másico",
    "masico": "másico",
    "Particulas": "Partículas",
    "particulas": "partículas",
    "Usalo": "Úsalo",
    "usalo": "úsalo",
    "Comunmente": "Comúnmente",
    "comunmente": "comúnmente",
    "Atmosferica": "Atmosférica",
    "atmosferica": "atmosférica",
    "Atmosfera": "Atmósfera",
    "atmosfera": "atmósfera",
    "Inorganica": "Inorgánica",
    "inorganica": "inorgánica",
    "Comun": "Común",
    "comun": "común",
    "Aplicacion": "Aplicación",
    "aplicacion": "aplicación",
    "Tecnica": "Técnica",
    "tecnica": "técnica",
    "Guia": "Guía",
    "guia": "guía",
    "Pagina": "Página",
    "pagina": "página",
    "Practica": "Práctica",
    "practica": "práctica",
    "Simbolo": "Símbolo",
    "simbolo": "símbolo",
    "Disena": "Diseña",
    "disena": "diseña",
    "Senala": "Señala",
    "senala": "señala",
    "Pequeno": "Pequeño",
    "pequeno": "pequeño",
    "Pequenos": "Pequeños",
    "pequenos": "pequeños",
    "Pequena": "Pequeña",
    "pequena": "pequeña",
    "Pequenas": "Pequeñas",
    "pequenas": "pequeñas",
    "Mas": "Más",
    "mas": "más",
    "Asi": "Así",
    "asi": "así",
}


def fix_spanish_text_segment(text: str) -> str:
    for source, target in SPANISH_TEXT_REPLACEMENTS.items():
        text = re.sub(rf"\b{re.escape(source)}\b", target, text)
    text = re.sub(r"\bPor qué\b([^?]*\?)", r"¿Por qué\1", text)
    text = re.sub(r"\bQué\b([^?]*\?)", r"¿Qué\1", text)
    text = re.sub(r"\bCómo\b([^?]*\?)", r"¿Cómo\1", text)
    text = re.sub(r"\bCuándo\b([^?]*\?)", r"¿Cuándo\1", text)
    text = re.sub(r"\bCuánto(s)?\b([^?]*\?)", lambda m: "¿Cuánto" + (m.group(1) or "") + m.group(2), text)
    text = re.sub(r"\bCuál(es)?\b([^?]*\?)", lambda m: "¿Cuál" + (m.group(1) or "") + m.group(2), text)
    return text


def fix_spanish_text_nodes(html: str) -> str:
    parts = re.split(r"(<[^>]+>)", html)
    for idx, part in enumerate(parts):
        if not part or part.startswith("<"):
            continue
        parts[idx] = fix_spanish_text_segment(part)
    return "".join(parts)


def first_sentence(text: str, limit: int = 260) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"-(\d+)$", path.stem)
    return (int(match.group(1)) if match else 999, path.stem)


def prompt_for(unit: str, visual_id: str) -> Path | None:
    matches = sorted((PROMPTS / unit).glob(f"{visual_id}*.md"))
    return matches[0] if matches else None


def description_from_prompt(path: Path | None) -> str:
    if not path:
        return "Visual pedagogico de apoyo para el tema."
    raw = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"## Descripci\S*n original del manual\s*(.*?)(?:\n## |\Z)", raw, re.S)
    if not match:
        return "Visual pedagogico de apoyo para el tema."
    lines: list[str] = []
    for line in match.group(1).splitlines():
        clean = line.strip()
        if not clean:
            continue
        if clean.startswith(">"):
            clean = clean[1:].strip()
        if clean.startswith("_Nota") or clean.startswith("|"):
            continue
        lines.append(clean)
    return " ".join(lines).strip() or "Visual pedagogico de apoyo para el tema."


def visuals(unit: str) -> list[Visual]:
    result: list[Visual] = []
    for img in sorted((VISUALES / unit).glob("*.*"), key=sort_key):
        if img.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
            continue
        desc = description_from_prompt(prompt_for(unit, img.stem))
        result.append(Visual(img.stem, unit, f"{IMG_PREFIX}/{unit}/{img.name}", desc))
    return result


def footer(left: str, right: str) -> str:
    return f'<div class="footer"><span>{e(left)}</span><span>{e(right)}</span></div>'


def section(body: str, cls: str = "page") -> str:
    return f'<section class="{cls}">\n{body}\n</section>\n'


def image_page(unit: dict, visual: Visual, topic: str, phrase: str, mini: str) -> str:
    number = int(visual.id.rsplit("-", 1)[1])
    intro = unit.get("visual_intros", {}).get(number, unit["case_link"])
    landscape = number in set(unit.get("landscape_visuals", []))
    dense = landscape or number in set(unit.get("dense_visuals", []))
    mini_block = ""
    if not dense:
        mini_block = f"""
    <div class="mini-activity">
      <h3>Mini actividad conectada al caso</h3>
      <p>{e(mini)}</p>
    </div>
        """
    body = f"""
    <div>
      <p class="kicker">{e(unit['kicker'])}</p>
      <h2>{e(topic)}</h2>
    </div>
    <p class="subtitle">{e(intro)}</p>
    <figure class="case-image" data-visual-id="{e(visual.id)}">
      <img src="{e(visual.src)}" alt="{e(topic)}">
    </figure>
    <p class="image-frase">{e(phrase)}</p>
    {mini_block}
    {footer('Colegio Nuevo Tecno', unit['short'])}
    """
    if landscape:
        page_class = "page case-image-page dense-visual-page landscape-visual-page"
    elif dense:
        page_class = "page case-image-page dense-visual-page"
    else:
        page_class = "page case-image-page"
    return section(body, page_class)


def activity_block(unit: dict, number: int, topic: str) -> str:
    kind_order = ["open", "calc", "compare", "match", "explain", "table"]
    kind = unit.get("activity_kinds", {}).get(number, kind_order[number % len(kind_order)])
    spec = unit.get("activity_specs", {}).get(number, {})
    if kind == "calc":
        title = spec.get("title", "Comprobacion con calculos")
        instruction = spec.get(
            "instruction",
            'Usa el tema "' + topic + '" para plantear un dato medible del caso, escribir la formula necesaria y comprobar si el resultado tiene sentido con sus unidades.',
        )
        steps = spec.get("steps", ["Dato y unidad inicial.", "Formula que usaras.", "Sustitucion con unidades visibles.", "Resultado y comprobacion."])
        step_html = "".join(
            f'<div class="step-box"><strong>{idx}.</strong> {e(step)}</div>' for idx, step in enumerate(steps, 1)
        )
        return f"""
    <div class="exercise-development">
      <h3>{e(title)}</h3>
      <p>{e(instruction)}</p>
      <div class="exercise-steps">{step_html}</div>
    </div>
        """
    if kind == "compare":
        left = spec.get("left", topic + " en el modelo")
        right = spec.get("right", topic + " aplicado al bebedero")
        title = spec.get("title", "Cuadro comparativo")
        instruction = spec.get(
            "instruction",
            f"Compara {left} y {right}. Completa cada criterio y escribe una conclusion que conecte la comparacion con el caso del bebedero.",
        )
        criteria = spec.get("criteria", ["Que representa", "Dato que puede medirse", "Formula, unidad o evidencia", "Conclusion para el caso"])
        headers = "".join(f"<th>{e(h)}</th>" for h in ["Criterio", left, right, "Conclusion"])
        rows = "".join(
            "<tr>" + "".join(f"<td>{e(cell)}</td>" for cell in row) + "</tr>"
            for row in [[criterion, "", "", ""] for criterion in criteria]
        )
        return f"""
    <div class="exercise-development">
      <h3>{e(title)}</h3>
      <p>{e(instruction)}</p>
      <table class="mini-table"><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table>
    </div>
        """
    if kind == "match":
        title = spec.get("title", "Relacion de columnas")
        instruction = spec.get(
            "instruction",
            f"Relaciona los conceptos de {topic.lower()} con la descripcion correcta. Escribe las parejas en formato A-__, B-__, C-__.",
        )
        left_items = spec.get("left_items", [("A", "Concepto clave"), ("B", "Formula o representacion"), ("C", "Error frecuente")])
        right_items = spec.get("right_items", [("1", "Dato o ejemplo del caso"), ("2", "Unidad o evidencia"), ("3", "Correccion posible")])
        max_rows = max(len(left_items), len(right_items))
        rows_data = []
        for idx in range(max_rows):
            left = left_items[idx] if idx < len(left_items) else ("", "")
            right = right_items[idx] if idx < len(right_items) else ("", "")
            rows_data.append([f"{left[0]}. {left[1]}" if left[0] else "", f"{right[0]}. {right[1]}" if right[0] else ""])
        headers = "".join(f"<th>{e(h)}</th>" for h in ["Columna A: letras", "Columna B: numeros"])
        rows = "".join(
            "<tr>" + "".join(f"<td>{e(cell)}</td>" for cell in row) + "</tr>"
            for row in rows_data
        )
        return f"""
    <div class="exercise-development">
      <h3>{e(title)}</h3>
      <p>{e(instruction)}</p>
      <table class="mini-table"><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table>
      <div class="worksheet-lines"><span></span><span></span></div>
    </div>
        """
    if kind == "table":
        title = spec.get("title", "Tabla aplicada")
        instruction = spec.get("instruction", "Completa la tabla con ejemplos propios conectados con " + topic.lower() + ".")
        table_headers = spec.get("headers", ["Ejemplo", "Clasificacion", "Dato necesario", "Justificacion"])
        table_rows = spec.get("rows", [["", "", "", ""], ["", "", "", ""], ["", "", "", ""]])
        headers = "".join(f"<th>{e(h)}</th>" for h in table_headers)
        rows = "".join(
            "<tr>" + "".join(f"<td>{e(cell)}</td>" for cell in row) + "</tr>"
            for row in table_rows
        )
        return f"""
    <div class="exercise-development">
      <h3>{e(title)}</h3>
      <p>{e(instruction)}</p>
      <table class="mini-table"><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table>
    </div>
        """
    if kind == "open":
        title = spec.get("title", "Preguntas abiertas")
        questions = spec.get("questions", [
            f"Que evidencia te haria cambiar tu interpretacion sobre {topic.lower()}?",
            "Que dato falta para defender una conclusion quimica?",
            "Como conectarias este tema con el bebedero escolar?",
        ])
        question_html = "".join(
            f'<div class="question"><p>{idx}. {e(q)}</p><div class="answer-lines"><span></span><span></span><span></span></div></div>'
            for idx, q in enumerate(questions, 1)
        )
        return f"""
    <div class="exercise-development">
      <h3>{e(title)}</h3>
      <div class="questions-grid">{question_html}</div>
    </div>
        """
    title = spec.get("title", "Explicacion con evidencia")
    instruction = spec.get(
        "instruction",
        "Redacta una explicacion breve sobre " + topic.lower() + " usando una evidencia, una unidad o una representacion quimica.",
    )
    steps = spec.get("steps", ["Idea principal.", "Evidencia o dato.", "Limite o error posible.", "Decision para el caso."])
    step_html = "".join(
        f'<div class="step-box"><strong>{idx}.</strong> {e(step)}</div>' for idx, step in enumerate(steps, 1)
    )
    return f"""
    <div class="exercise-development">
      <h3>{e(title)}</h3>
      <p>{e(instruction)}</p>
      <div class="exercise-steps">{step_html}</div>
    </div>
    """


def concept_page(unit: dict, visual: Visual, topic: str) -> str:
    number = int(visual.id.rsplit("-", 1)[1])
    special = unit.get("special_concept_pages", {}).get(number)
    if special:
        return special_concept_page(unit, special, topic)
    desc = unit.get("concept_narratives", {}).get(
        number,
        f"Este apartado conecta {topic.lower()} con una decision del caso conductor. La imagen no se copia ni se describe: se usa para traducir una idea quimica en dato, formula, criterio de clasificacion o registro de laboratorio.",
    )
    body = f"""
    <p class="kicker">{e(unit['kicker'])}</p>
    <h2>{e('Que implica: ' + topic)}</h2>
    <p class="subtitle">{e(desc)}</p>
    <div class="development-grid">
      <div class="development-card"><h3>Idea quimica</h3><p>{e(unit['concept_frame'])}</p></div>
      <div class="development-card"><h3>Decision del caso</h3><p>{e(unit['decision_frame'])}</p></div>
      <div class="development-card"><h3>Dato que se debe registrar</h3><p>{e(unit['data_frame'])}</p></div>
      <div class="development-card"><h3>Error a evitar</h3><p>{e(unit['error_frame'])}</p></div>
    </div>
    {activity_block(unit, number, topic)}
    {footer('Colegio Nuevo Tecno', unit['short'] + ' / desarrollo')}
    """
    return section(body)


def special_concept_page(unit: dict, special: dict, topic: str) -> str:
    paragraphs = "".join(f"<p>{e(text)}</p>" for text in special.get("paragraphs", []))
    cards = "".join(
        f'<div class="development-card"><h3>{e(title)}</h3><p>{e(text)}</p></div>'
        for title, text in special.get("cards", [])
    )
    table = ""
    if special.get("table"):
        headers = "".join(f"<th>{e(item)}</th>" for item in special["table"]["headers"])
        rows = "".join(
            "<tr>" + "".join(f"<td>{e(cell)}</td>" for cell in row) + "</tr>"
            for row in special["table"]["rows"]
        )
        table = f"""
        <div class="classification-task">
          <h3>{e(special['table']['title'])}</h3>
          <p>{e(special['table']['instruction'])}</p>
          <table class="mini-table"><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table>
        </div>
        """
    steps = "".join(
        f'<div class="step-box"><strong>{idx}.</strong> {e(step)}</div>'
        for idx, step in enumerate(special.get("steps", []), 1)
    )
    exercise = ""
    if special.get("exercise"):
        exercise = f"""
        <div class="exercise-development">
          <h3>{e(special.get('exercise_title', 'Ejercicio de desarrollo'))}</h3>
          <p>{e(special['exercise'])}</p>
          <div class="exercise-steps">{steps}</div>
        </div>
        """
    if special.get("split_after_cards"):
        page_one = f"""
    <p class="kicker">{e(unit['kicker'])}</p>
    <h2>{e(special.get('title', 'Que implica: ' + topic))}</h2>
    <div class="reading-text">{paragraphs}</div>
    <div class="{e(special.get('card_class', 'development-grid'))}">{cards}</div>
    {footer('Colegio Nuevo Tecno', unit['short'] + ' / conceptos')}
        """
        page_two = f"""
    <p class="kicker">{e(unit['kicker'])}</p>
    <h2>{e(special.get('activity_page_title', special.get('table', {}).get('title', 'Actividad aplicada')))}</h2>
    {table}
    {exercise}
    {footer('Colegio Nuevo Tecno', unit['short'] + ' / actividad')}
        """
        return section(page_one) + section(page_two)
    body = f"""
    <p class="kicker">{e(unit['kicker'])}</p>
    <h2>{e(special.get('title', 'Que implica: ' + topic))}</h2>
    <div class="reading-text">{paragraphs}</div>
    <div class="{e(special.get('card_class', 'development-grid'))}">{cards}</div>
    {table}
    {exercise}
    {footer('Colegio Nuevo Tecno', unit['short'] + ' / desarrollo')}
    """
    return section(body)


def formula_page(unit: dict) -> str:
    cards = []
    for title, formula, desc in unit["formulas"]:
        cards.append(
            f'<div class="formula-card"><h3>{e(title)}</h3><div class="formula">{e(formula)}</div><p>{e(desc)}</p></div>'
        )
    body = f"""
    <p class="kicker">{e(unit['kicker'])}</p>
    <h2>{e('Formulas antes de practicar')}</h2>
    <p class="subtitle">{e(unit['formula_intro'])}</p>
    <div class="formula-grid">{''.join(cards)}</div>
    {footer('Colegio Nuevo Tecno', unit['short'] + ' / formulas')}
    """
    return section(body)


def bank_pages(unit: dict) -> str:
    pages: list[str] = []
    exercises = unit["exercises"]
    for start in range(0, len(exercises), 4):
        items = []
        for idx, text in enumerate(exercises[start : start + 4], start + 1):
            items.append(
                f'<div class="bank-item"><p><strong>{idx}.</strong> {e(text)}</p><div class="bank-lines"><span></span><span></span><span></span></div></div>'
            )
        body = f"""
        <p class="kicker">{e(unit['kicker'])}</p>
        <h2>{e('Banco de ejercicios ' + str(start // 4 + 1))}</h2>
        <div class="exercise-bank">{''.join(items)}</div>
        {footer('Colegio Nuevo Tecno', unit['short'] + f' / ejercicios {start + 1}-{min(start + 4, len(exercises))}')}
        """
        pages.append(section(body))
    return "\n".join(pages)


def calc_bank_pages(unit: dict) -> str:
    exercises = unit.get("calc_bank", [])
    if not exercises:
        return ""
    pages: list[str] = []
    for start in range(0, len(exercises), 2):
        items = []
        for idx, text in enumerate(exercises[start : start + 2], start + 1):
            items.append(
                f'<div class="bank-item"><p><strong>{idx}.</strong> {e(text)}</p><div class="bank-lines"><span></span><span></span><span></span><span></span><span></span></div></div>'
            )
        body = f"""
        <p class="kicker">{e(unit['kicker'])}</p>
        <h2>{e('Banco de calculo ' + str(start // 2 + 1))}</h2>
        <p class="subtitle">Resuelve con formula, sustitucion, unidades y comprobacion del resultado. Usa el espacio completo para operaciones.</p>
        <div class="exercise-bank calc-bank">{''.join(items)}</div>
        {footer('Colegio Nuevo Tecno', unit['short'] + f' / calculo {start + 1}-{min(start + 2, len(exercises))}')}
        """
        pages.append(section(body))
    return "\n".join(pages)


def unit_cover(unit: dict, first_visual: Visual) -> str:
    body = f"""
    <div>
      <p class="kicker">{e(unit['kicker'])}</p>
      <h2>{e(unit['title'])}</h2>
    </div>
    <p class="subtitle">{e(unit['story'])}</p>
    <figure class="case-image" data-visual-id="{e(first_visual.id)}">
      <img src="{e(first_visual.src)}" alt="{e(unit['title'])}">
    </figure>
    <p class="image-frase">{e(unit['cover_phrase'])}</p>
    <div class="mini-activity">
      <h3>Arranque de unidad</h3>
      <p>{e(unit['start_activity'])}</p>
    </div>
    {footer('Colegio Nuevo Tecno', unit['short'] + ' / inicio')}
    """
    return section(body, "page case-image-page")


def unit_intro(unit: dict) -> str:
    concepts = "".join(
        f'<div class="concept"><strong>{e(name)}</strong>{e(desc)}</div>' for name, desc in unit["concepts"]
    )
    questions = "".join(
        f'<div class="question"><p>{idx}. {e(q)}</p><div class="answer-lines"><span></span><span></span><span></span></div></div>'
        for idx, q in enumerate(unit["questions"], 1)
    )
    body = f"""
    <p class="kicker">{e(unit['kicker'])}</p>
    <h2>{e(unit['intro_title'])}</h2>
    <p>{e(unit['intro_1'])}</p>
    <p>{e(unit['intro_2'])}</p>
    <div class="note"><strong>Idea central:</strong> {e(unit['central_idea'])}</div>
    <h3>Elementos que necesitas para comprender el tema</h3>
    <div class="concept-list">{concepts}</div>
    <div class="questions"><h3>Preguntas introductorias</h3><div class="questions-grid">{questions}</div></div>
    {footer('Colegio Nuevo Tecno', unit['short'] + ' / introduccion')}
    """
    return section(body)


def close_unit(unit: dict) -> str:
    body = f"""
    <p class="kicker">{e(unit['kicker'])}</p>
    <h2>{e('Cierre de ' + unit['title'])}</h2>
    <p class="subtitle">{e(unit['close'])}</p>
    <div class="note"><strong>Producto de unidad:</strong> {e(unit['product'])}</div>
    <div class="exercise-development">
      <h3>Entrega breve</h3>
      <p>{e(unit['deliverable'])}</p>
      <div class="exercise-steps">
        <div class="step-box"><strong>1.</strong> Evidencia principal.</div>
        <div class="step-box"><strong>2.</strong> Calculo o criterio usado.</div>
        <div class="step-box"><strong>3.</strong> Error o limite detectado.</div>
        <div class="step-box"><strong>4.</strong> Decision para el caso del bebedero.</div>
      </div>
    </div>
    {footer('Colegio Nuevo Tecno', unit['short'] + ' / cierre')}
    """
    return section(body)


def build_unit(unit: dict) -> str:
    vs = visuals(unit["unit"])
    pages = [unit_cover(unit, vs[0]), unit_intro(unit)]
    topic_map = unit["topics"]
    for visual in vs[1:]:
        number = int(visual.id.rsplit("-", 1)[1])
        topic = topic_map.get(number, first_sentence(visual.desc, 80))
        phrase = unit["phrases"].get(number, unit["default_phrase"])
        mini = unit["mini"].get(number, unit["default_mini"])
        pages.append(image_page(unit, visual, topic, phrase, mini))
        pages.append(concept_page(unit, visual, topic))
    pages.append(formula_page(unit))
    pages.append(calc_bank_pages(unit))
    pages.append(bank_pages(unit))
    pages.append(close_unit(unit))
    return "\n".join(pages)


ELEMENTS = [
    (1, "H", 1, 1, "nonmetal"), (2, "He", 18, 1, "noble"),
    (3, "Li", 1, 2, "alkali"), (4, "Be", 2, 2, "alkaline"), (5, "B", 13, 2, "metalloid"), (6, "C", 14, 2, "nonmetal"), (7, "N", 15, 2, "nonmetal"), (8, "O", 16, 2, "nonmetal"), (9, "F", 17, 2, "halogen"), (10, "Ne", 18, 2, "noble"),
    (11, "Na", 1, 3, "alkali"), (12, "Mg", 2, 3, "alkaline"), (13, "Al", 13, 3, "transition"), (14, "Si", 14, 3, "metalloid"), (15, "P", 15, 3, "nonmetal"), (16, "S", 16, 3, "nonmetal"), (17, "Cl", 17, 3, "halogen"), (18, "Ar", 18, 3, "noble"),
    (19, "K", 1, 4, "alkali"), (20, "Ca", 2, 4, "alkaline"), (21, "Sc", 3, 4, "transition"), (22, "Ti", 4, 4, "transition"), (23, "V", 5, 4, "transition"), (24, "Cr", 6, 4, "transition"), (25, "Mn", 7, 4, "transition"), (26, "Fe", 8, 4, "transition"), (27, "Co", 9, 4, "transition"), (28, "Ni", 10, 4, "transition"), (29, "Cu", 11, 4, "transition"), (30, "Zn", 12, 4, "transition"), (31, "Ga", 13, 4, "transition"), (32, "Ge", 14, 4, "metalloid"), (33, "As", 15, 4, "metalloid"), (34, "Se", 16, 4, "nonmetal"), (35, "Br", 17, 4, "halogen"), (36, "Kr", 18, 4, "noble"),
    (37, "Rb", 1, 5, "alkali"), (38, "Sr", 2, 5, "alkaline"), (39, "Y", 3, 5, "transition"), (40, "Zr", 4, 5, "transition"), (41, "Nb", 5, 5, "transition"), (42, "Mo", 6, 5, "transition"), (43, "Tc", 7, 5, "transition"), (44, "Ru", 8, 5, "transition"), (45, "Rh", 9, 5, "transition"), (46, "Pd", 10, 5, "transition"), (47, "Ag", 11, 5, "transition"), (48, "Cd", 12, 5, "transition"), (49, "In", 13, 5, "transition"), (50, "Sn", 14, 5, "transition"), (51, "Sb", 15, 5, "metalloid"), (52, "Te", 16, 5, "metalloid"), (53, "I", 17, 5, "halogen"), (54, "Xe", 18, 5, "noble"),
    (55, "Cs", 1, 6, "alkali"), (56, "Ba", 2, 6, "alkaline"), (57, "La", 3, 6, "lanth"), (72, "Hf", 4, 6, "transition"), (73, "Ta", 5, 6, "transition"), (74, "W", 6, 6, "transition"), (75, "Re", 7, 6, "transition"), (76, "Os", 8, 6, "transition"), (77, "Ir", 9, 6, "transition"), (78, "Pt", 10, 6, "transition"), (79, "Au", 11, 6, "transition"), (80, "Hg", 12, 6, "transition"), (81, "Tl", 13, 6, "transition"), (82, "Pb", 14, 6, "transition"), (83, "Bi", 15, 6, "transition"), (84, "Po", 16, 6, "metalloid"), (85, "At", 17, 6, "halogen"), (86, "Rn", 18, 6, "noble"),
    (87, "Fr", 1, 7, "alkali"), (88, "Ra", 2, 7, "alkaline"), (89, "Ac", 3, 7, "act"), (104, "Rf", 4, 7, "transition"), (105, "Db", 5, 7, "transition"), (106, "Sg", 6, 7, "transition"), (107, "Bh", 7, 7, "transition"), (108, "Hs", 8, 7, "transition"), (109, "Mt", 9, 7, "transition"), (110, "Ds", 10, 7, "transition"), (111, "Rg", 11, 7, "transition"), (112, "Cn", 12, 7, "transition"), (113, "Nh", 13, 7, "transition"), (114, "Fl", 14, 7, "transition"), (115, "Mc", 15, 7, "transition"), (116, "Lv", 16, 7, "transition"), (117, "Ts", 17, 7, "halogen"), (118, "Og", 18, 7, "noble"),
    (58, "Ce", 4, 8, "lanth"), (59, "Pr", 5, 8, "lanth"), (60, "Nd", 6, 8, "lanth"), (61, "Pm", 7, 8, "lanth"), (62, "Sm", 8, 8, "lanth"), (63, "Eu", 9, 8, "lanth"), (64, "Gd", 10, 8, "lanth"), (65, "Tb", 11, 8, "lanth"), (66, "Dy", 12, 8, "lanth"), (67, "Ho", 13, 8, "lanth"), (68, "Er", 14, 8, "lanth"), (69, "Tm", 15, 8, "lanth"), (70, "Yb", 16, 8, "lanth"), (71, "Lu", 17, 8, "lanth"),
    (90, "Th", 4, 9, "act"), (91, "Pa", 5, 9, "act"), (92, "U", 6, 9, "act"), (93, "Np", 7, 9, "act"), (94, "Pu", 8, 9, "act"), (95, "Am", 9, 9, "act"), (96, "Cm", 10, 9, "act"), (97, "Bk", 11, 9, "act"), (98, "Cf", 12, 9, "act"), (99, "Es", 13, 9, "act"), (100, "Fm", 14, 9, "act"), (101, "Md", 15, 9, "act"), (102, "No", 16, 9, "act"), (103, "Lr", 17, 9, "act"),
]


def inject_extra_style(base: str) -> str:
    if ".appendix-cover" in base:
        return base
    return base.replace("    @media print {", EXTRA_STYLE + "\n    @media print {", 1)


def adjust_base_toc(base: str) -> str:
    replacements = {
        "<div>Inicio</div><div>Portada, mapa de contenidos, hilo conductor, competencias y diagn&oacute;stica</div><div>10</div>": "<div>Inicio</div><div>Portada, mapa de contenidos, hilo conductor, competencias y diagn&oacute;stica</div><div>4</div>",
        "<div>U0</div><div>Lenguaje del Qu&iacute;mico</div><div>30</div>": "<div>U0</div><div>Lenguaje del Qu&iacute;mico</div><div>19</div>",
        "<div>U1</div><div>Temas B&aacute;sicos de la Materia</div><div>65</div>": "<div>U1</div><div>Temas B&aacute;sicos de la Materia</div><div>34</div>",
        "<div>U2</div><div>Agua</div><div>50</div>": "<div>U2</div><div>Agua</div><div>26</div>",
        "<div>U3</div><div>Aire</div><div>45</div>": "<div>U3</div><div>Aire</div><div>24</div>",
        "<div>Cierre</div><div>Examen integrador, bibliograf&iacute;a, recursos e &iacute;ndice anal&iacute;tico del semestre</div><div>18</div>": "<div>Cierre</div><div>Examen integrador, bibliograf&iacute;a, recursos, lecturas, tabla peri&oacute;dica e &iacute;ndice anal&iacute;tico</div><div>21</div>",
        '<div class="unit-title"><div class="id">U0</div><h3>Lenguaje del Qu&iacute;mico</h3><div class="hours">30 pp</div></div>': '<div class="unit-title"><div class="id">U0</div><h3>Lenguaje del Qu&iacute;mico</h3><div class="hours">19 pp</div></div>',
        '<div class="unit-title"><div class="id">U1</div><h3>Temas B&aacute;sicos de la Materia</h3><div class="hours">65 pp</div></div>': '<div class="unit-title"><div class="id">U1</div><h3>Temas B&aacute;sicos de la Materia</h3><div class="hours">34 pp</div></div>',
        '<div class="unit-title"><div class="id">U2</div><h3>Agua</h3><div class="hours">50 pp</div></div>': '<div class="unit-title"><div class="id">U2</div><h3>Agua</h3><div class="hours">26 pp</div></div>',
        '<div class="unit-title"><div class="id">U3</div><h3>Aire</h3><div class="hours">45 pp</div></div>': '<div class="unit-title"><div class="id">U3</div><h3>Aire</h3><div class="hours">24 pp</div></div>',
        '<div class="unit-title"><div class="id">Cierre</div><h3>Cierre integrador</h3><div class="hours">18 pp</div></div>': '<div class="unit-title"><div class="id">Cierre</div><h3>Cierre del semestre</h3><div class="hours">21 pp</div></div>',
    }
    for old, new in replacements.items():
        base = base.replace(old, new)
    return base


def element_cell(num: int, symbol: str, group: int, period: int, cls: str) -> str:
    return (
        f'<div class="element {e(cls)}" style="grid-column:{group}; grid-row:{period};">'
        f'<span class="num">{num}</span><strong>{e(symbol)}</strong></div>'
    )


def appendix_cover(number: int, title: str, subtitle: str, goals: list[str]) -> str:
    items = "".join(f"<li>{e(goal)}</li>" for goal in goals)
    body = f"""
    <div>
      <p class="kicker">{e('Portada de trimestre ' + str(number))}</p>
      <h2>{e(title)}</h2>
      <p class="subtitle">{e(subtitle)}</p>
    </div>
    <div class="appendix-panel">
      <h3>Proposito de trabajo</h3>
      <ul>{items}</ul>
    </div>
    {footer('Colegio Nuevo Tecno', 'Separador de trimestre ' + str(number))}
    """
    return section(body, "page appendix-cover")


def appendix_cards_page(kicker: str, title: str, subtitle: str, cards: list[tuple[str, str]], foot: str) -> str:
    card_html = "".join(
        f'<div class="appendix-card"><h3>{e(name)}</h3><p>{e(text)}</p></div>' for name, text in cards
    )
    body = f"""
    <p class="kicker">{e(kicker)}</p>
    <h2>{e(title)}</h2>
    <p class="subtitle">{e(subtitle)}</p>
    <div class="appendix-grid">{card_html}</div>
    {footer('Colegio Nuevo Tecno', foot)}
    """
    return section(body)


def reading_page(number: int, title: str, paragraphs: list[str], questions: list[str]) -> str:
    text = "".join(f"<p>{e(p)}</p>" for p in paragraphs)
    question_html = "".join(
        f'<div class="question"><p>{idx}. {e(q)}</p><div class="answer-lines"><span></span><span></span><span></span></div></div>'
        for idx, q in enumerate(questions, 1)
    )
    body = f"""
    <p class="kicker">{e('Lectura complementaria ' + str(number))}</p>
    <h2>{e(title)}</h2>
    <div class="reading-text">{text}</div>
    <div class="questions">
      <h3>Preguntas de comprension</h3>
      <div class="questions-grid">{question_html}</div>
    </div>
    {footer('Colegio Nuevo Tecno', 'Lectura complementaria ' + str(number))}
    """
    return section(body)


def periodic_table_page() -> str:
    table = "".join(element_cell(*item) for item in ELEMENTS)
    body = f"""
    <p class="kicker">Material complementario / tabla periodica</p>
    <h2>Tabla periodica de referencia</h2>
    <p class="subtitle">Usala para ubicar numero atomico, familias, metales, no metales, halogenos, gases nobles, lantanidos y actinidos antes de resolver ejercicios de materia, enlaces y mol.</p>
    <div class="periodic-table" aria-label="Tabla periodica con numero atomico y simbolo">{table}</div>
    <div class="note"><strong>Lectura rapida:</strong> los grupos son columnas, los periodos son filas. El numero atomico indica protones; el simbolo identifica el elemento en formulas y ecuaciones.</div>
    {footer('Colegio Nuevo Tecno', 'Tabla periodica')}
    """
    return section(body)


def mini_table_page(kicker: str, title: str, subtitle: str, headers: list[str], rows: list[list[str]], foot: str) -> str:
    head = "".join(f"<th>{e(h)}</th>" for h in headers)
    def cell_html(cell: str) -> str:
        if cell.startswith("http://") or cell.startswith("https://"):
            return f'<td><a href="{e(cell)}">{e(cell)}</a></td>'
        return f"<td>{e(cell)}</td>"

    row_html = "".join("<tr>" + "".join(cell_html(cell) for cell in row) + "</tr>" for row in rows)
    body = f"""
    <p class="kicker">{e(kicker)}</p>
    <h2>{e(title)}</h2>
    <p class="subtitle">{e(subtitle)}</p>
    <table class="mini-table"><thead><tr>{head}</tr></thead><tbody>{row_html}</tbody></table>
    {footer('Colegio Nuevo Tecno', foot)}
    """
    return section(body)


def supplemental_pages() -> str:
    pages: list[str] = []
    pages.append(appendix_cover(1, "Trimestre 1 - Lenguaje quimico y materia", "Separador para iniciar el trabajo con medicion, modelos, sustancias, atomos, tabla periodica y mol.", [
        "Usar instrumentos y unidades con criterio.",
        "Clasificar materia visible e invisible.",
        "Conectar formulas quimicas con masas y particulas.",
    ]))
    pages.append(appendix_cover(2, "Trimestre 2 - Agua", "Separador para trabajar estructura molecular del agua, pH, soluciones, concentracion, contaminacion y tratamiento.", [
        "Medir propiedades del agua con registro claro.",
        "Interpretar pH, ppm, molaridad y diluciones.",
        "Proponer acciones de cuidado con evidencia.",
    ]))
    pages.append(appendix_cover(3, "Trimestre 3 - Aire y cierre", "Separador para cerrar el semestre con aire, combustion, redox, contaminacion, lluvia acida y examen integrador.", [
        "Relacionar aire, agua y entorno escolar.",
        "Balancear reacciones y estimar cantidades.",
        "Cerrar el caso conductor con decision tecnica.",
    ]))
    pages.append(periodic_table_page())
    pages.append(appendix_cards_page("Material complementario", "Como leer la tabla periodica", "La tabla periodica no se memoriza como lista: se usa como mapa para tomar decisiones quimicas.", [
        ("Numero atomico", "Indica la cantidad de protones. En un atomo neutro tambien coincide con el numero de electrones."),
        ("Grupo", "Columna vertical. Ayuda a inferir electrones de valencia y comportamiento quimico."),
        ("Periodo", "Fila horizontal. Indica el nivel energetico principal ocupado."),
        ("Familia", "Metales alcalinos, alcalinoterreos, halogenos y gases nobles comparten patrones de reaccion."),
        ("Masa atomica", "Promedio ponderado de isotopos. Se usa para calcular masa molar."),
        ("Tendencia", "Radio, electronegatividad y energia de ionizacion cambian de forma ordenada en la tabla."),
    ], "Uso de tabla periodica"))
    pages.append(mini_table_page("Material complementario", "Unidades y conversiones de uso frecuente", "Antes de calcular, revisa que las magnitudes esten en unidades compatibles.", ["Magnitud", "Unidad comun", "Conversion util", "Uso en el manual"], [
        ["Volumen", "mL, L", "1000 mL = 1 L", "Molaridad, diluciones y muestras de agua"],
        ["Masa", "g, kg, mg", "1000 mg = 1 g", "Soluto, densidad, ppm y masa molar"],
        ["Temperatura", "C, K", "K = C + 273.15", "Gases y energia"],
        ["Cantidad", "mol", "1 mol = 6.022 x 10^23 particulas", "Moles, particulas y formulas"],
        ["Concentracion", "mol/L, ppm", "ppm en agua = mg/L", "Calidad del agua"],
        ["Presion", "atm, Pa", "1 atm = 101325 Pa", "Gas ideal y aire"],
    ], "Tabla de unidades"))
    pages.append(mini_table_page("Material complementario", "Bitacora de laboratorio", "Usa esta hoja como registro base cada vez que trabajes con muestra, instrumento y conclusion.", ["Dato", "Registro esperado", "Espacio de trabajo"], [
        ["Fecha y equipo", "Quien mide y cuando", ""],
        ["Muestra", "Origen, recipiente y condicion inicial", ""],
        ["Instrumento", "Nombre, escala y limite de lectura", ""],
        ["Variable", "Que se mide y en que unidad", ""],
        ["Resultado", "Dato con unidad y posible error", ""],
        ["Conclusion", "Que decision permite tomar", ""],
    ], "Bitacora"))
    pages.append(mini_table_page("Material complementario", "Formato de muestreo de agua escolar", "Esta tabla evita que el diagnostico del bebedero dependa solo de memoria o impresion visual.", ["Paso", "Accion", "Evidencia"], [
        ["1", "Lavar o identificar el recipiente de muestra.", ""],
        ["2", "Registrar hora, lugar, temperatura y aspecto.", ""],
        ["3", "Medir pH con tira, sensor o indicador disponible.", ""],
        ["4", "Medir volumen y masa cuando el ejercicio lo requiera.", ""],
        ["5", "Anotar olor, color, turbidez o sedimento sin exagerar.", ""],
        ["6", "Cerrar con una pregunta investigable para la siguiente prueba.", ""],
    ], "Muestreo"))
    pages.append(mini_table_page("Material complementario", "Rubrica breve para reportes", "El reporte final debe mostrar evidencia, calculo y decision; no basta con describir la actividad.", ["Criterio", "Excelente", "En proceso"], [
        ["Datos", "Incluye unidades, instrumento y condiciones.", "Faltan unidades o contexto."],
        ["Calculos", "Formula, sustitucion y resultado son visibles.", "Solo aparece el resultado."],
        ["Conceptos", "Relaciona materia, agua y aire con precision.", "Usa conceptos aislados."],
        ["Conclusion", "Toma una decision basada en evidencia.", "Opina sin justificar."],
        ["Fuentes", "Cita recurso y dato consultado.", "Solo pega una liga."],
        ["Presentacion", "Orden claro y lectura limpia.", "Informacion dispersa."],
    ], "Rubrica"))
    pages.append(appendix_cards_page("Material complementario", "Glosario esencial del semestre", "Estos terminos deben aparecer correctamente en ejercicios, reportes y examen integrador.", [
        ("Variable", "Magnitud que cambia o se controla durante una prueba."),
        ("Error absoluto", "Diferencia directa entre valor experimental y valor aceptado."),
        ("Masa molar", "Masa de un mol de sustancia, expresada en g/mol."),
        ("Solucion", "Mezcla homogenea formada por soluto y solvente."),
        ("pH", "Escala que expresa acidez o basicidad."),
        ("Redox", "Proceso donde ocurre transferencia de electrones."),
        ("Densidad", "Relacion entre masa y volumen: d = m / V."),
        ("ppm", "Partes por millon; en agua se usa como mg/L."),
    ], "Glosario"))
    pages.append(mini_table_page("Material complementario", "Banco de datos del caso conductor", "Estos datos simulados pueden usarse para ejercicios extra sin inventar nuevos contextos.", ["Dato", "Valor", "Uso posible"], [
        ["Volumen de muestra", "250 mL", "Conversion a L y calculo de concentracion"],
        ["Masa de residuo seco", "0.18 g", "Estimacion de solidos disueltos"],
        ["pH inicial", "6.4", "Comparacion con neutralidad"],
        ["Cloro residual", "0.35 ppm", "Lectura de mg/L"],
        ["Temperatura", "28 C", "Conversion a K"],
        ["Masa de vaso vacio", "52.40 g", "Densidad y medicion indirecta"],
    ], "Datos del caso"))
    pages.append(reading_page(1, "Cuando medir cambio la quimica", [
        "Durante siglos, muchas explicaciones sobre la materia se aceptaban porque sonaban razonables. La quimica moderna cambio cuando las balanzas, recipientes graduados y registros permitieron comparar resultados entre personas distintas.",
        "Medir no elimina todas las dudas, pero obliga a escribir de donde sale cada afirmacion. Un dato con unidad permite repetir una prueba; una impresion solo permite discutir.",
        "En el caso del bebedero, la diferencia entre sospecha y evidencia aparece cuando se registra volumen, masa, pH, temperatura y condiciones de la muestra.",
    ], [
        "Que ventaja tiene una medicion frente a una descripcion visual?",
        "Que dato seria indispensable para repetir una prueba del bebedero?",
        "Como puede afectar una unidad incorrecta a una conclusion?",
    ]))
    pages.append(reading_page(2, "Del atomo imaginado al modelo util", [
        "Los modelos atomicos no fueron dibujos decorativos; fueron respuestas cada vez mejores a preguntas concretas. Dalton ayudo a pensar la materia como particulas, Thomson mostro que el atomo tenia partes, Rutherford propuso un nucleo y Bohr organizo niveles de energia.",
        "Un modelo se conserva mientras explica datos y se modifica cuando ya no alcanza. Por eso estudiar la historia del atomo ayuda a entender que la ciencia corrige sus herramientas.",
        "Cuando interpretas iones disueltos en agua, usas modelos atomicos para explicar cargas, enlaces y comportamiento en solucion.",
    ], [
        "Por que un modelo cientifico puede cambiar sin que la ciencia fracase?",
        "Que modelo ayuda a explicar la existencia de iones?",
        "Como se relaciona la historia atomica con el agua del bebedero?",
    ]))
    pages.append(reading_page(3, "Agua clara no significa agua simple", [
        "Una muestra transparente puede contener iones, gases disueltos, pequenas cantidades de solutos o contaminantes que no se distinguen a simple vista. La claridad es una observacion, no una garantia.",
        "El agua es un solvente poderoso por su polaridad. Esa propiedad permite transportar sales y otras sustancias, pero tambien exige medir para saber que contiene.",
        "Por eso el analisis de agua combina observacion, pH, concentracion, posibles contaminantes y una conclusion responsable.",
    ], [
        "Por que la transparencia no basta para evaluar calidad del agua?",
        "Que relacion tiene la polaridad con las sales disueltas?",
        "Que medicion pedirias primero y por que?",
    ]))
    pages.append(reading_page(4, "pH: una escala pequena con decisiones grandes", [
        "El pH resume la acidez o basicidad de una solucion. Aunque parece un numero sencillo, representa una relacion logaritmica con la concentracion de iones hidrogeno.",
        "Un cambio de una unidad de pH no siempre debe interpretarse como un cambio pequeno. Por eso conviene comparar con controles, registrar instrumento y evitar conclusiones apresuradas.",
        "En una muestra escolar, el pH ayuda a decidir si se requieren pruebas adicionales, pero no reemplaza otros datos como olor, concentracion, cloro o presencia de solidos.",
    ], [
        "Que representa el pH de manera general?",
        "Por que no conviene interpretar pH sin contexto?",
        "Que otro dato combinarias con el pH del bebedero?",
    ]))
    pages.append(reading_page(5, "Aire, combustion y agua en el mismo entorno", [
        "El aire es una mezcla de gases. Aunque no se vea como una sustancia dentro del vaso, puede influir en el entorno del agua mediante particulas, combustion, dioxido de carbono y lluvia con cierta acidez.",
        "Una fuente de combustion cercana puede producir gases que despues reaccionan, se disuelven o modifican condiciones ambientales. El diagnostico escolar mejora cuando observa agua y aire como sistemas conectados.",
        "La quimica ambiental no busca alarmar: busca identificar fuentes, medir efectos y proponer acciones realistas.",
    ], [
        "Por que el aire debe considerarse en el caso del bebedero?",
        "Que fuente de combustion podria investigarse cerca del colegio?",
        "Que dato ayudaria a distinguir sospecha de evidencia?",
    ]))
    pages.append(reading_page(6, "De la formula a la decision", [
        "Una formula no es solo una expresion para sustituir numeros. Es una forma compacta de decir que magnitudes se relacionan y bajo que unidades deben compararse.",
        "Cuando calculas densidad, molaridad, porcentaje, error o moles de gas, estas traduciendo una situacion real a una relacion verificable. Si la unidad no coincide, la decision se debilita.",
        "El cierre del manual pide unir historia, imagen, concepto, formula, ejercicio y conclusion para proponer una respuesta al caso conductor.",
    ], [
        "Por que una formula debe explicarse antes de resolver ejercicios?",
        "Que ocurre si mezclas mL y L sin convertir?",
        "Como conecta un calculo con una decision del caso?",
    ]))
    pages.append(mini_table_page("Material complementario", "Recursos ampliados para consulta", "Usa estos recursos para resolver dudas, ampliar teoria o contrastar datos antes del reporte final.", ["Recurso", "Uso sugerido", "Liga"], [
        ["IUPAC", "Tabla periodica y nomenclatura", "https://iupac.org/"],
        ["PhET", "Simulaciones de quimica", "https://phet.colorado.edu/es/simulations/filter?subjects=chemistry"],
        ["NIST Chemistry WebBook", "Datos de sustancias", "https://webbook.nist.gov/chemistry/"],
        ["PubChem", "Propiedades de compuestos", "https://pubchem.ncbi.nlm.nih.gov/"],
        ["OpenStax Chemistry", "Lecturas de apoyo", "https://openstax.org/details/books/chemistry-2e"],
        ["Khan Academy Quimica", "Repaso de conceptos", "https://es.khanacademy.org/science/chemistry"],
    ], "Recursos ampliados"))
    return "\n".join(pages)


def closure_pages() -> str:
    exam_items = [
        "Disena una ruta de muestreo para revisar agua, materia disuelta y posible influencia del aire.",
        "Clasifica una muestra con sales disueltas como sustancia pura o mezcla y justifica.",
        "Calcula pH, concentracion o dilucion con unidades visibles.",
        "Explica una reaccion del aire que pueda afectar la calidad del agua.",
        "Redacta una conclusion tecnica para la comunidad escolar.",
    ]
    resources = [
        ("IUPAC Periodic Table", "https://iupac.org/what-we-do/periodic-table-of-elements/"),
        ("PhET Chemistry", "https://phet.colorado.edu/es/simulations/filter?subjects=chemistry"),
        ("NIST Chemistry WebBook", "https://webbook.nist.gov/chemistry/"),
        ("PubChem", "https://pubchem.ncbi.nlm.nih.gov/"),
    ]
    exam = "".join(
        f'<div class="bank-item"><p><strong>{i}.</strong> {e(item)}</p><div class="bank-lines"><span></span><span></span><span></span></div></div>'
        for i, item in enumerate(exam_items, 1)
    )
    links = "".join(f'<li><strong>{e(name)}:</strong> <a href="{e(url)}">{e(url)}</a></li>' for name, url in resources)
    index = [
        "Metodo cientifico: U0",
        "Sistema Internacional y error: U0",
        "Materia, mezcla, atomo, tabla periodica, enlaces y mol: U1",
        "Agua, polaridad, pH, soluciones, contaminacion y tratamiento: U2",
        "Aire, combustion, redox, ciclos y lluvia acida: U3",
    ]
    pages = []
    pages.append(section(f"""
    <p class="kicker">Cierre del manual</p>
    <h2>Examen integrador</h2>
    <p class="subtitle">El examen recupera el caso Agua escolar saludable y exige decidir con evidencia, no solo repetir conceptos.</p>
    <div class="exercise-bank">{exam}</div>
    {footer('Colegio Nuevo Tecno', 'Cierre / examen integrador')}
    """))
    pages.append(section(f"""
    <p class="kicker">Cierre del manual</p>
    <h2>Bibliografia y recursos</h2>
    <p class="subtitle">Estas fuentes sirven para ampliar conceptos, contrastar datos y revisar definiciones tecnicas.</p>
    <div class="note"><strong>Uso responsable:</strong> consulta la fuente, registra la liga y explica que dato tomaste de ella.</div>
    <ul>{links}</ul>
    {footer('Colegio Nuevo Tecno', 'Cierre / recursos')}
    """))
    pages.append(section(f"""
    <p class="kicker">Cierre del manual</p>
    <h2>Indice analitico basico</h2>
    <div class="concept-list">{''.join(f'<div class="concept"><strong>{e(item.split(":")[0])}</strong>{e(item)}</div>' for item in index)}</div>
    {footer('Colegio Nuevo Tecno', 'Cierre / indice analitico')}
    """))
    return "\n".join(pages)


UNIT_DATA = [
    {
        "unit": "u01",
        "title": "U1 - Temas Basicos de la Materia",
        "short": "U1 / Materia",
        "kicker": "Unidad 1 / Temas Basicos de la Materia",
        "story": "La etiqueta del analisis externo dice dureza, cloro residual y sodio. Tres numeros abren una pregunta mayor: que hay dentro del agua aunque no se vea?",
        "case_link": "En el caso conductor, esta unidad baja del agua visible al nivel de particulas, iones, enlaces y cantidad de sustancia.",
        "cover_phrase": "La materia no empieza donde la vista termina: empieza cuando sabes leer lo invisible con modelos.",
        "start_activity": "Toma una etiqueta real o simulada de agua potable y subraya todas las sustancias, iones o unidades que aparezcan.",
        "intro_title": "Ver lo invisible sin inventarlo",
        "intro_1": "La muestra del bebedero puede verse transparente y aun asi contener iones, sales y moleculas. La quimica permite nombrar esa composicion y calcular cuanta materia participa.",
        "intro_2": "Para no confundir apariencia con evidencia, la unidad conecta clasificacion de materia, estructura atomica, tabla periodica, enlaces, nomenclatura y mol.",
        "central_idea": "Una muestra se entiende cuando sabes clasificarla, nombrarla, representarla y calcularla.",
        "concepts": [
            ("Materia", "Todo lo que tiene masa y ocupa espacio."),
            ("Mezcla", "Sistema con mas de una sustancia."),
            ("Atomo", "Unidad basica para explicar elementos."),
            ("Ion", "Particula con carga por perdida o ganancia de electrones."),
            ("Enlace", "Interaccion que mantiene unidos atomos o iones."),
            ("Mol", "Puente entre gramos y particulas."),
        ],
        "questions": [
            "Que puede estar disuelto aunque el agua se vea clara?",
            "Por que la tabla periodica ayuda a predecir enlaces?",
            "Como conectas una formula quimica con una masa medible?",
        ],
        "concept_frame": "La materia se interpreta con modelos: mezcla, sustancia, atomo, ion, enlace y mol.",
        "decision_frame": "Cada concepto ayuda a decidir que hay en el agua y que prueba conviene hacer despues.",
        "data_frame": "Nombre de sustancia, formula, masa molar, tipo de enlace, carga y cantidad de muestra.",
        "error_frame": "Confundir formula con nombre comun, o calcular moles sin masa molar correcta.",
        "development_prompt": "Usa el visual como ejemplo y aplica la idea a una posible sal disuelta en el bebedero.",
        "default_phrase": "Cada modelo de la materia es una forma de ordenar lo que no se puede observar directamente.",
        "default_mini": "Elige una sustancia posible del agua escolar y explica como la representarias con nombre, formula y dato medible.",
        "topics": {
            2: "Recorrido de la materia en el caso",
            3: "Sustancias puras y mezclas",
            4: "Modelos atomicos: una historia de mejores explicaciones",
            5: "Isotopos y masa atomica",
            6: "Configuracion electronica",
            7: "Tabla periodica como mapa de decision",
            8: "Lewis y electrones de valencia",
            9: "Tendencias periodicas",
            10: "Tipos de enlace",
            11: "Fuerzas intermoleculares",
            12: "Nomenclatura inorganica",
            13: "Mol, masa molar y particulas",
            14: "Iones hidratados en el agua",
        },
        "dense_visuals": [2, 4, 7, 9, 10, 12],
        "landscape_visuals": [3, 5, 6, 8, 11, 13, 14],
        "activity_kinds": {
            4: "open",
            5: "calc",
            6: "match",
            7: "compare",
            8: "table",
            9: "calc",
            10: "compare",
            11: "open",
            12: "match",
            13: "calc",
            14: "explain",
        },
        "activity_specs": {
            4: {
                "title": "Preguntas abiertas sobre modelos atomicos",
                "questions": [
                    "Que dato experimental obligo a cambiar un modelo atomico anterior?",
                    "Por que el modelo de Bohr sirve para explicar niveles de energia, pero no basta para todos los atomos?",
                    "Como usarias un modelo atomico para explicar que un ion puede estar disuelto en el bebedero?",
                ],
            },
            5: {
                "title": "Comprobacion con calculos de isotopos",
                "instruction": "Calcula neutrones en Cl-35 y Cl-37 usando N = A - Z, con Z = 17. Despues explica por que ambos siguen siendo cloro aunque tengan distinta masa.",
                "steps": ["Formula N = A - Z.", "Sustitucion para Cl-35.", "Sustitucion para Cl-37.", "Conclusion sobre isotopos y masa atomica."],
            },
            6: {
                "title": "Investigacion guiada y relacion de columnas",
                "instruction": "Investiga por tu cuenta que significan Aufbau, Hund y Pauli antes de relacionar. En tu cuaderno anota: definicion breve, ejemplo de aplicacion y fuente consultada. Despues relaciona las parejas en formato A-__, B-__, C-__.",
                "left_items": [("A", "Principio de Aufbau"), ("B", "Regla de Hund"), ("C", "Principio de Pauli")],
                "right_items": [("1", "Un orbital acepta maximo dos electrones con espines opuestos."), ("2", "Los electrones ocupan primero los orbitales de menor energia."), ("3", "En orbitales equivalentes, los electrones se distribuyen primero desapareados.")],
            },
            7: {
                "title": "Cuadro comparativo: sodio y cloro en la tabla periodica",
                "left": "Sodio (Na)",
                "right": "Cloro (Cl)",
                "instruction": "Compara sodio y cloro usando la tabla periodica. Completa grupo, periodo, tendencia esperada y prediccion de ion; al final explica por que pueden formar NaCl.",
                "criteria": ["Grupo y periodo", "Metal o no metal", "Electron de valencia o tendencia", "Ion que tiende a formar", "Relacion con NaCl"],
            },
            8: {
                "title": "Tabla de Lewis: electrones de valencia",
                "instruction": "Completa la tabla con electrones de valencia y una representacion de Lewis. Usa puntos para electrones libres y una linea para electrones compartidos cuando aplique.",
                "headers": ["Especie", "Electrones de valencia", "Estructura de Lewis", "Que muestra"],
                "rows": [["Cl", "", "", "Atomo con electrones de valencia"], ["H2O", "", "", "Pares compartidos y pares libres"], ["NaCl", "", "", "Transferencia de electrones / iones"]],
            },
            9: {
                "title": "Comprobacion con diferencia de electronegatividad",
                "instruction": "Usa valores de electronegatividad aproximados: Na = 0.9, Cl = 3.0, H = 2.1 y O = 3.5. Calcula Delta EN para Na-Cl y O-H; despues decide cual enlace es mas polar.",
                "steps": ["Formula Delta EN = valor mayor - valor menor.", "Calculo para Na-Cl.", "Calculo para O-H.", "Conclusion sobre polaridad."],
            },
            10: {
                "title": "Cuadro comparativo: enlace ionico y covalente",
                "left": "Enlace ionico",
                "right": "Enlace covalente",
                "instruction": "Compara enlace ionico y covalente. Usa NaCl y H2O como ejemplos y concluye cual ayuda a explicar sales disueltas en el bebedero.",
                "criteria": ["Particulas que participan", "Que ocurre con los electrones", "Ejemplo", "Relacion con agua escolar"],
            },
            11: {
                "title": "Preguntas abiertas sobre fuerzas intermoleculares",
                "questions": [
                    "Por que las fuerzas entre moleculas pueden cambiar punto de ebullicion o solubilidad?",
                    "Que fuerza ayuda a explicar propiedades especiales del agua?",
                    "Como se conectan estas fuerzas con la disolucion de sustancias en el bebedero?",
                ],
            },
            12: {
                "title": "Relacion de columnas: formula, nombre y sistema",
                "instruction": "Relaciona cada formula con el nombre o sistema correcto. Escribe las parejas en formato A-__, B-__, C-__, D-__.",
                "left_items": [("A", "NaCl"), ("B", "CaCO3"), ("C", "CO2"), ("D", "FeCl3")],
                "right_items": [("1", "Cloruro de hierro(III), sistema Stock"), ("2", "Cloruro de sodio, sal binaria"), ("3", "Dioxido de carbono, prefijos"), ("4", "Carbonato de calcio, oxisal")],
            },
            13: {
                "title": "Comprobacion con mol y masa molar",
                "instruction": "Calcula moles y particulas para 5.85 g de NaCl. Usa M = 58.5 g/mol y NA = 6.022 x 10^23 particulas/mol.",
                "steps": ["Formula n = m / M.", "Sustitucion con gramos y g/mol.", "Formula N = n x NA.", "Resultado con unidades y significado."],
            },
            14: {
                "title": "Explicacion con evidencia: ion hidratado",
                "instruction": "Explica por que Na+ y Cl- no quedan aislados al disolverse en agua. Menciona carga, polaridad del agua y orientacion de las moleculas alrededor del ion.",
                "steps": ["Ion elegido y carga.", "Parte de H2O que se orienta hacia el ion.", "Evidencia o dibujo esperado.", "Decision para estudiar sales del bebedero."],
            },
        },
        "visual_intros": {
            2: "La muestra del bebedero obliga a seguir una ruta: primero se observa, despues se clasifica, luego se representa y al final se calcula.",
            3: "Antes de medir pH, masa o concentracion, el equipo debe decidir si mira una sustancia pura, un compuesto o una mezcla.",
            4: "La historia atomica muestra que la quimica no adivina lo invisible: construye modelos cada vez mas utiles para explicar datos.",
            5: "Algunas diferencias entre atomos no se ven a simple vista, pero cambian la masa y la forma en que interpretamos una muestra.",
            6: "Los electrones ayudan a explicar por que un elemento forma iones, enlaces o sustancias estables en el agua.",
            7: "La tabla periodica permite decidir donde buscar propiedades antes de memorizar nombres sueltos.",
            8: "Los puntos de Lewis vuelven visible una pregunta simple: cuantos electrones participan en un enlace?",
            9: "Las tendencias periodicas permiten anticipar que elemento atrae mas electrones o cambia de tamano con mayor facilidad.",
            10: "Cuando las particulas se unen, la muestra deja de ser una lista de atomos y se vuelve una estructura con propiedades.",
            11: "Entre moleculas tambien existen fuerzas: algunas explican por que una sustancia se disuelve, hierve o permanece unida.",
            12: "Los sistemas de nomenclatura organizan el nombre de las sustancias. Como el cuadro contiene mucha informacion, esta pagina se reserva para leerlo con calma antes de practicar.",
            13: "El mol permite pasar de una formula escrita en el cuaderno a una cantidad que puede medirse en gramos.",
            14: "Cuando un ion entra en agua, no queda aislado: las moleculas de agua lo rodean y cambian su comportamiento.",
        },
        "phrases": {
            2: "La ruta no es una lista para memorizar: es una historia de decisiones hasta llegar a una conclusion.",
            3: "Clasificar no es etiquetar por costumbre: es decidir que tipo de sistema tienes antes de medirlo.",
            7: "La tabla periodica funciona como un mapa: no resuelve el viaje, pero evita caminar a ciegas.",
            12: "Un nombre quimico bien elegido permite reconstruir la formula sin depender de la memoria.",
            13: "El mol traduce el mundo invisible de particulas al mundo medible de gramos.",
        },
        "mini": {
            2: "Cuenta en cuatro pasos como pasarias de observar agua transparente a proponer una prueba quimica concreta.",
            3: "Clasifica rapidamente: agua destilada, aire del salon y agua con arena. Indica si cada una es sustancia pura, compuesto o mezcla.",
            4: "Elige dos modelos atomicos y escribe que problema resolvio cada uno en una frase.",
            5: "Lee la pagina siguiente antes de calcular: usa la analogia de credenciales para explicar por que dos isotopos conservan el mismo Z aunque cambie A.",
            6: "Investiga por tu cuenta que significan Aufbau, Hund y Pauli. Anota una definicion corta de cada regla antes de pasar a la relacion de columnas.",
            7: "Ubica Na, Cl y Ca en la tabla periodica y anota grupo, periodo y una propiedad esperada.",
            8: "Lee la guia de Lewis de la pagina siguiente antes de dibujar. Subraya donde se explican electrones de valencia, pares libres y pares compartidos.",
            9: "Ordena F, Cl y Br por electronegatividad y justifica con la tendencia periodica.",
            10: "Propone un ejemplo de enlace ionico y uno covalente que puedan relacionarse con agua escolar.",
            11: "Explica por que una fuerza intermolecular puede cambiar solubilidad o punto de ebullicion.",
            12: "Nombra NaCl, CaCO3 y CO2; separa nombre comun, formula y tipo de compuesto.",
            13: "Convierte una masa dada de NaCl a mol y escribe que representa ese numero en particulas.",
            14: "Dibuja un ion rodeado por moleculas de agua y explica por que esa hidratacion importa.",
        },
        "special_concept_pages": {
            2: {
                "title": "La muestra que obligo a ordenar la materia",
                "paragraphs": [
                    "El equipo inicio con un vaso de agua que parecia normal. La primera tentacion fue saltar directo al pH, pero la muestra traia una pregunta anterior: que clase de materia estamos observando?",
                    "Primero se distinguio lo visible de lo disuelto. Luego aparecieron palabras que cambiaron la investigacion: mezcla, sustancia, ion, formula, enlace y mol. Cada palabra abrio una decision. Si era mezcla, habia que pensar en composicion; si habia iones, habia que revisar cargas; si habia una formula, habia que convertirla en masa o cantidad.",
                    "Asi, el recorrido de la unidad no funciona como una lista decorativa. Funciona como la historia de una muestra que obliga a pasar de la apariencia a la evidencia.",
                ],
                "cards": [
                    ("Primera decision", "Distinguir si el sistema observado es una sustancia pura o una mezcla."),
                    ("Segunda decision", "Reconocer si aparecen atomos, moleculas o iones en la explicacion."),
                    ("Tercera decision", "Usar nombre, formula y tabla periodica para representar la sustancia."),
                    ("Cuarta decision", "Calcular cantidad de materia cuando la pregunta exige masa, mol o particulas."),
                ],
                "exercise_title": "Relato de decisiones del caso",
                "exercise": "Escribe una historia de seis pasos donde el equipo pasa de observar el bebedero a decidir que dato quimico necesita medir primero.",
                "steps": [
                    "Observacion inicial de la muestra.",
                    "Clasificacion de la materia.",
                    "Particula o sustancia que podria estar presente.",
                    "Formula, unidad o dato necesario.",
                ],
            },
            3: {
                "title": "Sustancias puras y mezclas: clasificar antes de medir",
                "split_after_cards": True,
                "activity_page_title": "Tabla de clasificacion de sustancias y mezclas",
                "paragraphs": [
                    "Una sustancia pura tiene composicion definida. Puede ser un elemento, si esta formada por un solo tipo de atomo, o un compuesto, si contiene atomos de distintos elementos unidos quimicamente en proporcion fija.",
                    "Una mezcla contiene dos o mas sustancias juntas sin que todas formen una sola sustancia nueva. Si su composicion se ve uniforme, se llama mezcla homogenea; si se distinguen fases o partes, se llama mezcla heterogenea.",
                    "Esta diferencia importa en el caso del bebedero: el agua con sales disueltas no se clasifica igual que el agua destilada, y tampoco se estudia igual que agua con arena o sedimento visible.",
                ],
                "card_class": "classification-defs",
                "cards": [
                    ("Sustancia pura", "Materia con composicion fija y propiedades caracteristicas."),
                    ("Elemento", "Sustancia pura formada por un solo tipo de atomo, como Fe u O2."),
                    ("Compuesto", "Sustancia pura formada por elementos unidos quimicamente, como H2O o NaCl."),
                    ("Mezcla homogenea", "Sistema uniforme; no se distinguen sus componentes a simple vista."),
                    ("Mezcla heterogenea", "Sistema no uniforme; se distinguen fases, particulas o regiones."),
                    ("Criterio de separacion", "Si se separa por metodos fisicos, se trata de mezcla; si requiere reaccion quimica, puede ser compuesto."),
                ],
                "table": {
                    "title": "Tabla de clasificacion",
                    "instruction": "Indica si cada ejemplo es elemento, compuesto, mezcla homogenea o mezcla heterogenea. Justifica con una razon observable o quimica.",
                    "headers": ["Ejemplo", "Pista", "Clasificacion", "Justificacion"],
                    "rows": [
                        ["Agua destilada", "H2O sin solutos apreciables", "", ""],
                        ["Agua del bebedero con sales", "Se ve uniforme, contiene iones", "", ""],
                        ["Cloruro de sodio", "Formula NaCl", "", ""],
                        ["Hierro", "Simbolo Fe", "", ""],
                        ["Aire", "Varios gases mezclados", "", ""],
                        ["Agua con arena", "Se observa sedimento", "", ""],
                        ["Dioxido de carbono", "Formula CO2", "", ""],
                        ["Jugo con pulpa", "Tiene partes visibles", "", ""],
                    ],
                },
                "exercise_title": "Tabla de clasificacion y comprobacion",
                "exercise": "Selecciona dos ejemplos de la tabla y explica que prueba sencilla permitiria sostener tu clasificacion.",
                "steps": [
                    "Ejemplo elegido.",
                    "Tipo de materia.",
                    "Evidencia usada.",
                    "Prueba o separacion posible.",
                ],
            },
            5: {
                "title": "Isotopos: misma identidad, distinta masa",
                "paragraphs": [
                    "Imagina que dos estudiantes pertenecen al mismo colegio y tienen la misma credencial institucional, pero cargan mochilas con distinto peso. La credencial identifica a la institucion; la mochila cambia la masa que llevan. Con los isotopos ocurre algo parecido: el numero atomico Z identifica al elemento, mientras que los neutrones pueden cambiar la masa.",
                    "Un isotopo es una version de un mismo elemento. Conserva el mismo numero de protones, por eso sigue siendo el mismo elemento, pero puede tener diferente numero de neutrones. Si cambia el numero de protones, ya no seria el mismo elemento.",
                    "En quimica usamos A para numero masico, Z para numero atomico y N para neutrones. La relacion es A = Z + N. Si necesitas encontrar neutrones, despejas: N = A - Z.",
                ],
                "cards": [
                    ("Z: numero atomico", "Indica protones. Es la identidad del elemento. Si Z = 17, el elemento es cloro."),
                    ("A: numero masico", "Suma protones y neutrones. Por eso puede cambiar entre isotopos del mismo elemento."),
                    ("N: neutrones", "Se calculan con N = A - Z. No cambian la identidad del elemento, pero si la masa."),
                    ("Unidad y cuidado", "A, Z y N son conteos de particulas; no se expresan en gramos ni litros."),
                ],
                "exercise_title": "Comprobacion con isotopos",
                "exercise": "Calcula neutrones en Cl-35 y Cl-37 usando Z = 17. Despues explica por que ambos siguen siendo cloro aunque uno tenga mas neutrones.",
                "steps": [
                    "Escribe la formula N = A - Z.",
                    "Sustituye A = 35 y Z = 17.",
                    "Sustituye A = 37 y Z = 17.",
                    "Explica que permanece igual y que cambia.",
                ],
            },
            8: {
                "title": "Lewis: contar electrones antes de dibujar",
                "paragraphs": [
                    "La estructura de Lewis es una forma simple de representar electrones de valencia. No muestra todos los electrones del atomo: solo los que participan con mayor facilidad en enlaces o quedan como pares libres alrededor del simbolo.",
                    "La analogia es una mesa con lugares disponibles. Cada electron de valencia es un lugar que puede quedar libre, compartirse o participar en una transferencia. Antes de dibujar enlaces, primero se cuentan esos lugares.",
                    "Para elementos representativos, los electrones de valencia se estiman con el grupo de la tabla periodica: grupo 1 tiene 1, grupo 2 tiene 2, grupo 13 tiene 3, grupo 14 tiene 4, grupo 15 tiene 5, grupo 16 tiene 6, grupo 17 tiene 7 y grupo 18 tiene 8, salvo helio que tiene 2.",
                    "Al dibujar Lewis: 1) escribe el simbolo, 2) cuenta electrones de valencia, 3) coloca puntos alrededor antes de formar pares, 4) si hay enlace covalente, representa el par compartido con una linea, 5) si hay iones, muestra carga y transferencia cuando aplique.",
                ],
                "cards": [
                    ("Electron de valencia", "Electron de la capa externa; es el que se representa con puntos."),
                    ("Par libre", "Dos electrones que permanecen en un atomo y no forman enlace."),
                    ("Par compartido", "Dos electrones usados por dos atomos en un enlace covalente."),
                    ("Octeto", "Tendencia de muchos atomos a rodearse de ocho electrones de valencia."),
                ],
                "table": {
                    "title": "Guia para construir Lewis",
                    "instruction": "Completa la tabla paso a paso. No dibujes la estructura final sin justificar primero los electrones de valencia.",
                    "headers": ["Especie", "Dato previo", "Paso de Lewis", "Resultado esperado"],
                    "rows": [
                        ["Cl", "Grupo 17", "Cuenta 7 electrones de valencia", "Cl con 7 puntos"],
                        ["H2O", "H tiene 1; O tiene 6", "Coloca O al centro y dos enlaces O-H", "2 pares compartidos y 2 pares libres en O"],
                        ["NaCl", "Na grupo 1; Cl grupo 17", "Representa transferencia de Na hacia Cl", "Na+ y Cl- con octeto en Cl"],
                    ],
                },
            },
        },
        "formula_intro": "Estas relaciones permiten pasar de nombres y formulas a cantidades que pueden medirse en el laboratorio.",
        "formulas": [
            ("Numero masico", "A = Z + N", "A suma protones y neutrones; Z es numero atomico; N son neutrones."),
            ("Moles", "n = m / M", "n en mol, m en gramos y M en g/mol."),
            ("Particulas", "N = n x NA", "NA = 6.022 x 10^23 particulas por mol."),
            ("Porcentaje en masa", "%m/m = masa soluto / masa mezcla x 100", "Usalo para estimar composicion de una mezcla."),
        ],
        "exercises": [
            "Clasifica agua con sal disuelta como sustancia pura o mezcla y justifica.",
            "Calcula neutrones de un atomo con A=23 y Z=11.",
            "Identifica si NaCl representa elemento, compuesto o mezcla.",
            "Calcula moles en 58.5 g de NaCl si M=58.5 g/mol.",
            "Calcula particulas en 0.50 mol de H2O.",
            "Explica por que Ca2+ tiene carga positiva.",
            "Usa la tabla periodica para ubicar grupo y periodo del sodio.",
            "Dibuja el simbolo de Lewis del cloro.",
            "Compara enlace ionico y covalente con un ejemplo del agua escolar.",
            "Calcula masa de 0.25 mol de CaCO3 si M=100 g/mol.",
            "Nombra NaCl y CaCO3 con nomenclatura comun o Stock.",
            "Explica como una sal se hidrata en agua.",
            "Ordena tres elementos por electronegatividad usando tendencia periodica.",
            "Indica si H2O es polar y que implica para disolver iones.",
            "Calcula porcentaje en masa de 2 g de sal en 100 g de mezcla.",
            "Distingue formula, nombre y masa molar en una tabla.",
            "Propone una prueba para detectar iones disueltos.",
            "Explica por que el mol no es una masa sino una cantidad.",
            "Redacta una conclusion sobre que puede contener el bebedero aunque sea transparente.",
            "Conecta sustancia, formula, mol y particula en un mapa corto.",
        ],
        "calc_bank": [
            "Un atomo de sodio tiene A = 23 y Z = 11. Calcula protones, electrones de un atomo neutro y neutrones. Escribe cada resultado con su significado.",
            "Calcula la masa molar de H2O usando H = 1 g/mol y O = 16 g/mol. Despues calcula cuantos moles hay en 36 g de agua.",
            "Calcula cuantos moles hay en 11.7 g de NaCl si M = 58.5 g/mol. Luego calcula cuantas particulas representa usando NA = 6.022 x 10^23.",
            "Una muestra contiene 2 g de sal en 100 g de mezcla. Calcula el porcentaje masa/masa y explica si el dato describe una mezcla o una sustancia pura.",
            "Calcula la masa necesaria para preparar 0.25 mol de CaCO3 si M = 100 g/mol. Indica formula, sustitucion y unidad final.",
            "Compara Delta EN de Na-Cl con valores Na = 0.9 y Cl = 3.0, y H-O con H = 2.1 y O = 3.5. Decide cual enlace es mas polar y justifica.",
        ],
        "close": "Al terminar U1, el estudiante puede nombrar, representar y calcular sustancias presentes o posibles en una muestra.",
        "product": "Tabla de posibles sustancias e iones del bebedero con nombre, formula, tipo de enlace y calculo basico.",
        "deliverable": "Entrega una tabla de 6 sustancias posibles y una explicacion de cual conviene investigar primero.",
    },
    {
        "unit": "u02",
        "title": "U2 - Agua",
        "short": "U2 / Agua",
        "kicker": "Unidad 2 / Agua",
        "story": "El bebedero ya no es solo una muestra: ahora es un sistema acuoso con pH, concentracion, dureza, contaminantes y tratamiento posible.",
        "case_link": "La unidad usa el agua escolar para conectar estructura molecular, pH, soluciones, diluciones y decisiones de tratamiento.",
        "cover_phrase": "El agua parece simple porque es cotidiana; quimicamente es uno de los sistemas mas poderosos para transportar sustancias.",
        "start_activity": "Registra tres propiedades del agua que puedas medir en aula: pH, temperatura y volumen.",
        "intro_title": "El agua como laboratorio",
        "intro_1": "El agua disuelve, transporta y reacciona. Por eso una muestra transparente puede tener informacion quimica relevante.",
        "intro_2": "En esta unidad la estructura de H2O se conecta con pH, soluciones, diluciones, contaminacion y tratamiento responsable.",
        "central_idea": "El agua se comprende cuando relacionas estructura molecular con mediciones de calidad.",
        "concepts": [
            ("Polaridad", "Distribucion desigual de carga en la molecula."),
            ("Puente H", "Interaccion que explica propiedades del agua."),
            ("pH", "Indicador de acidez o basicidad."),
            ("Molaridad", "Moles de soluto por litro de solucion."),
            ("Dilucion", "Bajar concentracion sin perder soluto."),
            ("Contaminante", "Sustancia que altera calidad o seguridad."),
        ],
        "questions": [
            "Por que el agua disuelve sales?",
            "Que dice el pH sobre una muestra?",
            "Cuando una dilucion cambia la concentracion sin cambiar el soluto?",
        ],
        "concept_frame": "El comportamiento del agua se explica por su polaridad, enlaces de hidrogeno y capacidad como solvente.",
        "decision_frame": "Los datos de pH, ppm, molaridad y contaminantes orientan si la muestra requiere tratamiento.",
        "data_frame": "pH, volumen, masa de soluto, molaridad, ppm, temperatura y observaciones.",
        "error_frame": "Usar mL como si fueran L en molaridad o confundir ppm con porcentaje.",
        "development_prompt": "Aplica el concepto a una muestra del bebedero y decide que dato seria indispensable antes de recomendar tratamiento.",
        "default_phrase": "Cada propiedad del agua conecta una estructura invisible con una decision visible.",
        "default_mini": "Elige una medicion del agua escolar y explica que decision podria apoyar.",
        "topics": {
            2: "Mapa de ruta del agua",
            3: "Estructura molecular y polaridad",
            4: "Puentes de hidrogeno",
            5: "Propiedades fisicas y cambio de estado",
            6: "Escala de pH",
            7: "Acidos, bases y electrolitos",
            8: "Soluciones y concentracion",
            9: "Tratamiento del agua",
            10: "Taller de diagnostico de agua",
        },
        "dense_visuals": [2, 6, 7, 8],
        "landscape_visuals": [3, 4, 5, 9, 10],
        "phrases": {
            6: "El pH no dice todo sobre el agua, pero obliga a dejar de opinar y empezar a medir.",
            8: "Una solucion se entiende cuando puedes decir que hay, cuanto hay y en que volumen esta.",
        },
        "mini": {},
        "formula_intro": "Estas formulas convierten observaciones del agua en datos comparables.",
        "formulas": [
            ("pH", "pH = -log[H+]", "[H+] en mol/L; pH no tiene unidad."),
            ("Molaridad", "M = n / V", "M en mol/L; n en mol; V en litros."),
            ("Dilucion", "M1 V1 = M2 V2", "Usa las mismas unidades de volumen en ambos lados."),
            ("ppm", "ppm = mg / L", "Para agua, ppm se interpreta comunmente como mg/L."),
        ],
        "exercises": [
            "Calcula pH si [H+] = 1 x 10^-7 mol/L.",
            "Calcula [H+] si pH = 5.",
            "Calcula molaridad de 0.10 mol en 0.50 L.",
            "Convierte 250 mL a litros para usar en molaridad.",
            "Calcula ppm si hay 3 mg de soluto en 1 L.",
            "Calcula mg en 2 L si la concentracion es 0.45 ppm.",
            "Usa M1V1=M2V2 para diluir 1.0 M a 0.25 M en 100 mL.",
            "Explica por que una solucion puede ser transparente y aun contener iones.",
            "Clasifica tres sustancias como acidas, basicas o neutras por pH.",
            "Propone un control para medir pH del bebedero.",
            "Identifica un error comun al usar mL en molaridad.",
            "Calcula moles en 0.250 L de solucion 0.20 M.",
            "Describe que dato falta para evaluar dureza del agua.",
            "Compara pH 6 y pH 8 como diferencia de acidez.",
            "Redacta una conclusion si pH=7.2 y cloro=0.45 ppm.",
            "Propone una accion si el agua presenta olor pero pH normal.",
            "Calcula concentracion si 0.5 g se disuelven en 1 L en mg/L.",
            "Explica cuando una dilucion no elimina contaminacion.",
            "Relaciona polaridad del agua con disolucion de NaCl.",
            "Disena una tabla de registro para pH, temperatura y TDS.",
        ],
        "calc_bank": [
            "Calcula pH para [H+] = 1 x 10^-6 mol/L. Despues indica si la muestra es acida, neutra o basica.",
            "Una solucion contiene 0.20 mol de soluto en 0.500 L. Calcula la molaridad y explica que representa mol/L.",
            "Convierte 250 mL a L y calcula moles si la solucion tiene M = 0.40 mol/L. Usa n = M x V.",
            "Se diluyen 25 mL de una solucion 1.0 M hasta 100 mL. Calcula la concentracion final con M1V1 = M2V2.",
            "Una muestra tiene 4 mg de soluto en 2 L de agua. Calcula ppm como mg/L y escribe una conclusion sobre concentracion.",
            "Si el cloro residual es 0.35 ppm, calcula cuantos mg de cloro hay en 3 L de agua. Muestra conversion y unidades.",
        ],
        "close": "Al terminar U2, el estudiante conecta estructura del agua con mediciones que permiten tomar decisiones de calidad.",
        "product": "Reporte de calidad de agua con pH, ppm, concentracion y propuesta de tratamiento.",
        "deliverable": "Entrega un reporte de una pagina con datos, calculos, conclusion y siguiente prueba.",
    },
    {
        "unit": "u03",
        "title": "U3 - Aire",
        "short": "U3 / Aire",
        "kicker": "Unidad 3 / Aire",
        "story": "El bebedero no esta aislado: el aire del comedor, la combustion cercana y la lluvia pueden cambiar el entorno quimico del agua.",
        "case_link": "La unidad conecta composicion del aire, combustion, redox, ciclos y lluvia acida con el cuidado del agua escolar.",
        "cover_phrase": "El aire parece vacio hasta que una reaccion muestra que tambien deja huella.",
        "start_activity": "Identifica tres fuentes de gases o particulas cerca del bebedero y plantea que dato se podria medir.",
        "intro_title": "El entorno tambien reacciona",
        "intro_1": "El aire es una mezcla. Sus componentes pueden participar en combustion, oxidacion, ciclos y contaminacion.",
        "intro_2": "Para proteger el agua escolar, conviene mirar tambien lo que ocurre alrededor: gases, particulas, lluvia y fuentes de combustion.",
        "central_idea": "El aire se entiende como mezcla reactiva que puede modificar el ambiente del agua.",
        "concepts": [
            ("Mezcla gaseosa", "Combinacion de gases con proporciones."),
            ("Combustion", "Reaccion con oxigeno que libera energia."),
            ("Oxido", "Compuesto formado con oxigeno."),
            ("Redox", "Proceso con transferencia de electrones."),
            ("Ciclo", "Ruta natural de transformacion de elementos."),
            ("Lluvia acida", "Deposicion acida por gases contaminantes."),
        ],
        "questions": [
            "Que gases forman la mayor parte del aire?",
            "Como una combustion puede afectar agua cercana?",
            "Que evidencia usarias para sospechar lluvia acida?",
        ],
        "concept_frame": "El aire combina gases, reacciones y ciclos que influyen en agua, suelo y seres vivos.",
        "decision_frame": "Si el entorno aporta gases acidos o particulas, el diagnostico del agua debe considerar esa fuente.",
        "data_frame": "Composicion, fuente de combustion, pH de lluvia, presencia de particulas y reaccion observada.",
        "error_frame": "Analizar agua sin registrar el ambiente donde se encuentra.",
        "development_prompt": "Usa el visual como ejemplo para conectar un componente del aire con una posible consecuencia en el bebedero.",
        "default_phrase": "El aire no se ve como una muestra, pero sus reacciones pueden aparecer en cada gota.",
        "default_mini": "Elige una fuente de gases cercana al colegio y explica que dato permitiria investigarla.",
        "topics": {
            2: "Mapa de ruta del aire",
            3: "Composicion porcentual del aire",
            4: "Oxigeno, combustion y oxidos",
            5: "Balanceo de reacciones",
            6: "Ciclos biogeoquimicos",
            7: "Contaminantes del aire",
            8: "Smog, lluvia acida y efecto invernadero",
            9: "Taller de huella y mitigacion",
        },
        "dense_visuals": [2, 3, 5, 7, 9],
        "landscape_visuals": [4, 6, 8],
        "phrases": {
            3: "Conocer porcentajes evita tratar al aire como una sola sustancia.",
            8: "La contaminacion atmosferica se vuelve quimica del agua cuando cae, se disuelve o reacciona.",
        },
        "mini": {},
        "formula_intro": "Estas relaciones ayudan a cuantificar mezclas, gases y reacciones del aire.",
        "formulas": [
            ("Porcentaje", "% = parte / total x 100", "Parte y total deben estar en la misma unidad."),
            ("Gas ideal", "PV = nRT", "P, V, n, R y T deben ser compatibles; T en K."),
            ("Moles de gas", "n = PV / RT", "Permite estimar cantidad de gas en un volumen."),
            ("Combustion general", "CxHy + O2 -> CO2 + H2O", "Debe balancearse antes de interpretar cantidades."),
        ],
        "exercises": [
            "Calcula porcentaje de O2 si hay 21 partes de O2 en 100 partes de aire.",
            "Calcula moles de gas con P=1 atm, V=2 L, R=0.082 y T=298 K.",
            "Convierte 25 C a K para usar PV=nRT.",
            "Balancea CH4 + O2 -> CO2 + H2O.",
            "Explica por que CO2 puede relacionarse con efecto invernadero.",
            "Identifica si una reaccion es combustion u oxidacion lenta.",
            "Propone una observacion para detectar smog cerca del colegio.",
            "Relaciona lluvia acida con pH menor a 7.",
            "Calcula porcentaje si 4 moles de un gas estan en mezcla de 20 moles.",
            "Escribe una hipotesis sobre aire del comedor y agua de cisterna.",
            "Explica que dato ambiental agregarias al reporte del bebedero.",
            "Distingue O2, N2 y CO2 por funcion en el ambiente.",
            "Balancea C2H6 + O2 -> CO2 + H2O.",
            "Estima volumen si n=0.10 mol, T=300 K, P=1 atm.",
            "Redacta una conclusion sobre una muestra de lluvia con pH 5.5.",
            "Propone una accion para disminuir particulas cerca del bebedero.",
            "Relaciona ciclo del carbono con combustion escolar.",
            "Identifica un contaminante primario y uno secundario.",
            "Explica por que el aire se trata como mezcla y no como compuesto.",
            "Disena un mini monitoreo de aire durante una semana escolar.",
        ],
        "calc_bank": [
            "Calcula el porcentaje de CO2 si una mezcla tiene 0.04 partes de CO2 en 100 partes de aire. Expresa el resultado en porcentaje.",
            "Convierte 27 C a K y usa PV = nRT para calcular moles de gas con P = 1 atm, V = 1.5 L y R = 0.082 L atm/mol K.",
            "Calcula el volumen de 0.20 mol de gas a 300 K y 1 atm usando V = nRT/P. Escribe unidades en cada paso.",
            "Balancea CH4 + O2 -> CO2 + H2O y explica que coeficiente indica la cantidad de oxigeno requerida.",
            "Balancea C2H6 + O2 -> CO2 + H2O. Despues indica cuantos moles de CO2 se producen por 1 mol de C2H6.",
            "Una lluvia registra pH = 5.5 y otra pH = 6.5. Compara cual es mas acida y explica por que el pH se interpreta con cuidado.",
        ],
        "close": "Al terminar U3, el estudiante integra agua y aire como sistemas conectados.",
        "product": "Diagnostico ambiental del bebedero con dato de aire, posible reaccion y accion preventiva.",
        "deliverable": "Entrega un reporte breve que conecte una fuente atmosferica con una medicion o decision sobre agua escolar.",
    },
]


def main() -> None:
    base = U0_HTML.read_text(encoding="utf-8")
    base = base.replace("Colegio Nuevo Tecno - Quimica - Unidad 0", "Colegio Nuevo Tecno - Quimica - Manual 1 Completo")
    base = base.replace("../../../../../05_assets_visuales_iconos", "../../../../05_assets_visuales_iconos")
    base = adjust_base_toc(base)
    base = inject_extra_style(base)
    prefix = base.rsplit("</body>", 1)[0]
    pages = [prefix]
    for unit in UNIT_DATA:
        pages.append(build_unit(unit))
    pages.append(closure_pages())
    pages.append(supplemental_pages())
    html = "\n".join(pages) + "\n</body>\n</html>\n"
    html = fix_spanish_text_nodes(html)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()
