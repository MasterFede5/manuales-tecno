---
unidad: 1
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Identifica y clasifica IAs reales

::practica{titulo="Audita cinco productos del mercado y ubícalos en el árbol IA → ML → DL → LLMs"}
**Problema.** Tu equipo te encarga preparar una nota técnica. Toma 5 productos y responde:
A) ¿Es IA? ¿Bajo qué definición?
B) ¿Es ML, DL o LLM? Justifica.
C) ¿Es IA estrecha, general o súper-IA?
D) Frase simple para un no-técnico.

Productos:
1. Filtro de spam de Gmail.
2. Tesla Autopilot.
3. ChatGPT.
4. Recomendador de Netflix.
5. Google Maps con re-ruteo.

---

**Respuesta tabulada.**

| Producto | A) ¿Es IA? | B) ML/DL/LLM | C) Cuán estrecha | D) Frase simple |
|---|---|---|---|---|
| **1. Spam Gmail** | Sí (moderna) | ML clásico | Muy estrecha (solo correos) | "Aprende qué es basura viendo millones de mails" |
| **2. Tesla Autopilot** | Sí (todas) | DL (CNNs) | Estrecha (solo maneja) | "Computadora que mira cámaras y decide cómo girar" |
| **3. ChatGPT** | Sí (todas) | LLM | Estrecha pero ancha (texto) | "Programa que aprendió a hablar leyendo internet" |
| **4. Netflix** | Sí (moderna) | ML | Estrecha (solo recomienda) | "Aprende qué te gusta viendo a otros como tú" |
| **5. Google Maps** | Discutible | Mezcla (ML + clásico) | Estrecha | "Predice tráfico con datos de otros coches" |

---

**Discusión clave.**

> **¿Por qué ChatGPT se siente "más IA"?** 
> 1. **Generaliza** a tareas nuevas.
> 2. **Genera contenido**, no solo clasifica.
> 3. **Conversa**, disparando nuestra intuición de "inteligente".
>
> **Verificación:** Ante la pregunta "¿es IA?", la mejor respuesta es "depende de la definición operativa usada".
::/practica

---

## Práctica resuelta — De "es IA" a "es marketing"

::practica{titulo="Detecta marketing puro en 3 productos"}
**Problema.** Tu directora vio 3 productos "powered by AI". Tienes 20 minutos para evaluarlos.

Productos:
1. Refrigerador Samsung Family Hub.
2. Cepillo de dientes Oral-B iO.
3. Banca móvil BBVA (fraude).

**Paso 1 — Marco de auditoría:**
1. ¿Aprende de datos o aplica reglas fijas?
2. ¿Hay pista técnica (ML, red neuronal)?
3. ¿Explica cómo funciona o es "magia"?

**Paso 2 — Aplicación:**

| Producto | ¿Aprende? | Pista técnica | ¿Marketing? | Veredicto |
|---|---|---|---|---|
| **Samsung Hub** | Parcial | CNN + API externa | Mezcla | Sí es IA, pero el "wow" es un LLM ajeno |
| **Oral-B iO** | No (reglas) | Clasificador simple | Mayormente | ML clásico empacado como IA |
| **BBVA Fraude** | Sí | Random Forest + DL | No | IA real, ANI muy estrecha |

**Paso 3 — Reporte:**
> *"De los 3, solo BBVA usa IA en el sentido completo (aprende de datos masivos). Samsung mezcla IA real con marketing. Oral-B es ML clásico etiquetado como IA."*

> **Lección clave:** Si no hay pista técnica concreta documentada, asume que es marketing.
::/practica

---

## Práctica resuelta — Mapa mental de "qué es IA"

::practica{titulo="Construye un mapa mental para un no-técnico"}
**Problema.** Tu mamá pregunta "¿qué es la IA, es como Terminator?". Hazle un mapa mental de 5 minutos.

**Paso 1 — Centro y ramas:**
- Centro: **¿Qué es IA?**
- Ramas: Qué hace, Tipos, Ejemplos cotidianos.

**Paso 2 — Hojas y analogías:**
- **Qué hace:** "Programas que aprenden de ejemplos, no de reglas (como cuando aprendiste a reconocer frutas)".
- **Tipos:** "Estrecha (existe, hace 1 cosa bien) vs General (Terminator, no existe)".
- **Ejemplos:** "Filtro de spam, recomendaciones de Netflix".

**Paso 3 — Diseño:**
- Usa Whimsical o Canva.
- Cajas redondeadas, colores distintos, iconos simples.

**Paso 4 — Prueba:**
- Le muestras el mapa a tu mamá. 
- Si logra repetir los conceptos clave sin jerga técnica, funcionó.
- **Lección clave:** Explicar algo a un principiante es el mejor test de que lo entiendes.
::/practica
