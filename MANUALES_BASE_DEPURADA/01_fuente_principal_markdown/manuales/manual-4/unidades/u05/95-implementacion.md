---
unidad: 5
seccion: implementacion
paginas_objetivo: 4
---

::implementacion{titulo="Implementación Albatros — Suite de 3 workflows institucionales en producción"}
**Objetivo.** Construir y poner en producción **3 workflows críticos** del Asistente Institucional Albatros: 1) Inscripción nueva, 2) Solicitud de información, 3) Resumen semanal automático. Cada uno con patrones aplicados, monitoreo activo, runbook documentado y métricas de uso medidas a 1 semana.

**¿Por qué hacerla?** Los 3 workflows son el **músculo operativo** del Asistente: convierten conversaciones en acciones reales. Sin ellos, las unidades 1-4 son demos; con ellos, el Asistente entrega valor diariamente.

---

### Materiales y recursos

- Plataforma elegida: n8n self-hosted (recomendado) o Make/Zapier según institución.
- Credenciales: Notion, Airtable o Sheets, Gmail, Calendar, Slack, Anthropic.
- Repo Git con carpeta `workflows/` para versionado.
- 12-15 horas distribuidas en 4 sesiones.

### Pasos

#### Sesión 1 — Setup de plataforma (2 h)

1. **30 min — Instalación.** n8n self-hosted con Docker, o cuenta cloud Make.
2. **30 min — Credenciales.** Configurar todas las API keys en Credentials manager.
3. **30 min — Política de naming.** Acordar prefijos (`[Asist] inscripcion`, `[Asist] info`, `[Asist] reporte`) y carpetas.
4. **30 min — Templates de patrones.** Importar (o crear) sub-workflows reutilizables: Idempotency, Retry-Backoff, Approval.

#### Sesión 2 — Workflow 1: Inscripción nueva (4 h)

5. Aplicar la práctica resuelta de la unidad. Llevar a producción.
6. Pruebas exhaustivas: 5 casos felices + 3 casos de borde (duplicado, baja confianza, API caída).

#### Sesión 3 — Workflow 2: Solicitud de información (3 h)

7. Trigger: webhook desde el Asistente RAG (cuando categoría = "info").
8. Acciones: consultar RAG, formular respuesta, enviar correo, registrar conversación en Airtable, ofrecer follow-up en 48h con schedule.
9. Patrones: Retry-Backoff + Idempotency.

#### Sesión 4 — Workflow 3: Reporte semanal automático (2 h)

10. Trigger: Schedule cada lunes 8:00.
11. Acciones: query Airtable de la semana, query Sheets de logs, query métricas LangFuse, generar resumen con Claude, enviar a `#reporte-semanal` Slack y email a dirección.
12. Patrones: Fan-out de queries paralelas + Fan-in para resumen.

#### Sesión 5 — Documentación, monitoreo y socialización (2-3 h)

13. **Runbook** por workflow: qué hace, qué falla, cómo arreglar.
14. **Dashboard** de monitoreo (LangFuse, Helicone o Sheet con stats).
15. **Junta** con equipo para presentar y aprobar.
16. **Cadencia de revisión:** mensual.

::visual{tipo="ilustracion" descripcion="Mockup del ecosistema en operación: en el centro, un cuadro 'Workflows Albatros' con 3 sub-cuadros (Inscripción, Información, Reporte). De cada uno salen flechas a las plataformas externas (Notion, Airtable, Gmail, Calendar, Slack). Bajo el ecosistema, dashboard de monitoreo con métricas reales (tasa éxito, latencia, costo, alertas). A la izquierda, repo Git con tags v1.0.0 por cada workflow. Estilo blueprint Albatros." paginas=1}

---

### Entregable

