---
unidad: 10
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 10

> Banco de práctica para estrategia, costos y gobernanza del Asistente Institucional: comparativo de planes, costos por tokens y optimización, política institucional, métricas de retorno y confidencialidad de datos sensibles. Privilegia ejercicios de **decisión presupuestal**, **lectura de plan** y **construcción de matriz**. Resuelve antes de mirar la clave.

---

### Bloque A — Comparativo de planes (10.1)

::act-mcq{titulo="Decisión de proveedor"}
1. Tu institución usa Microsoft 365 + Outlook + Teams para todo el staff. La opción default debería ser:
   - [ ] ChatGPT Team
   - [ ] Claude Pro
   - [x] Microsoft 365 Copilot (integración Office inigualable)
   - [ ] Gemini Workspace

2. Si el patronato exige máxima privacidad y volumen alto pero hay capacidad TI:
   - [ ] ChatGPT Enterprise
   - [ ] Pagar las 4 plataformas premium
   - [x] Stack soberano híbrido (Claude Pro para staff técnico + Ollama local + Open WebUI multi-user)
   - [ ] Solo planes free

3. Para producción de contenido especializado de alto nivel (whitepapers, materiales pedagógicos), el plan con mejor razonamiento es:
   - [ ] ChatGPT Plus
   - [x] Claude Pro / Team / Enterprise (Opus 4.7 con MCP nativo)
   - [ ] Copilot M365
   - [ ] Gemini Workspace
::/act-mcq

::act-table{titulo="Costo total anual por opción para 50 staff"}
| Opción | Plan(es) | Costo mensual | Costo anual |
|---|---|---|---|
| A — Stack OpenAI mainstream | 50 × ChatGPT Team $30 | | |
| B — Stack mixto premium | 30 × Gemini Workspace + AI $20 + 5 × Claude Pro $20 | | |
| C — Stack Microsoft completo | 50 × M365 + Copilot $30 + 5 × ChatGPT Team adicional | | |
| D — Stack soberano híbrido | 5 × Claude Pro + Ollama local + Open WebUI | | |
::/act-table

::act-fill{titulo="Los 5 criterios de decisión"}
Los criterios para elegir proveedor:

1. **¿Dónde vive ya tu _____________?** (M365 → Copilot; Google → Gemini; sin preferencia → libre).
2. **¿_____________ estricta?** (Enterprise plans + Local con Ollama).
3. **¿Volumen _____________?** (Local soberano gana en TCO arriba de cierto volumen).
4. **¿Capacidad _____________?** (sin → cloud all-in; con → local soberano fuerte).
5. **¿_____________ específica?** (HIPAA → cloud Enterprise certificado).

Anti-patrones: pagar _____________ plataformas para todos = $4 500/mes innecesarios; lock-in temprano (plan Enterprise a 3 años puede ser jaula, negocia _____________ año primero); sin auditoría de uso, pagas planes que nadie usa.
::/act-fill

---

### Bloque B — Costos por tokens y optimización (10.2)

::act-match{titulo="Técnica de optimización → ahorro estimado"}
| Técnica | Efecto |
|---|---|
| 1. Modelo correcto por tarea (Haiku para clasificación) | a) ~85 % menos costo en la parte cacheable, ideal para system prompt + RAG largos |
| 2. Prompt caching | b) 50 % descuento, latencia 24h, ideal para tareas asíncronas |
| 3. Batch API | c) Hasta 18× más barato vs. usar Opus en todas las tareas |
| 4. Reducción de tokens | d) Cada palabra extra cuesta; edita prompts y limita `max_tokens` |
| 5. RAG eficiente | e) Re-ranker top-50 → top-5; chunks de 400-600 tokens (no 2000) |
| 6. Híbrido cloud-local | f) Tareas masivas y rutinarias en Ollama; cloud solo para crítico |
::/act-match

::act-mcq{titulo="Decisiones de optimización"}
1. Tu Asistente envía el mismo system prompt + RAG de 10k tokens en cada llamada. La técnica con mayor ROI es:
   - [ ] Cambiar a un modelo más barato
   - [x] Prompt caching (lectura desde cache es ~10 % del costo normal)
   - [ ] Batch API
   - [ ] Reducir el número de usuarios

2. Tienes 1000 correos para clasificar antes de mañana en la mañana. Lo correcto es:
   - [ ] Procesarlos uno por uno con Opus
   - [x] Batch API con Haiku/Flash a 50 % de costo, latencia 24h aceptable
   - [ ] Pagar plan Enterprise
   - [ ] Posponerlos al siguiente mes

3. Caso donde Batch API NO se debe usar:
   - [x] Chat en vivo con padres de familia (latencia 24h destruye la UX)
   - [ ] Reportes nocturnos
   - [ ] Procesamiento de logs masivos
   - [ ] Generación de exámenes para el siguiente bimestre
::/act-mcq

