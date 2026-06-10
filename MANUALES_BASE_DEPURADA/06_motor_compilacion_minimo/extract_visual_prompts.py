"""
Extrae cada ::visual{} de los 5 manuales Albatros y produce:

  assets/prompts-visuales/INDEX.md
  assets/prompts-visuales/inject-map.json
  assets/prompts-visuales/manual-N/sem-X/uXX/<ID>.md     (un archivo por prompt)
  assets/prompts-visuales/manual-N-prompts.md            (consolidado por manual)
  assets/prompts-visuales/manifest.json                  (todos los registros)
  assets/prompts-visuales/anidados-pendientes.md         (los ::visual dentro de bloques)
  assets/visuales/manual-N/uXX/                          (carpetas destino, vacías)
  assets/visuales/README.md                              (convención de nombres)

Los IDs (M{n}-uXX-NN) coinciden con los que asigna build/converter.py al
construir los HTML, así que basta con dejar la imagen final en
  assets/visuales/manual-N/uXX/<ID>.png
para que la próxima compilación la inyecte automáticamente.
"""
from __future__ import annotations
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
MANUALES = ROOT / "manuales"
OUT = ROOT / "assets" / "prompts-visuales"
VIS_DIR = ROOT / "assets" / "visuales"
OUT.mkdir(parents=True, exist_ok=True)
VIS_DIR.mkdir(parents=True, exist_ok=True)

# ---------- IDÉNTICO al converter ----------
BLOCK_RE = re.compile(
    r"^::(?P<tag>[\w-]+)(?P<attrs>\{[^}]*\})?(?:::)?\s*\n"
    r"(?P<body>.*?)"
    r"\n^::/(?P=tag)(?:::)?\s*$",
    re.DOTALL | re.MULTILINE,
)
SELF_CLOSING_RE = re.compile(
    r"^::(?P<tag>visual)(?P<attrs>\{[^}]*\})\s*$",
    re.MULTILINE,
)
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')
ATTR_NUM_RE = re.compile(r"(\w+)=([\d.]+)")

# Misma división que build/converter.py SEMESTER_MAP
SEMESTER_MAP = {
    1: {1: ["u00", "u01", "u02", "u03"],            2: ["u04", "u05", "u06"]},
    2: {1: ["u01", "u02", "u03", "u04", "u05"],     2: ["u06", "u07", "u08", "u09"]},
    3: {1: ["u01", "u02", "u03", "u04", "u05"],     2: ["u06", "u07", "u08", "u09"]},
    4: {1: ["u01", "u02", "u03", "u04", "u05"],     2: ["u06", "u07", "u08", "u09", "u10"]},
    5: {1: ["u01", "u02", "u03", "u04"],            2: ["u05", "u06", "u07", "u08"]},
}


def semestre_de(manual_n: int, unidad: str) -> int | None:
    # Las unidades virtuales del front/back matter de semestre (sem1/sem2)
    if unidad in ("sem1",):
        return 1
    if unidad in ("sem2",):
        return 2
    for sem, units in SEMESTER_MAP.get(manual_n, {}).items():
        if unidad in units:
            return sem
    return None


MANUAL_META = {
    1: {
        "titulo": "Química Albatros",
        "subtitulo": "Materia, Agua, Aire, Alimentos y Energía",
        "case_study": "Agua escolar saludable — bebedero del patio contaminado",
    },
    2: {
        "titulo": "Física Albatros",
        "subtitulo": "Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea",
        "case_study": "Equipo F1 Albatros — diseño y telemetría de un coche escolar",
    },
    3: {
        "titulo": "Inteligencia Artificial Básica",
        "subtitulo": "Alfabetización en IA Generativa",
        "case_study": "Mi tutor IA personal — capa por capa de un asistente educativo",
    },
    4: {
        "titulo": "Inteligencia Artificial Avanzada",
        "subtitulo": "Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza",
        "case_study": "Asistente Institucional Albatros — IA con herramientas reales",
    },
    5: {
        "titulo": "Inteligencia Artificial con Programación",
        "subtitulo": "De Python al primer modelo de Machine Learning y APIs de IA",
        "case_study": "Predictor de rendimiento escolar — pipeline ML completo",
    },
}

