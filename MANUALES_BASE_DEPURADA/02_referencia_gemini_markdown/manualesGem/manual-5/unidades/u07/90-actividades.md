---
unidad: 7
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 07

::act-mcq{titulo="Repaso conceptual"}
1. La función ReLU es:
   - [ ] σ(x) entre 0 y 1
   - [x] max(0, x)
   - [ ] Lineal
   - [ ] Periódica

2. Sin scaling antes de NN:
   - [ ] Acelera entrenamiento
   - [x] La red entrena mucho peor o no converge
   - [ ] Es opcional
   - [ ] Solo afecta árboles

3. Para regresión, la loss típica es:
   - [ ] CrossEntropy
   - [ ] BCE
   - [x] MSE
   - [ ] Hinge

4. Para evitar sobreajuste en NN:
   - [ ] Más neuronas
   - [x] Dropout + early stopping + regularización L2
   - [ ] Más epochs
   - [ ] Sin batch

5. Para tabular pequeño (<5000 filas), suele ganar:
   - [ ] Deep neural network
   - [x] Random Forest / XGBoost
   - [ ] Sigmoid lineal
   - [ ] PCA
::/act-mcq

::act-table{titulo="Activación según caso"}
| Caso | Activación | Razón |
|---|---|---|
| Capa oculta general |  |  |
| Output regresión |  |  |
| Output clasificación binaria |  |  |
| Output multi-clase |  |  |
::/act-table

::act-match{titulo="Componente PyTorch"}
| Componente | Función |
|---|---|
| 1. Tensor | a) Algoritmo que ajusta pesos |
| 2. nn.Module | b) Array multi-dimensional con autograd |
| 3. Optimizer | c) Definición de arquitectura |
| 4. Loss | d) Mide error de predicción |
::/act-match

::act-tf{titulo="V/F"}
1. NN siempre supera modelos clásicos. ( ) ____________________________________________

2. `model.eval()` desactiva Dropout y BatchNorm. ( ) ____________________________________________

3. Sin scaling, NN entrena igual de bien. ( ) ____________________________________________

4. Early stopping previene overfitting. ( ) ____________________________________________

5. Adam suele ser mejor default que SGD. ( ) ____________________________________________
::/act-tf

::albatros{titulo="MLP en PyTorch para tu dataset escolar" tipo="taller" tiempo="4 h"}
**Pregunta detonadora.** Aunque Random Forest gane numéricamente, ¿qué te llevas de entrenar tu primera red neuronal?

**Lo que harás.**
1. Implementa MLP de la práctica resuelta.
2. Compara contra Random Forest.
3. Genera curva de aprendizaje.
4. Aplica early stopping + Dropout.
5. Documenta lecciones aprendidas (qué funcionó, qué no).
6. Subir a GitHub.

**Materiales.** Colab con GPU opcional, PyTorch, 4 horas.

**Entregable.** Notebook + comparación + curva + reflexión.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| MLP funcional | sin entrenar | corre | con regularización |
| Comparación | uno solo | dos modelos | tabla y decisión |
| Diagnóstico | sin curva | grafica | analiza patrón |
| Reflexión | mínima | escrita | con lecciones específicas |
::/albatros

---

## Actividades adicionales (expansión práctica)

::act-fill{titulo="MLP con Dropout y weight_decay"}
```python
import torch.nn as nn
import torch.optim as optim

modelo = nn.Sequential(
    nn.Linear(3, 32), nn.ReLU(), nn.Dropout(___________),
    nn.Linear(32, 16), nn.ReLU(), nn.Dropout(0.2),
    nn.Linear(16, 1)
)

# Adam con regularización L2
optimizer = optim.Adam(modelo.parameters(), lr=0.001, weight_decay=___________)
```
::/act-fill

::act-order{titulo="Pasos de un loop con early stopping"}
[ ] Si val_loss empeora `paciencia` epochs, parar
[ ] Calcular val_loss en `model.eval()` con `torch.no_grad()`
[ ] Si val_loss mejora, guardar `state_dict` y resetear contador
[ ] Forward + loss + backward + step (modo train)
[ ] Cargar el mejor `state_dict` al final
::/act-order

::act-case{titulo="Caso — el MLP no converge" lineas=10}
Tu compañera te muestra esta curva:
```
Epoch 0:    loss=4.50
Epoch 100:  loss=4.48
Epoch 200:  loss=4.47
```

La loss apenas baja. Lista 5 hipótesis de por qué (lr muy baja, falta scaling, modelo muy pequeño, datos sin normalizar, problema de gradientes). Para cada una, ¿cómo lo verificarías y arreglarías?
::/act-case

::act-table{titulo="Hyperparam → efecto"}
| Hyperparam | Subir mucho | Bajar mucho |
|---|---|---|
| Learning rate |  |  |
| Batch size |  |  |
| Hidden units |  |  |
| Dropout |  |  |
| Epochs |  |  |
::/act-table

::act-mindmap{titulo="Mapa mental abierto" centro="REDES NEURONALES" nodos_primarios=5 nodos_secundarios=10}
5 nodos: arquitectura, entrenamiento, regularización, diagnóstico, deployment. 2 ejemplos por cada uno.
::/act-mindmap

::albatros{titulo="Reto Albatros — empaca tu modelo como artefacto reproducible" tipo="reto" tiempo="60 min"}
**Pregunta detonadora.** Si tu modelo entrenado se compartiera con otro equipo, ¿lo podrían cargar y predecir sin tener que re-entrenarlo o adivinar el orden de features?

**Lo que harás.**
1. Crea un **artefacto unificado** que contenga todo lo necesario para inferencia:

```python
import torch, joblib, json

artefacto = {
    "model_state": model.state_dict(),
    "model_arch": {"input": 3, "hidden": [16, 8], "output": 1, "dropout": 0.2},
    "scaler": scaler,                    # objeto sklearn
    "schema": {"features": ["horas_estudio", "asistencia", "cal_anterior"]},
    "metricas_train": {"r2": 0.71, "mae": 0.62},
    "version": "v1.0",
    "fecha_train": "2026-04-30",
    "dataset_origen": "dataset_escolar_limpio_2026Q1.csv",
    "n_train": 372
}
joblib.dump(artefacto, "predictor_v1.joblib")
```

2. Escribe `cargar_y_predecir.py` que reconstruya la arquitectura desde `model_arch`, cargue pesos y scaler, valide schema, y prediga.

3. Sube a GitHub con tag `v1.0`. Pasa el repo a un compañero. Que **él lo corra sin tu ayuda**.

4. Documenta el feedback: ¿qué le faltó? ¿le faltó el schema? ¿el scaler? ¿la versión de torch?

**Entregable.** Repo Git con artefacto + script de carga + README + reporte del feedback de tu compañero.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Artefacto unificado | solo .pt | + scaler | completo con schema y metadata |
| Reproducibilidad | requiere notebook | corre con README | + versionado dependencias |
| Feedback de compañero | no probado | probado | feedback documentado y atendido |
::/albatros
