---
unidad: 2
seccion: taller
paginas_objetivo: 2
---

## Taller — PRD de una mini-feature en 60 minutos

::albatros{titulo="Redactas un PRD de mini-feature firmable en 60 minutos" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Puedes documentar una mini-feature del Asistente —no el Asistente entero, una sola pieza— en menos de una hora, con una persona externa al equipo aprobándola al final?

**Lo que harás.** Vas a tomar **una mini-feature concreta** del Asistente Institucional y producir su PRD de 1 página, brief, criterios de aceptación, ADR del trade-off principal y plan de rollback. Al final, alguien fuera del equipo —tu compañero, una profesora, tu pareja— firma que entendió qué se construirá.

**Materiales reales.**
- Editor markdown.
- LLM (Claude o ChatGPT plan gratis sirve).
- 1 mini-feature elegida de esta lista (o propia):
  - Botón "explicar para padres" en el Asistente (toma una respuesta técnica y la simplifica).
  - Notificación automática al staff cuando el Asistente detecta una solicitud urgente.
  - Histórico de las últimas 10 preguntas del usuario para reutilizar contexto.
  - Selector de idioma (es / en) en la respuesta del Asistente.
- 60 minutos sin interrupciones.
- 1 persona disponible 10 minutos al final para validación.

**Pasos (10).**

1. **Min 0–5 — Elige y enuncia.** Escribe en una línea: *"como [rol], quiero [acción] para [valor]"*. Si no cabe en una línea, la mini-feature aún no es tan mini —recórtala—.

2. **Min 5–15 — Discovery rápido.** Lista 5 preguntas que necesitas resolver antes de escribir nada. Si no tienes respuesta, marca `[SUPUESTO: ...]`. No te detengas a investigar — el supuesto es válido.

3. **Min 15–25 — Borrador asistido.** Pega en el LLM el meta-PRD del subtema 2.1 con tus datos reales. Recibe v0.5. Pega tal cual en tu editor.

4. **Min 25–35 — Stress-test express.** Pídele al modelo que critique v0.5 desde 3 ángulos: escéptico técnico (qué se rompe), financiero (cuánto cuesta operar), riesgo no listado (qué se les pasó). Incorpora las 3 críticas más fuertes. Pasa a v0.8.

5. **Min 35–40 — Criterios de aceptación.** Escribe **5 criterios verificables**, cada uno con cómo se prueba. Si un criterio dice "robusto" o "intuitivo", reescríbelo.

6. **Min 40–45 — ADR del trade-off principal.** En 5 líneas: contexto · decisión · alternativa rechazada · consecuencia esperada · revisión a fecha X.

7. **Min 45–50 — Plan de rollback.** En 3 líneas: cómo detectas que algo va mal · quién lo apaga · cómo se restaura el estado anterior. Si no puedes contestar las 3, la mini-feature aún no entra a producción.

8. **Min 50–55 — Empaqueta.** Junta todo en un solo documento `docs/mini-feature-XYZ-v1.0.md`. Verifica que **cabe en 1 página impresa** (1 800-2 000 palabras máximo). Si no cabe, recorta.

9. **Min 55–60 — Validación social.** Pásale el documento a la persona disponible. **No le expliques** mientras lee — solo observa qué subraya y qué pregunta. Apunta esas preguntas: son los huecos reales de tu PRD.

10. **Cierre — Firma.** Si la persona puede explicar con sus palabras qué se construirá, qué queda fuera y cuándo se considera hecho, le pides que firme al pie. Si no, identificas qué sección reescribir y agendas otra ronda de 30 min.

**Entregable.**
- `mini-feature-XYZ-v1.0.md` con: PRD 1 pp + 5 criterios + ADR + rollback.
- Notas de validación social (qué preguntó la persona externa).
- Firma o feedback explícito de la persona externa.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cabe en 1 pp | excede | cabe pero abigarrado | cabe y se lee fluido |
| Criterios verificables | "intuitivo" | numéricos | con cómo se prueba |
| ADR | informal | con decisión | con alternativa rechazada y revisión |
| Rollback | ausente | mencionado | 3 líneas claras |
| Validación social | no se hizo | persona leyó | persona explicó con sus palabras y firmó |
::/albatros
