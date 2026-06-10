---
unidad: 2
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 02

::practica{titulo="Redactar el PRD v1.0 del Asistente Institucional Albatros en una sesión de 2 horas"}
**Problema.** 
- Tu director te encargó "construir el Asistente". 
- Tienes 2 horas antes de la junta del viernes. 
- Necesitas un PRD de 1 página, brief para 3 módulos, 1 ADR y DoD canónico.
- Todo asistido por IA.

**Paso 1 — Datos.**
- **Insumos:** 3 prompts de U1, presupuesto $300/mes, plazo 8 semanas, equipo de 3.
- **Stakeholders:** Dirección (decide), académica (usa), staff (usa), padres (impactados), legal (revisa).
- **Activos:** Repo prompts, dashboard LangFuse, política borrador.

**Paso 2 — Estrategia.**
1. PRD asistido por IA con meta-prompt.
2. Stress-test con 3 críticas (financiero, riesgos, etc.).
3. Brief para los 3 módulos prioritarios.
4. ADR para trade-off "calidad vs costo".
5. DoD canónico + 1 ítem propio.

**Paso 3 — PRD v0.5.**
- Pego el meta-prompt en Claude Opus. 
- Recibo PRD v0.5 con 6 marcas y 5 preguntas críticas.
- ¿Cuál es la métrica de éxito? ¿Qué pasa de noche?
- Contesto las preguntas en 10 min y obtengo PRD v0.7.

**Paso 4 — Stress-test.**
- *Devil's advocate*: "Satisfacción" no es verificable. Uso "resolución sin escalación ≥ 85 %".
- *Financiero*: Costo a 12 meses. Agrego "$300 setup + $2 400 año 1".
- *Riesgos*: Dependencia del LLM. Agrego "Mitigación: validar Ollama local".
- Resultado: PRD v0.9.

**Paso 5 — Briefs (40 min).**
- **B-014 (Clasificador):** Prompt v2.0 + 30 ejemplos.
- **B-015 (Comunicados):** Prompt v1.0 + flujo de aprobación.
- **B-016 (Resumen juntas):** Prompt v1.0 + integración Notion.
- Cada brief incluye: contexto, entregable, métrica y riesgo.

**Paso 6 y 7 — ADR y DoD.**
- **ADR-001:** Decisión de usar modelo híbrido (Haiku por defecto, escalar a Sonnet).
- **DoD:** 9 puntos canónicos + 1 extra ("Aprobación académica previa").

**Paso 8 y 9 — Trazabilidad y Verificación.**
- Asigno IDs: S-001 (reducir carga) → F-014, F-015 → B-014, B-015, B-016.
- El modelo verifica coherencia: Confirma que todo cuadra.

::interioriza
Preparar esto en 2 horas es como armar el equipaje de mano antes de un vuelo: 
No puedes llevar tu ropero entero (documentación de 50 páginas), 
solo lo esencial (PRD, ADR, briefs) bien doblado y listo para pasar seguridad (aprobación de dirección).
::/interioriza

**Respuesta y Validación.** 
- Junta de 2 horas. Dirección lee en 4 min. 
- Hace 2 preguntas. Se resuelven con los briefs. **Aprobado**.
- Coordinadora valida socialmente el documento.

**Lección.** 
- Las técnicas son **una sola cadena**: PRD → briefs → ADR → DoD → trazabilidad. 
- Saltarse un eslabón debilita todo.
::/practica

::pausa
**Deducción:** Si omites el ADR en esta cadena, ¿qué objeción de la junta te dejará sin respuesta documentada?
1. [ ] Cuánto costará el proyecto.
2. [ ] Por qué elegiste un modelo más barato en lugar del más preciso.
3. [ ] Quién aprueba los comunicados.
::/pausa

::practica{titulo="Cómo convertí un objetivo blando en métricas verificables sin pelearme con dirección"}
**Problema.** 
- El director firma: *"mejorar significativamente la atención a familias"*.
- Esa métrica es inauditable a los 90 días.
- Debes reescribirla sin que parezca un recorte de ambición.

**Paso 1 y 2 — Diagnóstico y Dimensiones.**
- ¿Mejorar contra qué? ¿Significativo es cuánto? 
- Dimensiones de la atención:
  - Calidad (resolución correcta).
  - Velocidad (tiempo).
  - Cobertura (casos sin escalar).
  - Equidad (mismo trato a todos).

