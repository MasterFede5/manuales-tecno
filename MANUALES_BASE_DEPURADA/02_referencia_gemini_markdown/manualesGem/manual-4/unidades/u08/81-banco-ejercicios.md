---
unidad: 8
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 08

> Banco de práctica para Model Context Protocol (MCP): concepto y arquitectura cliente-servidor, catálogo de servidores, configuración de Claude Desktop, ChatGPT con Connectors y casos de uso reales del Asistente Institucional. Privilegia ejercicios de **decisión de servidor**, **lectura de config** y **diseño de flujo**. Resuelve antes de mirar la clave.

---

### Bloque A — Concepto y arquitectura MCP (8.1)

::act-mcq{titulo="Fundamentos de MCP"}
1. La analogía más precisa para MCP es:
   - [ ] Una red social
   - [x] El estándar USB para periféricos (un solo conector, muchos dispositivos)
   - [ ] Una base de datos relacional
   - [ ] Un compilador

2. En la arquitectura MCP, el componente que ejecuta tools y expone resources es:
   - [ ] El cliente
   - [x] El servidor MCP
   - [ ] El LLM
   - [ ] El sistema operativo

3. Para tu Asistente con datos sensibles institucionales, el transport recomendado es:
   - [ ] WebSocket público
   - [ ] HTTP/SSE expuesto a internet
   - [x] stdio (subproceso local)
   - [ ] FTP

4. Antes de MCP (Q3 2024), el problema central era:
   - [x] Cada cliente LLM tenía su propio mecanismo de integración → fragmentación
   - [ ] Los modelos no soportaban tool calling
   - [ ] Las APIs eran demasiado caras
   - [ ] Las regulaciones lo prohibían
::/act-mcq

::act-fill{titulo="Las 3 capacidades que expone un servidor MCP"}
Un servidor MCP expone tres tipos de capacidades:

1. **_____________** — funciones invocables que producen efecto en el mundo. Ejemplos: `commit_git`, `send_slack_message`, `query_db`.
2. **_____________** — contenido leíble, estado del mundo. Ejemplos: `file://path`, `notion://page/{id}`, `db://table/row`.
3. **_____________** — plantillas reutilizables. Ejemplo: "resumir reunión usando contexto de [resource]".

El cliente LLM descubre las capacidades con `_____________` y `_____________`, decide qué invocar y maneja la respuesta. MCP fue lanzado por _____________ en _____________ de 2024 y en 2025 lo adoptaron OpenAI, Cursor, Windsurf y otros.
::/act-fill

---

### Bloque B — Catálogo de servidores (8.2)

::act-match{titulo="Servidor MCP → caso institucional"}
| Servidor | Caso del Asistente |
|---|---|
| 1. filesystem | a) Notificar canal de admisiones cuando hay solicitud nueva |
| 2. github | b) Búsqueda web actualizada de mejores prácticas pedagógicas |
| 3. slack | c) Acceder a documentos institucionales en `/data/asistente-docs/` |
| 4. postgres | d) Consultar prompts versionados (U1) y abrir issues de mejora |
| 5. brave-search | e) Memoria persistente del agente (perfiles, decisiones pasadas) |
| 6. memory | f) Consulta directa al sistema de calificaciones interno (read-only) |
::/act-match

::act-table{titulo="Catálogo mínimo del Asistente — completa"}
| Servidor | Tools clave | Permiso requerido | Riesgo principal |
|---|---|---|---|
| filesystem | | | |
| github | | | |
| slack | | | |
| postgres | | | |
| memory | | | |
::/act-table

::act-tf{titulo="V/F sobre adopción de servidores"}
1. Lo recomendable es activar 15 servidores el primer día para ver qué tools se aprovechan más. ( ) ____________
2. Un Slack token con acceso a TODOS los canales es un riesgo de prompt injection. ( ) ____________
3. Si tu sistema interno no tiene servidor MCP, NO puedes integrarlo: hay que esperar a que la comunidad lo construya. ( ) ____________
4. Construir un servidor MCP simple toma 1-2 horas para alguien con conocimiento básico de TypeScript o Python. ( ) ____________
5. El plan recomendado de adopción arranca con filesystem + memory + time, los 3 más simples. ( ) ____________
::/act-tf

---

### Bloque C — Claude Desktop con MCP (8.3)

