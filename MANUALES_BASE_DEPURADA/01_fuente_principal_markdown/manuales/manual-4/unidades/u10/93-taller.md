---
unidad: 10
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Plan a 12 meses para el patronato: presupuesto, política, KPIs y matriz de seguridad

> Este taller es el cierre operativo del manual. En 60 minutos sales con el **paquete ejecutivo firmable** que el patronato espera: comparativo de proveedores con costo total a 12 meses, política de uso institucional v1.0, dashboard de KPIs con baseline, matriz de clasificación de datos y runbook de incidente. Es la diferencia entre "experimento que está bien" y "infraestructura aprobada".

::albatros{titulo="Paquete ejecutivo del Asistente: 5 entregables, 60 minutos, firmable" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si el patronato te diera mañana 30 minutos de junta para decidir si el Asistente continúa, ¿llegas con un PDF que se firma o con un PowerPoint con buenas intenciones? Este taller produce el PDF que se firma.

**Lo que harás (12 pasos).**

1. **Define el contexto institucional (3 min).** Anota en `contexto.md`: tamaño del staff (ej: 50 personas), ecosistema actual (Google Workspace, M365 o mixto), capacidad TI (sin / básica / con equipo dedicado), restricciones de privacidad (LFPDPPP, datos de menores), presupuesto anual aproximado disponible para IA. Estos 5 datos guían todas las decisiones.

2. **Comparativo de proveedores con costo a 12 meses (8 min).** Construye en Google Sheets las **4 opciones** del subtema 10.1 (A Stack OpenAI · B Stack mixto premium · C Stack Microsoft completo · D Stack soberano híbrido) con costo mensual y anual para tu tamaño de staff. Anota fortalezas y debilidades de cada una en una columna adicional. Marca tu **opción recomendada** con argumento de 3 líneas basado en los 5 criterios del subtema 10.1.

3. **Plan de optimización de costos (5 min).** Para la opción elegida, aterriza las 6 técnicas del subtema 10.2: a) modelo correcto por tarea (clasificación → Haiku/Flash; razonamiento → Sonnet/Opus), b) prompt caching, c) Batch API para procesos nocturnos, d) reducción de tokens, e) RAG eficiente, f) híbrido cloud-local. Estima ahorro mensual proyectado al mes 6 vs. mes 1 (ej: $300 → $80).

4. **TCO mensual completo (3 min).** Llena la fórmula: API + suscripciones + hardware amortizado + electricidad + tiempo TI × tarifa + plataformas no-code + servicios externos. Anota en `tco.md` con las cifras concretas de tu institución.

5. **Política de uso de IA v1.0 (10 min).** Adapta la plantilla del subtema 10.3 a tu institución llenando las 9 secciones: alcance, casos permitidos (mínimo 3 ejemplos concretos), casos prohibidos (mínimo 3 ejemplos concretos), datos sensibles, atribución, sanciones, capacitación, comité de gobernanza, contactos. Guárdala como `politica-ia-v1.md` con frontmatter de versión y fecha de próxima revisión.

6. **Matriz dato × sistema (5 min).** Construye la matriz del subtema 10.5 con las **4 niveles de datos** (público, interno, confidencial, restringido) × **6 sistemas** (ChatGPT free, Pro, Claude Pro, Plan Enterprise, Asistente Local, Sin IA) y marca ✓ / ✗ / ✓ con condición. Después, lista los 10 datos institucionales más comunes (nombres de alumnos, calificaciones, planes pedagógicos, brochures, contratos staff, etc.) con su nivel asignado.

7. **Dashboard de KPIs con baseline (8 min).** En una nueva pestaña del Sheet, construye la tabla del subtema 10.4: 4 categorías (adopción, ahorro, calidad, impacto) × 12 KPIs concretos. Para cada KPI: definición, fórmula, baseline pre-IA (mide hoy o estima), objetivo a 6 meses, objetivo a 12 meses, frecuencia de medición, dueño/responsable. Si no tienes baseline, anota "por medir en semana 1".

8. **Reporte trimestral plantilla (4 min).** Crea el template de 1-2 páginas del subtema 10.4 con sus 6 bloques (adopción, ahorro, calidad, impacto, riesgos y ajustes, próximo trimestre). Llénalo con cifras proyectadas a Q2 (al mes 3) para que el patronato vea cómo se verá.

9. **Runbook de incidente IA (5 min).** Documenta los 8 pasos del subtema 10.5 (detección → contención → notificación → comunicación interna → comunicación a afectados → análisis → remediación → post-mortem) con: persona responsable, plazo, herramientas usadas, plantilla de comunicación. Anexa el plan específico para el caso "staff pega datos de calificaciones en ChatGPT free" (frecuente en práctica).

