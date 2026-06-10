---
unidad: 3
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — De prompt mediocre a prompt excelente en 6 iteraciones

> Este taller materializa la lección central de la unidad: **un prompt no se escribe, se diseña por iteración**. Saldrás con tu propio "prompt insignia" para tu tutor IA personal y un protocolo reproducible que vas a usar el resto del manual.

::albatros{titulo="Lleva un prompt de v1 vago a v6 profesional con métricas objetivas" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Cuántas iteraciones necesitas para que tu tutor IA explique un tema técnico con la calidad y estilo que tú quieres?

**Lo que harás (10 pasos).**

1. **Elige una tarea repetitiva** que harás muchas veces durante el semestre. Ejemplo: "Explícame [tema X] de [materia Y] como si fuera la primera vez que lo escucho, con analogía cotidiana y ejemplo numérico". Esa tarea es tu **caso base**.
2. **Define la rúbrica de evaluación** ANTES de escribir el prompt. 5 criterios, cada uno calificado 1-5: claridad de la analogía, precisión técnica, ejemplo numérico realista, longitud apropiada, tono coherente con tu estilo.
3. **Escribe v1 — Zero-shot vago.** Solo la tarea sin nada más. Ej: "Explícame derivadas".
4. **Ejecuta v1** en tu plataforma base. Califica con la rúbrica. Anota score total (máx. 25).
5. **Escribe v2 — Anatomía R-T-C-R-F-E.** Las 6 capas. Ejecuta y califica.
6. **Escribe v3 — Agrega few-shot.** Pega 1 ejemplo de respuesta ideal (puede ser una explicación de otro tema que sí te gustó). Ejecuta y califica.
7. **Escribe v4 — Agrega chain-of-thought.** Pide al modelo "antes de explicar, identifica 3 conceptos previos que debo dominar y verifica si los conozco con una pregunta". Ejecuta y califica.
8. **Escribe v5 — Agrega output structuring.** Define un esqueleto: ## Intuición · ## Fórmula · ## Ejemplo numérico · ## Pregunta socrática · ## Errores comunes. Ejecuta y califica.
9. **Escribe v6 — Pulido final.** Combina lo mejor de las versiones anteriores y agrega 2 restricciones que descubriste que faltaban. Ejecuta y califica.
10. **Grafica la evolución del score** (puede ser en Sheets o a mano). Anota cuál capa dio el mayor salto. Esa será tu **regla personal de prompting** para tareas similares.

**Materiales.**
- Plataforma elegida en U02 (Claude/ChatGPT/Gemini/Copilot).
- Hoja de cálculo para registrar las 6 versiones × 5 criterios.
- Cronómetro (opcional pero recomendado para medir tiempo de respuesta).

**Entregable.**
1. **Documento `prompt-insignia.md`** con las 6 versiones del prompt en orden, separadas y comentadas.
2. **Tabla de evaluación** con scores: criterio × versión.
3. **Gráfica de evolución** (línea: score total vs versión).
4. **Reflexión escrita** de 200 palabras: ¿qué iteración te dio el mayor salto y por qué? ¿Cuál fue la lección sobre tu propio estilo de prompts?

**Rúbrica corta.**

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Cantidad de iteraciones | 2-3 versiones | 4-5 versiones | 6 versiones distintas |
| Rúbrica aplicada | impresionista | 5 criterios consistentes | 5 criterios + comentarios cualitativos |
| Análisis comparativo | "v6 mejor" | identifica el salto | argumenta por qué cada capa aportó |
| Generalización | sin reflexión | menciona aprendizaje | regla personal aplicable a 3 tareas distintas |
| Documento entregable | suelto | ordenado | reproducible para un compañero |

**Tip Albatros.** Tu prompt v6 va al **banco de prompts personal** que vas a alimentar el resto del manual. Cada Unidad agregará 2-3 prompts más. Al terminar U09, vas a tener 25-30 prompts probados que valen su peso en oro. Guarda este archivo en una carpeta `mi-banco-prompts/` que sea fácil de encontrar.
::/albatros
