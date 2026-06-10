---
unidad: 8
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Tu Asistente conectado en una tarde: Claude Desktop + 6 servidores MCP

> Este taller convierte la teoría de MCP en una **estación operativa**: en 60 minutos configuras Claude Desktop con 6 servidores reales y resuelves dos de los cinco casos institucionales del subtema 8.5. Sales con un Asistente que lee documentos, ejecuta queries y notifica por Slack — sin escribir una sola línea de integración custom.

::albatros{titulo="6 servidores MCP, 2 casos resueltos, 60 minutos" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si tu coordinadora te pidiera mañana que el Asistente lea el Drive del consejo, abra issues en GitHub y notifique en Slack los acuerdos, ¿podrías habilitarlo en una tarde? Este taller te demuestra que sí, sin programar nada custom.

**Lo que harás (12 pasos).**

1. **Instala Claude Desktop (3 min).** Descarga de claude.ai/download para tu SO (macOS o Windows). Login con cuenta Pro (recomendado para acceso a Opus 4.7 y mayor cuota de tools). Verifica versión ≥ la última estable de 2025.

2. **Genera tokens y credenciales mínimas (10 min).** Antes de tocar el config, prepara 3 secretos con scope mínimo: a) `GITHUB_PERSONAL_ACCESS_TOKEN` con permiso de un solo repo institucional (read + issues), b) `SLACK_BOT_TOKEN` (xoxb-…) limitado a 2 canales (`#admisiones` y `#asistente-prueba`), c) usuario `readonly` en una base Postgres de prueba o un archivo SQLite de calificaciones de muestra. Documenta cada token en una nota privada.

3. **Crea la carpeta de trabajo (2 min).** En tu home crea `~/AlbatrosDocs/` con dos subcarpetas: `publico/` (con 3 documentos institucionales de ejemplo: reglamento de becas, calendario, plantilla de minuta) y `confidencial/` (vacía o con un solo doc de prueba). El `filesystem` solo verá `publico/` en la primera fase.

4. **Configura los 6 servidores MCP (10 min).** Edita `claude_desktop_config.json` (macOS: `~/Library/Application Support/Claude/`; Windows: `%APPDATA%\Claude\`) con el JSON que monta: `filesystem-publico` apuntando a `~/AlbatrosDocs/publico`, `memory`, `time`, `github` con tu token, `slack` con el bot token y team ID, y `postgres` o `sqlite` con tu connection string read-only. Pega el JSON con `env` para los tokens (NO en `args`).

5. **Reinicia y verifica (3 min).** Cierra Claude Desktop. Reábrelo. Confirma que en la barra inferior aparece "🔌 6 MCP servers connected". Si alguno no carga, abre los logs (`~/Library/Logs/Claude/mcp*.log`) y arregla el server fallido antes de seguir.

6. **Prompt de descubrimiento (3 min).** Tu primer prompt: *"Lista los servidores MCP que tienes disponibles, los tools de cada uno y un ejemplo de uso por servidor."* Confirma que Claude responde con los 6 servidores y sus tools. Si menciona menos de 6, hay un servidor fallido.

7. **Caso 1 ejecutado — minuta automática (8 min).** Coloca en `~/AlbatrosDocs/publico/` un audio (o transcripción .txt) de prueba de 3 minutos llamado `consejo-prueba.txt` y la plantilla `minutas/template.md`. Pídele a Claude: *"Lee `consejo-prueba.txt`, aplica la plantilla `minutas/template.md` y guarda la minuta en `minutas/2026-04-30-consejo.md`. Anota las decisiones tomadas en memoria con tag #consejo-2026-04-30."* Aprueba las acciones de escritura cuando se te pidan. Verifica que el archivo nuevo existe y que el resumen ejecutivo es coherente.

8. **Caso 2 ejecutado — ticketing al instante (8 min).** Pídele a Claude: *"Simula que un padre escribió este mensaje por Slack: 'Quiero información sobre la inscripción para el ciclo 2027'. Crea un ticket en GitHub Issues del repo `asistente-tickets` con clasificación `inscripción`, asigna a `@coordinador-academico`, plazo 48 h. Notifica en `#admisiones` con el folio y la liga al issue."* Aprueba el envío de Slack solo después de revisar el texto. Captura screenshot del issue y del mensaje en Slack.

9. **Auditoría de seguridad (5 min).** Revisa que: a) ningún servidor tiene path `/` o `~` (sólo el subset acordado), b) los tokens viven en `env` y no en plain text en `args`, c) `postgres` está con usuario `readonly` y no admin, d) Slack bot está limitado a 2 canales. Documenta hallazgos en `auditoria-mcp.md` con remediaciones pendientes.

