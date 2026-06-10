---
unidad: 2
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 02

> Practica NumPy y pandas con micro-ejercicios. Reta tu intuición prediciendo outputs antes de ejecutar.

::interioriza
* Imagina que NumPy es como un motor de Fórmula 1: realiza cálculos matemáticos a altísima velocidad.
* pandas es como la carrocería y el tablero: organiza los datos para que puedas conducirlos fácilmente.
* ¡Vamos a probar ambos en este circuito!
::/interioriza

::pausa{}
Antes de empezar:
* ¿Recuerdas cuál es la estructura principal de pandas para tablas?
* Piensa en cómo aplicarías una operación a todos los elementos de un arreglo sin usar bucles.
::/pausa

### Bloque A — NumPy básico (2.1)

::act-mcq{titulo="Predice el output de NumPy"}
1. ¿Qué imprime?
   ```python
   import numpy as np
   a = np.array([1, 2, 3, 4])
   print(a * 2)
   ```
   - [ ] `[1, 2, 3, 4, 1, 2, 3, 4]`
   - [x] `[2 4 6 8]`
   - [ ] `[1 2 3 4]`
   - [ ] Error

2. ¿Cuál es la forma (shape) resultante?
   ```python
   x = np.array([[1, 2, 3], [4, 5, 6]])
   print(x.shape)
   ```
   - [ ] `(3, 2)`
   - [x] `(2, 3)`
   - [ ] `(6,)`
   - [ ] `(1, 6)`

3. ¿Qué imprime `np.array([1, 2, 3]).mean()`?
   - [ ] 6
   - [x] 2.0
   - [ ] 1
   - [ ] 3
::/act-mcq

::act-fill{titulo="Operaciones vectorizadas"}
```python
import numpy as np

cals = np.array([7.5, 6.0, 9.0, 4.5, 8.0])

# Promedio
prom = cals.___________
# Sumar 0.5 a todas (curva)
cals_curva = cals + ___________
# Cuántas >= 6
n_aprueban = (cals >= ___________).sum()
# Calificación más alta
maxima = cals.___________
```
::/act-fill

### Bloque B — pandas Series y DataFrame (2.2)

::act-mcq{titulo="Estructuras pandas"}
1. ¿Cuál crea correctamente un DataFrame de 3 columnas?
   - [ ] `pd.DataFrame([1, 2, 3])`
   - [x] `pd.DataFrame({"a":[1,2], "b":[3,4], "c":[5,6]})`
   - [ ] `pd.Series([1,2,3])`
   - [ ] `pd.DataFrame("a, b, c")`

2. ¿Qué devuelve `df["materia"]` con un DataFrame escolar?
   - [ ] Una lista de Python
   - [x] Una `Series`
   - [ ] Un nuevo `DataFrame`
   - [ ] Un dict

3. Para acceder a la fila con índice 0:
   - [x] `df.iloc[0]`
   - [ ] `df[0]`
   - [ ] `df.row(0)`
   - [ ] `df.first()`
::/act-mcq

::act-fill{titulo="Crear DataFrame desde lista de dicts"}
```python
import pandas as pd

datos = [
    {"id": 1, "cal_final": 7.5, "materia": "Mate"},
    {"id": 2, "cal_final": 8.0, "materia": "Física"},
    {"id": 3, "cal_final": 6.5, "materia": "Mate"},
]

df = pd.___________(datos)
print(df.___________)        # → (3, 3)
print(df.dtypes)              # → tipos por columna
print(df["cal_final"].___________())   # → 7.333... (promedio)
```
::/act-fill

### Bloque C — Lectura de archivos (2.3)

::act-order{titulo="Pasos para leer un CSV europeo (separador ;, decimales ,)"}
[ ] Verificar tipos con `df.dtypes`
[ ] Identificar el separador real con `head archivo.csv`
[ ] Leer con `pd.read_csv(path, sep=";", decimal=",")`
[ ] Importar pandas como pd
[ ] Inspeccionar primeras filas con `df.head()`
::/act-order

::act-mcq{titulo="Predice el comportamiento"}
1. ¿Qué hace `pd.read_csv("a.csv", nrows=5)`?
   - [ ] Lee solo 5 columnas
   - [x] Lee solo las primeras 5 filas
   - [ ] Salta 5 filas
   - [ ] Crea 5 archivos
::/act-mcq

### Bloque D — Limpieza (2.4)

::act-fill{titulo="Pipeline de limpieza con method chaining"}
```python
df_limpio = (df
    .___________(subset=["id"])           # quitar duplicados por id
    .___________(subset=["cal_final"])    # quitar filas con NaN en cal_final
    .query("0 <= cal_final <= ___________")  # rango válido
    .reset_index(drop=___________)
)
print(f"Antes: {len(df)} · Después: {len(df_limpio)}")
```
::/act-fill

::act-tf{titulo="V/F sobre limpieza"}
1. `df.dropna()` sin argumentos elimina filas con **al menos un** NaN. ( ) ____________________
2. `df.fillna(0)` puede sesgar el análisis si hay muchos nulos en numéricas. ( ) ____________________
3. `df.drop_duplicates()` siempre necesita el argumento `subset=`. ( ) ____________________
4. `pd.to_numeric(s, errors="coerce")` convierte y mete `NaN` donde no pueda. ( ) ____________________
::/act-tf

### Bloque E — Filtrado y selección (2.5)

::act-mcq{titulo="Filtrado con condiciones"}
1. ¿Cuál filtra alumnos de Mate Y con cal_final >= 8?
   - [ ] `df[df.materia == "Mate" and df.cal_final >= 8]`
   - [x] `df[(df.materia == "Mate") & (df.cal_final >= 8)]`
   - [ ] `df[df.materia == "Mate" || df.cal_final >= 8]`
   - [ ] `df.where("Mate" and 8)`

