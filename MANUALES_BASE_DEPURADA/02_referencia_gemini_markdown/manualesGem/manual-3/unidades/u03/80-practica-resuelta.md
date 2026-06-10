---
unidad: 3
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — De prompt malo a prompt profesional

::practica{titulo="Toma un prompt vago, identifica antipatrones, refina con anatomía completa"}
**Problema.** Tu compañero te pasa este prompt y se queja de que ChatGPT le dio respuesta inútil:

```
Hazme un resumen del libro de física de bachillerato.
```

Tu tarea: 1) identificar los antipatrones, 2) re-escribir con la anatomía R-T-C-R-F-E, 3) aplicar técnicas (few-shot o CoT si aplica), 4) iterar si hace falta, 5) presentar v1 y v_final con análisis.

---

**Paso 1 — Identifica antipatrones.**

| Antipatrón | Cómo se manifiesta |
|---|---|
| **Vaguedad** | "el libro de física" — ¿cuál libro? ¿qué edición? |
| **Sin contexto** | ¿De quién? ¿Para qué? ¿Qué tan profundo? |
| **Sin formato** | ¿Resumen en bullets? ¿Texto corrido? ¿Cuántas palabras? |
| **Suposición implícita** | El modelo asume el libro más popular y aproxima |
| **Sin definir éxito** | ¿"Bueno" para qué? |

Hay **5 antipatrones** en una sola línea. No es de extrañar que el resultado sea inútil.

---

**Paso 2 — Re-escribe con anatomía completa.**

```
[ROL]
Eres un tutor de física para bachillerato mexicano que conoce a fondo
el programa oficial de la SEP de la UNAM (área I).

[TAREA]
Genera un resumen estructurado por unidades del libro "Física General"
de Tippens (séptima edición) — concretamente las unidades 1 a 5
(Cinemática, Dinámica, Trabajo y Energía, Termodinámica, Ondas).

[CONTEXTO]
Soy estudiante de 3er semestre de bachillerato CCH-Norte UNAM.
Examen final en 3 semanas. Mi profesor enfatiza comprensión conceptual
sobre cálculo. Ya domino álgebra y geometría básica.

[RESTRICCIONES]
- Máximo 1500 palabras totales (300 por unidad).
- Español neutro de México.
- Sin cálculo diferencial.
- Incluye fórmulas en formato simple, no LaTeX complejo.

[FORMATO]
Estructura por unidad:

## Unidad N — [Título]
- **Concepto central:** [1 oración].
- **Fórmulas clave:** lista de 2-4.
- **Aplicación cotidiana:** 1 ejemplo.
- **Pregunta de examen típica:** 1.

[EJEMPLO ÚNICO]
Como ejemplo de formato, así quiero la Unidad 1:

## Unidad 1 — Cinemática
- **Concepto central:** describe el movimiento sin importar las causas.
- **Fórmulas clave:** v = d/t, a = Δv/Δt, x = v₀t + ½at², v² = v₀² + 2ax.
- **Aplicación cotidiana:** calcular cuánto tarda un coche en frenar.
- **Pregunta de examen típica:** "Un objeto cae libre desde 45 m. ¿Cuánto tarda?"

Ahora aplica este formato a las Unidades 2-5.
```

---

**Paso 3 — Aplica técnica adecuada.**

He usado:
- **Role prompting** (capa 1).
- **Few-shot con un ejemplo** (la Unidad 1 ya completa, en lugar de explicarlo abstractamente).
- **Structured output** (formato exacto por unidad).
- **Restricciones explícitas** (palabras, idioma, complejidad).

No usé CoT porque la tarea no requiere razonamiento step-by-step.

---

**Paso 4 — Itera si hace falta.**

Después de ejecutar v1, observa:
- ¿El formato fue respetado en las 5 unidades?
- ¿Las fórmulas son correctas? Verifica al menos 2 al azar.
- ¿La pregunta de examen es realista para CCH-UNAM?

Si algo falla, refinas la capa correspondiente sin rehacer todo. Por ejemplo, si las preguntas de examen suenan inventadas, agrega: "Las preguntas deben estar basadas en exámenes reales del CCH-UNAM publicados en bibliotecas oficiales".

---

**Paso 5 — Comparativa v1 vs v_final.**

