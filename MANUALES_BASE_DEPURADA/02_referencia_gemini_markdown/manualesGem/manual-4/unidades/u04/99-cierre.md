---
unidad: 4
seccion: cierre
paginas_objetivo: 2
---

## Cierre y autoevaluación — Unidad 04

Cerraste la unidad de Bases de Conocimiento y RAG. Ahora puedes:

1. **Explicar** qué es RAG, por qué reduce alucinaciones y cómo funciona el pipeline indexación → consulta → generación con citas.
2. **Comprender** embeddings y vectores como huellas semánticas y elegir el modelo de embeddings correcto para español.
3. **Operar** las 3 plataformas RAG sin código (Custom GPT, Claude Projects, NotebookLM) y elegir según caso.
4. **Construir** pipelines en Dify, Flowise o Stack AI cuando necesites control fino o producción a escala.
5. **Aplicar** chunking estructurado, metadatos completos y citas verificables.
6. **Decidir** entre RAG, fine-tuning o ambos según el problema concreto.

> **Frase puente.** Tu Asistente lee documentos. La siguiente capa: que **actúe sobre el mundo**. Cuando un padre escribe pidiendo inscripción, no basta con responder texto: hay que crear ticket en Notion, mandar correo de confirmación, agendar reunión en Calendar. La Unidad 5 te enseña a orquestar esos flujos con n8n, Make, Zapier y Power Automate, conectados al RAG de esta unidad.

---

### Autoevaluación (rúbrica de 5 niveles)

| Saber | 1 — Inicial | 2 | 3 — Suficiente | 4 | 5 — Excelente |
|---|---|---|---|---|---|
| **Concepto RAG** | desconozco | conozco la idea | explico el pipeline | distingo casos donde NO usar | enseño a otros |
| **Embeddings** | "no entiendo" | concepto general | elijo modelo apropiado | comparo modelos por idioma | optimizo costo y calidad |
| **Plataformas no-código** | uso solo una | conozco las 3 | elijo según caso | uso multi-plataforma | matriz de decisión documentada |
| **Plataformas no-code técnicas** | desconozco | nombre solo | construí pipeline en una | con monitoring | self-hosted en producción |
| **Chunking y metadatos** | default | tamaño fijo | por estructura + overlap | con versionado | con re-ranking |
| **RAG vs fine-tuning** | "no sé diferencia" | sé diferencia | elijo según problema | combino cuando aplica | calculo ROI por caso |
| **Evaluación RAGAS** | no la hice | golden set básico | golden set + RAGAS manual | dashboard de métricas | re-evaluación periódica |

### Pregunta de cierre

> Tu RAG institucional está corriendo. Mes 3 de operación, recibes una queja específica: un padre dice que el Asistente le citó "Artículo 14" del reglamento, pero ese artículo en realidad dice algo distinto. Cuando vas a ver el log, descubres que el chunk recuperado **mezcló dos artículos** porque el chunking partió a la mitad. **Diseña** tu plan de respuesta en 5 pasos numerados, cubriendo: respuesta al padre, fix técnico inmediato, mitigación a corto plazo, mejora estructural, comunicación al equipo.

### Conexión con la siguiente unidad

En **U5 — Workflows e Integraciones No-Code**, vas a tomar las consultas que tu RAG resuelve y conectarlas con n8n para que **disparen acciones reales**: enviar correos, crear tickets, actualizar bases de datos, agendar citas. La cadena Asistente → RAG → Workflow → Acción es lo que convierte un chatbot en un sistema operativo institucional.