::act-fill{titulo="TCO y ROI del Asistente"}
La fórmula del costo total mensual del Asistente:

```
TCO mensual = costos _____________
            + suscripciones _____________ (ChatGPT Team, Claude Pro, etc.)
            + hardware _____________ amortizado
            + electricidad
            + tiempo TI mantenimiento × tarifa
            + plataformas _____________ (n8n cloud, Dify)
            + servicios externos (LangFuse, Vector DBs cloud)
```

Y la fórmula del retorno:

```
ROI = (Tiempo humano _____________  × tarifa)
    + (Casos resueltos sin _____________ × valor de cada uno)
    + (Reducción de _____________ × costo de error)
    − TCO
```

Anti-patrón crítico: optimizar sin medir _____________ — ahorros que pierden 20 % de calidad no son ahorros.
::/act-fill

---

### Bloque C — Política de uso de IA institucional (10.3)

::act-order{titulo="Las 8-9 secciones de la política — ordena"}
[ ] Comité de Gobernanza IA y reuniones trimestrales
[ ] Casos prohibidos con ejemplos concretos
[ ] Alcance (a quién aplica)
[ ] Capacitación obligatoria
[ ] Sanciones por nivel de falta
[ ] Casos permitidos con ejemplos concretos
[ ] Atribución y disclaimer
[ ] Datos sensibles y clasificación
[ ] Contactos para reportar incidentes
::/act-order

::act-tf{titulo="V/F sobre política institucional"}
1. Una política "Usa IA con responsabilidad" sin ejemplos concretos cumple su función. ( ) ____________
2. Si la política es demasiado restrictiva, todos terminan usando IA en secreto. ( ) ____________
3. Sin firma del staff, alguien puede argumentar que no conocía la política. ( ) ____________
4. Recomendable tener UN solo documento que aplique idéntico a staff y a alumnos. ( ) ____________
5. La revisión anual mínima es necesaria porque la IA cambia cada 6 meses. ( ) ____________
::/act-tf

::act-case{titulo="Caso de filtración por falta de política" lineas=10}
Tu institución **no** tiene política de uso de IA y un docente pega calificaciones de 30 alumnos en ChatGPT free pidiéndole "ayuda a redactar un informe". Diseña la **cascada del incidente** en 5 pasos: a) qué pasa con los datos en los servidores de OpenAI, b) cómo se entera la institución del incidente y cuánto tarda, c) qué autoridades hay que notificar (INAI, padres) y en qué plazo, d) qué falta consecuencia laboral correspondería, e) qué sanción legal podría caerle a la institución por LFPDPPP. Cierra proponiendo el caso como ejemplo concreto en la sección "Casos prohibidos" de tu política.
::/act-case

---

### Bloque D — Métricas de retorno (10.4)

::act-match{titulo="KPI → categoría"}
| KPI | Categoría |
|---|---|
| 1. DAU/MAU | a) Calidad |
| 2. Horas humanas ahorradas/mes | b) Adopción |
| 3. Satisfacción del usuario (encuesta 1-5) | c) Impacto |
| 4. NPS staff | d) Ahorro |
| 5. Casos resueltos sin escalación | e) Adopción |
| 6. Precisión factual (auditoría aleatoria) | f) Calidad |
| 7. Reducción tiempo respuesta a padres | g) Impacto |
::/act-match

::act-mcq{titulo="Métricas de vanidad vs. métricas útiles"}
1. La métrica más útil para defender el proyecto ante el patronato es:
   - [ ] Conversaciones totales
   - [ ] Total de logins
   - [x] Casos resueltos sin escalación humana (% auto-resueltos)
   - [ ] Total de tokens consumidos

2. Sin baseline pre-IA:
   - [ ] No importa, basta con la cifra actual
   - [x] No puedes mostrar mejora medible
   - [ ] El patronato lo entiende
   - [ ] Se puede inventar

3. Tu reporte muestra que la satisfacción cae de 4.3 a 3.6. Antes de la junta debes:
   - [ ] Esconder esa métrica
   - [x] Hacer auditoría de causa, hablar con usuarios y presentar plan de remediación
   - [ ] Cambiar el modelo
   - [ ] Pedir extensión del proyecto
::/act-mcq

::act-table{titulo="Tu dashboard mínimo viable — completa con cifras objetivo"}
| Categoría | KPI | Baseline (pre-IA) | Objetivo a 6 meses | Frecuencia |
|---|---|---|---|---|
| Adopción | DAU | | | |
| Adopción | Casos auto-resueltos | | | |
| Ahorro | Horas humanas/mes | | | |
| Ahorro | ROI | | | |
| Calidad | Satisfacción 1-5 | | | |
| Calidad | Precisión factual | | | |
| Impacto | NPS staff | | | |
::/act-table

---

### Bloque E — Confidencialidad y datos sensibles (10.5)

