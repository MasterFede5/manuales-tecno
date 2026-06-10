---
unidad: 5
seccion: cierre
paginas_objetivo: 2
---

## Cierre y autoevaluación — Unidad 05

Cerraste la unidad de Workflows e Integraciones No-Code. Ahora puedes:

1. **Operar n8n** self-hosted con nodos AI nativos para flujos de IA sin código.
2. **Comparar** n8n, Make, Zapier y Power Automate y elegir según ecosistema institucional.
3. **Diseñar** Webhooks, schedules y polling con criterio de costo y latencia.
4. **Integrar** con Notion, Airtable, Google Workspace y Microsoft 365 según donde viven los datos.
5. **Aplicar** los 5 patrones (Router, Fan-out/Fan-in, Retry-Backoff, Idempotency, Approval) en producción.
6. **Construir** una biblioteca interna de templates reutilizables.

> **Frase puente.** Tus workflows ejecutan **decisiones predefinidas**. La siguiente unidad da el salto: agentes que **deciden por sí mismos** qué tools usar, en qué orden, hasta lograr un objetivo. La Unidad 6 te lleva de la automatización al verdadero cerebro autónomo del Asistente.

---

### Autoevaluación (rúbrica de 5 niveles)

| Saber | 1 — Inicial | 2 | 3 — Suficiente | 4 | 5 — Excelente |
|---|---|---|---|---|---|
| **n8n** | nunca abrí | un workflow simple | self-host operativo | con nodos AI | producción con monitoreo |
| **Make / Zapier / Power Automate** | desconozco | uso uno | conozco los 3 | elijo según caso | matriz documentada |
| **Webhooks y APIs** | confuso | concepto general | webhook con auth | con retry y validación | con monitoreo y alertas |
| **Integraciones M365 / Google / Notion / Airtable** | uso uno | conozco varios | integro 2-3 | con single source of truth | mapa institucional |
| **Patrones reutilizables** | ninguno | aplico Retry | aplico 3 | biblioteca compartida | adoptados por todo el equipo |
| **Workflow en producción** | demo solo | uno corriendo | 3+ con monitoreo | con runbooks | con dashboard de métricas |

### Pregunta de cierre

> Tu workflow de inscripciones lleva 4 semanas estable. Procesa 80 solicitudes/mes. Súbitamente la API de Notion duplica precios. **Diseña** tu plan en 5 pasos numerados: (1) cómo lo detectas, (2) qué métricas miras, (3) cómo evalúas alternativas (Airtable, Sheets, Postgres), (4) cómo migras sin downtime, (5) qué runbook actualizas.

### Conexión con la siguiente unidad

En **U6 — Agentes de IA**, vas a llevar contigo **los 3 workflows de esta unidad como herramientas** que los agentes podrán invocar. La diferencia clave: en U5 tú decidiste el orden de las acciones; en U6 será **el agente** quien decide.
