---
unidad: 5
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Unidad 05

::albatros{titulo="Clasifica aprobado/reprobado con regresión logística + matriz de confusión" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si tu modelo identifica correctamente al **80% de los alumnos en riesgo** un mes antes del examen, ¿qué intervención harías?

**Contexto del case.** En U4 hiciste regresión (predecir nota numérica). Hoy haces **clasificación binaria**: aprueba/reprueba. Es lo que coordinación realmente necesita para activar tutorías. Métrica clave: **recall** sobre la clase "reprueba" (no se nos puede escapar un alumno en riesgo).

### Materiales

- Python 3 + pandas + numpy + scikit-learn + matplotlib + seaborn.
- Notebook (Jupyter / Colab).
- Dataset limpio de U2.

### Pasos del taller (60 min)

**Paso 1 — Preparar dataset binario (5 min).**

```python
import pandas as pd
import numpy as np

df = pd.read_csv("dataset_escolar_limpio.csv")

# Crear target binario
df["aprueba"] = (df["cal_final"] >= 6).astype(int)

# Verificar balance de clases
print("Balance:")
print(df["aprueba"].value_counts(normalize=True).round(3))
print(f"\nClase 0 (reprueba): {(df['aprueba']==0).sum()}")
print(f"Clase 1 (aprueba): {(df['aprueba']==1).sum()}")
```

Output esperado: ~81% aprueba, ~19% reprueba (desbalanceado).

**Paso 2 — Split estratificado (5 min).**

```python
from sklearn.model_selection import train_test_split

X = df[["horas_estudio", "asistencia", "cal_anterior"]]
y = df["aprueba"]

X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.2, random_state=42,
    stratify=y                              # mantiene proporción de clases
)
print(f"Train: {len(X_tr)} · Test: {len(X_te)}")
print(f"Balance test: {y_te.value_counts(normalize=True).round(3).to_dict()}")
```

**Paso 3 — Entrenar regresión logística (10 min).**

```python
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Pipeline con scaler (logistic se beneficia de scaling)
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000, random_state=42))
])

pipe.fit(X_tr, y_tr)

y_pred = pipe.predict(X_te)
y_proba = pipe.predict_proba(X_te)[:, 1]   # probabilidad de aprueba
```

**Paso 4 — Métricas y matriz de confusión (15 min).**

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score
)

print(f"Accuracy:  {accuracy_score(y_te, y_pred):.3f}")
print(f"Precision: {precision_score(y_te, y_pred):.3f}")
print(f"Recall:    {recall_score(y_te, y_pred):.3f}")
print(f"F1:        {f1_score(y_te, y_pred):.3f}")
print(f"AUC:       {roc_auc_score(y_te, y_proba):.3f}")

print(f"\nReporte completo:")
print(classification_report(y_te, y_pred,
      target_names=["Reprueba", "Aprueba"]))

# Matriz de confusión visual
import matplotlib.pyplot as plt
import seaborn as sns

cm = confusion_matrix(y_te, y_pred)
fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Reprueba", "Aprueba"],
            yticklabels=["Reprueba", "Aprueba"], ax=ax)
ax.set_xlabel("Predicho")
ax.set_ylabel("Real")
ax.set_title("Matriz de confusión", fontsize=13, fontweight="bold")
plt.savefig("confusion.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Paso 5 — Interpretación de la matriz (10 min).**

Lee tu matriz así (con números aproximados esperados):

```
                  Pred Reprueba   Pred Aprueba
Real Reprueba         12 (TN)        6 (FP)
Real Aprueba           3 (FN)       72 (TP)
```

- **TP=72**: aprueba reales que el modelo dijo aprueba ✓.
- **TN=12**: reprueba reales identificados ✓.
- **FN=3**: alumnos que **reprobaron** pero el modelo dijo aprueba — **estos son los costosos**, los que se nos escaparon de tutoría.
- **FP=6**: alumnos que **aprobaron** pero modelo dijo reprueba — los citaste a tutoría innecesariamente.

Costo de FN >> costo de FP en este case. Coordinación prefiere intervenir 6 alumnos extra que perder 3 reales.

**Paso 6 — Bajar threshold para subir recall sobre la clase reprueba (10 min).**

```python
# y_proba es la prob de "aprueba". Para detectar reprueba con más recall, 
# bajamos el threshold (más casos clasificados como reprueba).
import numpy as np

# Probabilidad de reprueba = 1 - prob_aprueba
prob_reprueba = 1 - y_proba

for th in [0.3, 0.4, 0.5, 0.6, 0.7]:
    y_th = (prob_reprueba > th).astype(int)
    # invertimos: 1 = reprueba en este experimento
    y_te_inv = (y_te == 0).astype(int)
    rec = recall_score(y_te_inv, y_th)
    pre = precision_score(y_te_inv, y_th, zero_division=0)
    print(f"Threshold {th}: precision_reprueba={pre:.3f}, recall_reprueba={rec:.3f}")
```

Output típico:
```
Threshold 0.3: precision=0.45, recall=0.95
Threshold 0.4: precision=0.55, recall=0.85
Threshold 0.5: precision=0.66, recall=0.67   ← default
Threshold 0.6: precision=0.78, recall=0.45
Threshold 0.7: precision=0.85, recall=0.30
```

**Decisión:** si quieres atrapar 95% de los reprobados, baja threshold a 0.3 (a costa de citar a más falsos positivos).

**Paso 7 — Reporte para coordinación (5 min).**

Cierra con una recomendación concreta:

> "Modelo logístico con 3 features alcanza accuracy 84%, AUC 0.89. A threshold default detecta 67% de los alumnos en riesgo; bajando threshold a 0.3 detectamos 95% al costo de 8 falsas alertas (alumnos citados a tutoría que igual aprueban). Recomendación: usar threshold 0.4 — recall 85% con precision 55% — balance razonable para programa de tutorías."

### Entregable

- Notebook con los 7 pasos.
- `confusion.png`.
- Tabla de threshold sweep.
- Recomendación de threshold operativo con justificación.

### Rúbrica corta

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Target binario | sin crear | con threshold | con balance verificado |
| Pipeline | sin scaler | con scaler | + max_iter ajustado |
| Métricas | solo accuracy | 4 métricas | + AUC + matriz |
| Threshold sweep | sin | una alternativa | tabla 5 thresholds |
| Recomendación | "uso default" | con métrica | + costo FN/FP justificado |

### Conexión con el case

Este clasificador es **el modelo que va a producir las alertas tempranas** del Predictor de Rendimiento. En U6 vas a segmentar a esos alumnos en perfiles (clusters); en U7 verás si una red neuronal lo mejora; en U8 lo expones por API/Streamlit con explicación generativa. La elección de threshold de hoy define cuántas alertas semanales recibirá coordinación.
::/albatros
