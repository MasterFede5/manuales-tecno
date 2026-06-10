---
unidad: 1
seccion: taller
paginas_objetivo: 2
---

## Taller — Tu biblioteca personal de prompts versionados en Notion

::albatros{titulo="Construyes tu biblioteca personal de prompts en 60 minutos" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Y si los prompts que mejor funcionan para tu trabajo desaparecieran mañana porque viven en el historial efímero de un chat? El equipo entero pierde ese saber. ¿Cómo lo proteges?

**Lo que harás.** Vas a construir tu **biblioteca personal de prompts** en Notion (o en Markdown puro si prefieres Git). Al cerrar el cronómetro tendrás 5 prompts versionados, con golden mini, y un proceso para añadir el sexto sin pensar.

**Materiales reales.**
- Cuenta gratuita de Notion (o un repo en GitHub).
- Acceso a un LLM (Claude, ChatGPT o Gemini, plan gratis sirve).
- Una hoja con 5 tareas reales que repites cada semana en tu institución.
- 60 minutos sin notificaciones.

**Pasos (8).**

1. **Min 0–5 — Inventario.** Anota 5 tareas repetitivas reales: "redactar correo a papás", "resumir junta de academia", "clasificar PQRS", "reescribir un comunicado borrador", "generar 5 variantes de un mensaje WhatsApp". Las 5 deben ser **tareas que ya hiciste** —no aspiracionales—.

2. **Min 5–10 — Estructura del workspace.** Crea en Notion una base de datos "Prompts Albatros" con columnas: `nombre`, `version`, `tarea`, `modelo_recomendado`, `fecha`, `estado` (draft/canary/prod), `costo_aprox`, `link_golden`.

3. **Min 10–25 — Meta-prompt en serie.** Para las primeras 3 tareas, abre Claude o ChatGPT, pega el meta-prompt patrón (§1.2) con el objetivo y criterios. Recibe v0. Pega v0 en Notion como `v1.0`. **No edites todavía** — solo guarda.

4. **Min 25–35 — Smoke test rápido.** Ejecuta cada v1.0 con 1 input real. Anota en Notion el output y una nota: "ok / falla en X / falla en Y". Si una falla obvia, levanta un comentario en Notion: "fix v1.1 — agregar restricción de fechas relativas".

5. **Min 35–45 — Constrained output.** Para los 2 prompts donde el output entrará en otro sistema (correo o tabla), agrega al final del prompt: `<output_format>JSON con campos: ... </output_format>` — schema mínimo. Reejecuta y valida que el JSON parsea.

6. **Min 45–50 — Mini-golden.** Para cada uno de los 5 prompts, captura **3 entradas reales** y la salida esperada (la que hubieras escrito tú). Pégalas en una sub-página `golden/` por prompt. No formal aún, basta con tabla.

7. **Min 50–55 — Process page.** Crea una página `cómo añadir un prompt` con 6 pasos: idea → meta-prompt → v0 → smoke → mini-golden → publicar a `prod`. Esta página vale más que los 5 prompts.

8. **Min 55–60 — Compartir y agendar revisión.** Comparte el workspace con 1 persona (compañero, jefa, alumna). Agenda **revisión mensual** de 30 minutos en tu calendario para los próximos 6 meses.

**Entregable.**
- URL del workspace Notion (o repo Git) con 5 prompts en `v1.0` + golden de 3 ejemplos cada uno + página de proceso.
- Captura de la base de datos con las columnas pobladas.
- Mensaje de invitación enviado a 1 persona externa.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cobertura | <3 prompts | 5 prompts en v1.0 | 5 prompts + 1 sexto añadido siguiendo el proceso |
| Golden mini | <2 ejemplos | 3 ejemplos por prompt | 3 ejemplos cubriendo borde |
| Constrained output | sin schema | en 1-2 prompts | en todos los que aplican |
| Proceso documentado | implícito | página con 6 pasos | proceso + cadencia de revisión |
| Socialización | privado | compartido a 1 persona | persona ya devolvió feedback |
::/albatros
