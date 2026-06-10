---
unidad: 4
seccion: implementacion
paginas_objetivo: 4
---

::implementacion{titulo="Implementación Albatros — RAG institucional con NotebookLM, Claude Project y opcional Dify"}
**Objetivo.** Construir el **sistema RAG completo del Asistente Institucional Albatros**, indexar la base documental institucional (mínimo 8 documentos), validar con golden set RAGAS de 15 preguntas, exponer 2-3 interfaces (NotebookLM público, Claude Project staff, opcional Dify para producción) y documentar el proceso para futuro mantenimiento.

**¿Por qué hacerla?** Esta unidad es donde el Asistente deja de ser un chatbot genérico y se convierte en **el cerebro institucional**. Sin esto, las siguientes unidades (n8n, agentes, MCP) operan sin contexto del lugar.

---

### Materiales y recursos

- 8+ documentos institucionales en PDF.
- Cuenta gratis NotebookLM, Claude Pro (recomendado), opcional Dify self-hosted o cloud.
- 8–12 horas distribuidas en 4 sesiones.
- 2 stakeholders distintos para validación.

### Pasos

#### Sesión 1 — Curaduría y limpieza documental (2 h)

1. **30 min — Inventario.** Lista los 8+ documentos: nombre, versión, fecha, dueño.
2. **30 min — Validación de calidad.** Cada PDF: ¿texto seleccionable? ¿OCR limpio? ¿metadatos visibles?
3. **30 min — OCR si hace falta.** OCRmyPDF gratis para los escaneados.
4. **30 min — Convención de nombres.** Renombras siguiendo `<tipo>_<nombre>_v<X.Y>_<fecha>.pdf`. Lo guardas en Drive con permisos correctos.

#### Sesión 2 — NotebookLM público (1.5 h)

5. **15 min — Notebook setup.** Subes los 8 PDFs.
6. **30 min — Configuración.** Instrucciones del notebook: rol, tono, política de no-respuesta.
7. **15 min — Audio Overview.** Generas el audio del reglamento.
8. **30 min — Pruebas internas.** 5 preguntas reales.

#### Sesión 3 — Claude Project profesional (2 h)

9. **30 min — Project setup.** Mismos 8 PDFs en Project knowledge.
10. **30 min — Instrucciones del Project.** Más estrictas: cita obligatoria, no responder fuera del corpus.
11. **30 min — Pruebas.** Mismas 5 preguntas de NotebookLM + 3 que requieren combinar 3 documentos.
12. **30 min — Comparación.** Matriz NotebookLM vs Claude Project con observaciones.

#### Sesión 4 — Golden set RAGAS y opcional Dify (2-3 h)

13. **45 min — Golden set RAGAS.** 15 preguntas: 8 con respuesta esperada, 4 que combinan fuentes, 3 que NO están.
14. **45 min — Evaluación.** Lanzas 15 preguntas en NotebookLM y Claude Project; calificas manualmente las 4 métricas RAGAS (faithfulness, context recall, context precision, answer relevancy).
15. **30 min — Análisis y plan.** Identificas la métrica más débil; defines plan de mejora.
16. **Opcional 1 h — Dify.** Si necesitas API propia o re-ranking, replicas en Dify self-hosted con Cohere multilingual.

::visual{tipo="ilustracion" descripcion="Mockup del ecosistema RAG institucional desplegado: en el centro, un cilindro 'Base documental v3.0' con 8 PDFs apilados. Tres flechas salen hacia: 1) NotebookLM (con icono Google + audio overview), público para staff. 2) Claude Project (icono Anthropic), staff profesional. 3) Dify (icono opcional), API y producción. Bajo cada destino, captura miniatura de la UI y métricas de uso. Al pie del diagrama, golden set de 15 preguntas con resultados RAGAS visualizados como barras. Estilo blueprint Albatros." paginas=1}

---

### Entregable

