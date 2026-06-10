"""
Genera, para cada manual, las dos carpetas:
  manuales/manual-N/semestre-1/
  manuales/manual-N/semestre-2/

con los archivos de front-matter y cierre por semestre:
  00-portada.md
  01-carta-estudiante.md
  02-carta-docente.md
  03-mapa-contenidos.md
  04-hilo-conductor.md
  05-competencias.md
  06-diagnostica.md
  90-cierre-semestre.md
  91-material-extra.md
  92-glosario-semestre.md
  93-bibliografia-semestre.md
  94-indice-analitico.md

Cada archivo cumple manual-md-author (frontmatter + bloques semánticos) y
manual-spec (carta, marca, hilo conductor). Los ::visual{} llevan descripcion
≥ 50 chars y tipo válido del catálogo.

Idempotente: si el archivo ya existe NO lo sobrescribe (a menos que se pase
--force).
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).parent
MANUALES_DIR = ROOT / "manuales"

# Metadatos por manual
META = {
    1: {
        "titulo": "Química Albatros",
        "subtitulo": "Materia, Agua, Aire, Alimentos y Energía",
        "case_study": "Agua escolar saludable",
        "premisa": "El bebedero del patio se llenó de algas y varios alumnos se enfermaron. La comunidad escolar te encarga diagnosticar, proponer y probar una solución química. Cada unidad te da una herramienta nueva.",
        "publico": "Estudiantes de bachillerato — aspirantes a ingeniería universitaria",
        "tema_color": "azul Albatros + matraces verdes",
        "unidades": ["u00","u01","u02","u03","u04","u05","u06"],
        "titulos_unidad": {
            "u00": "Lenguaje del Químico", "u01": "Temas Básicos de la Materia",
            "u02": "Agua", "u03": "Aire", "u04": "Alimentos",
            "u05": "Energía y Reacciones Químicas", "u06": "Seguridad Industrial"
        },
        "fuentes_curaduria": "ChemLibreTexts · Crash Course Chemistry · SEMARNAT · CONAGUA · IUPAC · Compound Interest · Programas oficiales de bachillerato",
        "competencia_eje": "Aplicar el método científico para investigar fenómenos químicos relevantes para la salud y el ambiente escolar",
    },
    2: {
        "titulo": "Física Albatros",
        "subtitulo": "Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea",
        "case_study": "Equipo F1 Albatros",
        "premisa": "Tu escuela compite en la liga nacional de F1 in Schools. Te encargan el diseño físico, instrumentación y telemetría del coche. Cada unidad te da una nueva herramienta de la física para mejorarlo.",
        "publico": "Estudiantes de bachillerato — aspirantes a ingeniería universitaria",
        "tema_color": "azul Albatros + naranja pista",
        "unidades": ["u01","u02","u03","u04","u05","u06","u07","u08","u09"],
        "titulos_unidad": {
            "u01": "Cinemática", "u02": "Dinámica", "u03": "Trabajo y Energía",
            "u04": "Termodinámica", "u05": "Ondas y Sonido",
            "u06": "Electromagnetismo", "u07": "Mecánica de Fluidos",
            "u08": "Óptica", "u09": "Física Contemporánea"
        },
        "fuentes_curaduria": "NASA · CERN · MIT OCW (8.01) · Khan Academy · PhET · Veritasium · Programas oficiales de bachillerato",
        "competencia_eje": "Modelar el comportamiento físico de un sistema real y validarlo con instrumentación y datos",
    },
    3: {
        "titulo": "Inteligencia Artificial Básica",
        "subtitulo": "Alfabetización en IA Generativa para Estudiantes",
        "case_study": "Mi tutor IA personal",
        "premisa": "A lo largo del manual construyes tu propio asistente IA personal: primero conversas con él, luego le das contexto, lo personalizas, le agregas multimedia, lo conviertes en GPT propio y lo publicas bajo principios éticos. Cada unidad le suma una capa.",
        "publico": "Bachillerato y profesionales sin experiencia previa en IA",
        "tema_color": "azul Albatros + acentos turquesa",
        "unidades": ["u01","u02","u03","u04","u05","u06","u07","u08","u09"],
        "titulos_unidad": {
            "u01": "Fundamentos e Historia de la IA",
            "u02": "Tu primer chat útil",
            "u03": "Prompts que sí funcionan",
            "u04": "Voz, imagen y video con IA",
            "u05": "IA que estudia un PDF contigo",
            "u06": "IA automatiza tu semana",
            "u07": "Tu GPT/Gem propio",
            "u08": "Producción de contenido educativo",
            "u09": "Ética y publicación responsable"
        },
        "fuentes_curaduria": "Anthropic Learn · OpenAI Cookbook · Google AI Studio docs · NotebookLM Help · Lex Fridman · AI Explained",
        "competencia_eje": "Usar IA generativa con criterio, ética y prompts efectivos para producir conocimiento propio",
    },
    4: {
        "titulo": "Inteligencia Artificial Avanzada",
        "subtitulo": "Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza",
        "case_study": "Asistente Institucional Albatros",
        "premisa": "La dirección de tu institución te encarga diseñar un Asistente IA Institucional: gestiona conocimiento interno, automatiza flujos, responde a estudiantes, opera con herramientas reales y respeta políticas de gobernanza. Cada unidad agrega una capa.",
        "publico": "Egresados de Manual 3 · profesionales con uso intensivo de IA",
        "tema_color": "azul Albatros + acentos púrpura institucional",
        "unidades": ["u01","u02","u03","u04","u05","u06","u07","u08","u09","u10"],
        "titulos_unidad": {
            "u01": "Prompts versionados",
            "u02": "PRD del Asistente Institucional",
            "u03": "Dashboards y Artifacts",
            "u04": "RAG sobre reglamento",
            "u05": "Automatización (n8n)",
            "u06": "Agentes con herramientas",
            "u07": "Versión local soberana",
            "u08": "Conexión vía MCP",
            "u09": "Material educativo certificable",
            "u10": "Implementación, costos y gobernanza"
        },
        "fuentes_curaduria": "Anthropic engineering blog · OpenAI platform docs · n8n academy · Ollama docs · MCP spec · GitHub docs",
        "competencia_eje": "Diseñar, implementar y gobernar sistemas IA institucionales con herramientas reales y políticas claras",
    },
    5: {
        "titulo": "Inteligencia Artificial con Programación",
        "subtitulo": "De Python al primer modelo de Machine Learning y APIs de IA",
        "case_study": "Predictor de rendimiento escolar",
        "premisa": "La coordinación académica te entrega un dataset anonimizado con horas de estudio, asistencia, calificaciones previas y resultado final. Tu misión: construir paso a paso un sistema que prediga el rendimiento de un estudiante y lo explique en lenguaje natural.",
        "publico": "Estudiantes con curiosidad técnica · sin experiencia previa de programación",
        "tema_color": "azul Albatros + verde terminal",
        "unidades": ["u01","u02","u03","u04","u05","u06","u07","u08"],
        "titulos_unidad": {
            "u01": "Python desde cero con CSV",
            "u02": "Limpieza con NumPy y Pandas",
            "u03": "Visualización (Matplotlib/Seaborn)",
            "u04": "ML clásico (scikit-learn)",
            "u05": "Redes neuronales básicas",
            "u06": "APIs de IA",
            "u07": "Proyecto con explicabilidad",
            "u08": "Publicación y despliegue"
        },
        "fuentes_curaduria": "Real Python · Pandas docs · scikit-learn user guide · PyTorch tutorials · Hugging Face course",
        "competencia_eje": "Construir, evaluar y publicar un modelo de ML completo con Python, datos reales y APIs de IA",
    },
}

SEMESTER_MAP = {
    1: {1: ["u00","u01","u02","u03"], 2: ["u04","u05","u06"]},
    2: {1: ["u01","u02","u03","u04","u05"], 2: ["u06","u07","u08","u09"]},
    3: {1: ["u01","u02","u03","u04","u05"], 2: ["u06","u07","u08","u09"]},
    4: {1: ["u01","u02","u03","u04","u05"], 2: ["u06","u07","u08","u09","u10"]},
    5: {1: ["u01","u02","u03","u04"], 2: ["u05","u06","u07","u08"]},
}


def render_portada(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    titulos = ", ".join(m["titulos_unidad"][u] for u in units)
    desc_visual = (
        f"Ilustración hero de portada para el Semestre {sem} del Manual {manual_n}: "
        f"{m['titulo']}. Composición editorial vertical con el logo Albatros en la "
        f"esquina superior derecha, título grande del manual, subtítulo, barra cromática "
        f"{m['tema_color']}, y al centro un escenario evocador del case study "
        f"'{m['case_study']}' que conecta visualmente las unidades del semestre "
        f"({titulos}). Tono editorial, sin photoreal, paleta azul Albatros con acento naranja."
    )
    return f"""---
