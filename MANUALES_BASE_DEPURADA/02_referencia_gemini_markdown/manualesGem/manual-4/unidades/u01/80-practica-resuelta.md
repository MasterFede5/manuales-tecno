---
unidad: 1
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 01

::practica{titulo="Diseñar el prompt 'redactor-institucional-v1' aplicando las 8 técnicas de la unidad"}
**Problema.** El equipo del Asistente Institucional necesita un prompt que reciba una solicitud (motivo, fecha, alcance) y produzca un comunicado oficial. Tu tarea: diseñar la versión 1.0, evaluarla con golden set de 10 ejemplos y dejarla lista para A/B.

**Paso 1 — Datos.**
- Tipo de solicitudes: 4 (suspensión, evento, cambio de horario, recordatorio).
- Audiencia: padres de familia + estudiantes.
- Tono institucional: formal pero cercano, sin emojis, "usted".
- Output esperado: JSON con `comunicado_humano` (texto) + `metadata` (categoria, fecha, requiere_revision).

**Paso 2 — Estrategia (qué técnicas aplico de la unidad).**
- 1.1 Estructura XML para separar role/context/task/constraints.
- 1.2 Meta-prompting con Claude Opus para generar v0.
- 1.3 CoT mínimo para que valide hechos antes de redactar.
- 1.6 Few-shot estratégico con 3 ejemplos diversos (suspensión, evento, queja procesada).
- 1.7 Constrained output con schema JSON estricto.
- 1.8 Golden set de 10 ejemplos para validar.

**Paso 3 — Diseño de v0 (meta-prompt).**

Pego en Claude el meta-prompt patrón (§1.2) con los datos del paso 1. Recibo v0 con estructura XML completa, 5 secciones y un schema JSON. Tiempo: 4 minutos.

**Paso 4 — Refinamiento iterativo.**
- Ejecuto v0 con 5 inputs reales del archivo histórico.
- Crítica del modelo sobre v0: "no maneja bien fechas relativas (mañana, próximo lunes)".
- Reescribo a v1 agregando `<date_resolution>` con regla: "convierte fechas relativas a absolutas usando contexto del prompt".

**Paso 5 — Few-shot (curaduría).**
Selecciono 3 ejemplos:
- Caso típico: suspensión por mantenimiento.
- Caso con tono difícil: cambio de horario tras quejas.
- Caso de borde: evento con dato pendiente (`[dato pendiente — confirmar]`).

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
- 4 casos típicos (uno por cada categoría).
- 3 casos con dato pendiente.
- 2 casos con tono delicado.
- 1 caso ambiguo (categoría borderline).

Construyo `evals/redactor-institucional-v1.jsonl` con cada `input` y `output_esperado` redactado por la coordinadora académica.

**Paso 8 — Corrida automática y rúbrica.**

| Métrica | Resultado |
|---|---|
| Validez de schema | 10/10 |
| Categoría correcta | 9/10 (1 falló entre evento/recordatorio) |
| Fecha resuelta correctamente | 10/10 |
| Tono institucional (rúbrica humana 1-5) | 4.3 promedio |
| Datos pendientes detectados | 3/3 |
| Latencia mediana | 2.1 s |
| Costo por llamada | $0.012 |

**Paso 9 — Versionado y publicación.**
- `prompts/redactor-institucional/v1.0.xml` + `v1.0.eval.json` en Git.
- CHANGELOG: "v1.0 release inicial con 9/10 categoría y 4.3/5 tono".
- Plan canary: 5 % del tráfico durante 5 días, comparando contra el flujo manual actual.

**Respuesta.** El prompt `redactor-institucional-v1.0` queda **listo para canary**. La única falla del golden (1 confusión categórica) se documenta como issue para v1.1: agregar mini few-shot de la confusión específica.

**Verificación.** Un revisor independiente del equipo replica el golden con outputs frescos. Obtiene 9/10 también, confirmando que no fue suerte.

**Lección.** Las 8 técnicas no son menú a la carta: son **un proceso completo**. Saltarse evaluación o constrained output deja un prompt frágil. Aplicarlas en orden produce algo desplegable en una mañana.
::/practica

::practica{titulo="Cómo evalué v3 vs v4 del clasificador y decidí no promover"}
**Problema.** Hace tres semanas el `clasificador-solicitudes-v3` está en producción al 100 %. Una compañera propone `v4` afirmando que "redacta mejor las razones de clasificación". Necesitas decidir antes del viernes si promueves o mantienes.

**Paso 1 — Establecer criterios de aceptación medibles.**
- Calidad: precisión global ≥ v3 (no caer ni 1 punto en macro-F1 sobre 50 ejemplos).
- Costo: incremento ≤ 15 %.
- Latencia: incremento ≤ 25 %.
- Trazabilidad: campo `razon` en JSON (es la promesa de v4).

**Paso 2 — Refrescar el golden set.**
El golden viejo tiene 30 ejemplos. Lo amplío a 50 incluyendo 8 casos de borde nuevos detectados en producción este mes. El borde más jugoso: solicitudes mixtas (admisión + cambio de horario en un mismo correo).

**Paso 3 — Corrida pareada.**
Mismo input al mismo tiempo, mismo modelo base, mismo schema. Logueo en hoja de cálculo con columnas: `id_input`, `categoria_real`, `categoria_v3`, `categoria_v4`, `razon_v4`, `latencia_v3`, `latencia_v4`, `tokens_v3`, `tokens_v4`.

**Paso 4 — Resultados crudos.**

