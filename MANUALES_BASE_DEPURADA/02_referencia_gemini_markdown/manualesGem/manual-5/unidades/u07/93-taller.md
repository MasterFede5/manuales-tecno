---
unidad: 7
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Unidad 07

::albatros{titulo="Exporta tu modelo entrenado y crea una API simple con FastAPI" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Tu modelo está entrenado. ¿Cómo lo expones para que **otra persona** lo use sin abrir tu notebook?

**Contexto del case.** El temario de U7 es "redes neuronales" pero el oficio práctico que necesitas para U8 es **deployment**: persistir el modelo y exponerlo por API. Hoy combinas ambos: entrenas un MLP rápido y lo expones con FastAPI.

### Materiales

- Python 3 + torch + scikit-learn + joblib + fastapi + uvicorn.
- Instalación: `pip install torch scikit-learn joblib fastapi uvicorn`
- Notebook + editor (VS Code recomendado para el `.py` final).
- Dataset limpio de U2.

### Pasos del taller (60 min)

**Paso 1 — Entrenar y persistir un MLP simple (15 min).**

`train.py`:

```python
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

df = pd.read_csv("dataset_escolar_limpio.csv")
X = df[["horas_estudio", "asistencia", "cal_anterior"]].values
y = df["cal_final"].values

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler().fit(X_tr)
X_tr_s = scaler.transform(X_tr)
X_te_s = scaler.transform(X_te)

# MLP
model = nn.Sequential(
    nn.Linear(3, 16), nn.ReLU(),
    nn.Linear(16, 8), nn.ReLU(),
    nn.Linear(8, 1)
)
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
criterion = nn.MSELoss()

X_t = torch.tensor(X_tr_s, dtype=torch.float32)
y_t = torch.tensor(y_tr, dtype=torch.float32).unsqueeze(1)

for epoch in range(300):
    model.train()
    optimizer.zero_grad()
    pred = model(X_t)
    loss = criterion(pred, y_t)
    loss.backward()
    optimizer.step()
    if epoch % 50 == 0:
        print(f"Epoch {epoch}: loss={loss.item():.4f}")

# Guardar
torch.save(model.state_dict(), "mlp_state.pt")
joblib.dump(scaler, "scaler.pkl")

# Schema (orden de features) — crítico para inferencia
import json
with open("schema.json", "w") as f:
    json.dump({"features": ["horas_estudio", "asistencia", "cal_anterior"]}, f)

print("✓ Modelo + scaler + schema guardados")
```

**Paso 2 — Inferencia local con script (5 min).**

`predict.py`:

```python
import torch
import torch.nn as nn
import numpy as np
import joblib
import json

with open("schema.json") as f:
    schema = json.load(f)

scaler = joblib.load("scaler.pkl")

# Reconstruir arquitectura idéntica al training
model = nn.Sequential(
    nn.Linear(3, 16), nn.ReLU(),
    nn.Linear(16, 8), nn.ReLU(),
    nn.Linear(8, 1)
)
model.load_state_dict(torch.load("mlp_state.pt"))
model.eval()

def predecir(features_dict):
    """Recibe dict, devuelve cal_final predicha."""
    x = np.array([[features_dict[k] for k in schema["features"]]])
    x_s = scaler.transform(x)
    with torch.no_grad():
        pred = model(torch.tensor(x_s, dtype=torch.float32))
    return float(pred.item())

# Test
ejemplo = {"horas_estudio": 4.0, "asistencia": 0.85, "cal_anterior": 7.0}
print(f"Predicción: {predecir(ejemplo):.2f}")
```

**Paso 3 — Crear API con FastAPI (15 min).**

`api.py`:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import torch
import torch.nn as nn
import numpy as np
import joblib
import json

app = FastAPI(title="Predictor Escolar API", version="1.0")

# Cargar artefactos al inicio (1 sola vez)
with open("schema.json") as f:
    schema = json.load(f)
scaler = joblib.load("scaler.pkl")

model = nn.Sequential(
    nn.Linear(3, 16), nn.ReLU(),
    nn.Linear(16, 8), nn.ReLU(),
    nn.Linear(8, 1)
)
model.load_state_dict(torch.load("mlp_state.pt"))
model.eval()

class Alumno(BaseModel):
    horas_estudio: float = Field(..., ge=0, le=24)
    asistencia: float = Field(..., ge=0, le=1)
    cal_anterior: float = Field(..., ge=0, le=10)

@app.get("/")
def root():
    return {"servicio": "Predictor Escolar Albatros", "version": "1.0"}

@app.post("/predecir")
def predecir(alumno: Alumno):
    try:
        x = np.array([[
            alumno.horas_estudio,
            alumno.asistencia,
            alumno.cal_anterior
        ]])
        x_s = scaler.transform(x)
        with torch.no_grad():
            pred = model(torch.tensor(x_s, dtype=torch.float32))
        cal = float(pred.item())
        riesgo = "alto" if cal < 6 else ("medio" if cal < 7.5 else "bajo")
        return {
            "calificacion_predicha": round(cal, 2),
            "riesgo": riesgo,
            "input": alumno.model_dump(),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
```

**Paso 4 — Levantar servidor (5 min).**

```bash
uvicorn api:app --reload --port 8000
```

Salida esperada:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

**Paso 5 — Probar la API (10 min).**

Opción A: navegador → `http://127.0.0.1:8000/docs` (Swagger UI generado por FastAPI).

Opción B: con `curl`:
```bash
curl -X POST http://127.0.0.1:8000/predecir \
  -H "Content-Type: application/json" \
  -d '{"horas_estudio": 4.0, "asistencia": 0.85, "cal_anterior": 7.0}'
```

Output esperado:
```json
{
  "calificacion_predicha": 7.34,
  "riesgo": "medio",
  "input": {"horas_estudio": 4.0, "asistencia": 0.85, "cal_anterior": 7.0}
}
```

Opción C: cliente Python:
```python
import requests
r = requests.post("http://127.0.0.1:8000/predecir",
                  json={"horas_estudio": 2.0, "asistencia": 0.6,
                        "cal_anterior": 5.5})
print(r.json())
```

**Paso 6 — Probar validación automática (5 min).**

Envía un input inválido (asistencia > 1):
```bash
curl -X POST http://127.0.0.1:8000/predecir \
  -H "Content-Type: application/json" \
  -d '{"horas_estudio": 4.0, "asistencia": 1.5, "cal_anterior": 7.0}'
```

FastAPI/Pydantic responde **automáticamente** con error 422 explicando que `asistencia` debe ser ≤ 1. Sin escribir código de validación tú.

**Paso 7 — Reto extra (5 min).** Agrega endpoint `/batch` que reciba una lista de alumnos y devuelva una lista de predicciones.

### Entregable

- 4 archivos: `train.py`, `predict.py`, `api.py`, `schema.json` + `mlp_state.pt` + `scaler.pkl`.
- Captura de Swagger UI funcionando.
- Captura del POST con respuesta exitosa y POST con error 422.

### Rúbrica corta

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Modelo entrenado y persistido | crashea | corre | + schema.json explícito |
| Predict.py | sin scaler | con scaler | con schema validado |
| API levanta | no levanta | corre | + Swagger UI accesible |
| Validación inputs | sin | básica | rangos pydantic |
| Endpoints adicionales | solo `/predecir` | + health | + batch funcional |

### Conexión con el case

Esta API es **el motor que U8 va a llamar** desde Streamlit. La unidad 7 oficial es "redes neuronales", pero la práctica del oficio te exige saber **exponer modelos**. Con FastAPI + uvicorn, un modelo entrenado pasa de "código de notebook" a "servicio que cualquiera consume". Es el paso entre ML experimental y ML operacional.
::/albatros
