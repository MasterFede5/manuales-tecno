---
unidad: 5
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 05

> Trabajas con n8n abierto (cloud o self-hosted en Docker) y, opcionalmente, una instancia de Make o Zapier para los ejercicios comparativos.

### Sección A — Plataformas (5.1, 5.2, 5.3, 5.4)

::act-mcq{titulo="A1. Plataforma correcta por contexto"}
1. Tu institución es 100 % Microsoft 365 con compliance estricto de TI:
   - [ ] n8n self-hosted
   - [ ] Make
   - [ ] Zapier
   - [x] Power Automate

2. Tu equipo es no técnico, todas las apps son mainstream y necesitas avanzar este viernes:
   - [ ] n8n
   - [ ] Make
   - [x] Zapier
   - [ ] Power Automate

3. Quieres self-host por privacidad de datos (no enviar nada a SaaS externo):
   - [x] n8n self-hosted
   - [ ] Make
   - [ ] Zapier
   - [ ] Power Automate

4. Workflow con muchas ramas, mergers y un equipo con apetito visual:
   - [ ] n8n
   - [x] Make (Iterator/Aggregator nativos)
   - [ ] Zapier
   - [ ] Power Automate
::/act-mcq

::act-table{titulo="A2. Comparativa rápida de plataformas"}
| Característica | n8n | Make | Zapier | Power Automate |
|---|---|---|---|---|
| Self-host posible |  |  |  |  |
| Mejor para no técnicos |  |  |  |  |
| Ideal para M365 |  |  |  |  |
| Modelo de precios |  |  |  |  |
| Iterator/Aggregator nativo |  |  |  |  |
| Code nodes |  |  |  |  |
::/act-table

### Sección B — Webhooks, APIs y triggers (5.5)

::act-fill{titulo="B1. Anatomía de un webhook autenticado"}
Un webhook seguro lleva siempre:

- Método _____________ (no GET para acciones).
- Header de _____________: `Authorization: Bearer ____________`.
- Validación del _____________ contra schema antes de procesar.
- Respuesta _____________ rápido para no bloquear al emisor.
- _____________ key calculado a partir del body para evitar duplicados.
::/act-fill

::act-mcq{titulo="B2. Schedule vs Webhook vs Polling"}
1. Quieres procesar un evento **al momento** de ocurrir en la app origen:
   - [x] Webhook (la app origen empuja el evento)
   - [ ] Schedule
   - [ ] Polling
   - [ ] Manual

2. La app origen no soporta webhooks pero tiene API de listado:
   - [ ] Webhook
   - [ ] Schedule cada 1 min
   - [x] Polling con marcador de "último procesado"
   - [ ] Manual

3. Quieres reporte semanal lunes 8:00 sin importar si hubo eventos:
   - [ ] Webhook
   - [x] Schedule
   - [ ] Polling
   - [ ] Manual
::/act-mcq

### Sección C — Integraciones (5.6)

::act-match{titulo="C1. App → caso institucional típico"}
| App | Caso institucional |
|---|---|
| 1. Notion | a) Calendario de exámenes y eventos |
| 2. Airtable | b) BD de alumnos con vistas filtradas multi-rol |
| 3. Gmail | c) Documentación viva del Asistente |
| 4. Google Calendar | d) Comunicaciones a familias |
| 5. Slack | e) Alertas a coordinación |
| 6. Sheets | f) Logs y reportes |
::/act-match

::act-tf{titulo="C2. Mitos de las integraciones"}
1. Una credencial OAuth con permiso de admin de toda la org es la mejor práctica. ( ) ____________________________________________
2. Notion API tiene rate limit, así que tu workflow debe manejarlo. ( ) ____________________________________________
3. Si el endpoint devuelve 429, debes esperar y reintentar con backoff exponencial. ( ) ____________________________________________
4. Una credencial puede vivir en el código fuente del workflow exportado. ( ) ____________________________________________
::/act-tf

### Sección D — Patrones reutilizables (5.7)

::act-match{titulo="D1. Patrón → problema que resuelve"}
| Patrón | Problema |
|---|---|
| 1. Router | a) Llamadas API que pueden fallar transitoriamente |
| 2. Fan-out / Fan-in | b) Acciones irreversibles que requieren validación humana |
| 3. Retry con backoff | c) Procesamiento duplicado del mismo evento |
| 4. Idempotency | d) Entradas heterogéneas que requieren rutas distintas |
| 5. Approval loop | e) Múltiples acciones independientes a ejecutar en paralelo |
::/act-match

