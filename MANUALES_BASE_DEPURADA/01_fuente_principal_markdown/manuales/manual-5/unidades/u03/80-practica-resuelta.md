---
unidad: 3
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 03

::practica{titulo="Dashboard de 5 gráficas para presentación al consejo académico"}
**Problema.** 
- Debemos producir 5 gráficas. 
- Contarán la historia "Predictor de rendimiento escolar — diagnóstico inicial".
- Su objetivo es una presentación al consejo en 10 minutos.

**Paso 1 — Estrategia.** 
- Aplicaremos *storytelling*: contexto → problema → datos → hallazgo → recomendación. 
- Las 5 gráficas correspondientes serán:
  1. Histograma de calificación final (contexto general).
  2. Boxplot por materia (problema central).
  3. Scatter horas-vs-cal con regresión (dato clave).
  4. Heatmap de correlaciones (el hallazgo principal).
  5. Bar chart de tasa de aprobación por materia.

::interioriza
Imagina que cuentas un chisme escolar: primero ubicas a los personajes (contexto), luego el drama (problema), muestras los mensajes (datos), descubres al culpable (hallazgo) y sugieres qué hacer (recomendación).
::/interioriza

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
- **Slide 1:** Portada con título y autor.
- **Slide 2:** Gráfico 1 (contexto de los 470 alumnos).
- **Slide 3:** Gráfico 2 ("Mate es la peor").
- **Slide 4:** Gráfico 3 ("más horas → mejor nota").
- **Slide 5:** Gráfico 4 ("calificación anterior es el mejor predictor").
- **Slide 6:** Gráfico 5 ("Mate por debajo de meta institucional").
- **Slide 7:** Recomendación en una frase.

**Paso 4 — Verificación.** 
- Comparte tus slides con un compañero. 
- Hazle leer el set sin tu voz ni explicaciones extra.
- Si entiende la historia, tu presentación está lista.

**Respuesta.** 
- Tenemos 5 gráficas y 7 slides para presentar en 10 minutos. 
- Mensajes destacados con paleta institucional.
- Tiempo de producción: 3 horas.

**Lección.** 
- Las técnicas aprendidas encajan perfectamente (matplotlib, seaborn).
- El *storytelling* es lo que diferencia un simple análisis de una comunicación efectiva.

::pausa{}
**Deduce:**
1. ¿Por qué ordenamos el boxplot antes que el heatmap en la presentación?
2. Si un colega no entiende las slides sin tu explicación, ¿qué fallo de storytelling ocurrió?
::/pausa
::/practica

---

## Práctica resuelta 2 — Pairplot diagnóstico para EDA rápido

::practica{titulo="Pairplot del dataset escolar para detectar relaciones en 30 segundos"}
**Problema.** 
- Antes de modelar, queremos ver **todas las combinaciones 2-a-2** de variables numéricas.
- Esto nos permite cazar relaciones inesperadas rápidamente en una sola figura.

**Paso 1 — Estrategia.** 
- Usaremos `sns.pairplot`.
- Colorearemos los datos por variable categórica (aprueba/reprueba).

::interioriza
El pairplot es como una foto de graduación de todas tus variables numéricas. Te permite ver quién se junta con quién (correlación) y quiénes se evitan, en un solo vistazo general.
::/interioriza

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
- **Diagonal:** Muestra el Histograma/KDE de cada variable, separado por clases.
- **Fuera de diagonal:** Muestra Scatter 2-a-2 para buscar clusters.

*Lo que cazas con el ojo:*
- ¿La nube de "Reprueba" está en horas bajas? → Es predictiva.
- ¿Se separan más en `cal_anterior`? → Mejor predictor.
- ¿Hay curva no-lineal? → Piensa en árboles, no regresión lineal.

**Paso 4 — Decisión derivada.** 
- **cal_anterior:** Separación visual clara (Predictor #1).
- **asistencia:** Separación moderada (Predictor #2).
- **horas_estudio:** Cierto solapamiento (Útil, pero no determinante).

**Paso 5 — Verificación.** 
- Compara estas separaciones visuales con los coeficientes del heatmap. 
- Mayor separación visual debe coincidir con un mayor `|r|`.
- Si no coinciden, sospecha de una relación no-lineal.

**Lección.** 
- Un pairplot toma **30 segundos en generar y 5 minutos en leer**. 
- Ahorra horas de modelado al revelar patrones ocultos antes del `model.fit()`.

::pausa{}
**Deduce:**
1. Si dos variables en el pairplot muestran una nube redonda sin forma, ¿qué significa para su uso en modelos predictivos?
2. ¿Por qué colorear por "resultado" (aprueba/reprueba) acelera tanto el diagnóstico?
::/pausa
::/practica

---

## Práctica resuelta 3 — Anotaciones inteligentes y export multi-formato

::practica{titulo="Gráfica con anotaciones que destacan al alumno con peor desempeño"}
**Problema.** 
- Tenemos un scatter de 465 puntos.
- Queremos marcar al alumno con menor `cal_final` con flecha y texto.
- Exportaremos en 3 formatos (PNG, SVG, PDF) para distintos usos.

**Paso 1 — Estrategia.** 
- Identificar el punto extremo con pandas.
- Dibujar el scatter y usar `ax.annotate(...)`.
- Exportar 3 veces con un ciclo `for`.

::interioriza
Anotar un gráfico es como ponerle subtítulos a una película. Sin ellos, el público ve la acción pero puede perderse el punto crucial de la escena.
::/interioriza

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
```text
Caso crítico: id=287, cal_final=3.5, asistencia=52%, horas=1.0
✓ scatter_anotado.png
✓ scatter_anotado.svg
✓ scatter_anotado.pdf
```

**Paso 4 — Cuándo usar cada formato.**
- **PNG (200 dpi):** Para presentaciones y redes. Tamaño moderado.
- **SVG:** Vectorial para web responsiva o Illustrator.
- **PDF:** Vectorial profesional para impresión o reportes.

**Paso 5 — Verificación.** 
- Abre el PNG y verifica la legibilidad de la anotación. 
- Abre el SVG en tu navegador y haz zoom.
- El texto en SVG debe seguir nítido, a diferencia del PNG.

**Lección.** 
- Detalles de presentación (anotaciones, leyendas claras) convierten gráficos en herramientas directivas. 
- Entregar en 3 formatos evita solicitudes extra de conversiones.

::pausa{}
**Deduce:**
1. Si fueras a imprimir la gráfica en una lona gigante para una conferencia, ¿qué formato debes usar y por qué?
2. ¿Por qué identificamos el "punto extremo" programáticamente (`idxmin`) en vez de buscar sus coordenadas (x,y) a mano en el gráfico?
::/pausa
::/practica
