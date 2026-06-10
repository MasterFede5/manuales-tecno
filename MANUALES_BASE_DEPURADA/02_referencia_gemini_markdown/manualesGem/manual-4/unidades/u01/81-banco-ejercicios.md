---
unidad: 1
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 01

> Trabajas con tu repo de prompts del Episodio 1 abierto. Cada ejercicio entra y sale del repo: lo que produces aquí lo dejas en `prompts/`, `evals/` o `docs/decisiones-de-diseno.md`. **Resuelve cada ítem antes de mirar la clave**.

### Sección A — Estructura XML y delimitadores (1.1)

::act-fill{titulo="A1. Completa el esqueleto XML obligatorio"}
Tu prompt institucional siempre lleva las 6 secciones de la unidad. Llena los huecos con la etiqueta correcta:

```xml
<________>
Eres el Asistente Institucional Albatros, tono profesional y cálido.
</________>

<context>...</context>

<________>
Redacta un comunicado de máximo 200 palabras.
</________>

<constraints>
- No inventes fechas que no aparezcan en el ________.
- Usa tratamiento de "________".
- Si falta un dato, escribe "[dato pendiente — confirmar]".
</constraints>

<examples>
<example_________>...</example_________>
<example_________>...</example_________>
</examples>

<________>
JSON con campos comunicado_humano y metadata.
</________>
```
::/act-fill

::act-tf{titulo="A2. Mitos sobre XML en prompts"}
1. XML solo funciona con Claude; GPT-5 lo ignora. ( ) ____________________________________________
2. Usar `<task>` y `<instrucciones>` mezclados en el mismo prompt es buena práctica. ( ) ____________________________________________
3. Las etiquetas inventadas (`<voz>`, `<estilo>`) son válidas si las usas con consistencia. ( ) ____________________________________________
4. Anidar `<example_good>` dentro de `<examples>` confunde al modelo. ( ) ____________________________________________
::/act-tf

### Sección B — Meta-prompting (1.2)

::act-order{titulo="B1. Orden del bucle de meta-prompting"}
Ordena los pasos del bucle prompt-author → prompt-critic → prompt-rewriter:

[ ] Ejecutar v0 con 5 inputs reales.
[ ] Pegar el meta-prompt patrón con el objetivo.
[ ] Pedir al modelo críticas concretas a v0.
[ ] Reescribir a v1 incorporando críticas.
[ ] Aceptar v1 si cumple criterios o iterar.
[ ] Recibir v0 propuesto por el modelo.
[ ] Definir 3 criterios de aceptación medibles.
::/act-order

::act-case{titulo="B2. Caso — meta-prompt para minutas" lineas=10}
Tu coordinadora pide un prompt que reciba la transcripción de una junta de 90 min y entregue: 5 puntos clave + 3 acuerdos + 2 pendientes con responsable. Escribe el **meta-prompt** que le pasarás al modelo (no el prompt final, sino la **petición** al modelo para que él te entregue v0). Mínimo 5 secciones.
::/act-case

### Sección C — CoT, ReAct, Self-consistency, ToT (1.3 y 1.4)

::act-mcq{titulo="C1. Tradeoffs de razonamiento avanzado"}
1. Tu Asistente clasifica solicitudes con 92 % de acierto base. Activas Self-consistency con n=5. Cabe esperar:
   - [ ] Subir a 100 % siempre
   - [x] Mejorar 1–4 puntos pagando ~5x el costo
   - [ ] Bajar el costo
   - [ ] Romper la salida JSON

2. ReAct es **estrictamente necesario** cuando:
   - [ ] El modelo debe redactar mejor
   - [ ] Quieres dar few-shot
   - [x] El modelo necesita consultar una herramienta externa antes de responder
   - [ ] La salida debe ser JSON

3. Tree-of-Thoughts conviene en:
   - [ ] Clasificación binaria
   - [ ] Resúmenes de juntas
   - [x] Problemas con múltiples ramas plausibles donde valga explorar y podar
   - [ ] Cualquier prompt para reducir costo

4. CoT "deja pensar antes de responder" funciona mejor cuando:
   - [ ] Pides "responde rápido"
   - [x] Le pides al modelo escribir su razonamiento en `<thinking>` antes del JSON final
   - [ ] Pones temperatura 0
   - [ ] Quitas el rol
::/act-mcq

::act-match{titulo="C2. Técnica → caso institucional"}
| Técnica | Caso institucional |
|---|---|
| 1. CoT con `<thinking>` | a) Resolver "¿cuántos cupos quedan?" sin equivocarse |
| 2. ReAct | b) Buscar el reglamento antes de responder a un papá |
| 3. Self-consistency | c) Clasificar solicitudes ambiguas con voto mayoritario |
| 4. Tree-of-Thoughts | d) Diseñar un calendario de exámenes con 3 restricciones cruzadas |
::/act-match

### Sección D — Prompt chaining y few-shot (1.5 y 1.6)

::act-order{titulo="D1. Diseña la cadena para 'comunicado de suspensión'"}
La tarea total es: input crudo de la dirección → comunicado pulido. Ordena los 6 eslabones:

[ ] Eslabón 5 — validador de tono institucional
[ ] Eslabón 1 — extractor de datos clave (fecha, motivo, alcance)
[ ] Eslabón 4 — redactor del comunicado
[ ] Eslabón 6 — empaquetador en JSON con metadata
[ ] Eslabón 2 — clasificador de tipo (suspensión / evento / cambio)
[ ] Eslabón 3 — buscador en reglamento (RAG, U4)
::/act-order

::act-fill{titulo="D2. Few-shot estratégico — diversidad obligada"}
Tu few-shot tiene **3 ejemplos**. Para que sea estratégico, cada uno debe cubrir un caso distinto:

