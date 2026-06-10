---
unidad: 6
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 06

::practica{titulo="Construir el primer agente del Asistente con n8n AI Agent + 5 tools + safeguards completos"}
**Problema.** 
- Construir agente para casos no rutinarios (cambios de turno, becas, quejas).
- Plataforma: n8n AI Agent node con Claude Sonnet 4.6.
- Restricciones: 5 tools, 7 safeguards, 3 horas de tiempo.

**Paso 1 — Datos.**
- 5 casos reales: 3 cambios de turno, 1 beca, 1 queja.
- 3 Workflows de U5 como "tools" (`inscripcion-nueva`, etc.).
- API keys de Anthropic, Notion, Calendar y Slack.

**Paso 2 — Estrategia.**
- **Agente deliberativo:** (plan-and-execute) para casos interdependientes.
- **5 tools curados:** RAG, calendario, ticket Notion, evento, email.
- **Safeguards:** max_iterations=10, max_cost=$2, approvals.
- **Logging:** Cada paso a Sheet "Agent_Logs" desde un Sandbox paralelo.

::interioriza
Imagina un chef con recetas estrictas (workflows) y un sous-chef (agente).
Al sous-chef solo le das 5 utensilios específicos y un límite de presupuesto.
Si la receta falla, el sous-chef avisa al chef en lugar de improvisar a ciegas.
::

**Paso 3 — System Prompt.**
```xml
<role>Resuelves casos no rutinarios de admisiones.</role>
<rules>Usa plan-and-execute, cita RAG, no inventes datos, escala a humano.</rules>
<tools>search_kb, search_calendar, create_notion_ticket, schedule_calendar_event, send_institutional_email.</tools>
```

**Paso 4 & 5 — Tools y Safeguards.**
- Cada tool es un sub-workflow expuesto al agente.
- Wrapper de tokens corta ejecución a los $2 USD.
- Approval loop manda Slack a la coordinadora para acciones críticas.
- Health check hace ping a APIs antes de iniciar.

**Paso 6 — Pruebas.**
- **Caso simple:** Cambio de turno, plan generado, ticket creado. ($0.18)
- **Caso conflicto:** Replanifica horario. ($0.31)
- **Caso beca:** Alcanza iteraciones, escala a humano correctamente.
- **Caso injection:** Rechaza mandar datos a externo y genera alerta.

**Conclusión.**
- Costo promedio: $0.24/caso.
- Ahorro de 5 horas a la semana.
- Un Sonnet con 7 safeguards supera a un Opus sin ellos.

::pausa{titulo="Analiza el éxito"}
¿Por qué escalar a un humano en la iteración 11 se considera un éxito del agente?
- Porque demuestra que el *safeguard* de `max_iterations` funciona.
- Porque evita alucinaciones o bucles infinitos gastando presupuesto.
::
::/practica

::practica{titulo="Cómo construí los 5 tools mínimos del agente eligiendo cuáles descartar"}
**Problema.** 
- El equipo propuso 18 tools iniciales.
- Se seleccionaron solo 5. ¿Por qué descartar las otras 13?

**Paso 1 — Criterios de Selección.**
- **Necesidad:** Pedido en ≥3 casos reales.
- **Riesgo:** Efectos colaterales bajos o fáciles de revertir.
- **Aislamiento:** No replica otra función.
- **Mantenimiento:** Schema e integración estables.

**Paso 2 — Análisis del Backlog.**
- `search_kb` y `create_notion_ticket` requeridos en >85% de casos.
- Tools de SMS/WhatsApp redundan con email y son difíciles.
- `fetch_url` tiene altísimo riesgo de exfiltración e inyección.
- `translate` o `summarize` son funciones nativas del LLM.

::interioriza
Tener muchos tools es como darle a un conductor aprendiz un panel de avión.
Es mejor empezar con volante, pedales y cambios (5 tools).
Cuando domine eso, le agregamos el control crucero.
::

**Paso 3 — Schema Estricto.**
- Define `type`, `properties` exactas y `required`.
- Incluye antiejemplos en la descripción para guiar al LLM.
- **Ejemplo:** "NO USES para fechas, usa search_calendar".

**Paso 4 — Idempotencia.**
- `search_kb` no altera nada.
- `create_ticket` requiere una clave de idempotencia única.
- `send_email` va protegido con whitelist de dominios.

**Conclusión.**
- Los 5 tools resuelven el 80% de los tickets.
- Las tools rechazadas quedan documentadas (ADR-007).
- Menos tools = mejor schema = agente enfocado.

::pausa{titulo="Aplica el criterio"}
Si el equipo pide agregar un tool "borrar_registro", ¿qué criterio fallaría primero?
- Fallaría el criterio de "Bajo riesgo".
- Sus efectos colaterales no son fáciles de revertir.
::
::/practica

::practica{titulo="Cómo evalué Claude Computer Use vs function calling para 2 casos del Asistente"}
**Problema.** 
- Se propuso usar Claude Computer Use para 2 tareas.
- (A) Actualizar un sistema escolar viejo de los 2000s (sin API).
- (B) Consolidar datos de 3 dashboards modernos SaaS (con API).

**Paso 1 — Prueba con Computer Use (Tarea A).**
- Toma control del mouse, busca alumno y guarda.
- Tarda ~1m 40s y cuesta ~$0.18.
- Tasa de error aceptable, ideal porque no hay API disponible.

**Paso 2 — Prueba con Computer Use (Tarea B).**
- Navega 3 webs, exporta y consolida.
- Tarda ~4m 30s y cuesta ~$0.45.
- Frágil: falla si la web cambia un simple botón.

**Paso 3 — Prueba con Function Calling (Tarea B).**
- Llama a las APIs de los 3 SaaS y consolida.
- Tarda 12 segundos y cuesta ~$0.04.
- 100% robusto a cambios visuales de las webs.

::interioriza
Computer Use es un robot humanoide escribiendo en un teclado.
Function Calling es un cable directo a la base de datos.
El robot es lento y caro; solo úsalo si no hay otra forma de entrar.
::

**Paso 4 — Decisión Final.**
- **Tarea A:** Usa Computer Use con approval humano antes del "Guardar".
- **Tarea B:** Usa Function calling, es 200x más barato y ultra robusto.

**Paso 5 — Mitigación para Computer Use.**
- Agregar *logging* con screenshots de cada clic.
- Escalar a humano si falla 3 veces seguidas.
- Documentar en ADR-009 que es el último recurso.

::pausa{titulo="Compara tecnologías"}
¿Cuál es la principal debilidad de Computer Use frente a APIs modernas?
- La fragilidad ante cambios de diseño (layout).
- Su alto costo y tiempo de ejecución.
::
::/practica
