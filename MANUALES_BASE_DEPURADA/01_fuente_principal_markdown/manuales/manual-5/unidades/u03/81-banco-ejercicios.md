---
unidad: 3
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 03

> Practica visualización con matplotlib y seaborn. 
> Cada ejercicio te pide **escribir o leer** código de gráficos.

::interioriza
Imagina que matplotlib es tu caja de herramientas manual, y seaborn es un conjunto de plantillas ya prefabricadas.
::/interioriza

::pausa{}
Antes de empezar:
- ¿Recuerdas cómo importar `pyplot`?
- ¿Y cómo importar `seaborn`?
::/pausa{}

### Bloque A — matplotlib esencial (3.1)

::act-mcq{titulo="Predice qué gráfico genera"}
1. ¿Qué imprime?
   ```python
   import matplotlib.pyplot as plt
   plt.plot([1, 2, 3], [1, 4, 9])
   plt.show()
   ```
   - [ ] Histograma
   - [x] Línea con 3 puntos en y=1, 4, 9
   - [ ] Scatter
   - [ ] Bar chart

2. Para barras horizontales:
   - [ ] `plt.bar(x, y)`
   - [x] `plt.barh(y, x)`
   - [ ] `plt.hbar(x, y)`
   - [ ] `plt.bar(x, y, horizontal=True)`

3. ¿Qué hace `plt.subplots(2, 3)`?
   - [ ] Crea 2 figuras de 3 ejes
   - [x] Crea 1 figura con 6 subplots en grid 2×3
   - [ ] Crea 5 ejes
   - [ ] Error
::/act-mcq

::act-fill{titulo="Plot básico de calificaciones"}
```python
import matplotlib.pyplot as plt

ids = [1, 2, 3, 4, 5]
cals = [7.5, 6.0, 9.0, 4.5, 8.0]

fig, ax = plt.subplots(figsize=(___________, 4))
ax.___________(ids, cals, marker="o")
ax.set_title("___________")
ax.set_xlabel("ID alumno")
ax.set_ylabel("___________")
plt.savefig("plot.png", dpi=200, bbox_inches="___________")
plt.show()
```
::/act-fill

### Bloque B — Histogramas y boxplots (3.2)

::act-mcq{titulo="Elige el gráfico correcto"}
1. Para mostrar **distribución** de una variable continua:
   - [x] Histograma
   - [ ] Bar chart
   - [ ] Pie chart
   - [ ] Heatmap

2. Para comparar **mediana, cuartiles y outliers** entre 3 grupos:
   - [ ] Histogramas separados
   - [x] Boxplot
   - [ ] Scatter
   - [ ] Línea

3. ¿Qué número en un boxplot indica un outlier (con `whis=1.5`)?
   - [ ] Q1 - 1.5×IQR
   - [ ] Q3 + 1.5×IQR
   - [x] Cualquier punto fuera de [Q1-1.5×IQR, Q3+1.5×IQR]
   - [ ] El máximo del array
::/act-mcq

::act-fill{titulo="Histograma con KDE"}
```python
import seaborn as sns

sns.___________(data=df, x="cal_final", bins=___________, kde=True)
plt.axvline(df["cal_final"].___________, color="red", linestyle="--", label="media")
plt.legend()
plt.title("Distribución de calificación final · n=___________")
```
::/act-fill

### Bloque C — Seaborn (3.3)

::act-match{titulo="Función seaborn ↔ uso"}
| Función | Uso |
|---|---|
| 1. `sns.histplot` | a) Relación entre dos variables numéricas |
| 2. `sns.scatterplot` | b) Distribución de una variable |
| 3. `sns.boxplot` | c) Matriz de correlaciones colorida |
| 4. `sns.heatmap` | d) Comparar distribuciones por grupo |
| 5. `sns.pairplot` | e) Todas las combinaciones 2-a-2 |
::/act-match

::act-mcq{titulo="seaborn vs matplotlib"}
1. Ventaja principal de seaborn sobre matplotlib puro:
   - [ ] Es más rápido
   - [x] Sintaxis más compacta para gráficos estadísticos con DataFrames
   - [ ] Soporta 3D nativamente
   - [ ] Reemplaza pandas

2. Para configurar el tema y paleta institucional:
   - [x] `sns.set_theme(style="whitegrid", palette=[...])`
   - [ ] `sns.style("dark")`
   - [ ] `plt.theme("blue")`
   - [ ] No se puede
::/act-mcq

### Bloque D — Personalización (3.4)

::act-fill{titulo="Personaliza un boxplot publicable"}
```python
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x="materia", y="cal_final", ax=ax)
ax.axhline(___________, color="red", linestyle="--", label="Aprobación (6)")
ax.set_title("Distribución por materia", fontsize=14, fontweight="___________")
ax.set_xlabel("___________")
ax.set_ylabel("Calificación (0-10)")
ax.___________()                              # mostrar leyenda
plt.savefig("boxplot.png", dpi=___________, bbox_inches="tight")
```
::/act-fill

### Bloque E — Interpretación visual (3.5)

::act-case{titulo="Caso — qué cuenta este boxplot" lineas=10}
Coordinación te muestra este boxplot resumido:

```
Matemáticas: Q1=4.5, mediana=6.0, Q3=7.5, outliers en {2.0, 9.5}
Física:      Q1=6.0, mediana=7.5, Q3=8.5, sin outliers
Química:     Q1=6.5, mediana=8.0, Q3=9.0, outlier en {3.5}
```

