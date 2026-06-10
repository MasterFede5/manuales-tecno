---
unidad: 5
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 05

::practica{titulo="Predictor de calificaciones con 3 modelos comparados"}
**Problema.** Construir 3 predictores, compararlos y elegir el mejor.
- Modelos: Regresión lineal, Árbol, Random Forest.
- Objetivo: Predecir calificaciones y elegir el modelo óptimo.

**Paso 1 — Estrategia.**
- Preparamos *features* y separamos los datos (split).
- Entrenamos los 3 modelos.
- Evaluamos, comparamos y elegimos.

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
- **Lineal**: Bajo en train y test. Tiene *underfitting* moderado, pero es estable.
- **Árbol**: Mejor que lineal en test, con un *gap* pequeño. Buen balance.
- **Random Forest**: Mejor RMSE, pero el gran *gap* indica *overfitting*.

**Paso 5 — Recomendación.**
- **Interpretabilidad**: Elige Regresión Lineal.
- **Precisión máxima**: Elige Random Forest (aceptando cierto *overfitting*).
- **Balance general**: Árbol de decisión.

::interioriza
Imagina que los modelos son trajes a medida.
- La **Regresión Lineal** es una talla única: no queda perfecta, pero es barata y predecible.
- El **Random Forest** es un sastre hiper-detallista: el traje te queda perfecto hoy, pero si subes 1 kg mañana no te cerrará (*overfitting*).
- El **Árbol de Decisión** es un elástico: adaptable y razonablemente cómodo para varias situaciones.
::

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

**Verificación.** Repetir con diferentes semillas (`random_state`) confirma la estabilidad.

**Lección.** 
- El *gap* entre *train* y *test* es crucial en producción.
- La precisión bruta no es lo único importante; también importan la interpretabilidad y la estabilidad.

::pausa{}
**Deduce:** Si entrenamos el modelo y el RMSE en test es altísimo comparado con train, ¿qué modelo de los anteriores refleja este comportamiento y por qué?
::
::/practica

---

## Práctica resuelta 2 — Curva de aprendizaje para diagnosticar bias-variance

::practica{titulo="¿Más datos o más modelo? Diagnóstico con learning curve"}
**Problema.** Tu modelo tiene R² test = 0.65.
- ¿Conviene recolectar más datos de alumnos?
- Una **curva de aprendizaje** responde a esto visualmente.

**Paso 1 — Estrategia.** 
- Entrenar el modelo incrementando los datos (10%, 25%, 50%, etc.).
- Graficar los resultados de R² en train y test.

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

| Patrón | Train alto, CV bajo | Train ≈ CV ambos bajos | Train alto, CV subiendo |
|---|---|---|---|
| **Diagnóstico** | Overfit / alta varianza | Underfit / alto sesgo | Más datos seguirían ayudando |
| **Solución** | Más datos · regularizar | Modelo más complejo | Recolectar datos |

::interioriza
Piensa en la curva de aprendizaje como preparar a un estudiante para un examen.
- Si saca 10 en las simulaciones (Train alto) y 4 en el real (CV bajo), solo se memorizó las preguntas (*Overfit*). Necesita ver problemas nuevos (Más datos).
- Si saca 4 en ambos, no está entendiendo el tema (*Underfit*). Necesita un mejor profesor o estudiar temas más profundos (Modelo más complejo).
::

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

**Paso 5 — Verificación.**
- Repetir con un modelo más simple (como Regresión Lineal).
- Si la curva CV es plana pero baja, añadir datos no servirá.

**Lección.** 
- La curva separa problemas de modelado de problemas de recolección de datos.
- Evita gastar meses buscando datos cuando un modelo ya alcanzó su límite.

::pausa{}
**Reflexiona:** Si tu R² en CV sigue subiendo con una pendiente pronunciada al agregar el último lote de datos, ¿deberías priorizar cambiar a un algoritmo más complejo o conseguir otro lote de datos?
::
::/practica

---

## Práctica resuelta 3 — Hyperparameter tuning con GridSearchCV

::practica{titulo="Encontrar hiperparámetros óptimos sin sobreajustar"}
**Problema.** El Random Forest tiene muchos hiperparámetros.
- Probarlos a mano es muy ineficiente y no escala.
- `GridSearchCV` prueba todas las combinaciones automáticamente usando CV.

**Paso 1 — Estrategia.** 
- Definir un "grid" o red de valores a probar.
- Sklearn entrena todas las combinaciones y devuelve la mejor.

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
    n_jobs=-1,
    verbose=1
)

grid.fit(X_tr, y_tr)

print(f"\nMejores hiperparámetros: {grid.best_params_}")
print(f"Mejor R² CV: {grid.best_score_:.4f}")

# Evaluar en test
mejor = grid.best_estimator_
y_pred = mejor.predict(X_te)
print(f"\nR² test: {r2_score(y_te, y_pred):.4f}")
print(f"MAE test: {mean_absolute_error(y_te, y_pred):.3f}")
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

**Paso 4 — Validar que NO hay leakage.** 
- Revisa si `R² test ≈ R² CV`.
- Si test es mucho mayor a CV, sospecha de un "leakage" de datos.

::interioriza
`GridSearchCV` es como un catador de vinos.
En vez de probar un vino cada día (tú cambiando variables a mano), pones 48 copas en la mesa y las evalúa sistemáticamente hasta darte la ganadora.
::

**Paso 5 — Tiempos y costos.** 
- En datasets chicos, toma segundos en procesar.
- Para combinaciones inmensas (miles), mejor usar `RandomizedSearchCV`.

**Paso 6 — Guardar el modelo final.**

```python
import joblib
joblib.dump(mejor, "modelo_predictor_v2_tuneado.pkl")
print("✓ modelo_predictor_v2_tuneado.pkl guardado")
```

**Lección.** 
- Comienza siempre con un "grid" de valores pequeños.
- Usa CV (por ejemplo, 5-fold) para no contaminar el test set.
- Revisa si la desviación estándar entre iteraciones es alta (inestabilidad).

::pausa{}
**Deduce:** Si tu grid tiene 10 valores para 3 hiperparámetros distintos (10x10x10) y usas 5 folds, ¿cuántos entrenamientos en total realizará el algoritmo?
::
::/practica
