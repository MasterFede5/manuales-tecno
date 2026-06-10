---
unidad: 4
seccion: taller
paginas_objetivo: 2
---

## Taller — Sube tu reglamento personal y haz 5 preguntas golden

::albatros{titulo="Subes un documento personal y construyes tu mini-RAG en 60 minutos" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Tu Asistente puede responder, en 30 segundos y con la página exacta, una pregunta que tú habrías tenido que buscar durante 10 minutos en un PDF largo?

**Lo que harás.** Vas a subir un **documento personal real** —el reglamento de tu institución, un manual técnico, las bases de un concurso, un libro extenso— y construir tu mini-RAG en NotebookLM. Al cerrar el cronómetro, tu mini-RAG responde 5 preguntas golden con cita, una pregunta deliberadamente fuera del documento (debe responder "no tengo info"), y una pregunta combinada que cruza dos secciones.

**Materiales reales.**
- Cuenta gratis NotebookLM (Google).
- 1 PDF real con texto seleccionable. Si solo tienes escaneo, primero pasarlo por OCRmyPDF (gratis) o Adobe Acrobat OCR. Mínimo 20 páginas, máximo 100.
- 60 min sin notificaciones.

**Pasos (10).**

1. **Min 0–5 — Verificación del PDF.** Abre el PDF. Selecciona texto. Si **no se selecciona**, es escaneo: pasalo por OCR antes de seguir. Renómbralo: `<tipo>_<nombre>_v<X.Y>_<fecha>.pdf` (ej. `reglamento_albatros_v3.0_2026-08-15.pdf`).

2. **Min 5–10 — Crear notebook.** Entra a notebooklm.google.com. Crea un Notebook nuevo. Dale título: *"Reglamento Albatros — RAG personal v1"*. Sube el PDF. Espera análisis automático (1-3 min).

3. **Min 10–15 — Configurar instrucciones.** En "Notebook guide" o equivalente, escribe instrucciones:
   - Tono profesional y cálido.
   - Cita siempre página exacta entre paréntesis.
   - Si no encuentras la respuesta en el documento, di **literalmente** "no tengo información sobre eso en el documento cargado".
   - No inventes artículos, fechas o nombres que no estén en el documento.

4. **Min 15–25 — Construir golden set de 7 preguntas.** En tu editor, escribe:
   - **5 preguntas con respuesta esperada** (sabes dónde está la respuesta y cuál es).
   - **1 pregunta combinada** que cruza dos secciones del documento.
   - **1 pregunta deliberadamente fuera del documento** (debe disparar "no tengo info").

5. **Min 25–40 — Lanzar las 7 preguntas.** Una a una en el chat de NotebookLM. Para cada respuesta, registra en una tabla:
   - Texto de la respuesta.
   - ¿Citó página? (sí/no)
   - ¿Acertó? (sí / parcial / inventó / dijo "no sé" correctamente)
   - Tiempo de respuesta (visual).

6. **Min 40–45 — Identificar el patrón de fallo.** Si tienes una falla, mira el chunk que se recuperó (NotebookLM lo muestra). Pregúntate:
   - ¿La respuesta sí estaba en el documento? Sí → problema de recuperación o instrucciones.
   - ¿No estaba? → la pregunta era fuera-de-documento, comportamiento correcto si dijo "no sé".
   - ¿Inventó? → endurece instrucciones anti-alucinación y vuelve a intentar.

7. **Min 45–50 — Reforzar instrucciones si hubo invención.** Si NotebookLM alucinó, agrega a las instrucciones del notebook:
   - "Antes de responder, copia textualmente la frase del documento que respalda tu respuesta. Si no puedes copiarla, di 'no tengo información'".
   - Reejecuta la pregunta que falló.

8. **Min 50–55 — Audio Overview.** Genera el Audio Overview del documento (botón "Audio Overview" en NotebookLM). Tarda 5-12 min — déjalo corriendo de fondo.

9. **Min 55–58 — Documentar resultados.** En un archivo `notebooklm-rag-v1.md`, pega: nombre del PDF, las 7 preguntas, las 7 respuestas, tu evaluación, el patrón de fallo encontrado, y la versión de instrucciones que mejor funcionó.

10. **Min 58–60 — Compartir.** Comparte el notebook (botón Share) con **una persona** y mándale 1 pregunta para que la lance ella misma. Apunta su feedback de 30 segundos.

**Entregable.**
- Notebook NotebookLM compartido.
- Audio Overview en MP3 o link.
- Archivo `notebooklm-rag-v1.md` con golden de 7 preguntas, resultados, patrón de fallo, instrucciones finales.
- Captura del feedback de la persona externa.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Calidad del PDF | sin OCR | seleccionable | con metadatos limpios |
| Golden set | <5 preguntas | 7 con tipos mixtos | 7 incluyendo fuera-de-doc y combinada |
| Mitigación de alucinaciones | reactiva | instrucciones reforzadas | instrucciones probadas con re-test |
| Audio Overview | no se generó | generado | usado para onboarding o estudio |
| Documentación | informal | tabla con resultados | tabla + análisis + plan v1.1 |
| Validación social | no se hizo | persona miró | persona lanzó pregunta y dio feedback |
::/albatros
