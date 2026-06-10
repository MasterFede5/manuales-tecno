---
unidad: 5
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Pipeline de investigación académica en 1 hora

::practica{titulo="Genera un ensayo investigativo de 2 páginas con citas verificables sobre 'Beneficios del aprendizaje activo'"}
**Problema.** Tu profesor pide ensayo de 2 pp sobre **"beneficios del aprendizaje activo en bachillerato mexicano"** con mínimo 5 citas científicas. Lo entregas mañana.

**Tu tarea:** ejecutar pipeline completo aplicando las 6 herramientas de la unidad. **Tiempo: 1 hora.**

---

**Paso 1 — Define pregunta y scope (5 min).**

Pregunta: *"¿El aprendizaje activo (vs pasivo) mejora rendimiento académico en estudiantes de 15-18 años en contexto latinoamericano/mexicano?"*

Scope: estudios 2015-2025, peer-reviewed cuando sea posible, mezcla de tipos (experimentales, observacionales, meta-análisis).

---

**Paso 2 — Búsqueda inicial con Perplexity (10 min).**

Modo: **Pro + Academic focus**.

Prompt:
```
Compara aprendizaje activo vs pasivo en bachillerato. Enfócate en
estudios con población latinoamericana o mexicana. Lista los 5
papers más citados con resumen de 1 línea, año, sample size.
Distingue entre meta-análisis y estudios primarios.
```

Output: 5-7 papers con citas verificables. Anota DOIs.

---

**Paso 3 — Validación con Consensus (10 min).**

Pregunta en Consensus:
```
Does active learning improve academic performance in high school students?
```

Resultado: barra de consenso (probablemente 70-80% **YES**), papers individuales.

Cruza con los de Perplexity. Quédate con los **5 más citados y consistentes**.

---

**Paso 4 — Lectura asistida con SciSpace (15 min).**

De los 5 papers seleccionados, abre los **3 más relevantes** en SciSpace.

Para cada uno:
- Pregunta al chat: *"Cuál es la metodología en simple, sample size, hallazgo principal y limitación principal."*
- Copia las respuestas a un Doc.

Extrae automáticamente con SciSpace su **bloque de citas** en APA 7.

---

**Paso 5 — Síntesis con NotebookLM (10 min).**

1. Crea notebook nuevo.
2. Carga los 5 PDFs (los que tengas; si no, sus links).
3. Genera **Briefing Doc** (resumen de 2 pp).
4. Genera **Mind Map** para visualizar conexiones.
5. Pregunta al notebook: *"Genera un párrafo de 200 palabras sintetizando los 5 papers, manteniendo citas a las páginas exactas."*

---

**Paso 6 — Redacción del ensayo con Claude/ChatGPT (15 min).**

Prompt al modelo:
```
Eres redactor académico. Redacta ensayo de 2 páginas (~700 palabras)
sobre 'beneficios del aprendizaje activo en bachillerato mexicano'.

Estructura:
1. Introducción (100 palabras): contexto y pregunta.
2. Marco teórico (200 palabras): aprendizaje activo definición + teóricos.
3. Evidencia (300 palabras): integra los 5 papers que te paso abajo,
   citando en APA 7.
4. Aplicación al contexto mexicano (100 palabras).
5. Conclusión (50 palabras).

Tono: académico pero accesible. Voz mía: yo soy estudiante de
bachillerato, no especialista.

[pega los 5 resúmenes de SciSpace + briefing de NotebookLM]
```

Recibes ensayo de 700 palabras con citas en APA 7.

---

**Paso 7 — Verificación y declaración (5 min).**

1. **Verifica cada cita.** Click en DOI → confirma que el paper existe y dice lo que cita.
2. **Reescribe** 2-3 párrafos en tu propia voz (no quede 100% como output del modelo).
3. **Agrega declaración de uso de IA** al final.
4. Pasa por **Grammarly o Hemingway** para pulir.

---

**Resultado.**

Ensayo de 2 pp, 5 citas verificables APA 7, marco teórico sólido, declaración de uso. **Tiempo total: 1 hora.**

