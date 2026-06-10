---
unidad: 7
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — MLP comparado contra modelos clásicos"}
**Objetivo.** Producir notebook completo con MLP entrenado, regularizado, comparado con Random Forest y XGBoost (de la investigación de U5 si hiciste). Reporte honesto: ¿qué modelo gana para tu dataset y por qué?

**Materiales.** PyTorch, Colab, GitHub, 5-6 horas.

**Pasos.**
1. Pipeline MLP completo con regularización (2 h).
2. Comparación contra RF y XGBoost (1 h).
3. Curvas de aprendizaje y diagnóstico (1 h).
4. Reporte con decisión final justificada (1 h).
5. Subir a GitHub con README (30 min).

**Entregable.** Notebook + reporte 1-2 pp + curvas + modelo guardado.

**Rúbrica.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| MLP construido | sin entrenar | corre | con regularización efectiva |
| Comparación | un solo modelo | dos | 3+ con tabla |
| Curvas | sin graficar | una | múltiples con análisis |
| Decisión | "uso NN porque es cool" | basada en métricas | basada en datos + contexto + dominio |

**Próximo paso.** En **U8** vas a integrar tu predictor con **APIs de IA generativa** para que **explique** sus predicciones en lenguaje natural.

### Hitos intermedios

| Hito | Tag git | Criterio de cierre |
|---|---|---|
| H1 | `u7-h1-tensores` | Operaciones básicas con torch.tensor + autograd |
| H2 | `u7-h2-mlp` | MLP definido con `nn.Module` o Sequential |
| H3 | `u7-h3-loop` | Training loop con loss bajando consistentemente |
| H4 | `u7-h4-regularizacion` | Dropout + early stopping aplicados |
| H5 | `u7-h5-comparacion` | Tabla MLP vs RF con métricas idénticas |
| H6 | `u7-h6-deploy` | Modelo serializado + script de inferencia + API simple |

### Reto bonus extendido (3 retos)

**Reto bonus 1 — TensorBoard para tracking.** Integra `torch.utils.tensorboard.SummaryWriter` para loggear loss, learning rate y pesos por epoch. Lanza TensorBoard local. Esfuerzo: 60 min.

```python
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter("runs/exp1")
writer.add_scalar("Loss/train", loss.item(), epoch)
```

**Reto bonus 2 — Cross-validation con NN.** Implementa K-Fold manual sobre PyTorch (sklearn no lo hace para tensores). 5 folds, reporta R² medio y std. Esfuerzo: 90 min.

**Reto bonus 3 — ONNX export.** Exporta tu modelo a formato ONNX (interoperable). Cárgalo desde `onnxruntime` y predice. Esfuerzo: 60 min.

```python
torch.onnx.export(model, X_dummy, "modelo.onnx",
                  input_names=["input"], output_names=["pred"])
```
::/implementacion

---

::albatros{titulo="Caso bonus — defender la elección del modelo final" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Si tienes que defender ante coordinación una decisión "MLP vs Random Forest" para producción, ¿qué argumentos usas?

**Contexto.** Sub-comité técnico de Albatros pide que justifiques el modelo final que va a producción en U8. Tienes 5 minutos y debes evitar 2 trampas:
- "Uso NN porque es lo más nuevo." → no es argumento técnico.
- "Uso lo que dio mejor R² en mi último experimento." → no consideras estabilidad ni operación.

**Lo que harás.**
1. Construye una matriz de decisión con 6 criterios:
   - Precisión (R² CV mean ± std).
   - Estabilidad (varianza entre folds).
   - Tiempo de entrenamiento.
   - Tiempo de inferencia.
   - Interpretabilidad.
   - Costo de mantenimiento (¿cada cuánto re-entrenar?).
2. Pondera cada criterio (porcentaje, suma 100).
3. Aplica la matriz a MLP y RF; calcula score ponderado.
4. Redacta una recomendación de **2 párrafos** con la decisión y un disclaimer (qué pasa si los criterios cambian).
5. Identifica 2 escenarios donde **cambiarías de opinión**.

**Entregable.** Documento de 1 página con: matriz de decisión + score ponderado + recomendación + escenarios de cambio.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Criterios definidos | <4 | 5 | 6 con peso justificado |
| Score ponderado | sin números | calculado | con fuente de cada métrica |
| Recomendación | "uso X" | con porqué | con disclaimer |
| Escenarios de cambio | sin | uno | 2 con condiciones específicas |
::/albatros
