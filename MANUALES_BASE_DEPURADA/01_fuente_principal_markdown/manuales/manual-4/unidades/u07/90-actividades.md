---
unidad: 7
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 07

::interioriza
**Analogía: La Cocina Propia**
Tener un modelo local es como cocinar en casa en lugar de pedir a un restaurante (cloud).
- Pagas los electrodomésticos (hardware) y cocinas (mantenimiento).
- Tienes control absoluto de los ingredientes (privacidad de datos).
- Nadie te cobra extra por cada plato que preparas.
::/interioriza

::pausa{}
1. ¿Cuál es el mayor costo oculto al tener un RAG local?
2. ¿Por qué la RAM/VRAM es el cuello de botella más crítico frente a la CPU?
::/pausa

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
**Pregunta detonadora.**
- Si pudieras correr ChatGPT en tu computadora...
- Sin pagar nunca y sin enviar datos a internet...
- ¿Qué pondrías en él que hoy no pones por miedo?

**Lo que harás.**
1. Instala Ollama en tu computadora o servidor.
2. Descarga un modelo (Qwen 2.5 7B) y un embedder (bge-m3).
3. Instala Open WebUI con Docker.
4. Crea cuenta admin y define el modelo default.
5. Crea knowledge base con 3 PDFs institucionales reales.
6. Customiza el system prompt con un Modelfile.
7. Prueba 10 preguntas y mide: latencia y calidad (1-5).
8. Documenta hardware, tiempo de setup y compara vs cloud.

**Materiales.**
- PC con mínimo 16 GB RAM (GPU recomendada).
- Docker instalado.
- 50 GB de disco libre.
- 4 horas disponibles.

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
Las 7 ramas principales:
- (1) Hardware (CPU/GPU/RAM).
- (2) Ollama + modelos descargados.
- (3) Open WebUI configurado.
- (4) Embedder + vector store local.
- (5) Auth/SSO.
- (6) Backup y monitoreo.
- (7) Golden set comparativo cloud.
Cada secundario debe incluir un dato concreto.
::/act-mindmap

::act-label{titulo="Etiqueta el stack soberano"}
::visual{tipo="ilustracion" descripcion="Diagrama del stack soberano del Asistente local: hardware (servidor con GPU) en la base, encima Docker, encima Ollama (con modelos Qwen, Llama, embedder bge-m3), encima Open WebUI con SSO, conectado a ChromaDB local con knowledge base, todo dentro de un escudo etiquetado 'cero datos a internet'. Espacio para etiquetar cada capa con su rol y modo de falla típico." paginas=0.5}
> Marca lo siguiente:
- a) La capa que más impacta la calidad final.
- b) La capa que más impacta la latencia.
- c) La capa más fácil de comprometer sin políticas de acceso.
- d) La capa que protege contra cambios del proveedor cloud.
::/act-label

::act-case{titulo="Caso de diseño — TCO real local vs cloud" lineas=14}
- Tu institución gasta $4 200/año en cloud.
- Migración: workstation $3 500 (one-time).
- Electricidad: $80/mes.
- Mantenimiento: 4 h/mes a $25/h.

Calcula el TCO a 12, 24 y 36 meses.
¿En qué momento se "paga" la inversión?
Identifica 3 consideraciones no-monetarias clave.
¿Cómo justificarías el monto al patronato?
::/act-case

::albatros{titulo="Reto — benchmark Qwen 7B vs 14B vs 32B sobre 10 preguntas" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.**
- ¿Vale la pena pagar 4x más memoria por el modelo grande?
- ¿O el modelo chico ya cubre bien tu caso de uso?

**Lo que harás.**
1. Descarga Qwen 2.5 7B, 14B y 32B (Q4_K_M) si hay hardware.
2. Construye 10 preguntas (6 sencillas, 2 complejas, 2 out-of-scope).
3. Lanza las mismas 10 preguntas a los 3 modelos.
4. Califica cada respuesta del 1 al 5 usando tu rúbrica.
5. Anota tiempo de respuesta y memoria usada.
6. Decide: ¿qué tamaño basta para tu caso?

**Entregable.**
- Tabla 10×3.
- Decisión documentada en 5 líneas con tu criterio de selección.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Modelos comparados | 1 | 2 | 3 |
| Métricas | calidad | calidad + tiempo | calidad + tiempo + memoria |
| Decisión | preferencia | con dato | con dato + cuándo cambiar de tamaño |
::/albatros
