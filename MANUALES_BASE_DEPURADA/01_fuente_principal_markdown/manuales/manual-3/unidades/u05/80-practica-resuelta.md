---
unidad: 5
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Pipeline de investigación académica en 1 hora

::practica{titulo="Genera un ensayo investigativo de 2 páginas con citas verificables sobre 'Beneficios del aprendizaje activo'"}
**Problema:**
- Profesor exige 2 páginas sobre **aprendizaje activo en México**.
- Requiere 5 citas científicas reales.
- Entrega mañana a primera hora.

**Tu misión:**
- Ejecutar el pipeline completo de IA.
- Tiempo límite: **1 hora**.

---

**Paso 1 — Define pregunta y scope (5 min)**
- **Pregunta:** ¿El aprendizaje activo mejora el rendimiento en bachillerato mexicano?
- **Scope:** 2015-2025, peer-reviewed, diversos enfoques.

**Paso 2 — Búsqueda inicial con Perplexity (10 min)**
- Usa **Pro + Academic focus**.
- **Prompt:** "Compara aprendizaje activo vs pasivo en bachillerato. Enfócate en Latinoamérica/México. Lista 5 papers top con citas y DOIs."

**Paso 3 — Validación con Consensus (10 min)**
- **Prompt:** "Does active learning improve academic performance in high school students?"
- Cruza resultados y filtra los 5 más citados y sólidos.

**Paso 4 — Lectura asistida con SciSpace (15 min)**
- Abre los 3 papers más relevantes.
- Pregunta: *"Metodología simple, sample size, hallazgo principal y limitación."*
- Extrae bloque de citas en APA 7.

::interioriza
**Analogía del Chef Investigador:**
Hacer este pipeline es como preparar un platillo rápido. Perplexity y Consensus cazan los ingredientes. SciSpace te los pela y corta. NotebookLM es tu procesador de alimentos, y Claude es el horno.
::/interioriza

**Paso 5 — Síntesis con NotebookLM (10 min)**
- Sube los 5 PDFs.
- Genera **Briefing Doc** (resumen 2 pp) y **Mind Map**.
- Pide: *"Párrafo de 200 palabras sintetizando los 5 papers con citas."*

**Paso 6 — Redacción del ensayo con Claude/ChatGPT (15 min)**
- **Rol:** Redactor académico nivel bachillerato.
- **Estructura:** Intro (100), Teoría (200), Evidencia (300), Aplicación (100), Cierre (50).
- Integra el material extraído de SciSpace y NotebookLM.

**Paso 7 — Verificación y declaración (5 min)**
- **Verifica:** Click en cada DOI para asegurar existencia.
- **Edita:** Reescribe 30% en tu propia voz.
- **Declara:** Agrega nota de uso de IA.

::pausa{}
**Deducción lógica:**
¿Por qué el paso 3 (Consensus) es crítico antes del paso 6 (Claude)?
*Pista: Piensa en lo que Claude suele hacer cuando le faltan datos verificables.*
::/pausa

> **Trampa común evitada:** Nunca pidas a ChatGPT "genérame 5 citas". Te dará alucinaciones. Primero busca papers reales, luego redacta.
::/practica

---

## Práctica resuelta — Estudio activo de 80 páginas en 50 minutos

::practica{titulo="Estudio activo de un capítulo de 80 páginas con audio + mapa + quiz autogenerado"}
**Problema:**
- Capítulo "Termodinámica" (80 páginas).
- Examen en pocos días.
- Lectura tradicional: 4 horas. Tu meta: 50 minutos.

**Paso 1 — Pre-flight (5 min)**
- Confirma OCR del PDF (texto seleccionable).
- Sube a NotebookLM y haz pregunta de control para validar indexación.

**Paso 2 — Audio overview (10 min)**
- Genera podcast explicativo nivel bachillerato.
- Tono conversacional, analogías cotidianas, 12 minutos.

**Paso 3 — Escucha activa (15 min)**
- Sal a caminar. Escucha sin tomar notas.
- Objetivo: **Construir un mapa mental general**.

**Paso 4 — Mapa mental (10 min)**
- Pide a NotebookLM un esquema jerárquico Markdown.
- Pega en Markmap para visualizar las ramas principales.

**Paso 5 — Quiz autogenerado (10 min)**
- Pide 12 preguntas formato examen UNAM-CCH.
- Exige justificación y página de referencia.

::interioriza
**Analogía del Entrenador:**
El audio es el calentamiento que relaja el cerebro. El mapa mental es la táctica en el pizarrón. El quiz es el partido amistoso donde no importa fallar, solo ajustar la técnica.
::/interioriza

**Auditoría y Plan:**
- Revisa aleatoriamente 3 preguntas del quiz con el PDF.
- Distribuye el estudio: 2.5 horas en 5 días breves vs. 4 horas de golpe.

::pausa{}
**Reflexión:**
Si el quiz autogenerado te da una respuesta errónea pero tú debes buscar en el PDF para desmentirla, ¿eso arruinó tu sesión o la mejoró?
::/pausa
::/practica

---

## Práctica resuelta — Detecté 2 citas alucinadas

::practica{titulo="Audita citas reales del pipeline académico y rescata el ensayo"}
**Problema:**
- Profesor marcó 2 citas como sospechosas en tu ensayo.
- Debes auditar, verificar y rescatar el trabajo.

**Paso 1 y 2 — Verificación por DOI**
- Pegar cada DOI en `doi.org`.
- Freeman (2014) y Theobald (2020) existen.
- López-García (2019) y Hernández-Ruiz (2021) dan error 404. ¡Alucinadas!

**Paso 3 — Rescate ágil**
- Vuelve a Consensus/Google Scholar.
- Busca: `"aprendizaje activo" "México" 2015..2024`.
- Encuentra 2 papers reales para suplir los falsos.
- Reescribe sutilmente los párrafos afectados.

::interioriza
**Analogía del Inspector:**
No eres el autor ciego, eres el inspector de aduanas. Toda cita que entra al ensayo debe mostrar su pasaporte (DOI) real. Si el pasaporte es falso, se deporta la cita.
::/interioriza

**Paso 4 — Re-entrega transparente**
- Envía versión corregida.
- Incluye bitácora de auditoría demostrando rigor.

::pausa{}
**Análisis forense:**
Si Claude es tan avanzado, ¿por qué inventó a "López-García (2019)" en vez de decir "no encontré más papers mexicanos"?
::/pausa

> **Regla de oro:** Las alucinaciones son el error más letal. Verifica con DOI cada cita antes de entregar.
::/practica