**Pregunta.** 
Escribe en 4–6 líneas qué le dirías al consejo: 
- 1) qué materia preocupa más y por qué
- 2) qué materia está mejor
- 3) qué casos individuales merecen atención
::/act-case

::act-mcq{titulo="Lee el gráfico"}
1. Un scatter de `horas_estudio` vs `cal_final` con nube ascendente sugiere:
   - [ ] No hay relación
   - [x] Correlación positiva
   - [ ] Correlación negativa
   - [ ] Causalidad confirmada

2. Un heatmap de correlaciones con `cal_anterior–cal_final = 0.72` significa:
   - [ ] Sin relación
   - [x] Relación lineal fuerte positiva
   - [ ] Causalidad
   - [ ] Outliers presentes
::/act-mcq

### Bloque F — Storytelling con datos (3.6)

::act-tf{titulo="Buenas prácticas en visualización"}
1. Más colores hacen el gráfico más profesional. ( ) ____________________
2. Eje Y en barras debe empezar en 0 para no engañar visualmente. ( ) ____________________
3. Pie chart con 12 secciones es válido si están bien etiquetadas. ( ) ____________________
4. Una buena visualización transmite **un solo mensaje** principal. ( ) ____________________
5. Anotar los valores en barras evita que el lector tenga que adivinar. ( ) ____________________
::/act-tf

::act-order{titulo="3 actos del storytelling: ordena los gráficos para presentación"}
- [ ] Heatmap de correlaciones (hallazgo: cal_anterior es el predictor #1)
- [ ] Histograma de cal_final (contexto: distribución general)
- [ ] Bar chart de tasa de aprobación con meta institucional (cierre + recomendación)
- [ ] Boxplot por materia (problema: Mate tiene mediana más baja)
- [ ] Scatter horas vs cal_final con regresión (dato clave: relación clara)
::/act-order

### Bloque G — Caso integrador

::act-fill{titulo="Dashboard mínimo en una sola figura"}
```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top-left: histograma
sns.histplot(df["cal_final"], bins=20, ax=axes[___________, 0])
axes[0, 0].set_title("Distribución general")

# Top-right: boxplot por materia
sns.boxplot(data=df, x="materia", y="cal_final", ax=axes[0, ___________])

# Bottom-left: scatter horas vs cal_final
sns.scatterplot(data=df, x="horas_estudio", y="___________", ax=axes[1, 0])

# Bottom-right: heatmap correlaciones
cols = ["horas_estudio", "asistencia", "cal_anterior", "cal_final"]
sns.___________(df[cols].corr(), annot=True, ax=axes[1, 1])

plt.tight_layout()
plt.savefig("dashboard.png", dpi=200)
```
::/act-fill

::act-table{titulo="Pregunta → gráfico ideal"}
| Pregunta de negocio | Gráfico recomendado | Por qué |
|---|---|---|
| ¿Cómo se distribuyen las calificaciones? |  |  |
| ¿Hay diferencia entre materias? |  |  |
| ¿Más horas ↔ mejor cal? |  |  |
| ¿Qué variables predicen mejor? |  |  |
| ¿Qué % aprueba en cada materia? |  |  |
::/act-table

---

## Clave de respuestas

**Bloque A.**
- `act-mcq`: 1·B, 2·B (`barh`), 3·B.
- `act-fill`: `figsize=(8, 4)`, `ax.plot(...)`, título libre, `"Calificación"`, `bbox_inches="tight"`.

**Bloque B.**
- `act-mcq`: 1·A, 2·B, 3·C.
- `act-fill`: `sns.histplot`, `bins=20`, `df["cal_final"].mean()`, `len(df)`.

**Bloque C.**
- `act-match`: 1-b, 2-a, 3-d, 4-c, 5-e.
- `act-mcq`: 1·B, 2·A.

**Bloque D.**
- `act-fill`: `axhline(6, ...)`, `fontweight="bold"`, `set_xlabel("Materia")`, `ax.legend()`, `dpi=200`.

**Bloque E.**
- `act-case`: respuesta modelo:
  > "Matemáticas concentra el problema: mediana 6.0 (apenas pasa) y dispersión más alta (IQR 4.5–7.5) con outliers en ambos extremos.
  > Química está mejor (mediana 8.0). 
  > Atención individual: el outlier de 2.0 en Mate y el de 3.5 en Química son alumnos en riesgo agudo."
- `act-mcq`: 1·B, 2·B.

**Bloque F.**
- `act-tf`: 1·F (más colores ≠ mejor); 2·V (especialmente en barras); 3·F (>5 secciones es ilegible); 4·V; 5·V.
- `act-order`: 2·4·5·1·3 (contexto → problema → dato → hallazgo → cierre).

**Bloque G.**
- `act-fill`: `axes[0, 0]`, `axes[0, 1]`, `y="cal_final"`, `sns.heatmap`.
- `act-table`:

| Pregunta | Gráfico |
|---|---|
| Distribución | histograma |
| Diferencia entre grupos | boxplot |
| Relación 2 numéricas | scatter (con regplot opcional) |
| Predictores | heatmap correlaciones |
| % por categoría | bar chart |

> **Cierre.** 
> Si tus gráficos llevan título, ejes etiquetados y un mensaje claro, ya pasaste el filtro mínimo del consejo académico.
