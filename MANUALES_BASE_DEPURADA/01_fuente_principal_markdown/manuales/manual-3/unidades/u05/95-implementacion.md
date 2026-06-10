---
unidad: 5
seccion: implementacion
paginas_objetivo: 4
---

::implementacion{titulo="Implementación Albatros — NotebookLM completo de UNA materia tuya"}
**Objetivo.** Construir un **NotebookLM completo** para una materia que estás cursando: 12-20 fuentes (libro, papers, slides, apuntes), un audio overview maestro, mapa mental general, briefing por capítulo, study guide. El producto será **tu compañero de estudio principal** para esa materia durante el semestre.

**¿Por qué hacerla?** Aplicas la unidad a tu vida real, no a un ejercicio académico. Y construyes un activo permanente: cada vez que estudies esa materia el resto del semestre, tendrás todo organizado.

---

### Materiales y herramientas

- Cuenta gratis NotebookLM (Google).
- Tu material de la materia (libro, slides, papers, apuntes digitalizados).
- Acceso a Perplexity Pro (recomendado) para complementar.
- 4 horas en 2 sesiones.

### Pasos

1. **Elige la materia.** La que más se te dificulte o la que más te gusta.
2. **Inventario de fuentes.** Lista 12-20 fuentes que necesitas digerir:
   - Libro de texto principal (PDF).
   - Slides del profesor (PDFs o links Google Slides).
   - 3-5 papers complementarios.
   - Tus apuntes (digitaliza si están a mano).
   - Videos de YouTube relevantes (URLs).
3. **Crea el notebook.** Sube todas las fuentes. Verifica que NotebookLM las procesó.
4. **Genera contenido inicial:**
   - Briefing Doc (3-5 páginas).
   - Mind Map (exporta como imagen).
   - Audio Overview de 15-20 minutos. Escúchalo.
   - Study Guide (30+ preguntas).
5. **Profundiza por capítulo.** Para los 5-7 capítulos más importantes:
   - Pregunta al notebook: *"Resume el capítulo X en 200 palabras + 3 preguntas tipo examen + 1 ejemplo aplicado."*
   - Guarda como nota en el notebook.
6. **Conecta con Perplexity.** Para los temas con dudas, busca con Perplexity Academic, anota las citas y agrégalas al notebook como nuevas sources.
7. **Mantenimiento.** Cada semana, agrega: clase nueva (foto del pizarrón), tu nuevo apunte, lecturas asignadas. NotebookLM se mantiene actualizado.
8. **Antes de examen.** Genera Audio Overview enfocado: *"haz audio overview pero centrado en los temas X, Y, Z que vienen en el examen del viernes"*.

::visual{tipo="ilustracion" descripcion="Captura de NotebookLM completo del estudiante: panel Sources con 18 documentos cargados (libro Tippens, slides 1-12, apuntes octubre-diciembre, 4 papers Khan Academy, videos YouTube). Panel central con notebook chat activo y notas guardadas. Panel Studio con: Briefing Doc generado (5 pp), Mind Map exportado, Audio Overview de 18 min, Study Guide con 35 preguntas, FAQ con 12 preguntas. Estudiante con auriculares escuchando en transporte público con celular." paginas=1}

---

### Entregable

1. **Link a NotebookLM** (compartido en lectura con tu profesor para validación).
2. **Audio Overview** descargado MP3 (15-20 min).
3. **Briefing Doc** descargado PDF (3-5 pp).
4. **Mind Map** exportado como imagen.
5. **Study Guide** con respuestas modelo (puedes pedirlas al notebook).
6. **Reporte de implementación** (1-2 pp):
   - Materia elegida y fuentes cargadas (lista).
   - Mejor descubrimiento (algo que no sabías de las fuentes).
   - Cómo cambió tu manera de estudiar después de hacerlo.
   - Plan de mantenimiento del notebook el resto del semestre.
7. **Captura de tu calificación** del primer examen después de usar el notebook (si aplica).

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| **Cantidad de fuentes** | < 8 | 12-15 | 18+ con variedad |
| **Diversidad de fuentes** | un solo tipo | 2-3 tipos | libros + papers + slides + videos + apuntes |
| **Producto generado** | solo briefing | briefing + audio | briefing + audio + mind map + study guide + FAQ |
| **Notas personales agregadas** | 0 | 5-10 | 20+ con valor crítico |
| **Plan de mantenimiento** | sin plan | mensual | semanal con calendario |
| **Impacto medido** | sin medir | reflexión cualitativa | comparación cuantitativa con calificaciones |

### Hitos intermedios

| Sprint | Duración | Mini-entregable | Verificación |
|---|---|---|---|
| **S1 — Curaduría de fuentes** | 60 min | Lista de 18+ fuentes con prioridad y tipo | Variedad confirmada (papers + libros + slides + videos + apuntes) |
| **S2 — Carga e indexado** | 45 min | Notebook poblado y verificado con preguntas de control | 3 preguntas en zonas distintas devuelven citas correctas |
| **S3 — Generación de productos** | 60 min | Briefing + audio + mapa mental + study guide | Cada producto auditado con al menos 2 datos |
| **S4 — Mantenimiento y plan** | 30 min | Calendario semanal + plan de actualización mensual | Próximas 4 semanas con tareas concretas |

### Reto bonus extendido

1. **Reto comparativo de plataformas.** Repite el mismo notebook en **Claude Projects** y compara: ¿qué hace mejor cada una con tus fuentes? Documenta diferencias.
2. **Reto del notebook colaborativo.** Junta tus fuentes con las de 2 compañeros de la misma materia (60 fuentes en total). Curen colectivamente y compartan los productos generados.
3. **Reto del impacto medido.** Mide tu calificación en **3 exámenes consecutivos** después de implementar el notebook, y compárala con tu promedio anterior. Documenta delta.
::/implementacion

---

::albatros{titulo="Reto rápido — el ensayo de 30 minutos con 5 citas verificadas" tipo="reto" tiempo="30 min"}
**Pregunta detonadora.** ¿Puedes producir un ensayo investigativo de 1 página con 5 citas reales y verificadas en solo 30 minutos?

**Lo que harás.**
1. **Define la pregunta** específica de tu ensayo en 30 segundos.
2. **Lanza Perplexity Academic** y obtén 5 papers candidatos con DOI (5 min).
3. **Verifica cada DOI** en doi.org (3 min).
4. **Cruza con Consensus** para validar consenso (3 min).
5. **Pide a Claude/ChatGPT** que redacte 700 palabras integrando las 5 citas reales (8 min).
6. **Reescribe** en tu voz personal 2 párrafos (5 min).
7. **Agrega declaración de uso de IA** y entregas (3 min).

**Materiales.** Cuentas free de Perplexity, Consensus, doi.org, Claude/ChatGPT.

**Entregable.** Ensayo de 1 página + bitácora de verificación de DOIs + declaración de uso de IA.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Citas verificadas | 0-2 | 4 | 5/5 con bitácora |
| Voz personal | 0% reescrito | 1 párrafo | 2+ párrafos en voz propia |
| Tiempo | > 45 min | 30-45 min | < 30 min con calidad |
::/albatros