2. Para sacar las columnas `id` y `cal_final` solamente:
   - [ ] `df.id.cal_final`
   - [x] `df[["id", "cal_final"]]`
   - [ ] `df["id", "cal_final"]`
   - [ ] `df.select(id, cal_final)`
::/act-mcq

::act-fill{titulo="Filtrar y contar"}
```python
# ¿Cuántos alumnos de Física aprobaron con asistencia >= 0.85?
mask = (df["materia"] == ___________) & (df["cal_final"] >= ___________) & (df["asistencia"] >= ___________)
n = mask.___________
print(f"Físicos aprobados con buena asistencia: {n}")
```
::/act-fill

### Bloque F — groupby y agregaciones (2.6)

::act-mcq{titulo="groupby"}
1. ¿Qué imprime?
   ```python
   df.groupby("materia")["cal_final"].mean()
   ```
   - [ ] Una fila por alumno
   - [x] Una fila por materia con promedio de cal_final
   - [ ] El promedio global solamente
   - [ ] Error

2. Para contar alumnos Y promedio en una sola operación:
   - [ ] `df.groupby("materia").mean().count()`
   - [x] `df.groupby("materia").agg(n=("id","count"), prom=("cal_final","mean"))`
   - [ ] `df.groupby("materia").describe()`
   - [ ] No es posible
::/act-mcq

::act-fill{titulo="Agregación múltiple"}
```python
resumen = df.groupby("___________").agg(
    n=("id", "___________"),
    promedio=("cal_final", "___________"),
    desviacion=("cal_final", "___________"),
    aprobados=("cal_final", lambda x: (x >= ___________).sum())
).round(2)

print(resumen)
```
::/act-fill

### Bloque G — Caso integrador

::act-table{titulo="Equivalencia Python puro vs pandas"}
| Tarea | Python puro (U1) | pandas (U2) |
|---|---|---|
| Cargar CSV | `csv.DictReader + for + dict` |  |
| Quitar nulos en columna | `if val is not None: lista.append(...)` |  |
| Promedio por materia | `for + dict acumulador` |  |
| Top 5 | `sorted(...)[:5]` |  |
| Guardar a CSV | `csv.DictWriter` |  |
::/act-table

::act-case{titulo="Caso — limpia el dataset corrupto" lineas=10}
Recibes `dataset_escolar.csv` con: 480 filas declaradas, **8 duplicados** por `id`, **12 filas con NaN** en `cal_final`, **3 filas** con asistencia >1.0 (imposible). Diseña en pseudocódigo (5–7 líneas) el pipeline pandas exacto que devuelve el dataset limpio. Indica el número final esperado.
::/act-case

::act-tf{titulo="Buenas prácticas pandas"}
1. Mutar el DataFrame original siempre es mejor que devolver uno nuevo. ( ) ____________________
2. `df.copy()` evita modificar el original al hacer cambios. ( ) ____________________
3. Method chaining (`df.X().Y().Z()`) hace el código más legible. ( ) ____________________
4. `inplace=True` está siendo desaconsejado por el equipo de pandas. ( ) ____________________
::/act-tf

---

## Clave de respuestas

**Bloque A.**
- `act-mcq`: 1·B (broadcasting), 2·B, 3·B (mean siempre devuelve float).
- `act-fill`: `cals.mean()`, `+ 0.5`, `>= 6`, `cals.max()`.

**Bloque B.**
- `act-mcq`: 1·B, 2·B, 3·A.
- `act-fill`: `pd.DataFrame(datos)`, `df.shape`, `df["cal_final"].mean()`.

**Bloque C.**
- `act-order`: 4·2·3·5·1 (importar → inspeccionar separador → leer → head → dtypes).
- `act-mcq`: 1·B.

**Bloque D.**
- `act-fill`: `drop_duplicates`, `dropna`, `<= 10`, `drop=True`.
- `act-tf`: 1·V; 2·V; 3·F (sin subset elimina duplicados completos); 4·V.

**Bloque E.**
- `act-mcq`: 1·B (operadores `&` con paréntesis), 2·B (lista de columnas).
- `act-fill`: `"Física"`, `>= 6`, `>= 0.85`, `mask.sum()`.

**Bloque F.**
- `act-mcq`: 1·B, 2·B (`agg` con tuplas).
- `act-fill`: `groupby("materia")`, `("id", "count")`, `("cal_final", "mean")`, `("cal_final", "std")`, `(x >= 6).sum()`.

**Bloque G.**
- `act-table`:

| Tarea | pandas |
|---|---|
| Cargar CSV | `pd.read_csv(path)` |
| Quitar nulos | `df.dropna(subset=["col"])` |
| Promedio por materia | `df.groupby("materia")["cal"].mean()` |
| Top 5 | `df.nlargest(5, "cal_final")` |
| Guardar a CSV | `df.to_csv(path, index=False)` |

- `act-case`: pipeline modelo:
```python
df = pd.read_csv("dataset_escolar.csv")
df = (df.drop_duplicates(subset=["id"])      # -8 → 472
        .dropna(subset=["cal_final"])         # -12 (de los que queden) → ~460
        .query("0 <= asistencia <= 1")        # -3 → ~457
        .reset_index(drop=True))
print(df.shape)   # esperado ≈ (457, 6)
```
- `act-tf`: 1·F (devolver nuevo es más seguro); 2·V; 3·V; 4·V.

> **Cierre.** Si pasaste 70 % de los bloques A–F, tu base pandas está sólida para U3.
