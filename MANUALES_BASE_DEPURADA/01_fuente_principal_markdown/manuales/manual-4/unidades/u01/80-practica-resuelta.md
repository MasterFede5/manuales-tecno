---
unidad: 1
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 01

::practica{titulo="Diseñar el prompt 'redactor-institucional-v1' aplicando las 8 técnicas de la unidad"}
**Problema.** 
- El equipo del Asistente Institucional necesita un prompt para emitir comunicados oficiales.
- Debe recibir: motivo, fecha y alcance.
- Tu tarea: diseñar la versión 1.0, evaluarla con un golden set de 10 ejemplos y dejarla lista para pruebas A/B.

**Paso 1 — Datos.**
- **Tipos de solicitudes:** Suspensión, evento, cambio de horario, recordatorio.
- **Audiencia:** Padres de familia y estudiantes.
- **Tono institucional:** Formal pero cercano, sin emojis, uso de "usted".
- **Output esperado:** JSON con `comunicado_humano` y `metadata`.

**Paso 2 — Estrategia (técnicas de la unidad).**
- **1.1 Estructura XML:** Separa role, context, task y constraints.
- **1.2 Meta-prompting:** Usa Claude Opus para generar la versión 0.
- **1.3 CoT mínimo:** Valida hechos antes de redactar.
- **1.6 Few-shot estratégico:** 3 ejemplos diversos.
- **1.7 Constrained output:** Schema JSON estricto.
- **1.8 Golden set:** 10 ejemplos para validar.

**Paso 3 — Diseño de v0 (meta-prompt).**
- Pegamos en Claude el meta-prompt patrón con los datos del Paso 1. 
- Recibimos la v0 con estructura XML completa, 5 secciones y un schema JSON en 4 minutos.

**Paso 4 — Refinamiento iterativo.**
- Ejecutamos v0 con 5 inputs reales históricos.
- La crítica revela un fallo con fechas relativas ("mañana", "próximo lunes").
- Reescribimos a v1 agregando `<date_resolution>` para convertir fechas a absolutas usando el contexto.

::interioriza
> Piensa en el refinamiento iterativo como afinar un instrumento antes del concierto.
> La primera versión (v0) hace ruido, pero afinas las cuerdas (fechas relativas) 
> hasta que suene perfecto en los ensayos (inputs reales).
::

**Paso 5 — Few-shot (curaduría).**
- Seleccionamos 3 ejemplos clave:
- **Típico:** Suspensión por mantenimiento.
- **Tono difícil:** Cambio de horario tras quejas.
- **Borde:** Evento con dato pendiente (`[confirmar]`).

**Paso 6 — Constrained output.**
```json
{
  "type": "object",
  "properties": {
    "comunicado_humano": {"type": "string", "minLength": 80, "maxLength": 600},
    "metadata": {
      "type": "object",
      "properties": {
        "categoria": {"enum": ["suspensión", "evento", "cambio_horario", "recordatorio"]},
        "fecha_principal": {"type": "string", "format": "date"},
        "requiere_revision": {"type": "boolean"},
        "datos_pendientes": {"type": "array", "items": {"type": "string"}}
      },
      "required": ["categoria", "fecha_principal", "requiere_revision"]
    }
  },
  "required": ["comunicado_humano", "metadata"],
  "additionalProperties": false
}
```

**Paso 7 — Golden set (10 ejemplos).**
- 4 casos típicos y 3 con dato pendiente.
- 2 casos de tono delicado y 1 ambiguo.
- Construimos `evals/redactor-institucional-v1.jsonl` con el input y output esperado por coordinación.

**Paso 8 — Corrida automática y rúbrica.**

| Métrica | Resultado |
|---|---|
| Validez de schema | 10/10 |
| Categoría correcta | 9/10 (1 falló entre evento/recordatorio) |
| Fecha resuelta | 10/10 |
| Tono institucional | 4.3 promedio (rúbrica 1-5) |
| Datos pendientes | 3/3 |
| Latencia mediana | 2.1 s |
| Costo por llamada | $0.012 |

**Paso 9 — Versionado y publicación.**
- Subimos `prompts/redactor-institucional/v1.0.xml` a Git con su reporte.
- El CHANGELOG documenta: "v1.0 release inicial con 9/10 categoría y 4.3/5 tono".
- Se lanza en canary al 5 % del tráfico durante 5 días para comparar.

**Respuesta y Verificación.** 
- El prompt queda listo para canary. La falla de categoría se anota como issue para v1.1.
- Un revisor independiente replicó el golden y obtuvo el mismo 9/10.
- **Lección:** Las técnicas son un proceso completo. Saltarse la evaluación deja prompts frágiles.

::pausa{tipo="deduccion"}
1. ¿Por qué es crucial añadir el caso "ambiguo" al golden set en vez de solo casos típicos?
2. Si la latencia hubiera sido de 15s en el paso 8, ¿qué técnica de la estrategia revisarías primero?
::
::/practica

::practica{titulo="Cómo evalué v3 vs v4 del clasificador y decidí no promover"}
**Problema.** 
- El `clasificador-solicitudes-v3` lleva tres semanas en producción al 100%.
- Una compañera propone `v4` argumentando que "redacta mejor las razones".
- Hay que decidir si promover o mantener antes del viernes.

