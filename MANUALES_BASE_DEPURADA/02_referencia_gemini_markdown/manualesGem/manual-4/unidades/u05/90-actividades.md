---
unidad: 5
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 05

::act-mcq{titulo="Repaso conceptual"}
1. Para una institución 100 % Microsoft 365 con compliance estricto, la mejor opción es:
   - [ ] n8n self-hosted
   - [ ] Make
   - [ ] Zapier
   - [x] Power Automate

2. El patrón **Idempotency** previene principalmente:
   - [ ] Fallos de API
   - [x] Procesamiento duplicado del mismo evento
   - [ ] Latencia alta
   - [ ] Costo de tokens

3. Un workflow con Schedule cada minuto suele ser **peor** que uno con Webhook porque:
   - [x] Consume operaciones aunque no haya cambios
   - [ ] Es más complejo de configurar
   - [ ] No soporta retry
   - [ ] No funciona en n8n

4. Para iterar sobre 50 alumnos en un escenario complejo, la plataforma más elegante es:
   - [ ] Zapier
   - [x] Make (Iterator/Aggregator nativos)
   - [ ] Power Automate
   - [ ] cualquiera

5. El patrón "Approval loop" es esencial cuando:
   - [ ] El workflow es lento
   - [x] La acción es irreversible o de alta consecuencia
   - [ ] Se necesita logging
   - [ ] Hay rate limit
::/act-mcq

::act-table{titulo="Completa la tabla — plataforma por caso institucional"}
| Caso del Asistente | Plataforma recomendada | Por qué |
|---|---|---|
| Stack 100 % M365 con compliance |  |  |
| Self-host por privacidad |  |  |
| Equipo no-técnico, mainstream apps |  |  |
| Workflow con muchas ramas y mergers |  |  |
| Volumen alto y constante (10k tasks/mes) |  |  |
| Integración con apps obscuras |  |  |
::/act-table

::act-match{titulo="Relaciona el patrón con su problema"}
| Patrón | Resuelve |
|---|---|
| 1. Router | a) Llamadas API que pueden fallar transitoriamente |
| 2. Fan-out / Fan-in | b) Acciones irreversibles que requieren validación humana |
| 3. Retry con backoff | c) Procesamiento duplicado del mismo evento |
| 4. Idempotency | d) Entradas heterogéneas que requieren rutas distintas |
| 5. Approval loop | e) Múltiples acciones independientes a ejecutar en paralelo |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Un Webhook sin autenticación es seguro porque la URL es secreta. ( ) ____________________________________________

2. Make es siempre más caro que Zapier. ( ) ____________________________________________

3. Notion API tiene rate limit, así que tu workflow debe manejarlo. ( ) ____________________________________________

4. Si tu workflow pasa rate limit (429), debes esperar y reintentar con backoff. ( ) ____________________________________________

5. Una credencial OAuth con permiso de admin de toda la org es la mejor práctica. ( ) ____________________________________________
::/act-tf

::act-order{titulo="Ordena los pasos para llevar un workflow a producción"}
[ ] Documentar y compartir con el equipo
[ ] Diseñar el workflow visualmente con los nodos
[ ] Probar con casos reales y casos de error
[ ] Configurar credenciales en gestor central
[ ] Activar workflow y monitorear primeras 50 ejecuciones
[ ] Aplicar patrones (idempotency, retry, fan-out)
[ ] Definir trigger (webhook / schedule / polling)
[ ] Versionar (export JSON, commit Git)
::/act-order

::albatros{titulo="Construye y despliega tu primer workflow institucional con 5 patrones aplicados" tipo="taller" tiempo="3 h"}
**Pregunta detonadora.** Si una sola persona de tu institución gana 10 horas semanales con un workflow, ¿cuántas personas más en tu organización podrían ganar lo mismo si replicas el patrón?

**Lo que harás.**
1. Identifica un proceso real de tu institución que ocupe >1 hora semanal manual y se pueda automatizar.
2. Elige plataforma según los criterios de la unidad (n8n, Make, Zapier o Power Automate).
3. Diseña el workflow aplicando **al menos 3** de los 5 patrones (router, fan-out, retry, idempotency, approval).
4. Construye con webhooks o triggers apropiados.
5. Integra con al menos 2 servicios externos (Notion, Airtable, Sheets, Gmail, Slack, etc.).
6. Pruébalo con 5 casos reales y 2 casos de error inducido.
7. Versiona (export JSON + commit Git + CHANGELOG).
8. Comparte con el equipo y mide ahorro de tiempo a 1 semana.

