---
unidad: 4
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 04

::interioriza
- **Piensa en RAG** como un examen a libro abierto: el modelo busca en tus apuntes antes de responder.
- **Piensa en Fine-Tuning** como estudiar durante meses para interiorizar un tono o estilo particular.
- *Analogía:* Si cambias las reglas (tu reglamento), RAG solo requiere nuevos apuntes. Fine-tuning requeriría estudiar de nuevo.
::/interioriza

::pausa{}
1. Si tu reglamento escolar cambia cada semestre, ¿cuál enfoque es más fácil de mantener y por qué?
2. ¿Por qué crees que un "chunk" muy grande diluye la respuesta correcta?
::/pausa

::act-mcq{titulo="Repaso conceptual"}
1. RAG **NO** elimina alucinaciones automáticamente. La instrucción clave es:
   - [ ] Aumentar a top-50 chunks
   - [x] "Si no encuentras la respuesta en los fragmentos, di 'no tengo información'"
   - [ ] Usar fine-tuning combinado
   - [ ] Bajar la temperatura a 0

2. Para indexar tu reglamento con citas, la mejor herramienta sin código actual es:
   - [ ] Custom GPT
   - [x] NotebookLM
   - [ ] Claude Projects
   - [ ] Dify

3. ¿En qué caso fine-tuning supera a RAG?
   - [ ] Conocer el contenido del reglamento
   - [x] Aprender un tono institucional muy específico que no se logra con prompts
   - [ ] Reducir costo total
   - [ ] Reducir tiempo de setup

4. Un chunk demasiado grande (>2000 tokens) suele:
   - [x] Diluir la relevancia y costar más al modelo
   - [ ] Mejorar siempre la precisión
   - [ ] Eliminar la necesidad de overlap
   - [ ] Acelerar la búsqueda

5. La métrica de similitud coseno vale 0.45. Esto significa:
   - [ ] Muy similar
   - [ ] Idéntico
   - [x] Temáticamente cerca, riesgo de ruido
   - [ ] Opuesto
::/act-mcq

::act-table{titulo="Completa la tabla — herramienta por caso"}
| Necesidad | Herramienta recomendada | Por qué |
|---|---|---|
| Distribuir chatbot público con tu reglamento |  |  |
| Audio overview del manual del docente |  |  |
| Razonamiento profundo en consulta combinada de 3 documentos |  |  |
| Pipeline RAG self-hosted con Cohere multilingual |  |  |
| Integraciones con Salesforce y SharePoint |  |  |
| Citas precisas con superíndice clickable |  |  |
::/act-table

::act-match{titulo="Relaciona el concepto con su descripción"}
| Concepto | Descripción |
|---|---|
| 1. Embedding | a) Etiquetas que viajan con el chunk: archivo, página, sección |
| 2. Chunk | b) Lista de números que representa el significado de un texto |
| 3. Metadatos | c) Fragmento del documento original |
| 4. Re-ranking | d) Segundo paso que ordena los top-50 candidatos para top-5 |
| 5. RAG | e) Recuperar fragmentos antes de generar la respuesta |
| 6. Fine-tuning | f) Continuar el entrenamiento del modelo con tus datos |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. RAG es siempre mejor que fine-tuning. ( ) ____________________________________________

2. Si indexas con OpenAI y consultas con Cohere, la similitud funciona. ( ) ____________________________________________

3. Un chunk sin metadatos no afecta la calidad con buen embedder. ( ) ____________________________________________

4. NotebookLM puede generar audio podcast del reglamento. ( ) ____________________________________________

5. Fine-tuning con 50 ejemplos suele dar buenos resultados. ( ) ____________________________________________
::/act-tf

::act-order{titulo="Ordena los pasos del pipeline RAG en producción"}
[ ] Construir prompt aumentado con chunks recuperados
[ ] Generar embedding de la pregunta del usuario
[ ] LLM produce respuesta con citas
[ ] Buscar top-k chunks por similitud en vector store
[ ] Indexar documentos (chunking + embedding) — offline
[ ] Re-ranking opcional para refinar top-5
[ ] Validar citas vs chunks recuperados (post-hoc)
::/act-order

