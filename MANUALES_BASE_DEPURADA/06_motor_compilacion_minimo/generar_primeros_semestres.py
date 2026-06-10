from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
MANUALES = ROOT / "01_fuente_principal_markdown" / "manuales"
VISUALES = ROOT / "05_assets_visuales_iconos" / "visuales"
PROMPTS = ROOT / "05_assets_visuales_iconos" / "prompts-visuales"
DOCS = ROOT / "07_docs_pedagogicos"

CSS_REL = "../../primer-manual.css"
IMG_REL_PREFIX = "../../../../05_assets_visuales_iconos/visuales"


@dataclass
class Visual:
    id: str
    src: str
    desc: str
    tipo: str
    rol: str


@dataclass
class Page:
    title: str
    kicker: str
    body: str
    classes: str = ""
    plain: bool = False


def ascii_text(value: str) -> str:
    value = value.replace("–", "-").replace("—", "-").replace("’", "'")
    value = value.replace("“", '"').replace("”", '"').replace("·", " ")
    value = unicodedata.normalize("NFKD", value)
    return value.encode("ascii", "ignore").decode("ascii")


def h(value: str) -> str:
    return escape(ascii_text(str(value)), quote=True)


def short(value: str, limit: int = 180) -> str:
    text = " ".join(ascii_text(value).split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def slug_title(stem: str) -> str:
    bits = stem.split("__")
    if len(bits) < 3:
        return stem
    tipo = bits[1].replace("-", " ")
    rol = bits[2].replace("-", " ")
    return f"{tipo.title()} - {rol}"


def extract_prompt_data(prompt_path: Path | None, fallback_id: str) -> tuple[str, str, str]:
    if not prompt_path or not prompt_path.exists():
        return slug_title(fallback_id), "visual pedagogico asociado al tema de la pagina", "contenido"

    raw = prompt_path.read_text(encoding="utf-8", errors="replace")
    text = ascii_text(raw)
    tipo = "visual"
    rol = "contenido"
    for line in text.splitlines()[:40]:
        if line.startswith("tipo:"):
            tipo = line.split(":", 1)[1].strip()
        if line.startswith("rol_archivo:"):
            rol = line.split(":", 1)[1].strip()

    desc = ""
    match = re.search(r"## Descripcion original del manual\s*(.*?)(?:\n## |\Z)", text, re.S)
    if match:
        lines = []
        for line in match.group(1).splitlines():
            clean = line.strip()
            if not clean:
                continue
            if clean.startswith(">"):
                clean = clean[1:].strip()
            if clean.startswith("|"):
                continue
            lines.append(clean)
        desc = " ".join(lines)

    if not desc:
        desc = slug_title(prompt_path.stem)
    return desc, tipo, rol


def find_prompt(manual: int, unit: str, stem: str) -> Path | None:
    prompt_dir = PROMPTS / f"manual-{manual}" / "sem-1" / unit
    if not prompt_dir.exists():
        return None
    matches = sorted(prompt_dir.glob(f"{stem}*.md"))
    return matches[0] if matches else None


def visual_sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"-(\d+)$", path.stem)
    return (int(match.group(1)) if match else 999, path.stem)


def get_visuals(manual: int, unit: str) -> list[Visual]:
    visual_dir = VISUALES / f"manual-{manual}" / unit
    if not visual_dir.exists():
        return []

    visuals: list[Visual] = []
    for img in sorted(visual_dir.iterdir(), key=visual_sort_key):
        if img.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp", ".svg"}:
            continue
        prompt = find_prompt(manual, unit, img.stem)
        desc, tipo, rol = extract_prompt_data(prompt, img.stem)
        src = f"{IMG_REL_PREFIX}/manual-{manual}/{unit}/{img.name}"
        visuals.append(Visual(img.stem, src, desc, tipo, rol))
    return visuals


def figure(visual: Visual | None, mode: str = "half") -> str:
    if not visual:
        return ""
    return (
        f'<figure class="visual {mode}" data-visual-id="{h(visual.id)}">'
        f'<img src="{h(visual.src)}" alt="{h(short(visual.desc, 130))}">'
        f"<figcaption>{h(visual.id)}. {h(short(visual.desc, 210))}</figcaption>"
        "</figure>"
    )