10. **Roadmap a 12 meses (4 min).** Línea de tiempo con hitos por trimestre: Q1 piloto + política firmada + capacitación · Q2 expansión a 70 % staff + 3 KPIs verdes · Q3 producción de contenido especializado (whitepapers, módulos) + servidor MCP custom · Q4 evaluación anual + ajuste de plan v2 + decisión de continuar/escalar/cancelar. Marca dependencias y responsable por hito.

11. **Resumen ejecutivo de 1 página (3 min).** El primer documento que lee el patronato. Estructura: a) qué es el Asistente y qué hace hoy (3 líneas), b) inversión total año 1 (costo concreto), c) ahorro proyectado al mes 12 (con baseline), d) ROI esperado (X×), e) gobernanza activa (política + comité + runbook), f) **decisión que se pide al patronato** (aprobar continuidad, presupuesto, comité). Una página, números visibles, sin jerga.

12. **Empaque y firma (2 min).** Junta los 5 entregables en una carpeta `paquete-patronato-2026-2027/` con el resumen ejecutivo de portada y los anexos numerados. Genera PDF único listo para firmar. Comparte el link al patronato con asunto "Plan a 12 meses del Asistente Institucional Albatros · solicita 30 min de junta".

**Materiales.**
- Google Sheets / Excel para el comparativo, TCO y dashboard de KPIs.
- Editor Markdown (VS Code, Notion, Obsidian) para política, runbook y roadmap.
- Plantillas del manual: política (subtema 10.3), runbook (subtema 10.5), dashboard (subtema 10.4).
- Datos reales: tamaño de staff, ecosistema actual, presupuesto disponible, tarifa promedio del staff (para cálculo de ahorro).
- Generador de PDF (Pandoc, exportador de Notion, o Word/Docs → PDF).

**Entregable.**
1. **`comparativo-proveedores.xlsx`** — 4 opciones con costo mensual/anual + opción recomendada con argumento.
2. **`tco.md`** — TCO mensual completo con todas las líneas del Asistente.
3. **`politica-ia-v1.md`** — política institucional con las 9 secciones, versión y fecha.
4. **`matriz-datos-sistemas.md`** — matriz 4×6 + lista de 10 datos clasificados.
5. **`dashboard-kpis.xlsx`** — 12 KPIs con baseline, objetivos y dueño.
6. **`reporte-trimestral-template.md`** — template + ejemplo proyectado al Q2.
7. **`runbook-incidente.md`** — los 8 pasos + plantilla de comunicación + caso específico.
8. **`roadmap-12-meses.md`** — línea de tiempo Q1–Q4 con hitos y dependencias.
9. **`resumen-ejecutivo.pdf`** — 1 página firmable con los 6 bloques.
10. **Carpeta `paquete-patronato-2026-2027/`** — todos los anteriores + portada + PDF único listo para firmar.

**Rúbrica corta.**

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Comparativo de proveedores | 1 opción genérica | 4 opciones con cifras | 4 opciones + recomendada + 5 criterios + ahorro proyectado |
| Política institucional | borrador parcial | 6 secciones | 9 secciones con ejemplos concretos + versión + comité asignado |
| Matriz de datos | sin matriz | matriz 4×6 | matriz + 10 datos clasificados + controles técnicos por nivel |
| Dashboard de KPIs | métricas de vanidad | 6 KPIs con baseline | 12 KPIs con baseline + objetivos a 6 y 12 meses + dueño |
| Runbook de incidente | sin documentar | 5 pasos | 8 pasos + plantilla de comunicación + caso real ensayado |
| Roadmap | sin fechas | trimestral | trimestral con dependencias y responsables |
| Resumen ejecutivo | múltiples páginas | 1 página sin números | 1 página con TCO, ROI, gobernanza y decisión solicitada |

**Tip Albatros.** El paquete que entregas no es para impresionar al patronato — es para **transferirles riesgo controlado**. Cuando un patronato firma este documento, está aprobando un sistema con métricas, política y runbook; ya no es "el experimento de Federico". Esa transferencia es la última pieza del manual. A partir de aquí tu trabajo deja de ser convencer y empieza a ser **operar la maquinaria que tú diseñaste**. El siguiente paso natural, si el patronato firma, es la siguiente generación del Asistente: nuevos servidores MCP, nuevos casos de uso, nuevos módulos de contenido. Pero todo se sostiene sobre este paquete. Sin él, todo lo anterior se cae.
::/albatros
