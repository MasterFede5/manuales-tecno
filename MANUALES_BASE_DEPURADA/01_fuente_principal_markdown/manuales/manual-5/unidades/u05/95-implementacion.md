---
unidad: 5
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Predictor escolar v1.0 con scikit-learn"}
**Objetivo.** Construir, evaluar y guardar el **predictor de calificación final v1.0** del Asistente Albatros con scikit-learn, listo para integrarse en U8 (API + interfaz Streamlit).

**Materiales.** Dataset limpio U2, scikit-learn, joblib, GitHub, 6-8 horas.

**Pasos.**
1. Pipeline completo (1 h).
2. Comparar 3-4 modelos (Linear, Tree, RandomForest, ¿XGBoost de la investigación?) (2 h).
3. Validar con CV 5-fold (1 h).
4. Análisis de overfitting + ajuste hiperparámetros (1 h).
5. Modelo final guardado con joblib (30 min).
6. Función `predecir(alumno_dict)` reutilizable (1 h).
7. Documentación con limitaciones y advertencias éticas (1 h).
8. Subir a GitHub público + README ejecutable (30 min).

**Entregable.**
- Notebook completo con código y comentarios.
- `modelo_predictor_v1.pkl`.
- Función `predecir(...)` con docstring.
- README con instrucciones.
- Documento de limitaciones (1 pp): qué predice bien, qué no, sesgos posibles.

**Rúbrica.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Pipeline completo | sin split | con train/test | con CV 5-fold |
| Modelos | uno | dos-tres | 3+ comparados con tabla |
| Diagnóstico | sin gap | menciona | analiza overfitting con curva de aprendizaje |
| Modelo guardado | inexistente | .pkl | + función + docstring |
| Documentación | mínima | README | + limitaciones éticas |

**Próximo paso.** En **U6** vas a aprender **clustering no supervisado** (K-Means) para **descubrir perfiles** de alumnos sin etiquetas.

### Hitos intermedios

| Hito | Tag git | Criterio de cierre |
|---|---|---|
| H1 | `u5-h1-pipeline` | Pipeline básico (split, fit, score) corriendo |
| H2 | `u5-h2-cv` | CV 5-fold con std reportada |
| H3 | `u5-h3-comparacion` | Tabla comparativa 3 modelos con métricas |
| H4 | `u5-h4-tuning` | GridSearch ejecutado, mejor combinación documentada |
| H5 | `u5-h5-curva` | Curva de aprendizaje generada e interpretada |
| H6 | `u5-h6-modelo-pkl` | `modelo_predictor_v1.pkl` guardado y cargable |

### Reto bonus extendido (3 retos)

**Reto bonus 1 — Importancia de features (SHAP).** Instala `shap` y genera explicaciones globales y por instancia. Identifica para 3 alumnos específicos qué feature **más subió** o **bajó** la predicción. Esfuerzo: 90 min.

```python
import shap
explainer = shap.TreeExplainer(modelo_final)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

**Reto bonus 2 — Calibración de probabilidades.** Para regresión logística: ¿las probabilidades predichas reflejan la realidad? Genera `calibration_curve` y diagnostica. Si está descalibrada, aplica `CalibratedClassifierCV`. Esfuerzo: 60 min.

**Reto bonus 3 — Modelo persistido + cargado en script independiente.** Crea `predict.py` separado del notebook que carga el `.pkl` y predice para nuevos alumnos vía CLI:

```bash
python predict.py --horas 4 --asistencia 0.85 --cal_anterior 7.0
```

Esfuerzo: 45 min.
::/implementacion

---

::albatros{titulo="Caso bonus — comité revisa tu modelo antes de producción" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ¿Tu modelo aguanta una revisión formal antes de afectar la vida académica de 480 alumnos?

**Contexto.** Coordinación convocó un comité de 4 personas (estadística, pedagogía, derecho/ética, sistemas) para revisar tu predictor antes de implementarlo. Te entregan 5 preguntas:

> 1. **Estadística:** "¿Qué tan estables son las predicciones si el dataset cambia?"
> 2. **Pedagogía:** "¿Cómo explicarías a un docente por qué un alumno particular fue clasificado como riesgo?"
> 3. **Ética:** "¿Hay sesgo por materia? ¿El modelo discrimina alguna cohorte?"
> 4. **Sistemas:** "¿Qué pasa si el modelo predice mal? ¿Cómo lo detectamos en producción?"
> 5. **Coordinación:** "¿Qué umbral de probabilidad recomiendas y por qué?"

**Lo que harás.**
1. Para cada pregunta, prepara una respuesta de 3-5 líneas con evidencia (métricas, gráficas, código).
2. Identifica las 2 preguntas para las que NO tienes respuesta sólida; documenta qué necesitarías para tenerla.
3. Diseña un protocolo de **monitoreo en producción**: qué métricas reportar mensualmente.
4. Redacta una recomendación final: ¿implementar ya, implementar con condiciones, o no implementar?

**Entregable.** Documento ejecutivo de 2 páginas con tabla pregunta/respuesta + protocolo monitoreo + recomendación.

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Respuestas técnicas | <3 | 4 | 5 con evidencia |
| Reconocimiento de límites | sin | algunos | 2 honestos con plan |
| Protocolo monitoreo | sin | borrador | 4+ métricas con frecuencia |
| Recomendación final | sin matiz | binaria | con condiciones específicas |
::/albatros
