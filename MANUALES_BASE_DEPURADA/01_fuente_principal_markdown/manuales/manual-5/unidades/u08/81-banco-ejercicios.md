---
unidad: 8
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 08

> Practica APIs de IA generativa, embeddings, RAG y Streamlit. Cada bloque conecta con la app final.

::interioriza
- Piensa en la app final como un Lego avanzado.
- Cada bloque de ejercicios es una bolsa de piezas clave.
- Si dominas APIs, RAG y Streamlit por separado, el ensamble final será muy sencillo.
::/interioriza

::pausa{}
Antes de arrancar, reflexiona rápido:
- ¿Qué componente crees que será el más desafiante?
- ¿Tienes a la mano tu editor de código?
::/pausa

### Bloque A — Configurar API (8.1)

::act-mcq{titulo="Manejo seguro de API keys"}
1. ¿Dónde NUNCA debe ir tu API key?
   - [ ] Variable de entorno
   - [ ] Streamlit secrets
   - [x] Código fuente subido a Git
   - [ ] `.env` añadido a `.gitignore`

2. Si ya pusiste tu key en un commit público:
   - [ ] Borrar el commit es suficiente
   - [x] Rotar la key inmediatamente (los crawlers ya la tomaron)
   - [ ] No pasa nada
   - [ ] Cambiar el repo a privado

3. Para usar Anthropic en Streamlit:
   - [ ] Variable global en código
   - [x] `st.secrets["ANTHROPIC_API_KEY"]`
   - [ ] Hardcoded en string
   - [ ] En el README
::/act-mcq

::act-fill{titulo="Setup mínimo Anthropic"}
```python
import os
from anthropic import ___________

client = Anthropic(api_key=os.getenv("___________"))

resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=[
        {"role": "___________", "content": "Hola, ¿qué puedes hacer?"}
    ]
)
print(resp.content[0].___________)
```
::/act-fill

### Bloque B — Tu primer chatbot (8.2)

::act-order{titulo="Pasos para chatbot conversacional con historial"}
[ ] Llamar API con la lista de mensajes
[ ] Mantener lista `messages = []` con turnos
[ ] Append respuesta del assistant a la lista
[ ] Loop: pedir input al usuario
[ ] Agregar mensaje del usuario a la lista
[ ] Mostrar respuesta al usuario
::/act-order

::act-mcq{titulo="Roles en messages"}
1. ¿Qué role lleva la respuesta del modelo en el historial?
   - [ ] user
   - [x] assistant
   - [ ] system
   - [ ] bot

2. ¿Dónde declaras la "personalidad" del asistente?
   - [ ] Primer message del usuario
   - [x] Parámetro `system` (no en messages)
   - [ ] Variable de entorno
   - [ ] No se puede
::/act-mcq

### Bloque C — Streaming y tool use (8.3)

::act-mcq{titulo="Streaming"}
1. Streaming significa:
   - [ ] La API es más rápida
   - [x] Recibes tokens uno a uno mientras se generan
   - [ ] Compresión de respuesta
   - [ ] Solo funciona con Claude

2. Beneficio principal del streaming:
   - [ ] Costo menor
   - [x] Mejor UX (el usuario ve la respuesta apareciendo)
   - [ ] Más tokens
   - [ ] Cache automático
::/act-mcq

::act-fill{titulo="Streaming con SSE"}
```python
with client.messages.___________(
    model="claude-sonnet-4-6",
    max_tokens=500,
    messages=[{"role": "user", "content": "Cuéntame sobre IA"}]
) as stream:
    for text in stream.___________:
        print(text, end="", flush=True)
print()
```
::/act-fill

### Bloque D — Embeddings (8.4)

::act-mcq{titulo="Embeddings"}
1. Un embedding es:
   - [ ] El nombre del archivo
   - [x] Vector numérico que representa significado de un texto
   - [ ] Una imagen
   - [ ] Compresión sin pérdida

2. La similitud entre dos embeddings se calcula con:
   - [ ] Resta y comparas signos
   - [x] Coseno (o producto punto)
   - [ ] Solo distancia euclidiana
   - [ ] No se puede comparar

3. ¿Por qué embeddings > keywords para buscar?
   - [ ] Son más rápidos siempre
   - [x] Capturan sinónimos y parafraseo
   - [ ] Son más cortos
   - [ ] No requieren API
::/act-mcq

::act-fill{titulo="Similitud coseno"}
```python
import numpy as np

def coseno(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.___________(a) * np.linalg.norm(b))

# Test
v1 = [1, 0, 0]
v2 = [1, 0, 0]
v3 = [0, 1, 0]
print(coseno(v1, v2))   # esperado: ___________
print(coseno(v1, v3))   # esperado: ___________
```
::/act-fill

### Bloque E — Mini-RAG (8.5)

::act-order{titulo="Pasos del pipeline RAG mínimo"}
[ ] LLM responde con prompt aumentado
[ ] Embed cada chunk y guardar en JSON o vector store
[ ] Embed la query del usuario
[ ] Buscar top-k chunks por similitud coseno
[ ] Chunk los documentos en fragmentos
[ ] Concatenar chunks recuperados con la query en el prompt
::/act-order

::act-mcq{titulo="RAG"}
1. RAG soluciona principalmente:
   - [x] Acceso del LLM a información que no entrenó (privada, reciente)
   - [ ] Acelerar el modelo
   - [ ] Reducir el costo
   - [ ] Eliminar alucinaciones siempre

