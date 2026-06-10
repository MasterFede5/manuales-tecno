---
unidad: 5
seccion: taller
paginas_objetivo: 2
---

## Taller — Construye un workflow real de notificaciones en 60 minutos

::albatros{titulo="Construyes un workflow de notificaciones en 60 minutos" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Tu institución tiene una tarea repetitiva que hoy pasa por WhatsApp/Slack/correo manual. ¿Y si dejaras un workflow corriendo que la haga sola por ti durante el próximo mes?

**Lo que harás.** Vas a construir tu **primer workflow real de notificaciones**: un evento dispara una alerta automatizada al canal correcto con el mensaje adecuado. Aplicas 3 patrones (idempotency, retry, router). Al cerrar el cronómetro: el workflow está activo, lo probaste con 5 inputs reales y un input erróneo, y ahorra al menos 1 acción humana por evento.

**Materiales reales.**
- Cuenta n8n cloud free trial (o n8n self-hosted con Docker, o Make free).
- Acceso a 1 origen de evento: webhook desde un formulario, Sheet con nuevas filas, o trigger manual.
- Acceso a 2 destinos: Slack, Telegram, Email, Discord, WhatsApp Business o lo que tengas.
- 60 min sin notificaciones.

**Caso sugerido.** *"Cuando llega una nueva inscripción al formulario de Google Forms, notificar a `#admisiones` en Slack y al correo de la coordinadora con el detalle del solicitante. Si el formulario marca bandera 'urgente', notificar también al móvil de dirección por Telegram."*

**Pasos (10).**

1. **Min 0–5 — Mapeo del evento y destinos.** En papel: dibuja origen → procesamiento → 2-3 destinos. Lista qué dato sale del origen, qué transformación necesita, qué texto va a cada destino. Sin papel previo, el workflow se hace caótico.

2. **Min 5–10 — Crear workflow vacío.** Entra a n8n. Click "+ New". Nómbralo `notif-inscripciones-v1`. Acuerda con tu equipo el prefijo (`[Asist]`).

3. **Min 10–20 — Trigger.** Configura el origen:
   - Si formulario Google Forms: nodo "Google Forms Trigger" con la cuenta correcta.
   - Si webhook propio: nodo "Webhook" con auth Bearer token (genera uno aleatorio en el momento).
   - Si Sheet con polling: nodo "Google Sheets Trigger" con polling 5 min.
   Smoke test: dispara un evento manual y verifica que el trigger lo recibe.

4. **Min 20–25 — Idempotency.** Agrega nodo "Set" después del trigger:
   - Crea variable `idempotency_key = $json.email + '|' + $json.timestamp.slice(0,16)`.
   - Nodo IF: si la clave existe en una hoja "Cache" → respond "ya procesado" sin seguir.
   - Si no existe → seguir y agregar clave a la hoja.

5. **Min 25–30 — Router (IF urgente).** Nodo IF que evalúa `$json.urgente === 'true'`:
   - Branch SÍ → 3 destinos (Slack + correo + Telegram dirección).
   - Branch NO → 2 destinos (Slack + correo).

6. **Min 30–40 — Construir las acciones (fan-out).** Para cada destino:
   - Slack: nodo "Slack" con channel `#admisiones`, message con datos del solicitante.
   - Email: nodo "Gmail" o "Send Email" con destinatario coordinadora, subject + body.
   - Telegram: nodo "Telegram" con chat_id de dirección.
   En cada uno, configura **Settings → Retry on Fail = 3, Wait between tries = 2s con backoff**.

7. **Min 40–45 — Fallback en errores.** Agrega un "Error Trigger" workflow global o un branch `Error Output` por nodo crítico. Que mande Slack a `#alertas-asistente` con: workflow, nodo, error, timestamp. Esto te avisa en producción.

8. **Min 45–55 — Pruebas.** Activa el workflow. Lanza 5 inputs reales (puedes usar el formulario o curl al webhook):
   - 3 inscripciones normales.
   - 1 inscripción urgente.
   - 1 inscripción duplicada (mismo email +1 segundo).
   Verifica:
   - 3 normales → 2 destinos (Slack + correo).
   - 1 urgente → 3 destinos.
   - 1 duplicada → respuesta "ya procesado", sin re-disparar.

9. **Min 55–58 — Versionado.** Click Workflow → Download (exporta JSON). Pega en `workflows/notif-inscripciones/v1.0.0/notif-inscripciones-v1.0.0.json` de tu repo. CHANGELOG: 1 línea. Commit. Tag opcional `v1.0.0`.

10. **Min 58–60 — Comparte y activa.** Mensaje al equipo en `#admisiones` con: nombre del workflow, qué hace, cómo monitorearlo, qué hacer si falla (manual rápido). Pídele a una persona del equipo que mire `#admisiones` durante 24 horas y reporte si el workflow funciona o si hay ruido.

**Entregable.**
- Workflow activo en n8n (URL al trigger).
- JSON exportado en repo `workflows/notif-inscripciones/v1.0.0/`.
- Mensaje al equipo con instrucciones de monitoreo.
- Tabla con resultados de las 5 pruebas + 1 duplicada.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Mapeo previo en papel | sin papel | bosquejado | dibujado y respetado |
| Patrones aplicados | 0-1 | 2 | 3 (idempotency, retry, router) |
| Pruebas | <3 | 5 normales | 5 + duplicado + urgente + chaos |
| Manejo de errores | sin retry | retry básico | retry + fallback + alerta |
| Versionado externo | sin commit | export + commit | con CHANGELOG y tag |
| Adopción | privado | activado | persona monitoreando 24 h |
::/albatros
