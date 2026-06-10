---
manual: 4
titulo: "Inteligencia Artificial Avanzada"
subtitulo: "Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza"
publico: "Egresados de Manual 3 · profesionales con uso intensivo de IA"
unidades: 10
paginas_total_objetivo: 382
paginas_min: 350
paginas_max: 450
prerrequisitos: "Manual 3 (IA Básica)"
case_study:
  nombre: "Asistente Institucional Albatros"
  premisa: |
    La dirección de tu institución te encarga diseñar un Asistente IA
    Institucional: gestiona conocimiento interno, automatiza flujos,
    responde a estudiantes, opera con herramientas reales y respeta
    políticas de gobernanza. Cada unidad agrega una capa al sistema.
  episodios:
    U1: "Prompts versionados y plantillas de la institución"
    U2: "PRD del Asistente Institucional"
    U3: "Dashboard interactivo del Asistente como Artifact"
    U4: "El Asistente lee el reglamento (RAG)"
    U5: "El Asistente automatiza solicitudes (n8n)"
    U6: "El Asistente actúa: agente con herramientas"
    U7: "Versión local soberana con Ollama + Open WebUI"
    U8: "El Asistente conectado a archivos vía MCP"
    U9: "El Asistente produce material educativo certificable"
    U10: "Plan de implementación, costos y gobernanza"
---

# Manifest — Manual 4: IA Avanzada

## Asignación de páginas (suma = 376 pp)

| Sección | pp | acumulado |
|---|---:|---:|
| Front matter (10) + diagnóstica (4) | 14 | 14 |
| **U1 — Prompt Engineering Avanzado** | 35 | 49 |
| **U2 — Especificaciones de Tareas y Proyectos** | 30 | 79 |
| **U3 — Artifacts y Canvases** | 35 | 114 |
| **U4 — Bases de Conocimiento y RAG** | 35 | 149 |
| **U5 — Workflows e Integraciones (No-Code)** | 35 | 184 |
| **U6 — Agentes de IA** | 35 | 219 |
| **U7 — IA Local y Open Source** | 30 | 249 |
| **U8 — MCP y Conexión de Herramientas** | 30 | 279 |
| **U9 — Contenido Especializado de Alto Nivel** | 40 | 319 |
| **U10 — Estrategia, Costos y Gobernanza** | 30 | 349 |
| Examen integrador + glosario + biblio + índice | 27 | **376** |

---

## U1 — Prompt Engineering Avanzado (35 pp)

**Caso E1:** Sistema de prompts versionados para todo el equipo.

| Subtema | pp |
|---|---:|
| 1.1 Estructura XML y delimitadores | 4 |
| 1.2 Meta-prompting | 4 |
| 1.3 CoT avanzado y ReAct | 5 |
| 1.4 Self-consistency y Tree-of-Thoughts | 4 |
| 1.5 Prompt chaining | 5 |
| 1.6 Few-shot estratégico | 3 |
| 1.7 Constrained output (JSON, schemas) | 4 |
| 1.8 Evaluación de prompts (rúbricas, A/B) | 3 |
| Práctica resuelta + Actividades + Implementación | 3 |

**Visuales:** anatomía XML · diagrama prompt chain · rúbrica de evaluación.

---

## U2 — Especificaciones de Tareas y Proyectos (30 pp)

**Caso E2:** PRD del Asistente Institucional Albatros.

| Subtema | pp |
|---|---:|
| 2.1 PRD asistido por IA | 5 |
| 2.2 Plantillas Albatros: brief, scope, criterios | 4 |
| 2.3 Definition of Done para tareas con IA | 4 |
| 2.4 Especificaciones por capas | 5 |
| 2.5 Spec-driven prompting | 5 |
| 2.6 Manejo de ambigüedad y trade-offs | 3 |
| Práctica resuelta + Actividades + Implementación | 4 |

**Visuales:** plantilla PRD · diagrama capas · ejemplo trade-off.

---

## U3 — Artifacts y Canvases (35 pp)

**Caso E3:** Dashboard interactivo del Asistente Institucional como Artifact.

| Subtema | pp |
|---|---:|
| 3.1 ¿Qué son los Artifacts? Tipos | 5 |
| 3.2 Claude Artifacts (creación, iteración, publicación) | 8 |
| 3.3 ChatGPT Canvas y Gemini Canvas | 5 |
| 3.4 Mini-apps con Artifacts (React, HTML, p5.js) | 6 |
| 3.5 Compartir y embeber | 3 |
| 3.6 Versionado y control de cambios | 3 |
| Práctica resuelta + Actividades + Implementación | 5 |

**Visuales:** capturas builder · cuadro tipos · ejemplo embed.

---

## U4 — Bases de Conocimiento y RAG (35 pp)

**Caso E4:** El Asistente lee el reglamento institucional.

