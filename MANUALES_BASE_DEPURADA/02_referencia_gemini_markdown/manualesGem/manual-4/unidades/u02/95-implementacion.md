---
unidad: 2
seccion: implementacion
paginas_objetivo: 4
---

::implementacion{titulo="Implementación Albatros — PRD operativo del Asistente Institucional"}
**Objetivo.** Producir el **PRD v1.0 oficial del Asistente Institucional Albatros**, con sus 3 briefs prioritarios, su mapa de capas, sus ADRs y su DoD adoptado por el equipo. Será la fuente de verdad sobre la que se montan las 8 unidades restantes (RAG, agentes, MCP, Ollama, contenido, gobernanza).

**¿Por qué hacerla?** Sin PRD operativo, las unidades U3–U10 van a producir piezas que pueden no encajar entre sí. Con PRD, cada unidad agrega una capa **acordada** al sistema.

---

### Materiales y recursos

- Repo de la U1 (`prompts-asistente-albatros`).
- Cuenta gratis de un LLM (Claude o ChatGPT).
- Editor markdown.
- Acceso a 2 stakeholders distintos para validación (1 técnico, 1 no técnico).
- 6–8 horas distribuidas en 3 sesiones.

### Pasos

#### Sesión 1 — PRD v1.0 (3 h)

1. **45 min — Recolección.** Entrevista breve con 2 stakeholders sobre dolor real, metas, restricciones.
2. **45 min — Borrador asistido.** Aplicas el meta-PRD del subtema 2.1.
3. **30 min — Stress-test.** 3 críticas (escéptico técnico, financiero, riesgos no listados).
4. **30 min — Refinamiento.** Resuelves preguntas marcadas; firmas v1.0.
5. **30 min — Capa estratégica con IDs.** Asignas `S-NNN` a cada objetivo.

#### Sesión 2 — Briefs y ADRs (2 h)

6. **60 min — 3 briefs.** Para los 3 módulos con mayor prioridad. Cada uno con scope y criterios de aceptación.
7. **40 min — 2-3 ADRs.** Documenta los trade-offs principales (modelo a usar, modo de hosting, tipo de RAG, alcance v1).
8. **20 min — Trazabilidad.** Asignas `F-NNN`, `T-NNN`, `O-NNN` y verificas que cada item técnico/operativo tenga padre estratégico.

#### Sesión 3 — DoD, política y socialización (2-3 h)

9. **30 min — DoD personalizado.** Adoptas el canónico de 9 puntos y agregas 1-2 ítems institucionales.
10. **45 min — Política de uso.** Una página en `/docs/política-uso.md` por módulo.
11. **45 min — Socialización.** Junta con el equipo extendido. Presentas PRD + briefs + DoD. Recolectas dudas.
12. **30 min — Acta y plan.** Documentas decisiones de la junta, abres issues, defines cadencia de revisión (mensual).
::/implementacion

::visual{tipo="ilustracion" descripcion="Mockup del repositorio extendido con la nueva estructura post U2: árbol de archivos visible con `docs/PRD-v1.0.md`, `docs/briefs/B-014.md`, `docs/decisiones/ADR-001.md`, `docs/DoD.md`, `docs/política-uso.md`. A la derecha, una pizarra con el mapa de IDs (S-001 → F-014 → T-027 → O-001) dibujado a mano y firmas de stakeholders al pie. Arriba, etiqueta 'PRD v1.0 firmado el 2026-04-30'. Estilo blueprint paleta Albatros." paginas="1" src="../manualesGem/assets/visuales/manual-4/u02/95-implementacion-v01.svg"}

::implementacion{titulo="Evidencia, entregable y seguimiento"}
### Entregable

