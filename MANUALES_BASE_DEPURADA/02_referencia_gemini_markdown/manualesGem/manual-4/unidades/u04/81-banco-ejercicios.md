---
unidad: 4
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 04

> Trabajas con NotebookLM y Claude.ai abiertos. Tienes 5-8 PDFs institucionales reales (o usa los del repo del manual si tu institución no te los facilita).

### Sección A — Concepto y embeddings (4.1 y 4.2)

::act-fill{titulo="A1. La fórmula mental de RAG"}
RAG = ____________ + ____________. El proceso de **indexar** ocurre en _____________ y consiste en partir el documento en _____________, generar para cada uno un _____________ (lista de números) y guardarlos en un ____________ store. El proceso de **consultar** ocurre en tiempo real: la pregunta del usuario se convierte en _____________, se busca por _____________ ____________, se recuperan top-k _____________, se construye un _____________ _____________ con esos chunks, y el LLM produce respuesta _____________ con _____________.
::/act-fill

::act-mcq{titulo="A2. Tradeoffs de RAG"}
1. La métrica de similitud coseno entre la pregunta y un chunk vale 0.45. Esto significa:
   - [ ] Idéntico
   - [x] Temáticamente cerca, riesgo de ruido — revisar
   - [ ] Opuesto
   - [ ] Error de cálculo

2. RAG **no** elimina alucinaciones. La instrucción más eficaz para reducirlas:
   - [ ] Subir top-k a 50
   - [x] "Si no encuentras la respuesta en los fragmentos, responde 'no tengo información'"
   - [ ] Bajar temperatura a 0
   - [ ] Cambiar de modelo

3. Si indexas con embeddings de OpenAI y consultas convirtiendo la pregunta con embeddings de Cohere:
   - [ ] Funciona si ambos son multilingual
   - [x] No funciona — los espacios vectoriales son incompatibles
   - [ ] Funciona con factor de corrección
   - [ ] Funciona solo en inglés
::/act-mcq

::act-tf{titulo="A3. Mitos sobre RAG"}
1. RAG es siempre mejor que fine-tuning. ( ) ____________________________________________
2. Un chunk demasiado grande (>2000 tokens) mejora la precisión. ( ) ____________________________________________
3. Los metadatos del chunk (archivo, página, sección) no afectan calidad si el embedder es bueno. ( ) ____________________________________________
4. Fine-tuning con 50 ejemplos suele dar buenos resultados. ( ) ____________________________________________
::/act-tf

### Sección B — Sin código vs no-code vs code (4.3 y 4.4)

::act-match{titulo="B1. Necesidad → herramienta"}
| Necesidad | Herramienta recomendada |
|---|---|
| 1. Distribuir un chatbot público con tu reglamento | a) Claude Projects |
| 2. Audio overview del manual del docente | b) Dify |
| 3. Razonamiento profundo combinando 3 documentos | c) NotebookLM |
| 4. Pipeline RAG con Cohere multilingual y re-ranking | d) Stack AI |
| 5. Integraciones empresariales (Salesforce, SharePoint) | e) Flowise |
| 6. Self-hosted con drag-and-drop, sin SaaS | f) Custom GPT |
::/act-match

::act-table{titulo="B2. Comparativa de plataformas (RAG sin/poco código)"}
| Plataforma | Login del usuario final | Citas con superíndice | Audio overview | Multi-doc retrieval | Costo gratis | API propia |
|---|---|---|---|---|---|---|
| NotebookLM |  |  |  |  |  |  |
| Claude Projects |  |  |  |  |  |  |
| Custom GPT |  |  |  |  |  |  |
| Dify |  |  |  |  |  |  |
| Flowise |  |  |  |  |  |  |
| Stack AI |  |  |  |  |  |  |
::/act-table

### Sección C — Chunking, metadatos, citado (4.5)

::act-order{titulo="C1. Pipeline de indexación"}
[ ] Validar texto seleccionable (no escaneo)
[ ] Aplicar OCR si es escaneo
[ ] Convención de nombres y metadatos por archivo
[ ] Chunkear con tamaño y overlap definidos
[ ] Generar embeddings por chunk
[ ] Almacenar en vector store con metadatos
[ ] Lanzar smoke test con 3 preguntas conocidas
::/act-order

::act-fill{titulo="C2. Tamaños de chunk típicos"}
Para un reglamento de 35 páginas con artículos numerados, un chunking razonable es **chunks de** _____________ _____________ con **overlap** de _____________ _____________ y **metadatos** que viajan con cada chunk: _____________, _____________, _____________ y _____________ _____________. Si los chunks son demasiado grandes, _____________ la relevancia; si son demasiado chicos, _____________ el contexto.
::/act-fill

::act-case{titulo="C3. Caso — diseña el chunking de tu reglamento" lineas=10}
Tu reglamento tiene 12 capítulos, 87 artículos, 4 fracciones promedio por artículo. La pregunta típica del usuario referencia un artículo concreto. Diseña tu estrategia de chunking: ¿chunkeas por artículo, por fracción, por página, por capítulo? ¿Qué overlap? ¿Qué metadatos? Justifica con el caso de uso real.
::/act-case

### Sección D — RAG vs fine-tuning (4.6)

::act-mcq{titulo="D1. Cuándo cada enfoque"}
1. Necesitas que tu Asistente conozca el contenido específico del reglamento 2026.
   - [x] RAG
   - [ ] Fine-tuning
   - [ ] Ambos
   - [ ] Ninguno

