---
unidad: 3
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 03

::practica{titulo="Dashboard de 5 gráficas para presentación al consejo académico"}
**Problema.** Producir 5 gráficas que cuenten la historia "Predictor de rendimiento escolar — diagnóstico inicial" para presentación al consejo en 10 min.

**Paso 1 — Estrategia.** Aplicar storytelling: contexto → problema → datos → hallazgo → recomendación. 5 gráficas correspondientes:
1. Histograma de calificación final (contexto: distribución general).
2. Boxplot por materia (problema: Matemáticas más baja).
3. Scatter horas-vs-cal con regresión (dato clave: correlación clara).
4. Heatmap de correlaciones (hallazgo: cal_anterior es el mejor predictor).
5. Bar chart de tasa de aprobación por materia con línea de meta institucional.

**Paso 2 — Código.**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo institucional
sns.set_theme(style="whitegrid", palette=["#0E3A8A", "#1E5BB8", "#F39C12"])

df = pd.read_csv("dataset_escolar_limpio.csv")

# 1. Histograma general
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=df, x="cal_final", bins=20, kde=True, ax=ax)
ax.axvline(df["cal_final"].mean(), color="red", linestyle="--", label=f"Media={df['cal_final'].mean():.2f}")
ax.set_title("Distribución de calificaciones finales · n=470", fontsize=14, fontweight="bold")
ax.set_xlabel("Calificación (0–10)")
ax.set_ylabel("Estudiantes")
ax.legend()
plt.savefig("01_distribucion.png", dpi=200, bbox_inches="tight")
plt.show()

# 2. Boxplot por materia
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x="materia", y="cal_final", ax=ax)
ax.axhline(6, color="red", linestyle="--", label="Aprobación")
ax.set_title("Distribución por materia · Mate muestra mediana más baja", fontsize=14)
ax.set_xlabel("Materia")
ax.set_ylabel("Calificación final")
ax.legend()
plt.savefig("02_por_materia.png", dpi=200, bbox_inches="tight")
plt.show()

# 3. Scatter con tendencia
fig, ax = plt.subplots(figsize=(10, 6))
sns.regplot(data=df, x="horas_estudio", y="cal_final", scatter_kws={"alpha":0.4}, ax=ax)
ax.set_title("Horas de estudio vs calificación final · correlación positiva", fontsize=14)
ax.set_xlabel("Horas de estudio semanales")
ax.set_ylabel("Calificación final")
plt.savefig("03_scatter.png", dpi=200, bbox_inches="tight")
plt.show()

# 4. Heatmap correlaciones
fig, ax = plt.subplots(figsize=(8, 6))
cols = ["horas_estudio", "asistencia", "cal_anterior", "cal_final"]
sns.heatmap(df[cols].corr(), annot=True, cmap="RdBu_r", center=0, ax=ax)
ax.set_title("Correlaciones · cal_anterior es el predictor más fuerte (0.72)", fontsize=14)
plt.savefig("04_heatmap.png", dpi=200, bbox_inches="tight")
plt.show()

# 5. Tasa de aprobación
tasas = df.groupby("materia").apply(lambda x: (x["cal_final"] >= 6).mean() * 100)
fig, ax = plt.subplots(figsize=(10, 6))
colors = ["#0E3A8A" if t < 80 else "#F39C12" for t in tasas]
ax.bar(tasas.index, tasas.values, color=colors)
ax.axhline(80, color="red", linestyle="--", label="Meta institucional 80%")
for i, v in enumerate(tasas.values):
    ax.text(i, v + 1, f"{v:.0f}%", ha="center", fontweight="bold")
