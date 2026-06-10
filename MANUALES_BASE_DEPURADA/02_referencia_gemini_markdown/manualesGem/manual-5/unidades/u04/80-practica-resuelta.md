---
unidad: 4
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 04

::practica{titulo="Análisis estadístico defendible del dataset escolar"}
**Problema.** Producir reporte estadístico que respalde la decisión "qué variables predicen el rendimiento final". Reporte para consejo en 1 página.

**Paso 1 — Estrategia.** Aplicar las 6 técnicas: descriptivos, percentiles, correlaciones, distinguir causalidad, outliers.

**Paso 2 — Código.**

```python
import pandas as pd
import numpy as np

df = pd.read_csv("dataset_escolar_limpio.csv")

# 1. Descriptivos
print(df[["horas_estudio", "asistencia", "cal_anterior", "cal_final"]].describe())

# 2. Por materia
print(df.groupby("materia")["cal_final"].agg(["mean", "median", "std"]).round(2))

# 3. Percentiles clave
print("Percentiles cal_final:")
print(df["cal_final"].quantile([0.10, 0.25, 0.50, 0.75, 0.90]))

# 4. Correlaciones
corr = df[["horas_estudio", "asistencia", "cal_anterior", "cal_final"]].corr()
print("Matriz correlaciones:")
print(corr.round(3))

# 5. Outliers IQR
Q1, Q3 = df["cal_final"].quantile([0.25, 0.75])
IQR = Q3 - Q1
outliers = df[(df["cal_final"] < Q1 - 1.5*IQR) | (df["cal_final"] > Q3 + 1.5*IQR)]
print(f"Outliers detectados: {len(outliers)}")

# 6. Reporte ejecutivo
print(f"""
RESUMEN EJECUTIVO

n = {len(df)} estudiantes
Calificación final: media {df['cal_final'].mean():.2f} (mediana {df['cal_final'].median():.2f}, σ={df['cal_final'].std():.2f})
Tasa de aprobación: {(df['cal_final']>=6).mean()*100:.1f}%

Predictores ordenados por correlación con cal_final:
1. cal_anterior  r = {corr.loc['cal_anterior','cal_final']:.3f}  (muy fuerte)
2. asistencia    r = {corr.loc['asistencia','cal_final']:.3f}    (fuerte)
3. horas_estudio r = {corr.loc['horas_estudio','cal_final']:.3f} (moderada)

Outliers: {len(outliers)} estudiantes ({len(outliers)/len(df)*100:.1f}%) requieren atención individual.

⚠ Importante: estas son CORRELACIONES, no causalidades. 
   Para afirmar causalidad se requiere experimento controlado.
""")
```

**Paso 3 — Output ejecutivo.**

```
RESUMEN EJECUTIVO

n = 470 estudiantes
Calificación final: media 7.42 (mediana 7.50, σ=1.49)
Tasa de aprobación: 81.2%

Predictores ordenados por correlación con cal_final:
1. cal_anterior  r = 0.722  (muy fuerte)
2. asistencia    r = 0.554  (fuerte)
3. horas_estudio r = 0.418  (moderada)

Outliers: 7 estudiantes (1.5%) requieren atención individual.

⚠ Importante: estas son CORRELACIONES, no causalidades.
   Para afirmar causalidad se requiere experimento controlado.
```

**Paso 4 — Recomendaciones derivables.**
1. Calificación anterior es el predictor más fuerte (r²=0.52, explica 52% de la varianza).
2. Asistencia es segundo predictor con poder real (r²=0.31).
3. Horas de estudio tiene correlación moderada — relevante pero no determinante por sí sola.
4. 7 outliers concentran riesgo o casos excepcionales — atención individual.
5. **No afirmamos** que más asistencia "cause" mejores notas; afirmamos que correlacionan fuertemente.

**Paso 5 — Verificación.** Comparte con un compañero estadísticamente entrenado. Si encuentra una afirmación causal sin experimento, corrige.

