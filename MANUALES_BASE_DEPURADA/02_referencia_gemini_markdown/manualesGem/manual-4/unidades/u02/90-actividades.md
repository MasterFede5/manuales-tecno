---
unidad: 2
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 02

::act-mcq{titulo="Repaso conceptual"}
1. La sección más subestimada de un PRD es:
   - [ ] Métricas de éxito
   - [x] No-objetivos
   - [ ] Riesgos
   - [ ] Calendario

2. Un criterio de aceptación que dice "el sistema debe ser robusto" es:
   - [ ] Aceptable porque deja flexibilidad
   - [x] Defectuoso porque no es verificable por un tercero
   - [ ] Aceptable si el equipo entiende
   - [ ] Aceptable si lo escribió un senior

3. La capa que más errores previene en producción suele ser:
   - [ ] Estratégica
   - [ ] Funcional
   - [ ] Técnica
   - [x] Operativa

4. En un trade-off "calidad vs costo" para un clasificador, el patrón híbrido (modelo barato escalando a uno caro si baja confianza) optimiza:
   - [ ] Solo costo
   - [ ] Solo calidad
   - [x] Punto medio según umbral calibrado
   - [ ] Latencia exclusivamente

5. Spec-driven prompting busca:
   - [ ] Que la IA escriba la spec sola
   - [x] Que prompt y spec sean una sola fuente de verdad
   - [ ] Reemplazar la documentación
   - [ ] Eliminar revisiones humanas
::/act-mcq

::act-table{titulo="Completa la tabla — capas y artefactos"}
| Capa | Audiencia natural | Artefacto principal | Riesgo si se omite |
|---|---|---|---|
| Estratégica |  |  |  |
| Funcional |  |  |  |
| Técnica |  |  |  |
| Operativa |  |  |  |
::/act-table

::act-match{titulo="Relaciona la pieza con su propósito"}
| Pieza | Propósito |
|---|---|
| 1. PRD | a) Captura una decisión de trade-off con su contexto |
| 2. Brief | b) Documento de visión y métricas de un producto |
| 3. Scope | c) Lo que sí y no entra en una entrega concreta |
| 4. ADR | d) Encarga un módulo o feature |
| 5. DoD | e) Lista de condiciones para declarar "hecho" cualquier entrega |
| 6. Criterios de aceptación | f) Verificables por un tercero, específicos del módulo |
::/act-match

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Un PRD de 3 páginas siempre es mejor que uno de 1 página. ( ) ____________________________________________

2. Los criterios de aceptación pueden ser revisados por el autor del módulo. ( ) ____________________________________________

3. Un proyecto puede saltarse el plan de rollback si los tests pasan. ( ) ____________________________________________

4. El cono de incertidumbre se cierra solo, sin trabajo del equipo. ( ) ____________________________________________

5. Spec-driven prompting es esencial desde el primer día del proyecto. ( ) ____________________________________________
::/act-tf

::act-case{titulo="Caso para resolver — la junta del viernes" lineas=12}
Tu director llega a la junta y propone agregar 4 features más al Asistente sin mover la fecha de entrega. La coordinadora académica calla; el desarrollador hace cara de horror. Tienes el PRD v1.0 impreso en la mano.

Diseña tu intervención en 4 actos: (1) cómo abres usando el PRD; (2) qué le muestras del cono de incertidumbre y trade-offs; (3) qué propones concretamente (3 escenarios A/B/C); (4) cómo cierras pidiendo decisión documentada en ADR. Mínimo 10 líneas en total.
::/act-case

::albatros{titulo="Tu primer PRD asistido por IA + 3 briefs + 1 ADR" tipo="taller" tiempo="3 h"}
**Pregunta detonadora.** Si no escribes el PRD, alguien lo escribirá por ti — o peor, no se escribirá y construirán cualquier cosa. ¿Cómo te garantizas que la conversación quede capturada?

**Lo que harás.**
1. Elige un proyecto IA real que estés iniciando o que comenzarás en 30 días. Si no tienes uno, usa "Asistente de tu materia favorita".
2. Aplica el meta-PRD del subtema 2.1 con tus datos reales.
3. Refina con stress-test de 3 ángulos (escéptico técnico, financiero, riesgo no listado).
4. Redacta 3 briefs (subtema 2.2) para los 3 primeros módulos.
5. Documenta 1 ADR del trade-off principal del proyecto.
6. Adopta el DoD canónico (subtema 2.3) y agrégale 1 ítem propio.
7. Asigna IDs por capa S-/F-/T-/O- a cada item del PRD.
8. Comparte el conjunto con al menos una persona y pide que te haga 5 preguntas.