10. **Plan de approval por riesgo (3 min).** En `politica-mcp.md` registra qué acciones requieren approval explícito (write_file fuera de `borradores/`, send_message en cualquier canal, query con `INSERT/UPDATE/DELETE`) y cuáles auto-aprobar (read_file, list_directory, search). Esta política se vuelve la guía del staff.

11. **Plan de adopción para tu institución (3 min).** Llena la plantilla del subtema 8.5: semana 1 filesystem + memory · semana 2 + github · semana 3 + slack y gmail · semana 4 + notion · mes 2 + postgres readonly · mes 3 servidor MCP custom. Marca quién instala, quién capacita y qué métrica usarás (tiempo ahorrado por caso, # de tickets generados, # de minutas asistidas).

12. **Demo y entrega (2 min).** Graba una pantalla de 2 minutos resolviendo Caso 1 + Caso 2 en una sola conversación. La grabación es tu evidencia de despliegue. Súbela junto al `auditoria-mcp.md`, `politica-mcp.md` y los archivos generados al repo del proyecto.

**Materiales.**
- Claude Desktop (macOS o Windows) con cuenta Pro recomendado.
- Node.js ≥ 18 instalado (para `npx` que ejecuta los servidores oficiales).
- Cuenta GitHub con un repo institucional de prueba.
- Workspace Slack con bot configurado (Slack admin) y al menos 2 canales.
- Base SQLite o Postgres de prueba con datos sintéticos (ej: 50 registros de matrícula simulada).
- Editor (VS Code) para tocar el `claude_desktop_config.json` con resaltado JSON.
- Grabador de pantalla (CleanShot, OBS, ScreenStudio) para la demo final.

**Entregable.**
1. **`claude_desktop_config.json`** con los 6 servidores configurados (tokens **redactados** en el commit, vivos solo en local).
2. **Captura de pantalla** del indicador "🔌 6 MCP servers connected".
3. **Caso 1 resuelto** — archivo `minutas/2026-04-30-consejo.md` generado por el Asistente.
4. **Caso 2 resuelto** — link al GitHub Issue creado + screenshot de la notificación en Slack `#admisiones`.
5. **`auditoria-mcp.md`** — checklist de seguridad con hallazgos y remediaciones.
6. **`politica-mcp.md`** — política de approval por nivel de riesgo (auto-aprobar / requerir aprobación / prohibido).
7. **Demo de 2 min** grabada mostrando los dos casos en una sola conversación de Claude Desktop.
8. **Reflexión escrita (200 palabras)** — qué integración custom evitaste construir, cuánto tiempo ahorras al año en tareas mainstream, qué servidor MCP custom construirías como siguiente paso.

**Rúbrica corta.**

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Servidores configurados | 1–2 | 3–4 | 6 conectados y verificados |
| Seguridad de tokens | tokens en plain text | env vars | env vars + scopes mínimos + auditoría documentada |
| Caso 1 (minuta) | flujo manual | minuta generada con errores menores | minuta generada + memoria persistente con tags |
| Caso 2 (ticketing) | issue manual | issue + Slack sin approval | issue + Slack con approval explícito y folio único |
| Política y plan | sin documentar | política básica | política completa + plan de adopción institucional con métricas |
| Demo | no entregada | entregada sin narración | demo de 2 min con narración del flujo y los servidores activos |
| Reflexión | superficial | menciona ahorros | identifica integración custom evitada y siguiente servidor a construir |

**Tip Albatros.** El verdadero ROI de MCP no es el primer caso que resuelves — es el **vigesimoquinto**. Cuando tu staff descubre que cada nueva pregunta se resuelve "agregando un servidor que ya existe" en lugar de pedirle un proyecto al área de TI, la velocidad institucional cambia de fase. Empieza con 6 servidores y dos casos para que el equipo lo vea con sus ojos; el tercer mes ya nadie pregunta "¿se podrá conectar?", todos preguntan "¿qué servidor uso?".
::/albatros
