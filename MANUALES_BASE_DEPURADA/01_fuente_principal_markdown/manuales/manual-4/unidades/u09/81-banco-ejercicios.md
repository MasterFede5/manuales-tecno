---
unidad: 9
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 09

> Banco de práctica para producción de contenido especializado de alto nivel:
> - Investigación profunda con citas y whitepapers.
> - Materiales pedagógicos certificables y prototipos UX.
> - Contenido legal con disclaimer y datasets sintéticos.
> 
> Privilegia ejercicios de **decisión de herramienta**, **diseño de prompt** y **definición del filtro humano**.
> Resuelve antes de mirar la clave.

---

### Bloque A — Investigación profunda (9.1)

::act-mcq{titulo="Decisión de herramienta Deep Research"}
1. Para un reporte académico en español mexicano sobre tendencias pedagógicas, la herramienta más adecuada en 2025 es:
   - [ ] ChatGPT Deep Research
   - [x] Gemini Deep Research (mejor en multilingüe y español académico)
   - [ ] Perplexity Pro
   - [ ] Manus

2. Si necesitas factualidad rápida y citas siempre visibles para una nota corta, eliges:
   - [ ] ChatGPT Deep Research
   - [ ] Gemini Deep Research
   - [x] Perplexity Pro
   - [ ] Manus

3. Caso donde Deep Research **falla** y debes usar otra cosa:
   - [ ] Estado del arte de un tema técnico
   - [ ] Análisis competitivo de otras instituciones
   - [x] Investigación sobre tus propios documentos institucionales (usa RAG, U4)
   - [ ] Whitepaper interno con citas verificables
::/act-mcq

::act-fill{titulo="Proceso correcto de Deep Research"}
El proceso correcto en 5 pasos:

1. **Pregunta de investigación bien formulada** — no vaga, sino con _____________ específicas (geografía, periodo, comparación).
2. **Especificar restricciones de _____________** — preferir papers académicos, reportes oficiales (SEP/OCDE), evitar opinion sites genéricos.
3. **Esperar y revisar el output** — no es respuesta, es _____________.
4. **Verificar citas** — abrir cada cita importante; aproximadamente _____________ % suele ser inexacta.
5. **Iterar con preguntas de _____________** — "profundiza el punto 3 con 3 ejemplos específicos".

Antes de usarse externamente, todo Deep Research pasa por verificación humana:
- Revisar 5-10 citas al azar.
- Lectura por experto del dominio (~30 min).
- Comparar con conocimiento institucional y anotar _____________ para follow-up.
::/act-fill

::act-case{titulo="Pregunta perfecta para tu Deep Research" lineas=8}
Diseña la **pregunta de Deep Research perfecta** para arrancar un curso digital de orientación vocacional para bachillerato mexicano. Debe incluir:
- a) Ámbito geográfico delimitado (mexicano público/privado).
- b) Periodo temporal (ej: 2020-2025).
- c) Tipo de fuentes preferidas (papers, SEP/OCDE, reportes UNESCO).
- d) Comparación que exija al modelo (público vs privado, urbano vs rural).
- e) Entregable solicitado (reporte estructurado con N páginas, X citas mínimo).
::/act-case

---

### Bloque B — Whitepapers (9.2)

::act-mcq{titulo="Pipeline canónico de un whitepaper"}
1. La fase **más importante** en producción de whitepaper con IA es:
   - [ ] La maquetación final
   - [x] El outline (si la base falla, todo falla)
   - [ ] La portada
   - [ ] La elección del modelo

2. Para que el whitepaper "no suene a IA", lo más efectivo es:
   - [ ] Pedir al modelo "que sea creativo"
   - [x] Pegar 2-3 párrafos de whitepapers anteriores como ejemplos few-shot + edición humana de longitud variable + ejemplos institucionales concretos
   - [ ] Usar el modelo más nuevo
   - [ ] Hacerlo todo de una sola vez con un prompt enorme

3. La verificación obligatoria de citas debe alcanzar al menos:
   - [ ] 5 % de las citas
   - [ ] 10 % de las citas
   - [x] 100 % de citas críticas (que sostienen tesis) + 30 % muestra random del resto
   - [ ] Solo las que se ven sospechosas
::/act-mcq

