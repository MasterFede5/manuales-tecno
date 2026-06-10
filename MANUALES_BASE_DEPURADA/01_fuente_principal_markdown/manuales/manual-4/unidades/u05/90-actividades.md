---
unidad: 5
seccion: actividades
paginas_objetivo: 2
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
**Pregunta detonadora.** 
Si una sola persona de tu institución gana 10 horas semanales con un workflow...
¿Cuántas personas más podrían ganar lo mismo si replicas el patrón?

**Lo que harás.**
- Identifica un proceso real (>1 hora semanal manual) a automatizar.
- Elige plataforma (n8n, Make, Zapier o Power Automate).
- Diseña el workflow aplicando **al menos 3** patrones.
- Construye con webhooks o triggers apropiados.
- Integra con al menos 2 servicios externos.
- Pruébalo con 5 casos reales y 2 casos de error.
- Versiona (export JSON + commit Git + CHANGELOG).
- Comparte con el equipo y mide ahorro.

**Materiales.** 
- Cuenta de plataforma elegida y credenciales.
- Repositorio Git y 3 horas libres.

**Entregable.**
- JSON exportado del workflow.
- README con propósito, trigger, patrones, riesgos y runbook.
- Reporte de pruebas y métrica de ahorro a 1 semana.

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
- **Ramas principales:**
  - Workflows en producción y su trigger.
  - Integraciones activas.
  - Patrones aplicados (idempotency, retry, router, etc.).
  - Métricas semanales.
  - Runbooks documentados.
  - Próximas mejoras (datos reales).
::/act-mindmap

::act-label{titulo="Etiqueta el flujo de un workflow institucional"}
::visual{tipo="diagrama-flujo" descripcion="Diagrama de flujo de un workflow institucional con estaciones numeradas: webhook entrante, idempotency check, clasificación IA, router, fan-out a 3 ramas paralelas (Notion, Gmail, Calendar) cada una con retry, fan-in, notificación Slack, respond webhook. Espacio para que el alumno escriba el patrón aplicado en cada estación y el modo de falla más común." paginas=0.5}
> Marca: 
> a) La estación que evita duplicados. 
> b) La estación que protege de rate limits. 
> c) La estación que detiene el workflow (confianza baja). 
> d) La estación con mayor riesgo de timeout.
::/act-label

::act-case{titulo="Caso de diseño — re-arquitectura de un workflow lento" lineas=14}
Tu workflow `inscripcion-v1.0` tarda 24 segundos en promedio.
Las acciones (Notion, Gmail, Calendar) corren **en serie**.
El padre espera 24 s sin respuesta y se queja.

**Re-arquitéctalo aplicando:**
- Respuesta inmediata 200 al webhook tras idempotency check.
- Procesamiento asíncrono con fan-out.
- Notificación final cuando todas las ramas terminan.
- **Diseña** el nuevo flujo y estima la latencia percibida.
::/act-case

::albatros{titulo="Reto — reemplazas un workflow Zapier por uno equivalente en n8n" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** 
Tu institución paga Zapier por un workflow simple. 
¿Cuánto ahorras al migrar a n8n self-hosted, y qué pierdes?

**Lo que harás.**
- Toma un workflow real de Zapier.
- Replícalo en n8n cloud free trial.
- Aplica al menos un patrón nuevo (idempotency o retry).
- Mide latencia, costo mensual y mantenibilidad.
- Decide si migras o no, justificando con números.

**Entregable.** 
Tabla comparativa Zapier vs n8n + decisión en 5 líneas.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Replica en n8n | parcial | funciona | funciona + patrón nuevo |
| Métricas | una | 3 dimensiones | 4 dimensiones con costo a 12 meses |
| Decisión | preference | con dato | con plan o defensa de Zapier |
::/albatros