**Respuesta.** Reporte de 1 página, defendible, con números y advertencias éticas. Tiempo: 2 horas con datos limpios.

**Lección.** Las 6 técnicas no se usan en aislado: se combinan para construir argumento. Lo poderoso no es Pearson solo, ni outliers solo: es la integración bajo un mensaje coherente y honesto sobre limitaciones.
::/practica

---

## Práctica resuelta 2 — Test de normalidad y QQ-plot

::practica{titulo="Verifica visual y numéricamente si cal_final es normal"}
**Problema.** Antes de aplicar técnicas que **asumen normalidad** (regresión lineal, intervalos de confianza paramétricos), confirma si tu variable lo es.

**Paso 1 — Estrategia.** Tres herramientas complementarias: histograma + KDE, QQ-plot, test de Shapiro-Wilk.

**Paso 2 — Código.**

```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset_escolar_limpio.csv")
cal = df["cal_final"]

# Stats descriptivos
print(f"n = {len(cal)}")
print(f"Media: {cal.mean():.2f}, Mediana: {cal.median():.2f}, Std: {cal.std():.2f}")
print(f"Skew: {stats.skew(cal):.3f}  (0 = simétrica, neg = cola izq)")
print(f"Kurtosis: {stats.kurtosis(cal):.3f}  (0 = mesokúrtica)")

# Test Shapiro-Wilk (válido n < 5000)
muestra = cal.sample(min(len(cal), 5000), random_state=42)
W, p = stats.shapiro(muestra)
print(f"\nShapiro-Wilk · W={W:.4f}, p={p:.4g}")
if p < 0.05:
    print("Rechazamos normalidad (p < 0.05).")
else:
    print("No rechazamos normalidad (p ≥ 0.05).")

# Visualización dual
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Histograma + KDE + curva normal teórica
sns.histplot(cal, bins=25, kde=True, stat="density", ax=axes[0],
             color="#0E3A8A")
xs = np.linspace(cal.min(), cal.max(), 200)
axes[0].plot(xs, stats.norm.pdf(xs, cal.mean(), cal.std()),
             color="red", linestyle="--", label="Normal teórica")
axes[0].set_title("Histograma vs normal")
axes[0].legend()

# QQ-plot
stats.probplot(cal, dist="norm", plot=axes[1])
axes[1].set_title("QQ-plot vs normal")

plt.tight_layout()
plt.savefig("normalidad.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Paso 3 — Output esperado.**
```
n = 465
Media: 7.42, Mediana: 7.50, Std: 1.49
Skew: -0.234
Kurtosis: -0.187
Shapiro-Wilk · W=0.987, p=0.0042
Rechazamos normalidad (p < 0.05).
```

**Paso 4 — Interpretación.**
- **Skew −0.23**: ligera cola izquierda (cola de "alumnos en riesgo").
- **Kurtosis −0.19**: ligeramente más plana que normal.
- **Shapiro p<0.05**: rechazamos normalidad estricta. Pero con n=465, Shapiro detecta desviaciones mínimas; el QQ-plot muestra que la cola izquierda se desvía un poco, el resto sigue la diagonal razonablemente.

**Paso 5 — Decisión práctica.**
- Para regresión lineal: la normalidad estricta de la variable target NO es requerida (lo es la de los **residuos**). Procede con cuidado.
- Para intervalos de confianza paramétricos: con n=465 el TLC suele rescatarte. Confianza moderada.
- Para detectar outliers: prefiere IQR (no asume normalidad) sobre z-score.

**Paso 6 — Verificación.** Repite el test segmentando por materia. Es común que **sub-distribuciones** sean más normales que la global mezclada.

**Lección.** "Normal" es un ideal matemático; los datos reales **rara vez lo son perfectamente**. Pero para n ≥ 30, muchas técnicas siguen siendo válidas por el TLC. Reportar Shapiro + QQ-plot le dice a tu lector "miré, no asumo".
::/practica

---

## Práctica resuelta 3 — Bootstrap para intervalos de confianza

::practica{titulo="IC al 95% sin asumir normalidad: bootstrap manual"}
**Problema.** Reportar la calificación promedio con un intervalo de confianza del 95% **sin asumir normalidad**. Útil cuando el dataset es asimétrico o pequeño.

**Paso 1 — Estrategia.** Bootstrap: re-muestrear con reemplazo 5000 veces, calcular media en cada uno, tomar percentiles 2.5 y 97.5.

**Paso 2 — Código.**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_escolar_limpio.csv")
cal = df["cal_final"].values

def bootstrap_ic(datos, estimador=np.mean, n_iter=5000, alpha=0.05, seed=42):
    """Devuelve estimación puntual e IC con percentiles."""
    rng = np.random.default_rng(seed)
    estimaciones = np.empty(n_iter)
    n = len(datos)
    for i in range(n_iter):
        muestra = rng.choice(datos, size=n, replace=True)
        estimaciones[i] = estimador(muestra)
    punto = estimador(datos)
    lo = np.percentile(estimaciones, 100 * alpha / 2)
    hi = np.percentile(estimaciones, 100 * (1 - alpha / 2))
    return punto, lo, hi, estimaciones

# Aplicación
media, lo, hi, dist = bootstrap_ic(cal, np.mean, n_iter=5000)
print(f"Media: {media:.3f}")
print(f"IC 95%: [{lo:.3f}, {hi:.3f}]")

# También para mediana
mediana, lo_m, hi_m, _ = bootstrap_ic(cal, np.median, n_iter=5000)
print(f"\nMediana: {mediana:.3f}")
print(f"IC 95%: [{lo_m:.3f}, {hi_m:.3f}]")

# Visualizar la distribución bootstrap
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(dist, bins=50, color="#0E3A8A", alpha=0.7)
ax.axvline(media, color="red", linestyle="-", label=f"Media={media:.2f}")
ax.axvline(lo, color="orange", linestyle="--", label=f"IC95%=[{lo:.2f}, {hi:.2f}]")
ax.axvline(hi, color="orange", linestyle="--")
ax.set_title("Distribución bootstrap de la media · 5000 iteraciones",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Media de cal_final en cada muestra bootstrap")
ax.set_ylabel("Frecuencia")
ax.legend()
plt.savefig("bootstrap.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Paso 3 — Output esperado.**
```
Media: 7.420
IC 95%: [7.286, 7.554]

