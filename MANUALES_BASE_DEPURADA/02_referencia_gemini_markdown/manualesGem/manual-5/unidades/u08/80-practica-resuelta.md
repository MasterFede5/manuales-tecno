---
unidad: 8
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 08

::practica{titulo="App Streamlit final: Predictor + RAG + Explicación con buenas prácticas"}
**Problema.** Construir y desplegar **app web final del Asistente Predictor Albatros** que integra modelo ML (U5/U7) + RAG sobre 3 PDFs institucionales (U8) + explicación con Claude + Streamlit + buenas prácticas (caching, errores, secrets).

**Paso 1 — Estrategia.** Pipeline completo en archivo único `app.py`.

**Paso 2 — Código.**

```python
# app.py
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os
import time
import logging
from anthropic import Anthropic
from openai import OpenAI

# Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

claude = Anthropic(api_key=st.secrets.get("ANTHROPIC_API_KEY"))
openai_client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

# === Cargados con cache ===
@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_predictor_v1.pkl")

@st.cache_data
def cargar_indice_rag():
    """Carga embeddings pre-computados."""
    import json
    with open("indice_rag.json", "r") as f:
        return json.load(f)

@st.cache_data(ttl=3600)
def embed_query(query):
    return openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

# === Funciones ===
def buscar_rag(query, indice, k=3):
    e_q = np.array(embed_query(query))
    sims = []
    for c in indice:
        e_c = np.array(c["embedding"])
        sim = np.dot(e_q, e_c) / (np.linalg.norm(e_q) * np.linalg.norm(e_c))
        sims.append(sim)
    top_idx = np.argsort(sims)[::-1][:k]
    return [indice[i] for i in top_idx]

def explicar_con_claude(features_alumno, prediccion, contexto_rag):
    prompt = f"""Eres asesor académico. Explica la predicción para este alumno.

DATOS:
- Horas estudio: {features_alumno['horas_estudio']}/semana
- Asistencia: {features_alumno['asistencia']*100:.0f}%
- Calificación anterior: {features_alumno['cal_anterior']}

PREDICCIÓN: {prediccion:.2f}/10

CONTEXTO INSTITUCIONAL (reglamento):
{chr(10).join([c['texto'][:200] for c in contexto_rag])}

Responde en 3 partes:
1. **Lectura del riesgo**: ¿es alto/medio/bajo? ¿qué factor pesa más?
2. **Política institucional aplicable**: cita reglamento si aplica.
3. **3 acciones específicas**: qué proponer al coordinador."""
    
    try:
        response = claude.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=600,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        logger.error(f"Error API: {e}")
        return f"⚠ No pude generar explicación: {e}. Predicción solamente: {prediccion:.2f}"

# === UI ===
st.set_page_config(page_title="Predictor Albatros", page_icon="🎓", layout="wide")
st.title("🎓 Predictor de Rendimiento Albatros")
st.caption("ML + IA Generativa + RAG institucional")

# Cargar
modelo = cargar_modelo()
indice = cargar_indice_rag()

# Sidebar
with st.sidebar:
    st.header("Configuración")
    nombre = st.text_input("Nombre alumno (referencia)", "Sin nombre")
    materia = st.selectbox("Materia", ["Matemáticas", "Física", "Química"])

# Inputs
col1, col2, col3 = st.columns(3)
with col1:
    horas = st.slider("Horas estudio/sem", 0.0, 10.0, 4.0, 0.5)
with col2:
    asistencia = st.slider("Asistencia", 0.0, 1.0, 0.85, 0.05)
with col3:
    cal_ant = st.slider("Cal. anterior", 0.0, 10.0, 7.0, 0.5)

if st.button("🔮 Predecir y explicar", type="primary"):
    features = {
        "horas_estudio": horas,
        "asistencia": asistencia,
        "cal_anterior": cal_ant
    }
    X = pd.DataFrame([features])
    pred = modelo.predict(X)[0]
    
    # UI resultado
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Calificación predicha", f"{pred:.2f}", 
                  delta=f"{pred - cal_ant:+.2f} vs anterior")
    with col_b:
        riesgo = "🔴 ALTO" if pred < 6 else ("🟡 MEDIO" if pred < 7 else "🟢 BAJO")
        st.metric("Riesgo", riesgo)
    
    # RAG: buscar contexto institucional
    with st.spinner("Consultando reglamento..."):
        query_rag = f"Política para alumno con asistencia {asistencia*100:.0f}% y predicción {pred:.1f}"
        contexto = buscar_rag(query_rag, indice, k=3)
    
    # Explicar
    with st.spinner("Generando análisis..."):
        explicacion = explicar_con_claude(features, pred, contexto)
    
    st.markdown("### 📋 Análisis y recomendaciones")
    st.markdown(explicacion)
    
    # Mostrar fuentes RAG
    with st.expander("Fuentes consultadas"):
        for c in contexto:
            st.text(f"📄 {c['fuente']}: {c['texto'][:200]}...")
    
    # Log
    logger.info(f"Pred {nombre} {materia}: {pred:.2f} (riesgo={riesgo})")
```

**Paso 3 — Estructura del proyecto.**
```
predictor_albatros/
├── app.py
├── modelo_predictor_v1.pkl
├── indice_rag.json     ← pre-computado
├── requirements.txt
├── .streamlit/
│   └── secrets.toml    ← API keys (no en Git)
├── README.md
└── .gitignore
```

**Paso 4 — Despliegue (15 min).**
1. Subir a GitHub público (sin secrets.toml).
2. streamlit.io → "New app" → conecta repo.
3. Configurar secrets en panel.
4. Deploy. URL pública en 2 min.

**Paso 5 — Test con coordinadora.**
- 5 casos reales del backlog.
- Cada uno: predicción + explicación.
- Coordinadora valida que sugerencias tienen sentido pedagógico.

**Verificación.** App funciona, secrets seguros, errores manejados, costos monitoreados con logs.

**Lección.** Las 7 técnicas del manual encajan: API config + chatbot básico + streaming/tools + embeddings + RAG + Streamlit + buenas prácticas. Resultado: aplicación que combina ML clásico + IA generativa + datos institucionales en una sola interfaz usable. **Tu primer producto IA real**.

**Conexión con TODO el manual.** Esta app integra: Python (U1), Pandas (U2), Visualización opcional (U3), estadística para validar predicciones (U4), modelo entrenado (U5), perfiles para contexto (U6), red neuronal opcional (U7), y todas las APIs de IA generativa (U8). Es la síntesis del manual completo.
::/practica
