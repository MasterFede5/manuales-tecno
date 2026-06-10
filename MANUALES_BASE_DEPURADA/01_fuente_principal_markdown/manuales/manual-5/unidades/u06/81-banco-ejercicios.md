---
unidad: 6
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 06

> Practica clustering, PCA y detección de anomalías.
> Cada bloque conecta con el caso de rendimiento escolar.

::interioriza
Agrupar alumnos por rendimiento (clustering) es como organizar un armario sin etiquetas previas:
- Clasificación: poner la ropa en cajones ya definidos (pantalón, camisa).
- Clustering: juntar las prendas que se parecen entre sí sobre la cama, para ver qué grupos naturales se forman.
::/interioriza

::pausa{}
**Reflexiona antes de empezar:**
- ¿Por qué en clustering no tenemos una variable objetivo (Y)?
- ¿Qué pasaría con la distancia si medimos "horas" (0-10) e "ingresos" (0-100k) sin escalar?
::/pausa

### Bloque A — Concepto clustering (6.1)

::act-mcq{titulo="Conceptos de clustering"}
1. K-Means es:
   - [ ] Supervisado clasificación
   - [x] No supervisado clustering
   - [ ] Refuerzo
   - [ ] Híbrido

2. La diferencia clave entre clasificación y clustering:
   - [ ] Clasificación es más rápida
   - [x] Clasificación tiene etiquetas conocidas, clustering no
   - [ ] Clustering siempre es mejor
   - [ ] Solo el dataset cambia

3. ¿Cuál NO es algoritmo de clustering?
   - [ ] K-Means
   - [ ] DBSCAN
   - [x] Random Forest
   - [ ] Hierarchical
::/act-mcq

::act-fill{titulo="Setup K-Means básico"}
```python
from sklearn.cluster import ___________
from sklearn.preprocessing import StandardScaler

X = df[["horas_estudio", "asistencia", "cal_anterior", "cal_final"]]
X_scaled = StandardScaler().___________(X)

km = KMeans(n_clusters=___________, random_state=42, n_init=10)
labels = km.fit_predict(X_scaled)

df["cluster"] = ___________
print(df["cluster"].value_counts())
```
::/act-fill

### Bloque B — K-Means paso a paso (6.2)

::act-order{titulo="Pasos del algoritmo K-Means"}
[ ] Reasignar cada punto al centroide más cercano
[ ] Repetir hasta que los centroides no cambien
[ ] Recalcular centroides como media de cada cluster
[ ] Inicializar K centroides aleatorios (o k-means++)
[ ] Asignar cada punto al centroide más cercano
::/act-order

::act-mcq{titulo="K-Means en detalle"}
1. ¿Por qué es **obligatorio** hacer scaling antes de K-Means?
   - [ ] Acelera el algoritmo
   - [x] La distancia euclidiana se sesga por features de mayor magnitud
   - [ ] Sklearn lo exige
   - [ ] No es obligatorio

2. ¿Qué hace `n_init=10`?
   - [ ] Entrena 10 modelos
   - [x] Reinicia con 10 semillas distintas y elige la mejor inercia
   - [ ] 10 iteraciones máximas
   - [ ] 10 epochs

3. La inercia (`km.inertia_`) es:
   - [ ] El número de iteraciones
   - [x] Suma de distancias al cuadrado de cada punto a su centroide
   - [ ] El K elegido
   - [ ] La accuracy
::/act-mcq

### Bloque C — Elegir K (6.3)

::act-mcq{titulo="Elección de K"}
1. El método del codo busca:
   - [ ] El K que minimiza inercia (más alto posible)
   - [x] El K donde la mejora marginal en inercia "se aplana"
   - [ ] El K que maximiza accuracy
   - [ ] Siempre K=3

2. Silhouette score se interpreta:
   - [ ] Solo válido si K=2
   - [x] Cerca de +1 = clusters bien separados; cerca de 0 = solapados
   - [ ] En porcentaje
   - [ ] Solo con datos normalizados

3. Si codo dice K=4 y silueta dice K=6, decides:
   - [ ] Siempre el codo
   - [ ] Siempre la silueta
   - [x] Considerar dominio + interpretabilidad
   - [ ] Promediar (5)
::/act-mcq

::act-fill{titulo="Codo + silueta"}
```python
from sklearn.metrics import silhouette_score

inertias, sils = [], []
for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.___________)
    sils.append(silhouette_score(X_scaled, km.___________))

# K óptimo por silueta:
mejor_k_sil = range(2, 11)[___________(sils)]
print(f"K por silueta: {mejor_k_sil}")
```
::/act-fill

### Bloque D — PCA (6.4)

::act-mcq{titulo="PCA"}
1. PCA reduce dimensiones preservando:
   - [ ] La variable target
   - [x] La mayor varianza posible
   - [ ] El orden temporal
   - [ ] Los duplicados

2. `pca.explained_variance_ratio_` te dice:
   - [ ] La accuracy del modelo
   - [x] Qué % de varianza captura cada componente
   - [ ] El K óptimo
   - [ ] La inercia
::/act-mcq

::act-fill{titulo="PCA 2D para visualizar clusters"}
```python
from sklearn.decomposition import ___________

pca = PCA(n_components=___________)
X_2d = pca.fit_transform(X_scaled)

print(f"Varianza explicada: {pca.___________.sum():.2%}")

# Plot
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_2d[:, 0], y=X_2d[:, 1], hue=df["cluster"], palette="viridis")
plt.title(f"Clusters en 2D (PCA, {pca.___________.sum():.0%} varianza)")
plt.savefig("clusters_2d.png", dpi=200)
```
::/act-fill

