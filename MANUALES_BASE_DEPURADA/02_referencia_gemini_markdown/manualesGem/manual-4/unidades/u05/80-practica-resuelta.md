---
unidad: 5
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 05

::practica{titulo="Workflow 'Inscripción nueva' end-to-end en n8n self-hosted, con 5 patrones aplicados"}
**Problema.** Construir el workflow oficial del Asistente Institucional para procesar solicitudes de inscripción: webhook → clasificación IA → validación → 3 acciones paralelas (Notion, Gmail, Calendar) con retry → notificación humana. Tiempo objetivo: 90 minutos.

**Paso 1 — Datos.**
- n8n self-hosted en Docker corriendo en `localhost:5678` (o VPS).
- Notion BD "Solicitudes admisión 2026" con propiedades: Nombre, Email, Mensaje, Folio, Status, Fecha.
- Cuenta Gmail institucional con OAuth ya configurado.
- Google Calendar institucional.
- Slack workspace con canal `#admisiones`.
- API keys: Anthropic, Notion, Slack.

**Paso 2 — Estrategia.**
Aplicaré los patrones:
- Patrón 4 (idempotency) en el webhook.
- Patrón 1 (router) tras la clasificación IA.
- Patrón 2 (fan-out/fan-in) para Notion + Gmail + Calendar.
- Patrón 3 (retry con backoff) en cada llamada API.
- Patrón 5 (approval loop) si el clasificador devuelve confianza < 0.7.

**Paso 3 — Construcción del workflow (60 min).**

```
1. [Webhook trigger]
   URL: /webhook/admisiones
   Auth: Header Bearer token
   Method: POST

2. [Set] Idempotency check
   Variable: idempotency_key = email + timestamp_minute
   Si existe en DB cache → respond 200 "ya procesado"
   Si no → continúa

3. [Anthropic Chat] Clasificar mensaje
   Prompt: "Devuelve JSON {categoria, confianza}. Categorías: inscripcion, info, queja, otro."
   Schema enforced.

4. [IF] confianza > 0.7
   Sí → seguir
   No → [Slack] Pide humano clasificar manualmente, espera respuesta

5. [Switch] por categoría
   Caso "inscripcion" → seguir al fan-out
   Caso "info" → enviar respuesta automática FAQ
   Caso "queja" → escalar a coordinación
   Default → notificar humano

6. [Split In Batches: 1] FAN-OUT — paralelo
   Branch A:
     [Notion: Database append]
       Retry 3x con backoff (2s, 4s, 8s)
       En fallo → Slack alerta

   Branch B:
     [Gmail: Send email]
       Plantilla con folio
       Retry 3x

   Branch C:
     [Google Calendar: Create event]
       Slot disponible próximo
       Retry 3x

7. [Merge] FAN-IN
   Combina resultados de las 3 ramas
   Construye objeto final {folio, calendar_url, notion_id}

8. [Slack: Post to #admisiones]
   "📥 Nueva solicitud · Folio X · Nombre: [nombre] · Calendar: [url]"

9. [Respond to Webhook]
   200 OK con folio
```

**Paso 4 — Manejo de errores.**
- Cada nodo de API: retry 3 veces, backoff 2/4/8 segundos.
- Workflow Error trigger global: si algo cae al piso, alerta a `#alertas-asistente`.
- Logging: cada paso a un Sheet "Logs_Asistente_2026" con timestamp, paso, status.

**Paso 5 — Pruebas (15 min).**

Curl de prueba:
```bash
curl -X POST https://miinstitucion.app.n8n.cloud/webhook/admisiones \
  -H "Authorization: Bearer xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Andrea Hernández",
    "email": "andrea.h@example.com",
    "mensaje": "Quiero inscribir a mi hijo a 1.º bachillerato 2026"
  }'
```

