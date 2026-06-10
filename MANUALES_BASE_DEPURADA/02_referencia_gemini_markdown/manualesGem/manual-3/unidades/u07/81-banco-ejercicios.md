---
unidad: 7
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 07

> Banco de práctica para el diseño de GPTs personalizados, Gems, Claude Projects con instrucciones y agentes simples. Privilegia ejercicios de **redacción de instrucciones**, **decisión de plataforma** y **diseño de knowledge base**. Resuelve antes de mirar la clave.

---

### Bloque A — GPTs personalizados (7.1)

::act-mcq{titulo="Anatomía de un GPT custom"}
1. El componente que MÁS define la "personalidad" de un GPT es:
   - [ ] El nombre
   - [x] Las instructions (system prompt)
   - [ ] El avatar
   - [ ] Los conversation starters

2. Si quieres que tu GPT consulte tus PDFs antes de cada respuesta, configuras:
   - [ ] Web Browsing
   - [x] Knowledge files (con instrucción explícita de consultarlas)
   - [ ] Code Interpreter
   - [ ] Actions

3. Las "Actions" en un GPT permiten:
   - [ ] Editar texto
   - [ ] Generar imágenes
   - [x] Llamar APIs externas (con OpenAPI schema)
   - [ ] Búsqueda web
::/act-mcq

::act-fill{titulo="Redacta las instructions de tu primer GPT"}
Tu GPT se llama "Tutor Cálculo Albatros". Redacta sus instructions en 5 secciones:

1. **Identidad** (50 palabras): _____________________________________________
2. **Audiencia** (30 palabras): _____________________________________________
3. **Estilo de respuesta** (50 palabras): __________________________________
4. **Restricciones / lo prohibido** (50 palabras): _________________________
5. **Comportamiento ante incertidumbre** (50 palabras): ____________________
::/act-fill

::act-tf{titulo="V/F sobre GPTs"}
1. Un GPT publicado al "GPT Store" me da revenue share automático. ( ) ____________
2. Los archivos cargados como knowledge son privados (otros usuarios no los ven). ( ) ____________
3. Las instructions de un GPT pueden ser revertidas/leídas por usuarios curiosos con prompts de jailbreak. ( ) ____________
4. Los GPTs solo funcionan dentro de ChatGPT Plus/Pro. ( ) ____________
5. Puedo dar a mi GPT capability de "Web Browsing + Code Interpreter + DALL·E" simultáneamente. ( ) ____________
::/act-tf

---

### Bloque B — Gems de Gemini (7.2)

::act-match{titulo="Compara Gems vs GPTs"}
| Característica | Gem (Google) | GPT (OpenAI) |
|---|---|---|
| 1. Empresa | a) Google | b) OpenAI |
| 2. Necesita plan | c) Gemini Advanced | d) ChatGPT Plus/Pro |
| 3. Distribución | e) Privada o link directo | f) GPT Store público |
| 4. Knowledge | g) Sí, con archivos | h) Sí, hasta 20 archivos |
| 5. Web nativa | i) Sí (Google Search) | j) Sí (Bing) |
::/act-match

---

### Bloque C — Claude Projects (7.3)

::act-mcq{titulo="Cuándo Project bate a GPT"}
1. Para una **tesis de 6 meses** con knowledge base que crece, prefieres:
   - [ ] GPT custom
   - [x] Claude Project (mejor con contexto largo y memoria de proyecto)
   - [ ] Gem
   - [ ] Copilot Studio

2. Para **distribución pública a 10 000 usuarios anónimos**, NO eliges:
   - [ ] GPT Store
   - [x] Claude Project (no es público; orientado a colaboración privada)
   - [ ] Copilot Studio (con plan empresarial)
   - [ ] Despliegue de chatbot custom con API
::/act-mcq