_SEM_TITULOS = {"sem1": "Front/Back matter — Semestre 1", "sem2": "Front/Back matter — Semestre 2"}
UNIDAD_TITULOS = {
    1: {"u00": "Lenguaje del Químico", "u01": "Temas Básicos de la Materia",
        "u02": "Agua", "u03": "Aire", "u04": "Alimentos",
        "u05": "Energía y Reacciones Químicas", "u06": "Seguridad Industrial"},
    2: {"u01": "Cinemática (Telemetría)", "u02": "Dinámica (Fuerzas)",
        "u03": "Trabajo y Energía", "u04": "Termodinámica",
        "u05": "Ondas y Sonido", "u06": "Electromagnetismo",
        "u07": "Mecánica de Fluidos", "u08": "Óptica",
        "u09": "Física Contemporánea"},
    3: {"u01": "Fundamentos e Historia de la IA", "u02": "Tu primer chat útil",
        "u03": "Prompts que sí funcionan", "u04": "Voz, imagen y video con IA",
        "u05": "IA que estudia un PDF contigo", "u06": "IA automatiza tu semana",
        "u07": "Tu GPT/Gem propio", "u08": "Producción de contenido educativo",
        "u09": "Ética y publicación responsable"},
    4: {"u01": "Prompts versionados", "u02": "PRD del Asistente Institucional",
        "u03": "Dashboards y Artifacts", "u04": "RAG sobre reglamento",
        "u05": "Automatización (n8n)", "u06": "Agentes con herramientas",
        "u07": "Versión local soberana", "u08": "Conexión vía MCP",
        "u09": "Material educativo certificable",
        "u10": "Implementación, costos y gobernanza"},
    5: {"u01": "Python desde cero con CSV", "u02": "Limpieza con NumPy/Pandas",
        "u03": "Visualización (Matplotlib/Seaborn)",
        "u04": "ML clásico (scikit-learn)", "u05": "Redes neuronales básicas",
        "u06": "APIs de IA", "u07": "Proyecto con explicabilidad",
        "u08": "Publicación y despliegue"},
}

# ---------- Guía visual por tipo ----------
TIPO_GUIA = {
    "ilustracion": "ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando",
    "infografia": "INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes",
    "mapa-mental": "MAPA MENTAL radial: nodo central grande, 4-7 ramas curvas a sub-nodos, cada rama en color sólido distinto dentro de paleta Albatros; hojas con micro-ilustración",
    "cuadro-comparativo": "CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil",
    "linea-tiempo": "LÍNEA DE TIEMPO horizontal con eje cronológico central, hitos como cápsulas con fecha + título + micro-ilustración + frase corta",
    "diagrama-flujo": "DIAGRAMA DE FLUJO: cajas redondeadas conectadas por flechas, rombos para decisiones, azul Albatros para procesos, naranja para decisión, sin cruces",
    "grafica": "GRÁFICA CIENTÍFICA limpia: ejes etiquetados con magnitud+unidad, cuadrícula tenue, una o dos series, leyenda compacta arriba derecha",
    "tabla-grande": "TABLA AMPLIA editorial: encabezados azul sólido con texto blanco, zebra sutil, bordes finos, celdas con dato compacto o ícono",
    "interfaz": "MOCKUP DE INTERFAZ: marco de navegador o ventana de app con barra superior, sidebar opcional, área principal con contenido relevante, UI minimalista",
}
TIPO_DEFAULT_COMP = "Composición editorial educativa con jerarquía visual clara, elementos relevantes al concepto y espacio para etiquetas"

ASPECTO_POR_PAGINAS = {
    "0.25": "cuarto de página · 8.5x2.75 in · landscape ultra-ancho · `--ar 21:9`",
    "0.5": "media página · 8.5x5.5 in · landscape · `--ar 3:2`",
    "0.75": "tres cuartos · 8.5x8.25 in · casi cuadrado · `--ar 1:1`",
    "1": "página completa carta · 8.5x11 in · portrait · `--ar 17:22`",
    "1.5": "página y media · 8.5x16.5 in · `--ar 17:33`",
    "2": "doble página spread · 17x11 in · landscape · `--ar 3:2`",
}


def parse_attrs(raw: str) -> dict:
    attrs = {}
    for m in ATTR_RE.finditer(raw):
        attrs[m.group(1)] = m.group(2)
    for m in ATTR_NUM_RE.finditer(raw):
        attrs.setdefault(m.group(1), m.group(2))
    return attrs