::albatros{titulo="Construye el RAG de tu institución con NotebookLM + golden set" tipo="taller" tiempo="3 h"}
**Pregunta detonadora:**
- Si tu Asistente pudiera leer todos los documentos institucionales...
- Y pudiera citar la página exacta en sus respuestas...
- ¿Qué pregunta dejaría de viajar a coordinación cada semana?

**Lo que harás:**
1. Junta 5–8 documentos institucionales reales y límpialos (aplica OCR si aplica).
2. Usa la convención: `<tipo>_<nombre>_v<X.Y>_<fecha>.pdf`.
3. Súbelos a NotebookLM y configura instrucciones del notebook.
4. Genera un Audio Overview del reglamento como onboarding.
5. Crea un *golden set* de 10 preguntas variadas.
6. Evalúa: respondió bien / inventó / dijo "no sé".
7. Documenta hallazgos y decide tu próxima herramienta.

**Materiales y Entregables:**
- Cuenta gratis NotebookLM y 5–8 PDFs.
- Entregable: URL del notebook, Audio en Drive, doc de resultados.
- Incluye recomendación final (1 párrafo corto).

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cantidad y calidad | 1-2 sin limpiar | 5 limpios | 8+ con metadata |
| Golden set | 3 preguntas | 6-7 | 10+ casos de borde |
| Audio Overview | sin generar | generado | usado en onboarding |
| Documentación | informal | tabla básica | con recomendación |
| Distribución | privado | compartido | adoptado en operación |
::/albatros

::act-fill{titulo="Completa la fórmula mental de RAG"}
RAG = ____________ + ____________. 
- **Indexar** (offline): chunkear → _____________ → guardar en _____________ store. 
- **Consultar** (online): convertir pregunta en _____________, buscar por _____________ ____________.
- **Generar:** recuperar top-k chunks, construir _____________ aumentado, generar respuesta con _____________.
::/act-fill

::act-mindmap{titulo="Tu sistema RAG institucional v1" centro="RAG ALBATROS v1.0" nodos_primarios=6 nodos_secundarios=12}
Las 6 ramas: 
- (1) base documental, (2) herramienta principal, (3) golden set.
- (4) instrucciones anti-alucinación, (5) plan de mejora, (6) distribución. 
- En cada secundario, un dato concreto.
::/act-mindmap

::act-label{titulo="Etiqueta el pipeline RAG"}
::visual{tipo="diagrama-flujo" descripcion="Diagrama RAG: ingesta offline izquierda y consulta online derecha. Espacio para etiquetar cada estación." paginas=0.5}
- Marca: a) estación que más afecta calidad final.
- Marca: b) estación más costosa con millones de docs.
- Marca: c) estación que distingue RAG de fine-tuning.
- Marca: d) estación donde se reduce alucinación con buen diseño.
::/act-label

::act-case{titulo="Caso de diseño — eliges entre 4 herramientas para 3 casos" lineas=14}
- Te piden 3 RAGs: (1) público, (2) interno staff (razonamiento profundo), (3) API automatizada (n8n).
- Asigna NotebookLM, Claude Project, Custom GPT y Dify a los casos.
- Justifica usando criterios de costo, fricción y necesidad de API.
::/act-case

::albatros{titulo="Reto — diagnostica una alucinación grave de tu RAG" tipo="reto" tiempo="45 min"}
**Pregunta detonadora:**
- El Asistente inventó el "artículo 23 fracción II".
- ¿Cómo evitas que vuelva a pasar este error?

**Lo que harás:**
1. Reproduce la alucinación con la pregunta original.
2. Revisa los chunks recuperados (en NotebookLM, Dify o Claude).
3. Diagnostica: ¿fuera de documento?, ¿ruido?, ¿modelo ignoró chunk?
4. Aplica mitigación (instrucciones, chunking, o re-ranking).
5. Re-testea con la original + 4 variantes parecidas.
6. Documenta todo en `docs/alucinacion-001.md`.

**Entregable:** 
- Documento de 1 página.
- Debe incluir incident report y mitigación verificada.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Reproducción | informal | input exacto | chunks visibles |
| Diagnóstico | adivinanza | 1 hipótesis | verificada con evidencia |
| Mitigación | parche | aplicada | probada 4 variantes |
| Documentación | mínima | incident report | con plan preventivo |
::/albatros