1. **`docs/PRD-v1.0.md`** (1 página).
2. **`docs/briefs/`** con 3 archivos (B-014, B-015, B-016).
3. **`docs/decisiones/`** con 2-3 ADRs documentados.
4. **`docs/DoD.md`** con 9 ítems canónicos + 1-2 propios.
5. **`docs/política-uso.md`** con 1 párrafo por módulo.
6. **`docs/mapa-ids.md`** con la jerarquía S/F/T/O.
7. **Acta de junta** (1 pp) con asistentes, decisiones, issues abiertos.

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| PRD en 1 pp | excede o falta | cabe | cabe y stakeholders no técnicos lo entienden solos |
| No-objetivos | ausentes | 2-3 | 4+ explícitos y discutidos |
| Métricas verificables | "satisfactorio" | una numérica | múltiples con cómo medir |
| Briefs trazables | sin IDs | con IDs flojos | trazabilidad completa con padres |
| ADRs | 1 | 2 | 3+ con consecuencias y revisión futura |
| DoD personalizado | canónico tal cual | +1 ítem | +2 ítems institucionales aplicados |
| Política de uso | ausente | una para todo | una por módulo, revisada por legal |
| Socialización | privado | mostrado al equipo | aprobado y con issues abiertos |

### Hitos intermedios

| Día | Hito | Evidencia |
|---|---|---|
| Día 1 | 2 entrevistas a stakeholders | notas + lista de dolores |
| Día 2 | PRD v0.5 generado con meta-prompt | borrador en `docs/` |
| Día 3 | PRD v1.0 firmado | documento + firmas |
| Día 5 | 3 briefs redactados | 3 archivos en `docs/briefs/` |
| Día 6 | 2-3 ADRs principales | archivos en `docs/decisiones/` |
| Día 8 | DoD personalizado adoptado | `docs/DoD.md` |
| Día 9 | Política de uso por módulo | `docs/política-uso.md` |
| Día 10 | Junta de socialización | acta + issues abiertos |
| Día 12 | Mapa de IDs S/F/T/O completo | `docs/mapa-ids.md` |
| Día 14 | Cadencia de revisión agendada | invitación recurrente |

### Reto bonus extendido (3 retos)

**Bonus 1 — PRD diferencial.** Toma una decisión IA reciente de tu institución que se tomó sin PRD (real). Reconstruye el PRD que le habría faltado y compáralo con lo que sucedió. Documenta 3 cosas que el PRD habría prevenido o acelerado.

**Bonus 2 — DoD por módulo.** El DoD canónico es base. Diseña un DoD **específico** para el módulo más sensible del Asistente (ej. crisis emocional, datos de menores, comunicaciones legales) con 3 ítems propios justificados. Aplícalo a un módulo y mide cuánto retrabajo evitas.

**Bonus 3 — ADR retroactivo.** Tu equipo ya tomó 5 decisiones técnicas en U1. Escribe **5 ADRs retroactivos** documentando contexto, decisión, alternativas y consecuencias. Compártelos al equipo y pregunta si las decisiones siguen siendo correctas hoy. Lo que aprendas vale más que los 5 documentos.

### Próximo paso después de esta unidad

En **U3 — Artifacts y Canvases**, vas a tomar el PRD que acabas de aprobar y convertirlo en un **dashboard interactivo** del Asistente Institucional como Artifact. El PRD especifica qué se mide; el Artifact lo hace visible para los stakeholders sin que tengan que abrir el repo.
::/implementacion
::albatros{titulo="Caso complementario — diagnostica un PRD heredado" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Tu institución probablemente tiene un PRD viejo —de marketing, sistemas, RRHH— que nadie revisa hace 12 meses. ¿Sigue describiendo el sistema real?

**Lo que harás.**
1. Pide acceso a un PRD existente de tu institución (no necesariamente IA).
2. Léelo con la checklist de 8 secciones de la unidad.
3. Para cada sección anota: *presente / parcial / ausente*.
4. Para cada métrica anota: *verificable / blanda*.
5. Marca si los IDs (S/F/T/O) existen o no.
6. Identifica **3 brechas más graves** entre el PRD y la realidad operativa actual.
7. Recomienda **una sola** acción: dejar morir el PRD, refrescarlo con un v2 mínimo, o reemplazarlo por un brief operativo.

**Entregable.** Hoja de auditoría de 1 página con 3 brechas y 1 recomendación nominada a un dueño.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cobertura del checklist | <50 % | 8 secciones revisadas | 8 con evidencia y citas al PRD |
| Brechas | genéricas | concretas | concretas con dato observable |
| Recomendación | aspiracional | accionable | con dueño, plazo y costo |
::/albatros
