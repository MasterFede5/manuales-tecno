---
unidad: 4
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 04

> Practica estadística aplicada con código real. Cada ejercicio te pide leer un output o predecir el resultado.

### Bloque A — Tendencia central y dispersión (4.1)

::act-mcq{titulo="Predice los estadísticos"}
1. Lista `[5, 6, 7, 8, 100]`. ¿Qué afirmación es correcta?
   - [ ] mediana ≈ media
   - [x] media >> mediana (sesgada por outlier)
   - [ ] media < mediana
   - [ ] media = moda
   
2. ¿Qué imprime?
   ```python
   import numpy as np
   np.array([2, 4, 4, 4, 5, 5, 7, 9]).std(ddof=0).round(3)
   ```
   - [ ] 1.581
   - [x] 2.0
   - [ ] 4.875
   - [ ] 3.0

3. Para datos asimétricos con outliers, **lo más representativo del centro** es:
   - [ ] Media
   - [x] Mediana
   - [ ] Moda
   - [ ] Suma
::/act-mcq

::act-fill{titulo="Reporte de tendencia central"}
```python
import pandas as pd

df = pd.read_csv("dataset_escolar_limpio.csv")
cal = df["cal_final"]

print(f"Media:    {cal.___________():.2f}")
print(f"Mediana:  {cal.___________():.2f}")
print(f"Moda:     {cal.___________()[0]:.2f}")
print(f"Std:      {cal.___________():.2f}")
print(f"Var:      {cal.___________():.2f}")
print(f"Rango:    {cal.max() - cal.___________():.2f}")
```
::/act-fill

### Bloque B — Distribución normal (4.2)

::act-mcq{titulo="Regla 68-95-99.7"}
1. Una distribución con `µ=7` y `σ=1`. ¿Qué porcentaje cae entre 6 y 8?
   - [ ] 50%
   - [x] ~68%
   - [ ] 95%
   - [ ] 99.7%

2. El mismo set, ¿qué % cae fuera de [5, 9]?
   - [ ] 0%
   - [ ] 5%
   - [x] ~5%
   - [ ] 32%

3. Para verificar normalidad visualmente:
   - [ ] Bar chart
   - [x] QQ-plot o histograma con KDE
   - [ ] Pie chart
   - [ ] Heatmap
::/act-mcq

::act-fill{titulo="Generar y graficar normal"}
```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(___________)
muestras = np.random.normal(loc=___________, scale=1.5, size=1000)

fig, ax = plt.subplots()
ax.hist(muestras, bins=___________, density=True, alpha=0.6)
ax.set_title("Distribución normal · µ=7, σ=1.5")
plt.savefig("normal.png", dpi=200, bbox_inches="tight")
```
::/act-fill

### Bloque C — Percentiles y cuartiles (4.3)

::act-mcq{titulo="Lectura de percentiles"}
1. P25 = 6.0, P50 = 7.5, P75 = 8.5. El IQR es:
   - [ ] 1.5
   - [x] 2.5
   - [ ] 6.0
   - [ ] 8.5

2. Si tu calificación es percentil 90, significa:
   - [ ] Sacaste 9.0
   - [x] Estás por encima del 90% del grupo
   - [ ] El 90% sacó lo mismo que tú
   - [ ] Tu nota es exactamente la media + 1σ
::/act-mcq

::act-fill{titulo="Calcular percentiles clave"}
```python
percentiles = df["cal_final"].___________([0.10, 0.25, 0.50, 0.75, 0.90])
print(percentiles)

q1, q3 = df["cal_final"].quantile([___________, ___________])
iqr = ___________ - q1
print(f"IQR: {iqr:.2f}")
```
::/act-fill

### Bloque D — Correlación Pearson (4.4)

::act-mcq{titulo="Interpretar r"}
1. r = -0.85 indica:
   - [ ] Sin relación
   - [ ] Relación positiva fuerte
   - [x] Relación negativa fuerte
   - [ ] Causalidad

2. r = 0.05 sugiere:
   - [x] Esencialmente sin relación lineal
   - [ ] Relación moderada
   - [ ] Causalidad débil
   - [ ] Correlación perfecta

3. ¿Cuál NO es propiedad de r?
   - [ ] Está entre -1 y +1
   - [ ] Adimensional
   - [x] Detecta relaciones cuadráticas y exponenciales
   - [ ] Mide fuerza de relación lineal
::/act-mcq

::act-fill{titulo="Matriz de correlaciones con pandas"}
```python
cols = ["horas_estudio", "asistencia", "cal_anterior", "cal_final"]
corr = df[cols].___________()
print(corr.round(___________))

# Predictor más correlacionado con cal_final (excluyendo a sí misma)
predictor_top = corr["cal_final"].___________(ascending=False).index[___________]
print(f"Predictor #1: {predictor_top}")
```
::/act-fill

### Bloque E — Correlación vs causalidad (4.5)