Sin IA esto sería: 5-8 horas leyendo papers + redactando.

> **Verificación profesional.**
> - Las 5 citas son reales y consistentes (no inventadas por ChatGPT).
> - El ensayo tiene tu voz en al menos 30% de los párrafos.
> - La declaración de uso es transparente.
> - Tu profesor recibe trabajo de calidad y proceso transparente.

> **Trampa común evitada.** No le pidas a ChatGPT "*genérame ensayo con 5 citas*" — te dará citas inventadas. **Siempre encuentra papers reales primero** (Perplexity/Consensus), luego pide al modelo redactar **a partir de ellos**.
::/practica

---

## Práctica resuelta — Cómo NotebookLM redujo mi tiempo de estudio de 4 horas a 50 minutos

::practica{titulo="Estudio activo de un capítulo de 80 páginas con audio + mapa + quiz autogenerado"}
**Problema.** Tienes que estudiar el capítulo "Termodinámica" del libro de Física de Tippens, 80 páginas, examen el viernes. Con lectura tradicional son 4 horas. Vas a hacerlo en 50 minutos con calidad equivalente.

**Paso 1 — Pre-flight (5 min).**

- Verifica que tu PDF tenga OCR limpio. Abre y selecciona texto en una página al azar; si seleccionas correcto, OK.
- Sube el PDF a NotebookLM. Espera a que indexe.
- Pregunta de control: "¿Qué dice el capítulo sobre la primera ley de la termodinámica?". Si cita página correcta, OK.

**Paso 2 — Generar audio overview (10 min).**

Pides:

```
Audiencia: estudiante de bachillerato CCH-UNAM con álgebra básica.
Tono: conversacional, con analogías cotidianas.
Foco: las 3 leyes de la termodinámica con ejemplos numéricos.
Duración: 12 minutos.
Idioma: español neutro.
```

Mientras genera (3-5 min), abres tu app de podcast y bajas los AirPods.

**Paso 3 — Escucha activa caminando (15 min).**

Sales a caminar con el audio. **No tomas notas.** Solo escuchas con atención. Si te distraes, regresa 30 segundos. El objetivo no es memorizar, es **construir el modelo mental general**.

**Paso 4 — Mapa mental (10 min).**

Vuelves al notebook. Pides:

```
Genera un esquema jerárquico Markdown del capítulo con:
- 4 ramas principales (las 3 leyes + aplicaciones).
- 3-4 hojas por rama.
- En cada hoja, una palabra clave (no una oración).
- Markdown puro con guiones.
```

Pegas el Markdown en https://markmap.js.org. Te genera mapa interactivo.

**Paso 5 — Quiz autogenerado (10 min).**

Pides:

```
Genera 12 preguntas tipo examen UNAM-CCH:
- 6 opción múltiple con 4 opciones cada una.
- 3 verdadero-falso justificado.
- 3 problema numérico simple.
Para cada pregunta, da la respuesta correcta y la página/sección
del capítulo que la respalda.
Devuélvelo en formato Markdown.
```

Pegas en un documento aparte. Las respuestas en hoja separada.

**Paso 6 — Auditoría rápida (5 min).**

Antes de confiar el quiz:
- Verifica 3 preguntas al azar abriendo el PDF en la página citada.
- Si dos están bien y una mal, ya sabes la tasa de error (~33%); marca la mala como dudosa.

**Paso 7 — Plan de 5 días.**

| Día | Actividad | Tiempo |
|---|---|---|
| Lun | Audio caminando + mapa mental rápido | 25 min |
| Mar | Mapa mental detallado + lectura focalizada de zonas débiles | 40 min |
| Mié | Quiz primer intento sin respuestas | 30 min |
| Jue | Repaso de errores + lectura focalizada | 30 min |
| Vie | Quiz segundo intento + autoevaluación final | 30 min |

**Resultado:** 2 horas y media distribuidas en 5 días, vs 4 horas en una sola sesión que olvidas en una semana.

