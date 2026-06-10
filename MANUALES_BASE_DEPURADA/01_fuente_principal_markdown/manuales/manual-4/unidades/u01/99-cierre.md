---
unidad: 1
seccion: cierre
paginas_objetivo: 2
---

## Cierre y autoevaluación — Unidad 01

Cerraste la unidad de Prompt Engineering Avanzado. Ahora puedes:

1. **Estructurar prompts en XML** con secciones semánticas (role, context, task, constraints, examples, output_format).
2. **Meta-promptear** para que el modelo escriba sus mejores prompts e iterar con bucle críticar–reescribir.
3. **Aplicar CoT y ReAct** para forzar razonamiento explícito y conectar con herramientas externas.
4. **Usar Self-consistency y Tree-of-Thoughts** según el tipo de problema (preciso vs. abierto).
5. **Encadenar prompts** en pipelines lineales, ramificados o condicionales con contratos entre eslabones.
6. **Curar few-shot estratégico** con diversidad, calidad uniforme y orden intencional.
7. **Restringir outputs** con JSON Schema y los mecanismos del proveedor (Structured Outputs, function calling).
8. **Evaluar prompts** con golden sets, rúbricas humanas y A/B canary.

> **Frase puente.** Tienes prompts versionados, evaluados y desplegables. Pero un prompt aislado no es un sistema: una organización necesita **especificaciones** que lo encuadren — qué resuelve, qué no, quién lo usa, qué métricas lo gobiernan. La Unidad 2 te lleva a redactar el **PRD del Asistente Institucional Albatros**, donde cada prompt versionado será un activo identificable del producto.

---

### Autoevaluación (rúbrica de 5 niveles)

| Saber | 1 — Inicial | 2 | 3 — Suficiente | 4 | 5 — Excelente |
|---|---|---|---|---|---|
| **Estructura XML** | texto plano | uso etiquetas a veces | secciones consistentes | XML editable con justificación | plantilla del equipo, autodescriptiva |
| **Meta-prompting** | escribo a mano | uso modelo a veces | bucle críticar-reescribir | con criterios de éxito explícitos | flujo documentado y reusable |
| **CoT / ReAct** | respuesta directa | "piensa paso a paso" | scratchpad estructurado | ReAct con herramientas | trazabilidad y tope de pasos |
| **Self-consistency / ToT** | uso una sola corrida | varias a veces | aplico según tipo de problema | con voto y arbitraje | con presupuesto y log |
| **Prompt chaining** | mega-prompt único | 2-3 pasos sin contrato | pipeline con contratos | con paralelización | con router y observabilidad |
| **Few-shot** | sin ejemplos | ejemplos al azar | 3 diversos curados | dynamic few-shot con embeddings | banco curado y mantenido |
| **Constrained output** | texto libre | pido JSON en prompt | JSON mode | function calling con schema | schema estricto validado en runtime |
| **Evaluación** | "se siente bien" | smoke test | golden set + rúbrica | A/B canary | proceso continuo con métricas |
| **Versionado** | notas sueltas | un archivo | semver + CHANGELOG | repo con CONTRIBUTING | equipo lo opera con PRs |

### Pregunta de cierre

> Tu repositorio de prompts tiene 3 versiones para el "clasificador-solicitudes": v1.0, v1.1, v2.0. La v2.0 metió una mejora pero también un sutil bug que solo se ve en 2 % del tráfico. **Diseña** el flujo que permitiría a tu equipo: (a) detectar el bug rápido, (b) hacer rollback sin perder los avances de v2, (c) evitar que el bug regrese en v2.1. Anota tu propuesta en 5 pasos numerados con tiempos.

### Conexión con la siguiente unidad

En **U2 — Especificaciones de Tareas y Proyectos** vas a redactar el PRD del Asistente Institucional. Lleva contigo dos artefactos de esta unidad: tu **lista de prompts versionados** (que serán activos identificables del PRD) y tu **proceso de evaluación** (que será una sección de Definition of Done en el PRD).