seccion: portada
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 2
---

# {m['titulo']}

## Semestre {sem}

> {m['subtitulo']}

**Case study del manual:** *{m['case_study']}*

**Unidades de este semestre:** {", ".join(u.upper() + " — " + m['titulos_unidad'][u] for u in units)}

::visual{{tipo="ilustracion" descripcion="{desc_visual}" paginas=1 nota="hero de portada del semestre — eje narrativo del case study"}}

---

**Una colección Albatros · Manual {manual_n} de la serie**

*Material educativo para bachillerato y aspirantes a ingeniería universitaria.*

::visual{{tipo="ilustracion" descripcion="Pieza de créditos editoriales: logo Albatros centrado en azul Albatros sobre fondo blanco, debajo el texto 'Grupo Cultural Albatros · Edición Tecno · 2026', y al pie tres líneas finas naranja como ornamento. Composición simple, simétrica, tipografía sans-serif moderna." paginas=0.5 nota="página de créditos institucionales"}}
"""


def render_carta_estudiante(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    return f"""---
seccion: carta-estudiante
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 1
---

# Carta al estudiante

Bienvenido al **Semestre {sem}** del manual *{m['titulo']}*. Lo que tienes en
las manos no es un libro de teoría que vas a leer pasivamente: es un manual de
campo diseñado para que **construyas tu propio aprendizaje** mientras resuelves
un caso real que evolucionará contigo durante todo el manual.

**Tu misión durante este semestre.** {m['premisa']}

Vas a recorrer las unidades **{", ".join(u.upper() for u in units)}** y al final
podrás demostrar que dominas la competencia central:

> *{m['competencia_eje']}.*

::interioriza{{titulo="Cómo aprovechar este manual"}}
1. **Lee con lápiz en mano.** Cada unidad incluye espacios para que escribas.
2. **Haz las pausas.** Los bloques 💭 son obligatorios: sin reflexión no hay aprendizaje.
3. **Resuelve, no solo memorices.** El 60% del manual está pensado para que practiques.
4. **Conecta con el caso.** Cada concepto se aplica al case study; no son temas sueltos.
5. **Cuestiona y verifica.** Las fuentes recomendadas están para que vayas más allá.
::/interioriza

