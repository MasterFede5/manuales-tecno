---
unidad: 2
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 02

---

::act-mcq{titulo="Plataformas y anatomía — repaso"}
1. Un token en español equivale aproximadamente a:
   - [ ] 1 letra
   - [ ] 1 palabra completa
   - [x] 0.75 palabras (4 caracteres aprox)
   - [ ] 1 oración

2. ¿Qué plataforma tiene la ventana de contexto más grande en 2025?
   - [ ] ChatGPT GPT-5
   - [ ] Claude Opus 4.7
   - [x] Gemini 2.0 Pro (2M tokens)
   - [ ] Copilot Pro

3. ¿Qué función es **distintiva** de Claude (no presente nativamente en ChatGPT, Gemini o Copilot)?
   - [ ] Generar imágenes
   - [x] Artifacts (panel lateral con código/HTML editable)
   - [ ] Búsqueda web
   - [ ] Voz

4. Si tu trabajo está en Microsoft 365 Outlook + Excel, ¿qué plataforma te conviene priorizar?
   - [ ] ChatGPT Plus
   - [ ] Claude Pro
   - [ ] Gemini Advanced
   - [x] Microsoft Copilot

5. La causa principal por la que un LLM **alucina** (inventa hechos) es:
   - [ ] Tiene un bug
   - [x] Su entrenamiento solo le enseña a predecir tokens plausibles, no a verificar hechos
   - [ ] No tiene suficiente RAM
   - [ ] No conoce el tema

6. La fecha de corte (knowledge cutoff) significa:
   - [ ] El día que el modelo se apaga
   - [x] La fecha límite hasta la cual se entrenó con datos
   - [ ] Cuándo se actualizará la próxima vez
   - [ ] El máximo de tokens por conversación
::/act-mcq

---

::act-table{titulo="Mapa de funciones por plataforma"}
| Función | ChatGPT | Claude | Gemini | Copilot |
|---|:-:|:-:|:-:|:-:|
| Voz avanzada en tiempo real |  |  |  |  |
| Genera imágenes nativas |  |  |  |  |
| Artifacts / panel lateral |  |  |  |  |
| Projects con knowledge base |  |  |  |  |
| Integración con Office 365 |  |  |  |  |
| Integración con Google Workspace |  |  |  |  |
| Memoria persistente |  |  |  |  |
| Más de 1M tokens de contexto |  |  |  |  |

> Marca con ✓ si la función es nativa/distintiva, ✗ si no.
::/act-table

---

::act-match{titulo="Relaciona plataforma con su empresa fundadora"}
| Plataforma | Empresa |
|---|---|
| 1. ChatGPT | a) Anthropic |
| 2. Claude | b) Microsoft |
| 3. Gemini | c) OpenAI |
| 4. Copilot | d) Google DeepMind |
::/act-match

---

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Las cuatro plataformas (ChatGPT, Claude, Gemini, Copilot) usan el mismo modelo base GPT-4. ( ) ____________________________________________
2. Microsoft Copilot por debajo usa principalmente modelos de OpenAI. ( ) ____________________________________________
3. Tener mayor ventana de contexto siempre da mejores respuestas. ( ) ____________________________________________
4. La memoria persistente entre chats está activada por defecto en ChatGPT. ( ) ____________________________________________
5. Los LLMs no pueden alucinar si les pides que "no inventen". ( ) ____________________________________________
6. Gemini en Google Workspace puede leer mis correos y archivos del Drive automáticamente, sin permiso adicional. ( ) ____________________________________________
::/act-tf

---

::act-fill{titulo="Completa con los términos correctos"}
La unidad mínima de texto que procesa un LLM se llama _____________. Una palabra en español equivale a aproximadamente _____________ tokens. La cantidad máxima de tokens que un modelo procesa en una sola interacción se llama _____________. Los modelos sufren un fenómeno llamado _____________ que les hace prestar menos atención al medio del contexto largo.

Las tres limitaciones fundamentales de cualquier LLM son: _____________ (inventar hechos), _____________ (reflejar prejuicios del corpus) y _____________ (no saber eventos posteriores al entrenamiento).
::/act-fill

---

::act-order{titulo="Ordena las fases de procesamiento de un mensaje"}
[ ] El usuario escribe el mensaje
[ ] El texto se tokeniza en sub-palabras
[ ] Los tokens entran al modelo Transformer
[ ] El modelo predice tokens de salida uno a uno
[ ] La interfaz muestra la respuesta al usuario
[ ] El sistema acumula la conversación en la ventana de contexto
::/act-order

---

::albatros{titulo="El reto del prompt idéntico — comparativa real" tipo="experimento" tiempo="60 min"}
**Pregunta detonadora.** Si los cuatro modelos están entrenados con texto similar, ¿por qué dan respuestas tan distintas al mismo prompt?

