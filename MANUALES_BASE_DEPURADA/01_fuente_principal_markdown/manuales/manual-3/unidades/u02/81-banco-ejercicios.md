---
unidad: 2
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 02

> Banco extendido para reforzar el dominio de las 4 plataformas (ChatGPT, Claude, Gemini, Copilot).
> - Privilegia **redacción de prompts**.
> - Enfatiza **comparación de respuestas**.
> - Fomenta **detección de limitaciones**.
> 
> *Resuelve antes de mirar la clave.*

::interioriza
Imagina que estas 4 plataformas son herramientas de un taller mecánico:
- **ChatGPT:** El taladro multiusos (versátil y potente).
- **Claude:** El torno de precisión (ideal para textos largos y código).
- **Gemini:** La caja conectada a internet (rápida e integrada a tu Drive).
- **Copilot:** El asistente que ya vive en tu oficina (inserto en Word/Excel).
::/interioriza

::pausa{}
Antes de empezar a resolver: ¿Qué plataforma abrirías primero si te piden resumir un PDF de 200 páginas, y cuál si te piden analizar un Excel de ventas?
::/pausa

---

### Bloque A — Anatomía del chat (2.1)

::act-fill{titulo="Tokens, contexto y memoria"}
Un _____________ es la unidad mínima de texto que procesa un LLM. En español, una palabra promedio equivale a aproximadamente _____________ tokens. La cantidad máxima de tokens que un modelo procesa en una sola interacción se llama _____________. Cuando el contexto es muy largo, el modelo sufre el fenómeno _____________ que reduce la atención al medio del texto. La _____________ es la capacidad del modelo de recordar información de chats anteriores, y en ChatGPT se activa desde _____________.
::/act-fill

::act-mcq{titulo="Tokens y contexto — selecciona la mejor respuesta"}
1. Si pegas un PDF de 80 páginas en un chat con ventana de 200K tokens, en realidad estás usando aproximadamente:
   - [ ] 5K tokens
   - [x] 30-50K tokens (depende de la densidad)
   - [ ] 200K tokens completos
   - [ ] El modelo lo comprime automáticamente

2. ¿Por qué un modelo con 2M tokens de contexto **no siempre** da mejores respuestas que uno con 200K?
   - [ ] Porque cobra más caro
   - [x] Por el "lost in the middle": el modelo presta menos atención al medio del contexto extenso
   - [ ] Porque procesa más lento
   - [ ] Porque las dos primeras razones son incorrectas
::/act-mcq

---

### Bloque B — ChatGPT (2.2)

::act-case{titulo="Decide qué modelo de ChatGPT usar para cada tarea" lineas=10}
Para cada tarea, indica qué modelo o función de ChatGPT (GPT-4o, GPT-5, modo voz, modo razonamiento o1/o3, GPTs personalizados) elegirías y por qué:

1. Resumir 50 PDFs académicos para un trabajo de revisión bibliográfica.
2. Tener una conversación en inglés mientras caminas para practicar pronunciación.
3. Resolver un problema lógico complejo de olimpiada de matemáticas.
4. Crear un asistente recurrente para tu materia de Cálculo I que responda con un estilo específico.
5. Generar 6 ideas creativas para un post de Instagram sobre cuidado del agua.
::/act-case

---

### Bloque C — Claude (2.3)

::act-tf{titulo="Funciones distintivas de Claude"}
1. Los Artifacts de Claude permiten editar HTML/código en un panel lateral. ( ) ____________
2. Los Projects de Claude tienen knowledge base persistente que el modelo consulta automáticamente. ( ) ____________
3. Claude tiene generación nativa de imágenes (sin llamar a otro modelo). ( ) ____________
4. Los Estilos de Claude permiten replicar un tono de redacción a partir de ejemplos. ( ) ____________
5. Claude Opus tiene una ventana de contexto mayor que Gemini Pro. ( ) ____________
::/act-tf

::act-mcq{titulo="Cuándo brilla Claude"}
1. Si tu tarea es **redactar un ensayo largo manteniendo coherencia de estilo y voz**, la plataforma que mejor escala es:
   - [ ] ChatGPT 5 free
   - [x] Claude (por sus Estilos y consistencia de voz)
   - [ ] Gemini 2.0 Flash
   - [ ] Copilot Office

2. Para iterar **HTML/CSS/JS visualmente y verlo renderizar en vivo** sin cambiar de pestaña, el flujo más fluido es:
   - [ ] ChatGPT con bloques de código copiados
   - [x] Claude Artifacts
   - [ ] Gemini con extensiones
   - [ ] Copilot con Visual Studio Code
::/act-mcq

---

### Bloque D — Gemini con Workspace (2.4)

::act-fill{titulo="Gemini en Google Workspace"}
Gemini se integra nativamente en _____________ (5 apps de Google Workspace): _____________, _____________, _____________, _____________ y _____________. La función "Help me write" aparece en _____________ y _____________. Para que Gemini pueda leer un Drive, debes activar la integración desde _____________. La diferencia clave entre Gemini Free y Gemini Advanced es _____________ y el acceso al modelo _____________.
::/act-fill

---

### Bloque E — Copilot con Office (2.5)