- Ejemplo 1 — caso ________ (la mayoría del tráfico).
- Ejemplo 2 — caso con ________ delicado (queja, sanción).
- Ejemplo 3 — caso de ________ (datos pendientes, ambigüedad).

Si los 3 ejemplos son del mismo tipo, el modelo va a ________ ese patrón y fallar fuera de él.
::/act-fill

### Sección E — Constrained output y evaluación (1.7 y 1.8)

::act-table{titulo="E1. Completa el schema JSON para 3 tareas"}
| Tarea | Campo principal (string) | Campo enum (categorías) | Campo booleano | Campo array |
|---|---|---|---|---|
| Clasificador de solicitudes |  |  |  |  |
| Redactor de comunicados |  |  |  |  |
| Resumen de juntas |  |  |  |  |
::/act-table

::act-mcq{titulo="E2. Tomar decisiones con datos del golden"}
1. Tu golden de 50 ejemplos da: v3 = 41/50, v4 = 44/50. Test estadístico: p = 0.21. Decisión correcta:
   - [ ] Promover v4 directo a 100 %
   - [x] Mantener v3 y ampliar el golden a 200 antes de decidir
   - [ ] Mezclar ambos en producción
   - [ ] Rollback a v2

2. v5 baja la latencia 40 % y mantiene calidad en golden de 100. Pero el costo sube 60 % por más tokens. Decisión:
   - [ ] Promover v5 sin más
   - [x] Promover solo si el caso de uso justifica latencia menor (ej. UI síncrona) y rastrear costo mensual
   - [ ] Rollback
   - [ ] Pedir más golden
::/act-mcq

::act-tf{titulo="E3. Mitos de evaluación"}
1. Si el golden tiene 10 ejemplos y todos pasan, el prompt está listo para producción. ( ) ____________________________________________
2. Promover canary del 5 % al 100 % en el mismo día es prudente si el smoke pasa. ( ) ____________________________________________
3. La rúbrica humana solo aplica a respuestas creativas. ( ) ____________________________________________
::/act-tf

### Sección F — Caso integrador

::act-case{titulo="F1. Caso — eliges entre 3 técnicas" lineas=12}
La coordinadora pide un nuevo prompt: dado un correo de un papá con dudas múltiples, devolver una respuesta que (1) detecte cada duda, (2) consulte el reglamento, (3) redacte una respuesta unificada con tono cálido. Tienes 2 horas. Elige **una sola** técnica como columna vertebral —prompt chaining, ReAct o Tree-of-Thoughts— y justifica por qué. Anticipa qué pasa si te equivocas de elección.
::/act-case

::act-mindmap{titulo="F2. Mapa mental de tu repo de prompts" centro="REPO PROMPTS ALBATROS" nodos_primarios=6 nodos_secundarios=12}
Llena las burbujas con: tareas (3), técnicas activas (8), artefactos por prompt (XML, JSONL, CHANGELOG), métricas (5+), proceso de release (6 pasos), próximos issues (mín. 3 ideas).
::/act-mindmap

---

## Clave de respuestas

**A1.** `role` · `task` · `context` · `usted` · `_good` · `_bad` · `output_format`.

**A2.** 1) Falso — GPT-5 y Gemini 2 también están entrenados con datos estructurados; XML mejora parsing en los tres. 2) Falso — mezclar etiquetas con sinónimos rompe consistencia; elige una nomenclatura. 3) Verdadero **con consistencia** — etiquetas custom funcionan si las usas igual en todos los prompts del repo. 4) Falso — el anidamiento `<examples><example_good>` es práctica recomendada.

**B1.** Orden: `Definir criterios → Pegar meta-prompt → Recibir v0 → Ejecutar v0 con 5 inputs → Pedir críticas → Reescribir v1 → Aceptar o iterar`.

**B2.** Respuesta libre. Verifica que tu meta-prompt tenga: `<rol_del_modelo>` (ingeniero de prompts), `<objetivo>`, `<criterios_de_aceptacion>` medibles (ej. "5 puntos máx. 25 palabras c/u"), `<restricciones>`, `<formato_de_entrega>`.

**C1.** 1-b · 2-c · 3-c · 4-b.

**C2.** 1-a · 2-b · 3-c · 4-d.

**D1.** Orden: `1 extractor → 2 clasificador → 3 buscador reglamento → 4 redactor → 5 validador tono → 6 empaquetador JSON`.

**D2.** `típico` · `tono` · `borde` · `sobreajustar`.

**E1.** Sugerencia (acepta variantes razonables):
| Tarea | string | enum | bool | array |
|---|---|---|---|---|
| Clasificador | `categoria_principal` | `categoria` 5 valores | `requiere_revision` | `etiquetas_secundarias` |
| Redactor | `comunicado_humano` | `categoria` 4 valores | `requiere_revision` | `datos_pendientes` |
| Resumen | `resumen_corto` | `tipo_junta` 3-4 valores | `tiene_acuerdos` | `pendientes` |

**E2.** 1-b · 2-b.

**E3.** 1) Falso — 10 ejemplos no detectan errores raros; mínimo 30, mejor 50+. 2) Falso — la regla operativa es 5 % → 25 % → 50 % → 100 % con 24 h entre saltos. 3) Falso — la rúbrica humana también aplica a clasificación cuando hay categorías subjetivas.

**F1.** Respuesta libre. Una buena respuesta defiende **prompt chaining** (múltiples pasos especializados encadenados) por ser el más robusto para "detectar + consultar + redactar". ReAct serviría si **solo** fuera consultar herramientas. ToT desperdicia costo aquí.

**F2.** Mapa mental — autoevalúa cobertura: si te falta cualquiera de las 6 ramas, tu repo aún no es operativo.