::act-order{titulo="Las 12 etapas del pipeline canónico — ordena"}
[ ] Maquetación final (humano o diseñador)
[ ] Tema y outline inicial
[ ] Validación legal/compliance (humano)
[ ] Deep Research previo
[ ] Outline final detallado
[ ] Edición de tono y consistencia con prompt institucional
[ ] Datos y estadísticas con tu BD
[ ] Redacción sección por sección con tu voz
[ ] Citas y referencias verificadas
[ ] Revisión técnica por experto humano
[ ] Gráficas (Python, matplotlib, Excel)
[ ] Publicación
::/act-order

::act-tf{titulo="V/F sobre whitepapers"}
1. La IA hace 7-8 etapas y el humano dirige y valida 4-5. ( ) ____________
2. El error más común en whitepapers IA es citas inventadas o atribuidas mal. ( ) ____________
3. Si una cita no se verifica, lo correcto es dejarla y marcarla como "no verificada". ( ) ____________
4. Pegar 2-3 párrafos de whitepapers institucionales previos como ejemplos few-shot mejora la voz. ( ) ____________
5. Producir un whitepaper de 18 pp con 32 citas verificadas y 6 gráficas debería tomar 2-3 meses con IA bien orquestada. ( ) ____________
::/act-tf

---

### Bloque C — Materiales educativos (9.3)

::act-match{titulo="Producto educativo → característica clave"}
| Producto | Característica clave |
|---|---|
| 1. Rúbrica | a) Guion casi minuto a minuto, útil para docentes nuevos o sustitutos |
| 2. Secuencia didáctica | b) 4 niveles por criterio (Inicial / En desarrollo / Suficiente / Excelente) con descriptores observables |
| 3. Examen | c) Distribución por sesión: apertura (10 min) + desarrollo (25 min) + cierre (10 min) |
| 4. Plan de clase | d) Distractores plausibles con error específico identificado |
| 5. Taller práctico | e) Pasos del facilitador y del alumno + productos esperados + adaptaciones |
::/act-match

::act-fill{titulo="Distribución Bloom de un examen profesional"}
La distribución recomendada por nivel cognitivo de Bloom:

- _____________ % Recordar / Comprender
- _____________ % Aplicar
- _____________ % Analizar
- _____________ % Evaluar / Crear

Por tipo de reactivo:
- _____________ % opción múltiple (4 opciones, distractores plausibles).
- _____________ % verdadero/falso justificado.
- _____________ % completar.
- _____________ % problema abierto.

Lo que separa un examen IA mediocre de uno profesional es exigir explícitamente _____________ con error específico identificado, para que reflejen confusiones reales del estudiante.
::/act-fill

::act-tf{titulo="V/F sobre las reglas pedagógicas no negociables"}
1. Cada material educativo debe indicar explícitamente qué nivel cognitivo de Bloom desarrolla. ( ) ____________
2. Una rúbrica de "ensayo argumentativo" indistinguible de la de cualquier otra escuela aporta marca pedagógica. ( ) ____________
3. Cada material debe considerar al menos 1 adaptación para necesidades especiales (TDAH, dislexia, talento). ( ) ____________
4. Las secuencias didácticas pueden saltar el cierre sin afectar el aprendizaje. ( ) ____________
5. Mínimo un docente del área debe validar antes de aplicar el material. ( ) ____________
::/act-tf

---

### Bloque D — Diseño UX con IA (9.4)

::act-match{titulo="Herramienta UX → mejor caso del Asistente Institucional"}
| Herramienta | Mejor caso |
|---|---|
| 1. Galileo AI | a) Wireframes editables tipo Figma a partir de esbozos a mano |
| 2. Uizard | b) App full-stack funcional desplegada (frontend + backend + BD) |
| 3. v0.dev | c) Mockups visuales pulidos para presentar a fundadores |
| 4. Lovable | d) Componentes React + Tailwind reales y editables, integrables a Next.js |
| 5. Bolt.new | e) Demo rápida en navegador sin setup local (hackathon) |
::/act-match

::act-mcq{titulo="Decisión por contexto del Asistente"}
1. Tu institución quiere portal de orientación vocacional con quiz interactivo y backend ligero:
   - [ ] Galileo AI
   - [ ] Uizard
   - [ ] Solo v0.dev
   - [x] Lovable o Bolt.new (necesitas frontend + backend + BD funcional)

2. Mockup visual pulido para presentar a fundadores antes de decidir desarrollo:
   - [x] Galileo AI
   - [ ] Lovable
   - [ ] Bolt.new
   - [ ] v0.dev

