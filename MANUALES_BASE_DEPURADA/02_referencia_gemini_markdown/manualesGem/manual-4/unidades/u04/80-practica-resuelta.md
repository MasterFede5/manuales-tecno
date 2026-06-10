---
unidad: 4
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 04

::practica{titulo="Construir el 'Consultor del Reglamento' del Asistente Institucional con NotebookLM + Claude Project en 2 horas"}
**Problema.** Necesitas que el Asistente responda consultas del reglamento académico citando página exacta, en español, gratis si es posible, con audio overview opcional para padres que prefieren escuchar. Tiempo objetivo: 2 horas hasta tener un sistema usable.

**Paso 1 — Datos disponibles.**
- 5 PDFs institucionales: reglamento académico 2026 (35 pp), calendario 2026 (4 pp), manual del docente (60 pp), política de admisiones (12 pp), código de ética (8 pp).
- Plan: NotebookLM gratis para citas + audio; Claude Pro para razonamiento profundo en consultas largas.

**Paso 2 — Estrategia.**
1. Limpieza ligera de los PDFs (que no sean escaneos de baja calidad).
2. Subir los 5 PDFs a un Notebook NotebookLM.
3. Configurar guía de uso del Notebook con instrucciones de citado.
4. Crear Claude Project paralelo con los mismos 5 PDFs para casos profesionales.
5. Probar con golden set de 8 preguntas reales (4 con respuesta esperada, 2 que requieren combinar fuentes, 2 que NO están en los documentos).
6. Documentar resultados y publicar al equipo.

**Paso 3 — Limpieza (15 min).**
Verifico que los 5 PDFs sean texto seleccionable (no imagen). El reglamento académico está escaneado con OCR pobre; lo paso por OCRmyPDF (gratis) para mejorar reconocimiento. Los demás están bien. Renombro siguiendo convención: `reglamento_academico_v3.0_2026-08-15.pdf`, etc.

**Paso 4 — NotebookLM (20 min).**
- Creo notebook nuevo.
- Subo los 5 PDFs como sources.
- Espero análisis automático (~3 min).
- Pruebo con pregunta 1: "¿Cuál es el plazo para apelar una calificación?"
  - Respuesta correcta con cita superíndice clickable.
- Configuro instrucciones del notebook: tono, política de no-respuesta cuando falte info, no inventar artículos.

**Paso 5 — Claude Project (20 min).**
- Creo Project "Asistente Institucional · Reglamentos".
- Subo los 5 PDFs al Project knowledge.
- Defino instrucciones del Project con tono, formato de cita esperado, política de no-respuesta.
- Pruebo las 8 preguntas; ajusto instrucciones donde haga falta.

**Paso 6 — Golden set (30 min).**

8 preguntas reales del histórico:

| # | Pregunta | NotebookLM | Claude Project |
|---|---|---|---|
| 1 | Plazo para apelar calificación | ✓ con cita | ✓ con cita |
| 2 | Inasistencias permitidas por bimestre | ✓ con cita | ✓ con cita |
| 3 | Procedimiento para reincorporación tras 3 faltas seguidas (combina 2 docs) | ✓ con 2 citas | ✓ con 2 citas |
| 4 | Becas disponibles para hermanos | parcial — falta info | ✓ con 1 cita |
| 5 | Calendario de exámenes finales | ✓ con cita | ✓ con cita |
| 6 | "¿Quién es el director?" (NO está en docs) | "no tengo info" ✓ | "no tengo info" ✓ |
| 7 | "¿Aceptan estudiantes con dispraxia?" (NO está) | NotebookLM intentó inventar — flag | "no tengo info" ✓ |
| 8 | Tono difícil: "¿es legal que me cobren tanto?" | Maneja bien | Maneja excelente |