::act-mcq{titulo="Claude Desktop en producción institucional"}
1. La diferencia técnica más importante entre Claude.ai (web) y Claude Desktop es:
   - [ ] Solo Desktop tiene Opus 4.7
   - [x] Solo Desktop tiene MCP nativo (acceso a archivos y sistemas locales)
   - [ ] Solo Desktop puede usar artifacts
   - [ ] Solo Desktop tiene login con SSO

2. La ruta del archivo de configuración en macOS es:
   - [ ] `/etc/claude/config`
   - [ ] `/usr/local/claude.json`
   - [x] `~/Library/Application Support/Claude/claude_desktop_config.json`
   - [ ] `~/.claude.json`

3. El "approval flow" de Claude Desktop:
   - [ ] Aprueba todo automáticamente
   - [x] Pide aprobación visual antes de acciones de escritura/destructivas; lecturas suelen auto-aprobarse
   - [ ] Solo aprueba con MFA
   - [ ] No existe en Desktop
::/act-mcq

::act-order{titulo="Pasos para configurar Claude Desktop con un servidor MCP"}
[ ] Editar `claude_desktop_config.json` con la sección `mcpServers`
[ ] Cerrar y reabrir Claude Desktop
[ ] Login con cuenta Claude (Pro recomendado para Opus 4.7)
[ ] Verificar el indicador "MCP servers connected" en la barra
[ ] Descargar Claude Desktop de claude.ai/download e instalar
[ ] Probar primer prompt invocando un tool del servidor configurado
::/act-order

::act-tf{titulo="V/F sobre seguridad de Claude Desktop con MCP"}
1. Hardcodear tokens en `claude_desktop_config.json` y compartir el archivo es práctica aceptada. ( ) ____________
2. Configurar `filesystem` con path `/` (raíz) le da a Claude acceso a todo el disco. ( ) ____________
3. Activar logging de tool calls es recomendable, especialmente al inicio del despliegue. ( ) ____________
4. Claude Desktop es la mejor opción para usuarios no técnicos como una coordinadora académica. ( ) ____________
5. Los servidores MCP corren como subprocesos aislados (sandbox) lanzados por Claude Desktop. ( ) ____________
::/act-tf

---

### Bloque D — ChatGPT con Connectors (8.4)

::act-mcq{titulo="Claude+MCP vs ChatGPT+Connectors"}
1. Diferencia conceptual clave:
   - [ ] Connectors son MCP renombrado por OpenAI
   - [x] Connectors son integraciones first-party de OpenAI con OAuth corporativo; MCP es estándar abierto
   - [ ] MCP es propietario de Anthropic; Connectors son open source
   - [ ] Ambos son lo mismo, distintos nombres

2. Si tu institución vive 100 % en Microsoft 365 y el equipo no es técnico:
   - [ ] Forzar Claude Desktop con MCP custom
   - [x] ChatGPT Enterprise con Connectors mainstream (M365, Outlook, SharePoint)
   - [ ] Ninguna de las dos opciones
   - [ ] Construir un cliente propio

3. La privacidad-default es mejor en:
   - [x] Claude Desktop con servidores MCP locales (datos no salen del dispositivo)
   - [ ] ChatGPT Connectors (siempre cloud OpenAI)
   - [ ] Ambos son equivalentes
   - [ ] ChatGPT, porque tiene cifrado de extremo a extremo
::/act-mcq

::act-table{titulo="Matriz de decisión 2x2"}
| | Equipo técnico | Equipo no técnico |
|---|---|---|
| **Ecosistema mainstream (Drive, M365, Slack)** | | |
| **Sistemas custom (BD propietaria, ERP interno)** | | |
::/act-table

::act-fill{titulo="El camino híbrido institucional"}
Las instituciones serias usan **ambos clientes**:

- **ChatGPT con _____________** para tareas mainstream del staff (Drive, Calendar, Slack) con OAuth corporativo y _____________ enterprise grade.
- **Claude Desktop con _____________** para tareas con sistemas internos custom, servidores MCP locales y máxima _____________.

Anti-patrón: configurar los _____________ OAuth tokens en ambos clientes — replicas exposición y la auditoría se vuelve confusa. Cada usuario tiene los dos clientes y el gasto se distribuye según uso real.
::/act-fill

---

### Bloque E — Casos de uso reales (8.5)

