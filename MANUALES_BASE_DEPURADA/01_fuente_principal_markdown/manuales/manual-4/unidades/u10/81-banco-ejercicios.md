---
unidad: 10
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 10

> Banco de práctica para estrategia, costos y gobernanza del Asistente Institucional.
> - **Foco:** Comparativo de planes, optimización, políticas, métricas y datos sensibles.
> - **Prioridad:** Decisión presupuestal, lectura de plan y construcción de matriz.
> - **Regla:** Resuelve antes de mirar la clave.

::interioriza
Imagina que eres el chef ejecutivo armando el menú del año:
Debes balancear ingredientes premium (GPT-4) con básicos (Ollama), cuidar el presupuesto y asegurarte de que nadie sea "alérgico" a tu política de datos.
::/interioriza

::pausa{}
Antes de empezar:
- ¿Qué métrica de tu institución es la más crítica a mejorar con IA?
- ¿Qué dato es el más sensible que manejan hoy?
::/pausa

---

### Bloque A — Comparativo de planes (10.1)

::act-mcq{titulo="Decisión de proveedor"}
1. Tu institución usa Microsoft 365 + Outlook + Teams. La opción default debería ser:
   - [ ] ChatGPT Team
   - [ ] Claude Pro
   - [x] Microsoft 365 Copilot (integración nativa)
   - [ ] Gemini Workspace

2. El patronato exige privacidad máxima y volumen alto, pero hay capacidad TI:
   - [ ] ChatGPT Enterprise
   - [ ] Pagar las 4 plataformas premium
   - [x] Stack soberano híbrido (Claude Pro + Ollama + Open WebUI)
   - [ ] Solo planes free

3. Para contenido especializado de alto nivel (whitepapers), el mejor razonamiento es:
   - [ ] ChatGPT Plus
   - [x] Claude Pro / Team / Enterprise (Opus con MCP nativo)
   - [ ] Copilot M365
   - [ ] Gemini Workspace
::/act-mcq

::act-table{titulo="Costo total anual por opción (50 staff)"}
| Opción | Plan(es) | Costo mensual | Costo anual |
|---|---|---|---|
| A — Stack OpenAI mainstream | 50 × ChatGPT Team $30 | | |
| B — Stack mixto premium | 30 × Gemini Workspace + AI $20 + 5 × Claude Pro $20 | | |
| C — Stack Microsoft completo | 50 × M365 + Copilot $30 + 5 × ChatGPT Team | | |
| D — Stack soberano híbrido | 5 × Claude Pro + Ollama local + Open WebUI | | |
::/act-table

::act-fill{titulo="Los 5 criterios de decisión"}
Criterios clave para elegir proveedor:

1. **¿Dónde vive tu _____________?** (M365 → Copilot; Google → Gemini).
2. **¿_____________ estricta?** (Enterprise + Local con Ollama).
3. **¿Volumen _____________?** (Local soberano gana en volumen alto).
4. **¿Capacidad _____________?** (sin → cloud; con → local soberano).
5. **¿_____________ específica?** (HIPAA → cloud Enterprise certificado).

**Anti-patrones:** 
- Pagar _____________ plataformas para todos.
- Lock-in temprano (negocia _____________ año primero).
- Pagar licencias que nadie usa (sin auditoría).
::/act-fill

---

### Bloque B — Costos y optimización (10.2)

::act-match{titulo="Técnica de optimización → ahorro"}
| Técnica | Efecto |
|---|---|
| 1. Modelo correcto (Haiku para clasificar) | a) ~85 % menos costo en parte cacheable |
| 2. Prompt caching | b) 50 % descuento, latencia 24h |
| 3. Batch API | c) Hasta 18× más barato vs Opus |
| 4. Reducción de tokens | d) Edita prompts y limita `max_tokens` |
| 5. RAG eficiente | e) Re-ranker top-5; chunks 400-600 tokens |
| 6. Híbrido cloud-local | f) Masivas en Ollama; cloud para lo crítico |
::/act-match

