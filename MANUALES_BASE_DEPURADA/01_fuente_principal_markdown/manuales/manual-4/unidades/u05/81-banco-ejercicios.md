---
unidad: 5
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 05

> Trabajas con n8n abierto (cloud o self-hosted en Docker).
> Opcionalmente, usa Make o Zapier para ejercicios comparativos.

::interioriza
**Analogía: Las plataformas como vehículos**
- **Zapier:** Es un taxi. Fácil, te lleva al instante, pero caro a la larga.
- **Make:** Es un coche automático. Muy visual, cómodo y te permite ir a muchos lados sin ser mecánico.
- **n8n (self-hosted):** Es construir tu propio coche deportivo en tu garaje. Requiere saber mecánica, pero te ahorras el taxi de por vida.
- **Power Automate:** Es el blindado de la empresa oficial. Seguro pero rígido.
::/interioriza

::pausa{}
**Reflexiona rápido:**
- ¿Por qué un colegio con datos sensibles elegiría "construir su coche" (n8n)?
- Si necesitas una campaña de admisiones urgente y no hay técnicos, ¿qué tomas?
::/pausa{}

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

::interioriza
**Analogía: El Webhook es un cartero**
- **Polling:** Tú vas a correos cada 5 minutos a preguntar: "¿Hay cartas?".
- **Webhook:** El cartero te deja la carta en el buzón apenas llega.
- **Autenticación:** Es el candado del buzón para que nadie meta cartas falsas.
::/interioriza

::act-fill{titulo="B1. Anatomía de un webhook autenticado"}
Un webhook seguro lleva siempre:

- Método _____________ (no GET para acciones).
- Header de _____________: `Authorization: Bearer ____________`.
- Validación del _____________ contra schema antes de procesar.
- Respuesta _____________ rápida para no bloquear al emisor.
- _____________ key calculado del body para evitar duplicados.
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
1. Credencial OAuth con permiso admin global es la mejor práctica. ( ) _____________
2. Notion API tiene rate limit, tu workflow debe manejarlo. ( ) _____________
3. Si el endpoint devuelve 429, esperas y reintentas con backoff. ( ) _____________
4. Una credencial puede vivir en el código fuente exportado. ( ) _____________
::/act-tf

### Sección D — Patrones reutilizables (5.7)

::act-match{titulo="D1. Patrón → problema que resuelve"}
| Patrón | Problema |
|---|---|
| 1. Router | a) Llamadas API que pueden fallar transitoriamente |
| 2. Fan-out / Fan-in | b) Acciones irreversibles que requieren validación |
| 3. Retry con backoff | c) Procesamiento duplicado del mismo evento |
| 4. Idempotency | d) Entradas que requieren rutas distintas |
| 5. Approval loop | e) Múltiples acciones independientes en paralelo |
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
Una clave robusta combina **datos del evento** con **ventana temporal**.
Ejemplo para "inscripción nueva":

```
idempotency_key = sha256( ________ + "|" + ________ + "|" + ________ )
```

- ________ del solicitante.
- ________ truncado al ________.
- ________ del módulo.
- Si la clave se repite, devuelves ________ sin re-ejecutar.
::/act-fill

### Sección E — Diseño y producción

::act-case{titulo="E1. Caso — diseñas el workflow 'cambio de horario'" lineas=14}
- El padre solicita cambio al Asistente.
- El sistema valida cupos, agenda entrevista y notifica a los profesores.
- Tarea: Lista los nodos del workflow en orden.
- Identifica 3-5 patrones aplicados y cómo mitigar puntos de falla.
::/act-case

::act-mcq{titulo="E2. Modos de falla más comunes"}
1. Funcionó 30 días en sandbox. En producción falla 1/5. Causa probable:
   - [ ] El código del workflow tiene un bug
   - [x] Rate limits o credenciales OAuth caducadas
   - [ ] El modelo IA cambió
   - [ ] El servidor está caído

2. Falla 1 de 3 ramas paralelas (Notion+Gmail+Calendar). Decisión correcta:
   - [ ] Hacer rollback de las completadas
   - [x] Continuar, registrar error log, alerta y retry diferido
   - [ ] Reintentar todo el workflow
   - [ ] Ignorar
::/act-mcq

::act-mindmap{titulo="E3. Tu suite de workflows" centro="WORKFLOWS ALBATROS v1" nodos_primarios=6 nodos_secundarios=12}
6 ramas a detallar con datos concretos:
- (1) Workflows en prod y triggers.
- (2) Integraciones y credenciales.
- (3) Patrones y su ubicación.
- (4) Métricas semanales.
- (5) Runbooks documentados.
- (6) Próximas mejoras.
::/act-mindmap

---

## Clave de respuestas

**A1.** 1-d · 2-c · 3-a · 4-b.

**A2.** n8n self-host sí · Make visual · Zapier no técnicos · Power Automate M365. Iterator nativo: Make. Code nodes: n8n y Make. Precio: n8n auto-host, Make operaciones, Zapier tasks.

**B1.** POST · autenticación · token · payload · 200 · idempotency.

**B2.** 1-a · 2-c · 3-b.

**C1.** 1-c · 2-b · 3-d · 4-a · 5-e · 6-f.

**C2.** 1) Falso — usa menor privilegio. 2) Verdadero. 3) Verdadero. 4) Falso — nunca en el JSON exportado.

**D1.** 1-d · 2-e · 3-a · 4-c · 5-b.

**D2.** Orden: Idempotency → Approval loop → Router → Fan-out → Retry → Fan-in → Notificación.

**D3.** `email`, `timestamp` truncado al `minuto`, `nombre del módulo`. Devuelve `200 OK con folio existente`.

**E1.** Webhook con auth → idempotency → clasificador IA → router → validación cupo → fan-out (notif, BD, agenda) → fan-in → respond. Patrones: idempotency, router, fan-out/fan-in. Fallos: rate limit, mail rebote. Mitigación: retry, alerta humana.

**E2.** 1-b · 2-b.

**E3.** Mapa libre. Si una rama tiene <2 ítems concretos, aún no está madura.