**Paso 7 — Análisis y decisiones.**
- Pregunta 4: NotebookLM no encuentra info de hermanos porque está en política de admisiones bajo otro nombre. Decisión: agregar guía al notebook con sinónimos.
- Pregunta 7: NotebookLM falló (alucinó). Decisión: para preguntas sensibles (necesidades educativas especiales), enrutar a Claude Project que es más estricto.
- Costo aproximado: NotebookLM gratis; Claude Pro $20/mes ya pagado.

**Paso 8 — Distribución (15 min).**
- NotebookLM share link a coordinación académica para uso interno.
- Audio Overview generado del reglamento (12 minutos) y publicado en Drive del equipo de docentes nuevos como onboarding.
- Claude Project compartido con staff (Claude Team).
- Documento "Cómo consultar el Asistente" (1 pp) explicando cuándo usar cada uno.

**Paso 9 — Verificación final (20 min).**
Pasada de 5 personas distintas con 3 preguntas cada una (15 nuevas preguntas). 13/15 con respuesta correcta y citada; 2 con "no tengo info" apropiado. Tiempo de respuesta promedio: 4 segundos. Validación social aprobada.

**Respuesta.** Tienes operativo: NotebookLM público para staff y docentes (con audio overview del reglamento), Claude Project para staff con razonamiento profundo y consultas sensibles. Tiempo total: 2 horas. Costo recurrente: solo el plan Claude Pro ya existente.

**Verificación final.** Una semana después, el equipo de admisiones reporta haber resuelto 23 consultas de padres usando NotebookLM. Coordinadora académica reporta usar Claude Project para casos complejos (2-3 al día). Sistema validado.

**Lección.** RAG sin código ya **es** producción para 80 % de las instituciones. Las 6 técnicas de la unidad permiten elegir herramienta correcta, validar con golden, mitigar riesgos (alucinaciones en pregunta 7) y distribuir con criterio. La sofisticación viene cuando NotebookLM/Claude Project no alcanza — y ese día, U4 te equipó para Dify, Flowise, Stack AI.
::/practica

::practica{titulo="Cómo diagnostiqué una alucinación grave del RAG y la mitigué en una tarde"}
**Problema.** Lunes 9:00. La coordinadora académica reenvía un correo: una mamá pregunta sobre reincorporación tras 3 faltas. Le pasaron por chat la respuesta de NotebookLM, que cita: *"según el artículo 23 fracción II del reglamento, la reincorporación es automática"*. Problema: el artículo 23 fracción II **no existe**. La mamá ya hizo capturas. Tienes la tarde para diagnosticar y arreglar.

**Paso 1 — Reproducir el fallo.**
Abro el notebook con el reglamento y lanzo la misma pregunta exacta: *"¿cuál es el procedimiento para reincorporación tras tres faltas seguidas?"*. NotebookLM responde con la misma alucinación. **Reproducido.**

**Paso 2 — Examinar el chunk recuperado.**
NotebookLM muestra la cita superíndice. Click. Me lleva al artículo 18 — sobre **inasistencias permitidas por bimestre**, no sobre reincorporación. El chunk recuperado **no contiene la respuesta**, pero el modelo aún así inventó un artículo.

**Paso 3 — Hipótesis del diagnóstico.**
Tres causas posibles:
- (a) La pregunta está fuera del documento (no hay artículo de "reincorporación tras 3 faltas").
- (b) El chunk relevante existe pero no se recuperó (problema de chunking o embedding).
- (c) El modelo ignoró el "no tengo info" y compuso una respuesta verosímil.

**Paso 4 — Búsqueda manual en el PDF.**
Ctrl+F en el reglamento por "reincorporación". 0 resultados. Por "tres faltas". 0 resultados. Por "faltas consecutivas". 1 resultado en el manual del docente (otro PDF), capítulo de evaluación, no de reincorporación.

**Conclusión:** la respuesta **no está** en los documentos cargados. La pregunta es fuera-de-documento. Hipótesis correcta: **(c) — el modelo ignoró la regla anti-alucinación**.

**Paso 5 — Endurecer las instrucciones del notebook.**
Versión actual: *"si no encuentras la respuesta, di 'no tengo información'"*. Reescribo:

> *Antes de responder cualquier pregunta sobre el reglamento, identifica la frase textual del documento que respalda tu respuesta y cítala literalmente entre comillas. Si no puedes copiar una frase textual del documento, responde EXACTAMENTE: "No encuentro información sobre eso en los documentos cargados. Sugiero consultar a la coordinación académica directamente." No completes la respuesta con inferencias propias. No menciones artículos o fracciones que no aparezcan literalmente en el documento.*

**Paso 6 — Re-test con la pregunta original.**
Lanzo la pregunta de la mamá con las nuevas instrucciones. Respuesta: *"No encuentro información sobre el procedimiento de reincorporación tras tres faltas en los documentos cargados. Sugiero consultar a la coordinación académica directamente."*

**Correcto.**

**Paso 7 — Re-test con 4 variantes (regression suite).**
- *"¿Qué pasa si me ausento 3 veces?"* → "no tengo info" + sugiere coordinación. Correcto.
- *"¿Cuál es la regla de reincorporación?"* → "no tengo info". Correcto.
- *"¿Cuántas faltas puedo tener?"* → cita artículo 18 con frase textual. Correcto.
- *"¿Quién es el director?"* → "no tengo info". Correcto.

**Paso 8 — Plan preventivo.**
Detecto el patrón: la institución **necesita** un protocolo de reincorporación documentado. Es decir, el sistema reveló una **brecha del reglamento**, no solo una alucinación. Levanto issue para legal: redactar protocolo y agregar al reglamento v3.1. Mientras tanto, el "no tengo info + sugiere coordinación" es la respuesta correcta.

**Paso 9 — Comunicación a la mamá y a coordinación.**
Coordinación llama a la mamá, le explica que la respuesta inicial fue incorrecta y le da el procedimiento manual. Dejo `docs/alucinacion-001.md` con: incident report, diagnóstico, mitigación, regression suite, plan preventivo.

**Respuesta.** Alucinación mitigada en 4 horas. El sistema RAG ahora distingue correctamente preguntas dentro y fuera de documento. Como bonus, descubrimos una brecha de la documentación institucional que se va a cerrar en 2 semanas.

**Verificación.** A los 3 días, la coordinadora reporta que ninguna pregunta nueva del reglamento ha disparado alucinación. Las preguntas fuera-de-documento se enrutan correctamente.

**Lección.** Las alucinaciones RAG no son magia: son **señales operativas**. Cada una revela algo (instrucciones débiles, chunking malo, brecha documental, embeddings no entrenados para tu dominio). El proceso es siempre el mismo: reproducir → examinar el chunk → diagnosticar → mitigar → regression suite → plan preventivo. Nunca aceptes "es alucinación, qué se va a hacer" — siempre hay causa y siempre hay mitigación.
::/practica

::practica{titulo="Cómo decidí entre NotebookLM, Custom GPT y Dify para 3 casos del mismo trimestre"}
**Problema.** En el mismo trimestre, la institución necesita 3 sistemas RAG: (A) chatbot público en la web institucional para que padres consulten reglamento, (B) asistente interno para staff que cruza 5 documentos en consultas profundas, (C) endpoint API que n8n consume dentro de un workflow de admisiones. Tienes 3 días para decidir herramientas y empezar.

**Paso 1 — Listar requisitos por caso.**

| Caso | Volumen esperado | Login | Citas | Latencia | API | Costo |
|---|---|---|---|---|---|---|
| A — público web | ~200 consultas/mes | no | sí | aceptable | embed iframe | gratis preferido |
| B — staff interno | ~80 consultas/mes | google workspace | crítico | tolera 30 s | no necesaria | <$30/mes |
| C — n8n endpoint | ~500 consultas/mes | API key | sí | <5 s | obligatoria | <$50/mes |

**Paso 2 — Mapear herramientas a requisitos.**

