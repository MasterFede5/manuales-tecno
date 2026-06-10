---
unidad: 4
seccion: investigacion
paginas_objetivo: 1
---

::investiga{titulo="¿Cómo evalúan RAG en producción los principales laboratorios? Benchmark RAGAS aplicado a tu propio sistema." tiempo="3 h"}
**Pregunta de investigación.** Existen frameworks estándar para evaluar la calidad de un sistema RAG: **RAGAS**, **TruLens**, **DeepEval**, **LangSmith Evaluations**. Investiga uno de ellos, entiende sus métricas (faithfulness, context recall, context precision, answer relevancy) y aplica una **mini-evaluación** sobre tu RAG construido en la actividad Albatros.

**Lo que debes encontrar.**
- Definición de las 4 métricas RAGAS principales en lenguaje propio (no copy-paste).
- Cómo se calcula cada una conceptualmente (sin código formal).
- Aplicación: corres tus 10 preguntas golden y, para cada una, calificas manualmente las 4 métricas en escala 0-1.
- Tabla de resultados + análisis de cuál métrica está más débil.
- Plan de mejora basado en los hallazgos (chunking, prompt, modelo, etc.).

**Lugares para arrancar.**
- `docs.ragas.io` — documentación oficial.
- Paper RAGAS (2023): *"Automated Evaluation of Retrieval Augmented Generation"*.
- Lenny's Newsletter — *Evaluating RAG systems*.
- Anthropic Cookbook — RAG evaluation notebook.
- LangSmith docs sobre evaluación de RAG.

**Cómo presentarlo.** Documento de 2-3 páginas:
- Página 1: explicación de las 4 métricas.
- Página 2: tabla con tus 10 preguntas y scores 0-1 para cada métrica + observaciones.
- Página 3: plan de mejora priorizado y propuesta de v1.1 del sistema.

**Fuentes sugeridas.** Ver `94-fuentes.md`.

**Criterios de evaluación.**
- Comprensión real de las 4 métricas (no solo definir, sino diferenciar) (30%).
- Calidad de la evaluación manual aplicada (30%).
- Profundidad del análisis cruzado entre métricas (20%).
- Plan de mejora accionable y priorizado (20%).
::/investiga
