---
unidad: 5
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 05

::practica{titulo="Workflow 'Inscripción nueva' end-to-end en n8n self-hosted, con 5 patrones aplicados"}
**Problema.** Construir el workflow oficial del Asistente Institucional para procesar solicitudes de inscripción.
- Flujo: webhook → clasificación IA → validación → 3 acciones paralelas (Notion, Gmail, Calendar).
- Requerimientos: retry y notificación humana.
- Tiempo objetivo: 90 minutos.

**Paso 1 — Datos.**
- n8n self-hosted en Docker corriendo en `localhost:5678` (o VPS).
- Notion BD "Solicitudes admisión 2026".
- Cuenta Gmail y Google Calendar institucionales (OAuth).
- Slack workspace con canal `#admisiones`.
- API keys: Anthropic, Notion, Slack.

**Paso 2 — Estrategia.**
Aplicaremos los siguientes patrones clave:
- Patrón 4 (idempotency) en el webhook.
- Patrón 1 (router) tras la clasificación IA.
- Patrón 2 (fan-out/fan-in) para Notion + Gmail + Calendar.
- Patrón 3 (retry con backoff) en cada llamada API.
- Patrón 5 (approval loop) si confianza < 0.7.

::interioriza
Imagina un guardia de seguridad (Idempotency) que evita que pase la misma persona dos veces.
Una vez dentro, un supervisor reparte el trabajo simultáneo a tres oficinistas (Fan-out).
Así el trabajo no se atasca y nadie procesa el mismo documento dos veces.
::/interioriza

**Paso 3 — Construcción del workflow.**
- **Trigger:** Webhook POST en `/webhook/admisiones`.
- **Idempotency check:** `idempotency_key = email + timestamp_minute`.
- **Clasificación IA:** Anthropic extrae `{categoria, confianza}`.
- **Validación:** Si confianza < 0.7, pide a humano clasificar vía Slack.
- **Switch:** "inscripcion" (sigue), "info" (FAQ), "queja" (coordinación).
- **Fan-Out (paralelo):** Notion, Gmail y Calendar operan simultáneamente con retries.
- **Fan-In:** Une los resultados y construye objeto final `{folio, calendar_url, notion_id}`.
- **Notificación:** Avisa a Slack con datos. Responde OK 200.

**Paso 4 — Manejo de errores.**
- Nodos API configuran retry de 3 veces (backoff 2, 4 y 8 segundos).
- Si hay fallo global, alerta a `#alertas-asistente`.
- Logging centralizado en Google Sheets.

**Paso 5 — Pruebas y Resultados.**
- Curl test: Ejecuta en 8.4 segundos (todas las acciones en paralelo).
- Idempotency test: Un doble curl a los 3 segundos devuelve "ya procesado".
- Chaos test: Apagar Notion hace saltar retries y envía alerta, pero Gmail/Calendar completan.

**Respuesta.** Workflow `inscripcion-v1.0.json` activo.
- ROI a la 4ª solicitud.
- Ahorra 22 horas a la coordinadora.

**Lección.** Las técnicas de esta unidad son piezas de Lego.
Saltarse idempotency y retry es la causa #1 de fallos en producción.
::/practica

::pausa{}
**Reflexión:**
- ¿Qué pasaría si el webhook no tuviera idempotencia y el formulario sufriera un doble clic del usuario?
- ¿Por qué el fan-out de acciones independientes reduce drásticamente el tiempo de ejecución?
::/pausa

::practica{titulo="Cómo re-arquitecté el workflow lento en 90 minutos para que el padre no esperara 24 segundos"}
**Problema.** La coordinadora reporta que el padre espera de 20-30 segundos tras enviar su solicitud.
- Muchos padres cierran el chat creyendo que falló.
- Causado porque Notion, Gmail y Calendar operaban de forma en serie (secuencial).

**Paso 1 — Diagnóstico.**
- El proceso tardaba una mediana de 12.9s y P95 de 24s.
- Las tres acciones son totalmente independientes entre sí.
- El padre no necesita esperar a que todas terminen para recibir su confirmación y folio.