2. Si tu RAG **alucina** aunque tenga el contexto:
   - [ ] El modelo está roto
   - [x] Refuerza el prompt: "responde SOLO con base en el contexto"
   - [ ] Cambia de modelo
   - [ ] No hay solución
::/act-mcq

### Bloque F — Streamlit (8.6)

::act-match{titulo="Componente Streamlit ↔ uso"}
| Componente | Uso |
|---|---|
| 1. `st.slider` | a) Mostrar gráfico matplotlib |
| 2. `st.selectbox` | b) Subir archivo |
| 3. `st.file_uploader` | c) Selector entre opciones |
| 4. `st.pyplot` | d) Layout 2 columnas |
| 5. `st.columns(2)` | e) Input numérico continuo |
::/act-match

::act-mcq{titulo="Caching Streamlit"}
1. Para cachear el modelo cargado (objeto pesado, no serializable):
   - [ ] `@st.cache_data`
   - [x] `@st.cache_resource`
   - [ ] `@functools.cache`
   - [ ] No hay forma

2. Para cachear el resultado de una query a la API por 1 hora:
   - [x] `@st.cache_data(ttl=3600)`
   - [ ] `@st.cache_resource`
   - [ ] No se puede
   - [ ] Manualmente en Redis
::/act-mcq

::act-fill{titulo="App mínima Streamlit"}
```python
import streamlit as st

st.set_page_config(page_title="Predictor", page_icon="🎓")
st.title("Predictor de rendimiento")

col1, col2, col3 = st.___________(3)
with col1:
    horas = st.___________("Horas/sem", 0.0, 10.0, 4.0)
with col2:
    asistencia = st.slider("Asistencia", 0.0, 1.0, 0.85)
with col3:
    cal_anterior = st.slider("Cal anterior", 0.0, 10.0, 7.0)

if st.___________("Predecir"):
    # llamar tu modelo
    pred = 7.5   # placeholder
    st.metric("Calificación predicha", f"{pred:.2f}")
```
::/act-fill

### Bloque G — Buenas prácticas (8.7)

::act-tf{titulo="V/F producción IA"}
1. Llamar a la API en cada keystroke es buena idea (UX rápido). ( ) ____________________
2. Try/except con fallback es obligatorio cuando dependes de API externa. ( ) ____________________
3. Logs estructurados ayudan a debug en producción. ( ) ____________________
4. Validar inputs del usuario evita prompt injection. ( ) ____________________
5. Caching reduce costos sin afectar funcionalidad. ( ) ____________________
::/act-tf

::act-table{titulo="Riesgo → mitigación"}
| Riesgo | Mitigación |
|---|---|
| API key filtrada |  |
| Costo descontrolado |  |
| API caída rompe app |  |
| Prompt injection |  |
| Latencia alta |  |
| Datos sensibles a terceros |  |
::/act-table

::act-case{titulo="Caso — el costo se disparó" lineas=10}
- Tu app de predictor llevaba 3 días en producción.
- Hoy llega la factura: USD 240.
- Esperabas USD 20.

**Pregunta.** Diagnostica:
1. Lista 5 causas posibles del costo descontrolado.
2. ¿Cómo lo detectarías ANTES de la factura?
3. Diseña 3 controles operativos (rate limiting, presupuesto diario, alertas) para evitarlo.
::/act-case

---

## Clave de respuestas

**Bloque A.**
- `act-mcq`: 1·C, 2·B, 3·B.
- `act-fill`: `Anthropic`, `"ANTHROPIC_API_KEY"`, `role="user"`, `.text`.

**Bloque B.**
- `act-order`: 4·2·5·1·3·6 (loop input → append user → API → append assistant → mostrar → repetir).
- `act-mcq`: 1·B, 2·B.

**Bloque C.**
- `act-mcq`: 1·B, 2·B.
- `act-fill`: `client.messages.stream`, `stream.text_stream`.

**Bloque D.**
- `act-mcq`: 1·B, 2·B, 3·B.
- `act-fill`: `np.linalg.norm(a)`, output 1.0 (vectores idénticos), 0.0 (ortogonales).

**Bloque E.**
- `act-order`: 5·2·3·4·6·1 (chunkear → embed chunks → embed query → buscar → concatenar → LLM).
- `act-mcq`: 1·A, 2·B.

**Bloque F.**
- `act-match`: 1-e, 2-c, 3-b, 4-a, 5-d.
- `act-mcq`: 1·B, 2·A.
- `act-fill`: `st.columns(3)`, `st.slider`, `st.button`.

**Bloque G.**
- `act-tf`: 1·F (debounce/cache); 2·V; 3·V; 4·V; 5·V.
- `act-table`:

| Riesgo | Mitigación |
|---|---|
| API key filtrada | secrets manager + rotar + .gitignore |
| Costo descontrolado | rate limit + presupuesto + alertas |
| API caída | try/except + retry + fallback (predicción solo sin explicación) |
| Prompt injection | validar inputs + system prompt restrictivo |
| Latencia alta | streaming + caching + modelo más chico |
| Datos sensibles | anonimizar + revisar política del proveedor |

- `act-case`: respuesta modelo:
  > - (1) Loop infinito; max_tokens alto; bots/scrapers; sin caching; modelo sobredimensionado.
  > - (2) Detectar antes: dashboard de gasto con alertas; logs con costo estimado.
  > - (3) Controles: rate limit por IP, presupuesto diario, alerta si gasto >50%.

> **Cierre.** Si dominas estos 7 bloques, tu app final cumple los 5 requisitos profesionales:
> - Segura.
> - Robusta.
> - Eficiente.
> - Observable.
> - Sostenible en costo.