3. Pieza humana imprescindible en cualquier pipeline UX con IA:
   - [ ] Saber Figma
   - [x] Validación con usuarios reales (5 sesiones de 30 min descubren 80 % de problemas)
   - [ ] Saber programar React
   - [ ] Comprar plan Pro de la herramienta
::/act-mcq

::act-tf{titulo="V/F sobre UX con IA"}
1. Pasar mockup IA como diseño final es práctica aceptada para ahorrar tiempo. ( ) ____________
2. Las herramientas IA priorizan accesibilidad WCAG por default. ( ) ____________
3. 5 sesiones de 30 min con usuarios reales descubren ~80 % de problemas de usabilidad. ( ) ____________
4. Generar 50 variantes y no elegir produce análisis-parálisis; mejor 3-5 con decisión. ( ) ____________
5. El código generado por v0.dev o Lovable se puede llevar a producción sin code review humano ni tests. ( ) ____________
::/act-tf

---

### Bloque E — Contenido legal y compliance (9.5)

::act-table{titulo="Riesgo y validación por tipo de contenido legal"}
| Tipo de contenido | Riesgo (alto/medio/bajo) | IA puede borrador (% aprox) | Validación humana requerida |
|---|---|---|---|
| Política de privacidad / Aviso LFPDPPP | | | |
| Términos y condiciones | | | |
| Contratos | | | |
| Reglamentos internos | | | |
| Disclaimers | | | |
| FAQs sobre temas legales | | | |
::/act-table

::act-mcq{titulo="Las 3 reglas no negociables"}
1. La regla principal en contenido legal con IA es:
   - [ ] Borrador con IA, publicación inmediata
   - [x] Borrador con IA + validación con abogado + disclaimer visible + versionado
   - [ ] Solo IA si la institución es pequeña
   - [ ] Solo abogado, IA está prohibida

2. Por qué los modelos fallan particularmente en LFPDPPP, NOMs y jurisprudencia mexicana:
   - [ ] No saben leer español
   - [x] Están entrenados con corpus principalmente estadounidense
   - [ ] El modelo está sesgado políticamente
   - [ ] Es ilegal entrenar con leyes

3. Caso donde NO usar IA:
   - [ ] Reglamentos internos
   - [ ] FAQs sobre temas legales
   - [x] Demandas y litigios activos (confidencialidad y estrategia humana)
   - [ ] Disclaimers cortos
::/act-mcq

::act-case{titulo="Tu plantilla de disclaimer institucional" lineas=8}
Redacta la **plantilla de disclaimer obligatorio** que tu institución pondrá al final de cada documento legal asistido por IA. Debe declarar:
- a) Que el documento fue generado/asistido con IA.
- b) Nombre y cédula del abogado revisor.
- c) Versión y fecha de elaboración.
- d) Fecha de próxima revisión obligatoria.
- e) Leyenda de "para asesoría legal específica, consulte con su abogado".

Cierra con 3 preguntas adversariales que harías al modelo antes de publicar el aviso de privacidad institucional.
::/act-case

---

### Bloque F — Datasets sintéticos (9.6)

::act-mcq{titulo="Casos de uso de datasets sintéticos"}
1. El caso más típico para evaluar prompts del Asistente es:
   - [ ] Datos de prueba para BD
   - [x] Golden set (30-50 ejemplos con clase verdadera para evaluar el prompt)
   - [ ] Simulación de carga
   - [ ] Balanceo de clases

2. Tienes 100 ejemplos reales: 80 de A, 5 de B, 15 de C. Para que el modelo no se concentre en A:
   - [ ] Borrar ejemplos de A
   - [ ] Recolectar más datos reales (toma meses)
   - [x] Generar 75 ejemplos sintéticos para B con ejemplos reales como semilla
   - [ ] Cambiar de modelo

3. Caso donde NO usar sintéticos:
   - [ ] Golden set
   - [ ] Datos de prueba
   - [ ] Simulación edge
   - [x] Cumplimiento regulatorio que exige datos reales documentados
::/act-mcq

::act-fill{titulo="Las 5 reglas de oro"}
Las 5 reglas para producir datasets sintéticos útiles:

1. **_____________ explícito.** Define columnas, tipos, dominios y distribuciones esperadas.
2. **Ejemplos reales como _____________.** 5-15 ejemplos reales que el modelo imite.
3. **Validación _____________.** Verifica que la distribución del sintético se parezca a la real (medias, varianzas, proporciones).
4. **Etiquetado de origen.** Cada fila debe tener `_____________: true` para no confundir con real.
5. **Auditoría de _____________.** El modelo replica los suyos; revisa demografía, temas y lenguaje.