| Métrica | Prompt v1 (vago) | Prompt v_final |
|---|---|---|
| Longitud | 9 palabras | 320 palabras |
| Antipatrones | 5 | 0 |
| Tiempo de redacción | 5 segundos | 8 minutos |
| Tiempo de iteración requerido | 30+ min | < 5 min |
| Reusabilidad | nula | alta (template para otras unidades, otras materias) |
| Calidad de output | genérica | personalizada y útil |

**Conclusión.** El prompt v_final es 36× más largo, pero ahorra 6× más tiempo y produce un resultado **reutilizable**. Cada minuto que invirtiste en redactar el prompt vale 10 minutos de iteración futura.

> **Verificación.** Pega tu prompt v_final en Notion como "Tutor Resumen Física - Tippens v1". La próxima vez que necesites resumen de otra materia, lo clonas y cambias dos campos.

> **Trampa común evitada.** No "improvises" prompts complejos. Inviértele 5-10 minutos a cada uno la primera vez. Luego los reusas durante meses.
::/practica

---

## Práctica resuelta — Few-shot que aumentó precisión de 40% a 95% en clasificación

::practica{titulo="Diseña un clasificador de correos con 4 ejemplos few-shot"}
**Problema.** Necesitas que tu tutor IA te ayude a triar tu correo cada mañana. Tienes 5 categorías personales: **familia**, **escuela**, **trabajo**, **suscripciones** y **basura**. Probaste con zero-shot y la precisión fue mediocre (clasificaba "examen final" como suscripción y "newsletter de programación" como escuela). Vas a corregirlo con few-shot.

**Paso 1 — Define tus 5 categorías con criterios claros.**

| Categoría | Criterio operativo |
|---|---|
| **familia** | Remitente es padre, madre, hermanos, primos directos, pareja |
| **escuela** | Remitente con dominio de tu institución (.edu o .unam.mx), o profesor, o sistema de calificaciones |
| **trabajo** | Remitente de tu empleador, clientes, asuntos pagos |
| **suscripciones** | Newsletters, marketing, ofertas, notificaciones de servicios sin acción urgente |
| **basura** | Spam, phishing, remitente desconocido pidiendo dinero o datos |

**Paso 2 — Selecciona 4 ejemplos few-shot que cubran casos límite.**

Deliberadamente no elijas casos triviales. Elige los que confunden al modelo zero-shot:

```
Ejemplo 1:
Remitente: profe.martinez@cch-unam.mx
Asunto: "Recordatorio de examen miércoles"
→ escuela (no es suscripción aunque sea recordatorio; el dominio es escolar)

Ejemplo 2:
Remitente: newsletter@platzi.com
Asunto: "Curso de Python en oferta"
→ suscripciones (educativo pero es marketing comercial, no de tu institución)

Ejemplo 3:
Remitente: maría_tia@gmail.com
Asunto: "Te envío fotos del cumpleaños"
→ familia (remitente personal conocido, no escolar ni laboral)

Ejemplo 4:
Remitente: support@bancomer.com.mx
Asunto: "Transferencia recibida $1,500 MXN"
→ trabajo (transacción real, requiere atención; no es suscripción)
```

**Paso 3 — Estructura del prompt completo.**

```
[ROL]
Eres mi asistente de triage de correo. Clasificas cada correo en una sola
de las 5 categorías personales que ya definimos.

[CRITERIOS POR CATEGORÍA]
- familia: remitente padre/madre/hermanos/primos/pareja.
- escuela: dominio escolar o profesor o calificaciones.
- trabajo: empleador, clientes, transacciones reales.
- suscripciones: newsletters, marketing, notificaciones sin acción urgente.
- basura: spam, phishing, desconocidos pidiendo dinero o datos.

[EJEMPLOS]
[pegar los 4 ejemplos del Paso 2]

[FORMATO]
Para cada correo nuevo devuelve JSON:
{ "id": <id>, "categoria": "...", "confianza": <0-1>, "razon": "<10 palabras>" }

[TAREA]
Clasifica el siguiente correo:
[pegar correo]
```

**Paso 4 — Mide la mejora.**

Hiciste un set de prueba con 20 correos reales que sabes la respuesta correcta. Resultados:

| Versión del prompt | Precisión |
|---|---|
| Zero-shot puro | 11/20 = 55% |
| Zero-shot con criterios | 14/20 = 70% |
| Few-shot 4 ejemplos | 19/20 = 95% |