- **NotebookLM**: gratis, citas excelentes, audio overview, **no API**, login Google. → Caso A queda raro porque NotebookLM no embebe nativamente sin login.
- **Claude Projects**: citas parciales, sin API directa, login Anthropic. → Caso B encaja: staff con plan Claude Team.
- **Custom GPT**: API parcial via Actions, citas mejorables, login ChatGPT. → Caso A encaja si la institución tiene plan ChatGPT Enterprise (no), o se usa via web pública.
- **Dify**: API nativa, self-host, multi-modelo, requiere setup técnico. → Caso C encaja perfecto.

**Paso 3 — Decisión por caso (con tradeoffs documentados).**

**Caso A — público web.** Decisión: **Custom GPT público** publicado por web link, embebible en iframe en la web institucional. Tradeoff: pide cuenta gratis ChatGPT al usuario; mitigación: ofrecemos como alternativa un formulario de contacto si el padre no quiere cuenta. Costo: $0 (los padres usan plan gratis). Citas: pasables.

**Caso B — staff interno.** Decisión: **Claude Project con plan Team** (compartido entre 5 staff). Razonamiento profundo y privacidad enterprise. Costo: $25/usuario/mes × 5 = $125/mes. Justificable porque la institución ya paga ChatGPT Plus que nadie usa: cancelo y migro presupuesto.

**Caso C — n8n endpoint.** Decisión: **Dify self-hosted** en un VPS pequeño ($6/mes Hetzner). Conecto Dify con OpenAI o Cohere multilingual para embeddings. Cohere multilingual gana porque los documentos institucionales tienen frases en náhuatl y español; OpenAI embeddings degradan ahí. API REST nativa. Costo: $6 VPS + tokens consumidos (~$15/mes a 500 consultas).

**Paso 4 — Validación con stakeholders.**
Comparto la matriz con dirección y coordinación. La pregunta más dura: *"¿por qué tres herramientas distintas?"*. Respuesta: *"cada caso tiene un perfil distinto de fricción, latencia y privacidad. Forzar una herramienta única costaría más en compromisos que las 3 separadas. Si en 6 meses una herramienta cubre los 3, migramos."* Aprobado.

**Paso 5 — Setup paralelo (3 días).**
- Día 1: Custom GPT con los 8 PDFs públicos del reglamento + calendario. Smoke test 10 preguntas. Iframe embebido en la web institucional con disclaimer.
- Día 2: Claude Project con los 8 PDFs + 3 docs internos confidenciales. Instrucciones estrictas. Compartido con 5 staff.
- Día 3: Dify self-hosted en VPS. Misma base documental. API endpoint `/v1/chat-messages` con API key. Conecto desde n8n y verifico respuesta con cita.

**Paso 6 — Golden cruzado.**
Las **mismas 12 preguntas** las lanzo en los 3 sistemas. Comparo. Resultados: A acertó 9/12 con citas parciales; B acertó 11/12 con razonamiento profundo en preguntas combinadas; C acertó 10/12 con Cohere multilingual y velocidad <3 s.

**Paso 7 — ADR.**
ADR-012 documentado: *"3 herramientas RAG en paralelo, una por caso de uso, justificadas por perfiles de fricción, latencia y privacidad. Revisión a 6 meses para evaluar consolidación"*.

**Respuesta.** Los 3 sistemas RAG operativos en 3 días. Costo total mensual: ~$150 (vs. los $2 000+/mes de un proveedor único enterprise). Cobertura completa de los 3 casos.

**Verificación.** A 30 días, los 3 sistemas reportan métricas de uso reales. El más usado es B (staff). El más consultado por volumen es C (n8n). El A tuvo menos tráfico del esperado — issue: poca difusión, no problema técnico.

**Lección.** No existe "la mejor herramienta de RAG". Existe la **mejor herramienta para tu caso de uso concreto**. La unidad enseña 6 herramientas porque cada una gana en perfiles distintos. La sabiduría es **mapear caso → perfil → herramienta** con tradeoffs documentados, no buscar la unicornio que cubra todo.
::/practica
