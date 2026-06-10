---
unidad: 1
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 01

::act-mcq{titulo="Repaso conceptual — las 8 técnicas"}
1. ¿Cuál es la principal ventaja de envolver instrucciones en `<task>...</task>`?
   - [ ] El modelo escribe más rápido
   - [x] Permite parsing fiable y edición quirúrgica del prompt
   - [ ] Reduce el costo en tokens
   - [ ] Activa modo multilingüe

2. Self-consistency NO es la mejor opción cuando:
   - [ ] La pregunta tiene respuesta única correcta
   - [ ] Necesitas reducir error en cálculo
   - [x] El problema es abierto con múltiples soluciones aceptables
   - [ ] El golden set muestra varianza alta

3. En un pipeline de 5 prompts, el paso 1 falla 1/20. Probabilidad de éxito del pipeline (asumiendo independencia y ningún reintento, los demás pasos perfectos):
   - [ ] 100%
   - [ ] 99%
   - [x] 95%
   - [ ] 5%

4. Para integrar el output con n8n necesitas garantizar JSON válido. ¿Qué mecanismo es el más fiable?
   - [ ] Pedir "responde en JSON" en el prompt
   - [ ] Habilitar JSON mode del proveedor
   - [x] Function calling con JSON Schema estricto / Structured Outputs
   - [ ] Parsear con regex

5. Tu A/B canary muestra que v4 reduce 30 % la latencia y mantiene calidad. ¿Acción?
   - [ ] Rollback a v3 por seguridad
   - [x] Subir gradualmente v4 al 50 %, luego 100 %
   - [ ] Promover a 100 % directamente
   - [ ] Esperar 1 mes más de canary

6. ReAct se diferencia de CoT en que:
   - [ ] Razona en árbol y no en cadena
   - [x] Alterna razonamiento con acciones (llamadas a herramientas)
   - [ ] Solo aplica a tareas matemáticas
   - [ ] Es un sinónimo de few-shot
::/act-mcq

::act-table{titulo="Completa la tabla — qué técnica para qué problema"}
| Problema operativo del Asistente | Técnica principal | Por qué |
|---|---|---|
| Clasificar 5 categorías de solicitudes |  |  |
| Redactar comunicado oficial |  |  |
| Calcular cupos disponibles |  |  |
| Diseñar plan de comunicación trimestral |  |  |
| Decidir entre v3 y v4 del prompt |  |  |
| Conectar el modelo con base de datos |  |  |
::/act-table

::act-match{titulo="Relaciona la técnica con su caso ideal de uso"}
| Técnica | Caso ideal |
|---|---|
| 1. Estructura XML | a) Output que entrará a n8n para automatización |
| 2. Meta-prompting | b) Necesitas reducir error en cálculo determinista |
| 3. ReAct | c) Quieres que el modelo escriba la primera versión del prompt |
| 4. Self-consistency | d) Sistema de soporte que consulta base de conocimiento |
| 5. Prompt chaining | e) Tarea compleja descompuesta en pasos especializados |
| 6. Constrained output | f) Reusar las mismas instrucciones en múltiples sesiones |
::/act-match

::act-order{titulo="Ordena los pasos para llevar un prompt a producción"}
- [ ] Promover a 100 % del tráfico
- [ ] Diseñar v0 con meta-prompt
- [ ] Construir golden set de 20-50 ejemplos
- [ ] A/B canary al 5 %
- [ ] Iterar con bucle críticar-reescribir
- [ ] Versionar v1.0 en Git con CHANGELOG
- [ ] Validar cumplimiento del schema
- [ ] Smoke test con 3 inputs
::/act-order

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Few-shot con 30 ejemplos siempre supera a few-shot con 3. ( ) ____________________________________________

2. ReAct funciona sin ninguna herramienta externa, igual que CoT. ( ) ____________________________________________

3. Si tu schema usa `additionalProperties: true`, el modelo va a inventar campos extra. ( ) ____________________________________________

4. Self-consistency mejora todos los problemas de razonamiento por igual. ( ) ____________________________________________

5. Un prompt sin golden set no debería entrar a producción. ( ) ____________________________________________
::/act-tf

::albatros{titulo="Diseñas y publicas el primer prompt versionado de tu equipo" tipo="taller" tiempo="120 min"}
**Pregunta detonadora.** Si tu equipo opera con prompts escritos en notas sueltas y nadie sabe qué versión está corriendo, ¿qué pasa cuando uno se rompe en producción?

::interioriza
Imagina que los prompts son recetas en la cocina de un restaurante. 
Si cada cocinero tiene notas sueltas y la sopa sale salada, no sabes qué receta arreglar.
Versionar es tener un recetario oficial.
::/interioriza

::pausa
¿Qué mecanismo te permite asegurar que un cambio en la receta no arruinará la comida antes de dársela a todos los clientes?
::/pausa

**Lo que harás.**
- Elige una tarea operativa real de tu institución (clasificar correos, redactar respuestas, generar resúmenes).
- Aplica el flujo de la práctica resuelta: meta-prompt → v0 → critique → v1.
- Diseña un golden set de **al menos 10 ejemplos** validados por una persona del equipo distinta a ti.
- Implementa constrained output con JSON Schema.
- Versiona en Git (o Notion si tu equipo no usa Git): `v1.0.xml`, `v1.0.eval.json`, `CHANGELOG.md`.
- Comparte la URL del repo con el equipo y solicita evaluación cruzada.

