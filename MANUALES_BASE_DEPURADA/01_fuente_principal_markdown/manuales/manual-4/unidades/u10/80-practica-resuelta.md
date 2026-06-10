---
unidad: 10
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Unidad 10

::practica{titulo="Construir el Plan a 12 meses del Asistente Institucional Albatros listo para patronato"}
**Problema.** 
- Producir el plan a 12 meses del Asistente Institucional Albatros.
- Debe incluir presupuesto, gobernanza, KPIs, política y plan de salida.
- Requiere firmas y aprobación del patronato en 2 semanas.

**Paso 1 — Datos disponibles.**
- Resultados del piloto (3-6 meses): adopción, satisfacción, ahorros.
- Stack actual: ChatGPT Team, Claude Pro (5), n8n self-hosted, Open WebUI.
- Equipo: tú, coordinadora académica, TI y dirección.
- Patronato sesiona en 14 días.

**Paso 2 — Estrategia.**
- Comparativo de planes (10.1) → recomendación de proveedor.
- Cálculo de TCO + ahorros (10.2 + 10.4) → ROI defendible.
- Política de uso (10.3) → cumplimiento.
- KPIs (10.4) → tablero ejecutivo.
- Confidencialidad (10.5) → matriz dato × sistema.
- Roadmap 12 meses → hitos trimestrales.
- Plan de salida → resiliencia ante cancelación.

::interioriza
Imagina que presentas un proyecto arquitectónico a un comité de inversión. 
No solo muestras los planos (stack técnico), sino el costo de los materiales (TCO), 
el mantenimiento (Gobernanza) y qué pasa si la obra se detiene (Plan de salida).
::

**Paso 3 — Comparativo y recomendación (1 día).**
- Para 50 staff:
- Opción A (todo cloud premium): $54k/año.
- Opción B (mixto premium): $25k/año.
- **Opción C (híbrido cloud-local recomendada):** Stack actual continúa.
  - ChatGPT Team para 30 staff (mainstream).
  - Claude Pro para 8 staff técnicos.
  - Open WebUI gratis para 50 staff masivo.
- Costos Opción C:
  - Cloud anual: $13 200.
  - Servidor local amortizado: $1 333/año (3 años).
  - Mantenimiento TI: $18 000/año (5h/mes × $300/h).
  - **Total: $32 533/año.**

**Paso 4 — KPIs proyectados (medio día).**
- Adopción mes 12: 40 staff activos.
- Casos auto-resueltos: 70 %.
- Ahorro mensual: $60 000 (200 horas × $300 promedio).
- TCO mensual mes 12: $2 700.
- **ROI proyectado: 22×.**

**Paso 5 — Política de uso v1.0 (1 día).**
- Documento de 2 páginas firmable.
- Incluye secciones del 10.3.
- Validado por asesor legal externo de la institución.

**Paso 6 — Matriz dato × sistema (medio día).**
- Visual del 10.5 adaptado a la institución.
- Validado por los departamentos de TI y dirección.

**Paso 7 — Roadmap trimestral (1 día).**
- **Q1 (mes 1-3):** Adopción cloud + local 30 staff. 3 workflows. 1 curso.
- **Q2 (mes 4-6):** Adopción 40 staff. 5 workflows. 2 cursos. KPI: 60% completion.
- **Q3 (mes 7-9):** 50 staff. 8 workflows. 3 cursos. Auditoría de seguridad.
- **Q4 (mes 10-12):** Optimización de costos. Reporte anual. Expansión a alumnos.

**Paso 8 — Plan de salida (medio día).**
- Si se cancela en mes 6 o 12:
  - Datos locales: respaldo institucional, exportable.
  - Prompts y Workflows: versionados en repo institucional y Git.
  - Modelos cloud: exportar logs antes del cierre de cuentas.
  - Capacitación: workshops sobre uso responsable individual.
  - TCO de cierre: $2 000.

**Paso 9 — Documento final + firmas (3 días).**
- Extensión: 6-8 páginas.
- Secciones: Resumen ejecutivo, recomendaciones, TCO, ROI, roadmap, política, riesgos.
- Firmas requeridas: dirección, académica, TI y legal.

**Paso 10 — Presentación al patronato (1 sesión).**
- Tiempo: 20 minutos (10 presentación + 10 Q&A).
- Entregables: Documento físico + dashboard ejecutivo (Artifact React).

::pausa{}
1. ¿Por qué es vital incluir un "Plan de salida" al presentar el proyecto ante el patronato?
2. ¿Qué elementos justifican el ROI de 22× proyectado para el mes 12?
::

**Respuesta y Resultados.** 
- El plan fue aprobado con una enmienda menor.
- El asistente pasa de proyecto piloto a infraestructura permanente.
- A 3 meses: roadmap Q1 cumplido y ROI real medido en 22×.

**Lección.** 
- Planes, costos, políticas, métricas y confidencialidad son **obligatorios**.
- Sin esto, un piloto exitoso muere al mes 6.
- Con esto, la IA se vuelve un servicio crítico institucional.
::/practica
