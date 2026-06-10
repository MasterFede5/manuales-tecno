---
unidad: 5
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 05

::act-mcq{titulo="Repaso conceptual"}
1. ¿Qué métrica reporta el % de varianza explicada en regresión?
   - [ ] MAE
   - [ ] RMSE
   - [x] R²
   - [ ] Accuracy

2. Tu modelo da 99% en train y 65% en test. Esto se llama:
   - [ ] Buen ajuste
   - [x] Sobreajuste
   - [ ] Underfitting
   - [ ] Variance bajo

3. Para datos desbalanceados (95% aprueba), accuracy es engañosa. ¿Qué reportar?
   - [ ] R²
   - [ ] MSE
   - [x] F1 o AUC
   - [ ] MAE

4. Random Forest comparado con un solo árbol:
   - [ ] Menos preciso siempre
   - [x] Más preciso pero menos interpretable
   - [ ] Igual en todo
   - [ ] Solo para clasificación

5. ¿Para qué sirve `random_state=42` en train_test_split?
   - [ ] Aumenta accuracy
   - [x] Reproducibilidad: mismo split cada ejecución
   - [ ] Reduce overfitting
   - [ ] Acelera entrenamiento
::/act-mcq

::act-table{titulo="Modelo según caso"}
| Caso | Modelo recomendado | Justificación |
|---|---|---|
| Predecir cal_final exacta, interpretable |  |  |
| Aprueba/reprueba con datos pequeños |  |  |
| Múltiples categorías, no lineal |  |  |
| Producción con precisión alta |  |  |
| Selección automática de features |  |  |
::/act-table

::act-match{titulo="Relaciona métrica con uso"}
| Métrica | Uso |
|---|---|
| 1. Accuracy | a) Promedio de error absoluto |
| 2. F1 | b) Total predicciones correctas |
| 3. Recall | c) Balance precision-recall |
| 4. RMSE | d) De los positivos reales, cuántos detecté |
| 5. MAE | e) Error cuadrático en mismas unidades que y |
| 6. R² | f) % de varianza explicada |
::/act-match

::act-tf{titulo="V/F"}
1. R² siempre está entre 0 y 1. ( ) ____________________________________________

2. Sobreajuste mejora con más datos. ( ) ____________________________________________

3. Train/test split debe hacerse antes de feature scaling. ( ) ____________________________________________

4. Una accuracy 99% siempre indica buen modelo. ( ) ____________________________________________

5. Lasso (L1) puede llevar coeficientes a exactamente 0. ( ) ____________________________________________
::/act-tf

::albatros{titulo="Tu primer predictor escolar comparando 3 modelos" tipo="taller" tiempo="4 h"}
**Pregunta detonadora.** Si pudieras predecir con 80% precisión qué alumnos están en riesgo a inicio de bimestre, ¿qué intervención propondrías?

**Lo que harás.**
1. Implementa pipeline completo de la práctica resuelta.
2. Entrena 3 modelos: Linear, Tree (depth=4), Random Forest.
3. Compara con tabla de métricas (R², RMSE, gap, CV).
4. Diagnostica overfitting en cada uno.
5. Guarda el mejor modelo con joblib.
6. Crea función `predecir_riesgo(alumno_dict)` que devuelve probabilidad.
7. Documenta resultado y limitaciones.

**Materiales.** Scikit-learn, joblib, GitHub, 4 horas.

**Entregable.**
- Notebook con código.
- Modelo guardado .pkl.
- Documento (1-2 pp) con análisis.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Pipeline | incompleto | funcional | con CV |
| Modelos comparados | uno | dos | 3+ con tabla |
| Diagnóstico | sin gap | menciona | analiza overfitting |
| Métricas | solo accuracy | 2-3 | métricas correctas según caso |
| Documentación | mínima | reporte | con limitaciones honestas |
::/albatros

---

## Actividades adicionales (expansión práctica)

::act-fill{titulo="Pipeline con StandardScaler"}
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = ___________([
    ("scaler", ___________()),
    ("clf", LogisticRegression(max_iter=1000))
])

pipe.fit(X_train, ___________)
acc = pipe.___________(X_test, y_test)
print(f"Accuracy: {acc:.3f}")
```
::/act-fill

::act-order{titulo="Pasos para evitar data leakage en el pipeline"}
[ ] `pipeline.fit(X_train, y_train)` — el scaler aprende solo del train
[ ] Crear `Pipeline([("scaler", ...), ("model", ...)])`
[ ] Evaluar con `pipeline.score(X_test, y_test)`
[ ] Hacer `train_test_split` ANTES de cualquier scaler
[ ] Cargar dataset
::/act-order

::act-case{titulo="Caso — diagnóstico de overfitting" lineas=12}
Recibes este reporte de un compañero:

```
Random Forest (n_estimators=500, max_depth=None):
  R² train: 0.99
  R² test:  0.62
  CV mean:  0.61 (std 0.04)
```

**Pregunta.** Diagnostica:
1. ¿Hay overfit? ¿Por qué (1 línea)?
2. Da 3 cambios al modelo que probarías para reducirlo (con valores específicos).
3. ¿Cómo verificas si tu cambio funcionó? ¿Qué métrica deberías mirar?
::/act-case

::act-table{titulo="Comparación de algoritmos sklearn"}
| Algoritmo | Interpretable | Necesita scaling | Sensible a outliers | Costo entrenamiento |
|---|---|---|---|---|
| LinearRegression |  |  |  |  |
| LogisticRegression |  |  |  |  |
| DecisionTreeRegressor |  |  |  |  |
| RandomForestRegressor |  |  |  |  |
| KNeighborsRegressor |  |  |  |  |
::/act-table

::act-mindmap{titulo="Mapa mental abierto" centro="PIPELINE ML" nodos_primarios=6 nodos_secundarios=12}
6 nodos: features, split, modelo, métrica, validación, decisión. 2 ejemplos por cada uno.
::/act-mindmap

::albatros{titulo="Reto Albatros — feature engineering creativo" tipo="reto" tiempo="60 min"}
**Pregunta detonadora.** ¿Puedes mejorar el R² del modelo sin cambiar el algoritmo, solo creando **features derivadas** inteligentes?

**Lo que harás.**
1. Toma tu modelo Linear actual (R² ≈ 0.61).
2. Crea al menos 4 features derivadas y prueba su impacto:
   - **Interacción**: `horas_x_asistencia = horas_estudio * asistencia`.
   - **Ratio**: `cal_anterior_relativa = cal_anterior / 10`.
   - **Categórica → one-hot**: convertir `materia` a 3 columnas binarias.
   - **Discretización**: `nivel_horas` (low/med/high) basado en cuartiles.
3. Para cada feature nueva: agrégala al modelo, mide R², decide si la conservas.
4. Documenta cuáles funcionaron y cuáles no.

**Tip.** Empieza por agregar TODAS, luego usa `SelectKBest` para quedarte con las top.

```python
from sklearn.feature_selection import SelectKBest, f_regression

selector = SelectKBest(score_func=f_regression, k=5)
X_top = selector.fit_transform(X_completo, y)
print(selector.get_feature_names_out())
```

**Entregable.** Notebook + tabla comparativa (R² antes / después de cada feature) + recomendación.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Features creadas | <2 | 3 | 4+ con justificación |
| Comparación | sin tabla | tabla parcial | completa con delta |
| Selector | sin | aplicado | + interpretación de top features |
| R² mejorado | bajó | igual | subió ≥ 0.02 |
::/albatros
