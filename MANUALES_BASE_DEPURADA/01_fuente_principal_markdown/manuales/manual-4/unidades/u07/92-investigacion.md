---
unidad: 7
seccion: investigacion
paginas_objetivo: 1
---

::investiga{titulo="¿Qué tan cerca están los modelos abiertos de los cerrados? Benchmark personal de 4 modelos." tiempo="3 h"}
**Pregunta de investigación.** Los benchmarks oficiales (MMLU, HumanEval) dicen que los modelos abiertos están "cerca" de los cerrados. Pero los benchmarks son inglés y muy académicos. Diseña tu **propio benchmark de 15 preguntas** en español aplicado a un dominio específico (educación, salud, derecho mexicano), corre **4 modelos** (1 cloud + 3 abiertos), y reporta resultados honestos.

**Lo que debes encontrar.**
- 15 preguntas en español sobre dominio específico, con respuestas verificables.
- 4 modelos a comparar (sugerencia: Claude Sonnet 4.6 cloud + Llama 3.1 70B + Qwen 2.5 72B + DeepSeek-R1-distill 14B).
- Para cada modelo, ejecuta las 15 preguntas y califica:
  - Precisión (1-5).
  - Adherencia al español académico mexicano (1-5).
  - Manejo de casos NO-respuesta (1-5).
  - Tiempo de respuesta.
  - Tamaño de respuesta (tokens).
- Tabla comparativa con totales.

**Cómo presentarlo.** Documento de 3 páginas:
- Página 1: tu metodología (preguntas, criterios, ambiente).
- Página 2: tabla con resultados de los 4 modelos.
- Página 3: análisis de gaps reales y recomendación específica para tu institución.

**Lugares para arrancar.**
- Hugging Face Open LLM Leaderboard.
- Chatbot Arena (lmsys.org) — comparativa por humanos.
- Papers de evaluación: MMLU-Pro, BIG-Bench, MT-Bench.

**Fuentes sugeridas.** Ver `94-fuentes.md`.

**Criterios de evaluación.**
- Diseño riguroso del benchmark (30%).
- Ejecución honesta y reproducible (30%).
- Análisis crítico de resultados (25%).
- Recomendación accionable (15%).
::/investiga
