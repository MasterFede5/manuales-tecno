---
unidad: 6
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 06

::practica{titulo="Segmentación de perfiles + anomalías del dataset escolar"}
**Problema.** Descubrir 4 perfiles de estudiantes con K-Means, visualizar con PCA, identificar 5 % anomalías que requieren atención individual.

**Paso 1 — Estrategia.** Pipeline completo: scaling → elegir K → K-Means → PCA → caracterizar → anomalías → reporte.

**Paso 2 — Código.**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.ensemble import IsolationForest

df = pd.read_csv("dataset_escolar_limpio.csv")
features = ["horas_estudio", "asistencia", "cal_anterior", "cal_final"]
X = df[features]

# 1. Scaling
X_scaled = StandardScaler().fit_transform(X)

# 2. Elegir K (codo + silueta)
inertias, sils = [], []
for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
    sils.append(silhouette_score(X_scaled, km.labels_))

# Visualizar
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].plot(range(2, 11), inertias, marker="o")
axes[0].set_title("Codo")
axes[1].plot(range(2, 11), sils, marker="o", color="orange")
axes[1].set_title("Silueta")
plt.savefig("k_selection.png", dpi=200)

# 3. K=4 (decisión basada en codo + dominio)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(X_scaled)

# 4. Caracterizar perfiles
perfiles = df.groupby("cluster")[features].mean().round(2)
perfiles["n"] = df.groupby("cluster").size()
print("Perfiles de estudiantes:")
print(perfiles)

# 5. Visualizar con PCA
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_2d[:,0], y=X_2d[:,1], hue=df["cluster"], palette="viridis", s=50)
plt.title(f"Perfiles (PCA 2D, {pca.explained_variance_ratio_.sum():.0%} varianza)")
plt.savefig("clusters_pca.png", dpi=200)

# 6. Detectar anomalías
iso = IsolationForest(contamination=0.05, random_state=42)
df["es_anomalia"] = iso.fit_predict(X_scaled) == -1
print(f"\nAnomalías: {df['es_anomalia'].sum()}")
print(df[df['es_anomalia']][features + ["cluster"]].head(10))

# 7. Reporte
print("""
INSIGHTS:
- 4 perfiles naturales identificados.
- Cluster 0 (excelentes, n=110): horas altas, asistencia alta, notas altas.
- Cluster 1 (consistentes, n=180): horas medias, asistencia alta, notas medias-altas.
- Cluster 2 (en riesgo, n=60): horas bajas, asistencia baja, notas bajas.
- Cluster 3 (irregulares, n=120): mezclados, requieren observación individual.
- 24 anomalías para revisión humana caso por caso.
""")
```

**Paso 3 — Output esperado.**
```
Perfiles de estudiantes:
         horas_estudio  asistencia  cal_anterior  cal_final    n
cluster
0                 6.5         0.92          8.5        8.7  110
1                 4.5         0.85          7.0        7.2  180
2                 2.0         0.55          5.0        4.5   60
3                 5.5         0.75          6.5        6.8  120

