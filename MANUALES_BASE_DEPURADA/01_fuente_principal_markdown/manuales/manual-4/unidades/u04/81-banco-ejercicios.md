---
unidad: 4
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 04

> - Trabaja con NotebookLM y Claude.ai abiertos.
> - Usa 5-8 PDFs institucionales reales.
> - (O usa los del repositorio del manual).

::interioriza
Piensa en RAG como un estudiante a libro abierto. El *banco de ejercicios* es tu oportunidad para probar si el estudiante sabe en qué página buscar antes de responder.
::/interioriza

### Sección A — Concepto y embeddings (4.1 y 4.2)

::act-fill{titulo="A1. La fórmula mental de RAG"}
RAG = ____________ + ____________. 
El proceso de **indexar** ocurre en _____________ y consiste en:
- Partir el documento en _____________.
- Generar para cada uno un _____________ (lista de números).
- Guardarlos en un ____________ store. 
El proceso de **consultar** ocurre en tiempo real: 
- La pregunta se convierte en _____________.
- Se busca por _____________ ____________.
- Se recuperan top-k _____________.
- Se construye un _____________ _____________ con ellos.
- El LLM produce respuesta _____________ con _____________.
::/act-fill

::act-mcq{titulo="A2. Tradeoffs de RAG"}
1. La métrica de similitud coseno entre pregunta y chunk vale 0.45. Esto significa:
   - [ ] Idéntico
   - [x] Temáticamente cerca, riesgo de ruido — revisar
   - [ ] Opuesto
   - [ ] Error de cálculo

2. RAG **no** elimina alucinaciones. La instrucción más eficaz:
   - [ ] Subir top-k a 50
   - [x] "Si no encuentras la respuesta, di 'no tengo información'"
   - [ ] Bajar temperatura a 0
   - [ ] Cambiar de modelo

3. Indexas con OpenAI y consultas convirtiendo pregunta con Cohere:
   - [ ] Funciona si ambos son multilingual
   - [x] No funciona — espacios vectoriales incompatibles
   - [ ] Funciona con factor de corrección
   - [ ] Funciona solo en inglés
::/act-mcq

::act-tf{titulo="A3. Mitos sobre RAG"}
1. RAG es siempre mejor que fine-tuning. ( ) ____________________________________________
2. Un chunk demasiado grande (>2000 tokens) mejora la precisión. ( ) ____________________________________________
3. Los metadatos del chunk no afectan calidad si el embedder es bueno. ( ) ____________________________________________
4. Fine-tuning con 50 ejemplos suele dar buenos resultados. ( ) ____________________________________________
::/act-tf

### Sección B — Sin código vs no-code vs code (4.3 y 4.4)

::act-match{titulo="B1. Necesidad → herramienta"}
| Necesidad | Herramienta recomendada |
|---|---|
| 1. Distribuir chatbot público con reglamento | a) Claude Projects |
| 2. Audio overview del manual docente | b) Dify |
| 3. Razonamiento profundo combinando 3 PDFs | c) NotebookLM |
| 4. Pipeline RAG Cohere multilingual + re-ranking | d) Stack AI |
| 5. Integraciones (Salesforce, SharePoint) | e) Flowise |
| 6. Self-hosted drag-and-drop, sin SaaS | f) Custom GPT |
::/act-match

::act-table{titulo="B2. Comparativa de plataformas (RAG sin/poco código)"}
| Plataforma | Login usuario | Citas superíndice | Audio overview | Multi-doc | Costo gratis | API propia |
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
Para un reglamento de 35 páginas, un chunking razonable es:
- **Chunks de** _____________ _____________ 
- **Overlap** de _____________ _____________ 
- **Metadatos:** _____________, _____________, _____________ y _____________ _____________. 
Si los chunks son muy grandes, _____________ la relevancia; si son muy chicos, _____________ el contexto.
::/act-fill

::act-case{titulo="C3. Caso — diseña el chunking de tu reglamento" lineas=10}
Tu reglamento tiene 12 capítulos, 87 artículos y 4 fracciones por artículo.
La pregunta típica referencia un artículo concreto.
Diseña tu estrategia de chunking:
- ¿Por artículo, fracción, página o capítulo?
- ¿Qué overlap usas?
- ¿Qué metadatos incluyes?
Justifica con el caso de uso.
::/act-case

### Sección D — RAG vs fine-tuning (4.6)

::act-mcq{titulo="D1. Cuándo cada enfoque"}
1. El Asistente debe conocer el reglamento 2026 específico.
   - [x] RAG
   - [ ] Fine-tuning
   - [ ] Ambos

