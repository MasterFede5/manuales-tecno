---
unidad: 7
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 07

::act-mcq{titulo="Repaso conceptual"}
1. La principal razón para migrar a IA local en una institución educativa es:
   - [ ] Costo
   - [x] Soberanía de datos sensibles (menores, calificaciones, salud)
   - [ ] Velocidad
   - [ ] Calidad del modelo

2. Para una institución hispanohablante mexicana, la familia de modelos abiertos más recomendable es:
   - [ ] Llama 3.1
   - [ ] Mistral
   - [x] Qwen 2.5
   - [ ] Phi-3

3. Q4_K_M en cuantización significa:
   - [ ] Modelo cuantizado a 4 bits con calidad ~98 %, sweet spot
   - [ ] Modelo de 4B parámetros
   - [ ] Modelo Q4 con licencia Mit
   - [ ] Versión 4 de Llama

4. Para un equipo de 50 staff con login institucional, la mejor UI local es:
   - [ ] Ollama CLI
   - [ ] LM Studio
   - [ ] Jan
   - [x] Open WebUI

5. ¿Cuál es la condición ineludible para tener un RAG 100 % local?
   - [ ] Modelo local
   - [ ] Vector store local
   - [ ] Embedder local
   - [x] Las tres juntas
::/act-mcq

::act-table{titulo="Completa la tabla — modelo según hardware y caso"}
| Hardware | Modelo recomendado | Caso del Asistente |
|---|---|---|
| Laptop 16GB RAM, GPU integrada |  |  |
| PC RTX 3060 12GB VRAM |  |  |
| Workstation A6000 48GB VRAM |  |  |
| Mac M3 Max 128 GB |  |  |
| Servidor multi-GPU enterprise |  |  |
::/act-table

::act-match{titulo="Relaciona el componente con su rol"}
| Componente | Rol |
|---|---|
| 1. Ollama | a) UI multi-usuario tipo ChatGPT |
| 2. Open WebUI | b) Runtime de modelos abiertos |
| 3. Qwen 2.5 | c) Modelo de embeddings local multilingüe |
| 4. bge-m3 | d) Vector store local default |
| 5. ChromaDB | e) Modelo de lenguaje abierto top en español |
| 6. Q4_K_M | f) Cuantización sweet spot calidad/tamaño |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Llama 3.1 70B Q4 cabe en una GPU de 24 GB VRAM. ( ) ____________________________________________

2. Open WebUI es solo para usuario individual. ( ) ____________________________________________

3. RAG con embedder cloud y modelo local mantiene la soberanía. ( ) ____________________________________________

4. Apple Silicon es siempre superior a NVIDIA para IA local. ( ) ____________________________________________

5. Qwen 2.5 72B es bueno para razonamiento crítico en español. ( ) ____________________________________________
::/act-tf

::act-order{titulo="Ordena los pasos para desplegar Asistente local"}
[ ] Backup automático del volumen Docker
[ ] Crear cuentas usuarios con SSO
[ ] Instalar Ollama
[ ] Configurar knowledge base con embedder
[ ] Descargar modelo principal (Qwen 2.5 72B)
[ ] Probar con golden set vs cloud
[ ] Instalar Open WebUI con Docker
[ ] Crear Modelfile customizado con system prompt institucional
::/act-order

::albatros{titulo="Despliega tu primer Asistente IA local con stack completo" tipo="taller" tiempo="4 h"}
**Pregunta detonadora.** Si pudieras correr ChatGPT en tu propia computadora, sin pagar nunca y sin que ningún dato saliera a internet, ¿qué pondrías en él que hoy no pones por miedo?

**Lo que harás.**
1. Instala Ollama en tu computadora (o servidor).
2. Descarga 2 modelos: uno mediano (Qwen 2.5 7B) y un embedder (bge-m3 o nomic-embed-text).
3. Instala Open WebUI con Docker.
4. Crea cuenta admin y configura el modelo como default.
5. Crea una knowledge base con 3 PDFs reales de tu institución.
6. Customiza system prompt con Modelfile.
7. Prueba con 10 preguntas reales y mide: latencia, calidad subjetiva 1-5, número de respuestas con cita correcta.
8. Documenta hardware usado, tiempo de setup, y comparativa contra alternativa cloud.

