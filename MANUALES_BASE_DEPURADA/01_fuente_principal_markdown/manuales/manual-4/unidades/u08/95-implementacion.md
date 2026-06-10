---
unidad: 8
seccion: implementacion
paginas_objetivo: 4
---

::implementacion{titulo="Implementación Albatros — MCP Hub Institucional con servidores activos"}
**Objetivo.** Establecer el **MCP Hub Institucional** del Asistente Albatros: configuración Claude Desktop con 8-10 servidores MCP, política de tokens y permisos, capacitación de 5 staff, golden set de 10 casos resueltos vía MCP, y documentación operativa para mantenimiento. La meta: que MCP sea la capa "default" desde la cual el staff opera.

**¿Por qué hacerla?** MCP es la pieza que **transforma Claude Desktop de chat en sistema operativo institucional**. Sin esta capa, el staff sigue copiando-pegando entre apps. Con ella, conversa una vez y las acciones se distribuyen por los sistemas que ya tienes.

---

### Materiales y recursos

- 5 licencias Claude Pro (uno por staff piloto).
- Tokens: GitHub PAT, Notion API, Slack Bot, Postgres readonly, Brave Search.
- Acceso al repo institucional `albatros/asistente-prompts`.
- Notion DB "Solicitudes admisión 2026".
- Drive institucional con permisos.
- 12-15 horas distribuidas en 4 sesiones.

### Pasos

#### Sesión 1 — Diseño y políticas (3 h)

1. **45 min — Inventario de sistemas.** Listar qué sistemas tu staff toca diariamente (Drive, Notion, Slack, BD, GitHub, etc.).
2. **45 min — Mapeo a servidores MCP.** Para cada sistema: ¿hay servidor oficial? ¿comunitario? ¿custom?
3. **45 min — Política de tokens.** Cuáles, con qué permisos, dónde guardarlos (keychain, env, secret manager).
4. **45 min — Política de permisos.** Para cada servidor: read-only vs read-write, qué requiere approval.

#### Sesión 2 — Configuración y validación (3 h)

5. **30 min — Setup de Claude Desktop** en máquina principal.
6. **90 min — Configurar 8-10 servidores** con tokens y rutas correctas.
7. **45 min — Validar incrementalmente.** Probar cada servidor con prompt simple.
8. **15 min — Documentar config maestra** en formato template (sin secretos).

#### Sesión 3 — Golden set y refinamiento (3 h)

9. **60 min — Golden set.** 10 casos de uso reales del staff piloto.
10. **90 min — Ejecutar y medir.** Cada caso con tiempo y resultado.
11. **30 min — Refinar.** Ajustar permisos o servidores según hallazgos.

#### Sesión 4 — Adopción y operación (3-4 h)

12. **45 min — Capacitación piloto.** Sesión grupal de 30 min + 15 min por persona.
13. **45 min — Distribución.** Configurar Claude Desktop en máquinas de los 5 staff.
14. **45 min — Documentación final.**
    - `MCP-Setup-Albatros.md`: guía de instalación.
    - `MCP-Política.md`: tokens, permisos, dónde reportar incidentes.
    - `MCP-Casos.md`: 10 casos del golden con instrucciones reproducibles.
15. **30 min — Plan de monitoreo.** Métricas semanales: uso por servidor, errores, tiempo ahorrado.

::visual{tipo="ilustracion" descripcion="Mockup del MCP Hub Institucional Albatros: en el centro logo del Asistente. Alrededor, 10 servidores MCP en círculo (filesystem-publico, filesystem-confidencial, github, slack, notion, postgres-readonly, gdrive, gcalendar, brave-search, memory). Líneas hacia 5 staff con sus laptops y avatares. Bajo todo, un panel de operación con métricas de la semana (consultas exitosas, ahorro horas, alertas). Estilo blueprint Albatros con paleta azul + acentos por servidor." paginas=1}

---

### Entregable

1. **Config maestra** (template + 5 instalaciones activas).
2. **Documento `MCP-Setup-Albatros.md`** (1-2 pp).
3. **Política `MCP-Política.md`** con tokens, permisos, contingencia (1 pp).
4. **Catálogo `MCP-Casos.md`** con 10 casos resueltos y reproducibles (2-3 pp).
5. **Reporte de adopción** a 1 semana: 5 staff capacitados, casos ejecutados, métricas.
6. **ADR-009** Adopción de MCP como capa default del staff.

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Cantidad de servidores | 3 | 6-8 | 10+ activos |
| Cobertura de sistemas | 1-2 | 4-5 | todos los sistemas core |
| Política de tokens | hardcoded | env vars | secret manager + rotación |
| Permisos | overpowered | read-only por default | granular con approval |
| Golden set | 3 casos | 6-8 | 10+ con métricas |
| Capacitación | 1 persona | 3 | 5+ con seguimiento |
| Documentación | mínima | setup básico | setup + política + casos + ADR |
| Adopción a 1 semana | privado | piloto usa | métricas de tiempo ahorrado |

### Próximo paso después de esta unidad

En **U9 — Contenido Especializado de Alto Nivel**, usarás todo lo construido (RAG, agentes, MCP) para que el Asistente **produzca contenido educativo profesional**: cursos online, whitepapers, datasets sintéticos, reportes técnicos. El último episodio antes de la gobernanza (U10).
::/implementacion