Anomalías: 24
[lista de alumnos atípicos con sus features]
```

**Paso 4 — Recomendaciones.**
- **Cluster 2 (60 alumnos)**: intervención inmediata (asistencia y refuerzo).
- **Cluster 3 (120)**: observación cercana, programa de tutoría.
- **Cluster 1 (180)**: mantener (mayoría aprueba).
- **Cluster 0 (110)**: programa de excelencia / desafíos extra.
- **24 anomalías**: revisión 1-1 con coordinación.

**Paso 5 — Verificación.** Comparte clusters con coordinadora académica para validar que tienen sentido pedagógico antes de actuar.

**Lección.** Las 5 técnicas se combinan: scaling → elegir K → K-Means → PCA → anomalías. Sin scaling, todo falla; sin elegir K bien, clusters arbitrarios; sin PCA, ciegos; sin anomalías, casos especiales pasan desapercibidos.
::/practica

---

## Práctica resuelta 2 — Comparar K-Means vs DBSCAN sobre el dataset

::practica{titulo="¿Y si los clusters NO son esféricos? Prueba DBSCAN"}
**Problema.** K-Means asume clusters esféricos del mismo tamaño. ¿Y si los grupos reales tienen forma irregular o densidades distintas? **DBSCAN** los encuentra sin asumir forma.

**Paso 1 — Estrategia.** Comparar las dos segmentaciones lado a lado: K-Means (K=4) vs DBSCAN (autoexplora densidades).

**Paso 2 — Código.**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

df = pd.read_csv("dataset_escolar_limpio.csv")
features = ["horas_estudio", "asistencia", "cal_anterior", "cal_final"]
X = df[features]
X_scaled = StandardScaler().fit_transform(X)

# K-Means
km = KMeans(n_clusters=4, random_state=42, n_init=10)
labels_km = km.fit_predict(X_scaled)

# DBSCAN
db = DBSCAN(eps=0.6, min_samples=10)
labels_db = db.fit_predict(X_scaled)

# Comparativa
n_clusters_km = len(set(labels_km))
n_clusters_db = len(set(labels_db)) - (1 if -1 in labels_db else 0)
n_ruido_db = (labels_db == -1).sum()

print(f"K-Means: {n_clusters_km} clusters")
print(f"DBSCAN:  {n_clusters_db} clusters + {n_ruido_db} puntos como ruido")

# Silhouette (ignorando ruido en DBSCAN)
sil_km = silhouette_score(X_scaled, labels_km)
mask_db = labels_db != -1
sil_db = silhouette_score(X_scaled[mask_db], labels_db[mask_db]) if mask_db.sum() > 1 else None
print(f"Silhouette K-Means: {sil_km:.3f}")
print(f"Silhouette DBSCAN: {sil_db:.3f}" if sil_db else "DBSCAN: insuficientes puntos")

# Visualizar lado a lado con PCA
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

scatter1 = axes[0].scatter(X_2d[:, 0], X_2d[:, 1], c=labels_km,
                            cmap="viridis", alpha=0.6, s=40)
axes[0].set_title(f"K-Means · K=4 · sil={sil_km:.2f}")
plt.colorbar(scatter1, ax=axes[0])

scatter2 = axes[1].scatter(X_2d[:, 0], X_2d[:, 1], c=labels_db,
                            cmap="viridis", alpha=0.6, s=40)
axes[1].set_title(f"DBSCAN · {n_clusters_db} clusters + {n_ruido_db} ruido")
plt.colorbar(scatter2, ax=axes[1])

for ax in axes:
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")

plt.tight_layout()
plt.savefig("kmeans_vs_dbscan.png", dpi=200, bbox_inches="tight")
plt.show()
```

**Paso 3 — Output esperado (depende de eps).**
```
K-Means: 4 clusters
DBSCAN:  3 clusters + 28 puntos como ruido
Silhouette K-Means: 0.42
Silhouette DBSCAN: 0.51
```

**Paso 4 — Interpretación comparativa.**

| Aspecto | K-Means | DBSCAN |
|---|---|---|
| K | Lo eliges tú | Se descubre |
| Forma | Esférica | Cualquiera |
| Outliers | Forzados a un cluster | Marcados como ruido (-1) |
| Hiperparámetros | n_clusters | eps + min_samples |
| Dataset escolar (4 features tabular) | Funciona bien (sil 0.42) | Funciona pero requiere tunear eps |

**Paso 5 — Cuándo elegir cuál.**
- **K-Means** para tabular limpio con grupos naturales esféricos. Caso típico de coordinación académica.
- **DBSCAN** cuando sospechas grupos de forma irregular (datos espaciales, secuencias) o cuando los outliers son **el objeto del análisis** (fraude, intrusión).

**Paso 6 — Verificación.** Tunea `eps` con la regla del codo en gráfica de k-distance:

```python
from sklearn.neighbors import NearestNeighbors

nbrs = NearestNeighbors(n_neighbors=10).fit(X_scaled)
distances, _ = nbrs.kneighbors(X_scaled)
k_distances = np.sort(distances[:, -1])
plt.plot(k_distances)
plt.title("Gráfica k-distance para elegir eps")
plt.xlabel("Puntos ordenados")
plt.ylabel("Distancia al 10mo vecino")
plt.savefig("k_distance.png", dpi=200)
```

El "codo" sugiere el eps óptimo. Para nuestro dataset suele estar entre 0.5 y 0.8.

**Lección.** No hay un "mejor algoritmo de clustering universal". Para tabular limpio con grupos balanceados, K-Means es **la primera opción razonable**. Para detectar grupos irregulares o tratar outliers como categoría aparte, DBSCAN. Comparar las dos vistas te da una segunda opinión: si ambas concuerdan en cierto cluster, ese cluster es **muy robusto**.
::/practica

