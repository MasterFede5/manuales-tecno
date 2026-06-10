---
unidad: 6
seccion: cierre
paginas_objetivo: 2
---

## Cierre y autoevaluación — Unidad 06

Cerraste la unidad de Agentes de IA. Ahora puedes:

1. **Distinguir** chatbot, workflow y agente, y elegir el adecuado por caso.
2. **Diseñar agentes** con los 5 componentes (percepción, planificación, tools, memoria, ejecución) bien integrados.
3. **Elegir arquitectura** (reactivo, deliberativo, jerárquico, multi-agente) según complejidad real.
4. **Operar plataformas** modernas (n8n AI Agent, Lindy, Claude Computer Use, AutoGen).
5. **Aplicar tool use / function calling** con schemas estrictos y descripciones explícitas.
6. **Mitigar los 7 riesgos** de agentes en producción con safeguards documentados.

> **Frase puente.** Tu agente vive en la nube, depende de proveedores externos. Para casos donde tu institución requiere **soberanía total** (datos sensibles, presupuesto contenido, sin lock-in), la siguiente unidad cubre el camino: **IA local y open source** con Ollama, modelos abiertos como Llama y Qwen, y Open WebUI como interfaz tipo ChatGPT en tu propio servidor.

---

### Autoevaluación (rúbrica de 5 niveles)

| Saber | 1 — Inicial | 2 | 3 — Suficiente | 4 | 5 — Excelente |
|---|---|---|---|---|---|
| **Concepto agente** | confundido | conozco diferencia | distingo de chatbot/workflow | elijo según caso | enseño a otros |
| **Anatomía** | desconozco | conozco 2-3 componentes | 5 componentes integrados | con observabilidad | con memoria a largo plazo |
| **Arquitecturas** | uso una | conozco 4 | elijo según problema | con criterios de upgrade | matriz documentada |
| **Plataformas** | uso una | conozco varias | elijo según contexto | self-hosted con framework | combinación multi-plataforma |
| **Function calling** | desconozco | uso default | tools con schemas estrictos | descripciones explícitas | tools con permisos por rol |
| **Riesgos y safeguards** | sin atender | 2-3 mitigados | 5-6 de 7 | los 7 con evidencia | runbook + auditoría continua |
| **Agente en producción** | demo | uno corriendo | con monitoreo | con golden set | con métricas y costo proyectado |

### Pregunta de cierre

> Tu agente lleva 3 meses en producción. Acumuló: 1 200 ejecuciones, $580 de costo, 14 escalaciones a humano (1.2 %), 0 incidentes graves. La dirección quiere extender el agente a "redactar comunicados oficiales sin aprobación humana porque ahorra tiempo". **Diseña** tu respuesta en 5 actos numerados: (1) qué riesgo nuevo introduces; (2) qué dice tu ADR-008; (3) qué experimento controlado propones (canary/A/B); (4) qué nuevos safeguards exigirías; (5) cómo presentas la propuesta a dirección.

### Conexión con la siguiente unidad

En **U7 — IA Local y Open Source**, vas a llevar contigo el agente que construiste y aprenderás a **migrarlo a Ollama** para ciertos casos (especialmente clasificación, RAG ligero) donde la soberanía justifica el costo. El multi-stack (cloud + local) es la frontera de 2025.
