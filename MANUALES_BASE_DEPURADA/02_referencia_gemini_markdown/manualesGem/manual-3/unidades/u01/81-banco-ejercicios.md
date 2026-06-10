---
unidad: 1
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Unidad 01

> Este banco extiende las actividades del bloque `90-actividades.md`. Resuelve cada ejercicio en tu cuaderno o en un documento digital. Las respuestas oficiales están al final, pero **no las veas hasta haber intentado** cada ejercicio al menos una vez.

---

### Bloque A — Definiciones operativas (1.1)

::act-mcq{titulo="Definiciones de IA — selecciona la mejor opción"}
1. La definición que **mejor distingue** un termostato inteligente de una calculadora científica es:
   - [ ] La de Turing (indistinguible de un humano)
   - [x] La de Russell & Norvig (agente racional que percibe y actúa)
   - [ ] La de uso popular 2025 (genera contenido nuevo)
   - [ ] Ninguna; ambos son IA bajo cualquier definición

2. Tu primo dice que su licuadora "ya tiene IA" porque enciende sola al detectar peso. Bajo la definición moderna de IA (aprende de datos), esto es:
   - [ ] IA débil
   - [ ] IA simbólica
   - [x] No es IA — es solo un sensor con regla fija
   - [ ] IA generativa

3. Si una empresa promete "una solución con IA" en su software, la **primera pregunta útil** que puedes hacer es:
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
En _____________ Alan Turing publica el artículo "Computing Machinery and Intelligence" donde propone su famoso test. En _____________ se acuña el término "Artificial Intelligence" en la conferencia de _____________. El primer invierno de IA empezó en _____________ tras el reporte _____________. La revolución del deep learning moderno arranca en _____________ con _____________ (modelo) en el concurso ImageNet. El paper "Attention is all you need" se publica en _____________ y describe la arquitectura _____________. ChatGPT se lanza al público en _____________ y alcanza _____________ usuarios en 2 meses.
::/act-fill

::act-order{titulo="Ordena cronológicamente los hitos de IA"}
[ ] AlexNet gana ImageNet
[ ] Conferencia de Dartmouth
[ ] Test de Turing (artículo original)
[ ] Lanzamiento de ChatGPT
[ ] Publicación del Transformer (Vaswani et al.)
[ ] Deep Blue vence a Kasparov
[ ] Modelos razonadores (o1, o3) llegan al público
[ ] AlphaGo vence a Lee Sedol
::/act-order

---

### Bloque C — Tipos de IA (1.3)

::act-match{titulo="Relaciona ejemplo con tipo de IA"}
| Sistema | Tipo |
|---|---|
| 1. ChatGPT-5 ayudando con un ensayo | a) ANI muy estrecha (1 sola tarea) |
| 2. Filtro antispam de Gmail | b) ANI ancha (muchas tareas con texto) |
| 3. AlphaFold prediciendo proteínas | c) AGI (no existe aún) |
| 4. Un robot humanoide que aprende cualquier oficio igual que un humano | d) ANI especializada en biología |
| 5. ASI imaginada por Bostrom | e) Súper-IA (ASI, hipotética) |
::/act-match

::act-mcq{titulo="ANI, AGI o ASI"}
1. Hoy en 2025, lo único que existe comercialmente es:
   - [x] ANI (estrecha, incluso si es muy ancha)
   - [ ] AGI proto
   - [ ] ASI
   - [ ] Una mezcla difusa de las tres

2. El argumento más sólido para decir que GPT-5 NO es AGI es que:
   - [ ] No habla todos los idiomas
   - [x] Falla en tareas físicas, planeación a largo plazo y aprendizaje continuo, donde un humano promedio sí puede
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
Para cada sistema, indica si es **IA simbólica clásica**, **ML clásico (no DL)**, **DL no LLM** o **LLM**. Justifica con una pista técnica:

1. MYCIN (sistema experto médico de los 70).
2. Random Forest que predice si un cliente abandonará el servicio.
3. AlphaFold 3 prediciendo estructura de proteínas.
4. Claude Opus 4.7 escribiendo código.
5. CNN que detecta tumores en radiografías.
6. Algoritmo A* en Google Maps para ruta más corta.
::/act-case

---

