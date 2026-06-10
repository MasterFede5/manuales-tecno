---
unidad: 3
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 03

---

::act-mcq{titulo="Prompt Engineering — repaso"}
1. La anatomía R-T-C-R-F-E significa:
   - [ ] Razón-Tema-Caso-Reto-Formato-Estilo
   - [x] Rol-Tarea-Contexto-Restricciones-Formato-Ejemplos
   - [ ] Reflexión-Tema-Carga-Resultado-Formato-Evaluación
   - [ ] Random-Token-Context-Response-Format-Edition

2. La técnica que **mejor** se usa para problemas matemáticos complejos es:
   - [ ] Zero-shot
   - [ ] Few-shot solo
   - [x] Chain-of-thought ("piensa paso a paso")
   - [ ] Self-consistency

3. Few-shot prompting funciona porque:
   - [ ] Reentrenas el modelo
   - [ ] Le pagas más
   - [x] Le das ejemplos del patrón input-output deseado y el modelo lo imita
   - [ ] El modelo "memoriza" tus ejemplos para futuras conversaciones

4. ¿Cuál de estos es un antipatrón?
   - [ ] Definir el rol del asistente
   - [ ] Pedir formato JSON
   - [x] Mezclar 4 tareas distintas en un solo mega-prompt
   - [ ] Iterar la respuesta

5. La regla de oro del prompting es:
   - [ ] "ChatGPT siempre es lo mejor"
   - [x] Si el output no es lo esperado, el problema casi siempre está en el prompt
   - [ ] La temperatura debe ser 0.7
   - [ ] No usar emojis
::/act-mcq

---

::act-table{titulo="Identifica antipatrones en estos 4 prompts"}
| # | Prompt | Antipatrón principal | Corrección sugerida |
|---|---|---|---|
| 1 | "ayúdame" |  |  |
| 2 | "Eres experto pero también novato; explica detallado pero conciso, máximo 50 palabras pero cubre 10 temas" |  |  |
| 3 | "Hazlo bien" |  |  |
| 4 | "¿Cuál es el mejor político del mundo?" |  |  |
::/act-table

---

::act-match{titulo="Relaciona técnica con caso de uso ideal"}
| Técnica | Caso de uso |
|---|---|
| 1. Zero-shot | a) Necesito JSON con campos específicos |
| 2. Few-shot | b) Pregunta simple con conocimiento general |
| 3. Chain-of-thought | c) Decisión médica donde el costo del error es alto |
| 4. Self-consistency | d) Problema matemático complejo |
| 5. ReAct | e) Clasificar correos en 5 categorías custom |
| 6. Structured output | f) Tarea que requiere consultar herramientas externas |
::/act-match

---

::act-fill{titulo="Completa la anatomía"}
Un prompt profesional tiene 6 capas:
1. _____________ (quién es el modelo)
2. _____________ (qué hace)
3. _____________ (quién soy yo y por qué necesito esto)
4. _____________ (límites: longitud, idioma, lo prohibido)
5. _____________ (estructura de la respuesta)
6. _____________ (opcionales: pares input-output)

La técnica de pedir al modelo "_____________" antes de responder mejora dramáticamente la matemática y la lógica. Para tareas con formato custom, conviene dar _____________ ejemplos al modelo (3 a 5 suelen ser óptimos).
::/act-fill

---

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Cuanto más largo el prompt, mejor la respuesta. ( ) ____________________________________________
2. Few-shot reentrena al modelo permanentemente. ( ) ____________________________________________
3. Chain-of-thought es útil incluso para preguntas triviales. ( ) ____________________________________________
4. Si pongo "máximo 100 palabras" el modelo siempre lo respeta exactamente. ( ) ____________________________________________
5. Pedir un rol específico cambia el tono de la respuesta. ( ) ____________________________________________
6. Iterar prompts es de "principiantes"; un experto lo hace bien a la primera. ( ) ____________________________________________
::/act-tf

---

::act-order{titulo="Ordena el loop de refinamiento iterativo"}
[ ] Ejecutar el prompt en la plataforma
[ ] Escribir prompt v1 con anatomía R-T-C-R-F-E
[ ] Refinar identificando causa raíz del problema
[ ] Re-ejecutar y comparar versus v1
[ ] Evaluar contra criterios objetivos (precisión, formato, tono)
[ ] Si aceptable, guardar en banco personal
::/act-order

---

::albatros{titulo="Reto del prompt extremo: misma tarea, 5 técnicas distintas" tipo="reto" tiempo="60 min"}
**Pregunta detonadora.** ¿Cómo cambia la respuesta del modelo si le aplicas 5 técnicas distintas a la misma tarea?

**Lo que harás.**
1. Define una tarea concreta de tu vida real (ej. "Genera plan de estudio para examen de admisión UNAM").
2. Resuelvela con 5 prompts distintos:
   - **Zero-shot puro:** "Genera plan de estudio para examen UNAM".
   - **Con anatomía R-T-C-R-F-E:** prompt completo de 6 capas.
   - **Few-shot:** prompt con anatomía + 1 ejemplo de plan de estudio para otra materia.
   - **Chain-of-thought:** prompt con anatomía + "piensa paso a paso analizando primero los temas más débiles del estudiante".
   - **Combinación:** anatomía + few-shot + CoT + structured output JSON.
