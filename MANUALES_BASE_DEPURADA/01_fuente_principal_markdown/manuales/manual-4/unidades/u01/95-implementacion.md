---
unidad: 1
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Sistema de prompts versionados de tu institución"}
**Objetivo.** Construir y poner en marcha un **repositorio de prompts versionados** que cubra al menos **3 tareas operativas reales** del Asistente Institucional, con golden sets, evaluaciones cruzadas y un proceso de release definido. Es la primera capa de infraestructura sobre la que vas a construir las 9 unidades restantes.

**¿Por qué hacerla?** Sin un sistema de prompts versionados, todo lo que aprendas en U2–U10 (PRD, Artifacts, RAG, agentes, MCP) opera sobre arena: cualquier cambio rompe lo que funcionaba ayer. Esta unidad te entrega el **suelo**.

---

### Materiales y recursos

- Repositorio Git (GitHub gratis o GitLab) o, si tu equipo no usa Git, un Notion estructurado con la misma jerarquía.
- Cuenta en al menos un proveedor LLM (Claude o ChatGPT con API o web).
- Editor de texto (VSCode recomendado por syntax highlighting de XML/JSON).
- Hoja de cálculo para los golden sets (puedes exportar a JSONL después).
- 8–12 horas distribuidas en 4 sesiones.

### Pasos

#### Sesión 1 — Arquitectura del repo (2 h)

```
prompts-asistente-albatros/
├── README.md                  # cómo usar el repo
├── CONTRIBUTING.md            # cómo proponer cambios
├── prompts/
│   ├── tarea-A/
│   │   ├── v1.0.xml
│   │   ├── v1.0.eval.jsonl
│   │   └── CHANGELOG.md
│   ├── tarea-B/
│   └── tarea-C/
├── evals/
│   ├── runner.py              # corre golden sets
│   └── reports/
└── docs/
    └── decisiones-de-diseno.md
```

Documenta en `README.md` el ciclo de vida: idea → meta-prompt → v0 → critique → v1 → smoke → golden → A/B → producción.

#### Sesión 2 — Tarea A (3 h)

Elige tu tarea más obvia (sugerencia: **clasificador de solicitudes**). Aplica la práctica resuelta. Entregable de la sesión: `prompts/clasificador/v1.0.xml` + golden set de 20 ejemplos + reporte.

#### Sesión 3 — Tareas B y C (3 h)

- Tarea B sugerida: **redactor de comunicados oficiales**.
- Tarea C sugerida: **resumen ejecutivo de juntas** (input transcripción → output 5 puntos).

Cada una con su flujo completo: meta-prompt → v0 → v1 → golden de mínimo 15 ejemplos → eval cruzada por otra persona del equipo.

#### Sesión 4 — Documentación y socialización (2 h)

- Escribe `decisiones-de-diseno.md` con 5 decisiones difíciles que tomaste y por qué.
- Presenta el repo al equipo en una junta de 30 minutos.
- Recolecta dudas y registra al menos 3 issues para v1.1.
- Define cadencia de revisión: **mensual** durante los próximos 6 meses.

::visual{tipo="ilustracion" descripcion="Mockup del repositorio en GitHub: vista del árbol de archivos con prompts/clasificador/v1.0.xml, evals/runner.py, CHANGELOG.md visibles. A la derecha del repo, captura de pantalla de un PR abierto con la propuesta de v1.1, comentarios de revisión de un compañero y badge de tests passing tras correr el golden. Mensaje: 'tus prompts son ahora código y el equipo los revisa como tal'. Estilo limpio, paleta azul Albatros." paginas=1}

---

### Entregable

1. **URL del repositorio público o privado** con acceso de lectura para tu evaluador.
2. **3 prompts versionados** (v1.0 mínimo), cada uno con:
   - Archivo XML del prompt.
   - Golden set en JSONL (≥15 ejemplos).
   - CHANGELOG con decisiones documentadas.
