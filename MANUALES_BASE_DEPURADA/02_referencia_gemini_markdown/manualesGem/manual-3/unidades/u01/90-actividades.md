---
unidad: 1
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 01

---

::act-mcq{titulo="Fundamentos de IA — repaso conceptual"}
1. ¿Qué año se acuñó el término "Artificial Intelligence"?
   - [ ] 1936 (Turing)
   - [ ] 1950 (Test de Turing)
   - [x] 1956 (Conferencia de Dartmouth)
   - [ ] 2017 (Transformer)

2. La arquitectura técnica que **hace posible** ChatGPT, Claude y Gemini se llama:
   - [ ] Perceptrón
   - [ ] CNN (Convolutional)
   - [x] Transformer
   - [ ] GAN

3. La razón principal por la que ChatGPT a veces alucina (inventa hechos con confianza) es:
   - [ ] Está roto y todavía lo están arreglando
   - [x] Su entrenamiento solo le enseña a predecir el siguiente token, no a verificar hechos
   - [ ] Le dan poco RAM
   - [ ] Está saboteado por humanos

4. La jerarquía conceptual correcta es:
   - [ ] LLMs ⊃ DL ⊃ ML ⊃ IA
   - [x] IA ⊃ ML ⊃ DL ⊃ LLMs
   - [ ] ML ⊃ DL ⊃ IA ⊃ LLMs
   - [ ] Todos son sinónimos

5. RLHF significa:
   - [ ] Reinforcement Learning + High Fidelity
   - [x] Reinforcement Learning from Human Feedback
   - [ ] Real-time Linear High-bandwidth Forward
   - [ ] Recurrent Long-context Hidden Function

6. Hoy en 2025, el tipo de IA que **sí existe** comercialmente es:
   - [x] IA Estrecha (ANI)
   - [ ] IA General (AGI)
   - [ ] Súper-IA (ASI)
   - [ ] Las tres
::/act-mcq

---

::act-table{titulo="Línea de tiempo — completa los hitos"}
| Año | Evento | Por qué importa |
|---:|---|---|
| 1950 |  | Cambia "¿pueden las máquinas pensar?" por una pregunta operativa |
| 1956 |  | Nace oficialmente el campo de IA |
|  | 1er invierno IA | Cae el financiamiento por décadas |
| 2012 |  | Resurge el deep learning con GPUs |
| 2017 | Transformer (Vaswani et al.) |  |
|  | ChatGPT lanzado al público | Llega a 100M usuarios en 2 meses |
| 2024 | Modelos razonadores (o1, o3) |  |
::/act-table

---

::act-match{titulo="Relaciona modelo con su empresa creadora"}
| Modelo | Empresa |
|---|---|
| 1. GPT-4o, GPT-5 | a) Anthropic |
| 2. Claude Opus | b) Meta |
| 3. Gemini 2.0 | c) Mistral AI |
| 4. Llama 4 | d) Google DeepMind |
| 5. Mistral Large | e) DeepSeek |
| 6. DeepSeek V3 | f) OpenAI |
::/act-match

---

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Toda IA es Machine Learning. ( ) ____________________________________________
2. El Test de Turing mide si una máquina realmente piensa. ( ) ____________________________________________
3. Hoy existe IA General (AGI) en uso comercial. ( ) ____________________________________________
4. Un Random Forest le puede ganar a una red neuronal en datos tabulares. ( ) ____________________________________________
5. ChatGPT solo predice el siguiente token; "razonar" lo emerge. ( ) ____________________________________________
6. Los modelos abiertos (Llama, Mistral) son menos capaces que los cerrados. ( ) ____________________________________________
::/act-tf

---

::act-fill{titulo="Completa con los términos correctos"}
La IA moderna es principalmente _____________ (subcampo). Dentro de él, las redes neuronales con muchas capas se llaman _____________. Cuando se entrenan con texto a gran escala se llaman _____________. La arquitectura clave que las hace posibles fue publicada en _____________ (año) en el artículo "Attention is all you need" de _____________ (empresa).

El proceso de entrenamiento de un LLM tiene 3 fases: primero _____________, donde el modelo aprende a predecir tokens; luego _____________, donde aprende a seguir instrucciones; finalmente _____________, donde aprende preferencias humanas comparando respuestas.
::/act-fill

---

::act-order{titulo="Ordena la jerarquía técnica de mayor a menor"}
[ ] LLM (Large Language Model)
[ ] Inteligencia Artificial
[ ] Deep Learning
[ ] Machine Learning
::/act-order

---

::albatros{titulo="Construye TU línea de tiempo de IA en Genially o Canva" tipo="investigacion-corta" tiempo="60 min"}
**Pregunta detonadora.** ¿Cómo le explicarías a tu abuela en 5 minutos los 70 años de historia de la IA?

