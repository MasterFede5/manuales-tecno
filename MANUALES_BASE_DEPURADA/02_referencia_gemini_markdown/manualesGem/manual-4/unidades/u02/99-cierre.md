---
unidad: 2
seccion: cierre
paginas_objetivo: 2
---

## Cierre y autoevaluación — Unidad 02

Cerraste la unidad de Especificaciones y PRD. Ahora puedes:

1. **Redactar un PRD asistido por IA** con sus 8 secciones obligatorias, métricas verificables y no-objetivos explícitos.
2. **Aplicar plantillas Albatros** (brief, scope, criterios) para descomponer el PRD en encargos accionables.
3. **Adoptar Definition of Done** con los 9 ítems canónicos para tareas con IA y agregar los institucionales.
4. **Especificar por capas** (estratégica, funcional, técnica, operativa) con trazabilidad mediante IDs.
5. **Aplicar spec-driven prompting** para que tus prompts y tus specs sean una sola fuente de verdad.
6. **Documentar trade-offs y ambigüedad** con ADRs y el cono de incertidumbre, gestionando expectativas.

> **Frase puente.** Un PRD vive en un PDF. Para que el equipo, los stakeholders y los padres **vean cómo va el proyecto en tiempo real**, necesitas un dashboard. La Unidad 3 te enseña a construirlo como **Artifact** (Claude Artifacts, ChatGPT Canvas, Gemini Canvas) sin escribir HTML, CSS ni JS, conectado al PRD que acabas de redactar.

---

### Autoevaluación (rúbrica de 5 niveles)

| Saber | 1 — Inicial | 2 | 3 — Suficiente | 4 | 5 — Excelente |
|---|---|---|---|---|---|
| **PRD asistido por IA** | improvisado | con IA pero sin stress-test | con stress-test de 3 ángulos | con métricas y no-objetivos | con plan de pivote y costo a 12 meses |
| **Plantillas brief/scope/criterios** | no las uso | las uso a veces | brief + scope completos | con criterios verificables | revisadas por terceros y firmadas |
| **DoD para IA** | "se siente bien" | smoke test | DoD canónico aplicado | con ítems institucionales | con evidencias y rollback probado |
| **Capas y trazabilidad** | sin distinguir | menciono capas | uso IDs S/F/T/O | trazabilidad bidireccional | mapeo dinámico que el equipo opera |
| **Spec-driven prompting** | spec y prompt separados | comparto spec | spec ES el prompt | generador script→prompt | spec ejecutable con build automático |
| **Trade-offs y ADRs** | decido a ojo | a veces explico | ADRs informales | ADRs canónicos con consecuencias | revisión documentada cada trimestre |

### Pregunta de cierre

> Tu PRD v1.0 fue aprobado el viernes. El lunes a primera hora, el director te llama y dice "hablé con el patronato y necesito que el Asistente también ofrezca asesoría psicopedagógica". Esa funcionalidad está en tus no-objetivos como "v1.0 NO sustituye al psicopedagogo". **Diseña** tu respuesta en 5 pasos numerados, citando explícitamente: PRD, capa estratégica, ADR a abrir, criterios para incluir vs no, y plan de salida si la decisión no se concreta.

### Conexión con la siguiente unidad

En **U3 — Artifacts y Canvases**, vas a llevar contigo dos artefactos de esta unidad: el **PRD v1.0** (que será la fuente de los datos a visualizar) y el **mapa de IDs** (que será la estructura de navegación del dashboard). El siguiente Episodio convierte tu documento en una experiencia interactiva.