::act-mcq{titulo="Decisiones de optimización"}
1. Tu Asistente envía RAG de 10k tokens en cada llamada. Mayor ROI:
   - [ ] Cambiar a modelo más barato
   - [x] Prompt caching (~10 % del costo normal)
   - [ ] Batch API
   - [ ] Reducir usuarios

2. Tienes 1000 correos para clasificar antes de mañana:
   - [ ] Uno por uno con Opus
   - [x] Batch API con Haiku/Flash (50 % costo)
   - [ ] Plan Enterprise
   - [ ] Posponerlos

3. Caso donde Batch API NO sirve:
   - [x] Chat en vivo (latencia destruye UX)
   - [ ] Reportes nocturnos
   - [ ] Procesamiento de logs
   - [ ] Generar exámenes
::/act-mcq

::act-fill{titulo="TCO y ROI del Asistente"}
**Costo Total Mensual (TCO):**
- Costos _____________
- Suscripciones _____________ (Team, Pro)
- Hardware _____________ amortizado
- Electricidad y tiempo TI
- Plataformas _____________ (n8n, Dify)

**Retorno (ROI):**
- (Tiempo humano _____________ × tarifa)
- (Casos sin _____________ × valor)
- (Reducción de _____________ × costo de error)
- MENOS: TCO

**Ojo:** Optimizar sin medir _____________ es peligroso (ahorros sin calidad).
::/act-fill

---

### Bloque C — Política de uso institucional (10.3)

::act-order{titulo="Las 9 secciones de la política"}
[ ] Comité de Gobernanza IA y reuniones
[ ] Casos prohibidos (con ejemplos)
[ ] Alcance (a quién aplica)
[ ] Capacitación obligatoria
[ ] Sanciones por nivel de falta
[ ] Casos permitidos (con ejemplos)
[ ] Atribución y disclaimer
[ ] Datos sensibles y clasificación
[ ] Contactos para incidentes
::/act-order

::act-tf{titulo="V/F sobre política"}
1. Una política genérica sin ejemplos cumple su función. ( ) ____________
2. Políticas muy restrictivas generan uso secreto de IA. ( ) ____________
3. Sin firma del staff, pueden alegar desconocimiento. ( ) ____________
4. Un solo documento idéntico para staff y alumnos es ideal. ( ) ____________
5. Revisión anual mínima es vital porque la IA cambia rápido. ( ) ____________
::/act-tf

::act-case{titulo="Filtración por falta de política" lineas=10}
**Contexto:** Institución sin política.
**Incidente:** Docente pega calificaciones de 30 alumnos en ChatGPT free.
**Tu tarea:** 
Diseña la cascada del incidente en 5 pasos (datos en OpenAI, tiempo de detección, notificación al INAI/padres, falta laboral, multa LFPDPPP). 
Cierra proponiendo esto como caso en "Casos prohibidos".
::/act-case

---

### Bloque D — Métricas de retorno (10.4)

::act-match{titulo="KPI → Categoría"}
| KPI | Categoría |
|---|---|
| 1. DAU/MAU | a) Calidad |
| 2. Horas humanas ahorradas/mes | b) Adopción |
| 3. Satisfacción del usuario (1-5) | c) Impacto |
| 4. NPS staff | d) Ahorro |
| 5. Casos resueltos sin escalación | e) Adopción |
| 6. Precisión factual (auditoría) | f) Calidad |
| 7. Reducción tiempo de respuesta | g) Impacto |
::/act-match

::act-mcq{titulo="Métricas útiles vs vanidad"}
1. Métrica más útil para defender el proyecto ante el patronato:
   - [ ] Conversaciones totales
   - [ ] Total de logins
   - [x] Casos resueltos sin escalación (% auto-resueltos)
   - [ ] Tokens consumidos

2. Si no tienes baseline pre-IA:
   - [ ] No importa
   - [x] No puedes mostrar mejora medible
   - [ ] El patronato lo asume
   - [ ] Invéntalo

