---
unidad: 6
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 06

::practica{titulo="Segmentación de perfiles + anomalías del dataset escolar"}
**Problema.** 
- Descubrir 4 perfiles de estudiantes con K-Means.
- Visualizar con PCA.
- Identificar 5 % anomalías para atención individual.

**Paso 1 — Estrategia.** 
- **Pipeline:** scaling → elegir K → K-Means → PCA → caracterizar → anomalías → reporte.

::interioriza
**Analogía:** Imagina organizar a tus alumnos en mesas (K-Means). 
Si no ajustas las estaturas primero (Scaling), los más altos opacarán al resto. 
PCA es como tomarles una foto de grupo desde el mejor ángulo posible.
::/interioriza

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
```text
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
- **Cluster 0 (110)**: excelencia / desafíos extra.
- **Cluster 1 (180)**: mantener el ritmo.
- **Cluster 2 (60 alumnos)**: intervención inmediata.
- **Cluster 3 (120)**: tutoría y observación.
- **24 anomalías**: revisión 1-1.

**Paso 5 — Verificación.**
- Comparte los resultados con coordinación académica.
- Valida el sentido pedagógico de cada grupo antes de actuar.

::pausa{tipo="deduccion"}
**Deducción Lógica:** Si te saltas el paso de "scaling", ¿qué feature dominará el clustering y por qué?
*Respuesta:* Las calificaciones, por tener mayor rango numérico que la asistencia (0 a 1).
::/pausa

**Lección.** 
- Las 5 técnicas se complementan entre sí.
- Sin scaling = resultados distorsionados. 
- Sin K correcto = grupos arbitrarios. 
- Sin PCA = ceguera visual. 
- Sin detección = casos críticos ignorados.
::/practica

---

## Práctica resuelta 2 — Comparar K-Means vs DBSCAN sobre el dataset

::practica{titulo="¿Y si los clusters NO son esféricos? Prueba DBSCAN"}
**Problema.** 
- K-Means asume clusters esféricos.
- DBSCAN encuentra grupos de forma irregular o densidades distintas sin asumir forma.

**Paso 1 — Estrategia.** 
- Comparar segmentaciones: K-Means (K=4) vs DBSCAN (autoexploración).

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
```text
K-Means: 4 clusters
DBSCAN:  3 clusters + 28 puntos como ruido
Silhouette K-Means: 0.42
Silhouette DBSCAN: 0.51
```

**Paso 4 — Interpretación comparativa.**

| Aspecto | K-Means | DBSCAN |
|---|---|---|
| K | Se elige a mano | Se descubre solo |
| Forma | Esférica | Cualquiera |
| Outliers | Forzados al cluster | Aislados como ruido (-1) |
| Hiperparámetros | n_clusters | eps + min_samples |

**Paso 5 — Cuándo elegir cuál.**
- **K-Means:** Tabular limpio con grupos naturales esféricos.
- **DBSCAN:** Grupos de forma irregular o enfoque directo en anomalías.

::interioriza
**Analogía:** K-Means reparte una pizza en porciones iguales cueste lo que cueste.
DBSCAN sigue el queso derretido por donde fluya, y si hay un trozo caído, lo ignora (ruido).
::/interioriza

**Paso 6 — Verificación.** 
- Afina `eps` con la gráfica de k-distance:

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
- El "codo" suele sugerir el eps óptimo (entre 0.5 y 0.8 aquí).

::pausa{tipo="deduccion"}
**Deducción Lógica:** Si DBSCAN te dice que todo el dataset es ruido, ¿qué parámetro debes cambiar?
*Respuesta:* Aumentar `eps` (para abarcar más distancia) o reducir `min_samples` (para exigir menos vecinos).
::/pausa

**Lección.** 
- No existe un "algoritmo universal".
- Compara ambas vistas. Si coinciden en un cluster, es una agrupación robusta.
::/practica

---

## Práctica resuelta 3 — Persistir y aplicar el modelo de clustering a alumnos nuevos

::practica{titulo="Modelo de segmentación que clasifica alumnos nuevos sin re-entrenar"}
**Problema.** 
- Se necesita clasificar alumnos nuevos automáticamente.
- Solución: Persistir scaler y modelo (joblib) para reaplicarlos.

**Paso 1 — Estrategia.** 
- Entrenar pipeline (scaler → K-Means).
- Guardar el artefacto y reutilizar con `predict(nuevo)`.

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

# Nombres basados en medias
nombres = {
    0: "Excelentes",
    1: "Consistentes",
    2: "En riesgo",
    3: "Irregulares"
}

# Guardar modelo
joblib.dump({"pipeline": pipe, "nombres": nombres}, "modelo_clustering_v1.pkl")
print("✓ modelo_clustering_v1.pkl guardado")
```

**Paso 3 — Código de aplicación.**

```python
import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances_argmin_min

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

# Distancia al centroide
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
```text
Alumno asignado a cluster 2: En riesgo
Distancia al centroide: 1.34
```

**Paso 5 — Verificación.** 
- Prueba el pipeline con alumnos históricos conocidos.
- Los "Excelentes" deben coincidir siempre en su evaluación.

**Paso 6 — Re-entrenamiento periódico.** 
- Re-entrena bimestralmente.
- Re-mapea IDs a nombres usando el orden de las medias.

```python
def asignar_nombres(centroides_originales, features):
    """Mapea clusters por nivel de cal_final del centroide."""
    medias = centroides_originales[:, features.index("cal_final")]
    orden = np.argsort(medias)[::-1]
    nombres_ordenados = ["Excelentes", "Consistentes", "Irregulares", "En riesgo"]
    return {orden[i]: nombres_ordenados[i] for i in range(len(orden))}
```

::interioriza
**Analogía:** Guardar el modelo es como hacer un molde de galletas (entrenamiento). 
Cuando llega masa nueva (alumno nuevo), solo aplicas el molde, sin volver a fabricarlo.
::/interioriza

::pausa{tipo="deduccion"}
**Deducción Lógica:** Si el orden de los IDs en K-Means es aleatorio en cada ejecución, ¿qué pasará si no guardas el diccionario de nombres?
*Respuesta:* El cluster 0 que antes era "En riesgo" ahora podría ser "Excelentes", confundiendo todo el diagnóstico.
::/pausa

**Lección.** 
- Persistir el pipeline vuelve operativa tu analítica.
- La distancia al centroide sirve como "termómetro de normalidad".
::/practica
