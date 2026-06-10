---
unidad: 4
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 04

::act-mcq{titulo="Repaso conceptual"}
1. RAG **NO** elimina alucinaciones automáticamente. La instrucción más importante para reducirlas es:
   - [ ] Aumentar a top-50 chunks
   - [x] "Si no encuentras la respuesta en los fragmentos, di 'no tengo información'"
   - [ ] Usar fine-tuning combinado
   - [ ] Bajar la temperatura a 0

2. Para indexar tu reglamento institucional con citas verificables, la herramienta sin código más fuerte en 2025 es:
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

5. La métrica de similitud coseno entre la pregunta y un chunk vale 0.45. Esto significa:
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

2. Si indexas con OpenAI embeddings y consultas con Cohere, la similitud sigue funcionando. ( ) ____________________________________________

3. Un chunk con metadatos vacíos no afecta la calidad si el embedder es bueno. ( ) ____________________________________________

4. NotebookLM puede generar audio podcast del reglamento. ( ) ____________________________________________

5. Fine-tuning con un dataset de 50 ejemplos suele dar buenos resultados. ( ) ____________________________________________
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
**Pregunta detonadora.** Si tu Asistente pudiera leer todos los documentos de tu institución y citar la página exacta, ¿qué pregunta dejaría de viajar de papá a coordinación cada semana?

**Lo que harás.**
1. Junta 5–8 documentos institucionales reales (reglamento, calendario, política, manual docente, ética).
2. Limpia los PDFs si están escaneados (OCR si hace falta).
3. Aplica convención de nombres: `<tipo>_<nombre>_v<X.Y>_<fecha>.pdf`.
4. Súbelos a NotebookLM y configura instrucciones del notebook.
5. Genera Audio Overview del reglamento como onboarding.
6. Crea golden set de 10 preguntas: 5 con respuesta esperada, 3 que requieren combinar fuentes, 2 que NO están en los documentos.
7. Lanza las 10 preguntas y registra: respondió bien / inventó / dijo "no sé" correctamente.
8. Documenta hallazgos y decide si pasas a Claude Project, Dify o quedas con NotebookLM.

**Materiales.** Cuenta gratis NotebookLM, opcionalmente Claude Pro, los 5–8 PDFs.

**Entregable.**
- URL del notebook compartible.
- Audio Overview en Drive.
- Documento de golden set con resultados anotados (1–2 pp).
- Recomendación al equipo (1 párrafo).

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cantidad y calidad de documentos | 1-2 sin limpiar | 5 limpios | 8+ con metadata limpia |
| Golden set | 3 preguntas | 6-7 | 10+ con casos de borde |
| Audio Overview | sin generar | generado | generado y usado para onboarding |
| Documentación de hallazgos | informal | tabla básica | análisis con recomendación |
| Distribución | privado | compartido al equipo | adoptado en operación |
::/albatros

::act-fill{titulo="Completa la fórmula mental de RAG"}
RAG = ____________ + ____________. **Indexar** (offline): chunkear → _____________ → guardar en _____________ store. **Consultar** (online): convertir pregunta en _____________, buscar por _____________ ____________, recuperar top-k chunks, construir _____________ aumentado, generar respuesta con _____________.
::/act-fill

::act-mindmap{titulo="Tu sistema RAG institucional v1" centro="RAG ALBATROS v1.0" nodos_primarios=6 nodos_secundarios=12}
Las 6 ramas: (1) base documental con versiones, (2) herramienta principal y razón, (3) golden set y métricas RAGAS, (4) instrucciones anti-alucinación, (5) plan de mejora v1.1, (6) distribución a usuarios. En cada secundario, un dato concreto.
::/act-mindmap

::act-label{titulo="Etiqueta el pipeline RAG"}
> Marca: a) la estación que más afecta calidad final · b) la estación con mayor costo cuando hay millones de docs · c) la estación que distingue RAG de fine-tuning · d) la estación donde se reduce alucinación si está bien diseñada.
::/act-label


::visual{tipo="diagrama-flujo" descripcion="Diagrama del pipeline RAG completo: a la izquierda, ingesta offline (PDFs → chunking → embeddings → vector store con metadatos). A la derecha, consulta online (pregunta usuario → embedding → similitud → top-k chunks → re-ranking opcional → prompt aumentado → LLM → respuesta con citas). Espacio para etiquetar cada estación con su nombre, herramienta usada y posible modo de falla." paginas="0.5" src="../manualesGem/assets/visuales/manual-4/u04/90-actividades-v01.svg"}
::act-case{titulo="Caso de diseño — eliges entre 4 herramientas para 3 casos" lineas=14}
Tu institución te pide 3 sistemas RAG en el mismo trimestre: (1) **público** — papás consultan reglamento desde la web institucional, (2) **interno staff** — coordinación necesita razonamiento profundo cruzando 3 documentos, (3) **API automatizada** — n8n debe consultar el reglamento dentro de un workflow. Asigna NotebookLM, Claude Project, Custom GPT y Dify a los 3 casos (uno puede quedar sin uso) y justifica con costo, fricción y necesidad de API.
::/act-case

::albatros{titulo="Reto — diagnostica una alucinación grave de tu RAG" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** Tu Asistente RAG dijo *"según el artículo 23 fracción II del reglamento..."* y el artículo 23 fracción II **no existe**. ¿Cómo evitas que vuelva a pasar?

**Lo que harás.**
1. Reproduce la alucinación con la pregunta original.
2. Mira los chunks recuperados (NotebookLM y Dify lo muestran; Claude Projects parcial).
3. Diagnostica: ¿la pregunta está fuera de documento?, ¿el chunk recuperado es ruido?, ¿el modelo ignoró el chunk?
4. Aplica una de 3 mitigaciones: instrucciones más estrictas + re-test, ajuste de chunking, o cambio a herramienta con re-ranking.
5. Re-testea con la pregunta original + 4 variantes parecidas.
6. Documenta en `docs/alucinacion-001.md` con: input, salida original, diagnóstico, mitigación, salida nueva.

**Entregable.** Documento de 1 página con incident report y mitigación verificada.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Reproducción del fallo | informal | con input exacto | con input + chunks recuperados visibles |
| Diagnóstico | adivinanza | una hipótesis | hipótesis verificada con evidencia |
| Mitigación | parche | aplicada | aplicada y probada con 4 variantes |
| Documentación | mínima | incident report | incident report + plan preventivo |
::/albatros
