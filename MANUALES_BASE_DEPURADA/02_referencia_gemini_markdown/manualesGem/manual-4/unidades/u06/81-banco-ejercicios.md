---
unidad: 6
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 06

> Trabajas con n8n AI Agent o Claude API directa. Tienes 3 tools básicos (RAG, calendario, ticket Notion) ya construidos en U5.

### Sección A — Concepto y anatomía (6.1, 6.2)

::act-mcq{titulo="A1. Workflow vs agente"}
1. La diferencia clave entre workflow y agente:
   - [ ] El workflow no usa LLM
   - [x] El agente decide qué tools usar en runtime; el workflow tiene rutas predefinidas
   - [ ] El agente es siempre más caro
   - [ ] El workflow no tiene memoria

2. Para "responder duda sobre calendario" — ¿agente o workflow?
   - [ ] Agente
   - [x] Workflow (la ruta es predecible)
   - [ ] Cualquiera
   - [ ] Multi-agente

3. Para "procesar cambio de turno con conflicto de aulas" — ¿agente o workflow?
   - [x] Agente (la ruta depende de validaciones intermedias)
   - [ ] Workflow
   - [ ] Solo humano
   - [ ] Multi-agente
::/act-mcq

::act-match{titulo="A2. Componente → función"}
| Componente | Función |
|---|---|
| 1. Percepción | a) Lo que el agente recuerda entre pasos |
| 2. Planificación | b) Cómo recibe input del mundo |
| 3. Tools | c) Cómo descompone objetivos en pasos |
| 4. Memoria | d) Lo que puede hacer en el mundo |
| 5. Ejecución | e) Coordina el loop con safeguards |
::/act-match

::act-fill{titulo="A3. El loop ReAct del agente"}
El loop básico de un agente deliberativo es:

_____________ → _____________ → _____________ → repite hasta cumplir objetivo o alcanzar `max_iterations`.

Cada paso emite un trace que se guarda en _____________ y el siguiente paso lee. La _____________ entre pasos es la diferencia entre "chatbot que no recuerda" y "agente que avanza".
::/act-fill

### Sección B — Tipos y arquitecturas (6.3)

::act-match{titulo="B1. Caso → arquitectura"}
| Caso | Arquitectura recomendada |
|---|---|
| 1. Clasificar email entrante | a) Multi-agente colaborativo |
| 2. Procesar cambio de turno multi-paso | b) Reactivo (1 paso, sin plan) |
| 3. Generar reporte trimestral con sub-tareas independientes | c) Deliberativo plan-and-execute |
| 4. Investigar y comparar 5 proveedores con perspectivas distintas | d) Jerárquico (manager + workers) |
::/act-match

::act-tf{titulo="B2. Mitos de los agentes"}
1. Multi-agente colaborativo es siempre superior. ( ) ____________________________________________
2. Un agente con 50 tools siempre es mejor que uno con 5. ( ) ____________________________________________
3. Un agente reactivo no necesita memoria. ( ) ____________________________________________
4. Un agente deliberativo es más caro que uno reactivo. ( ) ____________________________________________
::/act-tf

### Sección C — Plataformas (6.4)

::act-table{titulo="C1. Plataforma de agente por caso"}
| Caso | Plataforma recomendada | Por qué |
|---|---|---|
| Agente para no técnicos, equipo pequeño |  |  |
| Agente que opere navegador (browser use) |  |  |
| Agente que use computadora completa (mouse, teclado) |  |  |
| Agente integrado a workflows existentes en n8n |  |  |
| Agente de software ingeniería (PR, código) |  |  |
| Agente con razonamiento profundo y multi-tool |  |  |
::/act-table

::act-mcq{titulo="C2. Cuándo NO usar Computer Use"}
1. Tu sistema tiene API REST moderna documentada.
   - [ ] Computer Use ahorra tiempo
   - [x] Function calling con la API es 100x más barato y más rápido
   - [ ] Computer Use es la única opción
   - [ ] Da igual

2. Necesitas que el agente opere un sistema legacy de los años 90 sin API.
   - [x] Computer Use es viable (única opción a veces)
   - [ ] Es prohibido
   - [ ] Solo función calling
   - [ ] Imposible
::/act-mcq

### Sección D — Tools y function calling (6.5)

::act-fill{titulo="D1. Anatomía de un tool bien definido"}
Un tool curado lleva:

- _____________ corto y verbo claro (ej. `search_kb`, `create_ticket`).
- _____________ explícita de qué hace y cuándo usarlo.
- _____________ JSON estricto con tipos y `required`.
- _____________ explícitos de cuándo NO usar este tool.
- _____________ — efectos colaterales documentados (¿es idempotente?).
::/act-fill

::act-order{titulo="D2. Orden de definir tools antes de habilitarlos"}
[ ] Probar el tool aislado con 5 inputs sintéticos
[ ] Escribir descripción explícita y antiejemplos
[ ] Definir schema JSON estricto con `additionalProperties: false`
[ ] Documentar efectos colaterales (idempotencia, rollback)
[ ] Decidir si requiere `approval` humano
[ ] Habilitar al agente con permisos mínimos
::/act-order