| Métrica | v3 | v4 | Δ |
|---|---|---|---|
| Macro-F1 | 0.91 | 0.89 | -0.02 |
| Precisión "admisión" | 0.94 | 0.92 | -0.02 |
| Precisión "cambio_horario" | 0.88 | 0.90 | +0.02 |
| Latencia mediana | 1.8 s | 2.6 s | +44 % |
| Costo/llamada | $0.011 | $0.018 | +64 % |
| Razón en JSON | no | sí | feature nueva |

**Paso 5 — Análisis de bordes.**
Reviso una a una las 8 solicitudes mixtas. v3 acierta 6/8. v4 acierta 5/8. La razón que v4 escribe es **convincente pero no más correcta** —en 2 casos da razones plausibles para una categoría equivocada, lo que es **peor que decir "no sé"**.

**Paso 6 — Decisión.**
- v4 viola dos criterios duros: macro-F1 cae 2 puntos y costo sube 64 %.
- La feature `razon` es deseable pero no rescata las regresiones.
- **Decisión: no promover. Pedir v3.1** que mantenga el motor de v3 y agregue `razon` como campo opcional —solo cuando el modelo tenga confianza— sin re-arquitectura.

**Paso 7 — Comunicación.**
Escribo entrada en `decisiones-de-diseno.md`:

> *2026-04-09 — Rechazo de v4 del clasificador.* Datos: macro-F1 0.91 → 0.89, costo +64 %, latencia +44 %. La feature `razon` se rescata como issue v3.1. Decisión revisable en 30 días si v3.1 incorpora `razon` sin regresión.

**Paso 8 — Cerrar el ciclo.**
Abro issue `v3.1-razon-opcional` con criterios de aceptación. Agendo revisión a 14 días.

**Respuesta.** v3 se mantiene en producción. v4 queda archivado en `prompts/clasificador/explorado/v4-rejected/` con la documentación de por qué.

**Lección.** Una mejora **plausible** no es una mejora **demostrada**. Sin golden y sin criterios duros, "se siente mejor" es enemigo del proyecto. Tu repo tiene que dejar registro de los **rechazos**, no solo de los lanzamientos.
::/practica

::practica{titulo="Cómo escogí entre prompt chaining y ReAct para 'respuesta unificada a correo de papá'"}
**Problema.** La coordinadora reenvía un correo de un papá con 3 dudas: (1) fechas de entrega del proyecto final, (2) si su hija puede salir antes los jueves por terapia, (3) cómo solicitar cambio de profesor. Necesita una sola respuesta cálida y precisa. ¿Prompt chaining o ReAct?

**Paso 1 — Mapear la tarea.**
- Detectar dudas (clasificación interna).
- Para cada duda: buscar respuesta en el reglamento o calendario.
- Redactar respuesta unificada.

**Paso 2 — Hipótesis A: prompt chaining (3 eslabones).**
Eslabón 1 (extractor): correo → JSON con `dudas[]`.
Eslabón 2 (resolutor por duda): para cada duda → consulta RAG → respuesta corta + cita.
Eslabón 3 (redactor): JSON con respuestas → comunicado unificado en tono cálido.

**Paso 3 — Hipótesis B: ReAct un solo prompt.**
Un solo prompt con razonamiento entrelazado: thought → action (search reglamento) → observation → thought → ... → final answer. Modelo decide cuántas búsquedas hace.

**Paso 4 — Pruebas de diseño con 5 inputs reales.**
- Input 1 (3 dudas claras): A acertó 3/3, B acertó 3/3.
- Input 2 (1 duda implícita): A perdió la implícita en el extractor; B la capturó porque el thought-loop la "descubrió" al razonar.
- Input 3 (duda fuera de reglamento, requiere "no sé"): A respondió "no sé" en el eslabón 2; B inventó un artículo. **Punto rojo para B.**
- Input 4 (5 dudas): A escaló bien; B se quedó sin tokens en thought y dejó respuestas truncas.
- Input 5 (duda sensible — separación parental): A dejó al redactor decidir tono; B mezcló razonamiento con redacción y el output reveló el reasoning interno al papá. **Punto rojo grave para B.**

**Paso 5 — Comparación de costo y trazabilidad.**

| Criterio | Chaining (A) | ReAct (B) |
|---|---|---|
| Acierto sobre 5 | 4/5 | 2/5 |
| Costo medio | $0.038 | $0.052 |
| Latencia | 6.2 s | 4.1 s |
| Trazabilidad | logs por eslabón | un solo log monolítico |
| Riesgo de leak de razonamiento | bajo | alto |
| Mantenibilidad | edito un eslabón | edito un prompt entero |

**Paso 6 — Decisión y justificación.**
**Elijo prompt chaining.** Razones: (a) trazabilidad por eslabón es esencial para auditar respuestas a familias; (b) menor riesgo de inventar artículos; (c) cada eslabón se mejora aislado. Pago latencia mayor (~2 s) — aceptable porque el flujo es asíncrono (correo, no chat en vivo). Costo +37 % — aceptable dada la criticidad.

**Paso 7 — Mitigación de la única falla de A.**
La duda implícita la perdió el extractor. Solución: meta-promptear v1.1 del extractor pidiéndole identificar dudas explícitas **e implícitas**, con few-shot que muestre 2 casos de duda implícita.

**Respuesta.** La cadena de 3 eslabones queda en `prompts/respuesta-unificada-correo-papa/v1.0/` con golden de 20, schema estricto y eval cruzada por la coordinadora.

**Lección.** Chaining vs ReAct no es debate religioso: es decisión basada en **trazabilidad**, **riesgo** y **modo de falla**. ReAct brilla cuando el espacio de acciones es grande y exploratorio; chaining brilla cuando necesitas auditar cada paso. Aquí, una familia preguntando reglamento, ganó la auditabilidad.
::/practica
