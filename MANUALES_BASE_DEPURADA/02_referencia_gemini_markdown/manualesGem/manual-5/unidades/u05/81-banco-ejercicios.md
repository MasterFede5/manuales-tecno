---
unidad: 5
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 05

> Practica el pipeline ML: features → split → entrenar → evaluar. Cada bloque te pide leer código sklearn y predecir métricas.

### Bloque A — Conceptos ML (5.1)

::act-mcq{titulo="Supervisado vs no supervisado"}
1. Predecir cal_final de un alumno con sus features es:
   - [x] Supervisado regresión
   - [ ] Supervisado clasificación
   - [ ] No supervisado
   - [ ] Refuerzo

2. Clasificar aprobado/reprobado es:
   - [ ] Supervisado regresión
   - [x] Supervisado clasificación
   - [ ] No supervisado
   - [ ] Refuerzo

3. Agrupar alumnos en perfiles sin etiquetas es:
   - [ ] Supervisado regresión
   - [ ] Supervisado clasificación
   - [x] No supervisado clustering
   - [ ] Refuerzo
::/act-mcq

### Bloque B — Pipeline (5.2)

::act-order{titulo="Pasos del pipeline ML"}
[ ] Evaluar con métricas en test
[ ] Limpiar datos
[ ] Cargar dataset
[ ] Train/test split
[ ] Definir features (X) y target (y)
[ ] Entrenar modelo (`fit`)
[ ] Predecir (`predict`)
[ ] Guardar modelo (`joblib.dump`)
::/act-order

::act-fill{titulo="Pipeline mínimo en sklearn"}
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = df[["horas_estudio", "asistencia", "cal_anterior"]]
y = df["___________"]

X_train, X_test, y_train, y_test = ___________(X, y, test_size=___________, random_state=42)

modelo = ___________()
modelo.fit(X_train, ___________)

y_pred = modelo.predict(___________)
r2 = r2_score(y_test, y_pred)
print(f"R²: {r2:.3f}")
```
::/act-fill

### Bloque C — Train/test split y CV (5.3)

::act-mcq{titulo="Split y validación"}
1. ¿Para qué sirve `random_state=42`?
   - [ ] Aumenta accuracy
   - [x] Reproducibilidad: mismo split en cada corrida
   - [ ] Reduce overfit
   - [ ] Acelera fit

2. K-Fold CV con k=5 significa:
   - [ ] Entrenar 5 modelos distintos
   - [x] Dividir en 5, entrenar 5 veces (cada vez con un fold como test)
   - [ ] Sólo 5% de los datos para test
   - [ ] 5 epochs

3. Si tu R² test es 0.85 pero CV mean es 0.55, sospechas:
   - [ ] Underfitting
   - [x] Test set fácil por suerte / data leakage
   - [ ] Modelo correcto
   - [ ] Bug en métrica
::/act-mcq

::act-fill{titulo="Cross-validation"}
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(modelo, X, y, cv=___________, scoring="r2")
print(f"CV R² scores: {scores}")
print(f"Media: {scores.___________():.3f}")
print(f"Std: {scores.___________():.3f}")
```
::/act-fill

### Bloque D — Métricas (5.4)

::act-match{titulo="Métrica ↔ tipo de tarea"}
| Métrica | Tarea ideal |
|---|---|
| 1. Accuracy | a) Regresión |
| 2. R² | b) Clasificación balanceada |
| 3. F1 | c) Clasificación desbalanceada |
| 4. RMSE | d) Regresión, mismas unidades que y |
| 5. Recall | e) Detectar todos los positivos reales |
::/act-match

::act-mcq{titulo="Métrica correcta"}
1. Dataset 95% aprueba, 5% reprueba. Tu modelo predice "aprueba" siempre. Accuracy = ?
   - [ ] 50%
   - [ ] 70%
   - [x] 95%  (engañosa: el modelo no sirve)
   - [ ] 99%

2. Para detectar al máximo de alumnos en riesgo (clase minoritaria):
   - [ ] Maximizar accuracy
   - [x] Maximizar recall (con precision aceptable)
   - [ ] Minimizar RMSE
   - [ ] Maximizar precision pura
::/act-mcq

::act-table{titulo="Llena las métricas"}
Modelo de regresión predice cal_final. Verdaderos: `[7, 8, 6, 9]`. Predicciones: `[6.5, 8.2, 6.5, 8.5]`.

| Métrica | Fórmula | Valor |
|---|---|---|
| MAE |  |  |
| MSE |  |  |
| RMSE |  |  |
::/act-table

### Bloque E — Regresión lineal (5.5)

::act-fill{titulo="Coeficientes interpretados"}
```python
modelo = LinearRegression().fit(X_train, y_train)
for col, coef in zip(X.___________, modelo.coef_):
    print(f"{col}: {coef:+.3f}")

# Intercepto:
print(f"Intercepto: {modelo.___________:.3f}")

# Predicción manual para un alumno
alumno = [4.0, 0.85, 7.0]
pred_manual = (alumno[0]*modelo.coef_[0] + 
               alumno[1]*modelo.coef_[1] + 
               alumno[2]*modelo.coef_[___________] + 
               modelo.intercept_)
pred_sklearn = modelo.predict([alumno])[0]
print(f"Manual: {pred_manual:.3f} vs sklearn: {pred_sklearn:.3f}")  # deben coincidir
```
::/act-fill

