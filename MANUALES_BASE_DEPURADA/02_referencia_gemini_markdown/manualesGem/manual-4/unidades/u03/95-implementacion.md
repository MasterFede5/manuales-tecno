---
unidad: 3
seccion: implementacion
paginas_objetivo: 5
---

::implementacion{titulo="Implementación Albatros — Mini-suite institucional de Artifacts"}
**Objetivo.** Construir, publicar y versionar la **mini-suite del Asistente Institucional Albatros**: un dashboard maestro + 2 mini-apps utilitarias accesibles por link público y respaldadas en Git. La suite es la cara visible del proyecto para stakeholders no técnicos durante las próximas 6 unidades.

**¿Por qué hacerla?** Artefactos publicados, versionados y compartibles convierten meses de prompts y PRDs en piezas que el equipo y la dirección **usan** todas las semanas. Sin esta capa visible, el proyecto sigue siendo "una promesa".

---

### Materiales y recursos

- Cuenta Claude Pro (recomendado) o ChatGPT Plus/Gemini Advanced.
- Repo Git existente del proyecto (de U1/U2).
- 6–8 horas distribuidas en 3 sesiones.
- Acceso a 3 stakeholders distintos para testeo (1 dirección, 1 administrativo, 1 docente).

### Pasos

#### Sesión 1 — Dashboard maestro (3 h)

1. **30 min — Diseño.** Define qué métricas, módulos, ADRs y riesgos van. Esboza wireframe a mano.
2. **30 min — Primer prompt estructurado.** Aplica plantilla del subtema 3.4.
3. **90 min — Iteración.** 5–8 versiones para datos, layout, mobile, polish, accesibilidad.
4. **15 min — Publicación.** Botón Publish, prueba en mobile e incógnito.
5. **15 min — Versionado.** Download + commit + tag v1.0.0 + snapshots.

#### Sesión 2 — Mini-apps utilitarias (2 h)

Elige 2 de las siguientes (las más útiles para tu institución):
- **Calculadora de cupos disponibles** (subtema 3.4 ejemplo 2).
- **Generador de comunicados** (3.4 ejemplo 6).
- **Quiz de orientación vocacional** (3.4 ejemplo 5).
- **Simulador de horarios** (proyecto propio).
- **Formulario de pre-inscripción** (3.4 ejemplo 4).

Cada mini-app: 60 min (prompt → iteraciones → publish → versionado).

#### Sesión 3 — Distribución, validación e integración (1–2 h)

6. **30 min — Hub de la suite.** Crea un Artifact índice (HTML estático simple) con cards y links a cada mini-app de la suite.
7. **30 min — Testeo cruzado.** 3 stakeholders abren los links desde sus dispositivos y reportan.
8. **30 min — Integración con Notion del equipo.** Embed iframes o links en página dedicada.
9. **30 min — Documentación final.** Actualiza `README.md` del repo con sección "Suite institucional v1.0".
::/implementacion

::visual{tipo="ilustracion" descripcion="Mockup de la suite institucional desplegada: hoja con índice (Artifact HTML) en el centro, 3 cards apiladas (Dashboard, Calculadora cupos, Generador comunicados), cada card con icono + nombre + URL. Alrededor, capturas pequeñas de los 3 Artifacts en distintos dispositivos (iPad, smartphone, laptop). Bajo todo, mini-tira de versiones v1.0.0, v1.1.0, v1.2.0 con fechas. Estilo blueprint Albatros, paleta azul + naranja." paginas="1" src="../manualesGem/assets/visuales/manual-4/u03/95-implementacion-v01.svg"}

::implementacion{titulo="Evidencia, entregable y seguimiento"}
### Entregable