Si en cualquier momento sientes que vas demasiado rápido o lento, vuelve al
**Mapa de Contenidos** y a la **Evaluación Diagnóstica** del inicio: te dan la
brújula del semestre.

Buen viaje. Cuando termines este semestre, tendrás una pieza concreta del caso
resuelto y un cuaderno de evidencias que podrás usar como portafolio.

— *Equipo Albatros*

::visual{{tipo="ilustracion" descripcion="Ilustración cálida de un estudiante mexicano de bachillerato sentado en su escritorio con el manual abierto, lápiz en mano, un vaso de agua o una herramienta del case study a un lado y una luz suave entrando por la ventana. Expresión concentrada y motivada. Estilo editorial outline + duotone, paleta azul Albatros y naranja, sin photoreal." paginas=0.5 nota="ilustración de apoyo a la carta al estudiante"}}
"""


def render_carta_docente(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    return f"""---
seccion: carta-docente
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 1
---

# Carta al docente / facilitador

Estimado docente:

Este semestre del manual *{m['titulo']}* fue construido sobre tres principios
metodológicos que conviene tener presentes para sacarle el máximo provecho:

::concepto{{titulo="Principios metodológicos"}}
1. **Aprendizaje basado en proyectos (ABP).** El case study **"{m['case_study']}"** es el hilo conductor único: cada unidad agrega una herramienta para resolverlo.
2. **60% práctico mínimo.** El manual está balanceado para que la mayor parte del tiempo en clase el estudiante esté haciendo, no solo escuchando.
3. **Evaluación continua.** Cada unidad ofrece evidencias concretas: prácticas resueltas, talleres, bancos de ejercicios, investigaciones y un proyecto integrador.
::/concepto

**Ritmo sugerido del semestre.** {len(units)} unidades × aproximadamente
3 a 4 semanas de clase cada una. Si tienes 16 semanas por semestre, asigna
~2 sesiones a cada **bloque de 4-6 páginas teóricas + pausa para pensar**, y
2 sesiones completas al **taller** y al **proyecto integrador** de cada unidad.

::albatros{{titulo="Cómo usar las Actividades Albatros en clase" tipo="taller" tiempo="por sesión"}}
**Pregunta detonadora para el docente.** ¿En qué momento de la unidad funcionará
mejor cada Actividad Albatros: como apertura, como puente entre conceptos o
como integradora del cierre?

**Recomendación.** Reserva una sesión completa para cada Actividad Albatros;
están diseñadas para 45–60 minutos efectivos de trabajo del estudiante.
Asegúrate de revisar la rúbrica corta antes de iniciar — los criterios están
pensados para que la calificación sea objetiva y replicable.

**Entregable del docente.** Una bitácora donde registres, sesión a sesión,
qué bloques aplicaste, qué actividades funcionaron mejor, y qué ajustes
proponen tus estudiantes. Ese material alimentará la próxima edición.

**Rúbrica para el docente.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Adaptación al grupo | mecánica | parcial | personalizada |
| Cobertura de competencias | < 60 % | 60-80 % | > 80 % |
| Evidencias recolectadas | sueltas | organizadas | portafolio claro |
::/albatros

**Si decides reordenar.** Las unidades de este semestre son secuenciales —
cada una usa lo construido en la anterior. **No** las reordenes a menos que
explícitamente reorganices también los episodios del case study.

Gracias por elegir Albatros para acompañar a tus estudiantes este semestre.

— *Equipo Albatros*

::visual{{tipo="cuadro-comparativo" descripcion="Cuadro comparativo de 3 columnas: 'Enfoque tradicional' vs 'Enfoque Albatros' vs 'Beneficio esperado'. Filas: rol del docente, papel del estudiante, fuente de evidencia, evaluación, ritmo de avance, integración del caso real. Encabezado azul Albatros con texto blanco, zebra sutil en filas." paginas=0.5 nota="ayuda visual para que el docente identifique los cambios metodológicos"}}
"""


def render_mapa_contenidos(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    filas = []
    for u in units:
        t = m["titulos_unidad"].get(u, "")
        filas.append(f"| {u.upper()} | {t} | 3–4 semanas | Episodio del case que toca |")
    tabla = "\n".join(filas)
    desc_visual = (
        f"Infografía vertical tipo mapa visual del semestre {sem} del manual "
        f"{m['titulo']}: en la parte superior, el título del case study "
        f"'{m['case_study']}'. Debajo, una columna de {len(units)} estaciones "
        f"conectadas verticalmente, una por unidad ({', '.join(units)}), cada "
        f"estación con su número, título, ícono temático y la herramienta que "
        f"aporta al caso. Al pie, un entregable de portafolio final del semestre. "
        f"Paleta azul Albatros + naranja en conectores."
    )
    return f"""---
seccion: mapa-contenidos
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 2
---

# Mapa de contenidos — Semestre {sem}

| Unidad | Tema central | Duración sugerida | Aporte al caso |
|---|---|---|---|
{tabla}

::visual{{tipo="infografia" descripcion="{desc_visual}" paginas=1 nota="mapa visual del semestre — pieza central del front matter"}}

## Cómo navegar este semestre