**Materiales.** Cuenta gratis de un LLM, repo (Git o Notion), 3 horas.

**Entregable.** Carpeta o repo con: PRD v1.0 (1 pp), 3 briefs, 1 ADR, DoD personalizado, mapa de IDs.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| PRD en 1 pp | excede | cabe pero abigarrado | cabe y es legible |
| Métricas verificables | "satisfactorio" | parcial | numéricas y con cómo medir |
| No-objetivos | ausentes | 1-2 | 4+ explícitos |
| Briefs consistentes con PRD | divergen | aceptable | trazables con IDs |
| ADR documentado | informal | con contexto | con consecuencias y revisión futura |
| DoD personalizado | adoptado tal cual | con 1 ítem propio | con 2+ ítems institucionales |
::/albatros

::act-order{titulo="Ordena los pasos de un PRD asistido por IA"}
[ ] Validación social con stakeholder no técnico
[ ] Stress-test desde 3 ángulos (técnico, financiero, riesgos)
[ ] Recolección de dolor con 2 stakeholders
[ ] Asignación de IDs por capa (S/F/T/O)
[ ] Borrador v0.5 con meta-prompt patrón
[ ] Refinamiento incorporando críticas
[ ] Cierre v1.0 firmable
::/act-order

::act-fill{titulo="Completa los IDs de trazabilidad"}
La objetivo *"reducir 60 % la carga del staff administrativo"* lleva ID ____-001 (capa _____________).
El módulo *"clasificador de solicitudes"* lleva ID ____-014 (capa _____________).
La conexión *"ASGI con base de matrícula"* lleva ID ____-027 (capa _____________).
La rotación *"on-call lunes-jueves coordinadora, viernes tú"* lleva ID ____-003 (capa _____________).
::/act-fill

::act-mindmap{titulo="Mapa mental del PRD del Asistente" centro="PRD ASISTENTE ALBATROS v1.0" nodos_primarios=8 nodos_secundarios=16}
Llena las 8 ramas con: (1) visión y problema, (2) objetivos S/F/T/O, (3) no-objetivos, (4) métricas, (5) usuarios y dolores, (6) alcance v1, (7) riesgos y mitigaciones, (8) plan de rollback y revisión. En cada nodo secundario escribe un dato concreto de tu propia institución, no genérico.
::/act-mindmap

::act-label{titulo="Etiqueta el cono de incertidumbre del proyecto"}
> Marca: a) la fase con mayor riesgo de sobrecompromiso · b) la fase donde por primera vez puedes prometer fecha · c) la fase donde el costo de cambio se vuelve alto · d) la fase típica donde mueren los proyectos de IA por mala gestión de incertidumbre.
::/act-label


::visual{tipo="grafica" descripcion="Gráfica del cono de incertidumbre con eje X (fases del proyecto: idea, discovery, PRD, briefs, smoke, golden) y eje Y (rango ±% estimación). Cinco bandas que se van cerrando de ±300 % a ±10 %. Espacio en blanco para etiquetar cada fase con la acción que la cierra y el artefacto entregable de esa fase." paginas="0.5" src="../manualesGem/assets/visuales/manual-4/u02/90-actividades-v01.svg"}
::albatros{titulo="Reto — convences a tu director de un trade-off impopular" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** Tu director firmó "queremos GPT-5 para todo, calidad máxima". Tú calculaste que con Haiku + escalación condicional ahorras $2 100/año sin perder calidad significativa. ¿Cómo lo convences sin perder la silla?

**Lo que harás.**
1. Construye un mini-experimento: 30 inputs reales, 3 modelos (Haiku, Sonnet, Opus), 3 criterios.
2. Mide calidad (rúbrica humana 1-5), latencia y costo.
3. Genera tabla resumen.
4. Redacta ADR-001 con decisión recomendada.
5. Diseña la junta de 15 minutos: portada con 1 número grande, tabla, alternativa, condición de revisión.

**Entregable.** Tabla de 30 inputs × 3 modelos + ADR-001 firmado + outline de 5 slides para la junta.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Datos | <10 inputs | 30 inputs | 30 con bordes deliberados |
| Métricas | 1 | 3 | 3 con incertidumbre |
| ADR | preferencias | con números | con alternativa rechazada y disparador de revisión |
| Junta | sin estructura | outline | outline con 1 número grande y plan B |
::/albatros
