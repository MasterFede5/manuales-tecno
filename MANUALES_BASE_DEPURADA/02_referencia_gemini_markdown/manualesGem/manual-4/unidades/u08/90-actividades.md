---
unidad: 8
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 08

::act-mcq{titulo="Repaso conceptual"}
1. MCP es comparable a USB porque:
   - [ ] Ambos son protocolos de hardware
   - [x] Ambos estandarizan integraciones que antes eran fragmentadas
   - [ ] Ambos son de Anthropic
   - [ ] Ambos requieren cable

2. Para un Asistente Institucional con datos sensibles, el transporte MCP preferible es:
   - [x] stdio (local, subproceso)
   - [ ] HTTP/SSE (servidor compartido)
   - [ ] WebSocket
   - [ ] FTP

3. El servidor MCP `filesystem` con argumento `/` (raíz) es:
   - [ ] Recomendado para máxima flexibilidad
   - [x] Peligroso: el modelo accede a todo el disco
   - [ ] Lo mismo que apuntar a una carpeta específica
   - [ ] Solo lectura por defecto

4. ChatGPT Connectors vs Claude Desktop+MCP: la diferencia clave es:
   - [ ] Pricing
   - [ ] Velocidad
   - [x] Apertura del ecosistema y servidores custom
   - [ ] Cantidad de tools

5. Si tu institución tiene un sistema legacy SIN servidor MCP, lo más razonable es:
   - [ ] Esperar
   - [ ] Forzar al staff a copiar-pegar
   - [x] Construir un servidor MCP custom (1-2 horas para developer)
   - [ ] Cambiar de cliente
::/act-mcq

::act-table{titulo="Completa la tabla — caso del Asistente y servidores MCP"}
| Caso | Servidores MCP necesarios | Riesgo principal |
|---|---|---|
| Minuta automática del consejo |  |  |
| Ticketing al instante |  |  |
| Búsqueda de prompts versionados |  |  |
| Comunicación masiva con padres |  |  |
| Reporte vivo de matrícula |  |  |
| Onboarding de docente nuevo |  |  |
::/act-table

::act-match{titulo="Relaciona el servidor MCP con su uso típico"}
| Servidor | Uso típico |
|---|---|
| 1. filesystem | a) Buscar mensajes pasados, postear notificaciones |
| 2. github | b) Leer y escribir archivos locales |
| 3. slack | c) Versionar prompts y configuraciones |
| 4. notion | d) Memoria persistente del agente |
| 5. postgres | e) Consultas read-only a sistema interno |
| 6. memory | f) Tickets y wiki institucional |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Cualquier cliente que soporte MCP puede usar todos los servidores MCP existentes. ( ) ____________________________________________

2. Es buena práctica configurar el servidor MCP filesystem apuntando a `/` para máxima flexibilidad. ( ) ____________________________________________

3. ChatGPT en 2025 tiene soporte MCP completo equivalente a Claude Desktop. ( ) ____________________________________________

4. Tokens hardcoded en `claude_desktop_config.json` son aceptables si el archivo no se comparte. ( ) ____________________________________________

5. Construir un servidor MCP custom requiere semanas de desarrollo. ( ) ____________________________________________
::/act-tf

::act-order{titulo="Ordena los pasos para adoptar MCP en tu institución"}
[ ] Documentar setup y compartir con coordinadora
[ ] Configurar tokens y credenciales seguramente
[ ] Editar claude_desktop_config.json
[ ] Validar cada servidor incrementalmente
[ ] Identificar 3-5 casos donde MCP aporta valor inmediato
[ ] Capacitar al equipo con sesión de 30 min
[ ] Elegir 6-8 servidores apropiados al caso
[ ] Reiniciar Claude Desktop
::/act-order

::albatros{titulo="Despliega tu primer setup MCP institucional con 5 casos resueltos" tipo="taller" tiempo="3 h"}
**Pregunta detonadora.** Si tu Asistente pudiera leer el Drive, GitHub, BD y Slack de tu institución sin que tú escribieras una sola línea de código de integración, ¿qué tareas resolverías el primer día?

**Lo que harás.**
1. Instala Claude Desktop (Mac o Windows).
2. Configura **6 servidores MCP** en `claude_desktop_config.json`: filesystem (apuntando a carpeta restringida), memory, time, github (con read-only token), notion o postgres, brave-search.
3. Reinicia y valida que los 6 estén "connected".
4. Ejecuta los **5 casos del subtema 8.5** adaptados a tu institución (puedes simular si no tienes ecosistema completo).
5. Mide tiempo de cada caso vs estimación manual previa.
6. Documenta config + lecciones aprendidas en repo.
7. Comparte config (sin tokens, con .env.example) con tu equipo.
8. Capacita a 1 persona en 30 min y mide qué tan rápido la adopta.

**Materiales.** Mac o Windows, Claude Desktop Pro, tokens de los servicios, 3 horas.

**Entregable.**
- `claude_desktop_config.json` (o template sin secretos).
- Reporte de los 5 casos con cifras de tiempo (1-2 pp).
- Documento de capacitación de 30 min para equipo (1 pp).
- Captura mostrando 6 servers connected y un caso ejecutado.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Setup completo | 2-3 servers | 4-5 | 6+ funcionando |
| Casos ejecutados | 1-2 | 3 | 5 con tiempos medidos |
| Documentación | mínima | config | config + capacitación + ADR |
| Seguridad | tokens hardcoded | env vars | secret manager o keychain |
| Capacitación | privado | mostrado | 1+ persona adoptó con métrica |
::/albatros