::concepto{{titulo="Estructura repetida en cada unidad"}}
Cada unidad de este semestre sigue la misma estructura para que sepas qué esperar:
1. **Portadilla + Mapa mental** (2 pp)
2. **Caso Albatros — Episodio** (½ pp): cómo evoluciona el case study aquí
3. **Conceptualización** (8–14 pp): bloques de teoría + interiorización + pausas
4. **Práctica resuelta** paso a paso (2 pp)
5. **Banco de ejercicios** con clave de respuestas (4 pp)
6. **Actividades del catálogo** (3–6 pp): variadas, del catálogo de 12 tipos
7. **🎯 Actividad Albatros** (2 pp): reto integrador de mediano alcance
8. **Taller práctico** (2 pp): trabajo colaborativo de 60 minutos
9. **🔎 Apartado de investigación** (1 pp): investigación por medios propios
10. **📚 Fuentes recomendadas** (½ pp): curaduría con al menos 4 medios
11. **🚀 Implementación Albatros** (3–4 pp): proyecto integrador con rúbrica
12. **Cierre y autoevaluación** (1 pp)
::/concepto

::interioriza{{titulo="Tip extra — cómo aprovechar el ritmo"}}
El manual está pensado para que **el 60% del tiempo lo dediques a actividades
prácticas** (resolver, construir, investigar) y solo el 40% a leer y escuchar.
Si en una unidad te encuentras leyendo más que haciendo, **regresa al taller
y al banco de ejercicios** — ahí está el aprendizaje real.
::/interioriza
"""


def render_hilo_conductor(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    episodios = []
    for i, u in enumerate(units, 1):
        t = m["titulos_unidad"].get(u, "")
        episodios.append(f"- **Episodio {u.upper()} — {t}.** Tu intervención en esta unidad le aporta al caso una pieza clave: ver la unidad correspondiente.")
    eps = "\n".join(episodios)
    desc_visual = (
        f"Línea de tiempo horizontal del semestre {sem}: en el extremo izquierdo, "
        f"el problema inicial del case study '{m['case_study']}'; en el centro, "
        f"{len(units)} hitos correspondientes a los episodios de cada unidad "
        f"({', '.join(units)}); en el extremo derecho, el entregable final del "
        f"portafolio del semestre. Cada hito con fecha tentativa (semana N), "
        f"título corto y micro-ilustración temática."
    )
    return f"""---
seccion: hilo-conductor
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 2
---

# Hilo conductor — Semestre {sem}

## El case study en una frase

> **{m['case_study']}** — {m['premisa']}

## Cómo evoluciona durante este semestre

::caso{{episodio="semestre-{sem}"}}
Durante el **Semestre {sem}** del manual *{m['titulo']}* vas a vivir los
siguientes episodios del case, cada uno como pieza de un mismo arco:

{eps}

Al finalizar el semestre tendrás **un portafolio de evidencias** que documenta
tu intervención completa hasta este punto y que te servirá para arrancar el
semestre siguiente con un cierre claro.
::/caso

::visual{{tipo="linea-tiempo" descripcion="{desc_visual}" paginas=1 nota="visión panorámica del hilo conductor del semestre"}}

::pausa{{titulo="💭 Pausa para pensar — antes de iniciar"}}
1. ¿Qué sabes ya sobre el problema central del case study? Escríbelo.
   _____________________________________________________________________
2. ¿Qué crees que vas a aprender en este semestre que te ayudará a resolverlo?
   _____________________________________________________________________
3. ¿Qué herramientas, materiales o personas necesitarás conseguir?
   _____________________________________________________________________
::/pausa
"""


def render_competencias(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    filas = []
    for i, u in enumerate(units, 1):
        t = m["titulos_unidad"].get(u, "")
        filas.append(f"| {manual_n}.{u[1:]}.A | {t} — competencia A | Aplicar | Práctica resuelta + Implementación de la unidad | U{u[1:]}-A |")
        filas.append(f"| {manual_n}.{u[1:]}.B | {t} — competencia B | Analizar | Banco de ejercicios + Taller de la unidad | U{u[1:]}-B |")
    tabla = "\n".join(filas)
    return f"""---
seccion: competencias
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 2
---

# Índice de competencias — Semestre {sem}

## Competencia eje del semestre

> **{m['competencia_eje']}.**

## Mapeo unidad → competencia → evidencia

| ID | Competencia | Verbo Bloom | Evidencia esperada | Reactivo |
|---|---|---|---|---|
{tabla}

::interioriza{{titulo="Cómo se evalúan las competencias"}}
Cada competencia tiene **tres niveles** que vas a ver en las rúbricas:
- **Nivel 1 (Inicial)**: identificas el concepto pero no lo aplicas con autonomía.
- **Nivel 3 (En desarrollo)**: aplicas el concepto con guía; entregable parcial.
- **Nivel 5 (Consolidado)**: aplicas el concepto con autonomía; entregable completo y reusable en otra situación.

El semestre se da por aprobado cuando demuestras **nivel 3 o superior** en al
menos el 80 % de las competencias, evidenciado en tu portafolio.
::/interioriza

::visual{{tipo="cuadro-comparativo" descripcion="Tabla extendida del índice de competencias del semestre con columnas: ID, descripción corta, verbo Bloom, % del manual dedicado, página del primer reactivo, página de la evidencia integradora. Encabezado azul Albatros, zebra sutil, ícono Bloom en la columna del verbo." paginas=1 nota="cuadro maestro para revisión de la coordinación académica"}}
"""


def render_diagnostica(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    return f"""---
seccion: diagnostica
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 4
---