**Paso 2 — Estrategia de re-arquitectura.**
- **Frontend Sync:** Lo que el padre ve (idempotency, clasificación, confirmación con folio).
- **Backend Async:** Lo que pasa detrás (Notion, Gmail, Calendar en paralelo).
- **Notificación final:** Tras terminar el Fan-in, avisa a la coordinadora por Slack.

::interioriza
Como en un drive-thru de comida rápida.
La ventana 1 te cobra y te da el ticket (Workflow síncrono, súper rápido).
La ventana 2 te prepara la comida mientras avanzas (Workflow asíncrono, background).
::/interioriza

**Paso 3 — Diseño en n8n.**
- **Workflow A (Sync):** Recibe petición, revisa idempotencia, genera folio y responde 200 OK. Llama al Workflow B.
- **Workflow B (Async):** Recibe payload del A, hace fan-out a Notion/Gmail/Calendar.
- **Manejo de errores:** Si Notion falla 3 veces, manda alerta Slack para retry manual.

**Paso 4 — Resultados.**
- Latencia percibida por el padre: de 13s a ~2.4s. **Mejora de 8.4x.**
- Las inscripciones completan 100% sus acciones asíncronas en ~5s de fondo.
- Cero reclamos de padres y cero confusiones.

**Lección.** Ejecutar todo en serie es cómodo pero caro en experiencia de usuario.
Lo que el usuario debe ver inmediato va en *sync*; lo demoroso en *async*.
::/practica

::pausa{}
**Deducción de arquitectura:**
- Al usar dos workflows separados, ¿qué debes monitorear si un folio se entrega pero la fila de Notion no aparece?
- ¿Cómo el patrón async mejora la percepción de fiabilidad del sistema para el usuario?
::/pausa

::practica{titulo="Cómo decidí migrar de Zapier a n8n self-hosted con números, no con preferencia"}
**Problema.** Determinar si conviene migrar 4 workflows desde Zapier ($79.99/mes) a n8n self-hosted ($7/mes).
- Volumen: ~10,000 tareas mensuales.
- La dirección de TI necesita argumentos numéricos claros.

**Paso 1 — Costos directos vs Ocultos.**
- Ahorro nominal: $73 al mes ($876/año).
- Costo migración (Setup + Pruebas): 16 horas de trabajo (~$400 one-time).
- Costo mantenimiento mensual (Updates + Monitoreo): 2 horas/mes (~$50).

**Paso 2 — Análisis Total.**
- Costo real n8n = $57/mes. Ahorro real = ~$23/mes.
- Break-even: recuperaríamos la inversión inicial a los 17 meses.
- Zapier incluye 99.9% de SLA, eliminando el riesgo de caída del VPS.

::interioriza
Migrar de software SaaS a Self-Hosted es como dejar de alquilar casa para construir una tú mismo.
El pago mensual baja drásticamente, pero el mantenimiento de tuberías y goteras corre 100% por tu cuenta.
::/interioriza

**Paso 3 — Decisión (ADR-016).**
- Mantenemos Zapier temporalmente por su estabilidad y bajo ahorro real.
- Riesgo no aceptable: depender del conocimiento de una sola persona en TI.
- Plan piloto: Migrar solo el workflow menos crítico (Reporte semanal) a n8n free.

**Respuesta.** No se migran los procesos críticos.
- La dirección de TI aprobó basarse en números reales de mantenimiento, no en favoritismos.
- Se evaluará nuevamente cuando el equipo crezca y el volumen supere 20,000 tareas/mes.

**Lección.** Solo migra cuando el ahorro a 12 meses supere 3x el costo de migración y mitigues riesgos.
Pagar por SaaS es, muchas veces, pagar por continuidad y tranquilidad.
::/practica

::pausa{}
**Reto estratégico:**
- Si un nuevo servicio *SaaS* similar a Zapier ofreciera cobrar $15/mes por 20,000 tareas, ¿volverías a calcular la migración? ¿Por qué?
::/pausa