ax.set_title("Tasa de aprobación por materia · Mate por debajo de meta", fontsize=14)
ax.set_xlabel("Materia")
ax.set_ylabel("% aprobados")
ax.legend()
plt.savefig("05_tasa_aprobacion.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Paso 3 — Presentación.**
- Slide 1: portada con título y autor.
- Slide 2: gráfico 1 (contexto: "tenemos 470 alumnos, distribución asimétrica negativa").
- Slide 3: gráfico 2 (problema: "Mate es la materia con peor desempeño").
- Slide 4: gráfico 3 (relación: "más horas → mejor calificación, claro").
- Slide 5: gráfico 4 (hallazgo: "calificación anterior predice fuertemente la actual").
- Slide 6: gráfico 5 (cierre: "Mate por debajo de meta institucional").
- Slide 7: recomendación (1 frase).

**Paso 4 — Verificación.** Comparte slides con un compañero. Hazle leer el set sin tu voz. Si entiende la historia, está bien. Si pregunta "y esto qué", retiraste mal el storytelling.

**Respuesta.** 5 gráficas + 7 slides listas para presentación de 10 minutos. Mensajes destacados con anotaciones, paleta institucional, tipografía clara. Tiempo total de producción: 3 horas.

**Lección.** Las 6 técnicas de la unidad encajan: matplotlib base, histogramas/boxplots para distribución, seaborn para velocidad estética, personalización para nivel publicación, interpretación para sacar mensaje, storytelling para secuenciarlo. Lo último —storytelling— es lo que más diferencia entre análisis y comunicación.
::/practica

---

## Práctica resuelta 2 — Pairplot diagnóstico para EDA rápido

::practica{titulo="Pairplot del dataset escolar para detectar relaciones en 30 segundos"}
**Problema.** Antes de modelar, querer ver **todas las combinaciones 2-a-2** de variables numéricas en una sola figura. Útil para cazar relaciones inesperadas.

**Paso 1 — Estrategia.** `sns.pairplot` con coloreado por variable categórica.

**Paso 2 — Código.**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_escolar_limpio.csv")

# Crear etiqueta para colorear (aprueba/reprueba)
df["resultado"] = df["cal_final"].apply(lambda c: "Aprueba" if c >= 6 else "Reprueba")

# Pairplot
sns.set_theme(style="whitegrid")
g = sns.pairplot(
    df[["horas_estudio", "asistencia", "cal_anterior", "cal_final", "resultado"]],
    hue="resultado",
    palette={"Aprueba": "#0E3A8A", "Reprueba": "#F39C12"},
    diag_kind="kde",
    plot_kws={"alpha": 0.5, "s": 30}
)
g.fig.suptitle(
    "Pairplot · variables numéricas vs resultado",
    y=1.02, fontsize=14, fontweight="bold"
)
g.savefig("pairplot.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Paso 3 — Lectura del pairplot.**

| Diagonal | Histograma/KDE de cada variable separado por aprueba/reprueba |
| Fuera de diagonal | Scatter 2-a-2; busca clusters separados de color |

**Lo que cazas con el ojo:**
- ¿La nube de "Reprueba" está concentrada en horas bajas? → variable predictiva.
- ¿Las dos clases se mezclan en `horas_estudio` pero se separan en `cal_anterior`? → cal_anterior es mejor predictor.
- ¿Ves curvatura no-lineal en algún scatter? → considera transformación o árbol en lugar de lineal.

**Paso 4 — Decisión derivada.** En este dataset:
- **cal_anterior**: separación visual clara → predictor #1.
- **asistencia**: separación moderada → predictor #2.
- **horas_estudio**: cierto solapamiento → predictor #3, útil pero no determinante.

**Paso 5 — Verificación.** Compara las separaciones del pairplot con los coeficientes de correlación del heatmap. Las variables con mejor separación visual deberían tener mayor `|r|`. Si no coinciden, sospecha relación no-lineal.

**Lección.** Un pairplot es **30 segundos de generación, 5 minutos de lectura, ahorras horas de modelado**. Antes de cualquier `model.fit()`, mira tus variables. El pairplot es la versión rica del heatmap (que solo muestra correlación lineal).
::/practica

---

## Práctica resuelta 3 — Anotaciones inteligentes y export multi-formato

::practica{titulo="Gráfica con anotaciones que destacan al alumno con peor desempeño"}
**Problema.** En un scatter de 465 puntos, marcar al alumno con menor `cal_final` con flecha y nombre, y exportar en 3 formatos (PNG, SVG, PDF) listos para presentación, web e impresión.

**Paso 1 — Estrategia.** Identificar punto extremo, dibujar scatter, agregar `ax.annotate(...)`, exportar 3 veces con `plt.savefig`.

**Paso 2 — Código.**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_escolar_limpio.csv")

# Identificar alumno con cal_final mínima
peor = df.loc[df["cal_final"].idxmin()]
print(f"Caso crítico: id={peor['id']}, cal_final={peor['cal_final']}, "
      f"asistencia={peor['asistencia']:.0%}, horas={peor['horas_estudio']}")

# Scatter principal
fig, ax = plt.subplots(figsize=(11, 7))
sns.scatterplot(data=df, x="horas_estudio", y="cal_final",
                hue="materia", alpha=0.5, s=40, ax=ax)

# Línea de referencia: aprobación
ax.axhline(6, color="red", linestyle="--", linewidth=1,
           label="Aprobación")

# Marcar el caso crítico
ax.scatter(peor["horas_estudio"], peor["cal_final"],
           s=200, edgecolors="red", facecolors="none", linewidths=2)

# Anotación con flecha
ax.annotate(
    f"Caso crítico\nID {int(peor['id'])}\n"
    f"Asistencia {peor['asistencia']:.0%}",
    xy=(peor["horas_estudio"], peor["cal_final"]),
    xytext=(peor["horas_estudio"] + 1.5, peor["cal_final"] + 1.5),
    fontsize=10,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#FFFACD", edgecolor="gray"),
    arrowprops=dict(arrowstyle="->", color="black", lw=1.2)
)

ax.set_title("Horas vs calificación · alumno con peor desempeño identificado",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Horas de estudio semanales")
ax.set_ylabel("Calificación final")
ax.legend(loc="lower right")

# Export multi-formato
for ext, dpi in [("png", 200), ("svg", None), ("pdf", None)]:
    nombre = f"scatter_anotado.{ext}"
    if dpi:
        plt.savefig(nombre, dpi=dpi, bbox_inches="tight")
    else:
        plt.savefig(nombre, bbox_inches="tight")
    print(f"✓ {nombre}")
plt.show()
```

**Paso 3 — Output esperado.**
```
Caso crítico: id=287, cal_final=3.5, asistencia=52%, horas=1.0
✓ scatter_anotado.png
✓ scatter_anotado.svg
✓ scatter_anotado.pdf
```

**Paso 4 — Cuándo usar cada formato.**
- **PNG** (200 dpi): presentaciones, redes, screenshots. Tamaño moderado, cualquier visor.
- **SVG**: vectorial, escalable; ideal para web responsiva o ediciones posteriores en Illustrator/Inkscape.
- **PDF**: vectorial, ideal para impresión profesional o reportes oficiales.

**Paso 5 — Verificación.** Abre el PNG y verifica que la anotación es legible. Abre el SVG en navegador, haz zoom; el texto debe quedar nítido (vs PNG que se pixelea).

**Lección.** Los detalles de presentación —anotaciones, círculos destacando, leyendas claras— **convierten un gráfico técnico en un gráfico que decisión-makers entienden en 5 segundos**. Y entregar 3 formatos significa que el receptor (impresor, web, junta) lo usa sin pedirte conversiones después.
::/practica