::act-order{titulo="D2. Orden de patrones en un workflow institucional"}
[ ] Approval loop si la confianza < umbral
[ ] Idempotency check al recibir el evento
[ ] Router por categoría
[ ] Fan-out a 3 acciones paralelas
[ ] Retry con backoff dentro de cada acción
[ ] Fan-in para construir respuesta final
[ ] Notificación + respond webhook
::/act-order

::act-fill{titulo="D3. Idempotency con clave compuesta"}
Una clave de idempotency robusta combina **datos del evento** con **ventana temporal**. Para "inscripción nueva", una clave razonable es:

```
idempotency_key = sha256( ____________ + "|" + ____________ + "|" + ____________ )
```

Donde los 3 componentes son: ____________ del solicitante, ____________ truncado al ____________, y _____________ del módulo. Si la misma clave llega 2 veces, devolves _____________ sin re-ejecutar.
::/act-fill

### Sección E — Diseño y producción

::act-case{titulo="E1. Caso — diseñas el workflow 'cambio de horario'" lineas=14}
La coordinadora quiere un workflow para procesar solicitudes de cambio de horario: el padre escribe al Asistente, este detecta intención, valida el cupo en el grupo destino, agenda entrevista de ajuste si aplica, notifica al profesor del grupo origen y al del destino, actualiza la base, y manda confirmación al padre. Lista los nodos del workflow en orden, identifica los 3-5 patrones que aplicas, marca los puntos de fallo más probables y propón mitigación de cada uno.
::/act-case

::act-mcq{titulo="E2. Modos de falla más comunes"}
1. Tu workflow funcionó 30 días en sandbox. En producción falla 1/5 ejecuciones. La causa más probable:
   - [ ] El código del workflow tiene un bug
   - [x] Rate limits o credenciales OAuth caducadas en producción
   - [ ] El modelo IA cambió
   - [ ] El servidor está caído

2. Tu workflow tiene **branch paralelas** (Notion + Gmail + Calendar). Una falla, las otras dos completan. ¿Decisión correcta?
   - [ ] Hacer rollback de las completadas
   - [x] Continuar con compensación: registrar en error log + alerta + retry diferido
   - [ ] Reintentar todo el workflow
   - [ ] Ignorar
::/act-mcq

::act-mindmap{titulo="E3. Tu suite de workflows" centro="WORKFLOWS ALBATROS v1" nodos_primarios=6 nodos_secundarios=12}
Las 6 ramas: (1) workflows en producción con su trigger, (2) integraciones activas con sus credenciales, (3) patrones aplicados con dónde, (4) métricas semanales (corridas, éxito, fallos), (5) runbooks documentados, (6) próximas mejoras. Datos concretos, no abstractos.
::/act-mindmap

---

## Clave de respuestas

**A1.** 1-d · 2-c · 3-a · 4-b.

**A2.** Sugerencia (acepta variantes razonables): n8n self-host sí · Make mejor visual · Zapier mejor para no técnicos · Power Automate ideal para M365. Iterator nativo: Make. Code nodes: n8n y Make. Modelo de precios: n8n por ejecución/auto-host, Make por operaciones, Zapier por tasks, PA por usuario.

**B1.** POST · autenticación · token · payload · 200 · idempotency.

**B2.** 1-a · 2-c · 3-b.

**C1.** 1-c · 2-b · 3-d · 4-a · 5-e · 6-f.

**C2.** 1) Falso — usa principio de menor privilegio: una credencial por scope mínimo. 2) Verdadero. 3) Verdadero. 4) Falso — credenciales viven en el gestor de credenciales/secrets, nunca en el JSON exportado.

**D1.** 1-d · 2-e · 3-a · 4-c · 5-b.

**D2.** Orden: Idempotency check → Approval loop si confianza baja → Router por categoría → Fan-out → Retry con backoff → Fan-in → Notificación + respond.

**D3.** Sugerencia: `email`, `timestamp` truncado al `minuto`, `nombre del módulo`. Devuelves `200 OK con folio existente`.

**E1.** Respuesta libre. Buena solución incluye: webhook con auth → idempotency → clasificador IA con confianza → router (cambio horario / otra cosa) → validación cupo en Sheet/Notion → si cupo OK: fan-out (notif profesor origen, notif profesor destino, update BD, agenda entrevista, mail confirmación al padre) → fan-in → respond. Patrones: idempotency, router, fan-out/fan-in, retry, approval cuando cupo justo o no hay. Modos de falla: rate limit Notion, mail rebote, calendar conflict — mitigaciones: retry + fallback + alerta humana.

**E2.** 1-b · 2-b.

**E3.** Mapa libre. Si una rama tiene <2 ítems concretos, esa dimensión aún no está madura.