::act-tf{titulo="Correlación o causalidad"}
1. Helado y ahogamientos correlacionan; comer helado **causa** ahogarse. ( ) ____________________
2. Una correlación r=0.95 garantiza causalidad. ( ) ____________________
3. Para afirmar causalidad necesitas un experimento controlado o supuestos fuertes. ( ) ____________________
4. Una variable de confusión (confounder) puede generar correlación espuria. ( ) ____________________
5. Decir "asistencia correlaciona con cal_final" es válido; "asistencia causa cal_final" no, sin más evidencia. ( ) ____________________
::/act-tf

::act-case{titulo="Caso — explica la correlación espuria" lineas=8}
Datos del case escolar muestran `r(altura, cal_final) = 0.18` (positiva débil). El director propone: "alumnos más altos rinden mejor; aumentemos la nutrición para hacerlos crecer".

**Pregunta.** Identifica al menos **un confounder** plausible y explica por qué la causalidad propuesta no se sostiene aún si la correlación fuera más alta.
::/act-case

### Bloque F — Outliers (4.6)

::act-mcq{titulo="Detección de outliers"}
1. Para datos no-normales, la regla más robusta es:
   - [ ] Z-score con umbral 3
   - [x] IQR con factor 1.5
   - [ ] Eliminar el 5% superior
   - [ ] Visual a ojo

2. Un outlier IQR es cualquier valor:
   - [ ] Mayor a la media + 2σ
   - [x] Fuera de [Q1 - 1.5·IQR, Q3 + 1.5·IQR]
   - [ ] Fuera de [P5, P95]
   - [ ] Mayor que el máximo razonable
::/act-mcq

::act-fill{titulo="Detector de outliers IQR"}
```python
def outliers_iqr(serie):
    q1, q3 = serie.quantile([0.25, ___________])
    iqr = ___________ - q1
    lo = q1 - 1.5 * ___________
    hi = q3 + 1.5 * iqr
    return serie[(serie < lo) | (serie ___________ hi)]

outs = outliers_iqr(df["cal_final"])
print(f"Outliers detectados: {len(___________)}")
print(outs.head())
```
::/act-fill

### Bloque G — Caso integrador

::act-table{titulo="Defender afirmaciones del case"}
Para cada afirmación, marca si es **correlación válida**, **causal sin evidencia** o **falsa**.

| Afirmación | Tipo | Justificación |
|---|---|---|
| "cal_anterior correlaciona r=0.72 con cal_final" |  |  |
| "Más asistencia causa mejor calificación" |  |  |
| "Quien estudia 7 h/sem siempre aprueba" |  |  |
| "Hay correlación moderada entre horas_estudio y cal_final" |  |  |
| "Los outliers son siempre alumnos en riesgo" |  |  |
::/act-table

::act-mcq{titulo="Decisión estadística"}
1. r=0.45 entre horas_estudio y cal_final. Tu recomendación a coordinación:
   - [ ] "Aumenta horas obligatorias, esto causa mejor cal"
   - [x] "Hay relación moderada; las horas explican parte del rendimiento, otros factores también"
   - [ ] "No hay relación útil"
   - [ ] "El r alto demuestra causalidad"
::/act-mcq

---

## Clave de respuestas

**Bloque A.**
- `act-mcq`: 1·B (outlier 100 jala la media), 2·B (varianza poblacional), 3·B.
- `act-fill`: `cal.mean()`, `cal.median()`, `cal.mode()[0]`, `cal.std()`, `cal.var()`, `cal.min()`.

**Bloque B.**
- `act-mcq`: 1·B (68% en ±1σ), 2·C (~5% fuera de ±2σ), 3·B.
- `act-fill`: `seed(42)`, `loc=7`, `bins=30`.

**Bloque C.**
- `act-mcq`: 1·B (8.5−6.0=2.5), 2·B.
- `act-fill`: `quantile`, `0.25, 0.75`, `q3`.

**Bloque D.**
- `act-mcq`: 1·C, 2·A, 3·C (Pearson solo lineal).
- `act-fill`: `df[cols].corr()`, `round(2)`, `sort_values`, `index[1]` (saltar la diagonal).

**Bloque E.**
- `act-tf`: 1·F (verano es confounder); 2·F; 3·V; 4·V; 5·V.
- `act-case`: respuesta modelo:
  > "Confounder: nivel socioeconómico. Familias con mejor situación tienden a tener hijos más altos (mejor nutrición temprana) y mejor rendimiento (apoyo educativo, recursos). Aumentar nutrición no convierte la correlación espuria en causalidad sin un experimento controlado."

**Bloque F.**
- `act-mcq`: 1·B, 2·B.
- `act-fill`: `0.75`, `q3 - q1`, `iqr`, `>`, `len(outs)`.

**Bloque G.**
- `act-table`:

| Afirmación | Tipo |
|---|---|
| cal_anterior correlaciona r=0.72 | correlación válida |
| Asistencia **causa** mejor cal | causal sin evidencia |
| Quien estudia 7h **siempre** aprueba | falsa (universaliza) |
| Correlación moderada horas-cal | correlación válida |
| Outliers son **siempre** en riesgo | falsa (pueden ser alumnos brillantes) |

- `act-mcq`: 1·B.

> **Cierre.** Distinguir correlación de causalidad es la habilidad estadística #1 que coordinación valora cuando recibe tus reportes.
