---
unidad: 2
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 02

> Cada ejercicio entrena un movimiento concreto del PRD. Trabajas con tu repo de la U1 abierto y un editor markdown a la mano.

### Sección A — PRD asistido por IA (2.1)

::act-fill{titulo="A1. Las 8 secciones obligatorias del PRD"}
Llena los huecos. Un PRD de 1 página debe tener **siempre** estas 8 secciones, en este orden:

1. _____________ y problema (1 párrafo).
2. Objetivos _____________ (numerables, con métrica).
3. _____________-objetivos (qué queda explícitamente fuera).
4. Métricas de _____________ (verificables, con cómo medir).
5. _____________ (audiencia: rol + dolor + valor recibido).
6. _____________ (lo que sí entra en v1.0).
7. _____________ (los principales 3-5 con mitigación).
8. Plan de _____________ y revisión (cuándo se reabre).
::/act-fill

::act-mcq{titulo="A2. Anti-patrones del PRD"}
1. "El sistema debe ser robusto y escalable" en métricas de éxito es:
   - [ ] Aceptable si el equipo entiende
   - [x] Defectuoso por no ser verificable por un tercero
   - [ ] Aceptable solo si lo escribió un senior
   - [ ] Aceptable si va con un disclaimer

2. La sección **más** subestimada de un PRD según la unidad es:
   - [ ] Métricas
   - [x] No-objetivos
   - [ ] Riesgos
   - [ ] Calendario

3. ¿Cuándo conviene escribir un PRD de 3 páginas en vez de 1?
   - [x] Cuando hay >3 stakeholders críticos con dolores divergentes y se requiere alinear lenguaje
   - [ ] Siempre que haya tiempo
   - [ ] Cuando el director pida formalidad
   - [ ] Cuando haya presupuesto > $50k
::/act-mcq

::act-case{titulo="A3. Convierte un objetivo blando en métrica" lineas=8}
Tu director firma: *"el Asistente debe mejorar la atención a familias"*. Reescribe esa frase como **3 métricas verificables** (numéricas, con cómo se mide y umbral). Mínimo una métrica de calidad, una de eficiencia, una de cobertura.
::/act-case

### Sección B — Plantillas Albatros: brief, scope, criterios (2.2)

::act-fill{titulo="B1. Brief mínimo de un módulo"}
Un brief no es un PRD: es una orden de trabajo para **un módulo**. Sus 7 campos obligatorios:

- _____________: 1-2 líneas de qué se construye.
- _____________: por qué importa para el PRD (vincula a S-NNN).
- _____________: rol que lo usará y dolor concreto que alivia.
- _____________: lo que entra · lo que no entra (al menos 3 fuera).
- _____________ de aceptación: lista verificable (≥4).
- _____________: una sola, con cómo medirla.
- _____________: el principal y su mitigación.
::/act-fill

::act-table{titulo="B2. Completa scope de los 3 módulos del Asistente"}
| Módulo | IN scope (3) | OUT scope (3) | Criterio de aceptación principal |
|---|---|---|---|
| Clasificador de solicitudes |  |  |  |
| Redactor de comunicados |  |  |  |
| Resumen ejecutivo de juntas |  |  |  |
::/act-table

### Sección C — Definition of Done (2.3)

::act-order{titulo="C1. Orden del checklist DoD canónico"}
Ordena los 9 ítems del DoD canónico (de la U2.3) por momento de aplicación:

[ ] Documentación actualizada (README, CHANGELOG)
[ ] Schema validado en runtime
[ ] Smoke test con 3 inputs reales
[ ] Plan de rollback escrito y probado
[ ] Approval de stakeholder no técnico
[ ] Golden set ≥ 30 ejemplos pasando umbral
[ ] Costo y latencia medidos en producción shadow
[ ] Tests unitarios verdes (si aplica)
[ ] Métrica única definida y monitoreada
::/act-order

::act-tf{titulo="C2. Mitos del DoD"}
1. Si el módulo pasa el golden set, ya está listo para producción. ( ) ____________________________________________
2. El DoD debe ser idéntico para todos los módulos. ( ) ____________________________________________
3. "Approval de stakeholder no técnico" es opcional cuando el equipo es senior. ( ) ____________________________________________
::/act-tf

### Sección D — Especificaciones por capas (2.4)

::act-match{titulo="D1. Capa → artefacto típico"}
| Capa | Artefacto típico |
|---|---|
| 1. Estratégica | a) Brief de módulo |
| 2. Funcional | b) ADR de elección tecnológica |
| 3. Técnica | c) PRD y OKRs |
| 4. Operativa | d) Runbook on-call y rotación |
::/act-match

::act-fill{titulo="D2. ID por capa"}
Asigna el prefijo correcto a cada item según la capa:

- "Reducir 60 % la carga del staff administrativo" → ____-001
- "Conectar el Asistente con la base de datos de matrícula" → ____-027
- "Responder dudas de inscripción en <2 min" → ____-014
- "Rotación on-call: lunes-jueves coordinadora, viernes tú" → ____-003
::/act-fill

### Sección E — Spec-driven prompting (2.5)

::act-case{titulo="E1. Caso — convierte spec en prompt" lineas=10}
Tu spec dice: *"el clasificador devuelve `categoria_principal` (uno de 5 valores), `confianza` (0-1) y `etiquetas_secundarias` (array máx. 3). Si confianza < 0.7, agrega `requiere_revision_humana=true`."* Escribe el prompt XML que materializa la spec **sin desviarse** y deja claro qué prueba va a confirmar que prompt y spec siguen sincronizados.
::/act-case

::act-mcq{titulo="E2. Cuándo activar spec-driven"}
Spec-driven prompting es **necesario** cuando:
- [ ] Estás explorando un prototipo en una tarde
- [ ] La salida es un texto libre que solo lee un humano
- [x] La salida alimenta otro sistema y un cambio de schema rompe pipelines downstream
- [ ] El equipo es de 1 persona y no hay rotación
::/act-mcq

### Sección F — Trade-offs y ambigüedad (2.6)

::act-table{titulo="F1. Cono de incertidumbre por fase"}
Completa la tabla con el rango ±% típico de incertidumbre y la acción concreta para cerrar el cono:

| Fase | Rango ±% | Acción para reducir |
|---|---|---|
| Idea inicial |  |  |
| Discovery / entrevistas |  |  |
| PRD aprobado |  |  |
| Briefs detallados |  |  |
| Smoke test del módulo |  |  |
::/act-table

::act-case{titulo="F2. Caso — escribes el ADR del trade-off principal" lineas=14}
Tu director propone usar GPT-5 (calidad alta, costo $0.04/llamada) para todo. La coordinadora prefiere Claude Haiku (calidad media, costo $0.004/llamada). El presupuesto de operación anual es $2 400. El volumen estimado es 60 mil llamadas/año.

Escribe el **ADR-001** con: contexto · decisión · alternativas consideradas · consecuencias · cuándo se revisa. Argumenta con números, no con preferencias.
::/act-case

---

## Clave de respuestas

**A1.** Visión · principales · No · éxito · Usuarios · Alcance · Riesgos · rollback.

**A2.** 1-b · 2-b · 3-a.

**A3.** Sugerencia (acepta variantes razonables): (1) calidad — *"satisfacción declarada por familia ≥ 4.2/5 en encuesta post-respuesta, n≥30/mes"*; (2) eficiencia — *"tiempo mediano de primera respuesta < 2 horas en 90 % de los casos"*; (3) cobertura — *"≥ 70 % de respuestas resueltas sin escalación a humano"*.

**B1.** Título · Contexto · Usuario · Alcance · Criterios · Métrica única · Riesgo principal.

**B2.** Sugerencia parcial: clasificador IN: 5 categorías + confianza + etiquetas; OUT: respuestas, integración n8n, multi-idioma. Criterio principal: macro-F1 ≥ 0.85 sobre golden 50. (Acepta variantes razonables para los otros 2.)

**C1.** Orden propuesto: Métrica única definida → Schema validado en runtime → Tests unitarios verdes → Smoke test 3 inputs reales → Golden set ≥ 30 pasando umbral → Costo y latencia en shadow → Plan de rollback escrito → Documentación actualizada → Approval stakeholder no técnico.

**C2.** 1) Falso — golden es **una** condición; faltan rollback, costo medido, approval, etc. 2) Falso — el DoD canónico es base; cada módulo le agrega ítems propios (ej. revisión legal en módulos sensibles). 3) Falso — el approval no es prueba técnica, es validación social que protege al equipo de retrabajo.

**D1.** 1-c · 2-a · 3-b · 4-d.

**D2.** S-001 · T-027 · F-014 · O-003.

**E1.** Respuesta libre. Verifica: (a) prompt usa los nombres exactos de campos del schema; (b) la regla de `requiere_revision_humana` está explícita en `<constraints>`; (c) la prueba es **golden con campos validados por contrato JSON Schema** + un test que falla si el prompt menciona un campo que el schema no incluye.

**E2.** c.

**F1.** Sugerencia: idea inicial ±300 % (entrevistar stakeholders) · discovery ±100 % (PRD borrador) · PRD aprobado ±50 % (briefs) · briefs ±25 % (smoke test) · smoke ±10 % (golden completo).

**F2.** Respuesta libre. Una buena respuesta calcula: 60k × $0.04 = $2 400 (consume **todo** el presupuesto). 60k × $0.004 = $240 (deja $2 160 para imprevistos). Decisión: Haiku por defecto, escalar a Sonnet/GPT cuando confianza < 0.7. Revisión a 90 días con datos de calidad reales.