Mediana: 7.500
IC 95%: [7.300, 7.600]
```

**Paso 4 — Interpretación.**
- "Estamos 95% seguros de que la media verdadera de la población escolar está entre 7.29 y 7.55."
- El IC de la mediana es ligeramente más estrecho aquí (la mediana es más estable a outliers).
- Si quieres mayor precisión: aumenta n (más datos), no n_iter (más iteraciones).

**Paso 5 — Verificación.** Compara contra el IC paramétrico clásico:

```python
# IC paramétrico (asume normalidad o n grande por TLC)
import scipy.stats as stats
n = len(cal)
sem = cal.std(ddof=1) / np.sqrt(n)
ic_param = stats.t.interval(0.95, df=n-1, loc=cal.mean(), scale=sem)
print(f"IC paramétrico 95%: [{ic_param[0]:.3f}, {ic_param[1]:.3f}]")
```

Con n=465 deberían coincidir bien. Si no coinciden mucho, sospecha distribución muy asimétrica.

**Lección.** Bootstrap es **la herramienta universal** para construir IC sin asumir distribución. Funciona para cualquier estadístico (media, mediana, correlación, percentil, lo que sea). Con 5000 iteraciones y semilla fija, es **reproducible** y **defendible** ante cualquier estadístico clásico.
::/practica