**Paso 1 — Criterios de aceptación.**
- **Calidad:** Precisión global no debe caer frente a v3 (en 50 ejemplos).
- **Costo:** Incremento máximo del 15%.
- **Latencia:** Incremento máximo del 25%.
- **Trazabilidad:** Inclusión del campo `razon` en el JSON.

**Paso 2 — Refrescar el golden set.**
- Se amplía el golden set de 30 a 50 ejemplos.
- Se incluyen 8 casos de borde recientes de producción (ej. solicitudes mixtas).

**Paso 3 y 4 — Corrida pareada y Resultados.**
- Se ejecuta el mismo input a la vez.

| Métrica | v3 | v4 | Δ |
|---|---|---|---|
| Macro-F1 | 0.91 | 0.89 | -0.02 |
| Precisión "admisión" | 0.94 | 0.92 | -0.02 |
| Latencia mediana | 1.8 s | 2.6 s | +44 % |
| Costo/llamada | $0.011 | $0.018 | +64 % |
| Razón en JSON | no | sí | feature nueva |

**Paso 5 — Análisis de bordes.**
- Se revisan las 8 solicitudes mixtas: v3 acierta 6, v4 solo 5.
- La razón de v4 es convincente, pero a veces justifica una categoría incorrecta.
- Justificar un error es peor que admitir "no sé".

::interioriza
> Comparar v3 con v4 es como probar un auto nuevo. 
> El auto nuevo (v4) tiene asientos de cuero (razón en JSON), 
> pero frena peor (menos precisión) y gasta más gasolina (costo +64%). 
> No lo compras solo por los asientos.
::

**Paso 6 y 7 — Decisión y Comunicación.**
- **Decisión:** No promover. v4 viola el macro-F1 y el límite de costo.
- Se pedirá una v3.1 que agregue la razón opcional sin tocar el motor base.
- Se documenta el rechazo en `decisiones-de-diseno.md` con los datos duros.

**Paso 8 — Cerrar el ciclo.**
- Se abre el issue `v3.1-razon-opcional` con fecha de revisión.
- v3 sigue en producción y v4 queda archivado y documentado.
- **Lección:** Una mejora plausible requiere demostración real. Documenta tus rechazos.

::pausa{tipo="deduccion"}
1. ¿Qué peligro esconde que un LLM te dé una "razón convincente" para una clasificación incorrecta?
2. ¿Por qué se decide mantener el motor de v3 y pedir un `v3.1` en vez de arreglar `v4`?
::
::/practica

::practica{titulo="Cómo escogí entre prompt chaining y ReAct para 'respuesta unificada a correo de papá'"}
**Problema.** 
- Una coordinadora reenvía un correo con 3 dudas variadas de un padre de familia.
- Necesitamos una única respuesta cálida y precisa usando reglamento escolar.
- ¿Usamos Prompt chaining (cadena) o ReAct (agente autónomo)?

**Paso 1 y 2 — Mapear la tarea y Chaining (A).**
- **Tarea:** Detectar dudas, buscar respuesta en reglamento y redactar.
- **Eslabón 1:** Extraer dudas en JSON.
- **Eslabón 2:** Búsqueda RAG y respuesta corta por duda.
- **Eslabón 3:** Redacción unificada y cálida.

**Paso 3 — ReAct (B).**
- Un solo prompt con razonamiento cíclico (thought → action → observation).
- El modelo decide cuántas búsquedas hacer de forma autónoma.

**Paso 4 — Pruebas de diseño (5 inputs reales).**
- **Input claro:** Ambos aciertan 3/3.
- **Duda implícita:** Chaining la pierde; ReAct la descubre al razonar.
- **Duda fuera de reglamento:** Chaining dice "no sé"; ReAct inventa un artículo (Alucinación).
- **Sobrecarga (5 dudas):** Chaining escala bien; ReAct se queda sin tokens.
- **Dato sensible:** ReAct filtra su "razonamiento interno" en la respuesta al padre (Grave).

::interioriza
> Chaining es como una cadena de montaje en una fábrica: paso a paso, predecible y fácil de inspeccionar.
> ReAct es como darle la llave a un genio creativo: puede sorprenderte resolviendo lo implícito, 
> pero también puede chocar el auto y contárselo a los clientes.
::

**Paso 5 — Comparación de costo y trazabilidad.**

| Criterio | Chaining (A) | ReAct (B) |
|---|---|---|
| Acierto sobre 5 | 4/5 | 2/5 |
| Costo medio | $0.038 | $0.052 |
| Trazabilidad | logs por eslabón | log monolítico |
| Riesgo de leak | bajo | alto |

**Paso 6 y 7 — Decisión y Mitigación.**
- **Decisión:** Gana Prompt chaining. 
- Priorizamos trazabilidad para auditar respuestas a familias y evitamos inventar artículos.
- Aceptamos el aumento de costo y latencia dada la criticidad.
- **Mitigación:** Para mejorar la extracción de dudas implícitas en Chaining, se añade meta-prompting y few-shot.

**Respuesta y Lección.** 
- La cadena de 3 eslabones pasa a versión 1.0 con un schema estricto.
- ReAct brilla en exploración abierta; chaining es para flujos auditables. 
- La trazabilidad mandó sobre la agilidad.

::pausa{tipo="deduccion"}
1. Sabiendo que el sistema es asíncrono, ¿por qué la latencia de 6.2s de Chaining no fue un problema?
2. ¿Cómo afecta un log monolítico (ReAct) la depuración cuando el modelo comete un error con un padre de familia?
::
::/practica