Resultados:
- Workflow corre en 8.4 segundos (todas las acciones paralelas).
- Notion: fila creada con folio AH-001.
- Gmail: email recibido con plantilla y folio.
- Calendar: evento creado para entrevista próximo lunes 16:00.
- Slack: notificación en `#admisiones`.

**Paso 6 — Test de idempotency.**
Reenvío el mismo curl 3 segundos después. Workflow detecta misma idempotency_key y devuelve "ya procesado" sin re-ejecutar nada. ✓

**Paso 7 — Test de fallo de API (chaos test).**
Apago temporalmente la integración Notion.
- Workflow detecta fallo, hace retry 3 veces con backoff.
- Falla las 3 veces.
- Salta al fallback: Slack alert "❌ Fallo Notion · Folio AH-002 · escalar manual".
- Las otras dos ramas (Gmail, Calendar) sí completan.

Reactivo Notion. Curl nuevo. Funciona normal. ✓

**Paso 8 — Test de baja confianza.**
Envío mensaje ambiguo: "necesito información". Clasificador devuelve confianza 0.55. Workflow se pausa, manda Slack a coordinadora con botones "inscripción / info / queja / otro". Coordinadora click "info", workflow continúa por la rama correcta. ✓

**Respuesta.** Workflow `inscripcion-v1.0.json` operativo en producción, exportado a Git, documentado. Procesa solicitudes en ~8 segundos vs 30 minutos manuales. ROI a la 4ª solicitud.

**Verificación final.** Una semana después: 47 solicitudes procesadas. 45 automáticas (96 %), 2 escaladas a humano (4 %, casos de baja confianza correctamente filtrados). Cero duplicados. Zero fallos no recuperados. Coordinadora ahorra 22 horas/semana.

**Lección.** Las 7 técnicas de la unidad encajan como piezas de Lego: trigger correcto + plataforma adecuada + integraciones limpias + patrones probados. Saltarse idempotency y retry es la causa #1 de fallos en producción.
::/practica

::practica{titulo="Cómo re-arquitecté el workflow lento en 90 minutos para que el padre no esperara 24 segundos"}
**Problema.** El workflow `inscripcion-v1.0` está en producción 3 semanas. La coordinadora reporta queja recurrente: *"el padre escribe y la respuesta tarda 20-30 segundos. Algunos cierran el chat creyendo que falló."*. La latencia es real: 24 s promedio. El motivo: las acciones (Notion + Gmail + Calendar) corren **en serie** dentro del mismo webhook.

**Paso 1 — Medir la línea base.**
Lanzo 10 inscripciones reales con timestamps. Resultado:
- Idempotency check: 0.4 s.
- Clasificación IA: 1.8 s.
- Notion append: 4.2 s (varianza alta, hasta 9 s).
- Gmail send: 3.1 s.
- Calendar create: 2.8 s.
- Slack notify: 0.6 s.
- Total mediano: 12.9 s. P95: 24 s.

**Paso 2 — Diagnóstico del cuello.**
Las 3 acciones (Notion, Gmail, Calendar) son **independientes** entre sí. Las corremos en serie por simplicidad inicial pero ninguna depende de la otra. El padre **no necesita** esperar a que todas completen — basta con saber que la solicitud quedó registrada.

**Paso 3 — Estrategia de re-arquitectura.**
- **Frontend del workflow** (lo que el padre espera): idempotency + clasificación + acuse rápido con folio. Objetivo: <3 s.
- **Backend asíncrono**: fan-out de Notion + Gmail + Calendar en paralelo. No bloquea la respuesta.
- **Notificación final**: cuando las 3 ramas terminan, fan-in y Slack a coordinadora con resumen.

**Paso 4 — Diseño nuevo en n8n.**
Workflow A (síncrono — responde al padre):
1. Webhook trigger.
2. Idempotency check.
3. Clasificación IA.
4. Generar folio (`AH-` + timestamp encoded).
5. Respond webhook 200 con folio.
6. **Trigger** workflow B con el payload + folio.

