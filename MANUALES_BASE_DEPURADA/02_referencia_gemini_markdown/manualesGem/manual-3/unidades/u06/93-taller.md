---
unidad: 6
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Tu tutor te organiza la semana: pipeline correo + agenda + reunión

> Este taller convierte a tu tutor IA en tu **chief of staff personal**: en una hora montas un sistema que te procesa correo, planea tu semana y resume tus reuniones. Saldrás con tu **tutor v0.6** automatizando 8-10 horas de tu próxima semana real.

::albatros{titulo="Monta tu chief of staff IA en 60 minutos" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Puedes ahorrar 1 hora real cada día con un setup que tarda 60 minutos en armar?

**Lo que harás (12 pasos).**

1. **Hace un inventario de tu semana real.** En una hoja, anota cuánto tiempo gastaste **la semana pasada** en: a) correo, b) planeación, c) reuniones, d) hojas/docs repetitivos. Será tu **baseline**.
2. **Capa 1 — Correo (10 min).** Activa Gemini en Gmail (si usas Google) o Copilot en Outlook (si usas Microsoft). Configura una "Smart Compose" con tu firma y tono. Prueba con 3 correos pendientes: deja que la IA proponga el borrador, edita lo que no te gusta y envía.
3. **Capa 2 — Triage de correo (10 min).** Crea 5 etiquetas/categorías: urgente_trabajo, urgente_escuela, requiere_respuesta_hoy, lectura_diferida, archivar. Pide a la IA un "resumen de bandeja de entrada" cada mañana con 5 grupos.
4. **Capa 3 — Planeación semanal (10 min).** Setup de Motion o Reclaim AI. Carga las tareas críticas de la próxima semana con deadline y prioridad. Si no quieres pagar, usa Notion AI con plantilla "Weekly Planner".
5. **Capa 4 — Hojas automatizadas (5 min).** Instala GPT for Sheets en Google Sheets. Pega 20 filas de algo repetitivo (correos a clasificar, papers a etiquetar). Aplica `=GPT()` y observa el output. Decide qué tareas vas a delegar al spreadsheet.
6. **Capa 5 — Reuniones (10 min).** Conecta Otter, Fireflies o Zoom Companion a tu plataforma de videocalls. Configura las **políticas éticas**: aviso al inicio, consentimiento, no grabar 1:1 sensibles.
7. **Capa 6 — Documento maestro (5 min).** Crea un **dashboard semanal** en Notion con secciones: prioridades, agenda crítica, decisiones pendientes, lecturas, métricas. Vincula tu Motion, tu Otter y tu Gmail con widgets.
8. **Define tu rutina diaria de 30 minutos.** Mañana: 10 min triage de correo + 5 min priorización + 15 min deep work. Cierre del día: 10 min bandeja a cero + 10 min preparar mañana + 10 min reflexión.
9. **Aplica el sistema durante 5 días reales.** Cronómetra cada actividad de las 4 categorías de tu baseline.
10. **Mide el delta.** ¿Ahorraste tiempo? ¿Cuánto? ¿Qué se atoró?
11. **Itera.** Identifica la capa que peor funcionó y mejórala. Identifica la mejor y profundízala.
12. **Documenta** en `chief-of-staff.md`: setup completo, baseline, mediciones día por día, lecciones, plan de mantenimiento mensual.

**Materiales.**
- Cuenta Workspace (gratis) o Microsoft 365 (estudiante gratis con .edu).
- Suscripción a una plataforma IA (Claude Pro / ChatGPT Plus / Gemini Advanced) — opcional pero recomendable.
- Motion o Reclaim AI (planes free disponibles).
- Otter o Fireflies free.
- Notion o equivalente para dashboard.

**Entregable.**
1. Documento `chief-of-staff.md` con setup detallado.
2. Tabla baseline vs medido (4 categorías × 5 días).
3. Captura de tu dashboard de Notion.
4. Reflexión escrita de 200 palabras: ¿qué automatización te dio más rendimiento? ¿qué fue contraproducente?

**Rúbrica corta.**

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Capas implementadas | 2-3 | 4-5 | las 6 capas + dashboard |
| Baseline medido | sin medir | estimado | cronómetro real por categoría |
| Delta documentado | impresionista | con números | con números + análisis cualitativo |
| Iteración | sin iterar | una iteración | iteración + plan de mantenimiento |
| Reflexión | superficial | menciona contras | discute trade-offs y costos |

**Tip Albatros.** El sistema que armas aquí va a evolucionar el resto del semestre. Una vez al mes, dedícale 30 minutos a auditar: ¿qué dejé de usar? ¿qué automatización falló? ¿qué nueva herramienta agregué? **Tu chief of staff es un ser vivo, no un setup estático.**
::/albatros