| Subtema | pp |
|---|---:|
| 4.1 Concepto de Retrieval-Augmented Generation | 4 |
| 4.2 Embeddings y vectores (concepto sin código) | 4 |
| 4.3 RAG sin código (GPT files, Claude Projects, NotebookLM Enterprise) | 8 |
| 4.4 Plataformas no-code: Dify, Flowise, Stack AI | 6 |
| 4.5 Chunking, metadatos, citado | 5 |
| 4.6 RAG vs fine-tuning: cuándo conviene | 4 |
| Práctica resuelta + Actividades + Implementación | 4 |

**Visuales:** infografía pipeline RAG · cuadro chunking · capturas Dify.

---

## U5 — Workflows e Integraciones No-Code (35 pp)

**Caso E5:** El Asistente automatiza solicitudes con n8n.

| Subtema | pp |
|---|---:|
| 5.1 n8n con IA | 6 |
| 5.2 Make (Integromat) | 5 |
| 5.3 Zapier AI Actions | 4 |
| 5.4 Power Automate con Copilot | 4 |
| 5.5 Webhooks, APIs y triggers | 4 |
| 5.6 Integraciones con Notion, Airtable, Workspace | 5 |
| 5.7 Patrones reutilizables | 3 |
| Práctica resuelta + Actividades + Implementación | 4 |

**Visuales:** capturas n8n · diagrama de patrones.

---

## U6 — Agentes de IA (35 pp)

**Caso E6:** El Asistente actúa: agente con herramientas reales.

| Subtema | pp |
|---|---:|
| 6.1 ¿Qué es un agente? Diferencia con un chatbot | 4 |
| 6.2 Anatomía: percepción, planificación, herramientas, memoria | 5 |
| 6.3 Tipos: reactivos, deliberativos, multi-agente | 4 |
| 6.4 Plataformas: ChatGPT Agents, Claude Computer Use, Manus, Devin, Lindy | 8 |
| 6.5 Tool use / function calling (concepto) | 4 |
| 6.6 Riesgos: alucinación de acciones, loops, costo | 4 |
| Práctica resuelta + Actividades + Implementación | 6 |

**Visuales:** anatomía agente · cuadro plataformas · diagrama riesgos.

---

## U7 — IA Local y Open Source (30 pp)

**Caso E7:** Versión soberana del Asistente con Ollama y Open WebUI.

| Subtema | pp |
|---|---:|
| 7.1 ¿Por qué local? Privacidad, costo, control | 3 |
| 7.2 Ollama: descarga y ejecución | 5 |
| 7.3 Open WebUI (interfaz local tipo ChatGPT) | 5 |
| 7.4 LM Studio y Jan | 3 |
| 7.5 Modelos abiertos: Llama, Mistral, Qwen, DeepSeek | 5 |
| 7.6 Cuantización y hardware | 3 |
| 7.7 Conexión con bases de conocimiento locales | 3 |
| Implementación Albatros: servidor IA personal | 3 |

**Visuales:** capturas Ollama / Open WebUI · cuadro modelos · diagrama hardware.

---

## U8 — MCP y Conexión de Herramientas (30 pp)

**Caso E8:** El Asistente conectado a archivos institucionales vía MCP.

| Subtema | pp |
|---|---:|
| 8.1 Model Context Protocol (qué resuelve) | 5 |
| 8.2 Servidores MCP populares (filesystem, GitHub, Slack, Notion) | 8 |
| 8.3 Claude Desktop con MCP | 5 |
| 8.4 ChatGPT con conectores empresariales | 4 |
| 8.5 Casos de uso reales | 4 |
| Implementación Albatros: MCP local con archivos propios | 4 |

**Visuales:** diagrama MCP · capturas configuración · cuadro conectores.

---

## U9 — Contenido Especializado de Alto Nivel (40 pp)

**Caso E9:** El Asistente produce material educativo certificable.

| Subtema | pp |
|---|---:|
| 9.1 Investigación profunda (Deep Research, ChatGPT/Gemini/Perplexity) | 6 |
| 9.2 Documentos técnicos y whitepapers | 5 |
| 9.3 Materiales educativos (rúbricas, secuencias, exámenes) | 6 |
| 9.4 Diseño UX con IA (Galileo, Uizard) | 5 |
| 9.5 Contenido legal y de cumplimiento (con disclaimer) | 5 |
| 9.6 Generación de datasets sintéticos | 5 |
| Implementación Albatros: curso digital corto producido con IA | 8 |

**Visuales:** capturas Deep Research · plantillas rúbrica · ejemplo dataset sintético.

---

## U10 — Estrategia, Costos y Gobernanza (30 pp)

**Caso E10:** Plan de implementación del Asistente para 1 año.

| Subtema | pp |
|---|---:|
| 10.1 Comparativo de planes (ChatGPT, Claude, Gemini, Copilot) | 5 |
| 10.2 Costos por tokens y optimización | 5 |
| 10.3 Política de uso de IA en la organización | 5 |
| 10.4 Métricas de retorno | 4 |
| 10.5 Confidencialidad y datos sensibles | 4 |
| Implementación Albatros: plan completo institucional | 7 |

**Visuales:** cuadro precios · plantilla política · dashboard métricas.
