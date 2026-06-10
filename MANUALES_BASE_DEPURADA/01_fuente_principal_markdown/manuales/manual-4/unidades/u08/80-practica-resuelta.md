---
unidad: 8
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 08

::practica{titulo="Configurar Claude Desktop con 6 servidores MCP institucionales y resolver los 5 casos del subtema 8.5 en una tarde"}
**Problema.** 
- Tomar Claude Desktop *fresh*.
- Configurar 6 servidores MCP institucionales (filesystem, memory, time, github, notion, postgres readonly).
- Validar su funcionamiento y ejecutar los 5 casos del 8.5.
- Documentar tiempos y ahorro. Tiempo objetivo: 4 horas.

**Paso 1 — Datos.**
- Mac M2 con Claude Desktop instalado (plan Pro).
- Tokens: GitHub PAT (read), Notion API key, credenciales Postgres readonly y Slack bot.
- Carpeta `/Users/yo/AlbatrosDocs/` (publico, confidencial, plantillas).
- Repo `albatros/asistente-prompts` y Notion DB "Solicitudes admisión 2026".
- BD Postgres con `alumnos`, `matricula` y `seguimiento_bimestre`.

**Paso 2 — Estrategia.**
- Editar `claude_desktop_config.json` con los servidores.
- Validar cada servidor de forma incremental.
- Ejecutar y medir los 5 casos de uso.
- Documentar y compartir con la coordinadora académica.

**Paso 3 — Configuración (45 min).**

```json
{
  "mcpServers": {
    "fs-publico": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/yo/AlbatrosDocs/publico"]
    },
    "fs-confidencial": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/yo/AlbatrosDocs/confidencial"]
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
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://readonly:xxx@localhost/asistente"]
    }
  }
}
```

- Reinicio Claude Desktop. 
- La barra inferior muestra "7 MCP servers connected" (6 configurados + 1 interno de memory).

::interioriza
Imagina que Claude es un nuevo empleado y los servidores MCP son sus "llaves maestras". 
En lugar de darle todas las llaves juntas y rogar que no se equivoque de puerta, pruebas una llave a la vez. 
Si la llave de Postgres no gira, sabes exactamente dónde está el problema sin revisar todo el llavero.
::/interioriza

**Paso 4 — Validación incremental (30 min).**
- **fs-publico:** "lista los archivos disponibles" → OK 12 archivos visibles.
- **memory:** "anota: hoy es lunes" → OK.
- **time:** "qué hora es" → OK.
- **github:** "busca prompts en albatros/asistente-prompts" → OK 4 prompts encontrados.
- **notion:** "busca en BD Solicitudes" → OK.
- **postgres:** "muestra 5 alumnos" → OK readonly funciona.

::pausa
**¿Por qué probamos cada servidor con una instrucción tan simple?**
1. Para evitar que un error complejo oculte un fallo de conexión.
2. Para agotar rápidamente nuestros tokens.
3. Porque Claude no puede procesar comandos largos.

*Respuesta: 1. Confirmamos la conexión pura antes de meter lógica compleja.*
::/pausa

**Paso 5 — Casos de Uso.**

- **Caso 1: Minuta automática (40 min).**
  - Acción: Claude lee plantilla del *fs*, estructura minuta y guarda en *fs*.
  - Resultado: `2026-04-29-consejo.md` creado. Tiempo: 7 min (Ahorro: 83 min).

- **Caso 2: Ticketing (30 min).**
  - Acción: Clasifica queja, crea página en Notion, postea en Slack.
  - Resultado: Flujo completado. Tiempo: 4 min (Ahorro: 26 min).

- **Caso 3: Buscador prompts (15 min).**
  - Acción: Busca prompt en GitHub y lo aplica a una queja real.
  - Resultado: Ejecución directa. Tiempo: 3 min (Ahorro: 12 min).

- **Caso 4: Comunicación contextualizada (45 min).**
  - Acción: Cruza datos del *fs*, identifica padres y redacta correos. 
  - Resultado: Correos en *clipboard*. Tiempo: 12 min (Ahorro: 78 min).

- **Caso 5: Reporte BD (30 min).**
  - Acción: Consulta Postgres, calcula tendencias, y crea un reporte `.md`.
  - Resultado: Gráfica generada. Tiempo: 8 min (Ahorro: ~232 min).

**Documentación y Resultados (15 min).**
- Creación de `MCP-Setup-Albatros-v1.0.md` para la coordinadora.
- Adopción de Claude Desktop como cliente principal (ADR-009).
- **Ahorro total estimado:** 6.5 horas en 5 casos. ¡ROI en la primera tarde!

**Verificación final y Lección.**
- Coordinadora capacitada en 30 min. 
- Logró operar minutas, reportes y tickets autónomamente.
- **Lección:** MCP convierte la "IA institucional" en realidad. 
- La fricción actual ya no es técnica, sino organizacional.
::/practica
