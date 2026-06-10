---
unidad: 10
seccion: practica-resuelta
paginas_objetivo: 2
---

## Práctica resuelta — Unidad 10

::practica{titulo="Construir el Plan a 12 meses del Asistente Institucional Albatros listo para patronato"}
**Problema.** Producir el documento de **plan a 12 meses del Asistente Institucional Albatros** que el patronato apruebe, con presupuesto, gobernanza, KPIs, política, plan de salida y firmas. Tiempo: 2 semanas.

**Paso 1 — Datos disponibles.**
- Resultados de piloto (3-6 meses): adopción, satisfacción, ahorros estimados.
- Stack actual: ChatGPT Team, Claude Pro (5), n8n self-hosted, Open WebUI con Ollama, MCP.
- Equipo: tú + coordinadora académica + TI + dirección.
- Patronato sesiona en 14 días.

**Paso 2 — Estrategia.**
1. Comparativo de planes (10.1) → recomendación de proveedor.
2. Cálculo de TCO + ahorros (10.2 + 10.4) → ROI defendible.
3. Política de uso (10.3) → cumplimiento.
4. KPIs (10.4) → tablero ejecutivo.
5. Confidencialidad (10.5) → matriz dato × sistema.
6. Roadmap 12 meses → hitos trimestrales.
7. Plan de salida → resiliencia ante cancelación.

**Paso 3 — Comparativo y recomendación de proveedor (1 día).**

Para 50 staff:
- Opción A (todo cloud premium): $54k/año.
- Opción B (mixto premium): $25k/año.
- **Opción C (híbrido cloud-local recomendada):** Stack actual continúa. ChatGPT Team para 30 staff que vive en mainstream + Claude Pro 8 staff técnicos + Open WebUI gratis para 50 staff masivo.
  - Cloud anual: $13 200.
  - Servidor local amortizado: $4 000 (3 años) = $1 333/año.
  - Mantenimiento TI: 5h/mes × $300/h = $18 000/año.
  - **Total: $32 533/año.**

**Paso 4 — KPIs proyectados (medio día).**

Adopción mes 12: 40 staff activos, 70 % casos auto-resueltos.
Ahorro mensual mes 12: 200 horas × $300 promedio = $60 000.
TCO mensual mes 12: $2 700.
**ROI: 22×.**

**Paso 5 — Política de uso v1.0 (1 día).**

Doc de 2 páginas firmable con secciones del 10.3. Validado por legal externo (asesor de la institución).

**Paso 6 — Matriz dato × sistema (medio día).**

Visual del 10.5 adaptado a la institución específica. Validado por TI y dirección.

**Paso 7 — Roadmap trimestral (1 día).**

```
Q1 (mes 1-3):
- Adopción cloud + local 30 staff.
- 3 workflows producción.
- 1 curso digital.
- 1 incidente menor esperado, mitigado.

Q2 (mes 4-6):
- Adopción 40 staff.
- 5 workflows.
- 2 cursos.
- Comité de gobernanza con 2 reuniones.
- KPI: 60% completion satisfacción ≥ 4.0.

Q3 (mes 7-9):
- 50 staff.
- 8 workflows.
- 3 cursos.
- Auditoría externa de seguridad.

Q4 (mes 10-12):
- Optimización de costos.
- Reporte anual al patronato.
- Plan v2.0 con expansión a alumnos.
```

**Paso 8 — Plan de salida (medio día).**

Si patronato cancela proyecto en mes 6 o 12:
- Datos en sistemas locales: respaldo institucional, exportable.
- Prompts versionados: en repo institucional, exportables.
- Workflows: JSONs en Git.
- Modelos cloud: cierre de cuentas, exportar logs antes.
- Capacitación al staff: workshops de 2h sobre uso responsable individual.
- TCO de cierre: $2 000.

**Paso 9 — Documento final + firmas (3 días).**

Documento de 6-8 páginas con:
- Executive summary (½ pp).
- Recomendaciones (1 pp).
- TCO y ROI (1 pp).
- Roadmap (1 pp).
- Política y gobernanza (1 pp).
- Riesgos y plan de salida (1 pp).
- Firmas: dirección, coordinadora académica, TI, asesor legal.

**Paso 10 — Presentación al patronato (1 sesión).**

20 minutos: 10 presentación + 10 Q&A. Materiales: el documento + dashboard ejecutivo (Artifact React).

**Respuesta.** Plan a 12 meses entregable, presupuestado, gobernado y firmable. Patronato lo aprobó con 1 enmienda menor (ampliar capacitación obligatoria a 4 horas/año). Asistente Institucional Albatros pasa de proyecto piloto a infraestructura permanente.

**Verificación final.** A 3 meses post-aprobación: roadmap Q1 cumplido. ROI real medido vs proyectado: 22× (vs 21× proyectado). Plan vivo con revisión trimestral.

**Lección.** Las 5 técnicas de la unidad (planes, costos, política, métricas, confidencialidad) **no son opcionales** para llevar un proyecto IA a infraestructura permanente. Sin ellas, el piloto exitoso muere en mes 6. Con ellas, se vuelve parte del sistema institucional como cualquier otro servicio crítico.
::/practica
