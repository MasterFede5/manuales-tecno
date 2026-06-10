---
unidad: 6
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Unidad 06

::albatros{titulo="K-fold CV y comparación rigurosa de 3 modelos sobre el dataset escolar" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si tu Random Forest gana en test pero pierde en CV, ¿en cuál confías para producción?

**Contexto del case.** En U5 entrenaste 3 modelos y los comparaste con un solo split. Hoy aplicas validación rigurosa con K-Fold y elaboras una **tabla defendible** ante un comité técnico. La unidad nominal es clustering pero el taller práctica el oficio cruzado: validación robusta + métricas múltiples.

### Materiales

- Python 3 + pandas + numpy + scikit-learn + matplotlib.
- Notebook (Jupyter / Colab).
- Dataset limpio de U2.
- Modelos exportados de U5 (opcional).

### Pasos del taller (60 min)

**Paso 1 — Cargar y preparar (5 min).**

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score, KFold
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import make_scorer, mean_absolute_error, r2_score

df = pd.read_csv("dataset_escolar_limpio.csv")
X = df[["horas_estudio", "asistencia", "cal_anterior"]]
y = df["cal_final"]
print(f"Shape: {X.shape}")
```

**Paso 2 — Definir 3 modelos con scaling apropiado (10 min).**

```python
modelos = {
    "Lineal": Pipeline([("scaler", StandardScaler()),
                         ("model", LinearRegression())]),
    "Árbol-d4": DecisionTreeRegressor(max_depth=4, random_state=42),
    "RF-d8-leaf20": RandomForestRegressor(
        n_estimators=200, max_depth=8, min_samples_leaf=20, random_state=42
    ),
}
```

**Paso 3 — K-Fold con 3 métricas distintas (15 min).**

```python
kf = KFold(n_splits=5, shuffle=True, random_state=42)

resultados = []
for nombre, modelo in modelos.items():
    r2s = cross_val_score(modelo, X, y, cv=kf, scoring="r2")
    maes = -cross_val_score(modelo, X, y, cv=kf, scoring="neg_mean_absolute_error")
    rmses = -cross_val_score(modelo, X, y, cv=kf, scoring="neg_root_mean_squared_error")
    resultados.append({
        "modelo": nombre,
        "R²_mean": r2s.mean().round(3),
        "R²_std": r2s.std().round(3),
        "MAE_mean": maes.mean().round(3),
        "MAE_std": maes.std().round(3),
        "RMSE_mean": rmses.mean().round(3),
        "RMSE_std": rmses.std().round(3),
        "R²_min": r2s.min().round(3),
        "R²_max": r2s.max().round(3),
    })

tabla = pd.DataFrame(resultados)
print(tabla.to_string(index=False))
tabla.to_csv("comparacion_modelos.csv", index=False)
```

**Paso 4 — Test estadístico de diferencia (10 min).**

¿La diferencia entre el ganador y el segundo es **estadísticamente significativa** o ruido?

```python
from scipy import stats

# Tomar los R² de cada fold para los 2 mejores
r2_lin = cross_val_score(modelos["Lineal"], X, y, cv=kf, scoring="r2")
r2_rf = cross_val_score(modelos["RF-d8-leaf20"], X, y, cv=kf, scoring="r2")

diff = r2_rf - r2_lin
print(f"\nDiferencia RF − Lineal por fold: {diff.round(3)}")
print(f"Media diff: {diff.mean():.3f}")

# Test t pareado (5 folds, n=5)
t, p = stats.ttest_rel(r2_rf, r2_lin)
print(f"t-test pareado: t={t:.3f}, p={p:.4g}")
if p < 0.05:
    print("Diferencia significativa: RF gana de forma defendible.")
else:
    print("Diferencia NO significativa: la simplicidad lineal es preferible.")
```

**Paso 5 — Visualización comparativa (10 min).**

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Boxplot de R² por modelo
r2_data = []
labels = []
for nombre, modelo in modelos.items():
    r2 = cross_val_score(modelo, X, y, cv=kf, scoring="r2")
    r2_data.append(r2)
    labels.append(nombre)
axes[0].boxplot(r2_data, tick_labels=labels)
axes[0].set_title("Distribución R² (5 folds)")
axes[0].set_ylabel("R²")
axes[0].grid(True, alpha=0.3)

# Bar chart de MAE
mae_means = [m["MAE_mean"] for m in resultados]
mae_stds = [m["MAE_std"] for m in resultados]
axes[1].bar(labels, mae_means, yerr=mae_stds, capsize=5,
            color=["#0E3A8A", "#1E5BB8", "#F39C12"])
axes[1].set_title("MAE promedio (5 folds, ±std)")
axes[1].set_ylabel("MAE")
axes[1].grid(True, alpha=0.3, axis="y")

plt.tight_layout()
plt.savefig("comparacion_cv.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Paso 6 — Decisión defendible (5 min).**

Combina criterios: R² medio + estabilidad (std) + costo computacional + interpretabilidad.

| Criterio | Peso | Lineal | Árbol | RF |
|---|---|---|---|---|
| R² medio | 30% | 0.61 | 0.65 | 0.70 |
| Estabilidad (1 - std) | 20% | alta | media | media |
| Interpretabilidad | 25% | alta | alta | baja |
| Costo train | 15% | mínimo | bajo | medio |
| Costo inferencia | 10% | mínimo | bajo | medio |

**Paso 7 — Reporte para coordinación (5 min).**

> "Comparamos 3 modelos con K-Fold 5-folds sobre 465 alumnos. Random Forest (R² 0.70 ± 0.04) gana sobre Lineal (R² 0.61 ± 0.04) por 0.09; t-pareado p = 0.018 (significativo). Sin embargo, la diferencia operativa en MAE es 0.55 vs 0.65, ~0.1 puntos de calificación. Recomendamos: **Lineal** como modelo de referencia por interpretabilidad; **RF** como modelo de producción cuando coordinación priorice precisión sobre explicabilidad."

### Entregable

- Notebook con los 7 pasos.
- `comparacion_modelos.csv` y `comparacion_cv.png`.
- Reporte de 1 página con decisión justificada y t-test reportado.

### Rúbrica corta

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| K-Fold aplicado | con un fold solo | 5-fold | con shuffle + seed reproducible |
| Métricas múltiples | una | dos | 3+ con std reportada |
| Test de significancia | sin | mencionado | t-pareado calculado e interpretado |
| Visualización | una | dos | boxplot + bar con std |
| Decisión final | "uso el mejor R²" | con criterios | matriz multi-criterio defendible |

### Conexión con el case

Este es el **comité de selección de modelo** del Predictor de Rendimiento. La tabla y el t-test que produjiste hoy son **el documento que coordinación firma** para autorizar el modelo de producción. Sin esta validación rigurosa, cualquier "ganador" en un solo split podría ser suerte.
::/albatros