3. **Reporte de evaluación cruzada** (1–2 pp): qué evaluó cada persona del equipo, hallazgos.
4. **Documento `decisiones-de-diseno.md`** con 5 decisiones difíciles.
5. **Acta de la junta de socialización** (1 pp): asistentes, dudas planteadas, issues abiertos.

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Estructura del repo | archivos sueltos | jerarquía propuesta | jerarquía + README + CONTRIBUTING |
| Prompts XML | texto plano disfrazado | XML con secciones | XML completo con justificación |
| Golden sets | <10 ejemplos | 15 ejemplos diversos | 20+ con bordes deliberados |
| Constrained output | sin schema | schema básico | schema estricto validado en runtime |
| Evaluación cruzada | autor solo | una persona más | rúbrica multi-evaluador con datos |
| Documentación | mínima | README + CHANGELOG | README + CHANGELOG + decisiones |
| Socialización | privado | mostrado al equipo | equipo lo adoptó y abrió issues |

### Hitos intermedios

Para no llegar al final con todo apilado, cierra cada hito antes de pasar al siguiente. Si un hito se atrasa más de 2 días, pide ayuda en lugar de seguir empujando solo:

| Día | Hito | Evidencia esperada |
|---|---|---|
| Día 1 | Repo creado con árbol vacío | URL del repo + README inicial |
| Día 2 | `clasificador/v1.0.xml` listo | XML completo + smoke test pasado |
| Día 3 | Golden de clasificador (20) | JSONL en `evals/` + reporte 1 página |
| Día 5 | `redactor/v1.0.xml` + golden 15 | XML + JSONL |
| Día 7 | `resumen-juntas/v1.0.xml` + golden 15 | XML + JSONL |
| Día 8 | Eval cruzada por compañero | reporte firmado |
| Día 10 | `decisiones-de-diseno.md` con 5 entradas | doc en `docs/` |
| Día 12 | Junta de socialización | acta + 3 issues abiertos |
| Día 14 | Cadencia mensual agendada | invitación recurrente |

### Reto bonus extendido (3 retos)

Cuando la implementación esté en su lugar, **uno** de estos 3 retos te lleva al siguiente nivel. Elige el que más rinda a tu contexto:

**Bonus 1 — Self-consistency en producción.** Aplica self-consistency con n=5 únicamente al `clasificador` (no al redactor — ahí es desperdicio). Mide en 50 ejemplos: ¿sube precisión? ¿cuánto sube el costo? Decide con datos si activarlo siempre, solo en categorías difíciles, o nunca. Documenta la decisión.

**Bonus 2 — Pipeline cruzado de modelos.** Reescribe `redactor-comunicados` para que el meta-prompting use Claude Opus (mayor calidad) y la inferencia de producción use Claude Haiku (10x más barato). Verifica que la calidad cae menos del 10 % en el golden y celebra el 90 % de ahorro.

**Bonus 3 — Detector automático de regresiones.** Escribe `evals/runner.py` para que corra el golden en CI cada vez que tocas un prompt. Si baja >2 puntos de calidad respecto al baseline, falla el commit. Convierte tu repo en CI-protected y deja un README de "cómo correr el runner localmente".

### Próximo paso después de esta unidad

En **U2** vas a aprender a redactar el **PRD del Asistente Institucional**. Cuando lo hagas, los prompts versionados de esta unidad serán las **piezas que el PRD lista como activos del sistema**. Sin este Episodio 1 cerrado, U2 va a flotar.
::/implementacion

::albatros{titulo="Reto complementario — auditas un prompt heredado de tu institución" tipo="reto" tiempo="30 min"}
**Pregunta detonadora.** Tu institución ya usa IA en algún flujo —marketing, admisiones, atención a padres—. Probablemente alguien escribió un prompt hace 6 meses, lo dejó en una nota y nadie lo ha tocado. ¿Está vivo o está pudriéndose?

**Lo que harás.**
1. Identifica un prompt **realmente en uso** en tu institución (puede ser de marketing, RRHH, atención al cliente, biblioteca).
2. Pide acceso a su versión actual y a 5 outputs recientes.
3. Audita con la checklist de la unidad: ¿XML?, ¿constrained output?, ¿golden?, ¿versionado?, ¿owner?, ¿cadencia de revisión?
4. Anota cada respuesta y asigna semáforo (rojo/ámbar/verde).
5. Escribe **una página** con 3 recomendaciones concretas y la persona responsable de cada una.

**Entregable.** Una página de auditoría con 6 ítems, semáforo y 3 recomendaciones nominadas a un dueño.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cobertura del checklist | <3 | 6 ítems | 6 ítems con evidencia |
| Recomendaciones | genéricas | accionables | con dueño y plazo |
| Comunicación | informal | reporte presentable | reporte aceptado por el dueño actual |
::/albatros
