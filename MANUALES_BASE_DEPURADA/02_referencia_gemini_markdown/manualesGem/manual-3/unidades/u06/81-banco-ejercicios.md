---
unidad: 6
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 06

> Banco de práctica para automatización personal con IA: correo, hojas, presentaciones, documentos, tareas y reuniones. Privilegia ejercicios de **decisión de herramienta** y **diseño de flujos automatizados**. Resuelve antes de mirar la clave.

---

### Bloque A — Correo (6.1)

::act-mcq{titulo="Decisiones de correo automatizado"}
1. Vives en Gmail con cuenta UNAM. Tu mejor opción para automatizar respuestas es:
   - [x] Gemini en Gmail (integración nativa)
   - [ ] Copilot
   - [ ] Claude
   - [ ] Superhuman gratis

2. La función de Superhuman que NO existe (free) en Gmail Classic es:
   - [ ] Búsqueda
   - [x] Triage automático con IA y "Instant Reply"
   - [ ] Etiquetas
   - [ ] Filtros

3. Tu compañero usa Outlook por trabajo y Gmail por estudios. Recomendación:
   - [ ] Solo Copilot
   - [ ] Solo Gemini
   - [x] Copilot para Outlook + Gemini para Gmail (cada uno donde es nativo)
   - [ ] ChatGPT en ambos
::/act-mcq

::act-fill{titulo="Anatomía del prompt de correo profesional"}
Para que tu IA redacte un buen correo, le das: a) **rol** (eres mi asistente ejecutivo), b) **destinatario** y _____________ con él, c) **objetivo del correo** en una línea, d) **tono** (formal/cordial/directo), e) **longitud** máxima (_____________ palabras), f) **información clave** que debe incluirse, g) **acción esperada** del destinatario. Si el correo va a un _____________, el tono se eleva; si es de seguimiento, agrega referencia al hilo previo.
::/act-fill

---

### Bloque B — Hojas de cálculo (6.2)

::act-case{titulo="Diseña 3 flujos con GPT for Sheets / Copilot Excel" lineas=12}
Para cada caso, redacta la fórmula y explica brevemente:

1. Tienes 200 reseñas de producto en columna A. Quieres clasificarlas en columna B como POSITIVA / NEGATIVA / NEUTRA.
2. Tienes 50 títulos de papers en columna A. Quieres en columna B su tema en 3 palabras y en columna C el método (cuantitativo / cualitativo / mixto).
3. Tienes 100 correos en columna A (texto crudo). Quieres en columna B un resumen de 1 frase y en columna C la categoría (familia / escuela / trabajo / suscripción / basura).
::/act-case

::act-tf{titulo="V/F sobre IA en hojas de cálculo"}
1. =GPT() de GPT for Sheets es gratuito. ( ) ____________
2. Copilot en Excel puede generar gráficas a partir de "muéstrame las tendencias por mes". ( ) ____________
3. Para 1000 filas, conviene correr la fórmula =GPT() en lote, no celda por celda. ( ) ____________
4. Copilot puede convertir lenguaje natural a fórmulas Excel complejas (XLOOKUP, FILTER, etc.). ( ) ____________
::/act-tf

---

### Bloque C — Presentaciones (6.3)

::act-match{titulo="Relaciona necesidad con herramienta de slides"}
| Necesidad | Herramienta |
|---|---|
| 1. 12 slides en 5 minutos desde un Word | a) Beautiful.ai |
| 2. Slides corporativas con plantillas premium | b) PowerPoint con Designer |
| 3. Slides con diseño automático que respeta marca | c) Gamma |
| 4. Slides para presentación tradicional con animaciones complejas | d) Canva con Magic Design |
| 5. Slides con generación rápida y sin marca de IA | e) Tome |
::/act-match

::act-mcq{titulo="Trampas de las presentaciones con IA"}
1. La trampa más común al usar Gamma/Tome es:
   - [x] Aceptar contenido genérico sin revisar y entregar
   - [ ] Que se cuelgue la app
   - [ ] Que cobre extra
   - [ ] Que no tenga plantillas

2. Para presentaciones académicas formales, conviene:
   - [ ] Usar Gamma de principio a fin
   - [x] Generar borrador con Gamma y migrar a PowerPoint/Keynote para refinar
   - [ ] Solo PowerPoint manual
   - [ ] Solo Canva