1. **3 URLs públicas** (dashboard maestro + 2 mini-apps).
2. **1 hub índice** con links a las 3.
3. **Repo `tools/`** con carpetas por mini-app, código, snapshots y CHANGELOGs.
4. **Documento de testeo** (1–2 pp): 3 reportes de stakeholders, hallazgos, issues abiertos.
5. **Actualización del README** del proyecto con la nueva sección.

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Cantidad de Artifacts | 1 | 2 | 3+ con hub |
| Calidad del dashboard | layout pobre | funcional | profesional con sparklines y tabs |
| Mobile responsive | no funciona | aceptable | impecable |
| Versionado | sin commit | commit | tag + CHANGELOG + snapshots |
| Distribución | privado | URLs compartidas | embed en hub corporativo |
| Validación con stakeholders | sin testeo | 1 persona | 3 personas con reporte documentado |
| Integración con repo | suelto | en carpeta | con README actualizado |

### Hitos intermedios

| Día | Hito | Evidencia |
|---|---|---|
| Día 1 | Wireframe a mano del dashboard | foto del papel |
| Día 2 | Dashboard v1.0.0 publicado | URL + repo + tag |
| Día 3 | Mini-app 1 publicada | URL + repo + tag |
| Día 5 | Mini-app 2 publicada | URL + repo + tag |
| Día 6 | Hub índice con 3 links | URL del hub |
| Día 7 | Testeo cruzado con 3 stakeholders | reporte 1 página |
| Día 9 | Integración con Notion del equipo | captura del Notion con embed |
| Día 10 | README del repo actualizado | sección "Suite institucional v1.0" |

### Reto bonus extendido (3 retos)

**Bonus 1 — Versionado en CI.** Configura GitHub Actions para que cada vez que se cree un commit en `tools/dashboard/` se genere automáticamente un snapshot PNG de la última versión y se publique en `tools/dashboard/snapshots/`. Esto te protege si pierdes acceso al proveedor.

**Bonus 2 — Suite con auth ligera.** Toma una de las mini-apps publicadas y migra a un deploy real en Vercel con un guard simple (URL con token compartido o login mínimo). Mide cuánto tarda y qué problemas surgen — esto te entrena para el día que un Artifact no alcance.

**Bonus 3 — Embed institucional.** Embebe el dashboard en la intranet de tu institución (Notion del equipo, página interna, lo que tengas). Mide visitas durante 2 semanas y reporta si los stakeholders lo abren más al estar embebido vs. con link suelto.

### Próximo paso después de esta unidad

En **U4 — Bases de Conocimiento y RAG**, vas a hacer que tu Asistente "lea" el reglamento institucional. Las mini-apps de esta unidad serán las **interfaces** desde las que los usuarios consultarán el conocimiento que U4 va a indexar. Sin la suite, el RAG funciona en el aire; con ella, los usuarios tienen por dónde entrar.
::/implementacion
::albatros{titulo="Reto complementario — un Artifact por dolor recurrente del equipo" tipo="reto" tiempo="30 min"}
**Pregunta detonadora.** En tu equipo seguro hay una tarea que **se repite cada semana** y nadie ha encontrado tiempo de automatizar. ¿Y si la convirtieras en Artifact en 30 minutos?

**Lo que harás.**
1. En 5 minutos, lista 5 tareas repetitivas de tu equipo (planeación de clases, conteo de horas, generación de minutas, seguimiento de tareas, etc.).
2. Elige la que más "duele" — la que más quejas genera o más tiempo consume.
3. Aplica el primer prompt patrón en Claude.
4. Itera 3-4 veces sin perfeccionar — busca un MVP en 25 min.
5. Publica el link.
6. Mándalo al equipo con el mensaje: *"esto está crudo, pero úsenlo esta semana y díganme si vale la pena pulirlo"*.

**Entregable.** URL del Artifact + lista de 5 tareas + decisión razonada de cuál atendiste.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Lista de tareas | <3 | 5 tareas | 5 tareas con tiempo semanal estimado |
| Justificación de la elegida | "me gustó" | duración | duración × frecuencia |
| MVP funcional | parcial | resuelve la tarea | resuelve y mobile |
| Distribución | privado | enviado al equipo | usado por al menos 1 persona |
::/albatros