1. **Drive institucional** con base documental v1.0 organizada.
2. **NotebookLM** compartido + Audio Overview en MP3.
3. **Claude Project** compartido con staff con instrucciones documentadas.
4. **Documento RAGAS** con golden de 15 preguntas y scores.
5. **Plan de mejora** prioritizado para v1.1 (1 página).
6. **Manual de uso** para el equipo (1 página): cuándo usar cada interfaz.
7. **Opcional:** Dify pipeline funcionando.

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Documentos en base | <5 | 8 limpios | 8+ con metadata y versión |
| Convención de nombres | inconsistente | aplicada | con CHANGELOG por documento |
| NotebookLM | sin configurar | funcional | con audio overview adoptado |
| Claude Project | sin configurar | funcional | con instrucciones estrictas validadas |
| Golden set | <5 preguntas | 10 con bordes | 15+ con casos NO-respuesta |
| Evaluación RAGAS | informal | manual con 4 métricas | con análisis cruzado |
| Distribución | privado | a equipo | adoptado en operación con métricas |
| Manual de uso | ausente | una página | con árbol de decisión |

### Hitos intermedios

| Día | Hito | Evidencia |
|---|---|---|
| Día 1 | Inventario y validación de 8 PDFs | listado en `docs/` con metadata |
| Día 2 | Convención de nombres aplicada | Drive ordenado |
| Día 3 | NotebookLM operativo | URL + audio overview |
| Día 5 | Claude Project operativo | URL + instrucciones |
| Día 7 | Golden RAGAS de 15 preguntas | hoja de cálculo |
| Día 8 | Evaluación cruzada NotebookLM vs Claude | matriz de comparación |
| Día 10 | Plan de mejora v1.1 redactado | 1 página |
| Día 12 | Manual de uso para el equipo | árbol de decisión |
| Día 14 | (Opcional) Dify self-host configurado | endpoint API funcionando |

### Reto bonus extendido (3 retos)

**Bonus 1 — RAG con re-ranking.** Si NotebookLM no acierta una pregunta clave, monta el mismo corpus en Dify con re-ranking activado (Cohere o BGE). Mide la diferencia de calidad sobre las 15 preguntas del golden. Documenta cuándo vale la pena pagar la complejidad de re-ranking.

**Bonus 2 — Detector de drift documental.** Cada vez que actualizas el reglamento, lanza el golden completo automáticamente y compara contra la corrida anterior. Si más de 2 preguntas cambian de respuesta, levantas alerta para revisión humana. Documenta el flujo en `docs/drift-detection.md`.

**Bonus 3 — RAG bilingüe.** Algunos documentos de tu institución pueden incluir frases en lengua originaria, regional o técnica. Replica el RAG con embeddings Cohere multilingual y compara recall sobre 5 preguntas en lengua mixta vs OpenAI embeddings. Documenta la decisión en ADR.

### Próximo paso después de esta unidad

En **U5 — Workflows e integraciones** vas a conectar tu Asistente RAG a **n8n** para que automatice solicitudes (cuando un padre pregunta por inscripción, el sistema crea ticket en Notion, manda correo, agrega al CRM). El RAG de esta unidad alimenta a esos flujos con contexto institucional.
::/implementacion

::albatros{titulo="Caso complementario — comparas 2 RAGs sobre el mismo corpus" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** ¿Tu elección de NotebookLM vs Claude Projects sería la misma si midieras con datos en lugar de intuición?

**Lo que harás.**
1. Toma el mismo corpus de 5+ PDFs en NotebookLM y Claude Project.
2. Construye golden mini de 8 preguntas (5 normales, 1 combinada, 1 fuera-de-doc, 1 sensible).
3. Lanza las 8 preguntas en ambos sistemas.
4. Califica cada respuesta en 4 dimensiones: precisión, calidad de cita, manejo de "no sé", tono.
5. Suma puntos y declara ganador por caso de uso.
6. Escribe ADR de 1 página con la elección.

**Entregable.** Tabla 8×2×4 + ADR de 1 página con decisión y disparador de revisión.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Golden | <5 preguntas | 8 con bordes | 8 con sensible y combinada |
| Calificación | una dimensión | 3 dimensiones | 4 con criterio explícito |
| ADR | preferencia | con datos | con datos + disparador de revisión |
::/albatros