> **Lección clave.** El audio overview no reemplaza estudiar; **multiplica la repetición** sin que pese. Tu cerebro graba mejor con repetición espaciada que con sesiones maratón. Aplica este pipeline a cada capítulo grande del semestre.
::/practica

---

## Práctica resuelta — Detecté 2 citas alucinadas en un workflow Perplexity → Claude

::practica{titulo="Audita citas reales del pipeline académico y rescata el ensayo"}
**Problema.** Hiciste el pipeline académico de la práctica anterior y entregaste el ensayo. Tu profesor te marca "verifica las citas 3 y 5; las búsquedas no las encuentran". Tienes que auditar y rescatar.

**Paso 1 — Lista las 5 citas y sus estatus iniciales.**

| # | Cita | DOI | Estatus inicial |
|---|---|---|---|
| 1 | Freeman et al. (2014). "Active learning increases student performance in science, engineering, and mathematics". PNAS, 111(23), 8410-8415. | 10.1073/pnas.1319030111 | A verificar |
| 2 | Theobald et al. (2020). "Active learning narrows achievement gaps...". PNAS, 117(12), 6476-6483. | 10.1073/pnas.1916903117 | A verificar |
| 3 | López-García y Méndez (2019). "Aprendizaje activo en CCH-UNAM". RMIE, 24(82), 567-589. | 10.1234/rmie.2019.82.05 | A verificar |
| 4 | Deslauriers et al. (2019). "Measuring actual learning vs feeling of learning". PNAS, 116(39), 19251-19257. | 10.1073/pnas.1821936116 | A verificar |
| 5 | Hernández-Ruiz (2021). "Meta-análisis aprendizaje activo Latinoamérica". Revista Iberoamericana de Educación, 85(2), 123-145. | 10.5678/rie.2021.85.07 | A verificar |

**Paso 2 — Verificación una por una.**

Pegas cada DOI en https://doi.org:

| # | Resultado | Veredicto |
|---|---|---|
| 1 | Freeman et al. (2014) PNAS — existe y es famoso | **REAL** |
| 2 | Theobald et al. (2020) PNAS — existe | **REAL** |
| 3 | DOI no encontrado. Buscas "López-García Méndez RMIE 2019 aprendizaje activo CCH" en Google Scholar: **no aparece** | **ALUCINADA** |
| 4 | Deslauriers et al. (2019) PNAS — existe | **REAL** |
| 5 | DOI no encontrado. La revista existe pero no hay artículo con ese título y autor | **ALUCINADA** |

**Resultado:** **3 citas reales, 2 alucinadas**. El profesor tenía razón.

**Paso 3 — Rescate.**

Necesitas reemplazar las 2 alucinadas con citas reales y mantener tu argumento (estudios de contexto latinoamericano/mexicano).

Vuelves a Consensus y a Google Scholar:

```
Site: scholar.google.com
"aprendizaje activo" OR "active learning" "México" OR "Latinoamérica" 
"bachillerato" OR "preparatoria" 2015..2024
```

Encuentras 3 papers reales:
- Sánchez-Mendoza (2017). RMIE 22(75) — sobre aprendizaje activo en preparatorias mexicanas. **DOI verificado**.
- García-Hernández (2020). Educar 56(3) — meta-análisis Latinoamérica. **DOI verificado**.
- Estrada-Vázquez (2018). Perfiles Educativos. **DOI verificado**.

Eliges 2 para reemplazar. Reescribes los dos párrafos correspondientes adaptando ligeramente la idea para que sean consistentes con los nuevos hallazgos.

**Paso 4 — Re-entrega con cambios marcados.**

Entregas el ensayo v2 con las citas reales + una nota: "agradezco la revisión; verifiqué las citas y reemplacé 2 que eran alucinaciones del modelo. Adjunto bitácora de verificación".

**Resultado.** Tu profesor sube tu nota porque demostraste **rigor en verificación**, que es exactamente la habilidad que evalúa.

> **Lección clave.** Las alucinaciones de citas son el **error más caro** del pipeline académico porque parecen reales. Regla: **verifica con DOI cada cita antes de entregar, sin excepciones**. Esos 5 minutos te ahorran reprobaciones.
::/practica