::act-table{titulo="Matriz dato × sistema — completa con ✓ / ✗ / ✓ con condición"}
| Sistema → / Datos ↓ | ChatGPT free | ChatGPT Pro | Claude Pro | Plan Enterprise | Asistente Local | Sin IA |
|---|---|---|---|---|---|---|
| Públicos | | | | | | |
| Internos | | | | | | |
| Confidenciales | | | | | | |
| Restringidos | | | | | | |
::/act-table

::act-match{titulo="Tipo de dato institucional → nivel de clasificación"}
| Dato | Nivel |
|---|---|
| 1. Brochure institucional | a) Restringido |
| 2. Calificaciones individuales | b) Confidencial |
| 3. Plan pedagógico de la materia | c) Público |
| 4. Contrato laboral con cláusula NDA | d) Interno |
| 5. Datos de salud específicos de un alumno | e) Confidencial / restringido |
| 6. Comunicaciones disciplinarias | f) Restringido |
::/act-match

::act-tf{titulo="V/F sobre controles técnicos"}
1. Para datos confidenciales basta con plan Pro/Plus del proveedor. ( ) ____________
2. La regla "two-man rule" (uno autoriza, otro ejecuta) reduce ~95 % los incidentes accidentales en datos restringidos. ( ) ____________
3. "Confío en OpenAI" cuenta como Data Processing Agreement firmado. ( ) ____________
4. Para datos restringidos, el sistema autorizado típico es solo el Asistente Local en infraestructura de la institución. ( ) ____________
5. Tener logs sin auditarlos periódicamente es como tener cámaras sin operador. ( ) ____________
::/act-tf

::act-order{titulo="Runbook de incidente IA — ordena los 8 pasos"}
[ ] Comunicación a afectados (padres si datos de menores se filtraron)
[ ] Detección — quién detecta y cómo se reporta
[ ] Contención — apagar el flujo, rotar credenciales, snapshot logs
[ ] Post-mortem sin culpa personal, foco en sistema
[ ] Notificación a INAI / autoridad si aplica (plazos LFPDPPP)
[ ] Análisis de qué falló específicamente
[ ] Comunicación interna a staff, dirección, patronato
[ ] Remediación técnica + actualizar política
::/act-order

---

## Clave de respuestas

**Bloque A — MCQ:** 1-c · 2-c · 3-b. **Tabla:** A = $1 500/mes / $18 000/año · B = $700/mes / $8 400/año · C = $1 650/mes / $19 800/año · D = $150/mes / $1 800/año + hardware amortizado. **Fill:** staff · privacidad · alto · TI · compliance · 3 (o 4) · 1.

**Bloque B — Match:** 1-c · 2-a · 3-b · 4-d · 5-e · 6-f. **MCQ:** 1-b · 2-b · 3-a. **Fill:** API · planes · local · no-code · ahorrado · escalación · errores · calidad.

**Bloque C — Order:** alcance → casos permitidos → casos prohibidos → datos sensibles y clasificación → atribución y disclaimer → sanciones → capacitación → comité de gobernanza → contactos. **V/F:** 1-F (sin ejemplos concretos no cumple) · 2-V · 3-V · 4-F (recomendable separar staff y alumnos por foco distinto) · 5-V. **Caso:** ejemplo libre, debe incluir: a) datos quedan en logs y pueden alimentar entrenamiento sin opt-out, b) el incidente puede tardar semanas en detectarse, c) notificar a INAI según plazos LFPDPPP y a padres si afectados son menores, d) amonestación o falta grave según el reglamento, e) multa LFPDPPP que puede llegar a millones de pesos.

**Bloque D — Match:** 1-b · 2-d · 3-a · 4-c · 5-e · 6-f · 7-g. **MCQ:** 1-c · 2-b · 3-b. **Tabla:** ejemplo: DAU baseline 0 / objetivo 30-40 staff a mes 6 / mensual · casos auto-resueltos 0 % / 70 % a mes 6 / semanal · horas humanas 0 / 80h/mes a mes 6 / mensual · ROI sin baseline / 13× a mes 6 / trimestral · satisfacción sin baseline / ≥4.0 / por conversación · precisión 0 % / ≥95 % / mensual · NPS sin baseline / ≥30 / semestral.

**Bloque E — Tabla:** Públicos = ✓/✓/✓/✓/✓/(innecesario) · Internos = ✗/✓ con opt-out/✓ con opt-out/✓/✓/✓ · Confidenciales = ✗/✗/✗/✓ con DPA/✓/✓ · Restringidos = ✗/✗/✗/✗/✓ con auditoría/✓. **Match:** 1-c · 2-b · 3-d · 4-a · 5-e · 6-f. **V/F:** 1-F (necesita Plan Enterprise + DPA o Asistente Local) · 2-V · 3-F (DPA implícito no cuenta; debe estar firmado) · 4-V · 5-V. **Order:** detección → contención → notificación a autoridad → comunicación interna → comunicación a afectados → análisis → remediación → post-mortem.