El salto fue **de 70% a 95% al agregar 4 ejemplos**. El error restante (1 correo de un primo lejano clasificado como suscripción) se resuelve agregando un quinto ejemplo de "primo lejano que sí cuenta como familia".

**Paso 5 — Reflexión.**

¿Por qué few-shot funcionó tanto? Porque tu definición de las categorías es **personal y no estándar**. El modelo zero-shot aplicaba sus prejuicios genéricos. Few-shot le mostró tus prejuicios. Los modelos no leen mentes; aprenden de patrones.

> **Lección clave.** Para tareas con definiciones custom (no estándar), few-shot bate a cualquier prompt zero-shot por elaborado que sea. Regla de bolsillo: **si la tarea depende de TU criterio personal, dale ejemplos**.
::/practica

---

## Práctica resuelta — Cómo el chain-of-thought salvó un problema matemático mal respondido

::practica{titulo="Mismo problema, dos prompts: uno falla, el otro razona y acierta"}
**Problema.** Pruebas un problema clásico de tipo "fechas y edades" en tu plataforma:

> *"María tiene el doble de edad que tenía Pedro cuando ella tenía la edad que Pedro tiene ahora. La suma de sus edades actuales es 70 años. ¿Cuántos años tiene cada uno?"*

**Paso 1 — Prompt zero-shot puro.**

```
Resuelve: María tiene el doble de edad que tenía Pedro cuando ella tenía la
edad que Pedro tiene ahora. La suma de sus edades actuales es 70 años.
¿Cuántos años tiene cada uno?
```

Respuesta típica del modelo (sin CoT):

> *"María tiene 35 años y Pedro tiene 35 años."*

Está **mal**. La verificación falla: 35 + 35 = 70 ✓ pero no satisface "el doble de la edad que tenía Pedro cuando…".

**Paso 2 — Prompt con chain-of-thought explícito.**

```
Resuelve este problema paso a paso. Antes de dar la respuesta:

1. Define las variables (M, P para María y Pedro hoy).
2. Define los tiempos involucrados (hoy, hace cuántos años).
3. Plantea las dos ecuaciones del problema.
4. Resuélvelas algebraicamente mostrando cada paso.
5. Verifica numéricamente que la solución cumple las dos condiciones del enunciado.

Solo después de los 5 pasos, da la respuesta final.

PROBLEMA: María tiene el doble de edad que tenía Pedro cuando ella tenía
la edad que Pedro tiene ahora. La suma de sus edades actuales es 70 años.
¿Cuántos años tiene cada uno?
```

Respuesta típica con CoT:

> 1. Variables: M = edad María hoy, P = edad Pedro hoy.
> 2. Tiempo: hace t años, tal que María tenía P años → M − t = P → t = M − P.
> 3. En ese momento, Pedro tenía P − t = P − (M − P) = 2P − M.
> 4. Condición 1: M = 2 · (2P − M) → M = 4P − 2M → 3M = 4P → M = (4/3)P.
> 5. Condición 2: M + P = 70 → (4/3)P + P = 70 → (7/3)P = 70 → P = 30, M = 40.
> 6. Verificación: hace 10 años, María tenía 30 (la edad de Pedro hoy), Pedro tenía 20. Doble de 20 es 40 = edad de María hoy. ✓ Suma 30 + 40 = 70 ✓.
>
> **Respuesta:** María tiene 40 años, Pedro tiene 30.

**Paso 3 — Resultado.**

| Versión | ¿Acertó? | Tiempo de respuesta | Tokens consumidos |
|---|---|---|---|
| Zero-shot | NO | 2 s | ~50 |
| Con CoT | SÍ | 8 s | ~350 |

El CoT cuesta más (4× más tokens) pero **acertó**. Para un problema de matemáticas, ese costo es aceptable.

**Paso 4 — Cuándo NO usar CoT.**

CoT es contraproducente cuando:
- La pregunta es trivial (traducción palabra-palabra, aritmética básica).
- Quieres respuesta corta y casual.
- La tarea es creativa y el "razonamiento explícito" arruina el output.

> **Lección clave.** CoT es la técnica más rentable para matemáticas, lógica y razonamiento de varios pasos. Tu regla personal: **si te equivocaste con zero-shot en un problema cuantitativo, antes de dar el problema por imposible, pruébalo con CoT explícito**.
::/practica