::/act-mcq

---

### Bloque D — Documentos (6.4)

::act-fill{titulo="Claude Projects y Canvas en práctica"}
Para una **tesis de 6 meses**, configuras un Project con _____________ instrucciones (sistema), _____________ documentos en knowledge base (mínimo) y un _____________ para colaborar quirúrgicamente sobre el documento. La función _____________ de Claude permite editar secciones específicas sin rehacer el documento entero. Para iterar un capítulo conservando coherencia con los anteriores, le das al modelo el _____________ del capítulo anterior y le pides solo trabajar la _____________ específica.
::/act-fill

---

### Bloque E — Tareas y planeación (6.5)

::act-tf{titulo="Tareas automatizadas — V/F"}
1. Motion calendariza automáticamente tus tareas según prioridad y deadline. ( ) ____________
2. Reclaim AI protege bloques de "deep work" en tu calendario. ( ) ____________
3. Notion AI puede generar tu plan semanal con base en tus proyectos. ( ) ____________
4. Si subes muchas tareas a Motion, terminarás todas a tiempo. ( ) ____________
5. La diferencia entre Motion y Notion AI es que Motion es para tareas con tiempo y Notion AI para conocimiento + tareas. ( ) ____________
::/act-tf

::act-order{titulo="Ordena la rutina dominical de planeación con IA (10 pasos)"}
[ ] Revisa lo no completado de la semana anterior
[ ] Pasa al cierre de domingo: bloquea calendario para descanso
[ ] Carga las tareas a Motion con deadline y prioridad
[ ] Pídele a Notion AI / Claude un análisis de tu carga vs disponibilidad
[ ] Define 3 prioridades de la semana entrante
[ ] Reagenda lo pendiente con criterio (¿sigue siendo prioritario?)
[ ] Activa Reclaim para proteger 2 bloques de deep work al día
[ ] Configura recordatorios automáticos para reuniones del lunes-martes
[ ] Bloquea 30 min para Inbox Zero el lunes a primera hora
[ ] Define un "objetivo único" de la semana que justifica todo lo demás
::/act-order

---

### Bloque F — Reuniones (6.6)

::act-case{titulo="Decide herramienta de reuniones para 4 escenarios" lineas=10}
Para cada escenario, recomienda una herramienta de transcripción/resumen y justifica:

1. Reuniones internas en Microsoft Teams (empresa Microsoft 365).
2. Clases grabadas de tu universidad en Zoom.
3. Reuniones de proyecto multi-empresa donde algunos están en Google Meet, otros Zoom, otros Teams.
4. Sesiones de coaching 1:1 donde necesitas privacidad y transcripción local sin que pase por servidor externo.
::/act-case

---

## Clave de respuestas

**Bloque A — MCQ:** 1-a · 2-b · 3-c. **Fill:** relación · 100-150 · superior jerárquico (boss, profesor titular).

**Bloque B — Caso:** 1) `=GPT("Clasifica como POSITIVA, NEGATIVA o NEUTRA. Solo devuelve la palabra: " & A2)`. 2) `=GPT("Tema en 3 palabras: " & A2)` y `=GPT("Método (cuantitativo, cualitativo o mixto): " & A2)`. 3) Resumen y categoría con prompts similares; **clave**: lote y cache para no quemar tokens. **V/F:** 1-F (cuesta) · 2-V · 3-V (con caché) · 4-V.

**Bloque C — Match:** 1-c · 2-a · 3-b · 4-b · 5-d (o e). **MCQ:** 1-a · 2-b.

**Bloque D — Fill:** 200-400 palabras · 5-10 · Canvas (o Artifact) · Canvas · esqueleto/resumen · sección.

**Bloque E — V/F:** 1-V · 2-V · 3-V · 4-F (Motion no garantiza nada; tú sigues siendo el cuello de botella) · 5-V. **Order:** revisa pendiente → reagenda → 3 prioridades → carga a Motion → análisis carga vs disponibilidad → Reclaim deep work → recordatorios → Inbox Zero lunes → objetivo único → bloque descanso.

**Bloque F — Caso:** 1) Zoom/Teams Companion (nativo). 2) Otter o Read.ai. 3) Otter (cross-plataforma) o Fireflies. 4) Whisper local (open source) en tu computadora.
