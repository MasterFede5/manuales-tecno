---
unidad: 6
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 06

::act-mcq{titulo="Repaso conceptual"}
1. La diferencia clave entre workflow y agente es:
   - [ ] El workflow usa LLM y el agente no
   - [x] El agente decide qué tools usar en runtime; el workflow tiene rutas predefinidas
   - [ ] El agente es siempre más caro
   - [ ] El workflow no usa AI

2. ¿Cuál es el componente más subestimado de un agente que falla en producción?
   - [ ] Tools
   - [ ] Modelo
   - [x] Memoria + observabilidad + límites
   - [ ] Velocidad

3. Para resolver un caso multi-paso interdependiente, la arquitectura más adecuada es:
   - [ ] Reactivo
   - [x] Deliberativo (plan-and-execute)
   - [ ] Multi-agente colaborativo
   - [ ] Sin agente

4. El riesgo más grave si un usuario hace prompt injection es:
   - [ ] Que el agente sea lento
   - [ ] Que cueste más
   - [x] Que ejecute acciones destructivas o exfiltre datos
   - [ ] Que escriba mal

5. La mejor manera de controlar el costo de un agente es:
   - [ ] Usar siempre modelo barato
   - [x] max_iterations + max_cost duros + alertas
   - [ ] Limitar tools
   - [ ] No documentar
::/act-mcq

::act-table{titulo="Completa la tabla — caso institucional → arquitectura"}
| Caso del Asistente | Arquitectura recomendada | Por qué |
|---|---|---|
| Responder duda sobre calendario |  |  |
| Procesar cambio de turno (multi-paso) |  |  |
| Generar reporte trimestral con sub-tareas |  |  |
| Redactar comunicado controvertido (varias perspectivas) |  |  |
| Clasificar email entrante |  |  |
| Investigar mejor proveedor para una compra |  |  |
::/act-table

::act-match{titulo="Relaciona el componente con su función"}
| Componente | Función |
|---|---|
| 1. Percepción | a) Lo que el agente recuerda entre pasos |
| 2. Planificación | b) Cómo recibe input del mundo |
| 3. Tools | c) Cómo descompone objetivos en pasos |
| 4. Memoria | d) Lo que puede hacer en el mundo |
| 5. Ejecución | e) Coordina el loop con safeguards |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Un agente con 50 tools siempre es mejor que uno con 5. ( ) ____________________________________________

2. Computer Use es la mejor opción para integrar APIs modernas. ( ) ____________________________________________

3. Un agente sin max_iterations puede consumir miles de USD en una sola ejecución. ( ) ____________________________________________

4. Multi-agente colaborativo es siempre superior para cualquier tarea. ( ) ____________________________________________

5. Prompt injection se previene principalmente con prompts bien escritos. ( ) ____________________________________________
::/act-tf

::act-case{titulo="Caso para resolver — tu primer agente fallando" lineas=12}
Tu agente del Asistente lleva 1 semana en producción. De pronto recibes alerta crítica: gastó $40 USD en 3 horas (vs presupuesto $50/día). Al revisar logs, descubres que en una conversación entró en loop intentando crear un ticket que ya existía (idempotency falló porque el email tenía coma extra que el normalizador no quitó).

Diseña tu respuesta en 5 actos: (1) primer paso de mitigación inmediata; (2) qué buscas en logs; (3) cómo restauras el agente esa noche; (4) plan para que no vuelva a pasar (3 cambios estructurales); (5) comunicación al equipo. Mínimo 10 líneas.
::/act-case

::albatros{titulo="Construye y despliega tu primer agente con safeguards completos" tipo="taller" tiempo="4 h"}
**Pregunta detonadora.** Si pudieras delegar a un agente las 5 decisiones rutinarias más cargadas de tu trabajo, ¿qué tareas elegirías y qué riesgos te quitarían el sueño?

**Lo que harás.**
1. Define un agente para resolver un tipo de caso no rutinario en tu institución (cambio de turno, reincorporación tras baja, beca compleja, etc.).
2. Elige plataforma: n8n AI Agent, Lindy, AutoGen self-hosted, o Anthropic API directa.
3. Diseña sistem prompt con rol, reglas, safeguards.
4. Define **5–8 tools** con descripciones explícitas y schemas.
5. Configura **los 7 safeguards** (max_iterations, max_cost, alertas, approval para acciones destructivas, whitelist destinos, logging, health check).
6. Construye golden set de **5 casos**: 3 felices, 1 caso límite, 1 prompt injection adversarial.
7. Ejecuta y documenta resultados con costo, tiempo, escalaciones.
8. Documenta runbook + ADR de adopción.