Anti-patrón principal: prompt vago como "genera datos de alumnos" → resultado: lorem ipsum tabulado.
Otro anti-patrón crítico: mezclar real con sintético sin _____________; imposible auditar después.
Y el más peligroso: usar sintético como _____________ para datos sujetos a LFPDPPP — son cosas distintas.
::/act-fill

::act-case{titulo="Prompt para 100 reactivos sintéticos de física" lineas=8}
Redacta el **prompt completo** para generar 100 reactivos sintéticos de exámenes de física para tu institución. Debe especificar:
- a) **Schema** del JSONL (campos: enunciado, opciones, correcta, distractores con error específico, nivel Bloom, tiempo estimado).
- b) **Distribución por tema** (cinemática, dinámica, energía, etc., con porcentajes).
- c) **Distribución por Bloom** (40/30/20/10).
- d) **15 ejemplos reales como semilla** (los pegas).
- e) **Etiqueta `is_synthetic: true`** en cada fila.
- f) **Rango de complejidad** y **estilos de redacción** variados.
::/act-case

---

## Clave de respuestas

**Bloque A — MCQ:** 1-b · 2-c · 3-c.
**Fill:** dimensiones (geografía, periodo, comparación) · fuentes · borrador · 5-10 % · profundización · dudas.
**Caso (ejemplo):** "¿Qué metodologías de orientación vocacional para bachilleratos mexicanos privados son más efectivas según evidencia 2020-2025? Compara con bachilleratos públicos. Prefiere papers académicos, reportes SEP/OCDE/UNESCO, y blogs especializados de Latinoamérica. Devuelve reporte estructurado de 8-15 páginas con mínimo 30 citas verificables."

**Bloque B — MCQ:** 1-b · 2-b · 3-c.
**Order:** tema + outline inicial → Deep Research previo → outline final detallado → redacción sección por sección → datos y estadísticas → gráficas → citas y referencias → edición de tono → revisión técnica experto → maquetación → validación legal → publicación.
**V/F:** 1-V · 2-V · 3-F (debe eliminarse o reemplazarse) · 4-V · 5-F (con IA bien orquestada toma 2-3 semanas).

**Bloque C — Match:** 1-b · 2-c · 3-d · 4-a · 5-e.
**Fill:** 40 · 30 · 20 · 10 · 60 · 20 · 10 · 10 · distractores.
**V/F:** 1-V · 2-F (no aporta marca pedagógica; necesita contexto local) · 3-V · 4-F (sin metacognición el aprendizaje queda incompleto) · 5-V.

**Bloque D — Match:** 1-c · 2-a · 3-d · 4-b · 5-e.
**MCQ:** 1-d · 2-a · 3-b.
**V/F:** 1-F (es prototipo, no producto; necesita iteración con UX/UI profesional) · 2-F (no priorizan WCAG por default; hay que auditar) · 3-V · 4-V · 5-F (para producción siempre code review humano y tests).

**Bloque E — Tabla:** Política de privacidad/aviso LFPDPPP = alto / 80 % / abogado obligatorio · Términos y condiciones = alto / 80 % / abogado obligatorio · Contratos = muy alto / 60 % / abogado obligatorio + revisión cliente · Reglamentos internos = medio / 70 % / coordinador + asesor legal · Disclaimers = bajo / 90 % / coordinador · FAQs sobre temas legales = medio / 80 % / abogado.
**MCQ:** 1-b · 2-b · 3-c.
**Caso:** ejemplo libre con disclaimer estándar de 5 elementos + 3 preguntas adversariales (ej: "critica este aviso como abogado adversarial: ¿qué fallas legales encuentras?", "si fueras INAI auditando, ¿qué cuestionarías?", "¿hay términos ambiguos que un demandante podría usar contra nosotros?").

**Bloque F — MCQ:** 1-b · 2-c · 3-d.
**Fill:** Schema · semilla · estadística · `is_synthetic` · sesgos · etiquetar · anonimización.
**Caso:** ejemplo libre, debe traer schema JSONL completo, distribución por tema y Bloom, 15 ejemplos reales pegados como semilla, flag `is_synthetic: true` en cada fila y variedad de estilo.