3. Compara las 5 respuestas en tabla con criterios: utilidad, estructura, personalización, tiempo de respuesta, longitud.
4. Identifica cuál técnica funcionó mejor para esta tarea específica.
5. Reflexiona: ¿siempre es mejor la técnica más compleja? ¿Cuándo basta zero-shot?

**Materiales.** Acceso a tu plataforma elegida · 60 min · hoja de cálculo o Notion para la comparativa.

**Entregable.** Reporte de 1-2 páginas con las 5 respuestas (capturas o copy-paste), tabla comparativa, conclusión sobre la técnica ganadora **para tu tarea específica**.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cobertura técnicas | 2-3 técnicas | 4 técnicas | 5 técnicas + combinación |
| Análisis comparativo | "me gustó X" | identifica diferencias | argumenta con criterios |
| Conclusión personal | sin reflexión | menciona aprendizaje | aplicable a otras tareas |
::/albatros

---

::act-case{titulo="Diagnostica 3 prompts reales y reescríbelos" lineas=12}
A continuación tres prompts reales que un compañero te muestra. Para cada uno: a) identifica los antipatrones presentes, b) reescríbelo con la anatomía R-T-C-R-F-E, c) anota qué capas agregaste:

1. *"hazme un resumen del tema 4"*
2. *"Eres muy inteligente y experto. Quiero que me ayudes mucho con todo. Tengo que entregar mañana, ayúdame a hacer una presentación, un ensayo y un quiz, todo bien hecho y profesional."*
3. *"Dame los 10 mejores libros del mundo."*
::/act-case

---

::act-mindmap{titulo="Mapa mental — Técnicas de prompting" centro="PROMPT ENGINEERING" nodos_primarios=5 nodos_secundarios=15}
Llena 5 ramas: anatomía RTCRFE · técnicas básicas (zero/few/CoT) · técnicas avanzadas (self-consistency, ReAct) · output structuring · refinamiento iterativo. Cada rama con 3 hojas concretas (qué es, cuándo usar, ejemplo).
::/act-mindmap

---

::act-label{titulo="Etiqueta las capas de un prompt profesional"}

> Etiqueta las 6 capas y describe en una línea cuál es la función de cada una.
::/act-label


::visual{tipo="ilustracion" descripcion="Ilustración de un prompt mostrado como 6 capas apiladas tipo cebolla o sándwich, con áreas vacías que el estudiante debe etiquetar. Cada capa tiene un color distinto y una flecha hacia un cuadro de descripción vacío. El estudiante debe identificar Rol, Tarea, Contexto, Restricciones, Formato y Ejemplos, y describir en una línea qué hace cada capa." paginas="0.5" src="../manualesGem/assets/visuales/manual-3/u03/90-actividades-v01.svg"}
---

::act-puzzle{titulo="Crucigrama — Vocabulario de prompt engineering" tipo="crucigrama" tamano="13x13"}
Horizontales:
1. Técnica que añade ejemplos del patrón input-output deseado.
3. Acrónimo "Reasoning + Acting" (técnica avanzada).
5. Capa del prompt que define la persona del modelo.
7. Antipatrón: pedir formato Y mientras prohíbes el formato Y.

Verticales:
2. Técnica de "piensa paso a paso".
4. Técnica que ejecuta varias veces y consensúa.
6. Capa que limita longitud, idioma o lo prohibido.
8. Estructura de salida tipo `{}` con campos definidos.
::/act-puzzle

---

::albatros{titulo="Debate: ¿es el prompt engineering una habilidad o un parche?" tipo="debate" tiempo="45 min"}
**Pregunta detonadora.** Algunos dicen que prompt engineering es la habilidad más importante del siglo XXI. Otros dicen que es un parche temporal hasta que los modelos "entiendan mejor lo que queremos". ¿Quién tiene razón?

**Lo que harás.**
1. Forma equipos de 4. Dos defienden "es habilidad esencial duradera"; dos defienden "es parche temporal".
2. Investiga 30 minutos: declaraciones de expertos (Andrej Karpathy, Ethan Mollick, Yann LeCun), evolución de capacidad de "instruction-following" entre GPT-3.5 y GPT-5.
3. Estructura tu argumento en 3 puntos: definición de prompting que usas, evidencia empírica, predicción 5 años.
4. Debate 15 minutos. Vota anonimamente.
5. Cierre individual: ¿cómo cambia tu inversión personal en aprender prompting si crees una postura u otra?

**Materiales.** Acceso a internet, cronómetro.

**Entregable.** a) Hoja con los 3 puntos del equipo + contra-argumentos anticipados; b) reflexión personal de 100 palabras independiente del bando.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Definición de prompting | ambigua | clara | técnica y citada |
| Evidencia | opinión | 1 fuente | 3 fuentes con fechas |
| Réplica | esquiva | responde | desmonta el contra-argumento |
| Reflexión | "el bando que me tocó" | matiza | independiente |
::/albatros
