---
unidad: 3
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 03

> **Práctica de prompt engineering:**
> - Privilegia ejercicios de **redacción**.
> - Evalúa **pares prompt-respuesta**.
> - Detecta **antipatrones**.
> - Trabaja en tu plataforma base (elegida en U02).
> - ¡Resuelve antes de mirar la clave!

::interioriza
Diseñar un prompt es como pedir una comida a domicilio en un restaurante nuevo:
Si solo dices "comida", te puede llegar cualquier cosa. Debes especificar plato, tamaño e ingredientes (Contexto/Restricciones) para que el resultado sea exacto.
::/interioriza

::pausa{}
**Reflexiona:**
- ¿Alguna vez un modelo te dio una respuesta inútil por ser muy vago en tu "pedido"?
- ¿Qué capa de la anatomía R-T-C-R-F-E crees que falló en ese momento?
::/pausa

---

### Bloque A — Anatomía R-T-C-R-F-E (3.1)

::act-fill{titulo="Redacta cada capa de la anatomía"}
Vas a estudiar el principio de Bernoulli para tu examen de Física. Redacta tu prompt en 6 capas:

1. **Rol:** _____________________________________________________________________
2. **Tarea:** ____________________________________________________________________
3. **Contexto:** _________________________________________________________________
4. **Restricciones:** ____________________________________________________________
5. **Formato:** __________________________________________________________________
6. **Ejemplos (opcional):** _____________________________________________________
::/act-fill

::act-mcq{titulo="Identifica la capa débil del prompt"}
1. Prompt: "Eres un tutor experto de Física. Explícame Bernoulli con un ejemplo numérico. Soy estudiante de prepa, español neutro. Devuelve en 3 párrafos."
   ¿Qué capa **falta** o está débil?
   - [ ] Rol
   - [ ] Tarea
   - [x] Ejemplos (no hay few-shot)
   - [ ] Formato

2. Prompt: "Hazme un cuento."
   ¿Cuántas capas faltan?
   - [ ] 1
   - [ ] 3
   - [x] 5 o 6
   - [ ] 0
::/act-mcq

---

### Bloque B — Zero-shot vs Few-shot vs CoT (3.2)

::act-case{titulo="Decide qué técnica usar para 5 tareas" lineas=10}
Elige la técnica más eficiente (zero-shot, few-shot, chain-of-thought, self-consistency):
Justifica tu respuesta en cada caso.

1. Traducir "hello" al español.
2. Resolver "Si compro 3 manzanas a 2 pesos cada una y un descuento del 15% al final, ¿cuánto pago?".
3. Clasificar correos en 5 categorías personales custom (familia, escuela, trabajo, suscripciones, basura).
4. Decidir si una transacción bancaria es fraude (alto costo del error).
5. Generar un haiku sobre la lluvia.
::/act-case

::act-mcq{titulo="Cuándo NO usar chain-of-thought"}
1. NO uses CoT cuando:
   - [ ] La pregunta es matemática compleja
   - [ ] Hay lógica de varios pasos
   - [x] La tarea es trivial (agregas latencia/costo sin ganar precisión)
   - [ ] Quieres trazabilidad del razonamiento

2. Few-shot con 50 ejemplos:
   - [ ] Es siempre mejor que con 5
   - [ ] No tiene problema de costo
   - [x] Aumenta costo, latencia y riesgo de "lost-in-the-middle" (ideal: 3-5)
   - [ ] El modelo memoriza los 50 ejemplos
::/act-mcq

---

### Bloque C — Role prompting y output structuring (3.3)

::act-match{titulo="Relaciona rol con efecto en la respuesta"}
| Rol asignado | Efecto típico en la respuesta |
|---|---|
| 1. "Eres profesor de prepa, paciente" | a) Tono ejecutivo, bullets cortos, datos accionables |
| 2. "Eres consultor McKinsey" | b) Output JSON limpio, sin texto extra |
| 3. "Eres editor de redacción rigurosa" | c) Texto pulido con cuidado de coherencia y estilo |
| 4. "Eres API que solo devuelve JSON" | d) Lenguaje accesible, analogías cotidianas, preguntas socráticas |
| 5. "Eres revisor de tesis" | e) Comentarios estructurados con citas y críticas constructivas |
::/act-match

