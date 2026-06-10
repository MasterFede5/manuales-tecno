---
unidad: 6
seccion: implementacion
paginas_objetivo: 6
---

::implementacion{titulo="Implementación Albatros — Agente del Asistente Institucional con safeguards completos"}
**Objetivo.** Construir, desplegar y operar el **agente oficial del Asistente Institucional Albatros** para resolver casos no rutinarios, con tools curados, los 7 safeguards activos, runbook documentado, monitoreo en producción y golden set de validación. Tras esta unidad, tu Asistente deja de ser solo workflows + RAG y se convierte en sistema autónomo bajo control.

**¿Por qué hacerla?** Los workflows de U5 cubren rutina; el agente cubre lo no anticipable. Sin agente, casos atípicos se acumulan sobre humanos. Con agente bajo safeguards, tu Asistente alcanza autonomía controlada.

---

### Materiales y recursos

- Plataforma: n8n AI Agent (recomendado por integración con U5) o LangGraph self-hosted (si quieres más control).
- API keys: Anthropic Claude Opus 4.7 + Sonnet 4.6, Notion, Calendar, Slack.
- Repo Git con carpeta `agents/`.
- 12-15 horas en 4 sesiones.
- 2 stakeholders para validación.

### Pasos

#### Sesión 1 — Diseño y arquitectura (3 h)

1. **45 min — Casos a cubrir.** Lista de 5-7 tipos de casos no rutinarios reales del backlog.
2. **45 min — Arquitectura.** Decide: reactivo, deliberativo, jerárquico, multi-agente. Para v1.0: deliberativo casi siempre.
3. **45 min — Tools curados.** Lista de 5-8 tools con nombres, descripciones explícitas, schemas estrictos.
4. **45 min — Safeguards.** Configura los 7 (max_iter, max_cost, alertas, approval para destructivos, whitelist destinos, logging, health check).

#### Sesión 2 — Construcción en n8n (4 h)

5. **30 min — Setup.** Workflow nuevo "Agente Asistente v1.0".
6. **2 h — AI Agent node + tools.** Cada tool como sub-workflow llamado.
7. **60 min — Approval loops.** Para `send_email` y `schedule_event` con Slack interactive.
8. **30 min — Logging.** Append a Google Sheet "Agent_Logs" con timestamp, iteración, tool, input, output.

#### Sesión 3 — Pruebas exhaustivas (3 h)

9. **60 min — Golden set.** 10 casos: 5 felices, 2 borde, 1 prompt injection, 1 escalación, 1 imposible.
10. **60 min — Ejecución.** Lanzas los 10 con monitor en vivo.
11. **30 min — Análisis costos.** Tokens, USD, tiempo por caso. Proyección mensual.
12. **30 min — Ajustes.** Refina prompts, descripciones de tools, safeguards basado en hallazgos.

#### Sesión 4 — Documentación, ADR, despliegue canary (2-3 h)

13. **30 min — Runbook.** Documenta operación, alarmas, qué hacer si entra en estado roto.
14. **30 min — ADR-008.** Adopción del agente con safeguards.
15. **30 min — Política.** Whitelist de destinos email, aprobaciones requeridas.
16. **60 min — Canary.** Despliega 10 % del tráfico no rutinario al agente; mantén workflows de U5 para el 90 %.

::visual{tipo="ilustracion" descripcion="Mockup del ecosistema con agente operando: en el centro, un cuadro 'Agente Asistente v1.0' con icono cerebro azul. Alrededor: 6 tools (RAG, Notion, Calendar, Email, Slack, Workflow U5) en círculo. Líneas hacia los 7 safeguards mostrados como escudos pequeños etiquetados (max_iter, max_cost, alertas, approval, whitelist, logging, health). Bajo el agente, dashboard de monitoreo con métricas reales del canary (10 % tráfico, costo $19/mes, 12 ejecuciones/día). Estilo blueprint Albatros." paginas=1}

---

### Entregable