2. Necesitas que tu Asistente adopte un tono institucional muy específico imposible de capturar con prompts.
   - [ ] RAG
   - [x] Fine-tuning
   - [ ] Ambos
   - [ ] Ninguno

3. El reglamento cambia cada semestre.
   - [x] RAG (re-indexar es barato; fine-tuning costaría re-entrenar cada cambio)
   - [ ] Fine-tuning
   - [ ] Ambos
   - [ ] Ninguno

4. El presupuesto es $0 y el equipo no tiene ML engineer.
   - [x] RAG con NotebookLM o Claude Projects
   - [ ] Fine-tuning
   - [ ] Custom training
   - [ ] No hacer nada
::/act-mcq

::act-tf{titulo="D2. Mitos del fine-tuning"}
1. Fine-tuning hace que el modelo "sepa" tus datos para siempre. ( ) ____________________________________________
2. Si tu RAG es bueno, fine-tuning no aporta nada. ( ) ____________________________________________
3. Fine-tuning + RAG en el mismo modelo es siempre mejor que solo RAG. ( ) ____________________________________________
::/act-tf

### Sección E — Caso integrador

::act-case{titulo="E1. Caso — golden set y mitigación de alucinaciones" lineas=14}
Lanzas tu RAG NotebookLM con 8 documentos. Construyes un golden de 12 preguntas. Resultados: 9/12 correctas con cita, 1 alucinación grave (inventó artículo del reglamento), 2 con "no tengo info" donde debería haber sabido. Diseña el plan de remediación: ¿qué cambias en chunking, instrucciones del notebook, herramienta, o golden? Lista 3 acciones priorizadas.
::/act-case

::act-mindmap{titulo="E2. Tu sistema RAG institucional" centro="RAG ALBATROS v1.0" nodos_primarios=6 nodos_secundarios=12}
Las 6 ramas: (1) base documental, (2) herramienta principal, (3) golden set y resultados, (4) instrucciones anti-alucinación, (5) plan de mejora v1.1, (6) distribución a usuarios. Cada secundario con un dato concreto.
::/act-mindmap

---

## Clave de respuestas

**A1.** Recuperación + Generación · offline · chunks · embedding · vector · embedding · similitud (semántica) · chunks · prompt aumentado · contextualizada · citas.

**A2.** 1-b · 2-b · 3-b.

**A3.** 1) Falso — RAG cuesta menos para conocimiento, fine-tuning gana en tono/estilo profundo. 2) Falso — un chunk demasiado grande diluye relevancia y aumenta costo. 3) Falso — sin metadatos no puedes citar página o artículo, y filtros pre-búsqueda son imposibles. 4) Falso — fine-tuning suele requerir 500-5000 ejemplos para resultados confiables.

**B1.** 1-f · 2-c · 3-a · 4-b · 5-d · 6-e.

**B2.** Sugerencia (acepta variantes razonables y verifica contra estado actual de cada producto):
| Plataforma | Login | Citas | Audio | Multi-doc | Free tier | API |
|---|---|---|---|---|---|---|
| NotebookLM | Google | sí | sí | sí | sí | no |
| Claude Projects | Anthropic | parcial | no | sí | con plan | con plan |
| Custom GPT | ChatGPT | parcial | no | sí | con plan | sí |
| Dify | varía | sí | no | sí | self-host | sí |
| Flowise | varía | sí | no | sí | self-host | sí |
| Stack AI | enterprise | sí | no | sí | trial | sí |

**C1.** Orden: Validar texto seleccionable → OCR si escaneo → Convención de nombres y metadatos → Chunkear → Generar embeddings → Almacenar en vector store → Smoke test 3 preguntas.

**C2.** Sugerencia: chunks de **400-800 tokens** · overlap **50-100 tokens** · metadatos: **archivo, capítulo, artículo, página**. Demasiado grandes: **diluyen** la relevancia; demasiado chicos: **pierden** el contexto.

**C3.** Respuesta libre. Buena respuesta: chunk por **artículo** con metadatos `{archivo, capítulo, articulo, fracciones[]}` + overlap mínimo (50 tokens) porque cada artículo es semánticamente autocontenido. Capítulos son demasiado grandes (>2k tokens). Fracciones son demasiado chicas si la pregunta cruza fracciones del mismo artículo.

**D1.** 1-a · 2-b · 3-a · 4-a.

**D2.** 1) Falso — fine-tuning entrena estilo y patrones, no garantiza recall confiable de hechos específicos. 2) Falso — fine-tuning aporta tono/voz que prompts no capturan; RAG aporta hechos. 3) Falso — fine-tuning + RAG es válido pero suma costo y complejidad; muchas veces RAG solo basta.

**E1.** Plan razonable: (a) **mitigar alucinación grave** — endurecer instrucciones del notebook con "si no encuentras cita textual, responde 'no tengo información'" y reproducir la pregunta para verificar; (b) **mejorar las 2 con 'no tengo info'** — diagnosticar si fue chunking o nombrado: revisa los chunks recuperados, si la respuesta está en el documento pero no se recuperó, ajustar chunk size/overlap o agregar sinónimos en instrucciones; (c) **ampliar golden a 30** antes de declarar v1.1 lista.

**E2.** Mapa libre. Si una rama no tiene dato concreto, indica brecha real en tu sistema.