**Lo que harás.**
1. Abre Genially (https://genial.ly), Canva o Prezi (versiones gratuitas son suficientes).
2. Selecciona la plantilla "línea de tiempo".
3. Investiga y agrega **mínimo 12 hitos** con: año, título, descripción de 2-3 líneas, imagen libre de derechos.
4. Incluye obligatoriamente: 1936 Turing computable, 1950 test Turing, 1956 Dartmouth, 1958 Perceptrón, 1966 ELIZA, 1974/1987 inviernos, 1986 retropropagación, 1997 Deep Blue, 2012 AlexNet, 2017 Transformer, 2022 ChatGPT, 2024 modelos razonadores.
5. Agrega 3 hitos extra que te llamen la atención (ej. AlphaGo 2016, GPT-3 2020, Claude 2023, Sora 2024).
6. Comparte el link público.

**Materiales.** Acceso a Genially / Canva / Prezi · cuenta Google · 60 min de tiempo.

**Entregable.** Link a tu línea de tiempo + reflexión escrita de 200 palabras: ¿qué hito te sorprendió más y por qué?

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cantidad de hitos | < 8 | 10-12 | > 12 con extras propios |
| Precisión histórica | varios errores | menores | impecable y citado |
| Diseño visual | desordenado | legible | atractivo y compartible |
| Reflexión | superficial | conecta con presente | discute implicaciones futuras |
::/albatros

---

::act-case{titulo="Caso real: la calculadora 'inteligente' del bachiller" lineas=10}
Tu prima de secundaria te muestra una calculadora gráfica nueva que la marca anuncia como "calculadora con IA". Resuelve integrales paso a paso, grafica funciones y reconoce ecuaciones escritas a mano. Tu prima dice: "es IA, ¿no?".

Argumenta tu respuesta usando las **tres definiciones operativas** de 1.1 (Turing, Russell & Norvig, Moderna). Indica bajo cuál sí, bajo cuál no, y dale a tu prima una recomendación práctica: ¿debe pagar 3000 pesos extra por la "función IA"? Justifica con base en si la calculadora **aprende** o no de uso.
::/act-case

---

::act-label{titulo="Etiqueta el árbol jerárquico IA → ML → DL → LLM"}

> Llena: a) nombre del nivel exterior, b) nivel medio amplio, c) nivel medio específico, d) núcleo. Para cada nivel agrega 2 ejemplos reales (mínimo uno de tu vida diaria).
::/act-label


::visual{tipo="diagrama-flujo" descripcion="Árbol jerárquico vacío con 4 niveles concéntricos. El nivel exterior representa el universo más amplio; los siguientes niveles son subconjuntos progresivamente más específicos. Cada nivel tiene una etiqueta vacía y dos cajas vacías para ejemplos. El estudiante debe escribir IA, ML, DL y LLMs en orden de mayor a menor amplitud, y dar dos ejemplos por nivel." paginas="0.5" src="../manualesGem/assets/visuales/manual-3/u01/90-actividades-v01.svg"}
---

::act-mindmap{titulo="Mapa mental abierto — Historia de la IA" centro="HISTORIA DE LA IA 1950-2025" nodos_primarios=5 nodos_secundarios=15}
Llena las burbujas con los 5 actos de la historia (pre-historia, primer optimismo, sistemas expertos, deep learning, era LLM). Para cada acto, agrega 3 hitos clave con año.
::/act-mindmap

---

::act-puzzle{titulo="Crucigrama — vocabulario fundamental de IA" tipo="crucigrama" tamano="12x12"}
Horizontales:
1. Test propuesto en 1950 para evaluar inteligencia conversacional.
3. Conferencia de 1956 donde se acuñó el término "Artificial Intelligence".
5. Arquitectura de red neuronal publicada en 2017 ("Attention is all you need").
7. Fenómeno donde un LLM inventa hechos con confianza.
9. Subcampo de ML que usa redes neuronales con muchas capas.

Verticales:
2. Empresa creadora de Claude.
4. Tipo de IA hipotética que supera a humanos en todo.
6. Acrónimo de Reinforcement Learning from Human Feedback.
8. Empresa creadora de Gemini.
10. Período de bajo financiamiento de IA tras los 70 y los 80.
::/act-puzzle

---

::albatros{titulo="Debate fundacional: ¿Hoy en 2025 estamos cerca de la AGI?" tipo="debate" tiempo="45 min"}
**Pregunta detonadora.** Sam Altman dice que "AGI llega en 2027". Yann LeCun dice "imposible antes de 2035 con la arquitectura actual". ¿Quién tiene razón y por qué?

**Lo que harás.**
1. **Forma equipos de 4 personas.** Dos defienden "AGI llega antes de 2030", dos defienden "AGI no llegará antes de 2035".
2. **Investiga 30 minutos** evidencia para tu lado: declaraciones públicas, papers, benchmarks (ARC-AGI, MMLU, etc.), capacidades reales de modelos razonadores 2024-2025.
3. **Estructura tu argumento** en 3 puntos: definición de AGI usada, evidencia técnica, implicaciones.
4. **Debate** 15 minutos: 3 min apertura por equipo, 6 min de réplica cruzada, 3 min cierre por equipo.
5. **Vota anonimamente** (incluido el equipo contrario) cuál argumento fue más sólido. La métrica no es ganar, es haber forzado al contrario a precisar su definición.
6. **Cierre individual:** escribe tu opinión real (independiente del lado que te tocó defender) en 100 palabras.

**Materiales.** Acceso a internet, cronómetro, espacio para presentar. Opcional: Claude o ChatGPT como "research assistant" para preparar argumentos (irónico pero útil).

**Entregable.** a) Hoja con los 3 puntos de tu equipo + 3 contra-argumentos anticipados; b) reflexión final individual de 100 palabras; c) acuerdo grupal sobre qué definición de AGI usaron.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Definición de AGI usada | ambigua | clara | técnica y citada |
| Evidencia | opinión | 1-2 fuentes | 3+ fuentes con benchmarks |
| Réplica | esquiva | responde | desmonta el contra-argumento |
| Reflexión final | "el que me tocó" | matiza | independiente del bando |
::/albatros