---

## Práctica resuelta 3 — Persistir y aplicar el modelo de clustering a alumnos nuevos

::practica{titulo="Modelo de segmentación que clasifica alumnos nuevos sin re-entrenar"}
**Problema.** Coordinación quiere asignar **automáticamente** un nuevo alumno (que no estaba en el dataset original) al cluster correcto. Solución: persistir scaler + modelo y re-aplicarlos.

**Paso 1 — Estrategia.** Entrenar pipeline (scaler → K-Means) sobre dataset histórico, guardar con joblib, cargar y usar `pipe.predict(nuevo)`.

**Paso 2 — Código entrenamiento (1 vez).**

```python
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline

df = pd.read_csv("dataset_escolar_limpio.csv")
features = ["horas_estudio", "asistencia", "cal_anterior", "cal_final"]
X = df[features]

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("kmeans", KMeans(n_clusters=4, random_state=42, n_init=10))
])
pipe.fit(X)

# Asignar nombres pedagógicos a cada cluster
df["cluster"] = pipe.predict(X)
medias = df.groupby("cluster")[features].mean()
print(medias)

# Suponiendo (basado en medias) la asignación:
nombres = {
    0: "Excelentes",
    1: "Consistentes",
    2: "En riesgo",
    3: "Irregulares"
}
# Importante: el orden depende de la inicialización; verifica antes de fijar.

# Guardar modelo + diccionario de nombres
joblib.dump({"pipeline": pipe, "nombres": nombres},
            "modelo_clustering_v1.pkl")
print("✓ modelo_clustering_v1.pkl guardado")
```

**Paso 3 — Código de aplicación (cada vez que llega un alumno nuevo).**

```python
import joblib
import pandas as pd

artefacto = joblib.load("modelo_clustering_v1.pkl")
pipe = artefacto["pipeline"]
nombres = artefacto["nombres"]

# Nuevo alumno
nuevo = pd.DataFrame([{
    "horas_estudio": 3.0,
    "asistencia": 0.65,
    "cal_anterior": 5.5,
    "cal_final": 5.8
}])

cluster_id = int(pipe.predict(nuevo)[0])
nombre = nombres[cluster_id]

# Distancia al centroide (qué tan típico es del cluster)
import numpy as np
from sklearn.metrics import pairwise_distances_argmin_min
nuevo_scaled = pipe.named_steps["scaler"].transform(nuevo)
centroides = pipe.named_steps["kmeans"].cluster_centers_
_, distancias = pairwise_distances_argmin_min(nuevo_scaled, centroides)
distancia = float(distancias[0])

print(f"Alumno asignado a cluster {cluster_id}: {nombre}")
print(f"Distancia al centroide: {distancia:.2f}")
if distancia > 2.0:
    print("⚠ Alumno atípico: revisar manualmente.")
```

**Paso 4 — Output esperado.**
```
Alumno asignado a cluster 2: En riesgo
Distancia al centroide: 1.34
```

**Paso 5 — Verificación.** Aplica `pipe.predict()` a 5 alumnos de coordinación, verifica que los del cluster "Excelentes" tienen `cal_anterior` y asistencia altas y los del cluster "En riesgo" tienen ambas bajas. Si no, sospecha que el orden de los clusters cambió en re-fit (los IDs son **arbitrarios**, no semánticos).

**Paso 6 — Re-entrenamiento periódico.** Cada bimestre re-entrena con nuevos datos y **re-mapea** los IDs a nombres con base en las medias. Automatiza:

```python
def asignar_nombres(centroides_originales, features):
    """Mapea clusters por nivel de cal_final del centroide."""
    medias = centroides_originales[:, features.index("cal_final")]
    orden = np.argsort(medias)[::-1]   # mayor a menor
    nombres_ordenados = ["Excelentes", "Consistentes", "Irregulares", "En riesgo"]
    return {orden[i]: nombres_ordenados[i] for i in range(len(orden))}
```

**Lección.** Persistir un pipeline (scaler + modelo + diccionario de nombres) hace tu segmentación **operativa**: coordinación clasifica un nuevo alumno con 3 líneas sin re-entrenar. La distancia al centroide te da un termómetro de "qué tan típico" — útil para casos atípicos que merecen revisión humana.
::/practica
