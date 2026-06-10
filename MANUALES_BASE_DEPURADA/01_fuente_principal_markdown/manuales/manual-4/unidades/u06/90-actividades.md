---
unidad: 6
seccion: actividades
paginas_objetivo: 2
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

::interioriza
**El agente como un chef en un restaurante**
- **LLM:** Es el chef que toma las decisiones.
- **Tools:** Son los cuchillos y los fogones.
- **Safeguards:** Son los extintores y límites de gasto en ingredientes.
Sin límites, el chef podría pedir langosta para cada plato y quebrar el restaurante en horas.
::/interioriza

::act-case{titulo="Caso para resolver — tu primer agente fallando" lineas=12}
Tu agente lleva 1 semana en producción y recibes una alerta crítica:
- **El problema:** Gastó $40 USD en 3 horas (presupuesto: $50/día).
- **La causa:** Entró en loop intentando crear un ticket existente.
- **El fallo:** La idempotencia falló por una coma extra en el email.

Diseña tu respuesta en 5 actos:
1. Primer paso de mitigación inmediata.
2. Qué buscas exactamente en los logs.
3. Cómo restauras el agente esa misma noche.
4. Plan preventivo (3 cambios estructurales).
5. Comunicación al equipo.
Mínimo 10 líneas.
::/act-case

::albatros{titulo="Construye y despliega tu primer agente con safeguards" tipo="taller" tiempo="4 h"}
**Pregunta detonadora.** 
Si pudieras delegar a un agente las 5 decisiones rutinarias más pesadas de tu trabajo:
- ¿Qué tareas elegirías?
- ¿Qué riesgos te quitarían el sueño?

**Lo que harás.**
1. Define un agente para resolver un caso no rutinario institucional (ej. cambio de turno).
2. Elige plataforma: n8n AI Agent, Lindy, AutoGen, o Anthropic API.
3. Diseña system prompt con rol, reglas y safeguards.
4. Define **5–8 tools** con descripciones explícitas y schemas.
5. Configura **los 7 safeguards** (max_iterations, alertas, approval, whitelist, etc.).
6. Construye golden set de **5 casos**: 3 felices, 1 límite, 1 prompt injection.
7. Ejecuta y documenta resultados con costo y tiempo.
8. Documenta runbook + ADR de adopción.

**Materiales.** Cuenta de plataforma, repo Git, 4 horas.

**Entregable.**
- Sistema prompt + tools + workflow.
- Reporte de pruebas (golden set).
- Runbook (1 página) y ADR de adopción.
- Métricas de costo proyectado mensual.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Sistema prompt | informal | con rol y reglas | reglas + contraejemplos + ignore-injection |
| Tools | sin schemas | schemas básicos | schemas estrictos + descripciones |
| Safeguards | <3 | 5 de 7 | 7 de 7 con evidencia |
| Golden set | 1-2 casos | 3-4 | 5+ con prompt injection |
| Documentación | mínima | runbook | runbook + ADR + diagrama |
| Adopción | privado | mostrado al equipo | con métricas a 1 semana |
::/albatros

::act-fill{titulo="El loop ReAct del agente"}
El loop básico de un agente deliberativo es:

_____________ (razonamiento) → _____________ (llamada a tool) → _____________ (resultado) → repite.

El loop termina cuando se cumple el objetivo, alcanza `____________`, o supera `____________`. 
- Cada paso emite un trace.
- Ese trace se guarda en _____________ y el siguiente paso lo lee.
::/act-fill

::act-mindmap{titulo="Tu primer agente institucional v1.0" centro="AGENTE ASISTENTE v1.0" nodos_primarios=7 nodos_secundarios=14}
Las 7 ramas principales:
1. Sistema prompt.
2. Tools curados con schemas.
3. Los 7 safeguards.
4. Golden set de 5+ casos.
5. Costo proyectado mensual.
6. Runbook con incident response.
7. Métricas a 7 días.
(Secundarios: datos concretos para cada rama).
::/act-mindmap

::act-label{titulo="Etiqueta los 7 safeguards en un agente"}
::visual{tipo="diagrama-flujo" descripcion="Diagrama de un agente con sus 7 safeguards como capas concéntricas alrededor del modelo: max_iterations, max_cost, alertas, approval, whitelist, logging, health check." paginas=0.5}
> Marca: 
> a) La capa que protege contra loops.
> b) La capa que protege contra prompt injection.
> c) La capa que protege contra exfiltración de datos.
> d) La capa que más estudiantes saltan en sus primeros agentes.
::/act-label

::act-case{titulo="Caso de diseño — 5 tools mínimos para tu Asistente" lineas=14}
Limita tu agente a **exactamente 5 tools**.
- ¿Cuáles elegirías para tu Asistente Institucional y por qué?
- Considera: cobertura de 5 casos típicos, mantenimiento y riesgo de error.
- Para cada tool anota: nombre, descripción, idempotencia y approval.
- Justifica por qué descartas otras 3 tools tentadoras.
::/act-case

::albatros{titulo="Reto — auditas un agente público con 'red team'" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** 
¿Qué tan robusto es un agente real cuando un usuario activamente intenta romperlo?

**Lo que harás.**
1. Elige un agente público (ChatGPT, Claude con MCP, Lindy demo).
2. Diseña 5 prompts de red team:
   - Acción destructiva (eliminar archivos).
   - Prompt injection clásica ("ignora tus reglas").
   - Exfiltrar info de sesión anterior.
   - Inducir loop (preguntas circulares).
   - Abuso de un tool legítimo.
3. Ejecuta los 5 y documenta la respuesta.
4. Identifica qué safeguards se activaron y cuáles faltaron.
5. Escribe recomendaciones éticas (no atacar, reportar).

**Entregable.** Reporte de 1 página con prompts, respuestas y análisis.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Diversidad | 1-2 tipos | 3-4 | los 5 vectores |
| Análisis | informal | identifica 1-2 | identifica todos |
| Ética | atacó sistema | benchmark | benchmark + reporte |
::/albatros