Workflow B (asíncrono — opera en background):
1. Trigger interno (recibe payload de A).
2. Fan-out paralelo:
   - Branch Notion: append + retry 3x backoff.
   - Branch Gmail: send con folio + retry 3x.
   - Branch Calendar: create event + retry 3x.
3. Fan-in (merge).
4. Slack a `#admisiones` con resumen y links.
5. Si alguna rama falló las 3 veces: Slack a `#alertas-asistente` + log error con folio para retry manual.

**Paso 5 — Implementación.**
- Construyo workflow B primero. Lo llamo desde n8n manualmente con payload de prueba — funciona, las 3 ramas paralelas terminan en ~5 s (vs los ~10 s en serie).
- Modifico workflow A para que termine en `Respond Webhook` y, después, dispare workflow B con el nodo "Execute Workflow".
- Versiono ambos: `inscripcion-sync-v2.0.0.json` y `inscripcion-async-v2.0.0.json`.

**Paso 6 — Pruebas con 10 inscripciones reales.**
- Latencia percibida por el padre (workflow A): mediana 2.4 s, P95 3.1 s. **Mejora 8.4x.**
- Latencia total backend (workflow B completo): mediana 4.8 s, P95 7.2 s.
- 10/10 sin errores.
- 10/10 folios recibidos por el padre antes de cerrar el chat.

**Paso 7 — Test de chaos.**
Apago Notion temporal. Lanzo inscripción.
- Workflow A: padre recibe folio en 2.5 s ✓.
- Workflow B: branch Notion falla 3 retries. Slack a `#alertas-asistente` con folio y razón. Branches Gmail y Calendar completan ✓.
- Reactivamos Notion. Re-ejecuto manualmente la rama Notion con el folio. Inscripción completa.

**Paso 8 — Documentación.**
Runbook actualizado: `workflows/inscripcion/runbook-v2.md`. Sección "Cuando una rama falla en producción" con pasos concretos para retry manual. ADR-014: *"separación sync/async para latencia percibida; tradeoff: complejidad operativa duplicada por monitoreo de 2 workflows"*.

**Paso 9 — Comunicación al equipo.**
Mensaje en `#admisiones`: *"Latencia mejorada de 13s a 2.5s percibida. Si una acción falla, lo verán en `#alertas-asistente` con el folio — siguen el runbook"*.

**Respuesta.** La queja desapareció en 48 h. La coordinadora reporta cero padres preguntando "¿se envió o no?". Los folios llegan rápido y las 3 acciones completan asíncronamente.

**Verificación.** A 7 días: 47 inscripciones procesadas, 100 % con folio entregado en <3 s, 2 fallos de Notion recuperados manualmente vía runbook, 0 reclamos de padres.

**Lección.** "Hacer las cosas en serie" es default cómodo pero **caro en latencia percibida**. La separación sync/async cuesta complejidad operativa, pero la paga el primer día con experiencia de usuario. La regla: lo que el usuario **debe ver inmediato** va en workflow sync; lo que puede tardar 5-30 s sin que el usuario lo note va en workflow async disparado al final del sync.
::/practica

::practica{titulo="Cómo decidí migrar de Zapier a n8n self-hosted con números, no con preferencia"}
**Problema.** La institución paga Zapier por 4 workflows: 2 con volumen alto (~5 000 tasks/mes cada uno) y 2 con volumen bajo (~500 tasks/mes). Costo mensual: $79.99 plan Professional. La dirección de TI me pide explorar si ahorramos con n8n self-hosted. Necesito decisión con datos en 1 semana.

**Paso 1 — Inventario de workflows actuales.**
- W1 — *Inscripciones nuevas* (5 200 tasks/mes): trigger Forms → Notion + Gmail + Calendar.
- W2 — *Notif solicitud info* (4 800 tasks/mes): trigger webhook → Sheet + Gmail.
- W3 — *Reporte semanal* (4 tasks/mes): schedule → query Sheets → email.
- W4 — *Alerta queja crítica* (320 tasks/mes): trigger webhook → Slack + Gmail.

