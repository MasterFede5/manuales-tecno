---
unidad: 4
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Unidad 04

::albatros{titulo="Entrena tu primer modelo baseline (regresión lineal)" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Antes de modelos sofisticados, ¿qué tan buena es una **regresión lineal de 1 línea** sobre tu dataset escolar? Spoiler: a veces sorprende.

**Contexto del case.** El temario marca esta unidad como "estadística", pero la estadística aplicada se traduce en un **baseline de regresión** que servirá de piso comparativo en U5. Si Random Forest no le gana al baseline por al menos 5 puntos, no vale la pena la complejidad.

### Materiales

- Python 3 + pandas + numpy + scikit-learn (sí, anticipamos U5).
- Notebook (Jupyter / Colab).
- Dataset limpio de U2.

### Pasos del taller (60 min)

**Paso 1 — Cargar y revisar los datos (5 min).**

```python
import pandas as pd
import numpy as np

df = pd.read_csv("dataset_escolar_limpio.csv")
print(df.describe())
print(f"\nCorrelación con cal_final:")
print(df[["horas_estudio", "asistencia", "cal_anterior", "cal_final"]]
      .corr()["cal_final"].sort_values(ascending=False))
```

**Paso 2 — Análisis estadístico defendible (10 min).**

```python
# 1. Tendencia central
print(f"Cal. final · media: {df['cal_final'].mean():.2f}, "
      f"mediana: {df['cal_final'].median():.2f}, "
      f"std: {df['cal_final'].std():.2f}")

# 2. Percentiles
print(df["cal_final"].quantile([0.10, 0.25, 0.50, 0.75, 0.90]))

# 3. Outliers IQR
q1, q3 = df["cal_final"].quantile([0.25, 0.75])
iqr = q3 - q1
outs = df[(df["cal_final"] < q1 - 1.5*iqr) | (df["cal_final"] > q3 + 1.5*iqr)]
print(f"Outliers: {len(outs)}")
```

**Paso 3 — Baseline mental (5 min).**

Antes de entrenar, calcula el "baseline tonto": predecir siempre la media. Si tu modelo no le gana, está roto.

```python
y = df["cal_final"]
y_pred_tonto = np.full(len(y), y.mean())
mae_tonto = np.abs(y - y_pred_tonto).mean()
print(f"Baseline tonto · MAE: {mae_tonto:.3f}")
```

**Paso 4 — Regresión lineal con sklearn (15 min).**

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

X = df[["horas_estudio", "asistencia", "cal_anterior"]]
y = df["cal_final"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nModelo lineal · MAE: {mae:.3f} · R²: {r2:.3f}")
print(f"\nCoeficientes:")
for col, coef in zip(X.columns, modelo.coef_):
    print(f"  {col}: {coef:+.3f}")
print(f"  intercepto: {modelo.intercept_:+.3f}")
```

Output esperado:
```
Modelo lineal · MAE: 0.65 · R²: 0.61

Coeficientes:
  horas_estudio:  +0.232
  asistencia:     +1.847
  cal_anterior:   +0.512
  intercepto:     +0.089
```

**Paso 5 — Interpretar coeficientes (10 min).**

Cada coeficiente lee así:
- `+0.232` en `horas_estudio`: cada hora extra/sem suma 0.232 a la cal predicha (manteniendo otras fijas).
- `+1.847` en `asistencia`: pasar de asistencia 0.5 a 1.0 suma 0.92 puntos.
- `+0.512` en `cal_anterior`: cada punto extra en cal anterior suma 0.5 a la predicción.

> **Advertencia.** Estos son coeficientes **descriptivos** (ajustan al patrón observado), NO **causales** (no prueban que aumentar horas cause mejor cal). Para causalidad necesitas experimento.

**Paso 6 — Visualizar predicciones vs reales (10 min).**

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(y_test, y_pred, alpha=0.5, color="#0E3A8A")
ax.plot([0, 10], [0, 10], color="red", linestyle="--", label="Predicción perfecta")
ax.set_xlabel("Cal real")
ax.set_ylabel("Cal predicha")
ax.set_title(f"Predicciones lineal · MAE={mae:.2f} · R²={r2:.2f}",
             fontsize=14, fontweight="bold")
ax.legend()
plt.savefig("predicciones_lineal.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Paso 7 — Reporte ejecutivo (5 min).** Cierra con un párrafo (3-5 líneas) defendible:

> "Un modelo lineal con 3 features (horas, asistencia, cal_anterior) explica el 61% de la varianza de la calificación final con MAE 0.65. Esto significa: en promedio nos equivocamos por 0.65 puntos. cal_anterior es el predictor más estable, asistencia es el segundo. Recomendación: usar este modelo como baseline mientras exploramos algoritmos más sofisticados en U5."

### Entregable

- Notebook con las 7 secciones.
- `predicciones_lineal.png`.
- Reporte ejecutivo (1 párrafo) con MAE, R² y recomendación.

### Rúbrica corta

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Análisis estadístico previo | sin | descriptivos | + percentiles + IQR |
| Baseline tonto | sin | calculado | comparado contra modelo |
| Modelo entrenado | crashea | corre | + coeficientes interpretados |
| Visualización pred vs real | sin | scatter básico | + diagonal + métricas en título |
| Reporte ejecutivo | confuso | con números | defendible y honesto sobre causalidad |

### Conexión con el case

Este es el **piso comparativo** para U5. Cuando entrenes Random Forest, Lineal y Árbol allí, vas a comparar cada uno contra **este MAE 0.65 y R² 0.61**. Si un modelo "complejo" no le gana al lineal, tira la complejidad y úsate este: más simple, más interpretable, más defendible.
::/albatros