**Materiales.** Computadora con mínimo 16 GB RAM (GPU recomendada), Docker, 50 GB disco libre, 4 horas.

**Entregable.**
- Open WebUI accesible en localhost.
- Knowledge base con 3 documentos.
- Reporte (1-2 pp): hardware, modelos elegidos, setup time, golden set, comparativa.
- Captura del Asistente respondiendo con cita.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Setup completo | uno de los 3 | 2 de 3 | Ollama + Open WebUI + KB |
| Modelo elegido | sin pensar | apto al hardware | optimizado calidad/recursos |
| Knowledge base | sin docs | 1-2 docs | 3+ docs con embedder bueno |
| Golden set | <5 preguntas | 7-10 | 10+ con casos NO-respuesta |
| Reporte | mínimo | con cifras | con comparativa cloud y decisión |
| Aplicabilidad | demo | usable individualmente | desplegable a equipo |
::/albatros

::act-fill{titulo="Comandos esenciales de Ollama"}
Para descargar e iniciar Qwen 2.5 7B en tu máquina:

```bash
ollama _____________ qwen2.5:7b
ollama _____________
ollama _____________ qwen2.5:7b
```

Para crear un modelo customizado:

```bash
ollama _____________ asistente -f Modelfile.asistente
```

Ollama sirve por defecto en HTTP localhost:_____________.
::/act-fill

::act-mindmap{titulo="Tu stack soberano v1.0" centro="ASISTENTE LOCAL ALBATROS" nodos_primarios=7 nodos_secundarios=14}
Las 7 ramas: (1) hardware (CPU/GPU/RAM), (2) Ollama + modelos descargados, (3) Open WebUI configurado, (4) embedder + vector store local, (5) auth/SSO, (6) backup y monitoreo, (7) golden set comparativo cloud. Cada secundario, dato concreto.
::/act-mindmap

::act-label{titulo="Etiqueta el stack soberano"}
> Marca: a) la capa que más impacta calidad final · b) la capa que más impacta latencia · c) la capa más fácil de comprometer si falta política de acceso · d) la capa que protege contra cambios forzados del proveedor cloud.
::/act-label


::visual{tipo="ilustracion" descripcion="Diagrama del stack soberano del Asistente local: hardware (servidor con GPU) en la base, encima Docker, encima Ollama (con modelos Qwen, Llama, embedder bge-m3), encima Open WebUI con SSO, conectado a ChromaDB local con knowledge base, todo dentro de un escudo etiquetado 'cero datos a internet'. Espacio para etiquetar cada capa con su rol y modo de falla típico." paginas="0.5" src="../manualesGem/assets/visuales/manual-4/u07/90-actividades-v01.svg"}
::act-case{titulo="Caso de diseño — TCO real local vs cloud" lineas=14}
Tu institución gasta $4 200/año en cloud. Para migrar: workstation $3 500 (one-time), electricidad $80/mes, mantenimiento 4 h/mes a $25/h. Calcula TCO a 12, 24 y 36 meses. ¿En qué momento "paga"? Identifica 3 consideraciones no-monetarias que pesan más que el costo y cómo justificarías el monto al patronato.
::/act-case

::albatros{titulo="Reto — benchmark Qwen 7B vs 14B vs 32B sobre 10 preguntas" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** ¿Vale la pena pagar 4x más memoria por el modelo grande, o el chico ya cubre tu caso?

**Lo que harás.**
1. Si tu hardware lo permite, descarga Qwen 2.5 7B, 14B y 32B (Q4_K_M).
2. Construye 10 preguntas: 6 sencillas, 2 razonamiento, 2 fuera de scope.
3. Lanza las mismas 10 a los 3 modelos.
4. Califica cada respuesta 1-5 con tu rúbrica.
5. Anota tiempo de respuesta y memoria usada.
6. Decide: ¿qué tamaño basta para tu caso?

**Entregable.** Tabla 10×3 + decisión documentada en 5 líneas con criterio.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Modelos comparados | 1 | 2 | 3 |
| Métricas | calidad | calidad + tiempo | calidad + tiempo + memoria |
| Decisión | preferencia | con dato | con dato + cuándo cambiar de tamaño |
::/albatros
