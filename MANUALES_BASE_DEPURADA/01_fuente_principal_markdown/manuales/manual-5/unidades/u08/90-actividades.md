---
unidad: 8
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 08

::act-mcq{titulo="Repaso conceptual"}
1. API key NUNCA debe ir en:
   - [ ] secrets.toml
   - [x] Código fuente subido a Git
   - [ ] Variable de entorno
   - [ ] Streamlit secrets

2. Para reducir costo de API en system prompt repetido, usa:
   - [ ] Modelo más grande
   - [x] Prompt caching
   - [ ] Más max_tokens
   - [ ] Sin caché

3. Embeddings + búsqueda semántica es preferible sobre keywords cuando:
   - [ ] Texto es muy corto
   - [x] Hay sinónimos / parafraseo
   - [ ] Solo hay 1 documento
   - [ ] Datos son numéricos

4. `@st.cache_resource` se usa para:
   - [ ] Resultados de API que cambian
   - [x] Objetos no serializables como modelos
   - [ ] Variables de entorno
   - [ ] CSS

5. Mini-RAG mínimo combina:
   - [x] Embeddings + vector store + LLM con prompt aumentado
   - [ ] Solo LLM
   - [ ] Solo embeddings
   - [ ] Modelo fine-tuned solamente
::/act-mcq

::act-table{titulo="Componente Streamlit"}
| Necesidad | Componente Streamlit |
|---|---|
| Selector entre opciones |  |
| Texto numérico de entrada |  |
| Layout en 2 columnas |  |
| Mostrar gráfico matplotlib |  |
| Subir archivo CSV |  |
::/act-table

::act-match{titulo="Buena práctica"}
| Práctica | Resuelve |
|---|---|
| 1. Caching | a) Costo descontrolado |
| 2. Try/except | b) API caída rompe app |
| 3. Secrets | c) API keys filtradas |
| 4. Logs | d) Imposible debug en prod |
| 5. Validación inputs | e) Prompt injection |
::/act-match

::act-tf{titulo="V/F"}
1. Streamlit requiere conocer JavaScript. ( ) ____________________________________________

2. Embeddings convierten texto a vectores numéricos. ( ) ____________________________________________

3. Tool use permite a LLM invocar funciones Python. ( ) ____________________________________________

4. RAG elimina alucinaciones automáticamente. ( ) ____________________________________________

5. Streaming reduce latencia total. ( ) ____________________________________________
::/act-tf

::albatros{titulo="App final del Asistente Predictor en producción" tipo="reto" tiempo="6 h"}
**Pregunta detonadora.** 
- Si tu coordinadora puede usar tu predictor desde su navegador sin abrir Colab, ¿qué cambia en su día a día?

::interioriza
- **Analogía:** Desplegar una app en Streamlit Cloud es como abrir un restaurante.
- Antes cocinabas en tu propia casa (Colab/Local) solo para ti.
- Ahora ofreces un menú público (App) al que cualquiera puede acceder y pedir su plato (Predicción).
::/interioriza

**Lo que harás.**
- [ ] 1. Implementa app completa de la práctica resuelta.
- [ ] 2. Pre-computa `indice_rag.json` con 3 PDFs institucionales.
- [ ] 3. Configura secrets correctamente.
- [ ] 4. Aplica las 5 buenas prácticas (caching, errores, logs, validación, modelo apropiado).
- [ ] 5. Sube a GitHub.
- [ ] 6. Despliega en Streamlit Community Cloud.
- [ ] 7. Test con 3 usuarios reales (coordinadora, docente, dirección).
- [ ] 8. Documenta lecciones.

**Materiales.** 
- API keys (Anthropic, OpenAI)
- 3 PDFs institucionales
- Cuentas en GitHub y Streamlit Cloud

**Entregable.**
- URL pública de app desplegada.
- Repo GitHub con código.
- README con setup y uso.
- Reporte de testeo (1-2 pp).
- Captura de pantalla de app funcionando.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| App funcional | local solo | desplegada | + multi-usuario |
| RAG | sin contexto | con búsqueda | + citas en respuesta |
| UX | crudo | con título y inputs | + métricas + tabs + sidebar |
| Buenas prácticas | none | 2-3 | las 5 implementadas |
| Validación usuarios | no probado | 1 persona | 3+ con feedback escrito |

::pausa
- ¿Qué problema solucionaría tu app para la dirección escolar en los primeros 10 minutos de uso?
::/pausa
::/albatros