::act-match{titulo="Función Copilot por aplicación de Office"}
| Aplicación | Función Copilot distintiva |
|---|---|
| 1. Excel | a) Genera presentaciones desde un Word |
| 2. PowerPoint | b) Resume hilos de correo y propone respuestas |
| 3. Outlook | c) Crea fórmulas, gráficas y análisis desde lenguaje natural |
| 4. Teams | d) Resume reuniones en vivo y extrae action items |
| 5. Word | e) Reescribe párrafos con tono ejecutivo |
::/act-match

---

### Bloque F — Comparativa práctica (2.6)

::act-case{titulo="Elige plataforma para 6 escenarios reales" lineas=12}
Para cada escenario, recomienda 1 plataforma primaria y 1 secundaria. Justifica con criterio (no opinión):

1. Estudiante de bachillerato que escribe ensayos largos y necesita coherencia de estilo.
2. Equipo de ventas en una PYME que vive en Outlook + Excel + Teams.
3. Investigador que quiere hacer revisión bibliográfica con citaciones reales.
4. Diseñador que necesita iterar HTML/CSS rápido para mockups.
5. Estudiante de medicina que estudia con PDFs largos (más de 500 páginas).
6. Creador de contenido que necesita ideas de copy + imágenes + voz.
::/act-case

::act-mcq{titulo="Comparativa relámpago"}
1. Para "investigador que quiere bibliografía con citaciones reales" la mejor opción **fuera** de las 4 plataformas grandes es:
   - [ ] Replit Ghostwriter
   - [x] Perplexity
   - [ ] Pi.ai
   - [ ] Character.ai

2. Para **ventana de contexto más grande** entre las 4 grandes (2025) gana:
   - [ ] ChatGPT 5
   - [ ] Claude Opus 4.7 (estándar)
   - [x] Gemini 2.0 Pro (2M tokens)
   - [ ] Copilot Pro
::/act-mcq

---

### Bloque G — Limitaciones (2.7)

::act-tf{titulo="Mitos sobre limitaciones de los LLMs"}
1. Si pongo "no inventes hechos" en mi prompt, el modelo deja de alucinar. ( ) ____________
2. Las alucinaciones ocurren más cuando el modelo no tiene información sobre el tema. ( ) ____________
3. Los sesgos de un LLM se eliminan completamente con RLHF. ( ) ____________
4. Después de la fecha de corte, el modelo no tiene NINGÚN dato más reciente, ni con búsqueda web. ( ) ____________
5. Si dos modelos coinciden en una respuesta, esa respuesta es correcta. ( ) ____________
::/act-tf

::act-order{titulo="Ordena los pasos para detectar una alucinación"}
[ ] Identifica una afirmación específica y verificable (nombre, fecha, cifra)
[ ] Pídele al modelo la fuente exacta
[ ] Verifica la fuente en su sitio oficial (no confíes solo en el link)
[ ] Si la fuente no existe o no dice eso, marca como alucinación
[ ] Confronta al modelo con el resultado y observa cómo reacciona
[ ] Documenta el patrón para futuras consultas similares
::/act-order

---

## Clave de respuestas

**Bloque A — Fill:** token · 1.3 (o 1.3-1.5) · ventana de contexto · lost-in-the-middle · memoria persistente · Settings/Personalization. **MCQ:** 1-b · 2-b.

**Bloque B — Caso:** 1) ChatGPT con Projects o Claude (mejor para volumen de PDFs por contexto largo). 2) Modo voz avanzado (real-time). 3) Modo razonamiento (o1, o3 o GPT-5 thinking). 4) GPT personalizado. 5) GPT-4o estándar (rapidez creativa).

**Bloque C — V/F:** 1-V · 2-V · 3-F (Claude usa modelos externos para imagen, no genera nativamente) · 4-V · 5-V (Opus 4.7 estándar 200K, Gemini 2.0 Pro tiene 2M, **error en mi pregunta**: F real). Aclaración: F · gemini Pro tiene mayor contexto. **MCQ:** 1-b · 2-b.

**Bloque D — Fill:** Workspace · Gmail · Docs · Sheets · Slides · Meet · Docs y Gmail · Workspace Admin (o Settings de la cuenta) · ventana de contexto y prioridad · Gemini Ultra/Pro (versión avanzada).

**Bloque E — Match:** 1-c · 2-a · 3-b · 4-d · 5-e.

**Bloque F — Caso:** 1) Claude (estilos) + ChatGPT. 2) Copilot (Office nativo) + Gemini si usan Workspace. 3) Perplexity + Claude/ChatGPT para síntesis. 4) Claude Artifacts + Cursor para producción. 5) Claude por contexto largo + NotebookLM. 6) ChatGPT + Midjourney + ElevenLabs. **MCQ:** 1-b · 2-c.

**Bloque G — V/F:** 1-F (reduces frecuencia pero no eliminas) · 2-V · 3-F (mitiga pero no elimina) · 4-F (con búsqueda web sí accede a datos posteriores) · 5-F (pueden coincidir en una alucinación si comparten sesgo del corpus). **Order:** identifica afirmación → pide fuente → verifica fuente → marca → confronta → documenta.