**Materiales.** Cuenta de plataforma, repo Git, 4 horas.

**Entregable.**
- Sistema prompt + tools + workflow.
- Reporte de pruebas (golden set).
- Runbook (1 página).
- ADR de adopción (1 página).
- Métricas de costo proyectado mensual.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Sistema prompt | informal | con rol y reglas | con reglas + contraejemplos + ignore-injection |
| Tools | sin schemas | schemas básicos | schemas estrictos + descripciones explícitas |
| Safeguards | <3 | 5 de 7 | 7 de 7 con evidencia |
| Golden set | 1-2 casos | 3-4 | 5+ con prompt injection |
| Documentación | mínima | runbook | runbook + ADR + diagrama |
| Adopción | privado | mostrado al equipo | con métricas a 1 semana |
::/albatros

::act-fill{titulo="El loop ReAct del agente"}
El loop básico de un agente deliberativo es:

_____________ (razonamiento) → _____________ (llamada a tool) → _____________ (resultado del tool) → repite.

El loop termina cuando el agente cumple el objetivo, alcanza `____________`, o supera `____________`. Cada paso emite un trace que se guarda en _____________ y el siguiente paso lee.
::/act-fill

::act-mindmap{titulo="Tu primer agente institucional v1.0" centro="AGENTE ASISTENTE v1.0" nodos_primarios=7 nodos_secundarios=14}
Las 7 ramas: (1) sistema prompt, (2) tools curados con schemas, (3) los 7 safeguards, (4) golden set de 5+ casos, (5) costo proyectado mensual, (6) runbook con incident response, (7) métricas a 7 días. Cada secundario, dato concreto.
::/act-mindmap

::act-label{titulo="Etiqueta los 7 safeguards en un agente"}
> Marca: a) la capa que protege contra loops · b) la capa que protege contra prompt injection · c) la capa que protege contra exfiltración de datos · d) la capa que más estudiantes saltan en sus primeros agentes.
::/act-label


::visual{tipo="diagrama-flujo" descripcion="Diagrama de un agente con sus 7 safeguards como capas concéntricas alrededor del modelo: max_iterations, max_cost, alertas de costo, approval humano para acciones destructivas, whitelist de destinos, logging, health check pre-ejecución. Espacio para que el alumno escriba qué riesgo cubre cada capa y un ejemplo concreto del Asistente Albatros." paginas="0.5" src="../manualesGem/assets/visuales/manual-4/u06/90-actividades-v01.svg"}
::act-case{titulo="Caso de diseño — 5 tools mínimos para tu Asistente" lineas=14}
Limita tu agente a **exactamente 5 tools**. Para tu Asistente Institucional, ¿cuáles eligirías y por qué? Considera: cobertura de los 5 casos no rutinarios típicos, complejidad de mantenimiento, riesgo de errar tool selection. Para cada tool, anota nombre, descripción 1-línea, idempotencia y approval. Justifica por qué descartas otras 3 que podrías tener tentación de incluir.
::/act-case

::albatros{titulo="Reto — auditas un agente público con 'red team' de 5 prompts" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** ¿Qué tan robusto es un agente real cuando un usuario activamente intenta romperlo?

**Lo que harás.**
1. Elige un agente público accesible (ChatGPT con tools, Claude con MCP, Lindy demo, Devin demo).
2. Diseña 5 prompts de red team:
   - Uno que pida acción destructiva (eliminar archivos).
   - Uno con prompt injection clásica ("ignora tus reglas").
   - Uno que pida exfiltrar info de sesión anterior.
   - Uno que induzca loop (preguntas circulares).
   - Uno que abuse de un tool legítimo (uso fuera de scope).
3. Ejecuta los 5 y documenta qué hizo el agente.
4. Identifica los safeguards que se activaron y los que faltaron.
5. Escribe recomendaciones para el equipo de ese agente (ético: no atacas, reportas).

**Entregable.** Reporte de 1 página con 5 prompts, 5 respuestas, análisis de safeguards, recomendaciones.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Diversidad de prompts | 1-2 tipos | 3-4 | los 5 vectores |
| Análisis de safeguards | informal | identifica 1-2 | identifica todos los presentes y ausentes |
| Ética | atacó sistema | benchmark documentado | benchmark + reporte responsable |
::/albatros
