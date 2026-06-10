---
unidad: 4
seccion: implementacion
paginas_objetivo: 2
---

::implementacion{titulo="Implementación Albatros — Reporte estadístico defendible"}
**Objetivo.** Producir reporte estadístico de 1-2 páginas que combine las 6 técnicas de la unidad y se defienda ante consejo académico, con números, advertencias éticas (causalidad), y recomendaciones accionables.

**Materiales.** Dataset limpio U2, pandas, scipy/numpy, 5-6 horas.

**Pasos.**
1. Análisis descriptivo completo (1 h).
2. Verificar normalidad de distribución (30 min).
3. Calcular percentiles clave (30 min).
4. Matriz de correlaciones + interpretación (1 h).
5. Detección y diagnóstico de outliers (1 h).
6. Análisis crítico: distinguir correlaciones de afirmaciones causales (30 min).
7. Reporte ejecutivo con recomendaciones y advertencias (1 h).

**Entregable.** Reporte 1-2 pp + código en Git + advertencias documentadas.

**Rúbrica.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| 6 técnicas integradas | <3 | 4-5 | 6 con coherencia |
| Distinción causal | confunde | nota | profundo con confounders y experimentos |
| Outliers | sin tratar | detectados | manejados con justificación |
| Recomendaciones | ausentes | genéricas | accionables y limitadas a evidencia |

**Próximo paso.** En **U5** vas a construir tu **primer modelo predictivo** con scikit-learn usando los predictores que esta unidad identificó.

### Hitos intermedios

| Hito | Tag git | Criterio de cierre |
|---|---|---|
| H1 | `u4-h1-descriptivos` | media, mediana, std, percentiles correctos |
| H2 | `u4-h2-normalidad` | Shapiro + QQ-plot generados |
| H3 | `u4-h3-corr` | Matriz Pearson + interpretación escrita |
| H4 | `u4-h4-outliers` | Detector IQR funcional + lista exportada |
| H5 | `u4-h5-bootstrap` | IC bootstrap con seed fija reproducible |
| H6 | `u4-h6-reporte` | Reporte 1pp con números + advertencia causal |

### Reto bonus extendido (3 retos)

**Reto bonus 1 — ANOVA o Kruskal-Wallis para 3 materias.** Compara formalmente si las 3 materias tienen promedios distintos. Reporta F (o H), p-valor, interpretación. Esfuerzo: 60 min.

```python
import scipy.stats as stats
grupos = [df[df.materia == m]["cal_final"].values for m in df.materia.unique()]
F, p = stats.f_oneway(*grupos)
H, p_kw = stats.kruskal(*grupos)
```

**Reto bonus 2 — Correlación parcial.** ¿Qué pasa con la correlación `horas_estudio ↔ cal_final` cuando **controlas por** `cal_anterior`? Usa `pingouin.partial_corr`. ¿La correlación se mantiene o desaparece? Esfuerzo: 60 min.

**Reto bonus 3 — Mapa de outliers individuales.** Para cada outlier IQR, genera ficha individual: id, cal_final, asistencia, horas, materia + 3 hipótesis de por qué es outlier. Exporta a `outliers_fichas.csv`. Esfuerzo: 45 min.
::/implementacion

---

::albatros{titulo="Caso bonus — defender el reporte ante una crítica externa" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ¿Aguantas un panel de 4 expertos atacando tu reporte estadístico?

**Contexto.** Tu reporte fue compartido con un profesor de estadística externo. Te devuelve 5 críticas duras (cópialas a tu cuaderno):

> 1. "Reportas Pearson pero la relación claramente no es lineal en el scatter."
> 2. "El test de Shapiro rechazó normalidad; ¿por qué sigues usando media?"
> 3. "Tu IC al 95% es paramétrico. ¿Por qué no bootstrap?"
> 4. "Hablas de 'predictores' pero no controlaste por confounders."
> 5. "Los 12 outliers que removiste podrían ser la señal más importante, no el ruido."

**Lo que harás.**
1. Por cada crítica: ¿es válida (sí/no/parcial), por qué? Una línea de respuesta técnica.
2. Identifica 2 que te obligan a **rehacer** el reporte y cuáles requieren solo **adendum**.
3. Diseña un plan de iteración (pasos concretos para responder a las críticas válidas).
4. Documenta lo que aprendiste para no repetirlo en U5.

**Entregable.** Documento de 1-2 páginas con tabla crítica/respuesta + plan de iteración + lecciones.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Críticas evaluadas | <3 | 4 | las 5 con justificación |
| Distinción rehacer/adendum | sin | parcial | clara y defendible |
| Plan iteración | vago | con pasos | accionable y priorizado |
| Lecciones | sin | una | aplicables a U5 |
::/albatros
