---
unidad: 1
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Identifica y clasifica IAs reales

::practica{titulo="Audita cinco productos del mercado y ubícalos en el árbol IA → ML → DL → LLMs"}
**Problema.** Tu equipo te encarga preparar una nota técnica para tu jefe de área. Toma estos 5 productos populares y para cada uno responde:

A) ¿Es IA? Bajo qué definición operativa de las tres del 1.1.
B) ¿Es ML, DL o LLM? Justifica con una pista técnica.
C) ¿Es IA estrecha, general o súper-IA? (todas son ANI hoy, pero argumenta cuán "estrecha" es).
D) Si tuvieras que decirle a tu mamá "qué hace", una sola frase clara.

Productos a auditar:
1. **Filtro de spam de Gmail.**
2. **Tesla Autopilot.**
3. **ChatGPT.**
4. **Recomendador de Netflix ("porque viste X").**
5. **Google Maps con re-ruteo por tráfico.**

---

**Respuesta tabulada.**

| Producto | A) ¿Es IA? | B) ML/DL/LLM | C) Cuán estrecha | D) Frase para mamá |
|---|---|---|---|---|
| **1. Filtro spam Gmail** | Sí — definición moderna (aprende de datos) | ML clásico (Naive Bayes + reglas heurísticas) | Muy estrecha: solo clasifica correo | "Aprende qué correos son basura mirando millones de ejemplos" |
| **2. Tesla Autopilot** | Sí — todas las definiciones | DL (CNNs para visión + RL para conducción) | Estrecha: solo manejar | "Una computadora que mira las cámaras del coche y decide cuándo frenar y girar" |
| **3. ChatGPT** | Sí — todas las definiciones, pasa Turing en mayoría de casos | LLM (Transformer entrenado con texto) | Estrecha pero **muy ancha**: muchas tareas distintas con texto | "Un programa que aprendió a hablar leyendo casi todo internet" |
| **4. Netflix recomendador** | Sí — moderna y amplia | ML (collaborative filtering + DL para deep recos) | Estrecha: solo recomienda | "Un sistema que aprende qué te gusta viendo lo que otros parecidos a ti vieron" |
| **5. Google Maps reruteo** | Discutible: es ML + algoritmos clásicos | Mezcla — A* (clásico) + ML para predecir tráfico | Estrecha | "Mapas inteligentes que predicen tráfico viendo datos de millones de coches" |

---

**Discusión clave.**

> **¿Por qué ChatGPT se siente "más IA" que el filtro de spam?** Tres razones:
> 1. **Generaliza** a tareas que no le mostraron explícitamente (zero-shot).
> 2. **Genera contenido nuevo** (texto), no solo clasifica.
> 3. **Conversa**, lo que dispara nuestra intuición humana de "interlocutor inteligente".
>
> Pero técnicamente las cinco son ANI. La diferencia es de **escala** (parámetros, datos), **arquitectura** (Transformer vs Naive Bayes) y **modalidad** (lenguaje conversacional vs clasificación).

> **Verificación.** Si en una entrevista te preguntan "¿es IA esto?", la respuesta correcta de un profesional NO es "sí" o "no", sino: "depende de qué definición operativa uses, y bajo cuál te conviene clasificarlo en este contexto".
::/practica

---

## Práctica resuelta — De "es IA" a "es marketing": 3 productos al microscopio

::practica{titulo="Detecta marketing puro en 3 productos que dicen tener IA"}
**Problema.** Tu compañía te pide investigar tres productos que la directora vio en un anuncio antes de aprobar la compra. Tienes 20 minutos. Cada producto dice "powered by AI".

Productos:
1. **Refrigerador Samsung Family Hub** — anuncio dice "IA que reconoce tus alimentos".
2. **Cepillo de dientes Oral-B iO** — anuncio dice "IA que mejora tu técnica de cepillado".
3. **Banca móvil de BBVA México** — anuncio dice "fraude detectado con IA".

**Paso 1 — Establece tu marco de auditoría.**

Para cada producto pregúntate, en orden:

1. ¿**Aprende de datos** o solo aplica reglas fijas? → si solo aplica reglas, NO es IA bajo la definición moderna.
2. ¿**Qué pista técnica** confirma el aprendizaje? Busca palabras como ML, deep learning, modelo, entrenado con N millones, predicción.
3. ¿La descripción del producto **dice cómo funciona** o solo "es mágico"? El marketing puro evita explicar.

**Paso 2 — Aplica el marco.**

