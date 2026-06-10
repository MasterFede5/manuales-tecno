---
unidad: 6
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Segmentación + recomendaciones de intervención"}
**Objetivo.** Producir segmentación profesional del dataset escolar con K-Means + PCA + anomalías, y traducir hallazgos en **plan de intervención de 4 perfiles** validado por coordinación académica.

**Materiales.** Dataset limpio, scikit-learn, 5-6 horas.

**Pasos.**
1. Pipeline K-Means con codo + silueta (1.5 h).
2. Caracterizar 4 clusters con tabla y nombres pedagógicos (1 h).
3. Visualizar con PCA (30 min).
4. Detectar anomalías con Isolation Forest (1 h).
5. Reporte de plan de intervención por perfil (1 h).
6. Validación con coordinadora académica (30 min).
7. Publicar en repo Git (30 min).

**Entregable.**
- Notebook completo.
- Reporte 2 pp con perfiles y recomendaciones.
- Visualizaciones PNG.
- Lista de anomalías con sugerencia individual.
- Acta de validación con coordinación.

**Rúbrica.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Pipeline | sin scaling | con scaling | + codo + silueta |
| Clusters | sin nombres | nombrados | nombres + caracterización |
| PCA | sin visualizar | con scatter | + interpretación |
| Anomalías | sin detectar | detectadas | analizadas individualmente |
| Plan intervención | genérico | por cluster | + validado dominio |

**Próximo paso.** En **U7** vas a mejorar el predictor de U5 con **redes neuronales** simples en PyTorch.

### Hitos intermedios

| Hito | Tag git | Criterio de cierre |
|---|---|---|
| H1 | `u6-h1-scaling` | StandardScaler aplicado y verificado |
| H2 | `u6-h2-codo` | Gráfica codo + silueta para K=2..10 |
| H3 | `u6-h3-kmeans` | K=4 entrenado, labels asignadas al df |
| H4 | `u6-h4-pca` | Visualización PCA 2D con clusters coloreados |
| H5 | `u6-h5-anomalias` | Isolation Forest detecta ~5% como anomalías |
| H6 | `u6-h6-pipeline-pkl` | Pipeline persistido y reaplicable a nuevos alumnos |

### Reto bonus extendido (3 retos)

**Reto bonus 1 — Comparar K-Means vs Hierarchical (linkage).** Ejecuta `AgglomerativeClustering` con 4 clusters y compara composiciones. ¿Cuántos alumnos coinciden de cluster en ambos? Esfuerzo: 60 min.

```python
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=4, linkage="ward")
labels_hc = hc.fit_predict(X_scaled)
```

**Reto bonus 2 — t-SNE o UMAP para visualización mejorada.** Reemplaza PCA con t-SNE (mejor preservación de estructura local) y compara si los clusters se separan más. Esfuerzo: 60 min.

**Reto bonus 3 — Estabilidad de clusters con bootstrap.** Re-corre K-Means 50 veces con bootstrap del dataset y mide qué % de alumnos cambian de cluster en cada corrida. Si <20% migran, son robustos. Esfuerzo: 90 min.
::/implementacion

---

::albatros{titulo="Caso bonus — el cluster 'En riesgo' explota un mes" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Tu segmentación arrojaba 60 alumnos en riesgo en marzo. En abril, son 140. ¿Qué pasa?

**Contexto.** Coordinación corre tu pipeline de segmentación cada mes. En marzo, K=4 funcionó perfecto y el cluster "En riesgo" tenía 60 alumnos. En abril, **el mismo pipeline con los mismos hiperparámetros** produce 140 en riesgo. La directora pregunta qué cambió.

**Lo que harás.**
1. Lista 5 hipótesis razonables del cambio:
   - Cambio real en la población (más alumnos están realmente en riesgo).
   - Cambio en la **distribución de features** (drift).
   - Cambio en el **scaler** (nuevo dataset cambia la normalización).
   - Inicialización aleatoria distinta del K-Means.
   - Bug en el pipeline (filas que no debían entrar).
2. Para cada hipótesis: ¿cómo la verificas con código?
3. Ordena las hipótesis por prioridad de investigación (cuál descartar primero).
4. Recomienda un protocolo de monitoreo para detectar este tipo de regresión la próxima vez.

**Entregable.** Documento de 1-2 páginas con: tabla hipótesis/verificación + plan de investigación priorizado + protocolo de monitoreo (3-5 métricas).

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Hipótesis identificadas | <3 | 4 | 5 con justificación |
| Verificación por hipótesis | sin código | algunas | todas con snippet |
| Priorización | sin orden | con orden | con criterio explícito |
| Protocolo monitoreo | sin | borrador | accionable mensualmente |
::/albatros