::act-fill{titulo="Output structuring — completa el prompt"}
Quiero que clasifiques 10 correos. Devuelve la respuesta en formato _____________ con los siguientes campos por correo: 
id, categoria (una de [familia, escuela, trabajo, suscripcion, basura]), 
confianza (un número entre _____________ y _____________), y razonamiento_corto (máximo _____________ palabras). 
NO incluyas texto adicional fuera del _____________; si la confianza es menor a _____________, marca categoria como _____________.
::/act-fill

---

### Bloque D — Refinamiento iterativo (3.4)

::act-order{titulo="Ordena el loop de refinamiento profesional"}
[ ] Identifica la causa raíz del problema (¿es rol? ¿formato? ¿restricciones?)
[ ] Escribe tu prompt v1 con la anatomía R-T-C-R-F-E
[ ] Ejecuta y observa la respuesta
[ ] Compara la respuesta contra tus criterios objetivos
[ ] Modifica solo la capa problemática (no rehagas todo)
[ ] Vuelve a ejecutar y mide mejora
[ ] Si v2 aceptable, guárdalo en tu banco personal con el contexto en el que sirve
[ ] Si no, vuelve al diagnóstico
::/act-order

::act-tf{titulo="V/F sobre refinamiento"}
1. Si pides "máximo 100 palabras", el modelo lo respeta exactamente. ( ) ____________
2. Iterar el prompt es señal de inexperiencia. ( ) ____________
3. La causa raíz suele estar en restricciones ambiguas o conflictivas. ( ) ____________
4. Cambiar varias capas a la vez en una iteración te ayuda a saber qué funcionó. ( ) ____________
5. Un prompt funcional para una tarea suele funcionar para tareas similares con cambios mínimos. ( ) ____________
::/act-tf

---

### Bloque E — Antipatrones (3.5)

::act-case{titulo="Audita 4 prompts y diagnostica el antipatrón" lineas=12}
Identifica el antipatrón principal y propón una versión mejorada para cada prompt:

1. *"Hazme un buen ensayo de literatura."*
2. *"Eres experto en todo. Explícame física, química y biología en una sola respuesta de 50 palabras."*
3. *"¿Cuál es el mejor presidente del mundo?"*
4. *"Resume este libro entero (PDF de 800 páginas) y dame 50 ideas accionables, cada una con 5 ejemplos numéricos, y un guion de TikTok de 60 s, todo junto, ahora."*
::/act-case

::act-mcq{titulo="Selecciona el peor antipatrón"}
1. ¿Cuál de estos es el antipatrón **más dañino** porque es el más invisible?
   - [ ] Prompt demasiado corto
   - [ ] Pedir formato JSON
   - [x] Mezclar 2 instrucciones contradictorias en el prompt
   - [ ] No definir rol

2. "Confiar en el primer output sin verificar" es:
   - [ ] Buena práctica si el modelo es Pro
   - [ ] Aceptable para tareas creativas
   - [x] Antipatrón en cualquier contexto profesional con consecuencias
   - [ ] Solo aplicable a Claude
::/act-mcq

---

## Clave de respuestas

**Bloque A — Fill:** 
1) "Eres tutor de Física para estudiante de prepa, paciente y socrático" 
2) "Explícame el principio de Bernoulli" 
3) "Soy estudiante de 4to año, examen el viernes, manejo derivadas básicas..."
4) "Máximo 600 palabras, español neutro, sin jerga universitaria" 
5) "Estructura: intuición + fórmula + ejemplo + 1 pregunta" 
6) "Estilo similar a Walter Lewin". 
**MCQ:** 1-c · 2-c.

**Bloque B — Caso:** 
1) zero-shot. 
2) chain-of-thought (matemática). 
3) few-shot con 5 ejemplos custom. 
4) self-consistency o CoT con verificación. 
5) zero-shot (creativo). 
**MCQ:** 1-c · 2-c.

**Bloque C — Match:** 1-d · 2-a · 3-c · 4-b · 5-e. 
**Fill:** JSON · 0 · 1 · 20 · JSON · 0.6 · "incierto".

**Bloque D — Order:** 
v1 → ejecuta → observa → compara contra criterios → diagnostica capa → modifica solo esa capa → re-ejecuta y mide → guarda. 
**V/F:** 1-F · 2-F · 3-V · 4-F · 5-V.

**Bloque E — Caso:** 
1) Vaguedad ("buen") → especificar género, nivel. 
2) Restricciones contradictorias → separar. 
3) Sin criterio objetivo → "según índices X y Y". 
4) Sobrecarga → fragmentar en pipeline. 
**MCQ:** 1-c · 2-c.
