---
unidad: 1
seccion: investigacion
paginas_objetivo: 1
---

::investiga{titulo="¿Qué hace que un prompt 'famoso' funcione tan bien? Ingeniería inversa de un repo público." tiempo="3 h"}
**Pregunta de investigación.** Hay repositorios públicos donde compañías y comunidades publican los prompts que están corriendo hoy en producción (Anthropic Cookbook, OpenAI Examples, dair-ai/Prompt-Engineering-Guide, awesome-chatgpt-prompts, system-prompts-and-models-of-ai-tools). Elige **un prompt complejo (>200 palabras)** de cualquiera de esos repos y disecciónalo con las 8 técnicas de la unidad: ¿qué técnicas usa, cuáles omite y por qué crees que está diseñado así?

**Lo que debes encontrar.**
- Identificación clara del prompt (URL, autor, propósito).
- Mapeo de cada parte del prompt a las técnicas 1.1–1.8.
- Aspectos donde el autor decidió **no** aplicar una técnica y tu hipótesis del porqué.
- Una versión propia "v2" donde mejorarías una sección y predigas el efecto.
- Una verificación: corres v1 y v2 contra 3 inputs y comparas outputs.

**Repositorios sugeridos para arrancar la búsqueda.**
- `github.com/anthropics/anthropic-cookbook` — prompts del equipo Anthropic.
- `github.com/openai/openai-cookbook` — prompts oficiales OpenAI.
- `github.com/dair-ai/Prompt-Engineering-Guide` — guía académica con ejemplos.
- `github.com/f/awesome-chatgpt-prompts` — colecciones comunitarias.
- Prompts de sistema filtrados de Claude, ChatGPT, Cursor publicados en `github.com/jujumilk3/leaked-system-prompts` (estudio académico, no piratería).

**Cómo presentarlo.** Documento de 2 páginas:
- Página 1 — el prompt original con anotaciones laterales por técnica.
- Página 2 — tu rediseño v2, justificación y resultados de pruebas.

**Fuentes sugeridas.** Ver bloque ::fuentes:: de la unidad.

**Criterios de evaluación.**
- Precisión del mapeo a las 8 técnicas (35%).
- Profundidad del análisis de las omisiones (25%).
- Calidad del rediseño v2 (20%).
- Verificación empírica con outputs comparados (20%).
::/investiga
