---
unidad: 2
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Configura tu primer Project en Claude para tu tutor IA

> Este taller materializa el case study **"Mi tutor IA personal"**: configuras un Project en Claude (o un equivalente en ChatGPT o Gemini) que será el cuarto general de tu tutor durante el resto del manual. Saldrás con tu tutor v0.1 vivo y respondiendo en tu estilo.

::albatros{titulo="Configura tu primer Project en Claude con knowledge base e instrucciones" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Cómo logras que ChatGPT o Claude **te recuerde** tu nivel, tus materias y tu estilo de aprendizaje sin que se lo expliques en cada chat?

**Lo que harás (10 pasos).**

1. **Elige tu plataforma base.** Recomendado: Claude Projects (Pro) o ChatGPT Projects (Plus). Si solo tienes Free, usa Gemini con Gems o un GPT personalizado en ChatGPT (free permite usar GPTs ajenos, no crear los tuyos; alternativa: AI Studio de Google).
2. **Crea un nuevo Project** llamado "Mi tutor IA — [tu nombre]".
3. **Redacta las instrucciones del sistema** (system prompt) en 200-400 palabras. Incluye: a) quién eres tú (nivel educativo, edad, materias actuales, idioma), b) cómo quieres que el tutor te trate (paciente, retador, formal, casual), c) qué evitar (jerga, dar respuestas sin explicar), d) qué priorizar (analogías cotidianas, preguntas socráticas, ejemplos numéricos).
4. **Sube 3-5 documentos** a la knowledge base del Project: tu temario oficial actual (descárgalo de tu escuela), apuntes propios de la materia más difícil, un examen anterior con tus errores marcados.
5. **Prueba con 5 preguntas reales** que te hayan tropezado en clase esta semana. Compara: ¿el tutor responde en el estilo que pediste? ¿usa los documentos que subiste? ¿te trata como pediste?
6. **Itera las instrucciones** una vez basándote en los problemas que detectes. Documenta el cambio.
7. **Crea un "Estilo"** (en Claude) o un "Custom Style" (en ChatGPT custom GPT) con 2-3 ejemplos de texto que te gustaría que el tutor imite (un divulgador favorito, un ensayo tuyo bueno, un libro que te gusta).
8. **Bautiza al tutor** con un nombre y una breve "personalidad" (ej. "Saturno, paciente y curioso").
9. **Documenta tu setup** en un archivo `tutor-v0.1.md` con: nombre, plataforma, instrucciones (copy-paste), documentos cargados, ejemplo de pregunta y respuesta.
10. **Compártelo** con un compañero. Que él haga 3 preguntas a tu tutor y te dé feedback. Anota qué mejorarías para la versión 0.2 (Unidad 03).

**Materiales.**
- Acceso a Claude Pro, ChatGPT Plus, Gemini Advanced o equivalente Free (Google AI Studio).
- 3-5 documentos personales en PDF/MD: temario, apuntes, examen.
- Un editor de texto para guardar tu setup.

**Entregable.**
1. Captura del Project configurado (vista de instrucciones + knowledge base).
2. Archivo `tutor-v0.1.md` con el setup completo.
3. Captura de 3 conversaciones de ejemplo donde se note el estilo.
4. Reflexión escrita de 150 palabras: ¿qué tan distinto fue tu tutor configurado vs. ChatGPT vacío?

**Rúbrica corta.**

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Instrucciones del sistema | 1-2 líneas vagas | 200 palabras coherentes | 400 palabras con contexto, restricciones y prioridades |
| Knowledge base | sin documentos | 1-2 docs | 3-5 docs realmente útiles |
| Estilo personalizado | omitido | mencionado | configurado con ejemplos |
| Iteración | una versión | dos versiones | iteró con feedback de compañero |
| Documentación del setup | ausente | tutor-v0.1.md básico | reproducible al pie de la letra |

**Tip Albatros.** El Project que configures aquí va a evolucionar a tu tutor v1.0 al final del manual. Cada unidad agrega capas: prompts mejores (U03), multimodalidad (U04), conexión con NotebookLM (U05), automatización (U06), GPT custom publicable (U07), creación de contenido (U08), y código de ética (U09). **Guarda el archivo `tutor-v0.1.md`** — lo vas a necesitar.
::/albatros