**Materiales.** 
- Editor de texto
- Cuenta gratis de un LLM (Claude o ChatGPT)
- Git/Notion
- Hoja de evaluación

**Entregable.**
- `v1.0.xml` (o equivalente).
- Golden set en JSONL.
- CHANGELOG.
- Reporte de evaluación cruzada (1 página).

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Claridad del XML | etiquetas inconsistentes | semánticas | impecables, autodescriptivas |
| Diversidad del golden | 1 tipo | 2-3 tipos | 5+ tipos cubriendo bordes |
| Cumplimiento de schema | sin schema | schema laxo | schema estricto validado |
| Versionado | un archivo | con CHANGELOG | repo organizado, equipo lo lee |
| Evaluación cruzada | autor solo | una persona más | rúbrica multi-evaluador |
::/albatros

::act-fill{titulo="Completa el contrato XML mínimo del Asistente"}
Escribe los identificadores de etiqueta que faltan en este contrato XML mínimo (el que vas a usar en el 90 % de tus prompts):

```xml
<________>Eres el Asistente Institucional Albatros. Tono profesional y cálido.</________>
<context>{datos del caso}</context>
<________>{lo que hay que producir}</________>
<________>
- No inventes fechas que no estén en el contexto.
- Si falta un dato, escribe "[dato pendiente — confirmar]".
</________>
<examples>...</examples>
<________>JSON con campos comunicado_humano y metadata.</________>
```
::/act-fill

::act-mindmap{titulo="Tu sistema personal de prompt engineering" centro="PROMPT ENGINEERING ALBATROS" nodos_primarios=8 nodos_secundarios=16}
- Llena las 8 ramas con las técnicas de la unidad.
- En cada secundario, anota un caso operativo del Asistente donde aplicaste esa técnica.
- Si un nodo queda vacío, agenda 30 min para llenarlo antes de pasar a U2.
::/act-mindmap

::act-case{titulo="Caso de diseño — eliges entre arquitecturas" lineas=14}
**El reto de la coordinadora:**
- Dado un correo de un papá con 3 dudas mezcladas.
- Devolver una respuesta unificada que detecte cada duda.
- Buscar en el reglamento institucional.
- Redactar respuesta cálida.

::interioriza
Elegir la arquitectura correcta es como elegir el vehículo para un viaje.
No usas un camión de carga (Tree-of-Thoughts) para ir a la esquina a comprar pan (Prompt simple).
Usa la herramienta más ligera que haga el trabajo de forma confiable.
::/interioriza

::pausa
¿Por qué Prompt Chaining podría ser más predecible que ReAct para esta tarea de 3 dudas?
::/pausa

**Tus restricciones:**
- Tienes 2 horas. 
- Elige **una sola** arquitectura (prompt chaining, ReAct o Tree-of-Thoughts) y justifica tu descarte.
- Anticipa el modo de falla más probable y tu mitigación.
::/act-case

::act-label{titulo="Etiqueta el ciclo de vida del prompt"}
::visual{tipo="diagrama-flujo" descripcion="Diagrama circular del ciclo de vida de un prompt institucional con 7 estaciones numeradas: idea, meta-prompt v0, smoke test, golden set, A/B canary, producción, retrospectiva. Espacio en blanco junto a cada estación para que el alumno escriba el nombre y un riesgo típico." paginas=0.5}

**Marca lo siguiente:**
- a) La estación donde se previene el prompt drift.
- b) La estación donde se detecta una regresión antes de producción.
- c) La estación donde se versiona en Git.
- d) La estación que más equipos saltan y luego pagan caro.
::/act-label

::albatros{titulo="Reto — A/B canary de tu propio prompt" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** Tu prompt v1.0 funciona, pero tu compañera dice que el suyo es mejor. ¿Cómo decides con datos?

::interioriza
Es como comparar dos neumáticos distintos en la Fórmula 1. 
No discutes cuál se ve mejor en boxes.
Das unas vueltas al circuito y mides el tiempo. El golden set es tu circuito.
::/interioriza

::pausa
¿Qué métrica usarías para saber si el nuevo neumático (v1.1) gasta demasiado combustible (tokens/costo)?
::/pausa

**Lo que harás.**
- Toma tu `redactor-comunicados-v1.0` y la propuesta v1.1 de tu compañera.
- Construye un golden de 20 inputs reales (mitad típicos, mitad bordes).
- Corre los dos prompts contra el golden.
- Mide: validez de schema, categoría correcta, fecha resuelta, tono (rúbrica 1–5), latencia, costo.
- Dibuja una mini-tabla comparativa.
- Decide: promueves v1.1, mantienes v1.0 o pides v1.2.

**Entregable.** 
- Tabla comparativa.
- Decisión escrita de 5 líneas justificando la elección.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Tamaño del golden | <10 | 20 | 20 con bordes deliberados |
| Métricas medidas | 1-2 | 4 | 6 incluyendo costo |
| Decisión justificada | "me gustó más" | con 1 dato | con 3 datos y plan de seguimiento |
::/albatros