3. La satisfacción cae de 4.3 a 3.6. Antes de la junta:
   - [ ] Esconder la métrica
   - [x] Hacer auditoría, hablar con usuarios y presentar plan
   - [ ] Cambiar el modelo
   - [ ] Pedir extensión
::/act-mcq

::act-table{titulo="Dashboard mínimo viable"}
| Categoría | KPI | Baseline | Objetivo a 6 meses | Frecuencia |
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

::act-table{titulo="Matriz dato × sistema (✓ / ✗ / ✓ con condición)"}
| Sistema → / Datos ↓ | ChatGPT free | Pro | Claude Pro | Enterprise | Asistente Local | Sin IA |
|---|---|---|---|---|---|---|
| Públicos | | | | | | |
| Internos | | | | | | |
| Confidenciales | | | | | | |
| Restringidos | | | | | | |
::/act-table

::act-match{titulo="Dato → Nivel de clasificación"}
| Dato | Nivel |
|---|---|
| 1. Brochure institucional | a) Restringido |
| 2. Calificaciones individuales | b) Confidencial |
| 3. Plan pedagógico | c) Público |
| 4. Contrato laboral con NDA | d) Interno |
| 5. Datos de salud de alumno | e) Confidencial / restringido |
| 6. Comunicaciones disciplinarias | f) Restringido |
::/act-match

::act-tf{titulo="V/F sobre controles técnicos"}
1. Para datos confidenciales basta con plan Pro. ( ) ____________
2. Regla "two-man rule" reduce incidentes un 95 %. ( ) ____________
3. "Confío en OpenAI" equivale a un DPA firmado. ( ) ____________
4. Datos restringidos = Asistente Local en infra propia. ( ) ____________
5. Logs sin auditoría son como cámaras sin operador. ( ) ____________
::/act-tf

::act-order{titulo="Runbook de incidente IA"}
[ ] Comunicación a afectados
[ ] Detección (quién y cómo)
[ ] Contención (apagar flujo, snapshot)
[ ] Post-mortem sin culpa
[ ] Notificación a autoridad (INAI)
[ ] Análisis de falla
[ ] Comunicación interna
[ ] Remediación y actualización de política
::/act-order

---

## Clave de respuestas

**Bloque A — MCQ:** 1-c · 2-c · 3-b. 
**Tabla:** A = $1 500/mes / $18 000/año · B = $700/mes / $8 400/año · C = $1 650/mes / $19 800/año · D = $150/mes / $1 800/año + hardware. 
**Fill:** staff · privacidad · alto · TI · compliance · 3 (o 4) · 1.

**Bloque B — Match:** 1-c · 2-a · 3-b · 4-d · 5-e · 6-f. 
**MCQ:** 1-b · 2-b · 3-a. 
**Fill:** API · planes · local · no-code · ahorrado · escalación · errores · calidad.

**Bloque C — Order:** alcance → permitidos → prohibidos → datos y clasificación → atribución → sanciones → capacitación → comité → contactos. 
**V/F:** 1-F · 2-V · 3-V · 4-F · 5-V. 
**Caso:** Incluir logs en OpenAI, tiempo de detección, INAI/padres, falta grave, multa.

**Bloque D — Match:** 1-b · 2-d · 3-a · 4-c · 5-e · 6-f · 7-g. 
**MCQ:** 1-c · 2-b · 3-b. 
**Tabla:** Ejemplo: DAU 30-40 (mes 6) · auto-resueltos 70 % · horas 80h/mes · ROI 13× · satisfacción ≥4.0 · precisión ≥95 % · NPS ≥30.

**Bloque E — Tabla:** Públicos = todos ✓ salvo innecesarios · Internos = ✓ con opt-out/✓ · Confidenciales = Enterprise/Local ✓ · Restringidos = Solo Local. 
**Match:** 1-c · 2-b · 3-d · 4-a · 5-e · 6-f. 
**V/F:** 1-F · 2-V · 3-F · 4-V · 5-V. 
**Order:** detección → contención → notificación autoridad → comunicación interna → afectados → análisis → remediación → post-mortem.