**Lo que harás.**
1. Abre **simultáneamente** las 4 plataformas (ChatGPT, Claude, Gemini, Copilot) en pestañas distintas.
2. Aplica **el mismo prompt** de la práctica resuelta (Bernoulli + alerón F1) en las 4.
3. **Captura** las 4 respuestas en una tabla (puede ser en Notion, Google Doc, o Excel).
4. Calíficalas con la rúbrica de 6 criterios (claridad, analogía, ejemplo numérico, pregunta, recomendación, tono).
5. Repite el experimento con un **segundo prompt** muy distinto: "Hazme un plan de estudio semanal de 20 horas para preparar examen de admisión a UNAM CCH".
6. Compara: ¿gana el mismo modelo en ambos casos? ¿Por qué sí o no?
7. Decide cuál será tu **base**.

**Materiales.** Acceso a las 4 plataformas (versiones Free son suficientes) · 60 min · hoja de cálculo o Notion para tabular.

**Entregable.** Reporte de 1-2 páginas con: a) tabla comparativa de los dos prompts × 4 plataformas × 6 criterios, b) decisión justificada de tu base, c) 3 patrones que observaste en las diferencias entre plataformas, d) capturas de pantalla de las 4 respuestas más interesantes.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cobertura | 1 plataforma | 3 plataformas | 4 plataformas, 2 prompts |
| Análisis cualitativo | "me gustó X" | identifica patrones | discute fortalezas por caso de uso |
| Decisión justificada | sin justificar | menciona criterios | argumenta con datos y necesidades |
::/albatros

---

::act-case{titulo="Tres conversaciones, una decisión" lineas=12}
Tu hermana mayor te pide consejo: tiene Pro de Office (Copilot incluido) por la universidad, pero también puede pagar Claude Pro. Ella escribe muchos ensayos largos para Derecho, vive 80% del día en Word/Outlook, y necesita coherencia de voz. ¿Le recomiendas mantener solo Copilot o agregar Claude Pro?

Argumenta con: a) las funciones distintivas de cada plataforma; b) en qué tareas brillaría cada una; c) costo total mensual; d) qué le sugieres como flujo de trabajo combinado. Cierra con un párrafo de "qué pasa si solo puede pagar uno".
::/act-case

---

::act-mindmap{titulo="Mapa mental — Plataformas conversacionales 2025" centro="LLMs CONVERSACIONALES" nodos_primarios=4 nodos_secundarios=16}
Genera 4 nodos primarios (uno por plataforma) y 4 secundarios por cada uno: empresa, modelo base 2025, ventana de contexto, función distintiva.
::/act-mindmap

---

::act-label{titulo="Etiqueta el flujo de procesamiento de tu mensaje"}

> Etiqueta cada caja del flujo y anota debajo qué tipo de problema ocurre en cada paso.
::/act-label


::visual{tipo="diagrama-flujo" descripcion="Diagrama de flujo de izquierda a derecha con 6 cajas vacías que muestran cómo viaja un mensaje desde el usuario hasta la respuesta. El estudiante debe etiquetar cada caja: 1) usuario escribe, 2) tokenización, 3) entrada al modelo Transformer, 4) cálculo de attention, 5) predicción token a token, 6) detokenización y respuesta. Debajo de cada caja, una línea para anotar 'qué falla aquí': el estudiante identifica en qué paso ocurren las alucinaciones, cortes por contexto, lentitud, etc." paginas="0.5" src="../manualesGem/assets/visuales/manual-3/u02/90-actividades-v01.svg"}
---

::act-puzzle{titulo="Sopa de letras — términos clave de plataformas" tipo="sopa-letras" tamano="14x14"}
Encuentra 14 términos: TOKEN · CONTEXTO · ARTIFACTS · PROJECTS · GEMS · COPILOT · CLAUDE · GEMINI · CHATGPT · ALUCINACION · CUTOFF · MEMORIA · TRANSFORMER · WORKSPACE.

Tras encontrarlas, escribe en la parte de abajo una frase que conecte 4 de los términos.
::/act-puzzle

---

::albatros{titulo="Reto del PDF gigante — quién aguanta el contexto" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** Si tienes que estudiar un libro de 600 páginas y tu profesor te toma examen mañana, ¿cuál plataforma te lee y resume todo sin perder detalles del medio?

**Lo que harás.**
1. **Consigue un PDF largo** (libro de texto, manual, ley) de al menos 200 páginas. Si no tienes, descarga uno público (Project Gutenberg, gob.mx, OpenStax).
2. **Súbelo** a las plataformas que soporten upload con contexto largo: Claude (200K-1M), ChatGPT con Projects, Gemini Advanced (2M), NotebookLM (limit alto).
3. **Haz 3 preguntas estratégicas:** una sobre el inicio, una sobre el medio (~página 300), una sobre el final.
4. **Verifica**: ¿la plataforma cita la página correcta? ¿inventa contenido del medio (lost-in-the-middle)?
5. **Compara** quién aguantó mejor y quién falló silenciosamente.

**Materiales.** PDF de 200+ páginas, acceso a 3-4 plataformas con contexto largo.

**Entregable.** Tabla con 4 plataformas × 3 preguntas × veredicto (correcto / parcial / inventó) + reflexión sobre el "lost-in-the-middle".

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cobertura | 2 plataformas | 3 plataformas | 4 plataformas |
| Detección de fallos | "respondió bien" | nota un fallo | identifica lost-in-the-middle |
| Recomendación | genérica | con criterio | con condiciones de uso |
::/albatros