::act-fill{titulo="Estructura de Claude Project para tesis"}
Para tu tesis de 6 meses, configuras un Claude Project con: a) **Project knowledge**: _____________ (mín. 8 archivos: tu propuesta, tu temario, tus apuntes, papers leídos, ejemplos de tesis exitosas previas), b) **Custom instructions**: _____________ palabras describiendo tu objetivo, voz, restricciones, c) **Estilo personalizado** ("style") con _____________ ejemplos de tu redacción anterior. La función _____________ (panel lateral editable) permite refinar capítulos sin romper coherencia.
::/act-fill

---

### Bloque D — Copilot Studio (7.4)

::act-tf{titulo="Copilot Studio en práctica"}
1. Copilot Studio está orientado a empresas con Microsoft 365. ( ) ____________
2. Copilot Studio permite flujos visuales tipo flowchart con triggers y acciones. ( ) ____________
3. Es tan barato como GPT Plus. ( ) ____________
4. Puede conectarse a Power Automate y Dataverse. ( ) ____________
5. Es la mejor opción para un proyecto personal de tutor IA. ( ) ____________
::/act-tf

---

### Bloque E — Casos de uso (7.5)

::act-case{titulo="Decide la plataforma para 5 proyectos" lineas=12}
Para cada proyecto, recomienda plataforma (GPT custom, Gem, Claude Project, Copilot Studio o app custom con API) y justifica:

1. Tu tutor IA personal de Cálculo, solo para ti.
2. Un asistente de marca para una pyme familiar (responde preguntas de catálogo a clientes en WhatsApp).
3. Un coach de hábitos que monitoree tu calendario y te empuje al gym 3x semana.
4. Un GPT educativo público que explique IA para bachillerato (audiencia 10 000+).
5. Un agente que automatice respuestas a correos en una empresa que vive en Outlook + Teams.
::/act-case

::act-order{titulo="Ordena los pasos para construir tu primer GPT custom"}
[ ] Decide audiencia, caso de uso, distribución
[ ] Reúne y organiza tus 8-15 archivos de knowledge
[ ] Redacta instructions de 400-600 palabras
[ ] Configura el GPT builder con todo lo anterior
[ ] Activa capabilities apropiadas (no todas)
[ ] Diseña 4 conversation starters representativos
[ ] Prueba con 7+ prompts diversos
[ ] Itera instructions con base en resultados
[ ] Publica con visibilidad apropiada
[ ] Recolecta feedback durante 1 semana
::/act-order

---

## Clave de respuestas

**Bloque A — MCQ:** 1-b · 2-b · 3-c. **Fill (ejemplo válido):** 1) Identidad: "Soy 'Tutor Cálculo Albatros', tu compañero de cálculo I orientado a comprensión geométrica antes que algebraica..." · 2) Audiencia: "Estudiantes de bachillerato CCH-UNAM en su 4-5to semestre, sin background técnico previo..." · 3) Estilo: "Empiezo con intuición visual, luego fórmula, luego ejemplo numérico, luego pregunta socrática..." · 4) Restricciones: "Nunca doy la respuesta directa antes de pedir el intento del estudiante..." · 5) Incertidumbre: "Si la pregunta sale del temario o no está en mi knowledge, lo digo explícitamente...". **V/F:** 1-V (con condiciones, requiere validación de identidad) · 2-V · 3-V (sí, hay riesgo) · 4-V · 5-V.

**Bloque B — Match:** 1-a/b · 2-c/d · 3-e/f · 4-g/h · 5-i/j (cada Gem/GPT con su par).

**Bloque C — MCQ:** 1-b · 2-b. **Fill:** Project knowledge · 200-400 · 2-3 · Canvas/Artifacts.

**Bloque D — V/F:** 1-V · 2-V · 3-F (cuesta más, plan empresarial) · 4-V · 5-F (sobreingeniería para uso personal).

**Bloque E — Caso:** 1) Claude Project (privado, contexto largo, memoria). 2) GPT custom o app con API + WhatsApp Business (clientes externos). 3) GPT custom + Actions a Calendar/Reclaim. 4) GPT en GPT Store (distribución pública). 5) Copilot Studio (M365 nativo). **Order:** decide audiencia → knowledge → instructions → builder → capabilities → starters → pruebas → itera → publica → feedback.
