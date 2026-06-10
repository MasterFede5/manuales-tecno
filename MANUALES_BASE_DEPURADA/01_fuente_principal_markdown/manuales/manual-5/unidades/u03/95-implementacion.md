---
unidad: 3
seccion: implementacion
paginas_objetivo: 2
---

::implementacion{titulo="Implementación Albatros — Dashboard ejecutivo del rendimiento escolar"}
**Objetivo.** Producir, presentar y compartir el **dashboard ejecutivo del rendimiento escolar 2026** ante stakeholders reales (consejo, dirección o coordinación), con 5-7 gráficos publicables y storytelling de 10 minutos.

**Materiales.** Dataset limpio de U2, matplotlib + seaborn, software de presentación, 5-6 horas distribuidas.

**Pasos.**
1. Brief del consejo (30 min): qué pregunta responder y qué quieren saber.
2. Producción de 5-7 gráficos (3 h) siguiendo storytelling.
3. Presentación con slides (1 h).
4. Test piloto (30 min) con compañero.
5. Iteración + presentación real (variable).
6. Recolectar feedback y documentar.

**Entregable.**
- 5-7 gráficos en PNG (200 dpi).
- Presentación PDF/PPT.
- Reporte de feedback (1 pp).
- Repo Git con código reproducible.

**Rúbrica.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cantidad gráficos | 1-2 | 4-5 | 5-7 con cohesión |
| Personalización | default | título y ejes | publicable institucional |
| Storytelling | sin orden | 3 actos básicos | con anotaciones y mensaje único |
| Adopción | privado | mostrado a equipo | con feedback y aplicación |

**Próximo paso.** En **U4** vas a profundizar en **estadística** para que tus interpretaciones tengan fundamento numérico (correlación, percentiles, outliers).

### Hitos intermedios

| Hito | Tag git | Criterio de cierre |
|---|---|---|
| H1 | `u3-h1-tema` | Tema institucional aplicado (sns.set_theme con paleta) |
| H2 | `u3-h2-distribucion` | Histograma con KDE + media marcada |
| H3 | `u3-h3-comparacion` | Boxplot por materia con línea de aprobación |
| H4 | `u3-h4-relacion` | Scatter con regresión y r anotado |
| H5 | `u3-h5-correlaciones` | Heatmap completo con anotaciones |
| H6 | `u3-h6-storytelling` | 5 gráficas en orden con mensaje escrito por gráfica |

### Reto bonus extendido (3 retos)

**Reto bonus 1 — Dashboard interactivo con Plotly Express.** Reemplaza una de las 5 gráficas con su versión Plotly (hover, zoom). Esfuerzo: 60 min.

```python
import plotly.express as px
fig = px.scatter(df, x="horas_estudio", y="cal_final",
                 color="materia", trendline="ols",
                 hover_data=["id", "asistencia"])
fig.write_html("scatter.html")
```

**Reto bonus 2 — Gráficas accesibles para daltónicos.** Reemplaza tu paleta por `viridis` o `cividis` (perceptualmente uniformes y daltónico-safe). Reproduce las 5 imágenes y compáralas. Esfuerzo: 30 min.

**Reto bonus 3 — Animación de evolución temporal.** Si tuvieras `cal_final_bimestre1, ...bimestre4`, anima cómo cambia el promedio por materia con `matplotlib.animation`. Genera GIF. Esfuerzo: 90 min.
::/implementacion

---

::albatros{titulo="Caso bonus — auditoría visual de un reporte ejecutivo" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ¿Sabrías detectar manipulación visual en un reporte que llega a junta directiva?

**Contexto.** El consultor externo entregó un reporte con 6 gráficas. Coordinación te pidió **auditarlo antes de circularlo**.

**Lo que harás.**
1. Audita los 6 gráficos descritos:
   - G1: bar chart con eje Y de 70 a 100 (no de 0).
   - G2: pie chart con 11 secciones similares.
   - G3: scatter sin línea de tendencia ni r.
   - G4: heatmap sin escala de color visible.
   - G5: línea con anotación "tendencia positiva" pero solo 2 puntos.
   - G6: stacked bar con leyenda incompleta.
2. Para cada uno: severidad (alta/media/baja), por qué engaña, propuesta de corrección.
3. Decide si publicar, devolver o corregir internamente.

**Entregable.** Tabla de auditoría + recomendación final + checklist de revisión visual para futuros reportes externos.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Problemas detectados | <3 | 4-5 | los 6 con explicación |
| Severidad asignada | uniforme | mixta | justificada con criterio |
| Propuesta de corrección | genérica | algunas | accionable para cada uno |
| Checklist replicable | sin | borrador | publicable como guía interna |
::/albatros