Total: ~10 320 tasks/mes. Plan Professional incluye 2 000 tasks; estamos en plan superior por overage.

**Paso 2 — Costo proyectado n8n self-hosted.**
- VPS Hetzner CX21: $6/mes.
- Base de datos Postgres (incluida en VPS): $0.
- Backups: $1/mes.
- Sin límite de tasks (autohosted).
- **Total: $7/mes.**

Ahorro nominal: $79.99 − $7 = $72.99/mes = $876/año. Pero esa cuenta ignora el costo humano de migrar y mantener.

**Paso 3 — Estimar costo de migración.**
- W1: complejo (3 integraciones + auth OAuth) — 4 horas.
- W2: medio — 2 horas.
- W3: simple — 1 hora.
- W4: medio — 2 horas.
- Setup VPS + n8n Docker: 3 horas.
- Pruebas: 4 horas.
- Total: **16 horas**. A $25/h estimado: $400 one-time.

**Paso 4 — Estimar costo de mantenimiento mensual.**
- Updates n8n + dependencias: 1 h/mes.
- Monitoreo: 0.5 h/mes (logs y alertas).
- Imprevistos (downtime, etc.): 0.5 h/mes.
- Total: **2 h/mes** = $50/mes.

**Paso 5 — Total real.**
- Zapier: $79.99/mes (incluye soporte, 99.9 % SLA, sin trabajo humano).
- n8n self-host: $7 + $50 = $57/mes (sin SLA del proveedor, depende del equipo).

Ahorro mensual real: ~$23. Anual: ~$276. Migración one-time: $400. **Break-even a ~17 meses.**

**Paso 6 — Riesgos no cuantificados.**
- Riesgo A — Downtime del VPS afectando inscripciones críticas: alto si no hay redundancia.
- Riesgo B — Si yo me voy de la institución, ¿quién mantiene n8n? Conocimiento concentrado.
- Riesgo C — n8n cambia licencia o dependencias rompen.

Zapier mitiga A, B y C porque es SaaS gestionado.

**Paso 7 — Decisión documentada en ADR.**
ADR-016: *"Mantenemos Zapier por ahora. Razones: ahorro real <$300/año, break-even a 17 meses, riesgos B y C no son aceptables hoy. Re-evaluar en 12 meses cuando el equipo tenga >2 personas y el volumen exceda 20 000 tasks/mes."*

**Paso 8 — Plan de mitigación parcial.**
Aunque no migramos, **sí migramos un solo workflow** —el W3 reporte semanal— a n8n cloud free trial como prueba. Si funciona 3 meses sin problemas y el equipo crece, extendemos.

**Paso 9 — Comunicación a TI.**
Reporte de 1 página con: tabla de costos, estimación de migración, riesgos, decisión, plan parcial, fecha de revisión. La directora de TI aprueba la decisión y agradece que se haya argumentado con números, no con preferencia.

**Respuesta.** No migramos los 4 workflows. Migramos 1 como piloto. Documentamos la decisión y el disparador de revisión. Ahorro inmediato: $0; ahorro a largo plazo: depende del crecimiento.

**Verificación.** A 6 meses, el W3 funciona sin problemas en n8n free. El equipo creció a 3 personas. Re-evaluamos: ya tiene sentido migrar W4 también.

**Lección.** "Migrar a herramienta más barata" es decisión que **suena obvia** y **casi nunca lo es**. Hay que sumar costo de migración + mantenimiento + riesgo de continuidad. La regla: solo migra cuando el ahorro a 12 meses supere 3x el costo de migración **y** el riesgo de continuidad esté mitigado. El resto del tiempo, paga por SaaS y duerme tranquilo.
::/practica
