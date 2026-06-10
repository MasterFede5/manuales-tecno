---
unidad: 6
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 06

::act-mcq{titulo="Repaso conceptual"}
1. K-Means es:
   - [ ] Supervisado
   - [x] No supervisado
   - [ ] Refuerzo
   - [ ] Híbrido

2. Antes de K-Means es **obligatorio**:
   - [ ] Eliminar duplicados
   - [x] Hacer scaling de features
   - [ ] Train/test split
   - [ ] Convertir a tipos enteros

3. Para elegir K, una combinación poderosa es:
   - [x] Codo + silueta + dominio
   - [ ] Solo el método del codo
   - [ ] K=3 siempre
   - [ ] PCA primero

4. PCA reduce dimensiones preservando:
   - [ ] La variable target
   - [x] La mayor varianza posible
   - [ ] Los duplicados
   - [ ] El orden temporal

5. Detección de anomalías es útil para:
   - [ ] Eliminar features
   - [x] Identificar puntos que merecen revisión humana
   - [ ] Acelerar K-Means
   - [ ] Reducir overfitting
::/act-mcq

::act-table{titulo="Algoritmo según caso"}
| Caso | Algoritmo | Justificación |
|---|---|---|
| Segmentar 4 perfiles esféricos |  |  |
| Reducir 100 features a 10 |  |  |
| Detectar fraude (5% de casos) |  |  |
| Clusters de forma irregular |  |  |
::/act-table

::act-match{titulo="Relaciona técnica con uso"}
| Técnica | Uso |
|---|---|
| 1. K-Means | a) Reducir dimensionalidad |
| 2. PCA | b) Encontrar K clusters esféricos |
| 3. Isolation Forest | c) Detectar anomalías |
| 4. Silueta | d) Validar calidad de clustering |
| 5. StandardScaler | e) Normalizar features |
::/act-match

::act-tf{titulo="V/F"}
1. PCA preserva la información de cada feature original. ( ) ____________________________________________

2. K-Means siempre encuentra el número óptimo de clusters automáticamente. ( ) ____________________________________________

3. Anomalías deben siempre eliminarse del dataset. ( ) ____________________________________________

4. Sin scaling, K-Means da resultados sesgados por la feature de mayor magnitud. ( ) ____________________________________________

5. Cluster es lo mismo que clase en clasificación supervisada. ( ) ____________________________________________
::/act-tf

::albatros{titulo="Segmenta perfiles + detecta anomalías de tu dataset escolar" tipo="taller" tiempo="3 h"}
**Pregunta.** Si descubrieras 5 perfiles distintos de alumnos, ¿qué intervención propondrías para cada uno?

**Lo que harás.**
- Aplica el pipeline completo de la práctica.
- Determina K con codo, silueta y tu juicio del dominio.
- Caracteriza cada cluster usando una tabla.
- Visualiza los resultados aplicando PCA.
- Detecta el 5% de anomalías.
- Documenta 5 perfiles y 5 anomalías con sugerencias de intervención.
- Comparte los resultados con el coordinador para validarlos.

::interioriza
Piensa en los clusters como las casas de Hogwarts: el algoritmo es el Sombrero Seleccionador que agrupa según características clave.
::/interioriza

::pausa{}
¿Por qué es vital validar los clusters con alguien experto en el dominio?
::/pausa

**Entregable.** Notebook + reporte 1-2 pp + visualizaciones.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Scaling | sin | con | + verificación |
| K elegido | arbitrario | con codo | + silueta + dominio |
| Caracterización | un par | tabla | + nombres pedagógicos |
| Anomalías | sin detectar | detectadas | + revisadas individualmente |
::/albatros

---

## Actividades adicionales (expansión práctica)

::act-fill{titulo="Pipeline K-Means con scaling integrado"}
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

pipe = ___________([
    ("scaler", StandardScaler()),
    ("kmeans", KMeans(n_clusters=4, random_state=42, n_init=___________))
])

labels = pipe.fit_predict(X)
df["cluster"] = ___________
```
::/act-fill

::act-order{titulo="Pasos para una segmentación profesional"}
[ ] Visualizar con PCA
[ ] Caracterizar centroides en escala original
[ ] Detectar anomalías post-clustering
[ ] Cargar y limpiar datos
[ ] Scaling de features
[ ] Elegir K con codo + silueta + dominio
[ ] Validar nombres de cluster con coordinador académico
::/act-order

::act-case{titulo="Caso — clusters inestables entre corridas" lineas=10}
- Tu compañero corre K-Means con `random_state=42` y obtiene clusters {A, B, C, D}.
- Tú lo corres con `random_state=7` y obtienes {A', B', C', D'}.
- Las composiciones cambian: 30% de los alumnos caen en clusters distintos.

::interioriza
Cambiar el `random_state` en K-Means es como tirar semillas al viento desde distintos puntos; dependiendo de dónde caigan inicialmente, los grupos finales cambiarán.
::/interioriza

**Pregunta.**
1. ¿Por qué pasa esto?
2. ¿Significa que tus clusters son "falsos"?
3. Da 3 estrategias para validar la robustez de los clusters.
::/act-case

::act-table{titulo="Algoritmo de clustering según escenario"}
| Escenario | Algoritmo | Por qué |
|---|---|---|
| Clusters esféricos, K conocido |  |  |
| Clusters de forma irregular |  |  |
| Quieres jerarquía de grupos |  |  |
| Datos con muchas anomalías |  |  |
| Alta dimensionalidad (~100 features) |  |  |
::/act-table

::act-mindmap{titulo="Mapa mental abierto" centro="APRENDIZAJE NO SUPERVISADO" nodos_primarios=5 nodos_secundarios=10}
5 nodos: clustering, reducción de dimensionalidad, anomalías, validación, aplicaciones. 2 ejemplos por cada uno.
::/act-mindmap

::albatros{titulo="Reto Albatros — segmentación + experimento de intervención" tipo="reto" tiempo="60 min"}
**Pregunta detonadora.** ¿Puedes diseñar un experimento que **valide pedagógicamente** los clusters que tu modelo encontró matemáticamente?

**Lo que harás.**
- Genera 4 clusters con K-Means sobre el dataset escolar.
- Identifica el cluster "en riesgo" (con la calificación final más baja).
- Diseña un experimento controlado.
  - **Hipótesis:** "El cluster en riesgo mejorará 0.5 puntos con la intervención X".
  - **Grupos:** Tratamiento y control dentro del mismo cluster.
  - **Tamaño muestral:** Para detectar el efecto (poder 0.8).
  - **Métricas:** Define métricas de éxito y plazos.
- Considera la ética: ¿es justo dar intervención solo a la mitad?
- Documenta el protocolo y diseño.

::pausa{}
¿Qué sesgos podrían introducirse al seleccionar a los alumnos del grupo de tratamiento?
::/pausa

**Entregable.** Documento de 2 páginas con: clusters identificados + protocolo experimental + cálculo de tamaño muestral + consideraciones éticas + plan de medición.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Clusters generados | sin | con K-Means | + caracterizados |
| Hipótesis | vaga | clara | testable y específica |
| Diseño experimental | sin grupos | con grupos | aleatorización + control |
| Ética considerada | no | mencionada | propuesta de mitigación |
| Métricas | sin | una | múltiples con plazos |
::/albatros
