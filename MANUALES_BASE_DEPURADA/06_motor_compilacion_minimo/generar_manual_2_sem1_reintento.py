from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "01_fuente_principal_markdown"
    / "manuales"
    / "manual-2"
    / "semestre-1"
    / "manual-2-fisica-semestre-1-reintento.html"
)
VISUAL_ROOT = ROOT / "05_assets_visuales_iconos" / "visuales" / "manual-2"
IMG_PREFIX = "../../../../05_assets_visuales_iconos/visuales/manual-2"


def e(text: object) -> str:
    return escape(str(text), quote=True)


def sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"-(\d+)$", path.stem)
    return (int(match.group(1)) if match else 999, path.stem)


def jpeg_size(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()
    if len(data) < 4 or data[:2] != b"\xff\xd8":
        return None
    idx = 2
    sof_markers = {
        0xC0, 0xC1, 0xC2, 0xC3,
        0xC5, 0xC6, 0xC7,
        0xC9, 0xCA, 0xCB,
        0xCD, 0xCE, 0xCF,
    }
    while idx < len(data) - 1:
        if data[idx] != 0xFF:
            idx += 1
            continue
        while idx < len(data) and data[idx] == 0xFF:
            idx += 1
        if idx >= len(data):
            break
        marker = data[idx]
        idx += 1
        if marker in {0xD8, 0xD9}:
            continue
        if idx + 2 > len(data):
            break
        length = int.from_bytes(data[idx:idx + 2], "big")
        if length < 2 or idx + length > len(data):
            break
        if marker in sof_markers and length >= 7:
            height = int.from_bytes(data[idx + 3:idx + 5], "big")
            width = int.from_bytes(data[idx + 5:idx + 7], "big")
            return width, height
        idx += length
    return None


def svg_size(path: Path) -> tuple[int, int] | None:
    raw = path.read_text(encoding="utf-8", errors="replace")
    width = re.search(r'\bwidth="(\d+)"', raw)
    height = re.search(r'\bheight="(\d+)"', raw)
    if width and height:
        return int(width.group(1)), int(height.group(1))
    viewbox = re.search(r'\bviewBox="[^"]*?\s+(\d+)\s+(\d+)"', raw)
    if viewbox:
        return int(viewbox.group(1)), int(viewbox.group(2))
    return None


def visual_path(folder: str, visual_id: str) -> Path:
    svg = VISUAL_ROOT / folder / f"{visual_id}.svg"
    if svg.exists():
        return svg
    return VISUAL_ROOT / folder / f"{visual_id}.jpg"


def is_landscape_image(folder: str, visual_id: str) -> bool:
    path = visual_path(folder, visual_id)
    if path.suffix.lower() == ".svg":
        size = svg_size(path)
    else:
        size = jpeg_size(path) if path.exists() else None
    return bool(size and size[0] >= size[1])


def foot(left: str, right: str) -> str:
    return f'<div class="footer"><span>{e(left)}</span><span>{e(right)}</span></div>'


def section(body: str, cls: str = "page") -> str:
    return f'<section class="{cls}">\n{body}\n</section>\n'


@dataclass
class Unit:
    unit: str
    title: str
    short: str
    kicker: str
    story: str
    episode: str
    intro_title: str
    intro_1: str
    intro_2: str
    central_idea: str
    concepts: list[tuple[str, str]]
    questions: list[str]
    topics: dict[int, str]
    formulas: list[tuple[str, str, str]]
    exercises: list[str]
    calc_bank: list[str]
    product: str
    close: str
    visual_phrases: dict[int, str]
    mini: dict[int, str]
    dense: set[int]
    landscape: set[int]


CSS = """
  @page { size: letter; margin: 0; }
  @page landscape { size: letter landscape; margin: 0; }

  :root {
    --blue: #0E3A8A;
    --cyan: #0E7490;
    --orange: #F39C12;
    --green: #15803D;
    --ink: #172033;
    --muted: #5B6472;
    --line: #D8DEE9;
    --soft: #F7FAFC;
    --cream: #FFF8E8;
  }

  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    background: #E8EEF6;
    color: var(--ink);
    font-family: Arial, "Segoe UI", sans-serif;
    line-height: 1.28;
  }
  .page {
    width: 216mm;
    height: 279mm;
    min-height: 279mm;
    padding: 13mm 13mm 14mm;
    margin: 0 auto 8mm;
    background: #FFFFFF;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 4mm;
    page-break-after: always;
    break-after: page;
  }
  .landscape {
    page: landscape;
    width: 279mm;
    height: 216mm;
    min-height: 216mm;
    padding: 8mm 10mm 11mm;
    gap: 2mm;
  }
  .cover {
    padding: 0;
    color: #FFFFFF;
    display: block;
  }
  .cover img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .cover::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, rgba(8, 31, 84, 0.92), rgba(14, 116, 144, 0.35));
  }
  .cover-content {
    position: relative;
    z-index: 1;
    height: 100%;
    padding: 22mm 18mm 18mm;
    display: grid;
    grid-template-rows: auto 1fr auto;
  }
  .school {
    font-size: 16pt;
    letter-spacing: 0;
    text-transform: uppercase;
    font-weight: 800;
  }
  .cover h1 {
    margin: 28mm 0 4mm;
    font-size: 42pt;
    line-height: .96;
    letter-spacing: 0;
    max-width: 145mm;
  }
  .cover .lead {
    max-width: 142mm;
    font-size: 15pt;
    color: rgba(255,255,255,.9);
  }
  .cover-meta {
    border-top: 1px solid rgba(255,255,255,.55);
    padding-top: 6mm;
    display: flex;
    justify-content: space-between;
    font-size: 11pt;
  }
  h2 {
    margin: 0;
    color: var(--blue);
    font-size: 20pt;
    line-height: 1.06;
    letter-spacing: 0;
  }
  h3 {
    margin: 1mm 0 2mm;
    color: var(--blue);
    font-size: 12.6pt;
    line-height: 1.12;
  }
  p, li {
    font-size: 11.2pt;
    line-height: 1.32;
  }
  .kicker {
    margin: 0 0 1.5mm;
    color: var(--orange);
    font-size: 9.8pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: .08em;
  }
  .subtitle {
    margin: 0;
    color: var(--muted);
    font-size: 11.2pt;
  }
  .note {
    border-left: 5px solid var(--orange);
    background: var(--cream);
    padding: 3mm;
    font-size: 11pt;
    break-inside: avoid;
  }
  .footer {
    border-top: 1px solid var(--line);
    color: var(--muted);
    font-size: 8.4pt;
    padding-top: 2mm;
    display: flex;
    justify-content: space-between;
    gap: 5mm;
    margin-top: auto;
  }
  .toc {
    display: grid;
    grid-template-columns: 18mm 1fr 23mm;
    border: 1px solid var(--line);
    font-size: 10.8pt;
  }
  .toc div {
    padding: 2.5mm;
    border-bottom: 1px solid var(--line);
  }
  .toc .head {
    background: var(--blue);
    color: #FFFFFF;
    font-weight: 800;
  }
  .temario-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3mm;
  }
  .temario-unit {
    border: 1px solid var(--line);
    border-left: 5px solid var(--blue);
    padding: 3mm;
    break-inside: avoid;
  }
  .temario-unit h3 {
    margin-top: 0;
    font-size: 12pt;
  }
  .temario-unit ul {
    margin: 1mm 0 0;
    padding-left: 5mm;
  }
  .temario-unit li {
    font-size: 10.4pt;
    line-height: 1.2;
    margin-bottom: .8mm;
  }
  .route {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 3mm;
  }
  .route-card,
  .concept,
  .development-card,
  .formula-card,
  .appendix-card {
    border: 1px solid var(--line);
    border-left: 5px solid var(--cyan);
    padding: 3mm;
    break-inside: avoid;
    background: #FFFFFF;
  }
  .route-card strong,
  .concept strong {
    display: block;
    color: var(--blue);
    font-size: 11.4pt;
    margin-bottom: 1mm;
  }
  .route-card p,
  .concept,
  .development-card p,
  .development-card li,
  .formula-card p,
  .appendix-card p,
  .appendix-card li {
    font-size: 10.8pt;
    line-height: 1.26;
  }
  .concept-list,
  .development-grid,
  .formula-grid,
  .appendix-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3mm;
  }
  .concept-list {
    grid-template-columns: repeat(3, 1fr);
  }
  .questions-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3mm;
  }
  .question {
    border: 1px solid var(--line);
    padding: 2.7mm;
    break-inside: avoid;
  }
  .question p {
    margin: 0 0 2mm;
    font-size: 10.8pt;
  }
  .answer-lines span,
  .worksheet-lines span {
    display: block;
    height: 4.4mm;
    border-bottom: 1px solid #B8C0CC;
  }
  .case-image-page {
  }
  .case-image {
    margin: 0;
    display: grid;
    place-items: center;
    min-height: 0;
    flex: 1 1 auto;
  }
  .case-image img {
    display: block;
    max-width: 100%;
    max-height: 186mm;
    object-fit: contain;
    object-position: center;
  }
  .landscape .case-image img {
    max-width: 255mm;
    max-height: 142mm;
  }
  .image-frase {
    margin: 0;
    text-align: center;
    color: var(--muted);
    font-size: 10pt;
    line-height: 1.2;
  }
  .mini-activity,
  .exercise-development {
    border: 1px solid var(--line);
    border-left: 5px solid var(--green);
    padding: 3mm;
    break-inside: avoid;
  }
  .mini-activity h3,
  .exercise-development h3 {
    color: var(--green);
    margin-top: 0;
  }
  .mini-activity p,
  .exercise-development p {
    font-size: 10.8pt;
    margin: 0 0 2mm;
  }
  .mini-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 10.6pt;
    line-height: 1.22;
    break-inside: avoid;
  }
  .mini-table th,
  .mini-table td {
    border: 1px solid var(--line);
    padding: 2.2mm;
    vertical-align: top;
  }
  .mini-table th {
    background: var(--blue);
    color: #FFFFFF;
    font-size: 10.8pt;
  }
  .step-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2.5mm;
  }
  .step-box {
    border: 1px solid var(--line);
    padding: 2.5mm;
    min-height: 23mm;
    font-size: 10.7pt;
    line-height: 1.25;
  }
  .worked-example {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3mm;
  }
  .worked-step {
    border: 1px solid var(--line);
    border-left: 5px solid var(--orange);
    padding: 2.6mm;
    min-height: 33mm;
    break-inside: avoid;
  }
  .worked-step h3 {
    margin: 0 0 1mm;
    color: var(--orange);
    font-size: 11.6pt;
  }
  .worked-step p {
    font-size: 10.5pt;
    line-height: 1.22;
    margin: 0;
  }
  .formula-card {
    border-left-color: var(--orange);
  }
  .formula {
    margin: 1.5mm 0;
    color: var(--blue);
    font-size: 15pt;
    font-weight: 800;
  }
  .exercise-bank {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: repeat(2, 1fr);
    gap: 3.5mm;
  }
  .bank-item {
    border: 1px solid var(--line);
    border-left: 5px solid var(--blue);
    padding: 3mm;
    min-height: 93mm;
    display: grid;
    grid-template-rows: auto 1fr;
    break-inside: avoid;
  }
  .bank-item p {
    margin: 0 0 2mm;
    font-size: 10.9pt;
    line-height: 1.26;
  }
  .bank-lines::before {
    content: "Aquí deja tus operaciones";
    display: block;
    color: var(--muted);
    font-size: 9.6pt;
    margin-bottom: 1mm;
  }
  .bank-lines span {
    display: block;
    height: 6mm;
    border-bottom: 1px solid #B8C0CC;
  }
  .calc-bank {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr);
  }
  .calc-bank .bank-item {
    min-height: 98mm;
  }
  .appendix-cover {
    background: linear-gradient(135deg, rgba(14,58,138,.95), rgba(14,116,144,.84)), var(--blue);
    color: #FFFFFF;
  }
  .appendix-cover h2,
  .appendix-cover h3 {
    color: #FFFFFF;
  }
  .appendix-cover .subtitle,
  .appendix-cover p,
  .appendix-cover li {
    color: rgba(255,255,255,.9);
  }
  .constant-table {
    font-size: 10.8pt;
  }
  @media print {
    body { background: #FFFFFF; }
    .page { margin: 0; box-shadow: none; }
  }
"""


def html_shell(body: str) -> str:
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Colegio Nuevo Tecno - Física - Manual 2 Semestre 1</title>
  <style>
{CSS}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def img_src(folder: str, visual_id: str) -> str:
    path = visual_path(folder, visual_id)
    return f"{IMG_PREFIX}/{folder}/{visual_id}{path.suffix}"


def visual_ids(unit: str) -> list[int]:
    folder = VISUAL_ROOT / unit
    return [
        int(path.stem.rsplit("-", 1)[1])
        for path in sorted(folder.glob("*.jpg"), key=sort_key)
        if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    ]


def concept_cards(items: list[tuple[str, str]]) -> str:
    return "".join(f'<div class="concept"><strong>{e(a)}</strong>{e(b)}</div>' for a, b in items)


def temario_unit_card(unit: str, title: str, items: list[str]) -> str:
    lis = "".join(f"<li>{e(item)}</li>" for item in items)
    return f'<div class="temario-unit"><h3>{e(unit + " - " + title)}</h3><ul>{lis}</ul></div>'


def front_pages() -> str:
    toc_rows = [
        ("U1", "Cinemática: posición, velocidad, aceleración, gráficas y trayectorias.", "23 pp"),
        ("U2", "Dinámica: fuerzas, leyes de Newton, torque, Hooke, gravitación y Kepler.", "26 pp"),
        ("U3", "Trabajo y energía: potencia, energía mecánica, ímpetu, colisiones y fricción.", "26 pp"),
        ("U4", "Termodinámica: calor, temperatura, transferencia, leyes y gases ideales.", "29 pp"),
        ("U5", "Ondas y sonido: parámetros, fenómenos ondulatorios, sonido y Doppler.", "22 pp"),
        ("Cierre", "Examen integrador, recursos, lecturas, constantes e índice analítico.", "10 pp"),
    ]
    toc = '<div class="toc"><div class="head">Unidad</div><div class="head">Ruta de aprendizaje</div><div class="head">Extensión</div>'
    toc += "".join(f"<div>{e(a)}</div><div>{e(b)}</div><div>{e(c)}</div>" for a, b, c in toc_rows)
    toc += "</div>"
    temario_1 = "".join([
        temario_unit_card("U1", "Cinemática", [
            "1.1 Características de los fenómenos mecánicos.",
            "1.2 Sistemas de referencia, posición, distancia y desplazamiento.",
            "1.3 Movimiento rectilíneo uniforme: v constante y x = x0 + vt.",
            "1.4 Movimiento rectilíneo uniformemente acelerado: a constante.",
            "1.5 Caída libre y tiro vertical: gravedad y sentido del movimiento.",
            "1.6 Movimiento parabólico: componentes horizontal y vertical.",
            "1.7 Movimiento circular uniforme: rapidez, radio y aceleración centrípeta.",
        ]),
        temario_unit_card("U2", "Fuerzas, Newton y Gravitación", [
            "2.1 Concepto vectorial de fuerza, suma y descomposición.",
            "2.2 Primera ley: inercia y equilibrio.",
            "2.3 Segunda ley: ΣF = ma, masa, peso y aceleración.",
            "2.4 Tercera ley: pares de acción y reacción.",
            "2.5 Equilibrio rotacional, torca y momento de inercia.",
            "2.6 Ley de Hooke: fuerza, constante elástica y deformación.",
            "2.7 Ley de gravitación universal.",
            "2.8 Leyes de Kepler como modelo orbital.",
        ]),
        temario_unit_card("U3", "Trabajo y Energía", [
            "3.1 Trabajo mecánico y ángulo entre fuerza y desplazamiento.",
            "3.2 Potencia como rapidez de transferencia de energía.",
            "3.3 Energía cinética y velocidad del prototipo.",
            "3.4 Energía potencial gravitacional y elástica.",
            "3.5 Conservación de energía mecánica.",
            "3.6 Ímpetu, impulso y conservación.",
            "3.7 Colisiones unidimensionales.",
            "3.8 Procesos disipativos: fricción, calor y sonido.",
        ]),
    ])
    temario_2 = "".join([
        temario_unit_card("U4", "Termodinámica", [
            "4.1 Calor y temperatura.",
            "4.2 Equilibrio térmico y ley cero.",
            "4.3 Escalas termométricas: °C, °F y K.",
            "4.4 Dilatación térmica.",
            "4.5 Conductividad y calor específico.",
            "4.6 Conducción, convección y radiación.",
            "4.7 Cambios de fase y calor latente.",
            "4.8 Primera y segunda ley de la termodinámica.",
            "4.9 Teoría cinética y gases ideales.",
        ]),
        temario_unit_card("U5", "Ondas y Sonido", [
            "5.1 Caracterización de ondas mecánicas.",
            "5.2 Parámetros: amplitud, longitud de onda, frecuencia y periodo.",
            "5.3 Reflexión y refracción.",
            "5.4 Difracción e interferencia.",
            "5.5 Energía transmitida, reflejada e intensidad.",
            "5.6 Sonido, ondas estacionarias y efecto Doppler.",
        ]),
        temario_unit_card("Cierre", "Integración del semestre", [
            "Examen integrador con cálculo e interpretación.",
            "Bibliografía, recursos de consulta y enlaces.",
            "Lecturas complementarias.",
            "Constantes, conversiones e índice analítico.",
            "Portadas de trimestre y continuidad al siguiente semestre.",
        ]),
    ])
    route = "".join(
        f'<div class="route-card"><strong>{e(a)}</strong><p>{e(b)}</p></div>'
        for a, b in [
            ("Medir", "Registrar posición, tiempo, fuerza, energía, temperatura y frecuencia con unidades claras."),
            ("Modelar", "Convertir el fenómeno físico en diagrama, gráfica, ecuación o tabla de datos."),
            ("Calcular", "Sustituir datos con unidades y revisar si el resultado tiene sentido físico."),
            ("Probar", "Usar mini actividades, bancos y prácticas para defender una decisión del equipo."),
            ("Cerrar", "Integrar evidencia en el diseño del coche F1 escolar del Colegio Nuevo Tecno."),
        ]
    )
    diagnostic = "".join(
        f'<div class="question"><p>{idx}. {e(q)}</p><div class="answer-lines"><span></span><span></span><span></span></div></div>'
        for idx, q in enumerate([
            "¿Qué diferencia hay entre distancia recorrida y desplazamiento?",
            "¿Por qué una fuerza necesita dirección para estar completa?",
            "¿Cómo sabes si una energía se conserva o se disipa?",
            "¿Qué cambia cuando una medición de temperatura se expresa en kelvin?",
            "¿Qué dato de una onda permite relacionar frecuencia y longitud de onda?",
            "¿Qué evidencia pedirías antes de modificar el diseño del coche F1?",
        ], 1)
    )
    pages = [
        section(f"""
  <img src="{e(img_src('sem1', 'M2-sem1-01'))}" alt="Coche F1 escolar con telemetría">
  <div class="cover-content">
    <div class="school">Colegio Nuevo Tecno</div>
    <div>
      <h1>Física<br>Manual 2</h1>
      <p class="lead">Semestre 1: mecánica, energía, termodinámica, ondas y sonido aplicadas al diseño de un coche F1 escolar.</p>
    </div>
    <div class="cover-meta"><span>Primer semestre</span><span>Equipo F1 Albatros</span></div>
  </div>
        """, "page cover"),
        section(f"""
  <p class="kicker">Manual 2 / Semestre 1</p>
  <h2>Temario completo del primer semestre</h2>
  <p class="subtitle">Este primer manual te ayudará a comprender las bases de la física y funciona como complemento de tu aprendizaje. La continuidad del proyecto llegará en el siguiente semestre, pero este tramo ya se trabaja como una ruta completa: leer, medir, calcular, comprobar y decidir.</p>
  {toc}
  {foot('Colegio Nuevo Tecno', 'Temario del semestre')}
        """),
        section(f"""
  <p class="kicker">Temario desglosado / parte 1</p>
  <h2>Unidades 1 a 3</h2>
  <p class="subtitle">Cada subtema se trabaja con historia, lectura visual, fórmula, unidades, práctica y banco de ejercicios.</p>
  <div class="temario-grid">{temario_1}</div>
  {foot('Colegio Nuevo Tecno', 'Temario completo 1/2')}
        """),
        section(f"""
  <p class="kicker">Temario desglosado / parte 2</p>
  <h2>Unidades 4, 5 y cierre</h2>
  <p class="subtitle">El semestre cierra con evidencia integradora, recursos, lecturas y herramientas de consulta.</p>
  <div class="temario-grid">{temario_2}</div>
  {foot('Colegio Nuevo Tecno', 'Temario completo 2/2')}
        """),
        sem_visual_page(
            "Mapa visual del semestre",
            "El semestre avanza como una pista de pruebas: primero se mide el movimiento, luego se explican fuerzas, energía, calor y sonido hasta cerrar con una decisión técnica.",
            "M2-sem1-05",
            "Cada unidad agrega una herramienta distinta; juntas forman la lectura física del prototipo."
        ),
        section(f"""
  <p class="kicker">Caso conductor</p>
  <h2>Equipo F1 Albatros</h2>
  <p>La escuela quiere competir con un coche F1 escolar. El reto parece de diseño, pero pronto se vuelve físico: el coche debe acelerar, resistir fuerzas, usar energía con eficiencia, controlar calor y reducir ruido o vibraciones.</p>
  <p>La historia del semestre no se cuenta como teoría aislada. Cada unidad agrega una herramienta para mejorar el prototipo: primero se mide el movimiento, después se interpretan fuerzas, se revisan pérdidas de energía, se controla la temperatura y finalmente se escucha el comportamiento del coche.</p>
  <div class="route">{route}</div>
  <div class="note"><strong>Regla de trabajo:</strong> ninguna conclusión del equipo se acepta sin dato, unidad, fórmula, sustitución y explicación breve.</div>
  {foot('Colegio Nuevo Tecno', 'Caso conductor')}
        """),
        section(f"""
  <p class="kicker">Diagnóstico inicial</p>
  <h2>Antes de entrar a pista</h2>
  <p class="subtitle">Responde sin buscar todavía. Estas preguntas permiten ubicar tus ideas previas antes de usar fórmulas o gráficas.</p>
  <div class="questions-grid">{diagnostic}</div>
  {foot('Colegio Nuevo Tecno', 'Diagnóstico')}
        """),
    ]
    return "\n".join(pages)


def sem_visual_page(title: str, subtitle: str, visual_id: str, phrase: str) -> str:
    page_cls = "page case-image-page landscape" if is_landscape_image("sem1", visual_id) else "page case-image-page"
    return section(f"""
  <div>
    <p class="kicker">Manual 2 / Semestre 1</p>
    <h2>{e(title)}</h2>
  </div>
  <p class="subtitle">{e(subtitle)}</p>
  <figure class="case-image" data-visual-id="{e(visual_id)}">
    <img src="{e(img_src('sem1', visual_id))}" alt="{e(title)}">
  </figure>
  <p class="image-frase">{e(phrase)}</p>
  {foot('Colegio Nuevo Tecno', 'Mapa visual del semestre')}
    """, page_cls)


def unit_cover(unit: Unit, first_visual: int) -> str:
    return section(f"""
  <div>
    <p class="kicker">{e(unit.kicker)}</p>
    <h2>{e(unit.title)}</h2>
  </div>
  <p class="subtitle">{e(unit.story)}</p>
  <figure class="case-image" data-visual-id="{e(f'M2-{unit.unit}-{first_visual:02d}')}">
    <img src="{e(img_src(unit.unit, f'M2-{unit.unit}-{first_visual:02d}'))}" alt="{e(unit.title)}">
  </figure>
  <p class="image-frase">{e(unit.episode)}</p>
  <div class="mini-activity">
    <h3>Arranque de unidad</h3>
    <p>Antes de resolver, escribe qué variable del coche F1 se debe medir primero y qué instrumento escolar permitiría obtenerla con unidad.</p>
  </div>
  {foot('Colegio Nuevo Tecno', unit.short + ' / inicio')}
    """, "page case-image-page")


def unit_intro(unit: Unit) -> str:
    questions = "".join(
        f'<div class="question"><p>{idx}. {e(q)}</p><div class="answer-lines"><span></span><span></span><span></span></div></div>'
        for idx, q in enumerate(unit.questions, 1)
    )
    return section(f"""
  <p class="kicker">{e(unit.kicker)}</p>
  <h2>{e(unit.intro_title)}</h2>
  <p>{e(unit.intro_1)}</p>
  <p>{e(unit.intro_2)}</p>
  <div class="note"><strong>Idea central:</strong> {e(unit.central_idea)}</div>
  <h3>Elementos necesarios para comprender el tema</h3>
  <div class="concept-list">{concept_cards(unit.concepts)}</div>
  <div class="questions">
    <h3>Preguntas introductorias</h3>
    <div class="questions-grid">{questions}</div>
  </div>
  {foot('Colegio Nuevo Tecno', unit.short + ' / introducción')}
    """)


def visual_page(unit: Unit, number: int) -> str:
    topic = unit.topics[number]
    phrase = unit.visual_phrases.get(number, "Un dato físico se vuelve útil cuando revela qué decisión debe tomar el equipo.")
    mini = unit.mini.get(number, f"Construye una versión pequeña del caso: elige una medición relacionada con {topic.lower()}, anota unidad, instrumento y cómo la usarías para mejorar el coche.")
    dense = number in unit.dense or number in unit.landscape
    mini_html = "" if dense else f"""
  <div class="mini-activity">
    <h3>Mini actividad conectada al caso</h3>
    <p>{e(mini)}</p>
  </div>
    """
    visual_id = f"M2-{unit.unit}-{number:02d}"
    page_cls = "page case-image-page landscape" if number in unit.landscape and is_landscape_image(unit.unit, visual_id) else "page case-image-page"
    if number in unit.dense and number not in unit.landscape:
        page_cls = "page case-image-page"
    return section(f"""
  <div>
    <p class="kicker">{e(unit.kicker)}</p>
    <h2>{e(topic)}</h2>
  </div>
  <p class="subtitle">{e(theory_bridge(unit, topic))}</p>
  <figure class="case-image" data-visual-id="{e(visual_id)}">
    <img src="{e(img_src(unit.unit, visual_id))}" alt="{e(topic)}">
  </figure>
  <p class="image-frase">{e(phrase)}</p>
  {mini_html}
  {foot('Colegio Nuevo Tecno', unit.short + f' / visual {number:02d}')}
    """, page_cls)


def theory_bridge(unit: Unit, topic: str) -> str:
    return (
        f"En el caso del coche F1, {topic.lower()} deja de ser una definición de cuaderno: "
        "se convierte en una forma de decidir qué medir, qué comparar y qué cambio del prototipo se puede justificar."
    )


def activity_block(unit: Unit, number: int, topic: str) -> str:
    cycle = ["calc", "table", "match", "compare", "open", "explain"]
    kind = cycle[(number - 2) % len(cycle)]
    if kind == "calc":
        formula = unit.formulas[(number - 2) % len(unit.formulas)]
        return f"""
  <div class="exercise-development">
    <h3>Comprobación con cálculo</h3>
    <p>Usa la relación <strong>{e(formula[1])}</strong> para crear un dato del coche F1. Debes escribir fórmula, sustitución, resultado y unidad final.</p>
    <div class="step-grid">
      <div class="step-box"><strong>1.</strong> Dato inicial y unidad.</div>
      <div class="step-box"><strong>2.</strong> Fórmula elegida y despeje si hace falta.</div>
      <div class="step-box"><strong>3.</strong> Sustitución con unidades visibles.</div>
      <div class="step-box"><strong>4.</strong> Resultado y revisión de sentido físico.</div>
    </div>
  </div>
        """
    if kind == "table":
        rows = "".join(
            "<tr><td></td><td></td><td></td><td></td></tr>" for _ in range(4)
        )
        return f"""
  <div class="exercise-development">
    <h3>Tabla de registro experimental</h3>
    <p>Completa la tabla para estudiar {e(topic.lower())}. Registra un ejemplo del coche, la magnitud, la unidad correcta y una conclusión breve.</p>
    <table class="mini-table"><thead><tr><th>Ejemplo del caso</th><th>Magnitud</th><th>Unidad</th><th>Conclusión</th></tr></thead><tbody>{rows}</tbody></table>
  </div>
        """
    if kind == "match":
        pairs = [
            ("A", "Magnitud física"),
            ("B", "Unidad compatible"),
            ("C", "Representación útil"),
            ("D", "Error frecuente"),
        ]
        targets = [
            ("1", "Se escribe antes de sustituir valores."),
            ("2", "Puede ser gráfica, vector, tabla o ecuación."),
            ("3", "Debe coincidir con la fórmula usada."),
            ("4", "Confundir escalar con vector o mezclar unidades."),
        ]
        rows = "".join(
            f"<tr><td>{e(a)}. {e(b)}</td><td>{e(c)}. {e(d)}</td></tr>"
            for (a, b), (c, d) in zip(pairs, targets)
        )
        return f"""
  <div class="exercise-development">
    <h3>Relación de columnas</h3>
    <p>Relaciona la Columna A con la Columna B. Escribe parejas en formato A-__, B-__, C-__, D-__. Usa la teoría de {e(topic.lower())} para justificar una pareja.</p>
    <table class="mini-table"><thead><tr><th>Columna A: letras</th><th>Columna B: números</th></tr></thead><tbody>{rows}</tbody></table>
    <div class="worksheet-lines"><span></span><span></span></div>
  </div>
        """
    if kind == "compare":
        return f"""
  <div class="exercise-development">
    <h3>Cuadro comparativo aplicado</h3>
    <p>Compara <strong>{e(topic)}</strong> en un prototipo lento y en un prototipo rápido. Usa como criterios: variable medida, unidad, gráfica esperada, fórmula útil y decisión de diseño.</p>
    <table class="mini-table"><thead><tr><th>Criterio</th><th>Prototipo lento</th><th>Prototipo rápido</th><th>Decisión</th></tr></thead><tbody>
      <tr><td>Variable medida</td><td></td><td></td><td></td></tr>
      <tr><td>Unidad</td><td></td><td></td><td></td></tr>
      <tr><td>Gráfica o diagrama</td><td></td><td></td><td></td></tr>
      <tr><td>Fórmula útil</td><td></td><td></td><td></td></tr>
    </tbody></table>
  </div>
        """
    if kind == "open":
        questions = [
            f"¿Qué dato de {topic.lower()} pedirías antes de aceptar una mejora del coche?",
            "¿Qué error de medición podría cambiar la conclusión?",
            "¿Cómo explicarías el resultado a alguien que no vio el experimento?",
        ]
        q_html = "".join(
            f'<div class="question"><p>{idx}. {e(q)}</p><div class="answer-lines"><span></span><span></span><span></span></div></div>'
            for idx, q in enumerate(questions, 1)
        )
        return f"""
  <div class="exercise-development">
    <h3>Preguntas abiertas con evidencia</h3>
    <div class="questions-grid">{q_html}</div>
  </div>
        """
    return f"""
  <div class="exercise-development">
    <h3>Explicación con evidencia</h3>
    <p>Redacta una explicación breve de {e(topic.lower())}. Debe contener una analogía, una magnitud con unidad, una fórmula o diagrama y una decisión para el Equipo F1 Albatros.</p>
    <div class="step-grid">
      <div class="step-box"><strong>1.</strong> Analogía propia.</div>
      <div class="step-box"><strong>2.</strong> Dato medible.</div>
      <div class="step-box"><strong>3.</strong> Representación física.</div>
      <div class="step-box"><strong>4.</strong> Decisión de diseño.</div>
    </div>
  </div>
    """


def concept_page(unit: Unit, number: int) -> str:
    topic = unit.topics[number]
    f1 = unit.formulas[(number - 2) % len(unit.formulas)]
    f2 = unit.formulas[(number - 1) % len(unit.formulas)]
    cards = [
        ("Concepto físico", f"{topic} se usa para traducir una situación del coche en una magnitud medible."),
        ("Analogía útil", "Trabajar con física es como leer la pista por capas: primero ubicas la situación, luego eliges el dato y al final verificas el cambio."),
        ("Fórmula cercana", f"{f1[0]}: {f1[1]}. {f1[2]}"),
        ("Unidad y cuidado", f"{f2[0]}: {f2[1]}. Antes de sustituir, revisa que las unidades sean compatibles."),
    ]
    card_html = "".join(
        f'<div class="development-card"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in cards
    )
    return section(f"""
  <p class="kicker">{e(unit.kicker)}</p>
  <h2>{e('Conceptos fundamentales: ' + topic)}</h2>
  <p class="subtitle">{e(theory_bridge(unit, topic))}</p>
  <div class="development-grid">{card_html}</div>
  {activity_block(unit, number, topic)}
  {foot('Colegio Nuevo Tecno', unit.short + ' / conceptos')}
    """)


def u01_motion_types_explanation(unit: Unit) -> str:
    rows = [
        ["MRU", "Línea recta, velocidad constante, aceleración cero.", "v = Δx / Δt; x = x0 + vt", "m, s, m/s", "El coche cruza un tramo con marcas igualmente separadas."],
        ["MRUA", "Línea recta con aceleración constante.", "a = Δv / Δt; v = v0 + at; x = x0 + v0t + 1/2at²", "m/s², m/s, s", "Las marcas se separan cada vez más si acelera."],
        ["Caída libre", "Movimiento vertical bajo gravedad.", "g = 9.8 m/s²; y = y0 + 1/2gt²", "m, s, m/s²", "Una pieza cae al banco de pruebas desde reposo."],
        ["Parabólico", "Horizontal constante más vertical acelerado.", "x = vx t; y = y0 + v0yt - 1/2gt²", "m, s, m/s", "Una pieza lanzada describe una curva."],
        ["Circular", "Trayectoria circular con cambio continuo de dirección.", "ac = v² / r", "m/s², m/s, m", "Una rueda o trayectoria curva exige aceleración al centro."],
    ]
    row_html = "".join("<tr>" + "".join(f"<td>{e(cell)}</td>" for cell in row) + "</tr>" for row in rows)
    return section(f"""
  <p class="kicker">{e(unit.kicker)}</p>
  <h2>Cómo leer la infografía de tipos de movimiento</h2>
  <p class="subtitle">La infografía no es un resumen decorativo: funciona como una ruta para elegir modelo. Primero mira la trayectoria; después revisa si la velocidad cambia; al final selecciona fórmula y unidades.</p>
  <table class="mini-table"><thead><tr><th>Tipo</th><th>Cómo reconocerlo</th><th>Fórmulas clave</th><th>Unidades</th><th>Relación con el caso F1</th></tr></thead><tbody>{row_html}</tbody></table>
  <div class="note"><strong>Regla de decisión:</strong> si el coche se mueve en línea recta y la velocidad no cambia, usa MRU; si la velocidad cambia, usa MRUA; si aparece curva, separa componentes o revisa aceleración centrípeta.</div>
  {foot('Colegio Nuevo Tecno', unit.short + ' / lectura de infografía')}
    """)


def formula_page(unit: Unit) -> str:
    pages: list[str] = []
    for start in range(0, len(unit.formulas), 6):
        cards = "".join(
            f'<div class="formula-card"><h3>{e(title)}</h3><div class="formula">{e(formula)}</div><p>{e(desc)}</p></div>'
            for title, formula, desc in unit.formulas[start:start + 6]
        )
        suffix = "" if len(unit.formulas) <= 6 else f" {start // 6 + 1}"
        pages.append(section(f"""
  <p class="kicker">{e(unit.kicker)}</p>
  <h2>{e('Fórmulas antes de practicar' + suffix)}</h2>
  <p class="subtitle">Una fórmula no es una receta para poner números: expresa qué magnitudes se relacionan y en qué unidades deben estar. Si una unidad no coincide, primero se convierte y después se calcula.</p>
  <div class="formula-grid">{cards}</div>
  {foot('Colegio Nuevo Tecno', unit.short + ' / fórmulas')}
        """))
    return "\n".join(pages)


def u01_worked_example_pages(unit: Unit) -> str:
    page_one_steps = [
        ("Datos del caso", "Un coche parte de x0 = 0 m. En 2.0 s llega a x = 12 m. En ese intervalo su velocidad cambia de 2.0 m/s a 8.0 m/s. En una curva posterior lleva v = 5.0 m/s y r = 2.0 m."),
        ("1. Velocidad promedio", "v = Δx / Δt = (12 m - 0 m) / 2.0 s = 6.0 m/s. Esto resume el tramo completo, no cada instante."),
        ("2. Aceleración promedio", "a = Δv / Δt = (8.0 m/s - 2.0 m/s) / 2.0 s = 3.0 m/s². La velocidad aumenta 3.0 m/s cada segundo."),
        ("3. MRU como comparación", "Si el coche mantuviera v = 6.0 m/s durante 2.0 s: x = x0 + vt = 0 + (6.0 m/s)(2.0 s) = 12 m."),
    ]
    page_two_steps = [
        ("4. MRUA: velocidad final", "Con v0 = 2.0 m/s, a = 3.0 m/s² y t = 2.0 s: v = v0 + at = 2.0 + (3.0)(2.0) = 8.0 m/s."),
        ("5. MRUA: posición", "x = x0 + v0t + 1/2at² = 0 + (2.0)(2.0) + 1/2(3.0)(2.0)² = 4.0 + 6.0 = 10.0 m. Si el dato real fue 12 m, revisa si a fue constante durante todo el tramo."),
        ("6. Movimiento circular", "En la curva: ac = v² / r = (5.0 m/s)² / 2.0 m = 12.5 m/s² hacia el centro. Aunque la rapidez sea constante, la dirección cambia."),
        ("Conclusión técnica", "El prototipo muestra aceleración clara en recta y demanda mucha aceleración centrípeta en curva; por eso conviene revisar alineación, ruedas y masa antes de aumentar potencia."),
    ]

    def render_steps(steps: list[tuple[str, str]]) -> str:
        return "".join(f'<div class="worked-step"><h3>{e(title)}</h3><p>{e(text)}</p></div>' for title, text in steps)

    return "\n".join([
        section(f"""
  <p class="kicker">{e(unit.kicker)} / ejemplo resuelto</p>
  <h2>Ejemplo resuelto de principio a fin</h2>
  <p class="subtitle">Antes del banco, resolvemos un caso completo para ver cómo se elige la fórmula, cómo se sustituyen datos y cómo se comprueba el resultado.</p>
  <div class="worked-example">{render_steps(page_one_steps)}</div>
  {foot('Colegio Nuevo Tecno', unit.short + ' / ejemplo resuelto 1')}
        """),
        section(f"""
  <p class="kicker">{e(unit.kicker)} / ejemplo resuelto</p>
  <h2>Ejemplo resuelto: comprobación y decisión</h2>
  <p class="subtitle">Las fórmulas de la infografía se usan como herramientas distintas. No todas responden la misma pregunta.</p>
  <div class="worked-example">{render_steps(page_two_steps)}</div>
  {foot('Colegio Nuevo Tecno', unit.short + ' / ejemplo resuelto 2')}
        """),
    ])


def bank_pages(unit: Unit) -> str:
    pages: list[str] = []
    for start in range(0, len(unit.exercises), 4):
        items = "".join(
            f'<div class="bank-item"><p><strong>{idx}.</strong> {e(text)}</p><div class="bank-lines"><span></span><span></span><span></span><span></span></div></div>'
            for idx, text in enumerate(unit.exercises[start:start + 4], start + 1)
        )
        pages.append(section(f"""
  <p class="kicker">{e(unit.kicker)}</p>
  <h2>{e('Banco de ejercicios ' + str(start // 4 + 1))}</h2>
  <div class="exercise-bank">{items}</div>
  {foot('Colegio Nuevo Tecno', unit.short + f' / ejercicios {start + 1}-{min(start + 4, len(unit.exercises))}')}
        """))
    return "\n".join(pages)


def calc_bank_pages(unit: Unit) -> str:
    pages: list[str] = []
    exercises = unit.calc_bank if unit.unit == "u01" else unit.calc_bank[:4]
    for start in range(0, len(exercises), 2):
        items = "".join(
            f'<div class="bank-item"><p><strong>{idx}.</strong> {e(text)}</p><div class="bank-lines"><span></span><span></span><span></span><span></span><span></span></div></div>'
            for idx, text in enumerate(exercises[start:start + 2], start + 1)
        )
        pages.append(section(f"""
  <p class="kicker">{e(unit.kicker)}</p>
  <h2>{e('Banco de cálculo ' + str(start // 2 + 1))}</h2>
  <p class="subtitle">Resuelve con fórmula, despeje cuando sea necesario, sustitución, resultado, unidades y comprobación del sentido físico.</p>
  <div class="exercise-bank calc-bank">{items}</div>
  {foot('Colegio Nuevo Tecno', unit.short + f' / cálculo {start + 1}-{min(start + 2, len(exercises))}')}
        """))
    return "\n".join(pages)


def unit_close(unit: Unit) -> str:
    return section(f"""
  <p class="kicker">{e(unit.kicker)}</p>
  <h2>{e('Cierre de ' + unit.title)}</h2>
  <p class="subtitle">{e(unit.close)}</p>
  <div class="note"><strong>Producto de unidad:</strong> {e(unit.product)}</div>
  <div class="exercise-development">
    <h3>Entrega breve</h3>
    <p>Entrega una hoja con evidencia, cálculo, error posible y decisión para el Equipo F1 Albatros.</p>
    <div class="step-grid">
      <div class="step-box"><strong>1.</strong> Evidencia principal.</div>
      <div class="step-box"><strong>2.</strong> Fórmula y sustitución.</div>
      <div class="step-box"><strong>3.</strong> Límite o error detectado.</div>
      <div class="step-box"><strong>4.</strong> Decisión de diseño.</div>
    </div>
  </div>
  {foot('Colegio Nuevo Tecno', unit.short + ' / cierre')}
    """)


def build_unit(unit: Unit) -> str:
    ids = visual_ids(unit.unit)
    if not ids:
        raise RuntimeError(f"No hay imágenes para {unit.unit}")
    pages = [unit_cover(unit, ids[0]), unit_intro(unit)]
    for number in ids[1:]:
        if number not in unit.topics:
            continue
        pages.append(visual_page(unit, number))
        if unit.unit == "u01" and number == 2:
            pages.append(u01_motion_types_explanation(unit))
        if number != 2:
            pages.append(concept_page(unit, number))
    pages.append(formula_page(unit))
    if unit.unit == "u01":
        pages.append(u01_worked_example_pages(unit))
    pages.append(calc_bank_pages(unit))
    pages.append(bank_pages(unit))
    pages.append(unit_close(unit))
    return "\n".join(pages)


def appendix_cover(number: int, title: str, subtitle: str, goals: list[str]) -> str:
    goals_html = "".join(f"<li>{e(goal)}</li>" for goal in goals)
    return section(f"""
  <div>
    <p class="kicker">Portada de trimestre {number}</p>
    <h2>{e(title)}</h2>
    <p class="subtitle">{e(subtitle)}</p>
  </div>
  <div class="note"><strong>Propósito:</strong><ul>{goals_html}</ul></div>
  {foot('Colegio Nuevo Tecno', f'Trimestre {number}')}
    """, "page appendix-cover")


def table_page(kicker: str, title: str, subtitle: str, headers: list[str], rows: list[list[str]], right: str) -> str:
    head = "".join(f"<th>{e(h)}</th>" for h in headers)
    def cell_html(cell: str) -> str:
        if cell.startswith("http://") or cell.startswith("https://"):
            return f'<td><a href="{e(cell)}">{e(cell)}</a></td>'
        return f"<td>{e(cell)}</td>"

    row_html = "".join("<tr>" + "".join(cell_html(cell) for cell in row) + "</tr>" for row in rows)
    return section(f"""
  <p class="kicker">{e(kicker)}</p>
  <h2>{e(title)}</h2>
  <p class="subtitle">{e(subtitle)}</p>
  <table class="mini-table constant-table"><thead><tr>{head}</tr></thead><tbody>{row_html}</tbody></table>
  {foot('Colegio Nuevo Tecno', right)}
    """)


def reading_page(number: int, title: str, paragraphs: list[str], questions: list[str]) -> str:
    text = "".join(f"<p>{e(p)}</p>" for p in paragraphs)
    q_html = "".join(
        f'<div class="question"><p>{idx}. {e(q)}</p><div class="answer-lines"><span></span><span></span><span></span></div></div>'
        for idx, q in enumerate(questions, 1)
    )
    return section(f"""
  <p class="kicker">Lectura complementaria {number}</p>
  <h2>{e(title)}</h2>
  <div>{text}</div>
  <div class="questions">
    <h3>Preguntas de comprensión</h3>
    <div class="questions-grid">{q_html}</div>
  </div>
  {foot('Colegio Nuevo Tecno', f'Lectura {number}')}
    """)


def closure_pages() -> str:
    exam = [
        "Un coche recorre 18 m en 1.2 s desde reposo. Estima aceleración promedio y velocidad final si el movimiento se considera uniformemente acelerado.",
        "Dibuja el diagrama de cuerpo libre del coche al arrancar y explica qué fuerzas favorecen o se oponen al movimiento.",
        "Calcula la energía cinética de un prototipo de 0.055 kg que alcanza 6.8 m/s y relaciona el resultado con pérdidas por fricción.",
        "Una pieza se calienta de 22 °C a 45 °C. Convierte ambas temperaturas a kelvin y explica por qué la escala importa en gases ideales.",
        "Un ruido dominante tiene frecuencia de 850 Hz. Si la rapidez del sonido es 343 m/s, calcula la longitud de onda y propón una mejora.",
        "Redacta una decisión técnica final: ¿qué modificarías primero, masa, fricción, alineación, ventilación o vibración? Justifica con evidencia.",
    ]
    exam_items = "".join(
        f'<div class="bank-item"><p><strong>{idx}.</strong> {e(item)}</p><div class="bank-lines"><span></span><span></span><span></span></div></div>'
        for idx, item in enumerate(exam[:4], 1)
    )
    exam_items_2 = "".join(
        f'<div class="bank-item"><p><strong>{idx}.</strong> {e(item)}</p><div class="bank-lines"><span></span><span></span><span></span></div></div>'
        for idx, item in enumerate(exam[4:], 5)
    )
    resources = [
        ["OpenStax University Physics", "Lectura de mecánica, energía, termodinámica y ondas", "https://openstax.org/details/books/university-physics-volume-1"],
        ["PhET Física", "Simulaciones de movimiento, fuerzas, energía, ondas y calor", "https://phet.colorado.edu/es/simulations/filter?subjects=physics"],
        ["NASA Glenn Beginner's Guide", "Fuerzas, movimiento, aerodinámica y mediciones", "https://www.grc.nasa.gov/www/k-12/airplane/"],
        ["NIST Constants", "Constantes físicas de referencia", "https://physics.nist.gov/cuu/Constants/"],
        ["Khan Academy Física", "Repaso guiado de conceptos", "https://es.khanacademy.org/science/physics"],
    ]
    index = [
        ["Aceleración", "U1", "Cambio de velocidad por unidad de tiempo."],
        ["Fuerza neta", "U2", "Suma vectorial responsable de acelerar el sistema."],
        ["Trabajo", "U3", "Transferencia de energía por fuerza a lo largo de una distancia."],
        ["Calor específico", "U4", "Energía necesaria para cambiar temperatura por masa."],
        ["Frecuencia", "U5", "Ciclos por segundo de una onda o vibración."],
        ["Doppler", "U5", "Cambio aparente de frecuencia por movimiento relativo."],
    ]
    pages = [
        section(f"""
  <p class="kicker">Cierre del semestre</p>
  <h2>Examen integrador</h2>
  <p class="subtitle">El examen exige unir datos de movimiento, fuerzas, energía, temperatura y sonido para tomar decisiones sobre el coche F1 escolar.</p>
  <div class="exercise-bank">{exam_items}</div>
  {foot('Colegio Nuevo Tecno', 'Examen integrador 1')}
        """),
        section(f"""
  <p class="kicker">Cierre del semestre</p>
  <h2>Examen integrador: decisión final</h2>
  <div class="exercise-bank calc-bank">{exam_items_2}</div>
  {foot('Colegio Nuevo Tecno', 'Examen integrador 2')}
        """),
        table_page("Bibliografía y recursos", "Recursos de consulta", "Usa estas fuentes para ampliar teoría, revisar simulaciones o contrastar constantes. Registra la liga consultada y el dato que tomaste.", ["Recurso", "Uso sugerido", "Liga"], resources, "Recursos"),
        table_page("Índice analítico", "Conceptos clave del semestre", "Este índice ayuda a volver a los puntos de mayor uso en actividades y cálculos.", ["Concepto", "Unidad", "Uso"], index, "Índice analítico"),
        appendix_cover(1, "Trimestre 1 - Movimiento y fuerzas", "Cinemática y dinámica del coche F1 escolar.", ["Medir posición, tiempo y velocidad.", "Construir gráficas de movimiento.", "Interpretar fuerzas y diagramas de cuerpo libre."]),
        appendix_cover(2, "Trimestre 2 - Energía y calor", "Trabajo, energía, fricción, temperatura y transferencia térmica.", ["Calcular energía útil y pérdidas.", "Comparar potencia y trabajo.", "Registrar datos térmicos con unidades."]),
        appendix_cover(3, "Trimestre 3 - Ondas y cierre", "Vibraciones, sonido, análisis de datos y decisión final.", ["Medir frecuencia y longitud de onda.", "Interpretar ruido del prototipo.", "Cerrar el caso con evidencia."]),
        table_page("Material complementario", "Constantes y conversiones útiles", "Antes de calcular, revisa que las magnitudes estén en unidades compatibles.", ["Magnitud", "Valor o conversión", "Uso"], [
            ["Gravedad", "g = 9.8 m/s²", "Caída libre, peso y energía potencial"],
            ["Rapidez del sonido", "v ≈ 343 m/s a 20 °C", "Ondas sonoras y Doppler"],
            ["Kelvin", "K = °C + 273.15", "Gases ideales y temperatura absoluta"],
            ["Newton", "1 N = 1 kg·m/s²", "Fuerza y segunda ley"],
            ["Joule", "1 J = 1 N·m", "Trabajo y energía"],
            ["Watt", "1 W = 1 J/s", "Potencia"],
        ], "Constantes"),
        reading_page(1, "Cuando medir cambió el movimiento", [
            "La física moderna avanzó cuando el movimiento dejó de explicarse solo con impresiones. Galileo comparó tiempos, distancias y pendientes para estudiar cómo cambian las velocidades. Esa idea sigue vigente: si el coche parece rápido, todavía falta registrar cuánto recorre y en cuánto tiempo.",
            "En el proyecto F1, una gráfica x-t o v-t permite discutir con evidencia. La medición no hace perfecto al prototipo, pero vuelve posible decidir qué modificación probar después.",
        ], [
            "¿Por qué una gráfica puede defender mejor una conclusión que una opinión?",
            "¿Qué dato mínimo necesitas para estimar velocidad promedio?",
        ]),
        reading_page(2, "Energía que se conserva y energía que se pierde", [
            "Un prototipo no solo se mueve: transforma energía. Parte se vuelve movimiento útil y parte se disipa en fricción, calor, vibración o ruido. Por eso mejorar un coche no significa únicamente hacerlo más ligero; también implica reducir pérdidas.",
            "Cuando calculas trabajo, energía cinética o potencia, conviertes una historia de pista en una comparación técnica. La energía ayuda a explicar por qué dos coches con apariencia similar pueden tener desempeños distintos.",
        ], [
            "¿Qué pérdida de energía sería más fácil observar en el aula?",
            "¿Cómo conectarías fricción, calor y sonido en un mismo reporte?",
        ]),
    ]
    return "\n".join(pages)


UNITS: list[Unit] = [
    Unit(
        unit="u01",
        title="U1 - Cinemática",
        short="U1 / Cinemática",
        kicker="Unidad 1 / Cinemática",
        story="El primer prototipo del coche F1 cruza la pista y todos celebran, pero nadie sabe si realmente mejoró. La historia cambia cuando el equipo coloca marcas en la pista, registra tiempos y transforma el recorrido en datos.",
        episode="La telemetría no vuelve más rápido al coche por sí sola; permite saber dónde acelera, dónde pierde velocidad y qué tramo conviene corregir.",
        intro_title="Contar el movimiento sin perseguirlo",
        intro_1="Desde Galileo, estudiar movimiento significa comparar posiciones y tiempos. Una caída, un tiro o un coche en línea recta se vuelven comprensibles cuando se elige un sistema de referencia y se registra cómo cambia la posición.",
        intro_2="En esta unidad el coche F1 sirve para distinguir distancia, desplazamiento, velocidad, aceleración y trayectorias. La meta no es memorizar ecuaciones: es saber cuándo cada ecuación describe el movimiento observado.",
        central_idea="El movimiento se entiende al relacionar posición, tiempo, velocidad y aceleración con gráficas y unidades.",
        concepts=[
            ("Sistema de referencia", "Lugar y orientación desde donde se describe la posición."),
            ("Distancia", "Longitud recorrida; es escalar y se mide en metros."),
            ("Desplazamiento", "Cambio de posición con dirección; es vectorial."),
            ("Velocidad", "Cambio de posición respecto al tiempo, en m/s."),
            ("Aceleración", "Cambio de velocidad respecto al tiempo, en m/s²."),
            ("Trayectoria", "Camino seguido por el objeto durante el movimiento."),
        ],
        questions=[
            "¿Puede un coche recorrer distancia y terminar con desplazamiento cero?",
            "¿Qué diferencia ves entre rapidez y velocidad?",
            "¿Cómo una gráfica puede mostrar aceleración sin mirar el coche?",
        ],
        topics={
            2: "Ruta de decisiones de la cinemática",
            3: "Magnitudes escalares y vectoriales",
            4: "Sistema de referencia, posición y desplazamiento",
            5: "Movimiento rectilíneo uniforme",
            6: "Movimiento rectilíneo uniformemente acelerado",
            7: "Caída libre y tiro vertical",
            8: "Movimiento parabólico",
            9: "Movimiento circular uniforme",
        },
        formulas=[
            ("Velocidad promedio", "v = Δx / Δt", "v se expresa en m/s; Δx es desplazamiento en metros y Δt es tiempo en segundos."),
            ("Aceleración promedio", "a = Δv / Δt", "a se expresa en m/s²; Δv es cambio de velocidad y Δt tiempo transcurrido."),
            ("MRU", "x = x0 + vt", "x y x0 están en metros; v en m/s; t en segundos."),
            ("MRUA", "v = v0 + at", "v y v0 están en m/s; a en m/s²; t en segundos."),
            ("Posición en MRUA", "x = x0 + v0t + 1/2 at²", "Usa metros, segundos y m/s² de forma compatible."),
            ("Caída libre", "y = y0 + 1/2 gt²", "y y y0 están en metros; g = 9.8 m/s²; t en segundos cuando parte del reposo."),
            ("Parabólico horizontal", "x = vx t", "x en metros; vx en m/s; t en segundos. El eje horizontal se analiza aparte."),
            ("Parabólico vertical", "y = y0 + v0y t - 1/2 gt²", "y en metros; v0y en m/s; g en m/s²; t en segundos."),
            ("Movimiento circular", "ac = v² / r", "ac está en m/s²; v en m/s; r en metros."),
        ],
        exercises=[
            "Calcula velocidad promedio si el coche recorre 20 m en 1.25 s.",
            "Distingue distancia y desplazamiento en una pista de ida y vuelta de 10 m.",
            "Convierte 72 km/h a m/s y explica si la unidad sirve para MRU.",
            "Traza una gráfica x-t para un coche que avanza 5 m cada segundo.",
            "Calcula aceleración si la velocidad cambia de 0 a 8 m/s en 2 s.",
            "Usa x = x0 + vt para encontrar la posición a los 3 s si v = 4 m/s.",
            "Calcula distancia de caída libre desde reposo durante 1.5 s usando g = 9.8 m/s².",
            "Explica por qué en MRU la aceleración es cero.",
            "Identifica en una gráfica v-t cuándo el coche acelera, frena o mantiene velocidad.",
            "Calcula velocidad final con v = v0 + at si v0 = 2 m/s, a = 3 m/s² y t = 4 s.",
            "Describe un ejemplo de movimiento parabólico en el lanzamiento de una pieza.",
            "Calcula aceleración centrípeta si v = 5 m/s y r = 2 m.",
        ],
        calc_bank=[
            "Velocidad promedio: el coche pasa de x0 = 0 m a x = 18 m en 1.2 s. Usa v = Δx / Δt y explica el resultado en m/s.",
            "MRU: si después mantiene v = 6.5 m/s durante 3.0 s desde x0 = 2 m, calcula posición con x = x0 + vt.",
            "Aceleración promedio: la velocidad cambia de 1.5 m/s a 7.5 m/s en 2.0 s. Usa a = Δv / Δt.",
            "MRUA velocidad final: con v0 = 2.0 m/s, a = 3.5 m/s² y t = 1.6 s, calcula v = v0 + at.",
            "MRUA posición: con x0 = 0, v0 = 1.0 m/s, a = 4.0 m/s² y t = 1.8 s, calcula x = x0 + v0t + 1/2at².",
            "Caída libre: una pieza cae desde reposo durante 0.80 s. Usa y = y0 + 1/2gt² con g = 9.8 m/s² y reporta la distancia.",
            "Parabólico: una pieza sale con vx = 3.0 m/s durante 1.4 s. Calcula x = vx t y explica por qué el eje vertical se resuelve aparte.",
            "Circular: un coche toma una curva de radio 1.4 m a 3.2 m/s. Calcula ac = v² / r y explica hacia dónde apunta esa aceleración.",
        ],
        product="Registro de telemetría básica con tabla x-t, gráfica, cálculo de velocidad, cálculo de aceleración y decisión sobre un tramo de pista.",
        close="Al terminar la unidad, el estudiante puede describir el movimiento del prototipo sin depender de impresiones: usa datos, gráficas y unidades.",
        visual_phrases={
            2: "La pista se vuelve legible cuando cada tramo tiene una pregunta de medición.",
            3: "Una cantidad sin dirección puede informar; una cantidad con dirección puede decidir.",
            4: "Moverse no siempre significa alejarse: por eso posición y desplazamiento no se confunden.",
            5: "En MRU la constancia es la pista: si la pendiente no cambia, la velocidad tampoco.",
            6: "Acelerar es cambiar la historia de la velocidad, no solo ir rápido.",
            7: "La gravedad no empuja con reloj visible, pero deja marcas cada vez más separadas.",
            8: "Una trayectoria curva se entiende separando lo horizontal de lo vertical.",
            9: "Girar exige aceleración aunque la rapidez parezca constante.",
        },
        mini={},
        dense={2, 3, 5, 6, 8, 9},
        landscape={2, 3, 5, 6, 8, 9},
    ),
    Unit(
        unit="u02",
        title="U2 - Dinámica",
        short="U2 / Dinámica",
        kicker="Unidad 2 / Fuerzas, Newton y Gravitación",
        story="El coche ya tiene telemetría, pero ahora aparece otra pregunta: ¿qué lo hace arrancar, frenar, girar o deformarse? El equipo aprende que ningún movimiento cambia sin interacción.",
        episode="La dinámica convierte la pista en un balance de fuerzas: lo que empuja, lo que se opone y lo que mantiene al prototipo estable.",
        intro_title="La fuerza detrás del cambio",
        intro_1="Newton organizó una idea decisiva: los cambios de movimiento no aparecen de la nada. Si el coche acelera, frena o se desvía, alguna fuerza neta está actuando sobre él.",
        intro_2="En esta unidad se usan vectores, leyes de Newton, torque, resortes y gravitación para explicar cómo un prototipo responde a empujes, peso, fricción y equilibrio.",
        central_idea="La fuerza neta explica la aceleración; el equilibrio aparece cuando las fuerzas o torques se compensan.",
        concepts=[
            ("Fuerza", "Interacción capaz de cambiar movimiento o deformar un cuerpo."),
            ("Vector", "Cantidad con magnitud y dirección."),
            ("Masa", "Medida de inercia; se expresa en kg."),
            ("Peso", "Fuerza gravitatoria: W = mg, en newton."),
            ("Fricción", "Fuerza que se opone al movimiento relativo."),
            ("Torque", "Tendencia de una fuerza a producir giro."),
        ],
        questions=[
            "¿Por qué empujar más fuerte no siempre significa acelerar más?",
            "¿Qué fuerzas aparecen en el coche cuando está quieto sobre la pista?",
            "¿Cómo puede un resorte ayudar a medir una fuerza?",
        ],
        topics={
            2: "Ruta de decisiones de la dinámica",
            3: "Fuerza como vector y diagrama de cuerpo libre",
            4: "Primera ley: inercia y equilibrio",
            5: "Segunda ley de Newton",
            6: "Tercera ley: acción y reacción",
            7: "Torque y equilibrio rotacional",
            8: "Ley de Hooke",
            9: "Gravitación universal",
            10: "Leyes de Kepler",
        },
        formulas=[
            ("Segunda ley", "ΣF = ma", "ΣF en N; m en kg; a en m/s²."),
            ("Peso", "W = mg", "W en N; m en kg; g ≈ 9.8 m/s²."),
            ("Fricción", "f = μN", "f y N en newton; μ no tiene unidad."),
            ("Torque", "τ = Fr senθ", "τ en N·m; F en N; r en m."),
            ("Hooke", "F = kx", "F en N; k en N/m; x en m."),
            ("Gravitación", "F = Gm1m2 / r²", "G = 6.67 x 10^-11 N·m²/kg²; masas en kg; r en m."),
        ],
        exercises=[
            "Calcula fuerza neta para m = 0.050 kg y a = 12 m/s².",
            "Calcula peso de un coche de 0.060 kg usando g = 9.8 m/s².",
            "Dibuja el diagrama de cuerpo libre de un coche que acelera en línea recta.",
            "Explica qué ley de Newton aparece cuando el coche no arranca aunque se empuje poco.",
            "Calcula fricción si μ = 0.20 y N = 0.60 N.",
            "Compara masa y peso con ejemplo del prototipo.",
            "Calcula torque con F = 3 N, r = 0.12 m y θ = 90°.",
            "Calcula fuerza de un resorte con k = 120 N/m y x = 0.03 m.",
            "Explica por qué acción y reacción no se cancelan si actúan en cuerpos distintos.",
            "Relaciona fuerza centrípeta con una curva de radio pequeño.",
            "Describe una situación de equilibrio traslacional en el coche.",
            "Explica por qué la gravedad universal importa aunque el coche sea pequeño.",
        ],
        calc_bank=[
            "Un prototipo de 0.055 kg acelera a 9.0 m/s². Calcula fuerza neta y explica qué interacción podría producirla.",
            "El coche pesa 0.62 N. Calcula su masa aproximada con m = W/g.",
            "Si la normal es 0.54 N y μ = 0.18, calcula fricción y decide si conviene revisar ruedas o pista.",
            "Un alerón recibe 2.5 N a 0.08 m del eje. Calcula torque máximo.",
            "Un resorte se estira 0.025 m al aplicar 4 N. Calcula k.",
            "Calcula fuerza gravitatoria entre dos masas de 1 kg separadas 0.5 m y explica por qué es pequeña en el aula.",
        ],
        product="Diagrama de cuerpo libre del prototipo con cálculo de fuerza neta, fricción o torque y recomendación de diseño.",
        close="Al terminar la unidad, el estudiante interpreta el cambio de movimiento como resultado de fuerzas, no como simple apariencia de rapidez.",
        visual_phrases={
            2: "Cada fuerza cuenta una parte de la historia; la suma decide el movimiento.",
            3: "Una flecha bien dibujada puede evitar una conclusión mal calculada.",
            4: "La inercia no es falta de movimiento: es resistencia a cambiar el estado actual.",
            5: "La segunda ley une lo que empuja con lo que cambia.",
            6: "Toda interacción tiene dos lados, aunque el efecto en cada cuerpo sea distinto.",
            7: "Cuando una fuerza actúa lejos del eje, puede convertir un empuje en giro.",
            8: "Un resorte traduce deformación en fuerza medible.",
            9: "La gravedad aparece pequeña en el prototipo y enorme en el sistema solar.",
            10: "Las órbitas muestran que una misma idea física puede cruzar escalas.",
        },
        mini={},
        dense={2, 3, 5, 7, 8, 9, 10},
        landscape={2, 3, 5, 7, 8, 9, 10},
    ),
    Unit(
        unit="u03",
        title="U3 - Trabajo y Energía",
        short="U3 / Energía",
        kicker="Unidad 3 / Trabajo y Energía",
        story="Dos prototipos llegan casi al mismo tiempo, pero uno vibra más, se calienta y pierde velocidad al final. El equipo descubre que la pregunta no es solo cuánto corre, sino cuánta energía conserva.",
        episode="La energía permite rastrear lo útil y lo perdido: movimiento, altura, deformación, fricción, impacto y potencia.",
        intro_title="Seguir la energía hasta la meta",
        intro_1="La idea de conservación permitió explicar máquinas, choques y movimientos sin mirar cada detalle microscópico. En el coche F1, la energía muestra qué parte del impulso termina como avance y qué parte se pierde.",
        intro_2="Esta unidad conecta trabajo, potencia, energía cinética, potencial, conservación, ímpetu y colisiones para evaluar el desempeño real del prototipo.",
        central_idea="La energía no desaparece: se transforma, se transfiere o se disipa en formas menos útiles para el objetivo.",
        concepts=[
            ("Trabajo", "Transferencia de energía por fuerza a lo largo de una distancia."),
            ("Potencia", "Rapidez con que se realiza trabajo o se transfiere energía."),
            ("Energía cinética", "Energía asociada al movimiento."),
            ("Energía potencial", "Energía asociada a posición o deformación."),
            ("Ímpetu", "Cantidad de movimiento: p = mv."),
            ("Disipación", "Transformación en calor, sonido o fricción."),
        ],
        questions=[
            "¿Puede un coche tener mucha energía y aun así perder una carrera?",
            "¿Qué evidencia mostraría que hay fricción importante?",
            "¿Por qué potencia y energía no significan lo mismo?",
        ],
        topics={
            2: "Ruta de decisiones de energía",
            3: "Trabajo mecánico",
            4: "Energía cinética y energía potencial",
            5: "Gráficas de energía",
            6: "Potencia",
            7: "Conservación de energía mecánica",
            8: "Ímpetu e impulso",
            9: "Colisiones unidimensionales",
            10: "Procesos disipativos",
        },
        formulas=[
            ("Trabajo", "W = Fd cosθ", "W en J; F en N; d en m; θ es el ángulo entre fuerza y desplazamiento."),
            ("Potencia", "P = W / t", "P en W; W en joule; t en segundos."),
            ("Energía cinética", "K = 1/2 mv²", "K en J; m en kg; v en m/s."),
            ("Energía potencial", "U = mgh", "U en J; m en kg; g en m/s²; h en m."),
            ("Ímpetu", "p = mv", "p en kg·m/s; m en kg; v en m/s."),
            ("Impulso", "J = FΔt = Δp", "J en N·s; conecta fuerza aplicada con cambio de ímpetu."),
        ],
        exercises=[
            "Calcula trabajo si una fuerza de 2 N desplaza el coche 4 m en la misma dirección.",
            "Calcula potencia si se realizan 12 J en 3 s.",
            "Calcula energía cinética de 0.055 kg a 6 m/s.",
            "Calcula energía potencial de 0.050 kg a 0.80 m de altura.",
            "Explica por qué la fricción convierte energía útil en calor.",
            "Compara trabajo positivo, negativo y cero con ejemplos.",
            "Calcula ímpetu de 0.060 kg a 5 m/s.",
            "Calcula impulso si una fuerza de 1.5 N actúa durante 0.20 s.",
            "Describe una colisión elástica y una inelástica en una pista escolar.",
            "Interpreta una gráfica donde la energía cinética baja al final.",
            "Relaciona potencia con tiempo de carrera.",
            "Propón una mejora para disminuir disipación.",
        ],
        calc_bank=[
            "Una fuerza de 1.8 N actúa durante 5 m en la dirección del movimiento. Calcula trabajo.",
            "El coche recibe 9 J en 1.5 s. Calcula potencia promedio.",
            "Calcula K para m = 0.052 kg y v = 7.0 m/s.",
            "Calcula U para m = 0.060 kg y h = 0.45 m.",
            "Un coche de 0.055 kg cambia de 3 m/s a 6 m/s. Calcula cambio de energía cinética.",
            "Calcula ímpetu inicial y final si m = 0.050 kg, v1 = 2 m/s y v2 = 8 m/s.",
        ],
        product="Reporte de energía con cálculo de trabajo, energía cinética, potencia y una hipótesis sobre pérdidas por fricción.",
        close="Al terminar la unidad, el estudiante puede defender si una modificación mejora el uso de energía o solo cambia la apariencia del prototipo.",
        visual_phrases={
            2: "La energía se sigue como una pista: entra, se transforma y deja huellas.",
            3: "Una fuerza solo realiza trabajo útil si acompaña al desplazamiento.",
            4: "Moverse y estar en posición también son formas de almacenar energía.",
            5: "Una gráfica de energía revela pérdidas que el cronómetro no explica solo.",
            6: "La potencia pregunta qué tan rápido ocurre la transferencia.",
            7: "Conservar energía no significa que toda sea útil para ganar.",
            8: "El ímpetu ayuda a leer choques y cambios bruscos de movimiento.",
            9: "En una colisión, la pregunta es qué se conserva y qué se transforma.",
            10: "La fricción no roba energía: la cambia a formas menos aprovechables.",
        },
        mini={},
        dense={2, 4, 5, 7, 9},
        landscape={2, 4, 5, 7, 9},
    ),
    Unit(
        unit="u04",
        title="U4 - Termodinámica",
        short="U4 / Termodinámica",
        kicker="Unidad 4 / Termodinámica",
        story="Después de varias pruebas, una parte del prototipo se siente caliente. El equipo podría ignorarlo, pero el calor cuenta una historia: fricción, energía interna, transferencia y eficiencia.",
        episode="La termodinámica permite decidir si el prototipo pierde energía en calor, cómo se transfiere y qué medición térmica conviene registrar.",
        intro_title="Cuando el prototipo también habla en calor",
        intro_1="La termodinámica nació al intentar entender máquinas, vapor, calor y trabajo. En el aula, esas ideas aparecen cuando una pieza se calienta, un gas cambia de volumen o una superficie transfiere energía.",
        intro_2="Esta unidad distingue calor y temperatura, usa escalas termométricas, calcula energía térmica y conecta gases ideales con decisiones de diseño.",
        central_idea="El calor es energía en tránsito; la temperatura indica estado térmico y debe expresarse con escala adecuada.",
        concepts=[
            ("Calor", "Energía que se transfiere por diferencia de temperatura."),
            ("Temperatura", "Medida relacionada con energía cinética promedio de partículas."),
            ("Equilibrio térmico", "Estado donde no hay transferencia neta de calor."),
            ("Calor específico", "Energía necesaria por masa y cambio de temperatura."),
            ("Calor latente", "Energía en cambio de fase sin cambio de temperatura."),
            ("Gas ideal", "Modelo que relaciona presión, volumen, temperatura y moles."),
        ],
        questions=[
            "¿Por qué no es lo mismo calor que temperatura?",
            "¿Qué pieza del coche podría calentarse por fricción?",
            "¿Por qué kelvin se usa en gases ideales?",
        ],
        topics={
            2: "Ruta de decisiones térmicas",
            3: "Calor y temperatura",
            4: "Equilibrio térmico y ley cero",
            5: "Escalas termométricas y dilatación",
            6: "Calor específico y conductividad",
            7: "Conducción, convección y radiación",
            8: "Cambios de fase y calor latente",
            9: "Curvas de calentamiento",
            10: "Primera y segunda ley de la termodinámica",
            11: "Teoría cinética y gases ideales",
        },
        formulas=[
            ("Kelvin", "K = °C + 273.15", "La temperatura absoluta se expresa en kelvin para gases."),
            ("Fahrenheit", "°F = 9/5 °C + 32", "Convierte escalas cuando el instrumento reporte otra unidad."),
            ("Calor sensible", "Q = mcΔT", "Q en J; m en kg o g según c; ΔT en °C o K."),
            ("Calor latente", "Q = mL", "Q en J; m es masa; L es calor latente."),
            ("Dilatación lineal", "ΔL = αL0ΔT", "ΔL y L0 en m; α en 1/°C; ΔT en °C."),
            ("Gas ideal", "PV = nRT", "P, V, n, R y T deben estar en unidades compatibles; T en K."),
        ],
        exercises=[
            "Convierte 25 °C a K.",
            "Convierte 40 °C a °F.",
            "Calcula Q si m = 100 g, c = 4.18 J/g°C y ΔT = 10 °C.",
            "Explica por qué dos objetos pueden tener misma temperatura y distinta energía térmica.",
            "Calcula dilatación si α = 12 x 10^-6 1/°C, L0 = 0.20 m y ΔT = 30 °C.",
            "Describe conducción, convección y radiación con ejemplos del prototipo.",
            "Calcula calor latente si m = 0.05 kg y L = 334000 J/kg.",
            "Interpreta una curva de calentamiento con meseta.",
            "Explica la primera ley con Q, W y ΔU.",
            "Convierte 30 °C a K y úsalo en PV = nRT.",
            "Describe cómo medir temperatura sin tocar una pieza caliente.",
            "Propón una mejora para reducir calentamiento por fricción.",
        ],
        calc_bank=[
            "Convierte 22 °C, 35 °C y 45 °C a kelvin. Explica por qué se suma 273.15.",
            "Calcula Q para 80 g de material con c = 0.90 J/g°C y ΔT = 18 °C.",
            "Una varilla de 0.15 m cambia 25 °C. Usa α = 23 x 10^-6 1/°C y calcula ΔL.",
            "Calcula energía para fundir 0.020 kg de hielo si L = 334000 J/kg.",
            "Usa PV = nRT para calcular n con P = 1 atm, V = 0.50 L, T = 300 K y R = 0.082 L atm/mol K.",
            "Si Q = 120 J entra al sistema y W = 45 J realiza trabajo, calcula ΔU usando ΔU = Q - W.",
        ],
        product="Bitácora térmica del prototipo con conversión de temperatura, cálculo de calor y recomendación para reducir pérdidas.",
        close="Al terminar la unidad, el estudiante puede distinguir temperatura, calor, transferencia y energía interna en situaciones del prototipo.",
        visual_phrases={
            2: "El calor deja pistas donde la energía útil se transforma.",
            3: "Temperatura es lectura de estado; calor es energía en camino.",
            4: "El equilibrio térmico aparece cuando los intercambios dejan de tener dirección neta.",
            5: "Cambiar de escala sin perder significado es parte del cálculo físico.",
            6: "Cada material responde distinto al mismo calor recibido.",
            7: "La energía térmica viaja por contacto, movimiento de fluido o radiación.",
            8: "En un cambio de fase la energía trabaja aunque la temperatura parezca quieta.",
            9: "Una meseta en la curva no es pausa: es energía cambiando el estado.",
            10: "La eficiencia obliga a preguntar qué energía queda disponible para trabajo útil.",
            11: "Un gas se entiende mejor cuando presión, volumen y temperatura se leen juntos.",
        },
        mini={},
        dense={2, 3, 5, 7, 9, 10, 11},
        landscape={2, 3, 5, 7, 9, 10, 11},
    ),
    Unit(
        unit="u05",
        title="U5 - Ondas y Sonido",
        short="U5 / Ondas",
        kicker="Unidad 5 / Ondas y Sonido",
        story="El coche más veloz no siempre es el mejor: un prototipo puede vibrar, sonar demasiado o revelar fallas por su frecuencia dominante. El equipo aprende a escuchar datos.",
        episode="Las ondas permiten estudiar vibración, reflexión, interferencia, sonido y Doppler como evidencia del comportamiento del prototipo.",
        intro_title="Escuchar el prototipo como sistema físico",
        intro_1="Las ondas explican cómo se transporta energía sin transportar materia de la misma manera. En sonido, vibración y señales, la información viaja en forma de frecuencia, periodo, longitud de onda y amplitud.",
        intro_2="En esta unidad el ruido del coche se convierte en dato: se mide, se grafica y se relaciona con vibración, energía y diseño.",
        central_idea="Una onda se describe por amplitud, longitud de onda, frecuencia, periodo y rapidez; el sonido aplica esas relaciones a vibraciones audibles.",
        concepts=[
            ("Onda", "Perturbación que transporta energía."),
            ("Amplitud", "Máxima separación respecto al equilibrio."),
            ("Frecuencia", "Ciclos por segundo, en hertz."),
            ("Periodo", "Tiempo de un ciclo, en segundos."),
            ("Longitud de onda", "Distancia entre puntos equivalentes, en metros."),
            ("Doppler", "Cambio aparente de frecuencia por movimiento relativo."),
        ],
        questions=[
            "¿Qué diferencia hay entre frecuencia y periodo?",
            "¿Por qué una vibración puede revelar una falla del prototipo?",
            "¿Cómo se relacionan longitud de onda y rapidez del sonido?",
        ],
        topics={
            2: "Ruta de decisiones ondulatorias",
            3: "Ondas mecánicas",
            4: "Parámetros de una onda",
            5: "Reflexión y refracción",
            6: "Difracción e interferencia",
            7: "Energía, intensidad y sonido",
            8: "Ondas estacionarias y efecto Doppler",
        },
        formulas=[
            ("Rapidez de onda", "v = fλ", "v en m/s; f en Hz; λ en m."),
            ("Periodo", "T = 1 / f", "T en segundos; f en hertz."),
            ("Frecuencia", "f = 1 / T", "f en hertz; T en segundos."),
            ("Intensidad", "I = P / A", "I en W/m²; P en watt; A en m²."),
            ("Nivel sonoro", "β = 10 log(I/I0)", "β en dB; I0 = 1 x 10^-12 W/m²."),
            ("Tubo abierto", "fn = n v / 2L", "fn en Hz; v en m/s; L en m; n entero positivo."),
        ],
        exercises=[
            "Calcula longitud de onda si v = 343 m/s y f = 686 Hz.",
            "Calcula periodo si f = 50 Hz.",
            "Calcula frecuencia si T = 0.02 s.",
            "Explica por qué el sonido necesita un medio material.",
            "Distingue reflexión y refracción con ejemplos de onda.",
            "Describe interferencia constructiva y destructiva.",
            "Calcula intensidad si P = 0.02 W y A = 4 m².",
            "Explica qué indica un aumento de amplitud en una vibración.",
            "Relaciona frecuencia dominante con ruido del prototipo.",
            "Describe un caso donde aparezca efecto Doppler.",
            "Propón cómo usar Audacity o una app de audio para registrar sonido.",
            "Explica por qué reducir vibración puede mejorar energía útil.",
        ],
        calc_bank=[
            "El sonido del prototipo tiene f = 850 Hz. Calcula λ con v = 343 m/s.",
            "Una vibración tiene T = 0.004 s. Calcula frecuencia.",
            "Una onda mide λ = 0.50 m y f = 12 Hz. Calcula rapidez.",
            "Calcula intensidad si una fuente de 0.05 W distribuye energía en 2.5 m².",
            "Compara dos frecuencias: 400 Hz y 1200 Hz. Calcula sus periodos y decide cuál vibra más rápido.",
            "Un tubo abierto de L = 0.30 m usa v = 343 m/s. Calcula frecuencia fundamental con f1 = v/2L.",
        ],
        product="Registro acústico o de vibración con cálculo de frecuencia, periodo o longitud de onda y propuesta de reducción de ruido.",
        close="Al terminar la unidad, el estudiante puede leer el sonido como evidencia física y no solo como molestia.",
        visual_phrases={
            2: "Una vibración ordenada se puede medir, comparar y corregir.",
            3: "La onda lleva energía aunque el material no viaje con ella hasta la meta.",
            4: "Frecuencia, periodo y longitud de onda son tres formas de contar el mismo ritmo.",
            5: "Cuando una onda cambia de medio, cambia también la forma de interpretarla.",
            6: "Dos ondas pueden reforzarse o debilitarse sin tocar piezas del coche.",
            7: "El ruido tiene números: intensidad, frecuencia y energía transportada.",
            8: "El Doppler recuerda que escuchar también depende del movimiento relativo.",
        },
        mini={},
        dense={2, 4, 5, 6, 7, 8},
        landscape={2, 4, 5, 6, 7, 8},
    ),
]


def main() -> None:
    body_parts = [front_pages()]
    for unit in UNITS:
        body_parts.append(build_unit(unit))
    body_parts.append(closure_pages())
    html = html_shell("\n".join(body_parts))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()
