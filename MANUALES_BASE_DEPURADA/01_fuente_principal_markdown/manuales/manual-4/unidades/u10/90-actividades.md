---
unidad: 10
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 10

::act-mcq{titulo="Repaso conceptual"}
1. La técnica de optimización con mayor impacto en costos para Asistente con system prompt largo es:
   - [ ] Modelo más barato
   - [x] Prompt caching
   - [ ] Batch API
   - [ ] Reducir max_tokens

2. Para una institución con datos confidenciales de menores, el sistema NO autorizado es:
   - [ ] Asistente local Ollama
   - [ ] Plan Enterprise con DPA
   - [x] ChatGPT free
   - [ ] Open WebUI con auth

3. La métrica MÁS útil para reportar al patronato sobre adopción es:
   - [ ] Conversaciones totales
   - [x] % de casos auto-resueltos sin escalación humana
   - [ ] Cantidad de prompts
   - [ ] Tokens consumidos

4. Una política de uso de IA "demasiado restrictiva" suele:
   - [x] Ser ignorada y empujar uso oculto sin guardrails
   - [ ] Garantizar cumplimiento total
   - [ ] Eliminar incidentes
   - [ ] Reducir costos

5. El plan de salida del proyecto es importante porque:
   - [ ] Aumenta optimismo
   - [ ] Reduce costos
   - [x] Demuestra resiliencia y respeta decisiones futuras del patronato
   - [ ] Es opcional
::/act-mcq

::act-table{titulo="Completa la tabla — caso institucional → decisión"}
| Caso | Recomendación | Justificación |
|---|---|---|
| 50 staff con M365 + datos confidenciales |  |  |
| 20 staff técnicos en Google Workspace |  |  |
| Volumen alto (50M tokens/mes) |  |  |
| Datos restringidos (contratos, NDAs) |  |  |
| Presupuesto cero, capacidad TI |  |  |
| Adopción rápida a 100 personas |  |  |
::/act-table

::act-match{titulo="Relaciona técnica de optimización con caso ideal"}
| Técnica | Caso ideal |
|---|---|
| 1. Prompt caching | a) Procesar 1000 emails clasificación nocturna |
| 2. Batch API | b) Reducir tokens del system prompt enviado en cada llamada |
| 3. Modelo correcto por tarea | c) Usar Haiku para clasificación, Opus para razonamiento |
| 4. RAG eficiente | d) Pasar 5 chunks al LLM en vez de 50 |
| 5. Local soberano | e) Volumen alto, datos sensibles |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. ChatGPT Enterprise + DPA es suficiente para procesar datos restringidos. ( ) ____________________________________________

2. El ROI de un Asistente Institucional puede medirse solo con horas humanas ahorradas. ( ) ____________________________________________

3. Una política de uso sin sanciones es equivalente a no tener política. ( ) ____________________________________________

4. El batch API funciona bien para chats en vivo con padres de familia. ( ) ____________________________________________

5. Tener plan de salida del proyecto demuestra falta de compromiso. ( ) ____________________________________________
::/act-tf

::act-case{titulo="Caso para resolver — el patronato cuestiona el presupuesto" lineas=15}
Tu plan a 12 meses fue presentado al patronato.
La presidenta pregunta: "Veo que el TCO sube 40% del Q1 al Q4. ¿Por qué? ¿Estamos perdiendo control?".
Tienes 5 minutos para responder en vivo.

Diseña tu respuesta en 5 actos:
- (1) Reconoces la observación.
- (2) Explicas que el aumento es por crecimiento de adopción, no descontrol.
- (3) Muestras la métrica de TCO/usuario que se mantiene estable.
- (4) Presentas 3 técnicas de optimización para Q3-Q4.
- (5) Ofreces revisión mensual con el comité.

Mínimo 12 líneas.
::/act-case

::albatros{titulo="Construye el Plan a 12 meses de tu proyecto IA con presupuesto y gobernanza" tipo="taller" tiempo="6 h"}
**Pregunta detonadora.** Si pudieras presentar a tu patronato/dirección un plan IA tan sólido que **no tuvieran objeciones razonables**, ¿qué incluiría?

**Lo que harás.**
1. Recolecta resultados del piloto IA en tu institución.
   - Si no tienes piloto, usa datos proyectados.
2. Aplica las 5 técnicas de la unidad:
   - **10.1**: Recomendación de proveedores con cálculo concreto.
   - **10.2**: TCO mensual + 3 técnicas de optimización con ahorros.
   - **10.3**: Política de uso v1.0 (2 páginas).
   - **10.4**: 8 KPIs con baseline y objetivos a 12 meses.
   - **10.5**: Matriz dato × sistema personalizada.
3. Define un Roadmap trimestral.
   - Incluye 4 hitos por trimestre.
4. Elabora un plan de salida.
   - Escenarios de cancelación mes 6 y mes 12.
5. Crea un documento final de 6-8 páginas.
   - Listo para recabar firmas.
6. Prepara una presentación de 20 minutos.
   - Incluye slides y dashboard ejecutivo.

::interioriza
**El Plan de Salida como un Seguro**
Tener un plan de salida no significa buscar cancelar el proyecto.
Es como un seguro: no planeas usarlo, pero muestra madurez.
El patronato verá que proteges a la institución ante imprevistos.
::/interioriza

::pausa{}
1. ¿Por qué un TCO global alto es buena señal si el TCO/usuario es estable?
2. ¿Qué pasa si dependes de un proveedor sin plan de salida y triplica precios?
::/pausa

**Materiales.**
- Datos del piloto.
- Software de presentaciones.
- 6 horas de dedicación.

**Entregable.**
- Plan a 12 meses (6-8 páginas).
- Política de uso (2 páginas).
- Slides de presentación (10-15 slides).
- Dashboard ejecutivo (Artifact U3 o Looker Studio).
- Plan de salida documentado.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Comparativo proveedores | sin justificar | con cifras | con escenarios y ROI |
| TCO + optimización | sin medir | medido | con técnicas aplicadas y ahorros proyectados |
| Política de uso | ausente | 1 página | 2 páginas con casos y sanciones |
| KPIs | <5 | 5-7 con baseline | 8+ con objetivos por trimestre |
| Confidencialidad | informal | matriz general | matriz adaptada con runbook |
| Roadmap | trimestral genérico | con hitos específicos | con riesgos identificados |
| Plan de salida | inexistente | mencionado | escenarios documentados |
| Presentación | borrador | clara | impactante con dashboard en vivo |
::/albatros