def archivo_rol(name: str) -> str:
    if name.startswith("00-portadilla"):
        return "portadilla"
    if name.startswith("01-mapa-mental"):
        return "mapa mental de unidad"
    if name.startswith("02-caso"):
        return "episodio del case study"
    if name.startswith("10-tema-"):
        return "desarrollo de subtema"
    if name.startswith("80-practica"):
        return "práctica resuelta"
    if name.startswith("81-banco"):
        return "banco de ejercicios"
    if name.startswith("90-actividades"):
        return "catálogo de actividades"
    if name.startswith("92-investigacion"):
        return "apartado de investigación"
    if name.startswith("93-taller"):
        return "taller práctico"
    if name.startswith("95-implementacion"):
        return "proyecto integrador"
    if name.startswith("99-cierre"):
        return "cierre y autoevaluación"
    return "contenido del manual"


def build_super_prompt(meta: dict, unidad: str, unidad_titulo: str, rol: str,
                        tipo: str, descripcion: str, paginas: str | None,
                        nota: str | None) -> str:
    comp = TIPO_GUIA.get(tipo, TIPO_DEFAULT_COMP)
    aspecto = ASPECTO_POR_PAGINAS.get(str(paginas), "según contenido")
    nota_str = f"  \n- **Nota editorial:** {nota}" if nota else ""

    return f"""**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **{meta['titulo']}** — {meta['subtitulo']}
- Unidad: **{unidad.upper()} — {unidad_titulo}**
- Case study: *{meta['case_study']}*
- Rol del archivo: **{rol}**
- Tipo de visual: **{tipo}**
- Ocupación: **{paginas or '?'}** página(s) → {aspecto}

**COMPOSICIÓN REQUERIDA ({tipo}):**
{comp}.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
{descripcion}{nota_str}

**REGLAS DE CALIDAD:**
- Texto en español de México, ortográfica y científicamente correcto (sin texto deformado IA).
- Fórmulas químicas/físicas/matemáticas con subíndices/superíndices correctos (H₂O, CO₂, E=mc², etc.).
- Sin marcas de agua, sin firmas, sin elementos decorativos no pedidos.
- Espacio para que el maquetador añada leyendas posteriores.
- Si es infografía/mapa-mental/tabla: zonas de texto editables (placeholders rectangulares claros).
- Resultado vector-friendly aunque se entregue como PNG @300 dpi.

**NEGATIVOS:**
sin photoreal, sin estilo Pixar, sin anime, sin elementos cursis, sin firma de artista, sin watermark, sin texto basura, sin manos deformes, sin números inventados, sin alfabetos no latinos."""


# ---------- Recorrido idéntico al converter ----------
def unidad_de(path: Path) -> str:
    parent = path.parent.name
    if parent.startswith("u") and parent[1:].isdigit():
        return parent
    if parent.startswith("semestre-"):
        return f"sem{parent.split('-')[-1]}"
    return "intro"


def collect_files(manual_dir: Path) -> list[Path]:
    """Igual que converter pero sin filtro de semestre — agarra TODO.

    Recorre raíz + semestre-1 + semestre-2 + unidades/uXX, en ese orden estable.
    """
    files: list[Path] = []
    for f in sorted(manual_dir.glob("*.md")):
        if f.name != "manifest.md":
            files.append(f)
    for sem in (1, 2):
        sem_dir = manual_dir / f"semestre-{sem}"
        if sem_dir.exists():
            for f in sorted(sem_dir.glob("*.md")):
                if f.name != "README.md":
                    files.append(f)
    unidades = manual_dir / "unidades"
    if unidades.exists():
        for u_dir in sorted(unidades.glob("u*")):
            for f in sorted(u_dir.glob("*.md")):
                files.append(f)
    return files


