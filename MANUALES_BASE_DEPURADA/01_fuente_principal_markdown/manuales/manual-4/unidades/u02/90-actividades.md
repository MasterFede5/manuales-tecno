---
unidad: 2
seccion: actividades
paginas_objetivo: 2
---

## Actividades — Unidad 02

::interioriza
Imagina que un PRD es como los planos de una casa. 
Si omites la estructura y los materiales permitidos, el equipo de construcción hará lo que pueda, 
pero el resultado podría derrumbarse a la primera tormenta.
::/interioriza

::pausa{}
**Deducción rápida:** Si no redactas los "no-objetivos" de la casa, ¿qué habitación innecesaria crees que construiría primero el equipo?
::/pausa

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
1. Un PRD de 3 páginas siempre es mejor que uno de 1 página. ( ) _________

2. Los criterios de aceptación pueden ser revisados por el autor del módulo. ( ) _________

3. Un proyecto puede saltarse el plan de rollback si los tests pasan. ( ) _________

4. El cono de incertidumbre se cierra solo, sin trabajo del equipo. ( ) _________

5. Spec-driven prompting es esencial desde el primer día del proyecto. ( ) _________
::/act-tf

::act-case{titulo="Caso para resolver — la junta del viernes" lineas=12}
* Tu director propone agregar 4 features más sin mover la fecha.
* La coordinadora académica calla.
* El desarrollador se horroriza.
* Tienes el PRD v1.0 impreso en la mano.

Diseña tu intervención en 4 actos: 
- (1) cómo abres usando el PRD.
- (2) qué le muestras del cono de incertidumbre y trade-offs.
- (3) qué propones concretamente (3 escenarios A/B/C).
- (4) cómo cierras pidiendo decisión documentada en ADR. 
Mínimo 10 líneas.
::/act-case

::albatros{titulo="Tu primer PRD asistido por IA + 3 briefs + 1 ADR" tipo="taller" tiempo="3 h"}
**Pregunta detonadora:**
Si no escribes el PRD, alguien lo escribirá por ti, o peor, no se escribirá y construirán cualquier cosa. 
¿Cómo te garantizas que la conversación quede capturada?

**Lo que harás:**
- Elige un proyecto IA real o usa "Asistente de tu materia favorita".
- Aplica el meta-PRD del subtema 2.1 con datos reales.
- Refina con stress-test de 3 ángulos: técnico, financiero, riesgo no listado.
- Redacta 3 briefs (subtema 2.2) para los primeros módulos.
- Documenta 1 ADR del trade-off principal.
- Adopta el DoD canónico (subtema 2.3) y suma 1 ítem propio.
- Asigna IDs por capa (S-/F-/T-/O-) a cada ítem del PRD.
- Pide a otra persona que lo revise con 5 preguntas.

**Materiales:** Cuenta de LLM, repo (Git/Notion), 3 horas.

**Entregable:** 
Carpeta/repo con PRD v1.0 (1 pp), 3 briefs, 1 ADR, DoD personalizado, mapa de IDs.

**Rúbrica corta:**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| PRD en 1 pp | excede | abigarrado | legible |
| Métricas | "satisfactorias" | parciales | numéricas |
| No-objetivos | ausentes | 1-2 | 4+ explícitos |
| Briefs | divergen | aceptables | trazables con IDs |
| ADR | informal | con contexto | consecuencias/revisión |
| DoD | adoptado tal cual | 1 ítem propio | 2+ ítems propios |
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
* La objetivo *"reducir 60 % carga"* lleva ID ____-001 (capa _____________).
* El módulo *"clasificador"* lleva ID ____-014 (capa _____________).
* La conexión *"ASGI con base"* lleva ID ____-027 (capa _____________).
* La rotación *"on-call lunes-jueves"* lleva ID ____-003 (capa _____________).
::/act-fill

::act-mindmap{titulo="Mapa mental del PRD del Asistente" centro="PRD v1.0" nodos_primarios=8 nodos_secundarios=16}
Llena las 8 ramas con: 
- (1) visión/problema, (2) objetivos S/F/T/O, (3) no-objetivos, (4) métricas.
- (5) usuarios/dolores, (6) alcance v1, (7) riesgos, (8) rollback.
En cada nodo secundario usa un dato concreto de tu institución.
::/act-mindmap

::act-label{titulo="Etiqueta el cono de incertidumbre del proyecto"}
::visual{tipo="grafica" descripcion="Gráfica del cono de incertidumbre con eje X (fases) y eje Y (rango ±%). Cinco bandas cerrándose. Espacios en blanco para la acción que cierra cada fase." paginas=0.5}
> Marca: 
> a) mayor riesgo de sobrecompromiso. 
> b) cuándo puedes prometer fecha. 
> c) cuándo el costo de cambio es alto. 
> d) dónde mueren los proyectos por mala gestión.
::/act-label

::albatros{titulo="Reto — convences a tu director de un trade-off impopular" tipo="reto" tiempo="45 min"}
**Pregunta detonadora:**
Director: "queremos GPT-5 para todo". Tú calculas que Haiku + escalación ahorra $2,100/año. 
¿Cómo lo convences sin perder la silla?

**Lo que harás:**
- Construye un mini-experimento: 30 inputs reales, 3 modelos, 3 criterios.
- Mide calidad, latencia y costo. Genera tabla resumen.
- Redacta ADR-001 con decisión recomendada.
- Diseña la junta: portada con 1 número grande, tabla, alternativa, revisión.

**Entregable:** 
Tabla 30 inputs × 3 modelos + ADR-001 + outline de 5 slides.

**Rúbrica corta:**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Datos | <10 inputs | 30 inputs | 30 con bordes deliberados |
| Métricas | 1 | 3 | 3 con incertidumbre |
| ADR | preferencias | con números | alternativa y disparador |
| Junta | sin estructura | outline | outline con plan B |
::/albatros