**Materiales.** Cuenta de plataforma elegida, credenciales de las apps a integrar, repo Git, 3 horas.

**Entregable.**
- JSON exportado del workflow.
- README con: propósito, trigger, patrones aplicados, riesgos, runbook.
- Reporte de pruebas (5 casos + 2 errores).
- Métrica de ahorro a 1 semana.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Diseño del workflow | lineal sin patrones | 1-2 patrones | 3+ patrones aplicados |
| Pruebas | 1 caso | 3-5 casos | 5+ casos + chaos test |
| Manejo de errores | sin retry | retry básico | retry + fallback + alerta |
| Documentación | mínima | README | runbook completo |
| Versionado | sin commit | export + commit | con CHANGELOG y tag |
| Adopción | privado | mostrado al equipo | adoptado con métricas |
::/albatros

::act-fill{titulo="Anatomía de un webhook autenticado"}
Un webhook seguro lleva siempre:

- Método _____________ (no GET para acciones).
- Header `Authorization: ____________ <token>`.
- Validación del _____________ contra un schema antes de procesar.
- Respuesta _____________ rápida para no bloquear al emisor.
- _____________ key calculado del body para evitar duplicados.
::/act-fill

::act-mindmap{titulo="Tu suite de workflows institucionales" centro="WORKFLOWS ALBATROS v1" nodos_primarios=6 nodos_secundarios=12}
Las 6 ramas: (1) workflows en producción y su trigger, (2) integraciones activas, (3) patrones aplicados (idempotency, retry, router, fan-out, approval), (4) métricas semanales, (5) runbooks documentados, (6) próximas mejoras. Datos reales, no abstractos.
::/act-mindmap

::act-label{titulo="Etiqueta el flujo de un workflow institucional"}
> Marca: a) la estación que evita duplicados · b) la estación que protege de rate limits · c) la estación que detiene el workflow si la confianza es baja · d) la estación con mayor riesgo de timeout en producción.
::/act-label


::visual{tipo="diagrama-flujo" descripcion="Diagrama de flujo de un workflow institucional con estaciones numeradas: webhook entrante, idempotency check, clasificación IA, router, fan-out a 3 ramas paralelas (Notion, Gmail, Calendar) cada una con retry, fan-in, notificación Slack, respond webhook. Espacio para que el alumno escriba el patrón aplicado en cada estación y el modo de falla más común." paginas="0.5" src="../manualesGem/assets/visuales/manual-4/u05/90-actividades-v01.svg"}
::act-case{titulo="Caso de diseño — re-arquitectura de un workflow lento" lineas=14}
Tu workflow `inscripcion-v1.0` tarda 24 segundos en promedio porque las acciones (Notion, Gmail, Calendar) corren **en serie**. La coordinadora se queja porque el padre espera 24 s sin respuesta. Re-arquitéctalo aplicando: (1) respuesta inmediata 200 al webhook tras idempotency check, (2) procesamiento asíncrono con fan-out, (3) notificación final cuando todas las ramas terminan. Diseña el nuevo flujo y estima latencia percibida por el padre.
::/act-case

::albatros{titulo="Reto — reemplazas un workflow Zapier por uno equivalente en n8n" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** Tu institución paga Zapier por un workflow simple. ¿Cuánto ahorras al migrar a n8n self-hosted, y qué pierdes?

**Lo que harás.**
1. Toma un workflow real de Zapier (tuyo o uno típico: nuevo formulario → email + Sheet).
2. Replícalo en n8n cloud free trial.
3. Aplica al menos un patrón nuevo (idempotency o retry) que Zapier no tenía.
4. Mide latencia, costo mensual y mantenibilidad de ambos.
5. Decide si migras o no, con números.

**Entregable.** Tabla comparativa Zapier vs n8n + decisión justificada en 5 líneas.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Replica en n8n | parcial | funciona | funciona + patrón nuevo |
| Métricas | una | 3 dimensiones | 4 dimensiones con costo a 12 meses |
| Decisión | preferencia | con dato | con plan de migración o defensa de Zapier |
::/albatros