1. **Workflow del agente** desplegado y activable.
2. **Documento de tools** (1 pp): lista, descripciones, schemas, permisos.
3. **Runbook** (1 pp): operación, alarmas, fallback.
4. **ADR-008**: adopción del agente.
5. **Reporte de golden set**: 10 casos con resultados, costo, tiempo, lecciones.
6. **Dashboard de monitoreo**: Sheet o LangFuse con stats en vivo.
7. **Política de uso** (1 pp): qué hace, qué no hace, quién aprueba qué.

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Tipo de agente justificado | sin claridad | uno elegido | con ADR de razón |
| Tools | sin schemas | schemas básicos | schemas + descripciones explícitas + permisos |
| Safeguards | <3 | 5 de 7 | 7 de 7 + evidencia |
| Golden set | 3 casos | 6-7 | 10+ con prompt injection |
| Costo controlado | sin monitor | medido | proyección mensual y alarmas |
| Documentación | básica | runbook | runbook + ADR + política |
| Despliegue | en local | demo | canary 10 % con métricas |

### Hitos intermedios

| Día | Hito | Evidencia |
|---|---|---|
| Día 1 | Lista de 5-7 casos no rutinarios reales | inventario en `docs/` |
| Día 2 | ADR de arquitectura (deliberativo vs reactivo) | `docs/decisiones/ADR-NNN.md` |
| Día 3 | Sistema prompt + tools schemas | archivos en `agents/v1.0.0/` |
| Día 5 | 7 safeguards configurados | screenshots + ADR de defaults |
| Día 7 | Golden de 10 casos ejecutado | reporte en `tests/` |
| Día 9 | Análisis de costo proyectado | tabla en runbook |
| Día 10 | Runbook + ADR-008 | docs publicados |
| Día 12 | Canary 10 % activado | log de canary |
| Día 14 | Reporte de 7 días de canary | métricas + decisión continuar |

### Reto bonus extendido (3 retos)

**Bonus 1 — Multi-agente para una tarea compleja.** Toma una tarea de tu Asistente que requiere perspectivas divergentes (ej. redactar comunicado controvertido). Diseña un sistema multi-agente con 3 roles (proponente, escéptico, sintetizador). Compáralo contra un agente único en costo, calidad y tiempo.

**Bonus 2 — Red team de tu propio agente.** Diseña 5 prompts adversariales para tu agente (prompt injection, abuso de tool, induce-loop, exfiltración de sesión, acción destructiva) y registra qué hizo. Refuerza los safeguards que fallaron.

**Bonus 3 — Cost dashboard.** Construye un Artifact (U3) que muestre el costo del agente día por día, con alerta si supera presupuesto. Comparte con dirección. La métrica que no se ve es la métrica que crece sin control.

### Próximo paso después de esta unidad

En **U7 — IA Local y Open Source**, vas a explorar **operar el agente sin proveedor cloud**: Ollama + Llama 3.1 + Open WebUI. Para casos donde la institución requiere soberanía total de datos (salud, gubernamental), el agente migra a infraestructura propia.
::/implementacion

::albatros{titulo="Reto complementario — incident response simulado de tu agente" tipo="reto" tiempo="30 min"}
**Pregunta detonadora.** Si tu agente quemara $40 USD en 3 horas mañana, ¿en cuántos minutos lo detendrías y cuánto te tomaría diagnosticar?

**Lo que harás.**
1. Inventa un incidente plausible (loop, prompt injection, tool roto, credenciales caducas).
2. En tu agente real (o sandbox), provoca el incidente.
3. Mide tiempo desde alerta hasta detención.
4. Mide tiempo desde detención hasta diagnóstico.
5. Diseña 3 cambios estructurales que reducirían ambos tiempos a la mitad.
6. Documenta en `docs/incident-001-simulado.md`.

**Entregable.** Documento de 1 página con timeline, tiempos medidos y 3 cambios.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Realismo del incidente | trivial | plausible | derivado de logs reales |
| Medición | informal | tiempos aproximados | timestamps precisos |
| Cambios estructurales | parches | 2-3 | 3 con dueño y plazo |
::/albatros
