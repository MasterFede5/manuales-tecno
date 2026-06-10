---
unidad: 7
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 07

::practica{titulo="MLP con early stopping comparado contra Random Forest del U5"}
**Problema.** Entrenar MLP con regularización (Dropout + early stopping) y comparar honestamente contra Random Forest. Decidir cuál llevar a producción.

**Paso 1 — Estrategia.** Pipeline completo PyTorch + early stopping + comparación.

**Paso 2 — Código completo.**

```python
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Datos y split
df = pd.read_csv("dataset_escolar_limpio.csv")
X = df[["horas_estudio", "asistencia", "cal_anterior"]].values
y = df["cal_final"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# === MLP con regularización ===
X_tr = torch.tensor(X_train_s, dtype=torch.float32)
y_tr = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)
X_te = torch.tensor(X_test_s, dtype=torch.float32)
y_te = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

model = nn.Sequential(
    nn.Linear(3, 32),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(32, 16),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(16, 1)
)

optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
criterion = nn.MSELoss()

# Loop con early stopping
losses_tr, losses_te = [], []
mejor = float('inf')
paciencia, contador = 20, 0

for epoch in range(500):
    model.train()
    optimizer.zero_grad()
    pred = model(X_tr)
    loss = criterion(pred, y_tr)
    loss.backward()
    optimizer.step()
    
    model.eval()
    with torch.no_grad():
        pred_te = model(X_te)
        loss_te = criterion(pred_te, y_te).item()
    
    losses_tr.append(loss.item())
    losses_te.append(loss_te)
    
    if loss_te < mejor:
        mejor = loss_te
        torch.save(model.state_dict(), "mejor.pth")
        contador = 0
    else:
        contador += 1
        if contador >= paciencia:
            print(f"Early stopping epoch {epoch}")
            break

# Cargar mejor modelo
model.load_state_dict(torch.load("mejor.pth"))
model.eval()
with torch.no_grad():
    y_pred_nn = model(X_te).numpy().flatten()

rmse_nn = np.sqrt(mean_squared_error(y_test, y_pred_nn))
r2_nn = r2_score(y_test, y_pred_nn)

# === Random Forest ===
rf = RandomForestRegressor(n_estimators=200, max_depth=8, random_state=42)
rf.fit(X_train_s, y_train)
y_pred_rf = rf.predict(X_test_s)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
r2_rf = r2_score(y_test, y_pred_rf)

# Comparación
print(f"\n=== Comparación ===")
print(f"MLP: RMSE={rmse_nn:.3f}, R²={r2_nn:.3f}")
print(f"RF:  RMSE={rmse_rf:.3f}, R²={r2_rf:.3f}")

# Gráfica
plt.plot(losses_tr, label="Train")
plt.plot(losses_te, label="Test")
plt.legend(); plt.title("Curva aprendizaje MLP")
plt.savefig("curva.png")
```

**Paso 3 — Output.**
```
Early stopping epoch 87

=== Comparación ===
MLP: RMSE=0.83, R²=0.71
RF:  RMSE=0.76, R²=0.78
```

**Paso 4 — Decisión.** Random Forest gana en RMSE y R². Para tabular pequeño, RF es la elección. **MLP sigue siendo experiencia formativa importante.**

**Paso 5 — Verificación.** Curva de aprendizaje muestra convergencia sin overfit (gracias a Dropout + early stopping). Honesto.

**Lección.** Las 6 técnicas de la unidad: neurona, capas, forward/backward, PyTorch recetario, MLP entrenado, diagnóstico curva. Para tu dataset pequeño Random Forest gana, pero el ejercicio te abrió la puerta a deep learning donde NN sí dominan (visión, NLP, secuencias).
::/practica

---

## Práctica resuelta 2 — Mini-batches con DataLoader

::practica{titulo="Entrenar con DataLoader para datasets que no caben en memoria"}
**Problema.** Hasta ahora pasaste el tensor entero por epoch. Cuando el dataset crece (50k+ filas), debes entrenar **por mini-batches**. PyTorch ofrece `Dataset` + `DataLoader` para esto.

**Paso 1 — Estrategia.** Crear un `Dataset` custom que devuelve `(X_i, y_i)`, envolverlo en `DataLoader` con `batch_size`, iterar batches en cada epoch.

**Paso 2 — Código.**

```python
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Dataset custom
class EscolarDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32).unsqueeze(1)
    def __len__(self):
        return len(self.X)
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# Datos
df = pd.read_csv("dataset_escolar_limpio.csv")
X = df[["horas_estudio", "asistencia", "cal_anterior"]].values
y = df["cal_final"].values
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler().fit(X_tr)
X_tr_s = scaler.transform(X_tr)
X_te_s = scaler.transform(X_te)

# DataLoaders
train_ds = EscolarDataset(X_tr_s, y_tr)
test_ds = EscolarDataset(X_te_s, y_te)

train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
test_loader = DataLoader(test_ds, batch_size=64, shuffle=False)

# Modelo
model = nn.Sequential(
    nn.Linear(3, 32), nn.ReLU(),
    nn.Linear(32, 16), nn.ReLU(),
    nn.Linear(16, 1)
)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.MSELoss()

# Entrenar por mini-batches
for epoch in range(50):
    model.train()
    total_loss = 0
    n_batches = 0
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        pred = model(X_batch)
        loss = criterion(pred, y_batch)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        n_batches += 1
    if epoch % 10 == 0:
        # Evaluar
        model.eval()
        with torch.no_grad():
            pred_te = torch.cat([model(xb) for xb, _ in test_loader])
            y_te_full = torch.cat([yb for _, yb in test_loader])
            test_loss = criterion(pred_te, y_te_full).item()
        print(f"Epoch {epoch}: train_loss={total_loss/n_batches:.4f}, "
              f"test_loss={test_loss:.4f}")
```

