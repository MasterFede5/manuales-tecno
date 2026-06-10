---
unidad: 8
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Unidad 08

::albatros{titulo="Pipeline E2E reproducible: dataset → modelo → API → app desplegada" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si te dieran un servidor vacío, ¿cuánto tardas en desplegar tu predictor desde cero? Spoiler: con un buen Makefile, < 10 minutos.

**Contexto del case.** Cierre del manual. Hoy integras todo: tu pipeline de datos (U2), tu modelo (U5/U7), tu API (U7-taller), tu app Streamlit (U8). Todo automatizado en un repo reproducible.

### Materiales

- Repo Git con el código acumulado de los 7 talleres.
- Python 3.10+, pip, venv.
- Cuenta GitHub.
- Cuenta Anthropic (key) — opcional para la parte de explicación.

### Pasos del taller (60 min)

**Paso 1 — Estructurar el repo (10 min).**

```
predictor-albatros/
├── README.md
├── Makefile
├── requirements.txt
├── data/
│   ├── raw/
│   │   └── dataset_escolar.csv
│   └── processed/
│       └── dataset_escolar_limpio.csv
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py      ← U2
│   ├── train.py              ← U5/U7
│   ├── predict.py            ← uso
│   └── api.py                ← FastAPI
├── notebooks/
│   ├── 01_eda.ipynb          ← U3/U4
│   └── 02_modelos.ipynb      ← U5
├── streamlit_app.py          ← U8
├── tests/
│   └── test_pipeline.py
├── modelos/                  ← .pkl/.pt versionados con DVC o ignorados
└── .env.example
```

**Paso 2 — `requirements.txt` (5 min).**

```
pandas==2.2.*
numpy==1.26.*
scikit-learn==1.4.*
matplotlib==3.8.*
seaborn==0.13.*
torch==2.2.*
joblib==1.3.*
fastapi==0.110.*
uvicorn==0.27.*
streamlit==1.32.*
anthropic==0.20.*
pytest==8.0.*
```

**Paso 3 — `Makefile` con targets (10 min).**

```makefile
.PHONY: install clean data train test api app deploy

install:
	pip install -r requirements.txt

data:
	python -c "from src.data_pipeline import limpiar_archivo; limpiar_archivo('data/raw/dataset_escolar.csv', 'data/processed/dataset_escolar_limpio.csv')"

train:
	python src/train.py --data data/processed/dataset_escolar_limpio.csv --salida modelos/predictor_v1.pkl

test:
	pytest tests/ -v

api:
	uvicorn src.api:app --reload --port 8000

app:
	streamlit run streamlit_app.py

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache modelos/*.pkl

all: install data train test
```

Ahora levantar todo se reduce a:

```bash
make install
make data
make train
make test
make api &      # background
make app
```

**Paso 4 — `streamlit_app.py` minimalista E2E (15 min).**

```python
import streamlit as st
import pandas as pd
import joblib
import json
from pathlib import Path

st.set_page_config(page_title="Predictor Albatros", page_icon="🎓", layout="wide")

# Cargar artefactos (1 sola vez)
@st.cache_resource
def cargar_artefactos():
    modelo = joblib.load("modelos/predictor_v1.pkl")
    return modelo

modelo = cargar_artefactos()

st.title("🎓 Predictor de Rendimiento Escolar")
st.caption("Pipeline E2E · Manual 5 Albatros · v1.0")

# Sidebar con metadata
with st.sidebar:
    st.header("Información del modelo")
    st.write(f"Tipo: Random Forest")
    st.write(f"Features: 3 (horas, asistencia, cal_anterior)")
    st.write(f"R² CV: 0.70")
    st.write(f"MAE CV: 0.65")
    st.divider()
    st.subheader("Cómo usar")
    st.write("1. Ajusta los sliders.\n2. Click en Predecir.\n3. Lee la calificación predicha y el riesgo.")

# Inputs
col1, col2, col3 = st.columns(3)
with col1:
    horas = st.slider("Horas estudio/semana", 0.0, 10.0, 4.0, 0.5)
with col2:
    asistencia = st.slider("Asistencia", 0.0, 1.0, 0.85, 0.01)
with col3:
    cal_anterior = st.slider("Cal. anterior", 0.0, 10.0, 7.0, 0.5)

# Predicción
if st.button("🔮 Predecir", type="primary"):
    X = pd.DataFrame([{
        "horas_estudio": horas,
        "asistencia": asistencia,
        "cal_anterior": cal_anterior
    }])
    pred = float(modelo.predict(X)[0])
    riesgo = "🔴 ALTO" if pred < 6 else ("🟡 MEDIO" if pred < 7.5 else "🟢 BAJO")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Calificación predicha", f"{pred:.2f}",
                  delta=f"{pred - cal_anterior:+.2f} vs anterior")
    with col_b:
        st.metric("Riesgo", riesgo)
    
    # Tabla de inputs
    st.subheader("Datos del alumno")
    st.dataframe(X, use_container_width=True)

st.divider()
st.caption("Modelo entrenado en U5 · Servido por Streamlit · Albatros 2026")
```

**Paso 5 — `tests/test_pipeline.py` mínimo (5 min).**

```python
import pandas as pd
import joblib
from pathlib import Path

def test_modelo_existe():
    assert Path("modelos/predictor_v1.pkl").exists(), "Modelo no entrenado"

def test_modelo_predice():
    modelo = joblib.load("modelos/predictor_v1.pkl")
    X = pd.DataFrame([{
        "horas_estudio": 4.0,
        "asistencia": 0.85,
        "cal_anterior": 7.0
    }])
    pred = modelo.predict(X)[0]
    assert 0 <= pred <= 10, f"Predicción fuera de rango: {pred}"

def test_dataset_limpio_existe():
    assert Path("data/processed/dataset_escolar_limpio.csv").exists()
    df = pd.read_csv("data/processed/dataset_escolar_limpio.csv")
    assert len(df) > 100
    assert "cal_final" in df.columns
    assert df["cal_final"].between(0, 10).all()
```

**Paso 6 — `README.md` ejecutable (5 min).**

```markdown
# Predictor Albatros — Manual 5 (final)

## Setup en 5 minutos

\`\`\`bash
git clone https://github.com/tu-user/predictor-albatros.git
cd predictor-albatros
python -m venv .venv && source .venv/bin/activate   # o .venv\Scripts\activate en Windows
make install
make all                # data + train + test
make app                # abre Streamlit en localhost:8501
\`\`\`

## Estructura

[diagrama del repo]

## Métricas del modelo

| Métrica | Valor |
|---|---|
| R² CV | 0.70 |
| MAE CV | 0.65 |

## Limitaciones conocidas

- Modelo entrenado con 465 alumnos; generalización a otras cohortes no validada.
- Predice calificación, NO causa: NO usar para decisiones disciplinarias automatizadas.
```

**Paso 7 — Despliegue final (10 min).**

```bash
git add .
git commit -m "v1.0: pipeline E2E reproducible"
git tag v1.0
git push --tags
```

Para deploy en Streamlit Community Cloud:
1. streamlit.io/cloud → "New app".
2. Conecta el repo.
3. Main file: `streamlit_app.py`.
4. Deploy. URL pública en 2 min.

### Entregable

- Repo Git con la estructura completa (al menos 4 archivos en src/, Makefile, requirements.txt, README, 1 test).
- Tag `v1.0` creado.
- Captura de Streamlit corriendo (local o Cloud).
- Reporte de 1 página: "qué armé, qué quedó pendiente, qué aprendí".

### Rúbrica corta

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Estructura del repo | plana | con src/ y data/ | la canónica completa |
| Makefile | sin | con targets | + comentarios + `make all` corre |
| Tests | sin | uno | 3+ con assert |
| Streamlit corre | local crashea | local OK | + Cloud accesible |
| README ejecutable | confuso | con steps | + métricas + limitaciones |

### Conexión con el case y cierre del manual

Este pipeline es **el cierre del Manual 5**. Lo que comenzó en U1 como un script de 50 líneas (cargar CSV) hoy es un **producto reproducible** que cualquiera con tu repo puede levantar en 5 minutos. Los próximos pasos no son técnicos, son de **adopción**: que coordinación use la app, que recoja feedback, que mida impacto. Has completado el viaje "de cero programación a app desplegada". Ahora tu pipeline va al mundo.
::/albatros