2. El Asistente debe adoptar un tono institucional complejo.
   - [ ] RAG
   - [x] Fine-tuning
   - [ ] Ambos

3. El reglamento cambia cada semestre.
   - [x] RAG (re-indexar es barato)
   - [ ] Fine-tuning
   - [ ] Ambos

4. Presupuesto $0 y sin ML engineer en el equipo.
   - [x] RAG con NotebookLM o Claude Projects
   - [ ] Fine-tuning
   - [ ] Custom training
::/act-mcq

::act-tf{titulo="D2. Mitos del fine-tuning"}
1. Fine-tuning hace que el modelo "sepa" tus datos para siempre. ( ) ____________________________________________
2. Si tu RAG es bueno, fine-tuning no aporta nada. ( ) ____________________________________________
3. Fine-tuning + RAG siempre es mejor que solo RAG. ( ) ____________________________________________
::/act-tf

### Sección E — Caso integrador

::act-case{titulo="E1. Caso — golden set y mitigación de alucinaciones" lineas=14}
Lanzas RAG en NotebookLM con 8 documentos.
Tu golden set tiene 12 preguntas. Resultados:
- 9/12 correctas con cita.
- 1 alucinación grave (inventó artículo).
- 2 dicen "no tengo info" (pero sí estaba).
Diseña el plan de remediación:
¿Qué cambias en chunking, instrucciones o herramienta? Lista 3 acciones priorizadas.
::/act-case

::act-mindmap{titulo="E2. Tu sistema RAG institucional" centro="RAG ALBATROS v1.0" nodos_primarios=6 nodos_secundarios=12}
Define 6 ramas principales:
1. Base documental.
2. Herramienta principal.
3. Golden set y resultados.
4. Instrucciones anti-alucinación.
5. Plan de mejora v1.1.
6. Distribución a usuarios.
*(Añade un dato concreto como nodo secundario en cada rama).*
::/act-mindmap

---

## Clave de respuestas

**A1.** Recuperación + Generación · offline · chunks · embedding · vector · embedding · similitud (semántica) · chunks · prompt aumentado · contextualizada · citas.

**A2.** 1-b · 2-b · 3-b.

**A3.** 
- 1) Falso — RAG cuesta menos para hechos; fine-tuning es para tono. 
- 2) Falso — Un chunk enorme diluye relevancia y sube costo. 
- 3) Falso — Sin metadatos no hay filtros ni citas exactas. 
- 4) Falso — Fine-tuning requiere 500-5000 ejemplos.

**B1.** 1-f · 2-c · 3-a · 4-b · 5-d · 6-e.

**B2.** Sugerencia:
| Plataforma | Login | Citas | Audio | Multi-doc | Free tier | API |
|---|---|---|---|---|---|---|
| NotebookLM | Google | sí | sí | sí | sí | no |
| Claude Projects | Anthropic | parcial | no | sí | con plan | con plan |
| Custom GPT | ChatGPT | parcial | no | sí | con plan | sí |
| Dify | varía | sí | no | sí | self-host | sí |
| Flowise | varía | sí | no | sí | self-host | sí |
| Stack AI | enterprise | sí | no | sí | trial | sí |

**C1.** Validar texto → OCR → Convención/metadatos → Chunkear → Embeddings → Vector store → Smoke test.

**C2.** Sugerencia: chunks de **400-800 tokens**, overlap **50-100 tokens**. Metadatos: **archivo, capítulo, artículo, página**. 
- Muy grandes: **diluyen** relevancia.
- Muy chicos: **pierden** contexto.

**C3.** Buena respuesta: 
- Chunk por **artículo**.
- Metadatos: `{archivo, capítulo, articulo, fracciones[]}`.
- Overlap mínimo (50 tokens) (artículos son autocontenidos).

**D1.** 1-a · 2-b · 3-a · 4-a.

**D2.** 
- 1) Falso — Fine-tuning entrena estilo, no garantiza recall. 
- 2) Falso — Fine-tuning da tono; RAG da hechos. 
- 3) Falso — Suma costo y complejidad; RAG suele bastar.

**E1.** Plan razonable:
- (a) **Mitigar alucinación:** Endurecer instrucciones ("si no hay cita, di 'no sé'").
- (b) **Mejorar 'no tengo info':** Revisar chunks y ajustar tamaño/overlap.
- (c) **Ampliar golden:** Subir a 30 preguntas para v1.1.

**E2.** Mapa libre. Identifica brechas si faltan datos en alguna rama.