**Paso 3 — Línea base.**
- Reviso 30 correos del mes anterior.
- Tiempo medio: 6.4 h. % resueltos: 48 %. Calidad: 3.1/5.

**Paso 4 — Proponer 3 métricas duras.**
- **Velocidad:** De 6.4 h a < 2 h (90%).
- **Cobertura:** De 48 % a ≥ 70 % sin escalar.
- **Calidad:** De 3.1 a ≥ 4.0 promedio.
- *Equidad* pasa a v2 por falta de instrumentación.

::interioriza
Medir sin línea base es como hacer dieta sin pesarse el primer día. 
Si el director te pide "bajar de peso significativamente", necesitas saber 
cuántos kilos pesan hoy los procesos del colegio para luego demostrar que el Asistente funcionó.
::/interioriza

**Paso 5 y 6 — Venta y Documentación.**
- Pregunta clave: *"Si bajamos de 6.4 h a 1.8 h, ¿hemos mejorado significativamente?"*
- El director dice "sí". Métrica firmada.
- **ADR-002:** Documenta esta decisión y postergación de equidad.

**Respuesta y Verificación.**
- El PRD v1.1 reemplaza métricas blandas por verificables.
- Dashboard instrumentado. Stakeholders auditan sin contexto.

**Lección.** 
- Reescribir métricas es **trabajo de discovery**, no política. 
- Mide primero, propón después. Tres métricas diluyen la presión de una sola.
::/practica

::pausa
**Deducción:** ¿Por qué es políticamente astuto proponer tres métricas en lugar de una?
1. [ ] Porque marea al director con datos técnicos.
2. [ ] Porque si una falla ligeramente, las otras dos pueden seguir demostrando el valor general del proyecto.
3. [ ] Porque requiere más presupuesto de instrumentación.
::/pausa

::practica{titulo="Cómo decidí entre 'PRD de 1 página' y 'PRD de 3 páginas' para un módulo sensible"}
**Problema.** 
- Módulo sensible: detecta crisis emocionales en estudiantes.
- Legal pide documentación extensa. Director quiere 1 página. 

**Paso 1 y 2 — Mapeo de Stakeholders.**
- **Dirección / Académica / Legal / Familias:** Intereses críticos y divergentes.
- **Psicóloga / Estudiantes:** Protocolos y privacidad crítica.
- Total: 7 stakeholders, 4 divergentes. Requiere PRD extendido.

**Paso 3 — Arquitectura del PRD (3 páginas).**
- **Página 1:** Visión, métricas, top riesgos (igual al de 1 pág).
- **Página 2:** Protocolo clínico (aprobado por psicóloga).
- **Página 3:** Gobernanza y bases legales (aprobado por legal).

**Paso 4, 5 y 6 — Discovery y Negociación.**
- Argumento al director: Si recorto, Legal no firma. Si no firman, no hay Asistente.
- **Psicóloga (45 min):** Define 6 disparadores de "no respuesta automática".
- **Legal (30 min):** Pide logs, SLA <30 min, retención 5 años.

::interioriza
Un PRD extendido por temas legales/clínicos es como un seguro a todo riesgo escolar. 
No lo compras porque sea breve, lo compras porque te cubre la espalda 
cuando un estudiante requiere derivación inmediata y no quieres zonas grises.
::/interioriza

**Paso 7 y 8 — Redacción y Validación.**
- Redacción asistida con IA por secciones.
- Junta de 30 min con 7 stakeholders. 
- Alinean "inmediata" (psicóloga) con "<30 min" (legal).

**Paso 9 — Decisión Documentada.**
- **ADR-005:** PRD extendido a 3 páginas justificado por criticidad.

**Respuesta y Lección.** 
- PRD-crisis-v1.0 aprobado y firmado por los 7.
- "1 página" es **default razonable**, no regla religiosa. 
- Lo vital es que cada decisión crítica tenga firma de quien asume el riesgo.
::/practica

::pausa
**Deducción:** El PRD de 3 páginas en este módulo se justificó principalmente por:
1. [ ] El presupuesto asignado al modelo LLM.
2. [ ] La necesidad de alinear a múltiples stakeholders críticos con intereses divergentes (Legal vs Clínica).
3. [ ] La falta de tiempo para resumirlo en una sola página.
::/pausa