1. **3 workflows** funcionando en producción con URLs/triggers documentados.
2. **3 runbooks** (1 página cada uno).
3. **Dashboard** de métricas (puede ser Sheet, LangFuse, o Artifact).
4. **Repo `workflows/`** con JSONs exportados, CHANGELOG y tags semver.
5. **Reporte de adopción** a 1 semana (1-2 pp): solicitudes procesadas, errores, ahorro de tiempo, incidentes.

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Cantidad de workflows | 1 | 2 | 3+ |
| Patrones aplicados | sin patrones | 1-2 | 3+ por workflow |
| Manejo de errores | sin retry | retry básico | retry + fallback + alerta |
| Documentación | mínima | runbook básico | runbook completo + diagrama |
| Versionado | sin commit | export + commit | tag + CHANGELOG por release |
| Monitoreo | invisible | logs informales | dashboard con KPIs |
| Adopción equipo | privado | mostrado | adoptado con métricas |

### Hitos intermedios

| Día | Hito | Evidencia |
|---|---|---|
| Día 1 | n8n setup + credenciales | screenshot de Credentials manager poblado |
| Día 2 | Templates de patrones reutilizables | sub-workflows en `templates/` |
| Día 3 | Workflow 1 (inscripción) en sandbox | JSON exportado |
| Día 5 | Workflow 1 con pruebas pasadas | reporte 1 página |
| Día 7 | Workflow 2 (información) operativo | JSON exportado |
| Día 9 | Workflow 3 (reporte) operativo | JSON exportado |
| Día 10 | 3 runbooks publicados | en `docs/runbooks/` |
| Día 12 | Dashboard de monitoreo activo | URL + capturas |
| Día 14 | Junta de adopción + cadencia mensual | acta |

### Reto bonus extendido (3 retos)

**Bonus 1 — Async fan-out.** Si tus workflows tardan más de 5 s desde el punto del usuario, refactoriza siguiendo la práctica resuelta de re-arquitectura sync/async. Mide latencia percibida antes/después y documenta en ADR.

**Bonus 2 — Test de chaos automatizado.** Crea un workflow `chaos-test` que cada lunes apague durante 5 minutos una integración (Notion o Gmail), lance 3 inscripciones, y verifique que: (a) el padre recibe folio, (b) la rama caída registra el fallo, (c) la alerta llega a `#alertas-asistente`. Si algo falla, abre issue automático. Esto te da confianza de que tu manejo de errores funciona.

**Bonus 3 — Métricas de ROI.** Construye un workflow Schedule semanal que cuente: (a) cuántas inscripciones se procesaron automáticamente, (b) cuántos minutos de trabajo humano ahorraste asumiendo 30 min/inscripción manual, (c) cuántos fallos hubo. Manda reporte a dirección. Es el dato que justifica seguir invirtiendo en automatización.

### Próximo paso después de esta unidad

En **U6 — Agentes de IA**, vas a evolucionar de workflows fijos a **agentes** que deciden qué tools usar según la situación. Los workflows de esta unidad serán las **herramientas** que esos agentes invoquen.
::/implementacion

::albatros{titulo="Reto complementario — auditas un workflow heredado de tu institución" tipo="reto" tiempo="30 min"}
**Pregunta detonadora.** Tu institución probablemente tiene workflows Zapier o Power Automate viejos. ¿Sabes qué hacen, quién los mantiene, qué pasaría si fallaran mañana?

**Lo que harás.**
1. Pide acceso a la cuenta de Zapier/Make/Power Automate de tu institución.
2. Lista todos los workflows activos.
3. Para cada uno: nombre, trigger, destino, dueño actual, última edición, ¿documentado?, ¿tiene retry?
4. Identifica los 3 más críticos (mayor impacto si fallan).
5. Para esos 3, escribe un mini-runbook de 5 líneas: qué hace, qué pasa si falla, cómo se reanuda.
6. Comparte el inventario con TI y agenda revisión semestral.

**Entregable.** Hoja de inventario + 3 mini-runbooks + acta de la revisión.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cobertura | <50 % de workflows | todos listados | listados con dueño |
| Identificación de críticos | informal | top 3 | top 3 con impacto cuantificado |
| Runbooks | ausentes | uno | tres con plan de fallback |
| Adopción | privado | compartido | con cadencia agendada |
::/albatros