::act-case{titulo="D3. Caso — defines un tool 'send_institutional_email'" lineas=12}
Tu agente necesita poder enviar correos institucionales. Define el tool completo: nombre, descripción, schema JSON, antiejemplos (cuándo NO usar), efectos colaterales, requiere approval (sí/no, justifica), whitelist de dominios destino, plantilla de mensaje. Mínimo 8 líneas.
::/act-case

### Sección E — Riesgos y safeguards (6.6)

::act-match{titulo="E1. Riesgo → safeguard"}
| Riesgo | Safeguard |
|---|---|
| 1. Loop infinito | a) max_cost duro con corte y alerta |
| 2. Costo descontrolado | b) max_iterations |
| 3. Acción destructiva | c) approval humano antes de ejecutar |
| 4. Prompt injection | d) ignore-injection en system + filtros input |
| 5. Datos exfiltrados | e) whitelist de dominios destino |
| 6. Tool indisponible | f) health check pre-ejecución |
| 7. Sin trazabilidad | g) logging de cada thought-action-observation |
::/act-match

::act-tf{titulo="E2. Mitos de safeguards"}
1. Si tu sistema prompt está bien escrito, no necesitas safeguards. ( ) ____________________________________________
2. max_iterations alto (50) es seguro porque el agente igual termina rápido cuando puede. ( ) ____________________________________________
3. Approval humano para todas las acciones es la mejor práctica. ( ) ____________________________________________
4. Logging de cada paso aumenta el costo significativamente. ( ) ____________________________________________
::/act-tf

::act-case{titulo="E3. Caso — incident response de tu agente" lineas=14}
Tu agente lleva 1 semana en producción. Recibes alerta crítica: gastó $40 USD en 3 horas (presupuesto diario $50). Logs muestran: el agente entró en loop intentando crear un ticket que ya existía (idempotency falló por coma extra en el email). Diseña tu respuesta: (1) mitigación inmediata, (2) qué buscas en logs, (3) cómo restauras esta noche, (4) 3 cambios estructurales para que no vuelva a pasar, (5) comunicación al equipo.
::/act-case

### Sección F — Caso integrador

::act-mindmap{titulo="F1. Tu primer agente institucional" centro="AGENTE ASISTENTE v1.0" nodos_primarios=7 nodos_secundarios=14}
Las 7 ramas: (1) sistema prompt con rol y reglas, (2) tools curados con schemas, (3) los 7 safeguards configurados, (4) golden set de 5+ casos, (5) costo proyectado mensual, (6) runbook con incident response, (7) métricas de uso a 7 días. Cada secundario, dato concreto.
::/act-mindmap

---

## Clave de respuestas

**A1.** 1-b · 2-b · 3-a.

**A2.** 1-b · 2-c · 3-d · 4-a · 5-e.

**A3.** Thought · Action · Observation · memoria · persistencia.

**B1.** 1-b · 2-c · 3-d · 4-a.

**B2.** 1) Falso — multi-agente añade complejidad y costo; conviene cuando hay perspectivas genuinamente divergentes. 2) Falso — más tools dispersan la atención del modelo y aumentan riesgo de error de selección. 3) Falso — incluso reactivo necesita memoria de la última acción para no repetir. 4) Verdadero generalmente — más iteraciones = más tokens, pero **resuelve casos** que reactivo no puede.

**C1.** Sugerencia (acepta variantes razonables): no técnicos → Lindy o ChatGPT Agents. Browser → Browserbase, Multi-On, ChatGPT Agents. Computadora → Claude Computer Use o Manus. n8n integrado → n8n AI Agent node. Software → Devin, Cursor agents, GitHub Copilot Workspace. Razonamiento profundo + multi-tool → Claude Opus + función calling vía SDK.

**C2.** 1-b · 2-a.

**D1.** Nombre · Descripción · Schema · Antiejemplos · Idempotencia.

**D2.** Orden: schema JSON → descripción + antiejemplos → idempotencia documentada → probar aislado 5 inputs → decidir approval → habilitar con permisos mínimos.

**D3.** Respuesta libre. Verifica: nombre `send_institutional_email`, descripción + cuándo usar, schema con `to`, `subject`, `body`, `template_id` opcional, antiejemplo "no usar para emergencias o avisos legales", side effects "envío irrevocable, no idempotente", approval=true, whitelist `@institucion.edu.mx` y proveedores de padres conocidos.

**E1.** 1-b · 2-a · 3-c · 4-d · 5-e · 6-f · 7-g.

**E2.** 1) Falso — system prompt es necesario pero no suficiente; un usuario hostil bypassa prompts cualesquiera. 2) Falso — 50 iters es ventana enorme para gastar mucho; defaults sanos: 8-15. 3) Falso — approval para **todo** anula el agente; aprueba solo lo destructivo o costoso. 4) Falso — logging es ~3-5 % del costo, irrelevante; no loguear es la causa #1 de incident sin diagnóstico.

**E3.** Respuesta libre. Buena respuesta: (1) corto el agente con kill-switch en n8n, (2) busco en logs último thought antes del loop y el error de idempotency check, (3) restauro con max_iterations bajado a 5 temporalmente, (4) cambios estructurales: normalizador de email robusto + idempotency check con clave hash + alerta cuando >2 retries en mismo evento, (5) comunico el incidente y plan en `#alertas-asistente` con timeline.

**F1.** Mapa libre. Si una rama tiene <2 datos concretos, ese pilar aún no está maduro.
