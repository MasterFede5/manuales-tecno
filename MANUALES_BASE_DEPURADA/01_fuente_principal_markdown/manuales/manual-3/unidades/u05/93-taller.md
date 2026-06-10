---
unidad: 5
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Tu tutor estudia un PDF contigo: pipeline NotebookLM + mapa mental + quiz

> Este taller convierte a tu tutor IA en un **compañero de estudio activo**. Le das un PDF que vas a leer en clase, y tu tutor te genera el paquete completo: audio para escucharlo caminando, mapa mental para repasar visualmente, y quiz para autoevaluarte antes del examen.

::albatros{titulo="De PDF a paquete de estudio completo en 60 minutos" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Puedes convertir cualquier capítulo de libro en un paquete multi-formato (audio + mapa mental + quiz) que reemplace 3 horas de estudio pasivo por 1 hora de estudio activo?

**Lo que harás (10 pasos).**

1. **Elige un PDF real** que vas a estudiar este mes (mínimo 30 páginas). Si es escaneado, verifica que el OCR sea legible; si no, conviértelo en https://tools.pdf24.org u OCR de Adobe.
2. **Sube el PDF a NotebookLM** y crea el notebook "Estudio [tema]".
3. **Pregunta de control:** haz una pregunta cuya respuesta esté en la página 5 y otra en la página 25. Verifica que NotebookLM cita correctamente. Si no cita, descartar y subir un PDF mejor.
4. **Genera el Audio Overview** en modo customizado: define audiencia (tú), tono (conversacional o académico), foco (los 3-5 temas que más caen en examen), duración 12-15 min.
5. **Genera el mapa mental.** Si NotebookLM tiene función "Mind Map", úsala. Si no, pídele a Claude/ChatGPT con el PDF subido: "Genera esquema jerárquico Markdown con 6 ramas principales y 3-5 hojas por rama". Pega el esquema en Markmap (markmap.js.org) o Whimsical AI para visualizarlo.
6. **Genera el quiz.** Pide al notebook: "Genera 15 preguntas tipo examen UNAM/admisión: 6 opción múltiple, 4 verdadero/falso, 3 conceptual abierta, 2 de aplicación. Para cada una, da la respuesta correcta y la página/sección que la respalda".
7. **Auditoría:** verifica 3 datos del audio + 3 preguntas del quiz contra el PDF abierto. Marca alucinaciones si las hay.
8. **Define tu plan de estudio activo:** lunes audio caminando, martes mapa mental, miércoles primer intento del quiz, jueves repaso de errores, viernes segundo intento sin ver respuestas.
9. **Documenta** en un archivo `estudio-[tema].md`: link al notebook, MP3 del audio, PNG del mapa mental, hoja con quiz + respuestas, plan de 5 días, 3 alucinaciones detectadas (si las hubo).
10. **Pruébalo.** Sigue el plan de 5 días. Al final, mide en una autoevaluación: ¿cuál de los 3 formatos te ayudó más?

**Materiales.**
- NotebookLM (gratis con cuenta Google).
- Claude o ChatGPT para refinar el esquema del mapa mental.
- Markmap (markmap.js.org), Whimsical AI o Mapify para visualización.
- Cuaderno o documento para tomar notas durante el quiz.

**Entregable.**
1. Archivo `estudio-[tema].md` con todo organizado.
2. MP3 del audio overview.
3. PNG/SVG del mapa mental.
4. Hoja de cálculo con quiz, respuestas y página que lo respalda.
5. Reflexión escrita de 200 palabras: ¿qué formato te ayudó más a recordar al final del 5to día? ¿qué descartaste y por qué?

**Rúbrica corta.**

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Calidad del audio | sin customizar | customizado básico | customizado con audiencia, foco y duración |
| Mapa mental | esquema texto | mapa generado | mapa visual con jerarquía clara |
| Quiz | 5 preguntas | 10 preguntas | 15 preguntas con 4 tipos distintos |
| Auditoría | sin verificar | 1-2 datos | 3+ datos verificados con páginas |
| Plan de 5 días aplicado | no aplicado | seguido parcial | aplicado completo con métricas finales |

**Tip Albatros.** El paquete que armas aquí es el formato estándar que vas a aplicar a CADA materia que estudies de aquí en adelante. Crea una **plantilla** (Notion template, archivo Markdown vacío) con la estructura para no rehacerla cada vez. La inversión inicial de esta hora vale meses de estudio más eficiente.
::/albatros
