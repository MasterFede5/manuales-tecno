---
unidad: 8
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 08

::practica{titulo="Configurar Claude Desktop con 6 servidores MCP institucionales y resolver los 5 casos del subtema 8.5 en una tarde"}
**Problema.** Tomar Claude Desktop fresh, configurar 6 servidores MCP institucionales (filesystem, memory, time, github, notion, postgres readonly), validar que cada uno funciona, ejecutar los 5 casos del 8.5, documentar tiempos y ahorro. Tiempo objetivo: 4 horas.

**Paso 1 — Datos.**
- Mac M2 con Claude Desktop instalado, plan Pro.
- Tokens disponibles: GitHub PAT (read), Notion API key, credenciales Postgres readonly.
- Carpeta institucional `/Users/yo/AlbatrosDocs/` con 3 sub-carpetas (publico, confidencial, plantillas).
- Repo GitHub `albatros/asistente-prompts` con prompts versionados de U1.
- Notion DB "Solicitudes admisión 2026" con propiedades definidas.
- BD Postgres con tablas `alumnos`, `matricula`, `seguimiento_bimestre`.
- Slack token bot.

**Paso 2 — Estrategia.**
1. Editar `claude_desktop_config.json` con los 6 servidores.
2. Validar cada servidor de forma incremental (no todos a la vez).
3. Ejecutar uno por uno los 5 casos del subtema 8.5.
4. Medir tiempo, errores, aprovechamiento.
5. Documentar y compartir config con coordinadora académica.

**Paso 3 — Configuración (45 min).**

```json
{
  "mcpServers": {
    "fs-publico": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem",
               "/Users/yo/AlbatrosDocs/publico"]
    },
    "fs-confidencial": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem",
               "/Users/yo/AlbatrosDocs/confidencial"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "time": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-time"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxx"}
    },
    "notion": {
      "command": "npx",
      "args": ["-y", "mcp-notion-server"],
      "env": {"NOTION_API_KEY": "ntn_xxx"}
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres",
               "postgresql://readonly:xxx@localhost/asistente"]
    }
  }
}
```

Reinicio Claude Desktop. La barra inferior muestra "7 MCP servers connected".

**Paso 4 — Validación incremental (30 min).**

1. fs-publico: "lista los archivos disponibles" → OK 12 archivos visibles.
2. memory: "anota: hoy es lunes" → OK.
3. time: "qué hora es" → OK.
4. github: "busca prompts en albatros/asistente-prompts" → OK 4 prompts encontrados.
5. notion: "busca en BD Solicitudes" → OK.
6. postgres: "muestra 5 alumnos" → OK readonly funciona.

**Paso 5 — Caso 1: Minuta automática (40 min).**

Pego transcripción cruda de junta del consejo (ya transcribí afuera con Whisper). Pido a Claude generar minuta con plantilla. Claude lee plantilla (fs), genera minuta estructurada, escribe nuevo doc en fs, anota decisiones en memory.

Resultado: minuta de 2 páginas en `minutas/2026-04-29-consejo.md`. Tiempo: 7 min.

**Paso 6 — Caso 2: Ticketing (30 min).**

Mensaje de prueba de "padre" (yo simulando). Claude clasifica, invoca notion.create_page, postea en slack #admisiones (vía workflow n8n callable que tengo). Tiempo: 4 min.

**Paso 7 — Caso 3: Buscador prompts (15 min).**

"Dame el prompt de clasificador-quejas más reciente y úsalo con esta queja real." Claude busca en GitHub, lo aplica directamente. Tiempo: 3 min.

**Paso 8 — Caso 4: Comunicación contextualizada (45 min).**

Pido reunión con padres de 5 alumnos en riesgo. Claude lee Excel en fs-confidencial, identifica padres, genera correos personalizados, espera mi aprobación. Aprobado, pero **no envió** (gmail server no estaba configurado todavía; lo dejé para v2). Genera correos en clipboard para enviar manualmente. Tiempo: 12 min.

**Paso 9 — Caso 5: Reporte BD (30 min).**

Pido reporte de matrícula. Claude consulta postgres, calcula tendencias, genera reporte en fs como `.md`, crea artifact con gráfica recharts. Tiempo: 8 min.

**Paso 10 — Documentación (15 min).**

- Documento `MCP-Setup-Albatros-v1.0.md` con instrucciones para coordinadora.
- ADR-009: Adopción de Claude Desktop+MCP como cliente principal del staff.

**Respuesta.** Sistema MCP institucional v1.0 operativo. 6 servidores funcionando + 1 (memory) extra. 5 casos del 8.5 ejecutados con éxito. Tiempo total: 4h 15min (cerca del objetivo). Ahorros estimados:
- Caso 1 (minuta): 7 min vs 90 min = 83 min ahorrados.
- Caso 2 (ticket): 4 min vs 30 min = 26 min.
- Caso 3 (prompt): 3 min vs 15 min = 12 min.
- Caso 4 (comunicación): 12 min vs 90 min = 78 min.
- Caso 5 (reporte): 8 min vs 4 horas (pidiendo a TI) = ~232 min.

Total ahorrado en 5 casos = 6.5 horas. ROI a la primera tarde de uso.

**Verificación final.** Comparto config con coordinadora académica. Le tomo 30 min capacitarla. Una semana después: ella ejecutó 11 minutas, 8 reportes y 14 tickets sin pedirme nada. Sistema validado.

**Lección.** MCP es el catalizador que convierte la promesa de "IA institucional" en realidad operativa. Las 5 técnicas (concepto, servidores, Claude Desktop, ChatGPT alternativo, casos reales) encajan en un setup de 4 horas. La friction de adoption ya no es técnica: es organizacional.
::/practica