### Bloque F — Clasificación logística (5.6)

::act-mcq{titulo="Logística"}
1. Regresión logística predice:
   - [ ] Un número continuo
   - [x] Una probabilidad entre 0 y 1
   - [ ] Una categoría sin probabilidad
   - [ ] Cualquier número real

2. ¿Cómo se obtiene la **clase** desde la probabilidad?
   - [ ] `np.round(prob)` con threshold 0.5 por default
   - [x] `model.predict()` aplica threshold automáticamente (0.5)
   - [ ] Entrenando otro modelo
   - [ ] No se puede

3. Para datos desbalanceados, ajustar threshold sirve para:
   - [ ] Cambiar accuracy
   - [x] Trocar precision por recall según costo del error
   - [ ] Acelerar inferencia
   - [ ] Reducir features
::/act-mcq

::act-fill{titulo="Pipeline de clasificación"}
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Crear target binario (aprueba/reprueba)
df["aprueba"] = (df["cal_final"] >= ___________).astype(int)

X = df[["horas_estudio", "asistencia", "cal_anterior"]]
y = df["aprueba"]

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression(max_iter=___________).fit(X_tr, y_tr)
y_pred = clf.predict(X_te)
y_proba = clf.predict_proba(X_te)[:, ___________]    # prob clase 1

print(classification_report(y_te, y_pred))
```
::/act-fill

### Bloque G — Árboles y overfit (5.7, 5.8)

::act-mcq{titulo="Árboles y bosques"}
1. Un árbol con `max_depth=None`:
   - [ ] Es siempre el mejor
   - [x] Tiende a sobreajustar (memoriza training)
   - [ ] No converge
   - [ ] Entrena más rápido

2. Random Forest reduce sobreajuste vs un solo árbol porque:
   - [ ] Usa más capas
   - [x] Promedia muchos árboles entrenados con bagging
   - [ ] Es más interpretable
   - [ ] Usa GPU

3. Tu modelo tiene R²(train)=0.95, R²(test)=0.62. El gap 0.33 indica:
   - [ ] Buen modelo
   - [x] Overfit fuerte
   - [ ] Underfit
   - [ ] Test set sucio
::/act-mcq

::act-tf{titulo="V/F regularización"}
1. Más datos típicamente ayuda contra el overfit. ( ) ____________________
2. `min_samples_leaf` alto hace el árbol más simple. ( ) ____________________
3. Lasso (L1) puede llevar coeficientes exactamente a 0. ( ) ____________________
4. Reducir `max_depth` aumenta el sesgo (bias). ( ) ____________________
5. Regularización L2 (Ridge) elimina features. ( ) ____________________
::/act-tf

::act-case{titulo="Caso — interpretar tabla comparativa" lineas=10}
| Modelo | R² train | R² test | CV mean | Gap |
|---|---|---|---|---|
| Lineal | 0.62 | 0.61 | 0.61 | 0.01 |
| Árbol depth=4 | 0.73 | 0.65 | 0.64 | 0.08 |
| Random Forest | 0.95 | 0.71 | 0.70 | 0.24 |

**Pregunta.** Si **interpretabilidad** es prioridad para coordinación, ¿cuál eliges? Si **precisión** es prioridad y aceptas algo de overfit, ¿cuál? Si quieres balance, ¿cuál? Justifica cada elección en 1 línea.
::/act-case

---

## Clave de respuestas

**Bloque A.** 1·A, 2·B, 3·C.

**Bloque B.**
- `act-order`: 3·2·5·4·6·7·1·8 (cargar→limpiar→X/y→split→fit→predict→evaluar→save).
- `act-fill`: `cal_final`, `train_test_split`, `0.2`, `LinearRegression`, `y_train`, `X_test`.

**Bloque C.**
- `act-mcq`: 1·B, 2·B, 3·B.
- `act-fill`: `cv=5`, `scores.mean()`, `scores.std()`.

**Bloque D.**
- `act-match`: 1-b, 2-a, 3-c, 4-d, 5-e.
- `act-mcq`: 1·C (95% pero modelo inútil), 2·B.
- `act-table`: errores `[0.5, 0.2, 0.5, 0.5]` → MAE=0.425, MSE=(0.25+0.04+0.25+0.25)/4=0.1975, RMSE≈0.444.

**Bloque E.**
- `act-fill`: `X.columns`, `modelo.intercept_`, `modelo.coef_[2]`.

**Bloque F.**
- `act-mcq`: 1·B, 2·B, 3·B.
- `act-fill`: `>= 6`, `max_iter=1000`, `[:, 1]`.

**Bloque G.**
- `act-mcq`: 1·B, 2·B, 3·B.
- `act-tf`: 1·V; 2·V; 3·V; 4·V; 5·F (Ridge encoge pero no elimina).
- `act-case`: respuesta modelo:
  > "Interpretabilidad → Lineal (ecuación clara, gap mínimo). Precisión → Random Forest (R² 0.71 con CV 0.70 sugiere que el overfit es moderado, no catastrófico). Balance → Árbol depth=4 (mejora sobre lineal sin overfit grave; estructura visual interpretable)."

> **Cierre.** Si interpretas correctamente la tabla del bloque G y conoces las métricas del bloque D, estás listo para el taller (clasificación binaria) y la implementación.