### Bloque E — Detección de anomalías (6.5)

::act-mcq{titulo="Anomalías"}
1. `IsolationForest(contamination=0.05)` significa:
   - [ ] Acepta 5% de error
   - [x] Espera ~5% de los datos como anomalías
   - [ ] Solo funciona con 5 features
   - [ ] Velocidad 5x

2. Una anomalía detectada se interpreta:
   - [ ] Eliminar siempre
   - [x] Revisar caso por caso (puede ser ruido o señal valiosa)
   - [ ] Cambiar el algoritmo
   - [ ] Es un bug del modelo

3. ¿Por qué Isolation Forest es eficiente para alta dimensionalidad?
   - [ ] Usa GPU
   - [x] Aísla anomalías con árboles cortos (pocos splits)
   - [ ] No requiere scaling
   - [ ] Es lineal en N
::/act-mcq

::act-fill{titulo="Isolation Forest"}
```python
from sklearn.ensemble import ___________

iso = IsolationForest(contamination=___________, random_state=42)
df["es_anomalia"] = iso.fit_predict(X_scaled) == ___________   # -1 = anomalía

print(f"Anomalías: {df['es_anomalia'].sum()}")
print(df[df["es_anomalia"]][features + ["cluster"]].head(5))
```
::/act-fill

### Bloque F — Caso integrador

::act-table{titulo="Caracteriza 4 perfiles del case escolar"}
Recibes los centroides en escala original. Llena el nombre pedagógico y la intervención.

| Cluster | horas | asis | cal_ant | cal_fin | n | Nombre pedagógico | Intervención propuesta |
|---|---|---|---|---|---|---|---|
| 0 | 6.5 | 0.92 | 8.5 | 8.7 | 110 |  |  |
| 1 | 4.5 | 0.85 | 7.0 | 7.2 | 180 |  |  |
| 2 | 2.0 | 0.55 | 5.0 | 4.5 | 60 |  |  |
| 3 | 5.5 | 0.75 | 6.5 | 6.8 | 120 |  |  |
::/act-table

::act-tf{titulo="V/F clustering"}
1. K-Means asume clusters esféricos en el espacio de features. ( ) ____________________
2. Sin scaling, K-Means funciona bien igualmente. ( ) ____________________
3. PCA puede preservar 100% de la varianza si no reduces dimensiones. ( ) ____________________
4. Cluster es lo mismo que clase supervisada. ( ) ____________________
5. Anomalía siempre = mala calidad de dato. ( ) ____________________
::/act-tf

::act-case{titulo="Caso — defender 4 clusters al consejo" lineas=10}
Tu segmentación dio 4 clusters: excelentes (110), consistentes (180), en riesgo (60), irregulares (120). El consejo pregunta:

1. "¿Por qué 4 y no 3 o 5?" — defiende con codo + silueta + dominio.
2. "¿Cómo sé que estos clusters son **reales** y no patrones aleatorios?" — propón validación.
3. "¿Estos 60 alumnos en riesgo son **siempre los mismos** o cambian cada bimestre?" — propón experimento.

Redacta respuestas en 3-5 líneas cada una.
::/act-case

---

## Clave de respuestas

**Bloque A.** 1·B, 2·B, 3·C.
- `act-fill`: `KMeans`, `fit_transform(X)`, `n_clusters=4`, `df["cluster"] = labels`.

**Bloque B.**
- `act-order`: 4·5·3·1·2 (init → asignar → recalcular → reasignar → repetir).
- `act-mcq`: 1·B, 2·B, 3·B.

**Bloque C.**
- `act-mcq`: 1·B, 2·B, 3·C.
- `act-fill`: `km.inertia_`, `km.labels_`, `np.argmax(sils)`.

**Bloque D.**
- `act-mcq`: 1·B, 2·B.
- `act-fill`: `PCA`, `n_components=2`, `explained_variance_ratio_`, `explained_variance_ratio_`.

**Bloque E.**
- `act-mcq`: 1·B, 2·B, 3·B.
- `act-fill`: `IsolationForest`, `contamination=0.05`, `== -1`.

**Bloque F.**
- `act-table`: respuesta sugerida:

| Cluster | Nombre | Intervención |
|---|---|---|
| 0 | Excelentes | Programa de excelencia, retos extra |
| 1 | Consistentes | Mantener; tutoría preventiva |
| 2 | En riesgo | Intervención inmediata, asistencia + refuerzo |
| 3 | Irregulares | Observación cercana, plan personalizado |

- `act-tf`: 1·V; 2·F; 3·V (con n_components=n_features); 4·F; 5·F.
- `act-case`: respuesta modelo:
  - **(1)** K=4 fue donde el codo se aplanó y silueta dio 0.42. Los perfiles tienen sentido pedagógico.
  - **(2)** Validar re-corriendo con `random_state` distintos. Si son robustos, las composiciones cambian poco. Comparar contra K=3 y K=5.
  - **(3)** Re-correr clustering bimestre a bimestre. Si <20% migran, son estables; si >50%, son volátiles.

> **Cierre.** El clustering no devuelve verdades absolutas.
> Devuelve **hipótesis estructurales** que debes validar con conocimiento de dominio y tiempo.
