---
unidad: 7
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 07

> Practica redes neuronales con PyTorch: tensores, capas, loss, optimizer, regularización.

::interioriza
- **PyTorch** es como una cocina profesional escolar:
- **Tensores:** los ingredientes crudos (calificaciones).
- **Capas:** estaciones de trabajo procesando datos.
- **Optimizer:** el maestro ajustando su método al ver los errores.
::/interioriza

::pausa{}
**Pregunta:** Si las predicciones de notas son pésimas al iniciar, ¿quién corrige el rumbo: los tensores o el optimizer?
- *Respuesta:* El optimizer (junto con la loss function) ajustando los pesos.
::/pausa

### Bloque A — Neurona artificial (7.1)

::act-mcq{titulo="Conceptos básicos NN"}
1. Una neurona calcula:
   - [ ] Solo `x + b`
   - [x] `f(w·x + b)` donde f es una función de activación
   - [ ] Solo el producto punto `w·x`
   - [ ] La media de los inputs

2. ¿Por qué necesitamos funciones de activación NO-lineales?
   - [ ] Por estética
   - [x] Sin ellas, una red de N capas equivale a 1 sola capa lineal
   - [ ] Para acelerar
   - [ ] Para usar GPU

3. Sin scaling, NN suele:
   - [ ] Entrenar más rápido
   - [x] Diverger o aprender mucho peor
   - [ ] Funcionar igual
   - [ ] Solo afectar regresión
::/act-mcq

::act-fill{titulo="Cálculo manual de una neurona"}
```python
import torch

# Pesos y bias de una neurona
w = torch.tensor([0.5, -0.3, 0.8])
b = torch.tensor(0.1)
x = torch.tensor([1.0, 2.0, 3.0])

# Salida lineal
z = (w * x).___________() + b
print(f"z = {z.item():.3f}")        # esperado: 2.000

# Activación ReLU
y = torch.___________(z)
print(f"y = {y.item():.3f}")        # esperado: 2.000 (z >= 0)

# Si z fuera negativo, ReLU daría:
print(torch.relu(torch.tensor(___________)).item())   # esperado: 0.0
```
::/act-fill

### Bloque B — Capas y activaciones (7.2)

::act-match{titulo="Activación ↔ uso"}
| Activación | Uso |
|---|---|
| 1. ReLU | a) Clasificación binaria output |
| 2. Sigmoid | b) Capa oculta general (default moderno) |
| 3. Softmax | c) Output regresión sin restricción |
| 4. Linear | d) Clasificación multi-clase output |
| 5. Tanh | e) Salida acotada en [-1, 1] |
::/act-match

::act-mcq{titulo="Output según tarea"}
1. Predecir cal_final (0-10):
   - [ ] Sigmoid
   - [ ] Softmax
   - [x] Linear
   - [ ] Tanh

2. Predecir aprueba/reprueba:
   - [x] Sigmoid + BCELoss
   - [ ] Softmax + MSELoss
   - [ ] Linear + CrossEntropy
   - [ ] Tanh + BCE

3. Clasificar 4 perfiles de cluster:
   - [ ] Sigmoid
   - [x] Softmax + CrossEntropy
   - [ ] Linear
   - [ ] ReLU
::/act-mcq

### Bloque C — Forward y backward (7.3)

::act-order{titulo="Pasos de un step de entrenamiento"}
[ ] `loss.backward()` — calcular gradientes
[ ] `optimizer.zero_grad()` — limpiar gradientes anteriores
[ ] `loss = criterion(pred, y)` — calcular error
[ ] `pred = model(X)` — forward pass
[ ] `optimizer.step()` — actualizar pesos
::/act-order

::act-tf{titulo="V/F sobre training loop"}
1. Olvidar `optimizer.zero_grad()` acumula gradientes y rompe el entrenamiento. ( ) ____________________
2. `loss.backward()` actualiza los pesos directamente. ( ) ____________________
3. `model.eval()` desactiva Dropout y BatchNorm para inferencia. ( ) ____________________
4. `with torch.no_grad():` ahorra memoria al evaluar. ( ) ____________________
5. La learning rate alta siempre acelera convergencia. ( ) ____________________
::/act-tf

### Bloque D — PyTorch recetario (7.4)

::act-fill{titulo="Define un MLP"}
```python
import torch.nn as nn

modelo = nn.Sequential(
    nn.Linear(___________, 32),         # 3 features de entrada
    nn.___________(),                    # activación
    nn.Dropout(___________),             # regularización 20%
    nn.Linear(32, 16),
    nn.ReLU(),
    nn.Linear(16, ___________),          # 1 output (regresión)
)
print(modelo)
```
::/act-fill

::act-fill{titulo="Convertir numpy a tensor"}
```python
import torch
import numpy as np

X_np = np.array([[1, 2, 3], [4, 5, 6]])
y_np = np.array([7.0, 8.0])

X = torch.tensor(X_np, dtype=torch.___________)         # float para NN
y = torch.tensor(y_np, dtype=torch.float32).___________(1)  # shape (2, 1)

print(X.shape)   # esperado: (2, 3)
print(y.shape)   # esperado: (___________)
```
::/act-fill

### Bloque E — Training loop (7.5)

::act-mcq{titulo="Diagnóstico de loss"}
1. La loss train baja, la loss val sube. Esto es:
   - [ ] Buen entrenamiento
   - [x] Overfitting
   - [ ] Underfitting
   - [ ] Bug

