---
unidad: 5
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 05

::practica{titulo="Predictor de calificaciones con 3 modelos comparados"}
**Problema.** Construir 3 predictores (regresión lineal, árbol, Random Forest), compararlos y elegir el mejor para producción.

**Paso 1 — Estrategia.** Pipeline completo: features → split → entrenar 3 modelos → evaluar → comparar → elegir.

**Paso 2 — Código.**

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("dataset_escolar_limpio.csv")
X = df[["horas_estudio", "asistencia", "cal_anterior"]]
y = df["cal_final"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelos = {
    "Regresión Lineal": LinearRegression(),
    "Árbol (depth=4)": DecisionTreeRegressor(max_depth=4, random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
}

resultados = []
for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    
    # Performance train y test
    train_score = modelo.score(X_train, y_train)
    test_score = modelo.score(X_test, y_test)
    
    # Predicciones test
    y_pred = modelo.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    # CV
    cv_scores = cross_val_score(modelo, X, y, cv=5, scoring="r2")
    
    resultados.append({
        "modelo": nombre,
        "R² train": round(train_score, 3),
        "R² test": round(test_score, 3),
        "RMSE test": round(rmse, 3),
        "CV R² mean": round(cv_scores.mean(), 3),
        "CV R² std": round(cv_scores.std(), 3),
        "Gap train-test": round(train_score - test_score, 3)
    })

resultados_df = pd.DataFrame(resultados)
print(resultados_df.to_string(index=False))
```

**Paso 3 — Output.**
```
            modelo  R² train  R² test  RMSE test  CV R² mean  CV R² std  Gap train-test
  Regresión Lineal     0.625    0.612      0.890       0.617      0.043           0.013
   Árbol (depth=4)     0.731    0.654      0.836       0.642      0.057           0.077
     Random Forest     0.952    0.715      0.764       0.701      0.041           0.237
```

**Paso 4 — Análisis.**
- **Lineal**: bajo train Y test → underfitting moderado, pero estable (gap 0.013).
- **Árbol**: mejor que lineal en test, gap pequeño (0.077). Bueno.
- **Random Forest**: mejor RMSE pero gap grande (0.237) → overfitting evidente. CV mean 0.701 confirma que no es solo train.

**Paso 5 — Recomendación.**
- Si **interpretabilidad** es prioridad: Regresión Lineal (ecuación clara).
- Si **precisión** es prioridad y aceptas algo de gap: Random Forest.
- **Balance**: Árbol de decisión con depth=4 (interpretable + decente).

Para producción institucional: Random Forest con regularización adicional (`max_depth=8`, `min_samples_leaf=20`) para reducir gap.

**Paso 6 — Modelo final.**
```python
modelo_final = RandomForestRegressor(
    n_estimators=200,
    max_depth=8,
    min_samples_leaf=20,
    random_state=42
)
modelo_final.fit(X_train, y_train)

# Guardar
import joblib
joblib.dump(modelo_final, "modelo_predictor_v1.pkl")
```

**Paso 7 — Predicciones nuevas.**
```python
nuevo_alumno = pd.DataFrame([{
    "horas_estudio": 5.0,
    "asistencia": 0.92,
    "cal_anterior": 7.5
}])
print(f"Predicción: {modelo_final.predict(nuevo_alumno)[0]:.2f}")
```

**Verificación.** Repetir con random_state distintos para confirmar estabilidad del modelo.

**Lección.** Las 8 técnicas de la unidad encajan: pipeline disciplinado, train/test, métricas correctas, comparación de modelos, diagnóstico de sobreajuste. La precisión bruta no es lo único: gap train-test, interpretabilidad y estabilidad importan en producción.
::/practica

---

## Práctica resuelta 2 — Curva de aprendizaje para diagnosticar bias-variance

::practica{titulo="¿Más datos o más modelo? Diagnóstico con learning curve"}
**Problema.** Tu modelo da R² test = 0.65. Coordinación pregunta: "¿conviene recolectar más alumnos para el dataset?". Una **curva de aprendizaje** te lo dice.

**Paso 1 — Estrategia.** Entrenar el mismo modelo con tamaños crecientes del training set (10%, 25%, 50%, 75%, 100%) y graficar R² train y test en cada caso.

**Paso 2 — Código.**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("dataset_escolar_limpio.csv")
X = df[["horas_estudio", "asistencia", "cal_anterior"]]
y = df["cal_final"]

modelo = RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42)

train_sizes, train_scores, val_scores = learning_curve(
    modelo, X, y,
    train_sizes=np.linspace(0.1, 1.0, 8),
    cv=5,
    scoring="r2",
    random_state=42
)

train_mean = train_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
val_mean = val_scores.mean(axis=1)
val_std = val_scores.std(axis=1)

# Visualizar
fig, ax = plt.subplots(figsize=(11, 6))
ax.plot(train_sizes, train_mean, "o-", color="#0E3A8A", label="Train R²")
ax.fill_between(train_sizes, train_mean - train_std, train_mean + train_std,
                alpha=0.2, color="#0E3A8A")
ax.plot(train_sizes, val_mean, "s-", color="#F39C12", label="CV R²")
ax.fill_between(train_sizes, val_mean - val_std, val_mean + val_std,
                alpha=0.2, color="#F39C12")
ax.set_xlabel("Tamaño del training set")
ax.set_ylabel("R²")
ax.set_title("Curva de aprendizaje · Random Forest",
             fontsize=14, fontweight="bold")
ax.legend(loc="lower right")
ax.grid(True, alpha=0.3)
plt.savefig("learning_curve.png", dpi=200, bbox_inches="tight")
plt.show()

# Diagnóstico automático
gap_final = train_mean[-1] - val_mean[-1]
print(f"\nR² train final: {train_mean[-1]:.3f}")
print(f"R² CV final:    {val_mean[-1]:.3f}")
print(f"Gap final:      {gap_final:.3f}")
print(f"Slope CV últimos 3 puntos: {val_mean[-1] - val_mean[-3]:.3f}")
```

**Paso 3 — Cómo leer la curva.**

Tres patrones canónicos:

| Patrón | Train alto, CV bajo | Train ≈ CV ambos bajos | Train alto, CV subiendo |
|---|---|---|---|
| Diagnóstico | Overfit / alta varianza | Underfit / alto sesgo | Más datos seguirían ayudando |
| Solución | Más datos · regularizar · simplificar | Modelo más complejo · más features | Recolectar |

**Paso 4 — Decisión basada en la slope final.**

```python
slope = val_mean[-1] - val_mean[-3]
if abs(slope) < 0.005:
    decision = "CV plateau: más datos NO ayuda. Cambia algoritmo o features."
elif slope > 0.02:
    decision = "CV sube: SÍ ayuda más datos. Recolecta más alumnos."
else:
    decision = "CV sube ligero. Ayuda marginal de más datos."
print(f"\nDecisión: {decision}")
```

**Paso 5 — Verificación.** Repite con `LinearRegression` (más simple). Si su CV es plana en un valor más bajo y el gap es chico, confirma que para ese modelo, "más datos no rescata"; necesitarías features más informativos o algoritmo más expresivo.

**Lección.** La curva de aprendizaje **separa el problema de modelado** (más complejidad ayudaría) **del problema de datos** (más alumnos ayudaría). Sin esta gráfica, coordinación gasta meses recolectando datos cuando el modelo ya tocó techo. O al revés: cambia de modelo en lugar de buscar más datos.
::/practica

---

## Práctica resuelta 3 — Hyperparameter tuning con GridSearchCV

::practica{titulo="Encontrar la mejor combinación de hiperparámetros sin sobreajustar"}
**Problema.** Tu Random Forest tiene 5 hiperparámetros que afectan resultado. Probarlos a mano no escala. `GridSearchCV` lo hace por ti, validando con CV para no engañarse.

**Paso 1 — Estrategia.** Definir grid de combinaciones, dejar que sklearn pruebe todas con CV 5-fold, recibir el ganador.

**Paso 2 — Código.**

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("dataset_escolar_limpio.csv")
X = df[["horas_estudio", "asistencia", "cal_anterior"]]
y = df["cal_final"]

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

# Grid de hiperparámetros
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [4, 6, 8, None],
    "min_samples_leaf": [1, 5, 10, 20],
}

# Total combinaciones: 3 * 4 * 4 = 48 (× 5 folds CV = 240 fits)
print(f"Combinaciones: "
      f"{len(param_grid['n_estimators']) * len(param_grid['max_depth']) * len(param_grid['min_samples_leaf'])}")

modelo_base = RandomForestRegressor(random_state=42)

grid = GridSearchCV(
    modelo_base,
    param_grid,
    cv=5,
    scoring="r2",
    n_jobs=-1,        # usar todos los cores
    verbose=1
)

grid.fit(X_tr, y_tr)

print(f"\nMejores hiperparámetros: {grid.best_params_}")
print(f"Mejor R² CV: {grid.best_score_:.4f}")

# Evaluar en test (no tocado por GridSearch)
mejor = grid.best_estimator_
y_pred = mejor.predict(X_te)
print(f"\nR² test: {r2_score(y_te, y_pred):.4f}")
print(f"MAE test: {mean_absolute_error(y_te, y_pred):.3f}")

# Top 5 combinaciones
import pandas as pd
res = pd.DataFrame(grid.cv_results_)
top = res.nlargest(5, "mean_test_score")[
    ["param_n_estimators", "param_max_depth",
     "param_min_samples_leaf", "mean_test_score", "std_test_score"]
]
print(f"\nTop 5 combinaciones:")
print(top.to_string(index=False))
```

**Paso 3 — Output esperado.**
```
Combinaciones: 48
Fitting 5 folds for each of 48 candidates, totalling 240 fits

Mejores hiperparámetros: {'max_depth': 8, 'min_samples_leaf': 10, 'n_estimators': 200}
Mejor R² CV: 0.7053

R² test: 0.7124
MAE test: 0.612
```

**Paso 4 — Validar que NO hay leakage.** Dos checks:
- `R² test ≈ R² CV`: si test mucho mejor, sospecha leakage en split.
- Repetir con `random_state` distinto: la ganadora cambia un poco pero los hiperparámetros relevantes permanecen.

**Paso 5 — Verificación de tiempo y costo.** En este dataset (~370 filas train, 48 combinaciones, 5 folds): ~30-60 segundos en laptop. Si tu grid crece (200+ combinaciones), considera `RandomizedSearchCV` o `HalvingGridSearchCV`.

**Paso 6 — Guardar el modelo final.**

```python
import joblib
joblib.dump(mejor, "modelo_predictor_v2_tuneado.pkl")
print("✓ modelo_predictor_v2_tuneado.pkl guardado")
```

**Lección.** GridSearch es la herramienta básica pero potente para tuning. Reglas pragmáticas:
- Empieza con grids pequeños (3-4 valores por hiperparámetro).
- Usa CV 5-fold (no test set) para no contaminar.
- Mira la **std** de los scores: si es alta, el modelo es inestable, no solo sub-óptimo.
- Confirma en test que el ganador generaliza.
::/practica
