---
unidad: 5
seccion: cierre
paginas_objetivo: 1
---

## Cierre y autoevaluación — Unidad 05

Cerraste tu primera unidad de Machine Learning. Ahora puedes:

1. **Distinguir** ML supervisado, no supervisado, regresión, clasificación.
2. **Aplicar pipeline ML** completo con scikit-learn.
3. **Train/test split** y **cross-validation** para evaluar honestamente.
4. **Elegir métricas** correctas según tarea (R², F1, RMSE).
5. **Entrenar** regresión lineal, logística, árboles, Random Forest.
6. **Diagnosticar y prevenir sobreajuste** con regularización y simplicidad.

> **Frase puente.** Has hecho ML supervisado: el modelo aprende de etiquetas. La Unidad 6 va al lado **no supervisado**: descubrir patrones sin etiquetas. K-Means para segmentar perfiles de alumnos.

---

### Autoevaluación

| Saber | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Concepto ML | confuso | sé los 3 tipos | aplico criterio | mezclo según caso | enseño a otros |
| Pipeline | desordenado | con split | + CV | + feature eng | reproducible reusable |
| Métricas | solo accuracy | 2-3 | correctas según tarea | múltiples métricas | reporto con criterio |
| Modelos lineales | no uso | linear básico | + logistic | con regularización | comparo lineal vs no-lineal |
| Árboles | desconozco | uno | + visualización | feature importance | + Random Forest |
| Sobreajuste | no detecto | gap evidente | uso CV | regularizo | curva de aprendizaje |

### Pregunta de cierre

> Tu modelo tiene R² 0.85 en producción y baja a 0.65 al mes 3. **Diseña** plan en 4 actos para diagnosticar y arreglar (drift de datos, modelo obsoleto, problema en pipeline, otra causa).

### Conexión con la siguiente unidad

En **U6** descubres el otro lado de ML: encontrar grupos sin etiquetas, descubrir estructura latente. K-Means te llevará a segmentar tu dataset en perfiles automáticamente.
