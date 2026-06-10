---
unidad: 4
seccion: cierre
paginas_objetivo: 1
---

## Cierre y autoevaluación — Unidad 04

Cerraste la unidad de Estadística. Ahora puedes:

1. **Calcular y reportar** media, mediana, varianza, std con criterio.
2. **Aplicar** distribución normal y la regla 68-95-99.7.
3. **Usar percentiles** para posicionar valores en grupo.
4. **Calcular y interpretar** correlación de Pearson.
5. **Distinguir** correlación de causalidad y nombrar confounders.
6. **Detectar y manejar outliers** con IQR, z-score, percentil.

> **Frase puente.** Tienes el lenguaje numérico. La Unidad 5 te lleva al **primer modelo predictivo** con scikit-learn: regresión lineal y logística, árboles de decisión. La estadística que aprendiste aquí es la base intuitiva de todos esos modelos.

---

### Autoevaluación

| Saber | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Descriptivos | media solo | + std | + mediana criterio | + CV | reporte ejecutivo |
| Distribución normal | desconozco | concepto | regla 68-95 | + verificación | inferencia simple |
| Percentiles | no uso | quantile básico | + IQR | + boxplot lectura | + ranking en producción |
| Correlación Pearson | desconozco | calculo | + interpreto | + matriz | + r² y limitaciones |
| Causalidad | confundo | distingo | + 4 explicaciones | + Hill criteria | propongo experimento |
| Outliers | sin tratar | detecto | + manejo | + decisión justificada | + multivariado |

### Pregunta de cierre

> Tu correlación cal_anterior - cal_final es 0.72. **¿Significa que cal_anterior es la mejor predictor o que ambas son consecuencia de algo más?** Diseña un análisis de 3 pasos para distinguir.

### Conexión con la siguiente unidad

En **U5** vas a usar todo esto: descriptivos para entender features, correlación para seleccionar predictores, outliers para limpiar, y por fin, **modelo ML real** que predice cal_final.
