---
unidad: 1
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 01

> Este banco extiende las actividades del bloque `90-actividades.md`. Resuelve cada ejercicio en tu cuaderno o en un documento digital. Las respuestas oficiales están al final, pero **no las veas hasta haber intentado** cada ejercicio al menos una vez.

---

### Bloque A — Definiciones operativas (1.1)

::act-mcq{titulo="Definiciones de IA — selecciona la mejor opción"}
1. La definición que **mejor distingue** un termostato de una calculadora es:
   - [ ] La de Turing (indistinguible de un humano)
   - [x] La de Russell & Norvig (agente racional que percibe y actúa)
   - [ ] La de uso popular 2025 (genera contenido nuevo)
   - [ ] Ninguna

2. Tu primo dice que su licuadora "ya tiene IA" porque enciende al detectar peso. Bajo la definición moderna de IA:
   - [ ] IA débil
   - [ ] IA simbólica
   - [x] No es IA — es solo un sensor con regla fija
   - [ ] IA generativa

3. Si una empresa promete "una solución con IA", la **primera pregunta** que haces es:
   - [ ] ¿Cuánto cuesta?
   - [x] ¿Qué tipo de IA: simbólica, ML clásico o generativa?
   - [ ] ¿En qué nube corre?
   - [ ] ¿Es open source?
::/act-mcq

::act-tf{titulo="V/F sobre las tres definiciones operativas"}
1. La definición de Turing mide inteligencia por **resultados** verificables. ( ) ____________
2. Bajo la definición de Russell & Norvig, un termostato es IA mínima. ( ) ____________
3. La definición moderna (2025) excluye la IA simbólica clásica. ( ) ____________
4. ChatGPT cumple las tres definiciones simultáneamente. ( ) ____________
::/act-tf

---

### Bloque B — Línea de tiempo (1.2)

::act-fill{titulo="Completa con los hitos correctos"}
En _____________ Alan Turing publica su artículo donde propone su test. En _____________ se acuña el término "Artificial Intelligence" en _____________. El primer invierno de IA empezó en _____________ tras el reporte _____________. La revolución moderna arranca en _____________ con _____________ (modelo) en ImageNet. El paper de la arquitectura _____________ se publica en _____________. ChatGPT se lanza en _____________ y alcanza _____________ usuarios en 2 meses.
::/act-fill

::act-order{titulo="Ordena cronológicamente los hitos de IA"}
[ ] AlexNet gana ImageNet
[ ] Conferencia de Dartmouth
[ ] Test de Turing
[ ] Lanzamiento de ChatGPT
[ ] Publicación del Transformer
[ ] Deep Blue vence a Kasparov
[ ] AlphaGo vence a Lee Sedol
::/act-order

---

### Bloque C — Tipos de IA (1.3)

::act-match{titulo="Relaciona ejemplo con tipo de IA"}
| Sistema | Tipo |
|---|---|
| 1. ChatGPT ayudando con un ensayo | a) ANI muy estrecha |
| 2. Filtro antispam de Gmail | b) ANI ancha (muchas tareas de texto) |
| 3. AlphaFold prediciendo proteínas | c) AGI (no existe) |
| 4. Un robot humanoide universal | d) ANI especializada en biología |
| 5. ASI por Bostrom | e) Súper-IA (ASI) |
::/act-match

::act-mcq{titulo="ANI, AGI o ASI"}
1. Hoy en 2025, lo único comercial es:
   - [x] ANI (estrecha)
   - [ ] AGI proto
   - [ ] ASI
   - [ ] Mezcla difusa

2. El argumento más sólido para decir que GPT-5 NO es AGI es que:
   - [ ] No habla todos los idiomas
   - [x] Falla en tareas físicas y aprendizaje continuo
   - [ ] Es muy caro
   - [ ] No tiene cuerpo
::/act-mcq

---

### Bloque D — Jerarquía IA → ML → DL → LLM (1.4)

::act-order{titulo="Ordena de mayor a menor (más amplio → más específico)"}
[ ] Deep Learning
[ ] Inteligencia Artificial
[ ] Large Language Models (LLMs)
[ ] Machine Learning
::/act-order

::act-case{titulo="Caso práctico: clasifica 6 sistemas en la jerarquía" lineas=12}
Indica si es **IA simbólica**, **ML clásico**, **DL no LLM** o **LLM**. Justifica:
1. MYCIN (sistema experto de los 70).
2. Random Forest para predecir cancelaciones.
3. AlphaFold prediciendo proteínas.
4. Claude Opus escribiendo código.
5. CNN detectando tumores.
6. Algoritmo A* en Google Maps.
::/act-case

---

### Bloque E — Cómo aprende un modelo (1.5)

::act-tf{titulo="V/F sobre entrenamiento de LLMs"}
1. Un LLM memoriza textos completos de internet. ( ) ____________
2. RLHF significa Reinforcement Learning from Human Feedback. ( ) ____________
3. El pre-entrenamiento enseña a seguir instrucciones. ( ) ____________
4. Las alucinaciones son bugs de software. ( ) ____________
5. Un modelo "comprende" como un humano. ( ) ____________
::/act-tf

::act-fill{titulo="Las tres fases del entrenamiento"}
El entrenamiento tiene tres fases. Primero el _____________, donde predice el siguiente _____________. Después viene el _____________ con datos curados. Finalmente se aplica _____________, donde humanos comparan respuestas.
::/act-fill

---

### Bloque F — Modelos fundacionales y LLMs (1.6)

::act-mcq{titulo="Modelos fundacionales — repaso"}
1. Un "modelo fundacional" es:
   - [ ] Muy caro
   - [x] Base reusable para muchas tareas distintas
   - [ ] Financiado por fundaciones
   - [ ] Antiguo

2. La diferencia entre un modelo abierto y uno cerrado es:
   - [ ] El abierto es más débil
   - [x] El abierto se puede correr localmente
   - [ ] El cerrado cuesta dinero
   - [ ] El abierto no tiene RLHF
::/act-mcq

::act-mindmap{titulo="Mapa mental abierto" centro="LLM" nodos_primarios=6 nodos_secundarios=12}
Llena las burbujas con lo aprendido. Usa: arquitectura, datos, fases, capacidades, limitaciones, ecosistema 2025.
::/act-mindmap

---

## Clave de respuestas

**Bloque A — MCQ:** 1-b · 2-c · 3-b. **V/F:** 1-F · 2-V · 3-V · 4-V.
**Bloque B — Fill:** 1950 · 1956 · Dartmouth · 1974 · Lighthill · 2012 · AlexNet · Transformer · 2017 · noviembre 2022 · 100 millones. **Order:** Test Turing (1950) → Dartmouth (1956) → Deep Blue (1997) → AlexNet (2012) → AlphaGo (2016) → Transformer (2017) → ChatGPT (2022).
**Bloque C — Match:** 1-b · 2-a · 3-d · 4-c · 5-e. **MCQ:** 1-a · 2-b.
**Bloque D — Order:** IA → ML → DL → LLMs. **Caso:** 1-Simbólica · 2-ML clásico · 3-DL no LLM · 4-LLM · 5-DL no LLM · 6-Simbólico.
**Bloque E — V/F:** 1-F · 2-V · 3-F · 4-F · 5-F. **Fill:** pre-entrenamiento · token · fine-tuning supervisado · RLHF.
**Bloque F — MCQ:** 1-b · 2-b.