2. Ambas losses están planas y altas. Esto es:
   - [ ] Overfitting
   - [x] Underfitting (modelo muy simple o lr muy baja)
   - [ ] Convergencia
   - [ ] Bug

3. Ambas losses bajan y convergen juntas. Esto es:
   - [x] Buen entrenamiento
   - [ ] Overfitting
   - [ ] Underfitting
   - [ ] Necesita early stopping
::/act-mcq

::act-fill{titulo="Loop de entrenamiento mínimo"}
```python
optimizer = torch.optim.___________(modelo.parameters(), lr=0.001)
criterion = nn.___________()       # MSE para regresión

for epoch in range(100):
    modelo.train()
    optimizer.zero_grad()
    pred = modelo(X)
    loss = criterion(pred, y)
    loss.___________()              # backward
    optimizer.___________()         # update
```
::/act-fill

### Bloque F — Diagnóstico curvas (7.6)

::act-case{titulo="Caso — diagnostica la curva" lineas=10}
Tu curva de aprendizaje muestra:
```
Epoch 0:   loss_train=2.50  loss_val=2.50
Epoch 50:  loss_train=0.40  loss_val=0.45
Epoch 100: loss_train=0.30  loss_val=0.42
Epoch 150: loss_train=0.18  loss_val=0.45
Epoch 200: loss_train=0.10  loss_val=0.50
Epoch 250: loss_train=0.05  loss_val=0.55
```

**Pregunta.** 
1. ¿Qué fenómeno ves a partir de epoch 100?
2. ¿En qué epoch deberías hacer **early stopping**?
3. ¿Qué dos cambios al modelo o entrenamiento podrían mitigarlo?
::/act-case

::act-mcq{titulo="Combatir overfit en NN"}
1. ¿Cuál NO ayuda contra overfit?
   - [ ] Más datos
   - [x] Más epochs
   - [ ] Dropout
   - [ ] Regularización L2

2. Early stopping monitorea:
   - [ ] Solo loss train
   - [x] Loss val (deja de entrenar cuando empeora)
   - [ ] Accuracy
   - [ ] El reloj
::/act-mcq

### Bloque G — Comparación con clásicos

::act-tf{titulo="Cuándo NN vs cuándo clásico"}
1. Para tabular pequeño (<5000 filas), Random Forest suele ganar a NN. ( ) ____________________
2. Para imágenes y secuencias largas, NN domina. ( ) ____________________
3. NN siempre necesita GPU. ( ) ____________________
4. Aprender NN es inútil si tu dataset es tabular. ( ) ____________________
5. NN entrenar siempre que tengas tiempo, no importa el dataset. ( ) ____________________
::/act-tf

::act-table{titulo="MLP vs Random Forest sobre el dataset escolar"}
Predice cuál gana o si empatan. Justifica brevemente.

| Métrica | MLP esperado | RF esperado | Por qué |
|---|---|---|---|
| RMSE |  |  |  |
| Tiempo entrenamiento |  |  |  |
| Interpretabilidad |  |  |  |
| Necesita scaling |  |  |  |
| Necesita más datos para mejorar |  |  |  |
::/act-table

---

## Clave de respuestas

**Bloque A.**
- `act-mcq`: 1·B, 2·B, 3·B.
- `act-fill`: `(w*x).sum()`, `torch.relu`, `torch.tensor(-2.0)` (cualquier negativo, output 0).

**Bloque B.**
- `act-match`: 1-b, 2-a, 3-d, 4-c, 5-e.
- `act-mcq`: 1·C, 2·A, 3·B.

**Bloque C.**
- `act-order`: 2·4·3·1·5 (zero_grad → forward → loss → backward → step).
- `act-tf`: 1·V; 2·F (solo calcula gradientes); 3·V; 4·V; 5·F (puede divergir).

**Bloque D.**
- `act-fill MLP`: `nn.Linear(3, 32)`, `nn.ReLU()`, `Dropout(0.2)`, `Linear(16, 1)`.
- `act-fill tensor`: `dtype=torch.float32`, `.unsqueeze(1)`, shape `(2, 1)`.

**Bloque E.**
- `act-mcq`: 1·B, 2·B, 3·A.
- `act-fill`: `optim.Adam`, `nn.MSELoss()`, `loss.backward()`, `optimizer.step()`.

**Bloque F.**
- `act-case`: respuesta modelo:
  > "(1) Overfitting clásico: train sigue bajando pero val sube. (2) Early stopping en epoch 100 (val mínimo en 0.42). (3) Agregar Dropout 0.2-0.3, agregar weight_decay (L2) en Adam, reducir tamaño del modelo o aumentar datos."
- `act-mcq`: 1·B, 2·B.

**Bloque G.**
- `act-tf`: 1·V; 2·V; 3·F (CPU es OK para tabular pequeño); 4·F (sirve aprender el oficio); 5·F.
- `act-table`:

| Métrica | MLP | RF | Por qué |
|---|---|---|---|
| RMSE | similar o peor | mejor | tabular pequeño, RF gana |
| Tiempo train | mayor | menor | NN itera muchas epochs |
| Interpretabilidad | baja | media-alta | RF da feature importances |
| Scaling | obligatorio | opcional | NN sí, RF no |
| Más datos ayudan | sí mucho | sí pero menos | NN escalan mejor |

> **Cierre.**
> - Aprendiste NN no para reemplazar RF en datos escolares.
> - Su verdadero poder es abrir la puerta a problemas complejos.
> - Dominan en visión artificial (CV) y procesamiento de lenguaje (NLP).