::act-match{titulo="Caso de uso → servidores MCP que combina"}
| Caso | Servidores activos |
|---|---|
| 1. Minuta automática del consejo académico | a) postgres + filesystem |
| 2. Ticketing al instante desde Slack | b) github + filesystem |
| 3. Buscador de prompts versionados | c) filesystem + gdrive + memory |
| 4. Comunicación contextualizada multi-sistema | d) notion + slack + time |
| 5. Reporte vivo de matrícula | e) gmail/slack + gdrive + gcalendar |
::/act-match

::act-tf{titulo="V/F sobre los patrones que emergen"}
1. Los 5 casos comparten una característica: cada uno usa solo 1 servidor MCP. ( ) ____________
2. El "approval flow" es esencial para acciones destructivas como envío de correos a padres de familia. ( ) ____________
3. La memoria entre pasos viene del servidor `memory`, que da knowledge graph en memoria. ( ) ____________
4. El tiempo manual ahorrado en estos casos es típicamente 80-95 %. ( ) ____________
5. Para acciones complejas multi-paso conviene usar un agente (U6) que **invoca MCP como tools**, no MCP solo. ( ) ____________
::/act-tf

::act-case{titulo="Diseña tu sexto caso institucional" lineas=10}
Diseña un **6° caso de uso real** específico para tu institución. Debe incluir: a) **dolor concreto** que resuelve (ej: "el departamento de cobranza pasa 3 h por semana cruzando pagos con lista de morosos"), b) **2-4 servidores MCP** combinados, c) **flujo paso a paso** (qué tool invoca el modelo en cada momento, en qué orden), d) **dónde aplica approval flow** (acciones destructivas o irreversibles), e) **tiempo manual ahorrado estimado** vs. tiempo con MCP.
::/act-case

::act-order{titulo="Plan de adopción institucional — ordena las semanas"}
[ ] + slack y gmail con approval flow
[ ] filesystem + memory para uso individual de power users
[ ] Servidor MCP custom para tu sistema de calificaciones
[ ] + github para staff técnico
[ ] + postgres con readonly para reportes
[ ] + notion para ticketing
::/act-order

---

## Clave de respuestas

**Bloque A — MCQ:** 1-b · 2-b · 3-c · 4-a. **Fill:** Tools · Resources · Prompts · `list_tools` · `list_resources` · Anthropic · noviembre.

**Bloque B — Match:** 1-c · 2-d · 3-a · 4-f · 5-b · 6-e. **Tabla:** filesystem (read_file, write_file, list_directory / path permitido / lectura de todo el disco si path = `/`) · github (search_repositories, create_issue, create_pull_request / GITHUB_PERSONAL_ACCESS_TOKEN / token con scope demasiado amplio) · slack (slack_post_message, slack_search_messages / SLACK_BOT_TOKEN + SLACK_TEAM_ID / acceso a TODOS los canales por default) · postgres (query / connection string con permisos / connection con permiso de admin en lugar de readonly) · memory (create_entities, add_observations, search_nodes / sin token / fugas a través de logs si no se cura). **V/F:** 1-F (comprometerse a 1-2 servidores y crecer) · 2-V · 3-F (puedes construir tu propio servidor) · 4-V · 5-V.

**Bloque C — MCQ:** 1-b · 2-c · 3-b. **Order:** descargar e instalar → login → editar config JSON → cerrar y reabrir Desktop → verificar indicador → probar primer prompt. **V/F:** 1-F (usar env vars o secret manager) · 2-V · 3-V · 4-F (Coordinadora probablemente prefiera Open WebUI o ChatGPT Connectors con UI guiada) · 5-V.

**Bloque D — MCQ:** 1-b · 2-b · 3-a. **Tabla:** mainstream + técnico = cualquiera (preferir el que ya pague la institución) · mainstream + no-técnico = ChatGPT Connectors · custom + técnico = Claude Desktop+MCP (servidor custom propio) · custom + no-técnico = camino híbrido (Connectors para mainstream + alguien técnico opera Claude+MCP para casos custom). **Fill:** Connectors · audit logs · MCP · privacidad/soberanía · mismos.

**Bloque E — Match:** 1-c · 2-d · 3-b · 4-e · 5-a. **V/F:** 1-F (los casos combinan 2-4 servidores; MCP brilla con multi-fuente) · 2-V · 3-V · 4-V · 5-V. **Caso:** ejemplo libre, debe declarar dolor + servidores + flujo + approval + tiempo ahorrado. **Order:** semana 1 filesystem + memory · semana 2 + github · semana 3 + slack y gmail · semana 4 + notion · mes 2 + postgres readonly · mes 3 servidor MCP custom.