def bullets(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{h(item)}</li>" for item in items) + "</ul>"


def formula_table(formulas: list[dict[str, str]]) -> str:
    rows = []
    for item in formulas:
        rows.append(
            "<tr>"
            f"<td><div class=\"formula\">{h(item['expr'])}</div></td>"
            f"<td>{h(item['meaning'])}</td>"
            f"<td>{h(item['vars'])}</td>"
            "</tr>"
        )
    return (
        "<table><tr><th>Formula o modelo</th><th>Uso</th><th>Elementos y unidades</th></tr>"
        + "".join(rows)
        + "</table>"
    )


def render_page(page: Page, manual_label: str, number: int) -> str:
    classes = f"page {page.classes}".strip()
    if page.plain:
        return f'<section class="{h(classes)}">\n{page.body}\n</section>'
    footer = (
        f'<div class="footer"><span>{h(manual_label)}</span>'
        f"<span>Semestre 1 / p. {number}</span></div>"
    )
    return (
        f'<section class="{h(classes)}">\n'
        f'<p class="kicker">{h(page.kicker)}</p>\n'
        f"<h2>{h(page.title)}</h2>\n"
        f"{page.body}\n"
        f"{footer}\n"
        "</section>"
    )


def render_html(title: str, pages: list[Page], manual_label: str) -> str:
    body = "\n\n".join(render_page(page, manual_label, idx + 1) for idx, page in enumerate(pages))
    return (
        "<!doctype html>\n"
        '<html lang="es">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"  <title>{h(title)}</title>\n"
        f'  <link rel="stylesheet" href="{CSS_REL}">\n'
        "</head>\n"
        "<body>\n"
        f"{body}\n"
        "</body>\n"
        "</html>\n"
    )


def make_exercises(unit: dict[str, object]) -> list[str]:
    title = str(unit["title"])
    product = str(unit["product"])
    data = str(unit["data"])
    return [
        f"Define el problema central de {title} usando solo datos observables del caso: {data}.",
        f"Identifica tres variables medibles para producir {product} y escribe la unidad de cada una.",
        f"Selecciona la formula principal de la unidad, sustituye datos razonables y conserva unidades.",
        f"Construye una tabla de 4 filas con dato, simbolo, unidad y criterio de aceptacion.",
        f"Explica en 5 lineas la analogia de la unidad sin usar palabras tecnicas innecesarias.",
        f"Resuelve un caso con un dato faltante: indica que falta, como se mide y por que importa.",
        f"Compara dos escenarios del caso y decide cual requiere intervencion inmediata.",
        f"Redacta una conclusion que no exceda 60 palabras y que cite al menos dos datos.",
        f"Propone un mini experimento de 15 minutos para verificar una afirmacion de la teoria.",
        f"Detecta un error comun de unidades y corrige el procedimiento paso a paso.",
        f"Convierte los datos del caso en una grafica, diagrama, tabla o prompt verificable.",
        f"Escribe una pregunta de investigacion que pueda responderse con evidencia de aula.",
        f"Calcula o estima el resultado esperado antes de ejecutar la practica.",
        f"Disena una rubrica de 4 criterios para evaluar {product}.",
        f"Explica que dato cambiaria si el contexto escolar fuera diferente y justifica la decision.",
        f"Cierra con una recomendacion tecnica para el equipo, separando hecho, inferencia y accion.",
    ]


def exercise_pages(unit: dict[str, object], kicker: str) -> list[Page]:
    exercises = make_exercises(unit)
    pages: list[Page] = []
    for idx in range(0, len(exercises), 4):
        chunk = exercises[idx : idx + 4]
        body = "".join(
            f'<div class="exercise"><strong>{i + 1}.</strong> {h(text)}</div>'
            for i, text in enumerate(chunk, start=idx)
        )
        body += (
            '<div class="box practice-box">'
            "<h3>Regla de banco</h3>"
            "<p>Trabaja en parejas, deja procedimiento visible y no entregues solo el resultado. "
            "Cada pagina concentra cuatro ejercicios para hoja carta.</p>"
            "</div>"
        )
        pages.append(Page(f"Banco de ejercicios {idx // 4 + 1}", kicker, body))
    return pages


def visual_pages(unit: dict[str, object], visuals: list[Visual], kicker: str) -> list[Page]:
    pages: list[Page] = []
    for visual in visuals[1:]:
        body = (
            f"{figure(visual, 'half')}"
            '<div class="grid-2">'
            '<div class="box theory-box">'
            "<h3>Lectura del concepto</h3>"
            f"<p>{h(short(visual.desc, 330))}</p>"
            "</div>"
            '<div class="box practice-box">'
            "<h3>Uso en actividad</h3>"
            f"<p>El estudiante debe conectar esta imagen con {h(unit['title'])}: "
            "nombrar los elementos visibles, justificar la relacion con el caso y registrar una evidencia.</p>"
            "</div>"
            "</div>"
        )
        pages.append(Page(f"{visual.id}: lectura guiada", kicker, body))
    return pages


def unit_pages(manual: int, unit: dict[str, object], min_pages: int) -> list[Page]:
    unit_id = str(unit["id"])
    kicker = f"Manual {manual} / {unit_id.upper()} / 40% teoria - 60% practica"
    visuals = get_visuals(manual, unit_id)
    pages: list[Page] = []

    pages.append(
        Page(
            "",
            "",
            (
                '<div class="cover-text">'
                f'<p class="kicker">{h(kicker)}</p>'
                f"<h1>{h(unit['title'])}</h1>"
                f'<p class="subtitle">{h(unit["case"])}</p>'
                "</div>"
                f"{figure(visuals[0] if visuals else None, 'full')}"
                '<div class="meta-strip">'
                f'<div class="meta"><strong>Historia</strong>{h(unit["history_short"])}</div>'
                f'<div class="meta"><strong>Producto</strong>{h(unit["product"])}</div>'
                '<div class="meta"><strong>Distribucion</strong>40% teoria / 60% practica.</div>'
                "</div>"
            ),
            classes="cover",
            plain=True,
        )
    )

    pages.append(
        Page(
            "Historia, analogia y preguntas",
            kicker,
            (
                f"<p>{h(unit['history'])}</p>"
                f"<p><strong>Analogia:</strong> {h(unit['analogy'])}</p>"
                '<div class="box question-box"><h3>Preguntas introductorias</h3>'
                f"{bullets(unit['questions'])}</div>"
                '<div class="ratio"><div class="theory">40% comprender</div>'
                '<div class="practice">60% medir, construir y defender evidencia</div></div>'
            ),
        )
    )

    pages.append(
        Page(
            "Modelo mental antes de la herramienta",
            kicker,
            (
                f"<p>{h(unit['theory'])}</p>"
                '<div class="box theory-box"><h3>Elementos clave</h3>'
                f"{bullets(unit['keywords'])}</div>"
                '<div class="box practice-box"><h3>Microactividad</h3>'
                f"<p>Antes de usar software, calculadora o IA, dibuja el sistema de {h(unit['title'])} "
                "con entradas, proceso, salida esperada y riesgo de error.</p></div>"
            ),
        )
    )

    pages.append(
        Page(
            "Formulas, variables y unidades",
            kicker,
            (
                "<p>Las formulas no se memorizan aisladas: cada simbolo debe tener significado, "
                "unidad y condicion de uso.</p>"
                f"{formula_table(unit['formulas'])}"
                '<div class="box question-box"><h3>Chequeo rapido</h3>'
                "<p>Si una operacion mezcla unidades incompatibles, el resultado no es evidencia; "
                "es ruido con apariencia numerica.</p></div>"
            ),
        )
    )

    pages.append(
        Page(
            "Caso resuelto guiado",
            kicker,
            (
                f"<p><strong>Situacion:</strong> {h(unit['case'])}</p>"
                f"<p><strong>Datos de partida:</strong> {h(unit['data'])}</p>"
                "<ol>"
                "<li>Se separan datos observados, supuestos y unidades.</li>"
                "<li>Se elige el modelo mas simple que responde la pregunta.</li>"
                "<li>Se calcula o se organiza la evidencia.</li>"
                "<li>Se redacta una conclusion tecnica con limite y siguiente prueba.</li>"
                "</ol>"
                f'<div class="box practice-box"><h3>Producto esperado</h3><p>{h(unit["product"])}</p></div>'
            ),
        )
    )

    pages.extend(visual_pages(unit, visuals, kicker))

    pages.append(
        Page(
            "Especificacion de actividad y practica",
            kicker,
            (
                "<table><tr><th>Fase</th><th>Accion del estudiante</th><th>Evidencia</th></tr>"
                f"<tr><td>Explorar</td><td>Leer historia, imagenes y preguntas de {h(unit['title'])}.</td><td>Mapa breve del problema.</td></tr>"
                f"<tr><td>Calcular</td><td>Usar formulas con unidades y datos del caso: {h(unit['data'])}.</td><td>Procedimiento revisable.</td></tr>"
                f"<tr><td>Construir</td><td>Producir {h(unit['product'])}.</td><td>Archivo, tabla, bitacora o prototipo.</td></tr>"
                "<tr><td>Defender</td><td>Explicar limite, error posible y siguiente mejora.</td><td>Conclusion oral o escrita.</td></tr>"
                "</table>"
                '<div class="box practice-box"><h3>Proporcion</h3>'
                "<p>La clase debe dedicar una introduccion corta a teoria y el bloque mayor a practica, revision y correccion.</p></div>"
            ),
        )
    )

    pages.extend(exercise_pages(unit, kicker))

    pages.append(
        Page(
            "Practica integradora",
            kicker,
            (
                f"<p>La practica integra historia, teoria, imagenes y calculo para entregar {h(unit['product'])}.</p>"
                "<ol>"
                "<li>Define una pregunta verificable.</li>"
                "<li>Recolecta o simula datos minimos.</li>"
                "<li>Aplica el modelo de la unidad.</li>"
                "<li>Presenta evidencia en formato limpio.</li>"
                "<li>Escribe una mejora para la siguiente iteracion.</li>"
                "</ol>"
                '<table class="rubric"><tr><th>Criterio</th><th>Logrado</th><th>En mejora</th></tr>'
                "<tr><td>Unidades</td><td>Consistentes en todo el proceso.</td><td>Hay mezcla o faltan simbolos.</td></tr>"
                "<tr><td>Argumento</td><td>Conclusion sale de datos.</td><td>Conclusion depende de opinion.</td></tr>"
                "<tr><td>Producto</td><td>Se puede revisar o replicar.</td><td>No queda evidencia suficiente.</td></tr>"
                "</table>"
            ),
        )
    )

    pages.append(
        Page(
            "Cierre de unidad",
            kicker,
            (
                f"<p>Al cerrar {h(unit['title'])}, el estudiante debe explicar la historia con lenguaje tecnico "
                "sin perder el hilo practico.</p>"
                '<div class="grid-2">'
                '<div class="box theory-box"><h3>Teoria minima</h3>'
                f"{bullets(unit['keywords'][:4])}</div>"
                '<div class="box practice-box"><h3>Evidencias</h3>'
                "<ul><li>Banco de ejercicios corregido.</li><li>Producto integrador.</li><li>Bitacora de errores.</li><li>Referencia consultada.</li></ul>"
                "</div></div>"
            ),
        )
    )

    pad = 1
    while len(pages) < min_pages:
        pages.append(
            Page(
                f"Taller adicional {pad}",
                kicker,
                (
                    f"<p>Este taller extiende la practica de {h(unit['title'])} con una variacion del caso.</p>"
                    '<div class="exercise"><strong>A.</strong> Cambia un dato del escenario y predice el efecto antes de calcular.</div>'
                    '<div class="exercise"><strong>B.</strong> Repite el procedimiento con el nuevo dato y conserva unidades.</div>'
                    '<div class="exercise"><strong>C.</strong> Compara ambos resultados en una tabla de dos columnas.</div>'
                    '<div class="exercise"><strong>D.</strong> Redacta una decision tecnica basada en la comparacion.</div>'
                ),
            )
        )
        pad += 1
    return pages


def cover_page(manual: int, data: dict[str, object], visuals: list[Visual]) -> Page:
    body = (
        '<div class="cover-text">'
        f'<p class="kicker">Manual {manual} / Semestre 1 completo</p>'
        f"<h1>{h(data['title'])}</h1>"
        f'<p class="subtitle">{h(data["subtitle"])}</p>'
        "</div>"
        f"{figure(visuals[0] if visuals else None, 'full')}"
        '<div class="meta-strip">'
        f'<div class="meta"><strong>Historia conductora</strong>{h(data["case"])}</div>'
        f'<div class="meta"><strong>Publico</strong>{h(data["audience"])}</div>'
        '<div class="meta"><strong>Formato</strong>Hoja carta HTML con imagenes inyectadas.</div>'
        "</div>"
    )
    return Page("", "", body, classes="cover", plain=True)


def front_pages(manual: int, data: dict[str, object], sem_visuals: list[Visual]) -> list[Page]:
    units = data["units"]
    manual_label = f"Manual {manual} / Semestre 1"
    toc = "".join(
        f'<div class="toc-row"><strong>{h(unit["id"].upper())}</strong><span>{h(unit["title"])}</span><span>{h(unit["product"])}</span></div>'
        for unit in units
    )
    return [
        cover_page(manual, data, sem_visuals),
        Page(
            "Carta al estudiante",
            manual_label,
            (
                f"<p>Este semestre se construye alrededor de una historia: {h(data['case'])}. "
                "Cada unidad inicia con una pregunta real, introduce teoria suficiente y pasa rapido a practica.</p>"
                "<p>Tu trabajo no es copiar definiciones. Tu trabajo es producir evidencia: calculos, tablas, prototipos, "
                "prompts, visualizaciones o conclusiones defendibles.</p>"
                '<div class="box practice-box"><h3>Metodo de estudio</h3>'
                "<p>Lee la historia, subraya datos, revisa formulas con unidades, resuelve cuatro ejercicios por pagina "
                "y cierra cada bloque con una evidencia verificable.</p></div>"
            ),
        ),
        Page(
            "Carta al docente",
            manual_label,
            (
                "<p>La estructura mantiene 40% teoria y 60% practica. La teoria aparece como modelo mental, formula "
                "o criterio de decision; la practica aparece como banco, taller, producto y defensa.</p>"
                "<p>Las imagenes no se usan como decoracion. Cada visual se inserta en una pagina cuyo texto explica "
                "el concepto inmediato del prompt original.</p>"
                '<div class="box question-box"><h3>Regla de aula</h3>'
                "<p>Si una imagen no coincide con la actividad de la pagina, se mueve o se sustituye antes de imprimir.</p></div>"
            ),
        ),
        Page(
            "Mapa de contenidos",
            manual_label,
            f'<div class="toc-list">{toc}</div>',
        ),
        Page(
            "Hilo conductor",
            manual_label,
            (
                f"<p>{h(data['story'])}</p>"
                f"{figure(sem_visuals[1] if len(sem_visuals) > 1 else None, 'half')}"
                '<div class="box theory-box"><h3>Como leer el semestre</h3>'
                "<p>La primera lectura da contexto; la segunda ubica formulas y conceptos; la tercera se hace con lapiz, "
                "datos y evidencia.</p></div>"
            ),
        ),
        Page(
            "Competencias y productos",
            manual_label,
            (
                "<table><tr><th>Competencia</th><th>Producto verificable</th><th>Revision</th></tr>"
                "<tr><td>Comprender modelos</td><td>Mapa o diagrama con variables.</td><td>Coherencia conceptual.</td></tr>"
                "<tr><td>Aplicar procedimientos</td><td>Banco de ejercicios y practica.</td><td>Unidades, datos y pasos.</td></tr>"
                "<tr><td>Comunicar evidencia</td><td>Reporte corto o presentacion.</td><td>Conclusion defendible.</td></tr>"
                "<tr><td>Usar recursos digitales</td><td>Simulacion, prompt, tabla o codigo.</td><td>Uso pertinente y documentado.</td></tr>"
                "</table>"
            ),
        ),
        Page(
            "Diagnostica 1",
            manual_label,
            (
                '<div class="exercise"><strong>1.</strong> Explica que dato necesitarias antes de afirmar que una solucion funciona.</div>'
                '<div class="exercise"><strong>2.</strong> Convierte una observacion cotidiana en una pregunta medible.</div>'
                '<div class="exercise"><strong>3.</strong> Identifica una unidad, una variable y un posible error de medicion.</div>'
                '<div class="exercise"><strong>4.</strong> Describe una evidencia que no dependa de opinion.</div>'
            ),
        ),
        Page(
            "Diagnostica 2",
            manual_label,
            (
                '<div class="exercise"><strong>5.</strong> Lee una grafica o diagrama y escribe dos inferencias validas.</div>'
                '<div class="exercise"><strong>6.</strong> Distingue hecho, supuesto y conclusion en un parrafo tecnico.</div>'
                '<div class="exercise"><strong>7.</strong> Propone una mejora a un procedimiento incompleto.</div>'
                '<div class="exercise"><strong>8.</strong> Escribe una pregunta para investigar durante el semestre.</div>'
            ),
        ),
        Page(
            "Uso de imagenes y fuentes",
            manual_label,
            (
                f"{figure(sem_visuals[2] if len(sem_visuals) > 2 else None, 'half')}"
                "<p>Cada imagen conserva ID estable. El ID permite volver al prompt, revisar el rol de la imagen "
                "y corregirla si no representa el contenido.</p>"
                '<div class="box practice-box"><h3>Evidencia visual</h3>'
                "<p>Cuando uses una imagen en una respuesta, no la describas completa: selecciona el elemento que prueba tu argumento.</p></div>"
            ),
        ),
        Page(
            "Ruta de trabajo",
            manual_label,
            (
                "<ol><li>Entrar por historia y preguntas.</li><li>Identificar datos y unidades.</li>"
                "<li>Usar formula, modelo o herramienta.</li><li>Resolver banco de ejercicios.</li>"
                "<li>Construir producto de unidad.</li><li>Contrastar con referencias y anexos.</li></ol>"
                '<div class="box theory-box"><h3>Cierre semanal</h3>'
                "<p>Cada semana termina con una decision: que se sabe, que falta y que accion sigue.</p></div>"
            ),
        ),
    ]


def link_grid(links: list[tuple[str, str]]) -> str:
    return '<div class="link-grid">' + "".join(
        f'<div class="link-card"><strong>{h(name)}</strong><br><a href="{h(url)}">{h(url)}</a></div>'
        for name, url in links
    ) + "</div>"


def periodic_table() -> str:
    rows = [
        ["H"] + [""] * 16 + ["He"],
        ["Li", "Be"] + [""] * 10 + ["B", "C", "N", "O", "F", "Ne"],
        ["Na", "Mg"] + [""] * 10 + ["Al", "Si", "P", "S", "Cl", "Ar"],
        ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
        ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
        ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
        ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"],
        ["", "", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "", ""],
        ["", "", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "", ""],
    ]
    cells = []
    for row in rows:
        for symbol in row:
            cls = "element" if symbol else "element empty"
            cells.append(f'<div class="{cls}">{h(symbol)}</div>')
    return '<div class="mini-periodic">' + "".join(cells) + "</div>"


def appendix_pages(manual: int, data: dict[str, object], sem_visuals: list[Visual], target_extra: int) -> list[Page]:
    label = f"Manual {manual} / Anexos semestre 1"
    pages: list[Page] = []
    tri_titles = ["Trimestre 1", "Trimestre 2", "Trimestre 3"]
    for idx, tri in enumerate(tri_titles):
        visual = sem_visuals[min(idx * 3, len(sem_visuals) - 1)] if sem_visuals else None
        pages.append(
            Page(
                "",
                "",
                (
                    '<div class="cover-text">'
                    f'<p class="kicker">{h(label)}</p>'
                    f"<h1>{h(tri)}</h1>"
                    f'<p class="subtitle">Portada interna para separar avance, evaluacion y material complementario.</p>'
                    "</div>"
                    f"{figure(visual, 'full')}"
                    '<div class="meta-strip">'
                    f'<div class="meta"><strong>Manual</strong>{h(data["title"])}</div>'
                    '<div class="meta"><strong>Uso</strong>Separador imprimible.</div>'
                    '<div class="meta"><strong>Revision</strong>Integrar evidencias del trimestre.</div>'
                    "</div>"
                ),
                classes="cover trimester",
                plain=True,
            )
        )

    pages.extend(
        [
            Page(
                "Material extra de trabajo",
                label,
                (
                    "<table><tr><th>Material</th><th>Uso</th><th>Evidencia</th></tr>"
                    "<tr><td>Bitacora</td><td>Registrar datos, errores y correcciones.</td><td>Una entrada por practica.</td></tr>"
                    "<tr><td>Calculadora o hoja de calculo</td><td>Verificar operaciones y tablas.</td><td>Archivo con formulas visibles.</td></tr>"
                    "<tr><td>Simulador o herramienta digital</td><td>Explorar escenarios antes de laboratorio.</td><td>Captura o reporte breve.</td></tr>"
                    "<tr><td>Referencias</td><td>Contrastar definiciones y procedimientos.</td><td>URL o cita corta.</td></tr>"
                    "</table>"
                ),
            ),
            Page(
                "Lecturas complementarias",
                label,
                (
                    f"<p>Las lecturas se usan para ampliar {h(data['case'])}, no para reemplazar la practica.</p>"
                    f"{bullets(data['readings'])}"
                    '<div class="box question-box"><h3>Regla de lectura</h3>'
                    "<p>Despues de leer, el estudiante escribe una idea util, una duda y una accion aplicable.</p></div>"
                ),
            ),
            Page(
                "Links y referencias",
                label,
                link_grid(data["links"]),
            ),
            Page(
                "Formato de reporte",
                label,
                (
                    "<table><tr><th>Seccion</th><th>Contenido</th><th>Extension</th></tr>"
                    "<tr><td>Pregunta</td><td>Problema verificable.</td><td>2 lineas</td></tr>"
                    "<tr><td>Datos</td><td>Tabla con unidades.</td><td>1 tabla</td></tr>"
                    "<tr><td>Procedimiento</td><td>Pasos numerados.</td><td>6 a 10 pasos</td></tr>"
                    "<tr><td>Resultado</td><td>Calculo, grafica, prompt, codigo o producto.</td><td>1 evidencia</td></tr>"
                    "<tr><td>Conclusion</td><td>Hecho, inferencia y accion.</td><td>80 palabras</td></tr>"
                    "</table>"
                ),
            ),
            Page(
                "Rubrica general",
                label,
                (
                    '<table class="rubric"><tr><th>Criterio</th><th>Excelente</th><th>Suficiente</th><th>Por corregir</th></tr>'
                    "<tr><td>Datos</td><td>Completos y con unidades.</td><td>Falta un detalle menor.</td><td>No son verificables.</td></tr>"
                    "<tr><td>Procedimiento</td><td>Replicable.</td><td>Entendible pero incompleto.</td><td>No permite revisar.</td></tr>"
                    "<tr><td>Producto</td><td>Resuelve el caso.</td><td>Responde parcialmente.</td><td>No responde la pregunta.</td></tr>"
                    "<tr><td>Comunicacion</td><td>Clara y tecnica.</td><td>Clara con imprecisiones.</td><td>Confusa o sin evidencia.</td></tr>"
                    "</table>"
                ),
            ),
            Page(
                "Glosario del semestre",
                label,
                "<table><tr><th>Termino</th><th>Uso en el manual</th></tr>"
                + "".join(f"<tr><td>{h(term)}</td><td>{h(desc)}</td></tr>" for term, desc in data["glossary"])
                + "</table>",
            ),
            Page(
                "Evaluacion integradora",
                label,
                (
                    f"<p>La evaluacion final retoma la historia: {h(data['case'])}.</p>"
                    '<div class="exercise"><strong>1.</strong> Selecciona una unidad y resume el problema en datos.</div>'
                    '<div class="exercise"><strong>2.</strong> Usa una formula, modelo o herramienta con unidades o criterios claros.</div>'
                    '<div class="exercise"><strong>3.</strong> Propone una mejora basada en evidencia.</div>'
                    '<div class="exercise"><strong>4.</strong> Presenta el resultado en 3 minutos con una imagen del manual.</div>'
                ),
            ),
            Page(
                "Indice analitico basico",
                label,
                (
                    "<p>Usa este indice para localizar evidencias, formulas y productos antes de imprimir o convertir a PDF.</p>"
                    + bullets([f"{unit['id'].upper()} - {unit['title']} - {unit['product']}" for unit in data["units"]])
                ),
            ),
        ]
    )

    if manual == 1:
        pages.append(
            Page(
                "Tabla periodica compacta",
                label,
                (
                    "<p>Tabla periodica de consulta rapida para nomenclatura, mol, enlaces y propiedades periodicas.</p>"
                    f"{periodic_table()}"
                    '<div class="box theory-box"><h3>Uso recomendado</h3>'
                    "<p>Primero identifica grupo y periodo; despues relaciona valencia, electronegatividad y tipo de enlace.</p></div>"
                ),
            )
        )

    while len(pages) < target_extra:
        pages.append(
            Page(
                f"Lectura complementaria {len(pages) - 8}",
                label,
                (
                    "<p>Selecciona una fuente del listado, resume su idea central y conectala con una practica del semestre.</p>"
                    '<div class="exercise"><strong>A.</strong> Escribe una cita o liga.</div>'
                    '<div class="exercise"><strong>B.</strong> Resume en 5 lineas.</div>'
                    '<div class="exercise"><strong>C.</strong> Explica que cambia en tu procedimiento.</div>'
                    '<div class="exercise"><strong>D.</strong> Formula una nueva pregunta verificable.</div>'
                ),
            )
        )
    return pages


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
    links = len(re.findall(r'<a href="', text))
    return {"pages": pages, "images": len(images), "broken": broken, "links": links}


def build_manual(manual: int, data: dict[str, object]) -> tuple[Path, dict[str, int]]:
    sem_visuals = get_visuals(manual, "sem1")
    units = data["units"]
    min_unit_pages = 25 if len(units) == 4 else 20
    target_extra = 23 if len(units) == 4 else 20

    pages: list[Page] = []
    pages.extend(front_pages(manual, data, sem_visuals))
    for unit in units:
        pages.extend(unit_pages(manual, unit, min_unit_pages))
    pages.extend(appendix_pages(manual, data, sem_visuals, target_extra))

    out_dir = MANUALES / f"manual-{manual}" / "semestre-1"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"manual-{manual}-semestre-1-completo.html"
    html = render_html(f"Manual {manual} - Semestre 1 completo", pages, f"Manual {manual}")
    out_path.write_text(html, encoding="utf-8", newline="\n")
    stats = verify_html(out_path)
    return out_path, stats


def make_index(results: dict[int, tuple[Path, dict[str, int]]]) -> Path:
    rows = []
    for manual, (path, stats) in results.items():
        rel = path.relative_to(MANUALES).as_posix()
        rows.append(
            "<tr>"
            f"<td>Manual {manual}</td>"
            f"<td>{h(DATA[manual]['title'])}</td>"
            f"<td>{stats['pages']}</td>"
            f"<td>{stats['images']}</td>"
            f"<td>{stats['links']}</td>"
            f"<td>{stats['broken']}</td>"
            f'<td><a href="{h(rel)}">Abrir semestre 1 completo</a></td>'
            "</tr>"
        )
    body = (
        '<section class="page">'
        "<h1>Primeros semestres completos</h1>"
        '<p class="subtitle">Indice de revision para los cinco manuales. Todos incluyen historia, teoria, practica, ejercicios, material extra, lecturas, referencias y visuales inyectados por ID.</p>'
        "<table><tr><th>Manual</th><th>Titulo</th><th>Paginas</th><th>Imagenes</th><th>Links</th><th>Imagenes rotas</th><th>Archivo</th></tr>"
        + "".join(rows)
        + "</table>"
        '<div class="box question-box"><h3>Control de imagen</h3>'
        "<p>Si una imagen no corresponde al contenido inmediato, corregir el prompt o mover el visual antes de convertir a PDF.</p></div>"
        '<div class="footer"><span>Serie Albatros</span><span>Semestres 1 completos</span></div>'
        "</section>"
    )
    html = (
        "<!doctype html>\n<html lang=\"es\">\n<head>\n"
        "  <meta charset=\"utf-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "  <title>Primeros semestres completos</title>\n"
        "  <link rel=\"stylesheet\" href=\"primer-manual.css\">\n"
        "</head>\n<body>\n"
        f"{body}\n"
        "</body>\n</html>\n"
    )
    out = MANUALES / "semestres-1-index.html"
    out.write_text(html, encoding="utf-8", newline="\n")
    return out


def write_report(results: dict[int, tuple[Path, dict[str, int]]], index: Path) -> Path:
    DOCS.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Reporte de primeros semestres completos",
        "",
        "Reglas aplicadas:",
        "- Hoja carta mediante `.page` y `@page size: letter`.",
        "- Imagenes sin marco ni tarjeta, usando la regla corregida de `primer-manual.css`.",
        "- Visuales vinculados por ID estable y descripcion del prompt.",
        "- Banco de 16 ejercicios por unidad, organizado a 4 ejercicios por pagina.",
        "- Anexos con portadas trimestrales, material extra, lecturas, links, glosario y evaluacion.",
        "",
        "| Manual | Archivo | Paginas | Imagenes | Links | Imagenes rotas |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for manual, (path, stats) in results.items():
        rel = path.relative_to(ROOT).as_posix()
        lines.append(
            f"| M{manual} | `{rel}` | {stats['pages']} | {stats['images']} | {stats['links']} | {stats['broken']} |"
        )
    lines.extend(
        [
            "",
            f"Indice HTML: `{index.relative_to(ROOT).as_posix()}`",
            "",
            "Pendiente recomendado:",
            "- Revision editorial fina por docente antes de exportar a PDF.",
            "- Reemplazar cualquier visual que el docente considere insuficiente aunque no este roto.",
        ]
    )
    out = DOCS / "REPORTE_SEMESTRES_1_COMPLETOS.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return out


def u(
    id_: str,
    title: str,
    case: str,
    history_short: str,
    history: str,
    analogy: str,
    questions: list[str],
    theory: str,
    formulas: list[tuple[str, str, str]],
    product: str,
    data: str,
    keywords: list[str],
) -> dict[str, object]:
    return {
        "id": id_,
        "title": title,
        "case": case,
        "history_short": history_short,
        "history": history,
        "analogy": analogy,
        "questions": questions,
        "theory": theory,
        "formulas": [{"expr": a, "meaning": b, "vars": c} for a, b, c in formulas],
        "product": product,
        "data": data,
        "keywords": keywords,
    }


DATA: dict[int, dict[str, object]] = {
    1: {
        "title": "Quimica Albatros",
        "subtitle": "Materia, agua y aire para resolver el caso del bebedero escolar",
        "audience": "Bachillerato y aspirantes a ingenieria",
        "case": "Agua escolar saludable",
        "story": "El bebedero del patio parece normal, pero el equipo debe comprobar si la muestra es confiable, que particulas contiene, como se comporta el agua y que relacion tiene el aire del entorno.",
        "readings": [
            "Historia de la medicion quimica: de Lavoisier al laboratorio escolar.",
            "La tabla periodica como mapa de propiedades, no como lista para memorizar.",
            "Agua potable, pH, dureza y criterios de seguridad en escuela.",
            "Aire, combustion y lluvia acida en entornos urbanos.",
        ],
        "links": [
            ("IUPAC Periodic Table", "https://iupac.org/what-we-do/periodic-table-of-elements/"),
            ("PhET Chemistry", "https://phet.colorado.edu/es/simulations/filter?subjects=chemistry"),
            ("NIST Chemistry WebBook", "https://webbook.nist.gov/chemistry/"),
            ("PubChem", "https://pubchem.ncbi.nlm.nih.gov/"),
        ],
        "glossary": [
            ("mol", "cantidad de sustancia relacionada con 6.022 x 10^23 entidades"),
            ("pH", "medida logaritmica de acidez"),
            ("ion", "atomo o grupo con carga electrica"),
            ("mezcla", "sistema con mas de una sustancia"),
            ("redox", "proceso con transferencia de electrones"),
        ],
        "units": [
            u(
                "u00",
                "Lenguaje del Quimico",
                "Que tan confiable es tu primera muestra de agua del bebedero?",
                "La primera muestra decide si el diagnostico sirve.",
                "La quimica moderna nacio cuando medir dejo de ser una intuicion y se convirtio en una practica compartida. En el caso del bebedero, la muestra solo vale si se sabe cuanto se midio, con que unidad y con que margen de error.",
                "Medir es como poner subtitulos a la realidad: sin unidades, todos ven la escena pero nadie entiende el mismo mensaje.",
                ["Que dato hace confiable una muestra?", "Como se reconoce un error de medicion?", "Por que el SI evita confusiones?", "Cuando un resultado parece preciso pero no exacto?"],
                "El lenguaje quimico ordena observaciones con unidades, notacion cientifica, cifras significativas e incertidumbre. Antes de discutir sustancias, hay que saber si los datos son comparables.",
                [
                    ("rho = m / V", "calcular densidad", "rho: densidad en g/mL o kg/m3; m: masa en g o kg; V: volumen en mL, L o m3"),
                    ("error % = |valor aceptado - valor medido| / valor aceptado x 100", "estimar desviacion", "error % sin unidad; valores en la misma unidad"),
                    ("valor nuevo = valor inicial x factor de conversion", "convertir unidades", "factor de conversion equivalente a 1; unidades canceladas"),
                ],
                "Bitacora de muestreo con unidades, incertidumbre y conclusion inicial",
                "volumen de muestra, masa del recipiente, temperatura, hora, etiqueta y precision del instrumento",
                ["Sistema Internacional", "cifras significativas", "exactitud", "precision", "incertidumbre", "notacion cientifica"],
            ),
            u(
                "u01",
                "Temas Basicos de la Materia",
                "Que particulas e iones forman el agua del bebedero?",
                "La muestra visible esconde una estructura atomica.",
                "La historia de los modelos atomicos muestra que cada explicacion mejoro cuando pudo explicar algo que la anterior no resolvia. La muestra de agua exige pasar de lo visible a lo atomico: mezclas, iones, enlaces y cantidad de sustancia.",
                "Una muestra es como una orquesta: el sonido final depende de instrumentos que no siempre se ven por separado.",
                ["Que puede estar disuelto aunque el agua se vea clara?", "Como se diferencia sustancia pura y mezcla?", "Por que la tabla periodica predice enlaces?", "Como conectan gramos, moles y particulas?"],
                "La materia se clasifica por composicion, se interpreta con modelos atomicos y se calcula con mol. La tabla periodica funciona como mapa de tendencias para anticipar enlace, reactividad y formula.",
                [
                    ("A = Z + N", "relacionar numero masico", "A: protones + neutrones; Z: protones; N: neutrones"),
                    ("n = m / M", "convertir masa a moles", "n: mol; m: g; M: g/mol"),
                    ("N = n x N_A", "convertir moles a particulas", "N: particulas; n: mol; N_A = 6.022 x 10^23 mol^-1"),
                ],
                "Clasificacion de la muestra y tabla de posibles iones",
                "masa de sales disueltas, formula, masa molar, numero de particulas y tipo de enlace",
                ["sustancia", "mezcla", "atomo", "isotopo", "configuracion electronica", "tabla periodica", "enlace", "mol"],
            ),
            u(
                "u02",
                "Agua",
                "Analisis fisico-quimico del bebedero: pH, dureza y contaminantes",
                "El agua se estudia como molecula, solvente y sistema medible.",
                "El agua ha sido el laboratorio natural de la quimica: disuelve, transporta, reacciona y revela errores de manejo. En la escuela, una muestra de agua permite conectar estructura molecular con pH, soluciones y tratamiento.",
                "El agua es como un taxi molecular: transporta iones, energia y contaminantes segun sus propiedades.",
                ["Por que el agua disuelve sales?", "Que indica el pH?", "Cuando una solucion esta diluida?", "Que tratamiento tiene sentido con los datos?"],
                "La polaridad del agua y los puentes de hidrogeno explican propiedades fisicas. Las soluciones permiten calcular concentracion, dilucion y pH para decidir si una muestra requiere tratamiento.",
                [
                    ("pH = -log[H+]", "medir acidez", "[H+]: mol/L; pH sin unidad"),
                    ("M = n / V", "calcular molaridad", "M: mol/L; n: mol; V: L"),
                    ("M1 V1 = M2 V2", "resolver diluciones", "M en mol/L; V en L o mL, misma unidad en ambos lados"),
                    ("ppm = mg / L", "estimar concentracion baja en agua", "mg de soluto por litro de solucion"),
                ],
                "Reporte de calidad de agua con pH, concentracion y accion propuesta",
                "pH medido, volumen de muestra, masa de soluto, lectura TDS, temperatura y observaciones",
                ["polaridad", "puente de hidrogeno", "pH", "molaridad", "dilucion", "contaminante", "tratamiento"],
            ),
            u(
                "u03",
                "Aire",
                "El aire del comedor sobre la cisterna: hay riesgo de lluvia acida?",
                "El entorno del agua tambien cambia la quimica.",
                "El estudio del aire conecta combustion, oxidos, ciclos y contaminacion. La cisterna no esta aislada: gases del entorno pueden reaccionar y cambiar el equilibrio quimico del agua.",
                "El aire es como una mezcla de visitantes invisibles: algunos pasan sin reaccionar y otros alteran todo el sistema.",
                ["Que gases componen el aire?", "Como se forma un oxido?", "Que relacion hay entre combustion y CO2?", "Como se explica la lluvia acida?"],
                "El aire es una mezcla de gases con porcentajes definidos. Las reacciones de oxigeno, redox y combustion permiten explicar contaminantes, smog y lluvia acida.",
                [
                    ("PV = nRT", "relacionar gases ideales", "P: atm o Pa; V: L o m3; n: mol; R segun unidades; T: K"),
                    ("% componente = parte / total x 100", "calcular composicion", "parte y total en la misma magnitud"),
                    ("CxHy + O2 -> CO2 + H2O", "representar combustion", "balancear atomos de C, H y O"),
                ],
                "Diagnostico de aire y propuesta de mitigacion para proteger el agua",
                "porcentaje de gases, temperatura, fuentes de combustion, pH de lluvia simulada y observaciones",
                ["mezcla gaseosa", "combustion", "oxido", "redox", "ciclo biogeoquimico", "smog", "lluvia acida"],
            ),
        ],
    },
    2: {
        "title": "Fisica Albatros",
        "subtitle": "Mecanica, termodinamica y ondas desde el coche F1 escolar",
        "audience": "Bachillerato y aspirantes a ingenieria",
        "case": "Equipo F1 Albatros",
        "story": "El equipo escolar construye un coche F1 de competencia. Cada unidad agrega una medicion fisica para mejorar el diseno, reducir perdidas y defender decisiones con datos.",
        "readings": [
            "De Galileo a Newton: movimiento medido, no solo observado.",
            "Energia y trabajo en maquinas escolares.",
            "Calor, gases y gestion termica en dispositivos pequenos.",
            "Ondas, sonido y vibracion en prototipos.",
        ],
        "links": [
            ("PhET Physics", "https://phet.colorado.edu/es/simulations/filter?subjects=physics"),
            ("NASA STEM", "https://www.nasa.gov/stem/"),
            ("NIST Constants", "https://physics.nist.gov/cuu/Constants/"),
            ("Khan Academy Physics", "https://www.khanacademy.org/science/physics"),
        ],
        "glossary": [
            ("velocidad", "cambio de posicion por unidad de tiempo"),
            ("fuerza", "interaccion que cambia movimiento o equilibrio"),
            ("energia", "capacidad de producir cambio"),
            ("temperatura", "medida relacionada con energia cinetica promedio"),
            ("onda", "perturbacion que transporta energia"),
        ],
        "units": [
            u("u01", "Cinematica", "Telemetria del coche: posicion, velocidad y aceleracion", "El coche solo mejora si primero se mide su movimiento.", "La fisica del movimiento comenzo cuando se pudieron registrar posiciones en el tiempo. En la pista escolar, cada marca permite reconstruir velocidad y aceleracion.", "La telemetria es como una bitacora del viaje: no empuja el coche, pero revela que paso.", ["Donde empieza el sistema de referencia?", "Que diferencia hay entre distancia y desplazamiento?", "Cuando la velocidad es constante?", "Que grafica muestra aceleracion?"], "La cinematica describe movimiento sin preguntar todavia por sus causas. Usa posicion, tiempo, velocidad y aceleracion para comparar trayectorias.", [("v = Delta x / Delta t", "velocidad media", "v: m/s; Delta x: m; Delta t: s"), ("a = Delta v / Delta t", "aceleracion media", "a: m/s2; Delta v: m/s; Delta t: s"), ("x = x0 + v0 t + 1/2 a t^2", "posicion con aceleracion constante", "x y x0: m; v0: m/s; t: s; a: m/s2")], "Reporte de telemetria con graficas x-t y v-t", "posiciones cada 0.5 s, tiempo total, distancia de pista y velocidad estimada", ["referencia", "posicion", "desplazamiento", "velocidad", "aceleracion", "grafica"]),
            u("u02", "Fuerzas, Newton y Gravitacion", "Fuerzas sobre el chasis y motor de CO2", "El movimiento cambia cuando se identifican fuerzas.", "Newton unifico observaciones terrestres y celestes con leyes que permiten calcular interacciones. En el coche, masa, empuje, friccion y peso explican el desempeno.", "Un diagrama de cuerpo libre es como separar las voces de una discusion: cada fuerza habla en una direccion.", ["Que fuerza empuja el coche?", "Que fuerza lo frena?", "Por que masa y peso no son lo mismo?", "Cuando hay equilibrio?"], "Las leyes de Newton conectan fuerza neta con aceleracion. La gravedad, la friccion y la torca permiten explicar movimiento lineal y rotacional.", [("F = m a", "segunda ley de Newton", "F: N; m: kg; a: m/s2"), ("W = m g", "peso", "W: N; m: kg; g: 9.8 m/s2"), ("F_g = G m1 m2 / r^2", "gravitacion universal", "G: N m2/kg2; masas en kg; r en m"), ("tau = r F sin(theta)", "torca", "tau: N m; r: m; F: N")], "Diagrama de fuerzas y recomendacion de diseno", "masa del coche, empuje estimado, friccion, angulo de pieza y radio de giro", ["fuerza", "masa", "peso", "inercia", "friccion", "torca", "gravedad"]),
            u("u03", "Trabajo y Energia", "Cuanta energia pierde el coche por friccion?", "La velocidad final depende de energia transferida y perdida.", "El concepto de energia permitio estudiar maquinas sin seguir cada fuerza por separado. En la pista, el reto es distinguir energia util, energia almacenada y energia perdida.", "La energia es como presupuesto: puedes gastarla en acelerar, elevar, deformar o perderla por friccion.", ["Que cuenta como trabajo mecanico?", "Donde se almacena energia?", "Como aparece la potencia?", "Que evidencia muestra perdida?"], "Trabajo, energia cinetica, energia potencial y conservacion permiten estimar desempeno y perdidas.", [("W = F d cos(theta)", "trabajo mecanico", "W: J; F: N; d: m; theta: grados"), ("K = 1/2 m v^2", "energia cinetica", "K: J; m: kg; v: m/s"), ("U = m g h", "energia potencial gravitacional", "U: J; m: kg; g: m/s2; h: m"), ("P = W / t", "potencia", "P: W; W: J; t: s")], "Balance de energia del coche y plan para reducir perdidas", "masa, velocidad final, distancia, fuerza de friccion y tiempo de recorrido", ["trabajo", "energia cinetica", "energia potencial", "potencia", "conservacion", "friccion"]),
            u("u04", "Termodinamica", "Calor del motor y gestion termica del coche", "El prototipo tambien intercambia energia como calor.", "La termodinamica nacio de maquinas que convertian calor en trabajo. Aunque el coche escolar sea pequeno, temperatura, expansion y gases afectan materiales y rendimiento.", "El calor es como una transferencia de energia que siempre deja huella en la temperatura o en el estado del material.", ["Que diferencia hay entre calor y temperatura?", "Por que se dilatan materiales?", "Como se calcula calor absorbido?", "Que limita una maquina termica?"], "La termodinamica estudia calor, temperatura, energia interna, cambios de fase y gases. Permite decidir materiales y condiciones de prueba.", [("Q = m c Delta T", "calor sensible", "Q: J; m: kg o g; c: J/kg K o J/g C; Delta T: K o C"), ("Q = m L", "calor latente", "Q: J; m: kg; L: J/kg"), ("PV = nRT", "gas ideal", "P, V, n, R y T en unidades compatibles; T en K"), ("Delta U = Q - W", "primera ley", "Delta U y Q y W en J")], "Registro termico y propuesta de gestion de calor", "temperatura inicial/final, masa del componente, material, tiempo de exposicion y presion", ["calor", "temperatura", "energia interna", "dilatacion", "gas ideal", "cambio de fase"]),
            u("u05", "Ondas", "Ruido y vibraciones del coche F1", "Las vibraciones cuentan historias del diseno.", "Las ondas permitieron entender sonido, luz y comunicacion. En el coche, vibracion y ruido revelan rozamiento, resonancia y transferencia de energia.", "Una onda es como un mensaje que viaja: no se lleva la cuerda completa, pero transporta informacion y energia.", ["Que parametro cambia el tono?", "Como se mide longitud de onda?", "Por que hay resonancia?", "Que diferencia hay entre reflexion y refraccion?"], "Las ondas se describen con amplitud, periodo, frecuencia, longitud de onda y velocidad. Su comportamiento explica sonido, vibracion e interferencia.", [("v = f lambda", "velocidad de onda", "v: m/s; f: Hz; lambda: m"), ("T = 1 / f", "periodo y frecuencia", "T: s; f: Hz"), ("E proporcional A^2", "energia relativa", "A: amplitud en unidad de la perturbacion")], "Analisis de vibracion y propuesta para reducir ruido", "frecuencia medida, amplitud relativa, longitud de onda estimada y fuente de vibracion", ["onda", "frecuencia", "periodo", "amplitud", "longitud de onda", "resonancia", "sonido"]),
        ],
    },
    3: {
        "title": "Inteligencia Artificial Basica",
        "subtitle": "Alfabetizacion en IA generativa para construir un tutor personal",
        "audience": "Bachillerato y profesionales sin experiencia en IA",
        "case": "Mi tutor IA personal",
        "story": "El estudiante construye un tutor IA por capas: primero entiende la historia de la IA, luego conversa, disena prompts, agrega multimodalidad y aprende a estudiar con fuentes.",
        "readings": ["Turing, Dartmouth y el origen de la pregunta por maquinas inteligentes.", "Modelos fundacionales y lenguaje natural.", "Como evaluar respuestas de IA con evidencias.", "Uso responsable de IA para estudiar."],
        "links": [("NIST AI RMF", "https://www.nist.gov/itl/ai-risk-management-framework"), ("OpenAI Docs", "https://platform.openai.com/docs"), ("Google AI", "https://ai.google/"), ("IBM AI Topics", "https://www.ibm.com/topics/artificial-intelligence")],
        "glossary": [("IA", "sistemas que realizan tareas asociadas a inteligencia humana"), ("modelo", "sistema entrenado para producir predicciones o respuestas"), ("prompt", "instruccion que guia una respuesta de IA"), ("contexto", "informacion que el modelo puede usar en una conversacion"), ("alucinacion", "respuesta plausible pero no verificada")],
        "units": [
            u("u01", "Fundamentos e Historia de la IA", "Que es esa IA que todos usan?", "El tutor empieza entendiendo de donde viene la IA.", "La historia de la IA no es una linea recta: incluye entusiasmo, inviernos, redes neuronales, datos masivos y modelos generativos. Entenderla evita tratar cada herramienta como magia.", "La IA es como un estudiante entrenado con muchos ejemplos: responde patrones, pero necesita criterio externo.", ["Que significa que una maquina 'aprenda'?", "Que cambio con los datos masivos?", "Por que un LLM no es una persona?", "Que puede salir mal si no verificas?"], "La IA combina datos, algoritmos, entrenamiento y evaluacion. La IA generativa produce texto, imagen, audio o codigo a partir de patrones aprendidos.", [("precision = aciertos / total", "evaluar respuestas simples", "aciertos y total son conteos; precision entre 0 y 1"), ("salida = modelo(entrada + contexto)", "modelo conceptual", "entrada: prompt; contexto: datos disponibles; salida: respuesta")], "Linea de tiempo comentada y definicion operativa de IA", "fechas clave, ejemplo de herramienta, tarea, dato usado y riesgo", ["Turing", "Dartmouth", "machine learning", "deep learning", "LLM", "modelo fundacional"]),
            u("u02", "Tu Primer Asistente Conversacional", "Elegir y probar ChatGPT, Claude o Gemini como base del tutor", "El tutor empieza como conversacion, no como automatizacion.", "Los asistentes conversacionales bajaron la barrera de entrada a la IA. Su potencia depende de interfaz, contexto, memoria, limites y forma de pedir resultados.", "Un chat de IA es como entrevistar a un experto rapido: puede ayudar mucho, pero hay que hacer preguntas verificables.", ["Que informacion necesita el asistente?", "Como se reconoce una respuesta debil?", "Que datos no debes compartir?", "Como comparas dos asistentes?"], "Un asistente procesa instrucciones, contexto y restricciones. La calidad depende de claridad, evidencia y revision iterativa.", [("costo = tokens x tarifa", "estimar consumo", "tokens: unidades de texto; tarifa: costo por token o por millon"), ("calidad = claridad + contexto + criterio", "modelo cualitativo", "cada componente se evalua con rubrica de 1 a 4")], "Tabla comparativa de asistentes y primera conversacion util", "tarea, contexto dado, respuesta obtenida, verificacion y mejora de prompt", ["token", "contexto", "memoria", "interfaz", "modelo", "verificacion"]),
            u("u03", "Prompt Engineering Fundamental", "Prompts que si funcionan para el tutor", "El tutor mejora cuando la instruccion deja de ser vaga.", "El prompt engineering no es hablar bonito: es especificar rol, tarea, contexto, formato y criterio. La practica nace de comparar versiones y medir cual responde mejor.", "Un prompt es como una orden de trabajo: si falta formato, plazo o criterio, la salida queda abierta.", ["Que debe incluir un buen prompt?", "Como das ejemplos sin confundir?", "Cuando iterar es mejor que empezar de cero?", "Que antipatron debes evitar?"], "Los prompts efectivos delimitan tarea, audiencia, restricciones, ejemplos y formato de salida. La mejora se logra con iteracion y evaluacion.", [("prompt = rol + tarea + contexto + formato + criterio", "estructura base", "cada componente se escribe en lenguaje claro"), ("puntaje = contenido + forma + evidencia", "rubrica de salida", "cada criterio de 1 a 4 puntos")], "Banco de 20 prompts personales para estudiar", "tema, rol, contexto, formato pedido, respuesta y revision", ["rol", "tarea", "contexto", "formato", "few-shot", "iteracion", "rubrica"]),
            u("u04", "IA Generativa Multimodal", "El tutor cobra voz, imagen y video", "El tutor deja de ser solo texto.", "La IA generativa multimodal permite aprender con imagenes, audio, video y documentos. El reto no es usar muchas herramientas, sino elegir el medio que mejor explica el concepto.", "La multimodalidad es como cambiar de pizarron: a veces texto alcanza, a veces una imagen o voz evita diez parrafos.", ["Cuando conviene una imagen?", "Que debe decir un prompt visual?", "Como verificas audio o video?", "Que riesgo tiene generar contenido falso?"], "Un flujo multimodal define objetivo, medio, entrada, salida y verificacion. La herramienta no sustituye el criterio de verdad.", [("prompt visual = sujeto + estilo + composicion + restricciones", "generar imagen controlada", "cada bloque se describe en texto"), ("duracion = escenas x segundos", "planear video", "escenas: conteo; segundos: s")], "Capsula educativa multimedia del tutor", "objetivo, guion, prompt visual, audio, video corto y criterio de revision", ["imagen", "audio", "video", "prompt visual", "guion", "verificacion"]),
            u("u05", "IA para Estudio e Investigacion", "El tutor estudia un PDF contigo y genera resumenes", "El tutor se vuelve util cuando trabaja con fuentes.", "Estudiar con IA exige separar resumen, explicacion, cita y opinion. Las herramientas de investigacion pueden acelerar lectura, pero la responsabilidad de verificar sigue en el estudiante.", "La IA para investigar es como un asistente de biblioteca: encuentra rutas, pero no reemplaza leer la fuente critica.", ["Que fuente es confiable?", "Como citas una respuesta con IA?", "Que diferencia hay entre resumen y evidencia?", "Como detectas una cita inventada?"], "El estudio con IA combina fuentes, preguntas, mapas, resumenes y verificacion. Cada salida debe apuntar a evidencia revisable.", [("confiabilidad = autoridad + actualidad + evidencia", "evaluar fuente", "cada componente con rubrica de 1 a 4"), ("resumen util = idea central + datos + limite", "estructura de lectura", "texto breve con referencia")], "Notebook de estudio con fuentes, resumen y mapa mental", "PDF, pregunta de estudio, citas, resumen, mapa y autoevaluacion", ["fuente", "cita", "resumen", "mapa mental", "verificacion", "sesgo"]),
        ],
    },
    4: {
        "title": "Inteligencia Artificial Avanzada",
        "subtitle": "Usuario de poder: especificaciones, artifacts, RAG y workflows",
        "audience": "Egresados de IA basica y usuarios intensivos",
        "case": "Asistente Institucional Albatros",
        "story": "La institucion necesita un asistente con instrucciones versionadas, especificaciones claras, artifacts, base de conocimiento y automatizaciones no-code.",
        "readings": ["De prompt simple a sistema versionado.", "Especificaciones como puente entre idea y ejecucion.", "RAG y recuperacion de conocimiento institucional.", "Automatizacion no-code con criterios de seguridad."],
        "links": [("OpenAI Docs", "https://platform.openai.com/docs"), ("Anthropic Docs", "https://docs.anthropic.com/"), ("n8n Docs", "https://docs.n8n.io/"), ("Microsoft Power Automate", "https://learn.microsoft.com/power-automate/"), ("Model Context Protocol", "https://modelcontextprotocol.io/")],
        "glossary": [("prompt chain", "secuencia de prompts conectados"), ("PRD", "documento de requisitos de producto"), ("artifact", "salida editable o interactiva generada con IA"), ("RAG", "generacion aumentada por recuperacion de fuentes"), ("workflow", "flujo automatizado con disparadores y acciones")],
        "units": [
            u("u01", "Prompt Engineering Avanzado", "Sistema de prompts versionados para todo el equipo", "El asistente necesita instrucciones estables.", "Cuando un equipo usa IA, los prompts dejan de ser ocurrencias individuales y se convierten en activos versionados. La historia de la unidad es pasar de improvisar a controlar calidad.", "Un prompt avanzado es como un protocolo de laboratorio: si cambia una linea, cambia el resultado.", ["Que debe versionarse?", "Como delimitas contexto?", "Cuando conviene JSON?", "Como comparas dos prompts?"], "El prompt avanzado usa delimitadores, estructura, ejemplos, salida restringida y evaluacion. La calidad se mide con rubricas y pruebas A/B.", [("score = exactitud + formato + utilidad + seguridad", "evaluar prompt", "cada criterio de 1 a 5"), ("salida = f(instrucciones, contexto, restricciones)", "modelo de control", "componentes escritos y revisables")], "Repositorio de prompts institucionales con rubrica", "prompt base, version, caso de uso, salida esperada y resultado de prueba", ["XML", "delimitador", "meta-prompt", "JSON", "rubrica", "A/B"]),
            u("u02", "Especificaciones de Tareas y Proyectos", "PRD del Asistente Institucional", "La IA ejecuta mejor cuando la tarea esta especificada.", "Muchos errores de IA nacen antes del prompt: objetivo ambiguo, alcance indefinido o criterios invisibles. La especificacion convierte deseo en contrato de trabajo.", "Una especificacion es como un plano: no construye sola, pero evita que todos imaginen edificios distintos.", ["Quien es el usuario?", "Que queda fuera del alcance?", "Como se define terminado?", "Que trade-off aceptas?"], "Una buena especificacion define usuario, problema, alcance, restricciones, criterios de aceptacion y riesgos. Luego se traduce a prompts y tareas.", [("DoD = criterios cumplidos / criterios totales", "medir terminado", "conteos de criterios"), ("alcance = objetivo + limites + entregables", "definir proyecto", "texto verificable")], "PRD completo para una funcion del asistente", "usuario, problema, alcance, restricciones, criterios y riesgos", ["PRD", "scope", "Definition of Done", "trade-off", "criterios", "riesgo"]),
            u("u03", "Artifacts y Canvases", "Dashboard interactivo del Asistente como Artifact", "La salida de IA se vuelve editable e interactiva.", "Artifacts y canvases cambian la relacion con la IA: ya no solo se recibe texto, se itera sobre documentos, codigo, visualizaciones o miniapps.", "Un artifact es como una mesa de trabajo compartida: la respuesta deja de estar cerrada y se puede ajustar.", ["Que tipo de artifact conviene?", "Como pruebas una miniapp?", "Que version se conserva?", "Como compartes sin perder control?"], "El trabajo con artifacts requiere especificar formato, interaccion, estado, revision y versionado. El usuario prueba, comenta y vuelve a iterar.", [("version nueva = version anterior + cambio probado", "control de cambios", "versiones numeradas"), ("bug = resultado esperado - resultado observado", "detectar falla", "descripcion comparativa")], "Dashboard HTML del asistente con checklist de prueba", "objetivo, componentes, prueba, captura y version", ["artifact", "canvas", "HTML", "React", "versionado", "prueba"]),
            u("u04", "Bases de Conocimiento y RAG", "El asistente lee el reglamento institucional", "La IA necesita fuentes antes de responder como institucion.", "RAG surge para que el modelo no dependa solo de memoria general. Recupera fragmentos de documentos y los usa como contexto para responder con trazabilidad.", "RAG es como responder con un archivo abierto al lado: no garantiza verdad, pero obliga a mirar la fuente.", ["Que documento entra a la base?", "Que es un chunk?", "Como se cita una fuente?", "Cuando RAG no conviene?"], "RAG combina documentos, fragmentacion, embeddings, busqueda, contexto y generacion. La calidad depende de fuentes limpias y recuperacion pertinente.", [("similitud coseno = A dot B / (|A| |B|)", "comparar vectores", "A y B: vectores numericos"), ("cobertura = fuentes usadas / fuentes necesarias", "revisar base", "conteos de documentos")], "Prototipo RAG sin codigo para reglamento escolar", "documento fuente, chunks, pregunta, respuesta citada y falla detectada", ["RAG", "embedding", "chunk", "vector", "cita", "fuente"]),
            u("u05", "Workflows e Integraciones No-Code", "El asistente automatiza solicitudes con n8n", "El asistente pasa de responder a operar flujos.", "La automatizacion no-code permite conectar formularios, correos, bases y modelos. El reto es disenar disparadores seguros y acciones revisables.", "Un workflow es como una receta con sensores: si entra un evento, sigue pasos, pero debe saber cuando detenerse.", ["Que evento inicia el flujo?", "Que accion requiere aprobacion?", "Como se registra el error?", "Que dato no debe enviarse a IA?"], "Un workflow define trigger, validacion, accion, salida, log y manejo de excepciones. La IA debe estar limitada por reglas del proceso.", [("SLA = tiempo resuelto / tiempo objetivo", "medir atencion", "tiempos en min u h"), ("riesgo = impacto x probabilidad", "priorizar controles", "escala 1 a 5")], "Workflow no-code para solicitudes estudiantiles", "trigger, pasos, herramienta, aprobacion, log y prueba", ["trigger", "webhook", "API", "n8n", "Make", "Zapier", "log"]),
        ],
    },
    5: {
        "title": "Inteligencia Artificial con Programacion",
        "subtitle": "De Python al primer analisis de datos y modelo clasico",
        "audience": "Estudiantes sin experiencia previa de programacion",
        "case": "Predictor de rendimiento escolar",
        "story": "La coordinacion entrega un dataset anonimizado. El semestre convierte datos escolares en codigo, limpieza, visualizaciones y estadistica para entender relaciones.",
        "readings": ["Python como lenguaje de automatizacion y datos.", "Estructura de tablas y datos limpios.", "Graficas para leer patrones antes de modelar.", "Estadistica descriptiva para decidir con cautela."],
        "links": [("Python Docs", "https://docs.python.org/3/"), ("NumPy Docs", "https://numpy.org/doc/"), ("Pandas Docs", "https://pandas.pydata.org/docs/"), ("Matplotlib Docs", "https://matplotlib.org/stable/contents.html"), ("scikit-learn User Guide", "https://scikit-learn.org/stable/user_guide.html")],
        "glossary": [("variable", "nombre que guarda un valor"), ("DataFrame", "tabla de datos con filas y columnas"), ("grafica", "representacion visual de datos"), ("media", "promedio aritmetico"), ("correlacion", "medida de relacion entre variables")],
        "units": [
            u("u01", "Tu Primer Python para IA", "Cargar la lista de calificaciones desde un CSV", "El predictor empieza leyendo datos sin romperlos.", "Programar para IA empieza con acciones simples: guardar valores, repetir pasos, leer archivos y detectar errores. Python permite convertir una tabla escolar en datos manipulables.", "Python es como una libreta que tambien sabe hacer cuentas: si escribes instrucciones claras, repite el procedimiento sin cansarse.", ["Que es una variable?", "Como se lee un CSV?", "Que error aparece si falta un dato?", "Por que conviene comentar poco y claro?"], "Python usa variables, tipos, condicionales, ciclos, funciones y archivos. Antes de IA, se necesita controlar datos basicos.", [("promedio = suma / n", "calcular media simple", "suma: puntos; n: numero de datos"), ("if condicion: accion", "tomar decision", "condicion booleana; accion indentada"), ("for item in lista", "repetir sobre datos", "item: elemento actual; lista: coleccion")], "Script que carga CSV y reporta resumen basico", "archivo CSV, columnas, filas, valores faltantes y promedio inicial", ["variable", "tipo", "if", "for", "funcion", "CSV", "error"]),
            u("u02", "Datos con NumPy y Pandas", "Limpiar el dataset escolar", "Los datos sucios producen conclusiones sucias.", "La ciencia de datos vive en tablas. NumPy trabaja con arreglos; Pandas organiza columnas, filtros y limpieza. El predictor solo aprende bien si los datos tienen forma confiable.", "Limpiar datos es como preparar ingredientes: antes de cocinar, separas, lavas y revisas que no falte lo esencial.", ["Que columna tiene nulos?", "Que tipo de dato espera cada campo?", "Cuando se elimina un duplicado?", "Como documentas una limpieza?"], "NumPy y Pandas permiten leer, filtrar, agrupar y limpiar datos. Cada transformacion debe poder explicarse.", [("missing rate = nulos / total", "medir faltantes", "nulos y total son conteos"), ("media = sum(x) / n", "resumir columna numerica", "x: valores; n: conteo"), ("df[columna]", "seleccionar columna", "df: DataFrame; columna: nombre")], "Dataset escolar limpio con bitacora de transformaciones", "filas, columnas, nulos, duplicados, tipos y reglas de limpieza", ["array", "Series", "DataFrame", "nulo", "duplicado", "groupby", "filtro"]),
            u("u03", "Visualizacion de Datos", "Visualizar distribucion de calificaciones por materia", "Antes de modelar hay que mirar.", "Las graficas permiten detectar patrones, outliers y errores que una tabla oculta. Visualizar no es decorar: es elegir una forma que responda la pregunta.", "Una grafica es como una ventana: muestra algo, pero tambien decide que queda fuera.", ["Que grafica conviene para comparar materias?", "Que muestra un histograma?", "Que oculta un promedio?", "Como evitas una grafica enganosa?"], "Matplotlib y Seaborn permiten crear lineas, barras, dispersion, histogramas y boxplots. La interpretacion debe decir que muestra y que no muestra.", [("x = variable independiente", "definir eje horizontal", "x en la unidad del dato"), ("y = variable dependiente", "definir eje vertical", "y en la unidad del dato"), ("bins = grupos de valores", "configurar histograma", "bins: conteo de intervalos")], "Dashboard de graficas basicas del dataset", "materia, calificacion, asistencia, horas de estudio y grafica seleccionada", ["eje", "histograma", "boxplot", "scatter", "outlier", "paleta"]),
            u("u04", "Estadistica para Entender Datos", "Correlacionan horas de estudio y calificacion final?", "El modelo necesita criterio estadistico.", "La estadistica descriptiva ayuda a distinguir patron, variacion y casualidad. Antes de entrenar modelos, el equipo debe entender distribucion, dispersion y correlacion.", "La estadistica es como una lupa con escala: acerca los datos, pero tambien muestra cuanto varian.", ["Que diferencia hay entre media y mediana?", "Que mide la desviacion estandar?", "Cuando correlacion no implica causalidad?", "Como detectas outliers?"], "Media, mediana, varianza, desviacion estandar, percentiles y correlacion permiten resumir datos sin perder cautela.", [("media = sum(x) / n", "promedio", "x: valores; n: conteo"), ("varianza = sum((x - media)^2) / n", "dispersion", "misma unidad al cuadrado"), ("r = cov(x,y) / (sigma_x sigma_y)", "correlacion de Pearson", "r sin unidad, entre -1 y 1")], "Analisis estadistico de relacion entre estudio y calificacion", "horas de estudio, calificacion, percentiles, outliers y r de Pearson", ["media", "mediana", "varianza", "desviacion", "percentil", "correlacion", "outlier"]),
        ],
    },
}


def main() -> None:
    results: dict[int, tuple[Path, dict[str, int]]] = {}
    for manual in range(1, 6):
        results[manual] = build_manual(manual, DATA[manual])

    index = make_index(results)
    report = write_report(results, index)

    for manual, (path, stats) in results.items():
        print(
            f"M{manual}: {stats['pages']} paginas, {stats['images']} imagenes, "
            f"{stats['links']} links, {stats['broken']} imagenes rotas -> {path}"
        )
    print(f"Indice: {index}")
    print(f"Reporte: {report}")


if __name__ == "__main__":
    main()