# Evaluación diagnóstica — Semestre {sem}

Antes de iniciar el semestre, responde con tus propias palabras y sin consultar
fuentes. **El objetivo no es calificarte**, sino saber de dónde partes para que
tu profesor pueda adaptar el ritmo.

::act-mcq{{titulo="Parte 1 — Conocimientos previos (8 preguntas de opción múltiple)"}}
1. ¿Qué relación crees que existe entre los temas de este semestre y el case study **"{m['case_study']}"**?
   - [ ] Ninguna, son temas independientes
   - [ ] Algunos temas ayudan, otros no
   - [ ] Todos los temas son herramientas para resolver el caso
   - [ ] No sé qué es el case study

2. ¿Cuántas horas a la semana estás dispuesto a dedicar a este manual fuera de clase?
   - [ ] Menos de 1 hora
   - [ ] 1 a 2 horas
   - [ ] 3 a 5 horas
   - [ ] Más de 5 horas

3. ¿Qué prefieres cuando aprendes algo nuevo?
   - [ ] Leer la teoría primero, luego practicar
   - [ ] Practicar primero, deducir la teoría después
   - [ ] Ver un video o demostración antes de tocar el tema
   - [ ] Que alguien me lo explique en persona

4. ¿Con cuál de estos términos del semestre te sientes más familiar?
   - [ ] {m['titulos_unidad'].get(units[0], 'Tema 1')}
   - [ ] {m['titulos_unidad'].get(units[len(units)//2], 'Tema medio')}
   - [ ] {m['titulos_unidad'].get(units[-1], 'Tema final')}
   - [ ] Ninguno, parto de cero

5. ¿Tienes acceso fluido a internet en casa?
   - [ ] Sí, todo el tiempo
   - [ ] Solo algunas horas al día
   - [ ] Solo en la escuela
   - [ ] No tengo acceso estable

6. ¿Trabajas mejor solo o en equipo?
   - [ ] Solo
   - [ ] En parejas
   - [ ] En equipo de 3–4
   - [ ] Depende del tema

7. ¿Cómo te sientes al iniciar este semestre?
   - [ ] Con miedo, no sé si voy a entender
   - [ ] Curioso, quiero ver qué pasa
   - [ ] Motivado, ya sé un poco del tema
   - [ ] Aburrido, lo estoy llevando porque toca

8. ¿Cuál entregable te emociona más imaginar?
   - [ ] El proyecto integrador del case study
   - [ ] El banco de ejercicios resueltos
   - [ ] El taller práctico
   - [ ] El examen integrador
::/act-mcq

::act-fill{{titulo="Parte 2 — Anclaje del case study (rellena con tus palabras)"}}
- Lo que entiendo del case study **{m['case_study']}** es: __________________________________________________________________
- Lo que NO entiendo todavía es: __________________________________________________________________
- Algo parecido que ya he vivido en mi escuela o comunidad es: __________________________________________________________________
- Lo que espero aprender este semestre es: __________________________________________________________________
::/act-fill

::act-case{{titulo="Parte 3 — Pregunta abierta detonadora" lineas=8}}
Imagina que **al final del semestre** tienes que explicarle a un familiar de
qué se trató este manual. En máximo 8 líneas, describe el aprendizaje que te
gustaría poder demostrar.
::/act-case

::visual{{tipo="grafica" descripcion="Gráfica de radar de 5 ejes para autoevaluación inicial: 1) Familiaridad con el tema, 2) Confianza para practicar, 3) Acceso a recursos, 4) Motivación inicial, 5) Tiempo disponible. Cada eje numerado de 0 a 5. El estudiante marcará con un punto su nivel actual y al final del semestre se compara con una segunda lectura." paginas=0.5 nota="gráfico para que el estudiante mida su evolución durante el semestre"}}
"""


def render_cierre_semestre(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    return f"""---
seccion: cierre-semestre
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 3
---

# Cierre del Semestre {sem}

Llegaste al final del semestre. Antes de cerrar el cuaderno, dedica unas
páginas a consolidar el aprendizaje y a preparar el siguiente paso.

::implementacion{{titulo="🚀 Proyecto Integrador de Semestre — Entregable del portafolio"}}
**Objetivo.** Reúne en un solo documento (físico o digital) todas las
evidencias del case study **{m['case_study']}** producidas durante este
semestre, agrega una reflexión final y prepara la presentación.

**Estructura del portafolio (mín. 10 piezas).**
1. Mapa mental general del semestre (1 pp).
2. Una evidencia por unidad: la mejor pieza que produjiste (típicamente el
   entregable de la Implementación Albatros de la unidad).
3. Línea de tiempo personal: cómo evolucionó tu entendimiento del case study.
4. Tres preguntas que te quedan abiertas y por qué.
5. Plan para el siguiente semestre.

**Materiales.** Carpeta o portafolio digital (Google Drive, Notion, Canva).
Plantilla mínima: portada con tu nombre + manual + semestre, índice clicable,
una sección por unidad, cierre.

**Pasos sugeridos (4 sesiones).**
1. Sesión 1 — Reunir evidencias por unidad.
2. Sesión 2 — Diseñar la línea de tiempo y la reflexión.
3. Sesión 3 — Maquetar el portafolio.
4. Sesión 4 — Presentación de 5 minutos ante el grupo.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Completitud | < 60 % piezas | 60–80 % piezas | Todas las piezas y más |
| Calidad de la evidencia | sin curar | curada parcial | curada y comentada |
| Reflexión personal | superficial | concreta | profunda y crítica |
| Conexión con el case | suelta | clara | imprescindible |
| Presentación oral | desorganizada | clara | persuasiva |
::/implementacion

::pausa{{titulo="💭 Pausa final — Autoevaluación del semestre"}}
1. ¿Qué fue lo más difícil de este semestre y cómo lo resolviste?
   _____________________________________________________________________
2. ¿Qué actividad disfrutaste más y por qué?
   _____________________________________________________________________
3. Si pudieras cambiar una cosa del semestre, ¿qué sería?
   _____________________________________________________________________
4. ¿Qué le dirías a un compañero que está a punto de iniciarlo?
   _____________________________________________________________________
::/pausa

::visual{{tipo="ilustracion" descripcion="Ilustración de cierre cálida: un estudiante revisando su portafolio terminado con varias hojas y evidencias del case study sobre la mesa, mirada satisfecha, fondo de salón de clases o espacio personal. Al pie de la ilustración, un cohete pequeño apuntando hacia arriba (símbolo del siguiente semestre). Paleta azul Albatros + naranja, outline + duotone." paginas=1 nota="pieza emocional de cierre del semestre"}}

## Hacia el Semestre {sem + 1 if sem == 1 else "siguiente del Manual " + str(manual_n + 1)}

::interioriza{{titulo="Lo que viene"}}
{"El próximo semestre vas a profundizar en las unidades restantes de este manual y a llevar el case study a su resolución final. Lo que construiste aquí es la base; ahí lo aplicarás." if sem == 1 else "Cerraste el manual. El portafolio que produjiste te servirá como punto de partida para el siguiente manual de la serie Albatros, donde retomarás competencias y elevarás el reto."}

**Antes de pasar a lo siguiente.** Comparte tu portafolio con un compañero
diferente y pídele una retroalimentación específica:
- Lo que está claro: ___________________________
- Lo que se puede mejorar: ___________________________
- Lo que más le gustó: ___________________________
::/interioriza
"""


def render_material_extra(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    return f"""---
seccion: material-extra
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 4
---

# Material extra del Semestre {sem}

Recursos opcionales para profundizar, ampliar o reforzar. No son obligatorios
para aprobar, pero **suben tu nivel** y son ideales si quieres llevar el
portafolio del semestre a un nivel sobresaliente.

## Tips extra del autor

::interioriza{{titulo="💡 Tip 1 — Cómo estudiar las pausas para pensar"}}
Las **pausas 💭** no son adorno: son el lugar donde el cerebro hace el trabajo
real de aprendizaje. **Cierra el manual** después de leerlas, intenta responder
desde tu memoria, y solo entonces vuelve a verificar. Si respondes con el libro
abierto, te estás engañando.
::/interioriza

::interioriza{{titulo="💡 Tip 2 — La regla de los 20 minutos"}}
Si llevas más de 20 minutos atorado en un mismo ejercicio: **levántate, camina
5 minutos** y vuelve. Si después de eso sigues atorado, **pasa al siguiente**
ejercicio y regresa al final. Los cerebros aprenden mejor con descanso
intercalado que con persistencia ciega.
::/interioriza

::interioriza{{titulo="💡 Tip 3 — Bitácora de errores"}}
Cuando te equivoques en un ejercicio, **no borres**: tacha y escribe abajo la
versión correcta + una frase que diga *por qué* te equivocaste. Esa bitácora
de errores es el mejor material de repaso para el examen integrador.
::/interioriza

## Lecturas cruzadas con otras unidades

::concepto{{titulo="Conexiones temáticas internas"}}
Algunos temas de este semestre conectan directamente con otros del manual o de
otros manuales de la serie. Aprovecharlos te dará una visión más sistémica:

- **{m['titulos_unidad'].get(units[0], 'Unidad inicial')}** conecta con la unidad final del semestre porque sienta las bases que ahí se aplican.
- **{m['titulos_unidad'].get(units[-1], 'Unidad final')}** prepara el terreno para el próximo semestre o manual.
- Los temas de este semestre son **insumo directo** para los demás manuales de la serie Albatros — guarda tus evidencias.
::/concepto

## Para profundizar

::fuentes{{titulo="📚 Curaduría extendida del semestre"}}
- 📘 **Libro** · Texto base recomendado para el manual completo (consulta la bibliografía general del manual).
- 🌐 **Web** · {m['fuentes_curaduria'].split(' · ')[0]}.
- 🎓 **OCW** · {m['fuentes_curaduria'].split(' · ')[2] if len(m['fuentes_curaduria'].split(' · ')) > 2 else 'OCW del área'}.
- 📺 **Video** · {m['fuentes_curaduria'].split(' · ')[1] if len(m['fuentes_curaduria'].split(' · ')) > 1 else 'Crash Course / Veritasium'}.
- 📰 **Artículo** · Lectura breve sobre el case study **{m['case_study']}** (consulta con tu docente la referencia local).
- 🇲🇽 **México** · Programas oficiales de bachillerato y referencias mexicanas relacionadas con el case.
::/fuentes

## Ejercicios extra (banco transversal del semestre)

::act-challenge{{titulo="🚀 Reto integrador del semestre"}}
Diseña una **infografía A3** que conecte las {len(units)} unidades del semestre
en torno al case study **{m['case_study']}**. Debe incluir:
- El problema inicial.
- Una herramienta por unidad.
- La evidencia que producirá cada unidad.
- La conexión con el siguiente semestre.

Compártela con #AlbatrosManual{manual_n}.
::/act-challenge

::act-mcq{{titulo="Repaso transversal de opción múltiple"}}
1. La función principal del case study **{m['case_study']}** en este manual es:
   - [ ] Decorar el manual con un ejemplo
   - [x] Ser hilo conductor que conecta unidades
   - [ ] Sustituir el examen final
   - [ ] Reducir las horas de clase

2. Para considerar aprobado el semestre debes demostrar competencias en al menos…
   - [ ] 50 % de los criterios
   - [ ] 65 % de los criterios
   - [x] 80 % de los criterios
   - [ ] 100 % de los criterios

3. Cuando una pausa 💭 te pide responder con tus palabras conviene:
   - [ ] Copiar del libro
   - [ ] Saltarla
   - [x] Cerrar el libro y responder de memoria
   - [ ] Pedirle la respuesta a un compañero
::/act-mcq

::visual{{tipo="infografia" descripcion="Infografía resumen del semestre completo en una sola hoja: panel superior con el case study, panel medio con las {len(units)} unidades del semestre como columnas (cada columna con título, ícono y entregable), panel inferior con los 3 hábitos de estudio Albatros y el portafolio final. Paleta azul Albatros + naranja, listo para colgar en el cuaderno." paginas=1 nota="resumen visual del semestre — útil como póster del estudiante"}}
"""


def render_glosario_semestre(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    return f"""---
seccion: glosario-semestre
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 4
---

# Glosario del Semestre {sem}

Compendio de términos clave introducidos durante este semestre. Cada término
remite a la unidad donde fue introducido. Si quieres una definición más
extensa, consulta el glosario general del manual completo.

::concepto{{titulo="Cómo usar este glosario"}}
- Si encuentras un término **en negritas** en cualquier unidad, búscalo aquí primero antes que en internet.
- Cada entrada tiene: **término** · *categoría* · definición operativa · referencia a la unidad de origen.
- Las entradas marcadas con 🟦 son del **eje teórico**; las marcadas con 🟧 son del **eje práctico/instrumental**.
::/concepto

**Términos del semestre** (orden alfabético — completar con los términos
introducidos en las {len(units)} unidades):

- 🟦 **Case study (hilo conductor)** · *concepto pedagógico* · Problema o
  situación real que un manual entero usa como contexto para que el alumno
  aplique cada unidad. En este manual: **{m['case_study']}**.
- 🟦 **Competencia eje** · *concepto pedagógico* · Saber-hacer central que el
  semestre entero pretende desarrollar. Para este semestre:
  *{m['competencia_eje']}.*
- 🟧 **Portafolio del semestre** · *evidencia* · Documento físico o digital que
  reúne todas las evidencias producidas; se entrega al cierre del semestre.
- 🟧 **Pausa para pensar** · *bloque pedagógico* · Mini-actividad detonadora
  que aparece cada 4–6 páginas para forzar reflexión antes de continuar.
- 🟧 **Implementación Albatros** · *bloque pedagógico* · Proyecto integrador
  al final de cada unidad con materiales, pasos, entregable y rúbrica.

::interioriza{{titulo="Lleva tu propio glosario"}}
Cada vez que encuentres un término en **negrita** que NO esté en este
glosario, agrégalo a tu cuaderno con tu propia definición. Al final del
semestre vas a tener un glosario personalizado mucho más útil que cualquiera
hecho por otro.
::/interioriza

::act-table{{titulo="Tabla de términos para llenar"}}
| Término | Categoría (🟦/🟧) | Definición con tus palabras | Unidad |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
::/act-table

::visual{{tipo="cuadro-comparativo" descripcion="Tabla amplia con dos columnas principales: 'Término en español' y 'Término en inglés equivalente' para los principales conceptos del semestre. Útil para estudiantes que también consultan fuentes en inglés. Encabezado en azul Albatros, zebra sutil, ícono de bandera 🇲🇽/🇺🇸 en cada cabecera de columna." paginas=0.5 nota="ayuda bilingüe para fuentes en inglés"}}
"""


def render_bibliografia_semestre(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    return f"""---
seccion: bibliografia-semestre
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 2
---

# Bibliografía y recursos del Semestre {sem}

Curaduría de fuentes recomendadas para profundizar en cada unidad del
semestre. Mezcla obligatoria de medios para que practiques aprender con
distintos formatos.

::fuentes{{titulo="📚 Curaduría base del manual"}}
{chr(10).join('- ' + line.strip() for line in m['fuentes_curaduria'].split(' · '))}
::/fuentes

::concepto{{titulo="Cómo citar las fuentes"}}
- **Libro:** Apellido, Inicial. (año). *Título*. Editorial, edición, página.
- **Web:** Nombre del sitio. (año). Título del recurso. URL corta. Consultado el día/mes/año.
- **Video:** Canal. (año). *Título del video* [video]. Plataforma. URL corta. Min. 00:00–00:00.
- **Artículo académico:** Apellido, Inicial. (año). Título del artículo. *Revista*, vol(núm), pp.
- **Fuente mexicana oficial:** SEMARNAT / CONAGUA / SEP / etc. (año). *Título del documento normativo*. URL oficial.

Sugerencia: lleva una **bitácora de fuentes** durante el semestre y al final
genera una bibliografía propia con al menos 15 entradas curadas.
::/concepto

::act-table{{titulo="Bitácora de fuentes (rellena durante el semestre)"}}
| # | Fuente (medio + título) | Unidad donde la usaste | Lo que aprendiste | Cita correcta |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |
| 7 |  |  |  |  |
| 8 |  |  |  |  |
::/act-table

::visual{{tipo="cuadro-comparativo" descripcion="Cuadro comparativo de 5 columnas con los principales tipos de fuente: Libro, Web, OCW, Video, Artículo. Por cada fila: profundidad esperada, tiempo de consulta promedio, criterio de verificación, ejemplos típicos del manual, ventajas y desventajas. Encabezado azul Albatros, ícono por columna." paginas=0.5 nota="ayuda visual para elegir el tipo de fuente correcto según objetivo"}}
"""


def render_indice_analitico(manual_n: int, sem: int, m: dict, units: list[str]) -> str:
    return f"""---
seccion: indice-analitico
semestre: {sem}
manual: {manual_n}
paginas_objetivo: 2
---

# Índice analítico del Semestre {sem}

Listado de términos, conceptos y figuras del semestre con referencia a la
unidad donde aparecen. Se generará automáticamente al cierre de la edición —
este archivo reserva el espacio de paginación.

::concepto{{titulo="Sobre este índice"}}
El índice analítico es la herramienta de **consulta rápida** del manual.
Mientras estudias, cada vez que encuentres un término clave anótalo aquí con
la página donde aparece — al final del semestre tendrás un índice personal
inmejorable.
::/concepto

::act-table{{titulo="Índice analítico personal (anota durante el semestre)"}}
| Término / concepto / figura | Tipo | Unidad | Página | Notas |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
::/act-table

::visual{{tipo="ilustracion" descripcion="Pieza de cierre del semestre: bandera con el logo Albatros izándose en una colina baja, sol naciendo detrás (símbolo del siguiente semestre). Composición simple, paleta azul Albatros con sol naranja, estilo editorial outline + duotone, sin texto adicional." paginas=0.5 nota="ilustración decorativa de cierre"}}
"""


GENERADORES = [
    ("00-portada.md", render_portada),
    ("01-carta-estudiante.md", render_carta_estudiante),
    ("02-carta-docente.md", render_carta_docente),
    ("03-mapa-contenidos.md", render_mapa_contenidos),
    ("04-hilo-conductor.md", render_hilo_conductor),
    ("05-competencias.md", render_competencias),
    ("06-diagnostica.md", render_diagnostica),
    ("90-cierre-semestre.md", render_cierre_semestre),
    ("91-material-extra.md", render_material_extra),
    ("92-glosario-semestre.md", render_glosario_semestre),
    ("93-bibliografia-semestre.md", render_bibliografia_semestre),
    ("94-indice-analitico.md", render_indice_analitico),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="sobrescribir archivos existentes")
    ap.add_argument("--manual", type=int, choices=[1, 2, 3, 4, 5], default=None)
    args = ap.parse_args()

    targets = [args.manual] if args.manual else [1, 2, 3, 4, 5]
    created = 0
    skipped = 0
    for n in targets:
        m = META[n]
        for sem in (1, 2):
            units = SEMESTER_MAP[n][sem]
            sem_dir = MANUALES_DIR / f"manual-{n}" / f"semestre-{sem}"
            sem_dir.mkdir(parents=True, exist_ok=True)
            for filename, gen in GENERADORES:
                target = sem_dir / filename
                if target.exists() and not args.force:
                    skipped += 1
                    continue
                content = gen(n, sem, m, units)
                target.write_text(content, encoding="utf-8")
                created += 1
            # README de la carpeta
            readme = sem_dir / "README.md"
            if not readme.exists() or args.force:
                readme.write_text(f"""# Semestre {sem} — Manual {n}: {m['titulo']}

**Unidades de este semestre:** {", ".join(u.upper() + " (" + m['titulos_unidad'][u] + ")" for u in units)}

## Front matter (en orden)

1. `00-portada.md` — Portada e identidad del semestre
2. `01-carta-estudiante.md` — Carta al estudiante
3. `02-carta-docente.md` — Carta al docente
4. `03-mapa-contenidos.md` — Mapa de contenidos del semestre
5. `04-hilo-conductor.md` — Hilo conductor (case study) en este semestre
6. `05-competencias.md` — Índice de competencias del semestre
7. `06-diagnostica.md` — Evaluación diagnóstica inicial

## Unidades

Las unidades viven en `manuales/manual-{n}/unidades/` — este semestre incluye
las carpetas {", ".join("`" + u + "`" for u in units)}.

## Cierre y material extra

8. `90-cierre-semestre.md` — Cierre del semestre + proyecto integrador
9. `91-material-extra.md` — Material extra opcional (tips, retos, lecturas cruzadas)
10. `92-glosario-semestre.md` — Glosario de términos del semestre
11. `93-bibliografia-semestre.md` — Bibliografía y bitácora de fuentes
12. `94-indice-analitico.md` — Índice analítico personal

## Build

```bash
python build/converter.py manuales/manual-{n} dist/manual-{n}-sem-{sem}.html --semester {sem}
python print_to_pdf.py --manual {n} --semester {sem}
```
""", encoding="utf-8")
                created += 1
            else:
                skipped += 1

    print(f"OK — {created} archivos creados · {skipped} archivos preexistentes preservados")


if __name__ == "__main__":
    main()