def main():
    todas = []
    por_manual = defaultdict(list)
    anidados = []   # ::visual dentro de bloques

    for n in (1, 2, 3, 4, 5):
        manual_dir = MANUALES / f"manual-{n}"
        if not manual_dir.exists():
            continue
        contadores: dict[str, int] = defaultdict(int)

        for md in collect_files(manual_dir):
            unidad = unidad_de(md)
            txt = md.read_text(encoding="utf-8", errors="replace")

            # Detecta ::visual{} dentro de bloques (BLOCK_RE primero)
            todos_match = list(re.finditer(r"::visual\{([^}]*)\}", txt))
            sin_bloques = BLOCK_RE.sub("", txt)
            externos_match = list(SELF_CLOSING_RE.finditer(sin_bloques))
            externos_attrs = {m.group("attrs") for m in externos_match}

            # Asignar IDs en orden de SELF_CLOSING_RE (=converter)
            for m in externos_match:
                raw = m.group("attrs").strip("{}")
                attrs = parse_attrs(raw)
                tipo = attrs.get("tipo", "ilustracion")
                desc = attrs.get("descripcion", "").strip()
                if not desc:
                    continue
                paginas = attrs.get("paginas")
                nota = attrs.get("nota")
                contadores[unidad] += 1
                ident = f"M{n}-{unidad}-{contadores[unidad]:02d}"
                # número de línea en archivo original
                linea = txt.count("\n", 0, txt.find(m.group(0))) + 1 if m.group(0) in txt else 1
                rec = {
                    "id": ident,
                    "manual": n,
                    "unidad": unidad,
                    "unidad_titulo": UNIDAD_TITULOS.get(n, {}).get(unidad, _SEM_TITULOS.get(unidad, "")),
                    "semestre": semestre_de(n, unidad),
                    "archivo_rel": str(md.relative_to(ROOT)).replace("\\", "/"),
                    "linea": linea,
                    "rol": archivo_rol(md.name),
                    "tipo": tipo,
                    "paginas": paginas,
                    "nota": nota,
                    "descripcion": desc,
                    "imagen_destino": f"assets/visuales/manual-{n}/{unidad}/{ident}.png",
                    "prompt_archivo": f"assets/prompts-visuales/manual-{n}/sem-{semestre_de(n, unidad) or '?'}/{unidad}/{ident}.md",
                }
                rec["prompt"] = build_super_prompt(
                    MANUAL_META[n], unidad, rec["unidad_titulo"], rec["rol"],
                    tipo, desc, paginas, nota,
                )
                todas.append(rec)
                por_manual[n].append(rec)

            # Visuales anidados (dentro de bloques)
            for m in todos_match:
                if m.group(0).split("::visual")[1] in {a for a in externos_attrs}:
                    continue
                raw = m.group(1).strip("{}")
                attrs = parse_attrs(raw)
                if not attrs.get("descripcion"):
                    continue
                anidados.append({
                    "manual": n,
                    "unidad": unidad,
                    "archivo_rel": str(md.relative_to(ROOT)).replace("\\", "/"),
                    "tipo": attrs.get("tipo", "ilustracion"),
                    "paginas": attrs.get("paginas"),
                    "descripcion": attrs.get("descripcion", ""),
                })

    # ---- escritura ----

    # manifest.json (todos)
    (OUT / "manifest.json").write_text(
        json.dumps(todas, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # inject-map.json (id -> rutas)
    inject_map = {
        r["id"]: {
            "manual": r["manual"],
            "unidad": r["unidad"],
            "semestre": r["semestre"],
            "tipo": r["tipo"],
            "paginas": r["paginas"],
            "archivo_md": r["archivo_rel"],
            "linea_md": r["linea"],
            "imagen_destino": r["imagen_destino"],
            "prompt_archivo": r["prompt_archivo"],
        }
        for r in todas
    }
    (OUT / "inject-map.json").write_text(
        json.dumps(inject_map, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Archivos individuales por prompt
    for r in todas:
        path = ROOT / r["prompt_archivo"]
        path.parent.mkdir(parents=True, exist_ok=True)
        header = f"""---
id: {r['id']}
manual: {r['manual']}
unidad: {r['unidad']}
semestre: {r['semestre']}
tipo: {r['tipo']}
paginas: {r['paginas']}
fuente_md: {r['archivo_rel']}:{r['linea']}
imagen_destino: {r['imagen_destino']}
---

# `{r['id']}` — {r['tipo']} ({r['paginas']} pp)

**Manual {r['manual']} · {r['unidad'].upper()} — {r['unidad_titulo']} · Semestre {r['semestre']}**

Rol del archivo: _{r['rol']}_  ·  Fuente: `{r['archivo_rel']}:{r['linea']}`

## Descripción original del manual

> {r['descripcion']}
"""
        if r["nota"]:
            header += f">\n> _Nota:_ {r['nota']}\n"
        header += f"""
## Prompt visual super-específico

```text
{r['prompt']}
```

## Cómo inyectar

1. Generar la imagen con el prompt de arriba.
2. Guardar el archivo como `{r['imagen_destino']}` (PNG, 300 dpi).
3. Re-correr el build del manual:

   ```
   python build/converter.py manuales/manual-{r['manual']} dist/manual-{r['manual']}.html
   python print_to_pdf.py --manual {r['manual']}
   ```

   El converter detectará la imagen por su ID y la inyectará automáticamente.
"""
        path.write_text(header, encoding="utf-8")

        # Crea carpeta destino vacía
        img_dir = ROOT / "assets" / "visuales" / f"manual-{r['manual']}" / r["unidad"]
        img_dir.mkdir(parents=True, exist_ok=True)

    # Consolidados por manual
    for n in (1, 2, 3, 4, 5):
        meta = MANUAL_META[n]
        regs = por_manual[n]
        lines = [
            f"# Prompts visuales — Manual {n}: {meta['titulo']}",
            "",
            f"_{meta['subtitulo']}_  ·  **Case study:** {meta['case_study']}",
            "",
            f"**Total visuales con ID asignado:** {len(regs)}",
            "",
            "| Semestre | Unidades |",
            "|---|---|",
        ]
        for sem in (1, 2):
            units = SEMESTER_MAP.get(n, {}).get(sem, [])
            lines.append(f"| {sem} | {', '.join(units)} |")
        lines.append("")
        # agrupar
        por_sem_unidad = defaultdict(lambda: defaultdict(list))
        for r in regs:
            por_sem_unidad[r["semestre"]][r["unidad"]].append(r)
        for sem in (1, 2):
            if sem not in por_sem_unidad:
                continue
            lines.append(f"## Semestre {sem}")
            lines.append("")
            for unidad in sorted(por_sem_unidad[sem].keys()):
                titulo = UNIDAD_TITULOS.get(n, {}).get(unidad, "")
                lines.append(f"### {unidad.upper()} — {titulo}")
                lines.append("")
                lines.append("| ID | Tipo | pp | Destino imagen | Prompt |")
                lines.append("|---|---|---:|---|---|")
                for r in por_sem_unidad[sem][unidad]:
                    lines.append(
                        f"| `{r['id']}` | {r['tipo']} | {r['paginas']} | "
                        f"`{r['imagen_destino']}` | [ver]({r['prompt_archivo'].split('assets/prompts-visuales/')[-1]}) |"
                    )
                lines.append("")
        (OUT / f"manual-{n}-prompts.md").write_text("\n".join(lines), encoding="utf-8")

    # Anidados pendientes
    if anidados:
        lines = [
            "# Visuales anidados pendientes",
            "",
            "Estos `::visual{}` están **dentro** de un bloque (`::albatros{}`, `::implementacion{}`, etc.) y el converter actual no los procesa como `::visual` self-closing — se renderizan como texto crudo dentro del bloque.",
            "",
            "Hasta resolver eso a nivel de converter (procesado recursivo de bloques), estos prompts no tienen ID estable ni inyección automática. Si los necesitas, sácalos del bloque o procésalos manualmente.",
            "",
            f"**Total:** {len(anidados)} visuales anidados.",
            "",
            "| Manual | Unidad | Archivo | Tipo | Descripción (truncada) |",
            "|---|---|---|---|---|",
        ]
        for a in anidados:
            desc = a["descripcion"][:140].replace("|", "·").replace("\n", " ")
            lines.append(
                f"| {a['manual']} | {a['unidad']} | `{a['archivo_rel']}` | {a['tipo']} | {desc}... |"
            )
        (OUT / "anidados-pendientes.md").write_text("\n".join(lines), encoding="utf-8")

    # README de assets/visuales/
    (VIS_DIR / "README.md").write_text(f"""# `assets/visuales/`

Carpeta destino para las imágenes de los manuales Albatros.

## Convención de nombres

```
assets/visuales/manual-{{N}}/u{{XX}}/M{{N}}-u{{XX}}-{{NN}}.png
```

- **N** = número de manual (1..5)
- **XX** = unidad con dos dígitos (00, 01, ... 10)
- **NN** = ordinal del visual dentro de la unidad (01, 02, ...)

Cada `M{{N}}-u{{XX}}-{{NN}}` corresponde a un `::visual{{}}` del .md fuente.
El mapeo exacto está en `assets/prompts-visuales/inject-map.json`.

## Formatos aceptados (en este orden)

`.png` > `.webp` > `.jpg` > `.jpeg` > `.svg`

## Inyección automática

`build/converter.py` busca la imagen cuando construye el HTML. Si existe,
inyecta `<img src="...">` con el atributo `id="M{{N}}-u{{XX}}-{{NN}}"` en
el `<figure>` correspondiente. Si no existe, deja el placeholder generado
(SVG simbólico).

Para regenerar:

```
python build/converter.py manuales/manual-1 dist/manual-1.html
python print_to_pdf.py --manual 1
```

## Imágenes pendientes

Total de IDs asignados a través de los 5 manuales: ver
`assets/prompts-visuales/INDEX.md`.
""", encoding="utf-8")

    # INDEX maestro
    tipo_cnt = defaultdict(int)
    for r in todas:
        tipo_cnt[r["tipo"]] += 1
    idx_lines = [
        "# Índice maestro — Prompts visuales de los manuales Albatros",
        "",
        "Generado por `extract_visual_prompts.py`. Re-correr si cambian los .md fuente.",
        "",
        f"**Total visuales con ID:** {len(todas)}  ·  **Anidados (pendientes):** {len(anidados)}",
        "",
        "## Conteo por manual y semestre",
        "",
        "| Manual | Título | Sem 1 | Sem 2 | Total |",
        "|---:|---|---:|---:|---:|",
    ]
    for n in (1, 2, 3, 4, 5):
        s1 = sum(1 for r in por_manual[n] if r["semestre"] == 1)
        s2 = sum(1 for r in por_manual[n] if r["semestre"] == 2)
        idx_lines.append(f"| M{n} | {MANUAL_META[n]['titulo']} | {s1} | {s2} | {s1 + s2} |")
    idx_lines.append("")
    idx_lines.append("## Conteo por tipo")
    idx_lines.append("")
    idx_lines.append("| Tipo | Cantidad |")
    idx_lines.append("|---|---:|")
    for t, c in sorted(tipo_cnt.items(), key=lambda x: -x[1]):
        idx_lines.append(f"| `{t}` | {c} |")
    idx_lines.append("")
    idx_lines.append("## Archivos")
    idx_lines.append("")
    for n in (1, 2, 3, 4, 5):
        idx_lines.append(f"- [Manual {n}](manual-{n}-prompts.md) — consolidado")
    idx_lines.append("- [`inject-map.json`](inject-map.json) — ID → metadatos (para herramientas)")
    idx_lines.append("- [`manifest.json`](manifest.json) — registros completos con prompts")
    if anidados:
        idx_lines.append("- [`anidados-pendientes.md`](anidados-pendientes.md) — visuales dentro de bloques (sin ID estable)")
    idx_lines.append("")
    idx_lines.append("## Workflow")
    idx_lines.append("")
    idx_lines.append("1. Abrir un archivo `manual-N/sem-X/uXX/<ID>.md` y copiar su prompt.")
    idx_lines.append("2. Generar la imagen con cualquier motor (Midjourney v6+, DALL·E 3, SD XL, Sora, Flux).")
    idx_lines.append("3. Guardar como `assets/visuales/manual-N/uXX/<ID>.png`.")
    idx_lines.append("4. Re-build: `python build/converter.py manuales/manual-N dist/manual-N.html` y `python print_to_pdf.py --manual N`.")
    idx_lines.append("5. El converter inyectará la imagen automáticamente por ID.")
    idx_lines.append("")
    (OUT / "INDEX.md").write_text("\n".join(idx_lines), encoding="utf-8")

    # Reporte
    print(f"OK — {len(todas)} prompts con ID estable")
    print(f"     {len(anidados)} visuales anidados (sin ID, ver anidados-pendientes.md)")
    print(f"  -> {OUT}")
    for n in (1, 2, 3, 4, 5):
        s1 = sum(1 for r in por_manual[n] if r["semestre"] == 1)
        s2 = sum(1 for r in por_manual[n] if r["semestre"] == 2)
        print(f"  M{n}: sem1={s1}  sem2={s2}  total={s1+s2}")


if __name__ == "__main__":
    main()
