---
unidad: 3
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Unidad 03

::albatros{titulo="Genera 5 gráficas exploratorias del dataset escolar limpio" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si tuvieras 5 minutos para presentar lo que **descubriste** sobre los 465 alumnos a la coordinadora, ¿qué 5 imágenes pondrías en la pantalla y por qué?

**Contexto del case.** Tienes el `dataset_escolar_limpio.csv` de U2. Antes de pensar en modelos (U5+), hay que **mirar los datos**. Un buen EDA visual ahorra semanas de modelado a ciegas.

### Materiales

- Python 3 + pandas + matplotlib + seaborn.
- Notebook (Jupyter / Colab).
- Dataset limpio de U2.

### Pasos del taller (60 min)

**Paso 1 — Setup y carga (5 min).**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tema institucional Albatros
sns.set_theme(
    style="whitegrid",
    palette=["#0E3A8A", "#1E5BB8", "#F39C12"]
)

df = pd.read_csv("dataset_escolar_limpio.csv")
print(f"Cargado: {df.shape}")
print(df.head())
```

**Paso 2 — Gráfica 1: distribución general (10 min).**

```python
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=df, x="cal_final", bins=20, kde=True, ax=ax,
             color="#0E3A8A")
ax.axvline(df["cal_final"].mean(), color="red", linestyle="--",
           label=f"Media={df['cal_final'].mean():.2f}")
ax.axvline(6, color="orange", linestyle=":",
           label="Aprobación")
ax.set_title(f"Distribución de calificación final · n={len(df)}",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Calificación (0–10)")
ax.set_ylabel("Estudiantes")
ax.legend()
plt.savefig("g1_distribucion.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Mensaje (anótalo en tu notebook):** "La distribución es ligeramente asimétrica negativa; la media (≈7.4) está sobre la mediana, sugiriendo cola izquierda con alumnos en riesgo".

**Paso 3 — Gráfica 2: comparación por materia (10 min).**

```python
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x="materia", y="cal_final", ax=ax)
ax.axhline(6, color="red", linestyle="--", label="Aprobación")
ax.set_title("Distribución por materia · ¿alguna materia preocupa?",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Materia")
ax.set_ylabel("Calificación final")
ax.legend()
plt.savefig("g2_por_materia.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Mensaje:** "Matemáticas tiene mediana más baja y mayor dispersión — foco de intervención".

**Paso 4 — Gráfica 3: relación horas vs calificación (10 min).**

```python
fig, ax = plt.subplots(figsize=(10, 6))
sns.regplot(data=df, x="horas_estudio", y="cal_final",
            scatter_kws={"alpha": 0.4, "color": "#0E3A8A"},
            line_kws={"color": "#F39C12"}, ax=ax)
r = df["horas_estudio"].corr(df["cal_final"])
ax.set_title(f"Horas de estudio vs calificación · r={r:.2f}",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Horas de estudio semanales")
ax.set_ylabel("Calificación final")
plt.savefig("g3_horas_vs_cal.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Mensaje:** "Correlación positiva moderada (r≈0.42): más horas correlaciona con mejor cal, pero no es determinante".

**Paso 5 — Gráfica 4: heatmap de correlaciones (10 min).**

```python
fig, ax = plt.subplots(figsize=(8, 6))
cols = ["horas_estudio", "asistencia", "cal_anterior", "cal_final"]
sns.heatmap(df[cols].corr(), annot=True, fmt=".2f",
            cmap="RdBu_r", center=0, ax=ax)
ax.set_title("Matriz de correlaciones · cal_anterior es el predictor #1",
             fontsize=14, fontweight="bold")
plt.savefig("g4_heatmap.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Mensaje:** "cal_anterior tiene la correlación más alta con cal_final (r≈0.72), seguido de asistencia (r≈0.55)".

**Paso 6 — Gráfica 5: tasa de aprobación con meta (10 min).**

```python
tasas = (df.groupby("materia")
           .apply(lambda x: (x["cal_final"] >= 6).mean() * 100)
           .sort_values(ascending=False))

fig, ax = plt.subplots(figsize=(10, 6))
colors = ["#0E3A8A" if t >= 80 else "#F39C12" if t >= 70 else "#C0392B"
          for t in tasas.values]
bars = ax.bar(tasas.index, tasas.values, color=colors)
ax.axhline(80, color="red", linestyle="--",
           label="Meta institucional 80%")
for bar, val in zip(bars, tasas.values):
    ax.text(bar.get_x() + bar.get_width()/2, val + 1,
            f"{val:.0f}%", ha="center", fontweight="bold")
ax.set_title("Tasa de aprobación por materia",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Materia")
ax.set_ylabel("% aprobados")
ax.set_ylim(0, 100)
ax.legend()
plt.savefig("g5_tasa_aprobacion.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Paso 7 — Storytelling: ordena las 5 gráficas (5 min).**

Para presentar al consejo, **el orden cuenta una historia**:

1. **g1_distribucion.png** — contexto: "tenemos 465 alumnos con esta distribución".
2. **g2_por_materia.png** — problema: "Mate preocupa".
3. **g3_horas_vs_cal.png** — dato clave: "horas correlacionan, pero moderado".
4. **g4_heatmap.png** — hallazgo: "cal_anterior es el mejor predictor".
5. **g5_tasa_aprobacion.png** — cierre + recomendación: "Mate por debajo de meta institucional → intervenir".

### Entregable

- Notebook con las 5 gráficas + comentarios de mensaje.
- 5 archivos PNG (200 dpi, fondo blanco).
- Documento de 1 página con los 5 mensajes ordenados como historia.

### Rúbrica corta

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| 5 gráficas generadas | <3 | 4 | las 5 con título y ejes |
| Personalización | default | colores | paleta institucional + anotaciones |
| Mensaje por gráfica | sin | implícito | escrito en una frase |
| Storytelling | sin orden | ordenado | secuencia lógica defendida |
| Reproducibilidad | un solo run | corre 2 veces | semilla + comentarios + paths claros |

### Conexión con el case

Estas 5 imágenes son **el diagnóstico inicial del Predictor de rendimiento escolar**. En U4 vas a defender estadísticamente lo que ahora ves visualmente. En U5, los predictores que el heatmap te marcó (cal_anterior, asistencia, horas_estudio) son las features que entrenarán el modelo. Esta unidad no es decoración: es el filtro de qué meterle al modelo.
::/albatros