| Producto | ¿Aprende? | Pista técnica | ¿Marketing? | Veredicto |
|---|---|---|---|---|
| **Refrigerador Family Hub** | Parcial: la cámara interna usa visión por computadora (DL real) para identificar alimentos. Pero "IA que sugiere recetas" es ChatGPT detrás. | CNN para reconocimiento + API de LLM externo | Mezcla | Sí es IA, pero el "wow" lo da un LLM ajeno al refri |
| **Oral-B iO** | Tiene sensores de presión y giroscopio. La "IA" detecta zonas no cubiertas con un algoritmo de reglas + clasificador. | Algoritmo embebido (no DL profundo en el cepillo) | Mayormente | ML clásico (clasificador), pero el cepillo no aprende por usuario |
| **BBVA detección de fraude** | Sí: modelos entrenados con millones de transacciones. | Random Forest + redes neuronales para anomaly detection. Documentado en su tech blog. | No | Es IA real, ML clásico + DL, ANI muy estrecha |

**Paso 3 — Comunica el resultado a tu directora.**

Frase corta para tu reporte ejecutivo:

> *"De los 3 productos, solo BBVA usa IA en el sentido completo (aprende de datos a gran escala). Samsung mezcla IA real con marketing. Oral-B es ML clásico empacado como 'IA'. Recomendación: si la compra busca capacidades de IA reales, prioriza BBVA o servicios similares; los otros dos son útiles por otras razones, no por su 'IA'."*

> **Lección clave.** No basta con leer el anuncio. La regla de oro: **si no encuentras una pista técnica concreta (modelo, datos de entrenamiento, paper) en su sitio oficial o tech blog, asume que es marketing puro hasta que demuestre lo contrario.**
::/practica

---

## Práctica resuelta — Diseñé un mapa mental de "qué es IA" para enseñárselo a mi mamá

::practica{titulo="Construye un mapa mental que un no-técnico entienda en 5 minutos"}
**Problema.** Tu mamá quiere entender qué estás estudiando. Le dijiste "IA básica" y ella respondió "¿como Terminator?". Necesitas un mapa mental de 1 página que ella entienda en 5 minutos sin haber tocado tecnología.

**Paso 1 — Define el centro y los hijos.**

Centro: **¿Qué es IA?**

Tres ramas hijas (no más, una mamá no aguanta más):

- **(A) Qué hace.** "Programas que aprenden de ejemplos en lugar de seguir reglas escritas."
- **(B) Tipos.** Estrecha (la única real hoy) vs General (la de las películas, no existe).
- **(C) Ejemplos cotidianos que usa mamá ya.** Filtro de spam, recomendaciones de Netflix, ChatGPT.

**Paso 2 — Para cada rama agrega 2 hojas con analogía.**

- (A) Qué hace:
  - "Como cuando aprendiste a reconocer fruta madura mirando muchas: nadie te dio una regla, viste muchos ejemplos."
  - "Diferente a una calculadora: la calculadora siempre da la misma respuesta a la misma pregunta. La IA puede mejorar si le das más ejemplos."
- (B) Tipos:
  - "Estrecha: lo que existe. Solo sabe hacer una cosa muy bien (como un campeón mundial de ajedrez que no sabe cocinar)."
  - "General: la de Terminator, la de las películas. **No existe** y nadie sabe si llegará."
- (C) Ejemplos:
  - "El filtro que manda mails de promociones a una carpeta aparte: te lo está haciendo IA hace años."
  - "Cuando Netflix te recomienda una serie: IA. Cuando ChatGPT te resume un artículo: IA."

**Paso 3 — Dibújalo.**

Abre **Whimsical** (whimsical.com), **Mindmeister** o **Canva** (plantilla "mind map"). Centro al medio. 3 ramas en colores distintos. Cada rama con sus 2 hojas en cajas redondeadas. Iconos simples: cerebro, robot, casa.

**Paso 4 — Pruébalo con mamá.**

Le mostraste el mapa. **Cronómetro: 5 minutos.** Si al final ella te puede repetir "es como aprender de ejemplos, no de reglas, y la de las películas no existe", funcionó. Si te pregunta "¿pero entonces ChatGPT piensa?", ahí mejoraste tu propia comprensión: tu siguiente iteración debe distinguir **predecir tokens** de **pensar**.

> **Lección clave.** El mejor test de que entiendes IA no es responder un examen, es **explicársela a alguien que no sabe nada**. Si tropiezas, ahí está tu próximo subtema por estudiar.
::/practica