**Paso 3 — Output esperado.**
```
Epoch 0:  train_loss=39.5421, test_loss=29.6123
Epoch 10: train_loss=0.7234,  test_loss=0.7891
Epoch 20: train_loss=0.5023,  test_loss=0.6132
Epoch 30: train_loss=0.4521,  test_loss=0.5712
Epoch 40: train_loss=0.4302,  test_loss=0.5654
```

**Paso 4 — Ventajas vs entrenamiento full-batch.**

| Aspecto | Full-batch | Mini-batch (DataLoader) |
|---|---|---|
| Memoria | todo el dataset en RAM | solo `batch_size` filas |
| Velocidad por epoch | rápido si cabe en memoria | un poco más lento, escala mejor |
| Estocasticidad | determinista | ruido del shuffling ayuda a escapar mínimos locales |
| GPU | utilización pobre | utilización alta con batch grande |
| Datasets grandes | imposible | indispensable |

**Paso 5 — Verificación.** Compara loss final de full-batch vs mini-batch. Para nuestro dataset (~370 train) la diferencia es marginal; con 50k filas el mini-batch es **la única opción**.

**Paso 6 — Bonus: ajuste fino del batch_size.**

| batch_size | Comportamiento |
|---|---|
| 1 (SGD puro) | mucho ruido, lento, escapa mínimos |
| 16-64 | sweet spot para CPU |
| 256-1024 | óptimo para GPU |
| dataset completo | full-batch (volvemos al inicio) |

**Lección.** `DataLoader` es la abstracción que separa "definir cómo se obtiene un dato" (`Dataset.__getitem__`) de "cómo se itera el conjunto" (`DataLoader` con shuffle, batch_size, num_workers). Cuando saltes a imágenes (ImageNet) o NLP (texto largo), reusas exactamente este patrón.
::/practica

---

## Práctica resuelta 3 — Modelo personalizado con `nn.Module`

::practica{titulo="Refactorizar de nn.Sequential a nn.Module para flexibilidad"}
**Problema.** `nn.Sequential` es elegante pero rígido: no soporta múltiples inputs, conexiones residuales, o lógica condicional en forward. Refactoriza a clase `nn.Module`.

**Paso 1 — Estrategia.** Subclase `nn.Module`, defines capas en `__init__`, defines flujo en `forward(x)`.

**Paso 2 — Código.**

```python
import torch
import torch.nn as nn

class PredictorEscolar(nn.Module):
    def __init__(self, input_dim=3, hidden_dims=(32, 16), dropout=0.2):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dims[0])
        self.fc2 = nn.Linear(hidden_dims[0], hidden_dims[1])
        self.fc_out = nn.Linear(hidden_dims[1], 1)
        self.dropout = nn.Dropout(dropout)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        return self.fc_out(x)

    def predict(self, x):
        """Inferencia con eval mode."""
        self.eval()
        with torch.no_grad():
            return self.forward(x)

# Uso idéntico a Sequential
modelo = PredictorEscolar(input_dim=3, hidden_dims=(32, 16), dropout=0.2)
print(modelo)

# Test forward
x_test = torch.randn(5, 3)   # 5 muestras, 3 features
out = modelo(x_test)
print(f"Output shape: {out.shape}")   # esperado: torch.Size([5, 1])
```

**Paso 3 — Beneficios sobre Sequential.**
- **Hiperparámetros explícitos** en `__init__` (input_dim, hidden_dims, dropout).
- **Método `predict`** con `eval` + `no_grad` integrado.
- Fácil de **extender**: agrega `predict_proba`, `embed_features`, etc.
- **Múltiples inputs/outputs** posibles (ej. multi-task learning).

**Paso 4 — Ejemplo de extensión: skip connection (residual).**

```python
class PredictorEscolarResidual(nn.Module):
    def __init__(self, input_dim=3, hidden_dim=16):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc_out = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        h1 = torch.relu(self.fc1(x))
        h2 = torch.relu(self.fc2(h1))
        h2 = h2 + h1                      # ← skip connection
        return self.fc_out(h2)
```

Con `nn.Sequential` esto era imposible. Con `nn.Module`, una línea más.

**Paso 5 — Save/load completo del modelo.**

```python
# Guardar
torch.save({
    "state_dict": modelo.state_dict(),
    "arch": {"input_dim": 3, "hidden_dims": (32, 16), "dropout": 0.2}
}, "predictor_v3.pt")

# Cargar (sin notebook original)
ckpt = torch.load("predictor_v3.pt")
nuevo = PredictorEscolar(**ckpt["arch"])
nuevo.load_state_dict(ckpt["state_dict"])
nuevo.eval()
print("✓ Modelo recargado y listo para inferencia")
```

**Paso 6 — Verificación.** Genera 3 predicciones con `modelo` y 3 con `nuevo`; deben ser idénticas.

**Lección.** `nn.Module` es la abstracción **canónica** de PyTorch. Cualquier modelo del paper más reciente (Transformer, ResNet, GAN) está escrito así. Aprenderlo te abre la puerta a **leer código de papers** y **adaptar** modelos del Hugging Face Hub.
::/practica