### Bloque E — Cómo aprende un modelo (1.5)

::act-tf{titulo="V/F sobre entrenamiento de LLMs"}
1. Un LLM "lee" internet y memoriza textos completos. ( ) ____________
2. RLHF significa Reinforcement Learning from Human Feedback. ( ) ____________
3. El pre-entrenamiento enseña al modelo a seguir instrucciones. ( ) ____________
4. Las alucinaciones son bugs del software, no consecuencias del entrenamiento. ( ) ____________
5. Un modelo "comprende" lo que escribe en el sentido humano del término. ( ) ____________
::/act-tf

::act-fill{titulo="Las tres fases del entrenamiento"}
El entrenamiento moderno de un LLM tiene tres fases. Primero el _____________ (a veces llamado _____________ en inglés), donde el modelo aprende a predecir el siguiente _____________. Después viene el _____________ con datos curados de pares pregunta-respuesta de calidad. Finalmente se aplica _____________ (siglas RLHF), donde humanos comparan respuestas y el modelo aprende _____________.
::/act-fill

---

### Bloque F — Modelos fundacionales y LLMs (1.6)

::act-mcq{titulo="Modelos fundacionales — repaso"}
1. Un "modelo fundacional" se llama así porque:
   - [ ] Cuesta mucho dinero entrenarlo
   - [x] Sirve como base reusable para muchas tareas distintas con poco ajuste extra
   - [ ] Lo financia una fundación
   - [ ] Es de los primeros en su categoría

2. La diferencia clave entre un modelo abierto (Llama, Mistral) y uno cerrado (Claude, GPT) es:
   - [ ] Que el abierto siempre es más débil
   - [x] Que del abierto puedes descargar pesos y correrlo localmente; del cerrado solo accedes vía API
   - [ ] Que el cerrado siempre cuesta dinero
   - [ ] Que el abierto no tiene RLHF
::/act-mcq

::act-mindmap{titulo="Mapa mental abierto" centro="LLM" nodos_primarios=6 nodos_secundarios=12}
Llena las burbujas con lo aprendido en 1.5 y 1.6. Usa estos primarios sugeridos: arquitectura, datos de entrenamiento, fases del entrenamiento, capacidades, limitaciones, ecosistema 2025.
::/act-mindmap

---

## Clave de respuestas

**Bloque A — MCQ:** 1-b · 2-c · 3-b. **V/F:** 1-F (mide por apariencia) · 2-V · 3-V · 4-V.

**Bloque B — Fill:** 1950 · 1956 · Dartmouth · 1974 · Lighthill · 2012 · AlexNet · 2017 · Transformer · noviembre 2022 · 100 millones. **Order:** Test Turing (1950) → Dartmouth (1956) → Deep Blue (1997) → AlexNet (2012) → AlphaGo (2016) → Transformer (2017) → ChatGPT (2022) → Modelos razonadores (2024-2025).

**Bloque C — Match:** 1-b · 2-a · 3-d · 4-c · 5-e. **MCQ:** 1-a · 2-b.

**Bloque D — Order:** IA → ML → DL → LLMs. **Caso:** 1-Simbólica (reglas y árbol de inferencia) · 2-ML clásico (algoritmo de ensemble sin redes profundas) · 3-DL no LLM (red neuronal específica para proteínas) · 4-LLM (Transformer entrenado con texto a gran escala) · 5-DL no LLM (CNN para visión médica) · 6-Simbólico (algoritmo clásico, no aprende).

**Bloque E — V/F:** 1-F (no memoriza textos completos, aprende patrones estadísticos) · 2-V · 3-F (eso es el fine-tuning supervisado, no el pre-entrenamiento) · 4-F (son consecuencia natural del entrenamiento por predicción de tokens) · 5-F (no hay evidencia de comprensión humana). **Fill:** pre-entrenamiento · pre-training · token · fine-tuning supervisado · Reinforcement Learning from Human Feedback · preferencias humanas.

**Bloque F — MCQ:** 1-b · 2-b. **Mindmap:** respuesta libre, valida que aparezcan: Transformer, atención, billones de tokens de texto, pre-train + SFT + RLHF, generar texto, alucinar, fecha de corte, modelos abiertos/cerrados.
