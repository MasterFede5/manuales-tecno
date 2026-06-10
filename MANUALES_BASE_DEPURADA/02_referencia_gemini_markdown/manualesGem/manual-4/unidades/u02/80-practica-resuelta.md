---
unidad: 2
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 02

::practica{titulo="Redactar el PRD v1.0 del Asistente Institucional Albatros en una sesión de 2 horas"}
**Problema.** Tu director te encargó "construir el Asistente". Tienes 2 horas antes de la junta del viernes. Necesitas un PRD de 1 página + brief para 3 módulos + 1 ADR del trade-off principal + DoD canónico. Todo asistido por IA.

**Paso 1 — Datos.**
- Insumos disponibles: 3 prompts versionados de la U1, presupuesto inicial $300/mes, plazo deseado 8 semanas, equipo de 3 personas.
- Stakeholders: dirección (decide), coordinadora académica (usa), staff administrativo (usa), padres (impactados), legal (revisa).
- Activos: repo prompts-asistente-albatros, dashboard LangFuse en demo, política de uso borrador.

**Paso 2 — Estrategia.**
1. PRD asistido por IA con meta-prompt patrón (subtema 2.1).
2. Stress-test con 3 críticas (devil's advocate, financiero, riesgos no listados).
3. Brief para los 3 módulos prioritarios.
4. ADR para el trade-off "calidad vs costo" del modelo.
5. DoD canónico copiado del checklist 2.3 con un ítem extra propio.

**Paso 3 — PRD v0.5 (35 min).**

Pego el meta-prompt patrón con mis datos en Claude Opus. Recibo PRD v0.5 con 8 secciones, 6 marcas `[PREGUNTA: ...]` y 4 `[SUPUESTO: ...]`. Las 5 preguntas críticas que devuelve:
- ¿Cuál es la métrica única que define éxito?
- ¿Qué pasa con consultas en horario nocturno?
- ¿Quién aprueba comunicados antes de salir?
- ¿Cómo se maneja un caso emocional (estudiante en crisis)?
- ¿Cuál es el plan de salida si en 6 meses dirección cambia de opinión?

Las contesto en 10 min y obtengo PRD v0.7.

**Paso 4 — Stress-test (15 min).**
- *Devil's advocate*: encuentra que la métrica "satisfacción" no es verificable; sugiere reemplazar por "tasa de resolución sin escalación humana ≥ 85 %".
- *Financiero*: pregunta por costo total a 12 meses, no solo construcción. Agrego "costo proyectado: $300 setup + $2 400 operación año 1".
- *Riesgos no listados*: alerta sobre dependencia única del proveedor LLM. Agrego "Riesgo R-007: cambio de precios o términos del proveedor → mitigación: validar Ollama local en U7".

PRD pasa a v0.9.

**Paso 5 — Briefs de los 3 módulos (40 min).**

Aplico la plantilla del subtema 2.2 a:
- B-014: Clasificador de solicitudes (entregable: prompt v2.0 + golden 30 ejemplos).
- B-015: Redactor de comunicados (entregable: prompt v1.0 + flujo de aprobación humana).
- B-016: Resumen ejecutivo de juntas (entregable: prompt v1.0 + integración Notion).

Cada brief: contexto, objetivo, audiencia, restricciones, entregable, métrica única, riesgo principal. Usé el modelo para redactar v0 y refiné en 5 min cada uno.

**Paso 6 — ADR del trade-off principal (15 min).**

`docs/decisiones/ADR-001-modelo-base.md` documenta la decisión de usar modelo híbrido (Haiku por defecto, escalar a Sonnet si confianza < 0.7). Costo proyectado, calidad esperada, alternativas consideradas, condición de revisión.

**Paso 7 — DoD del proyecto (10 min).**

Tomo el DoD canónico de 9 puntos del subtema 2.3 y le agrego un punto institucional propio:
> 10. Aprobación explícita de coordinadora académica antes de release a producción.

Lo guardo en `docs/DoD.md` y lo referencia el PRD.

**Paso 8 — Trazabilidad (10 min).**

Asigno IDs por capa (subtema 2.4):
- S-001 (estratégica): reducir 60 % carga staff.
  - F-014 (funcional): responder dudas inscripción → B-014, B-016.
  - F-015 (funcional): redactar comunicados → B-015.
- O-001 (operativa): rotación on-call + presupuesto $300/mes.

**Paso 9 — Verificación (5 min).**

Le pido al modelo: *"Lee este PRD y los 3 briefs. ¿Hay incoherencias? ¿Algún módulo quedaría fuera del alcance del PRD?"* Confirma coherencia. Detecto que B-016 cubre objetivo S-001 mejor que B-014; lo dejo documentado.

**Respuesta.** Llego a la junta del viernes con: PRD v1.0 (1 página), 3 briefs, 1 ADR, 1 DoD, mapa de trazabilidad. Tiempo total: 2 horas. La dirección lee el PRD en 4 minutos, hace 2 preguntas, ambas resueltas mostrando los briefs. **Aprobado**.

**Verificación final.** Comparto el repo con coordinadora académica y le pido que lea sin mí presente. Reporta entender qué se construirá v1, qué queda fuera y cuándo será evaluado. Validación social: el PRD funciona.

**Lección.** Las 6 técnicas de la unidad no son seis tareas paralelas: son **una sola cadena**. PRD → briefs → ADR → DoD → trazabilidad. Saltarse un eslabón deja el documento débil donde más cuesta.
::/practica

::practica{titulo="Cómo convertí un objetivo blando en métricas verificables sin pelearme con dirección"}
**Problema.** El director firma el PRD borrador, pero la métrica de éxito dice: *"el Asistente debe mejorar significativamente la atención a familias"*. Sabes que esa frase, en 90 días, no permite saber si fallaste o triunfaste. Necesitas reescribirla **antes de la junta del lunes** sin que dirección sienta que estás recortando ambición.

**Paso 1 — Diagnóstico del problema con la métrica.**
- "Mejorar" — ¿comparado contra qué línea base?
- "Significativamente" — ¿qué umbral?
- "Atención a familias" — ¿calidad? ¿velocidad? ¿cobertura? ¿las tres?

Sin línea base, sin umbral y sin dimensión específica, la métrica es **defensiva** (cualquier resultado se puede interpretar a favor o en contra).

**Paso 2 — Descomponer en dimensiones.**
Apunto en una tabla las 4 dimensiones de "atención":
- Calidad (¿qué tan bien resuelven?).
- Velocidad (¿qué tan rápido responden?).
- Cobertura (¿cuántos casos atienden sin escalación?).
- Equidad (¿responden igual a familias con diferente nivel socioeconómico?).

**Paso 3 — Línea base con datos viejos.**
Antes de proponer umbrales, mido **dónde estamos hoy**. Pido a la coordinadora 30 correos del último mes, los reviso a mano:
- Tiempo medio de primera respuesta: 6.4 horas.
- % resueltos sin escalación: 48 %.
- Calidad percibida (rúbrica de 5 criterios): 3.1/5.
- Equidad: no se mide.

Línea base lista.

**Paso 4 — Proponer 3 métricas (no 1).**
Convertir 1 métrica blanda en 3 duras es la jugada política: dirección no siente que recortas, siente que **traduzco**.

| Métrica | Línea base | Umbral v1 | Cómo medir |
|---|---|---|---|
| Tiempo de primera respuesta | 6.4 h | < 2 h en 90 % | timestamp evento + log Asistente |
| % resuelto sin escalación humana | 48 % | ≥ 70 % | clasificación de outcome semanal |
| Calidad percibida (rúbrica humana 1–5) | 3.1 | ≥ 4.0 promedio | encuesta post-respuesta n≥30/mes |

Equidad la dejo en `[plan v2]` con justificación: requiere instrumentación nueva y la postergamos a Q3.

**Paso 5 — Explicar al director con números, no con teoría.**
Junta de 10 minutos. Llevo una hoja con dos columnas:
- *Antes:* "mejorar significativamente atención" — no auditable.
- *Ahora:* tabla de 3 métricas con línea base y umbral.

Frase clave: *"si en 90 días el tiempo bajó de 6.4 h a 1.8 h, ¿podemos decirle al patronato que mejoramos significativamente?"*. El director responde "sí". Métrica firmada.

**Paso 6 — Documentar la conversación.**
ADR-002: *"métricas de éxito v1 — 3 indicadores numéricos con línea base medida; equidad postergada a v2 con justificación de instrumentación"*. Firmado por director + tú.

**Paso 7 — Implementación.**
Pido al desarrollador instrumentar los 3 logs en el dashboard del Episodio 3. Cada métrica con dueño, frecuencia de revisión y umbral de alerta.

**Respuesta.** El PRD v1.1 reemplaza la métrica blanda por 3 verificables. El patronato a 90 días tiene un dashboard con resultados objetivos. Si fallamos, sabremos por qué. Si triunfamos, podremos demostrarlo.

**Verificación.** A 30 días, una compañera audita el dashboard sin contexto previo: identifica las 3 métricas, su umbral y dónde estamos respecto a línea base. Si ella entiende, los stakeholders entienden.

**Lección.** Reescribir métricas blandas no es discusión política, es **trabajo de discovery**. Sin línea base medida, cualquier umbral es teórico. Mide primero, propón después, y entrega 3 métricas en lugar de 1 — una sola siempre se ve excesiva.
::/practica

::practica{titulo="Cómo decidí entre 'PRD de 1 página' y 'PRD de 3 páginas' para un módulo sensible"}
**Problema.** El nuevo módulo del Asistente es delicado: detecta y responde mensajes de **estudiantes en crisis emocional** (referencia a autolesión, indicadores de violencia familiar). El equipo legal pide documentación amplia. El director quiere "1 página como los demás". ¿Quién tiene razón?

**Paso 1 — Revisar el criterio de la unidad.**
La unidad dice: PRD de 1 página por defecto, 3 páginas cuando hay >3 stakeholders críticos con dolores divergentes y se requiere alinear lenguaje.

**Paso 2 — Mapear stakeholders del módulo sensible.**

| Stakeholder | Dolor / interés | Criticidad |
|---|---|---|
| Dirección | Reputación institucional | Alta |
| Coordinadora académica | Bienestar estudiantil | Alta |
| Equipo legal | Responsabilidad civil/penal | Alta |
| Psicóloga escolar | Protocolos clínicos | Crítica |
| Familias | Privacidad | Alta |
| Equipo técnico | Implementación | Media |
| Estudiantes | Confidencialidad | Crítica |

**7 stakeholders, 4 con dolores divergentes y nivel crítico.** Cumple criterio para PRD extendido.

**Paso 3 — Arquitectura del PRD extendido.**
- **Página 1 — núcleo ejecutivo** (idéntico al PRD de 1 página): visión, objetivos, no-objetivos, métricas, riesgos top 3.
- **Página 2 — protocolo clínico**: cuándo el Asistente responde, cuándo escala, a quién, en qué tiempo, con qué mensaje. Validado por psicóloga.
- **Página 3 — gobernanza**: privacidad, retención, acceso, auditoría, base legal del procesamiento, responsabilidad ante un fallo. Validado por legal.

Cada página firma uno o más stakeholders distintos.

**Paso 4 — Negociación con dirección.**
Argumento al director: *"1 página es la regla por buenas razones — la sigo en todos los demás módulos. Aquí necesito 3 porque tenemos 7 stakeholders y 2 de ellos (legal, psicóloga) **no entenderán** la página 1 sin la página 2 o la 3. Si recorto, no firman; si no firman, no se construye"*. Acepta.

**Paso 5 — Discovery con psicóloga (45 min).**
Antes de redactar la página 2, entrevista a la psicóloga escolar. Pregunta clave: *"¿en qué casos el Asistente debería NO responder y derivar de inmediato?"*. Lista 6 disparadores. Esos son los criterios de "no respuesta automática" del módulo.

**Paso 6 — Discovery con legal (30 min).**
Pregunta clave: *"¿qué pasa si el Asistente responde mal en un caso de crisis y la familia demanda?"*. Legal pide: (a) consentimiento informado familias; (b) log auditable de cada interacción; (c) escalación humana con SLA <30 min en horario escolar; (d) política de retención de 5 años. Eso es la página 3.

**Paso 7 — Redacción asistida.**
Para cada página, meta-prompt patrón con datos del discovery. Ronda con stakeholder dueño. Iteración de 3 vueltas hasta firma.

**Paso 8 — Validación cruzada.**
Junta de 30 minutos con los 7 stakeholders. Cada uno lee la página que firma + las otras como contexto. Detectan **una incoherencia**: la psicóloga escribió "escalación inmediata" y legal "<30 min". Aclaramos: "inmediata" significa "iniciada en <2 min, completada en <30 min". Reescribimos página 2 y 3 alineando lenguaje.

**Paso 9 — Documentación de la decisión.**
ADR-005: *"PRD del módulo crisis-emocional fue extendido a 3 páginas justificado por 7 stakeholders críticos con dolores divergentes. Volver a 1 página después de v2 si el módulo se simplifica"*.

**Respuesta.** PRD-crisis-v1.0 sale en 3 páginas, firmado por 7 stakeholders. La construcción puede arrancar con seguridad. El módulo nunca habría podido construirse con 1 página — el equipo legal **literalmente no firmaba** sin la página 3.

**Lección.** "1 página" no es regla religiosa, es **default razonable**. Cuando la heurística de la unidad (>3 stakeholders críticos divergentes) se cumple, defender 1 página es teatro. Lo importante no es páginas: es que **cada decisión quede capturada y firmada por quien la hereda**.
::/practica
