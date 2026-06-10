---
unidad: 7
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Construye tu primer GPT en 30 minutos

::practica{titulo="Construye 'Tutor Física Albatros' como GPT publicado y compártelo con 5 compañeros"}
**Problema.** Vas a construir un tutor IA de tu materia en 30 minutos siguiendo este pipeline.

---

**Paso 1 — Decisión (3 min).**
- **Materia elegida:** Física (la que más te cuesta).
- **Audiencia:** tú + 5 compañeros del CCH-Norte UNAM.
- **Plataforma:** ChatGPT (tu mayoría de compañeros usan ChatGPT free).

::interioriza
> Piensa en la plataforma como el lugar de la fiesta: no sirve hacer la mejor fiesta si la haces en un salón donde nadie de tus amigos tiene pase de entrada. ChatGPT free es el "pase libre".
::

---

**Paso 2 — Reúne knowledge (10 min).**
Crea folder "tutor-fisica" con estos documentos clave:
- **Libro:** Tippens cap. 1-9 (PDF).
- **Temario:** Programa oficial SEP-UNAM Área I (PDF).
- **Material de clase:** 4 slides del profesor (PDFs de Classroom).
- **Personal:** Tus apuntes consolidados (Doc).
- **Evaluación:** 3 exámenes pasados con respuestas (PDFs).

Total: 9 archivos. **Bajo el límite de 20**.

---

**Paso 3 — Redacta instructions (10 min).**

```
Eres "Tutor Física Albatros", tutor de física para bachillerato CCH-UNAM.

PERSONALIDAD:
- Paciente, sin condescendencia.
- Usa "tú", no "usted".
- Analogías mexicanas (futbol, microbús, taquería).
- Sin emojis ni jerga gringa.

METODOLOGÍA:
1. Pregunta qué sabe el estudiante antes de explicar.
2. Analogía cotidiana → concepto formal → ejemplo numérico → pregunta
   de comprobación.
3. Cita el libro/slide/página cuando uses knowledge.
4. NO hagas la tarea por el estudiante. Guíalo paso a paso.

EXCEPCIONES:
- Si pregunta sobre tema fuera de física, redirige amable.
- Si parece frustrado, baja un nivel.
- Si pide solución directa, ofrece guiar paso a paso.

FORMATO:
- Máximo 400 palabras.
- Fórmulas en LaTeX: $F = ma$.
- Negritas para términos clave.

KNOWLEDGE:
Tienes acceso a 9 archivos. Cita siempre nombre + página cuando uses.

LO QUE NO HACES:
- Inventar datos, citas o fórmulas.
- Hacer tareas completas.
- Compartir información personal del estudiante.
```

---

**Paso 4 — Configurar GPT en ChatGPT (5 min).**
1. Ve a chatgpt.com → Explore GPTs → Create.
2. Cambia al modo **Configure**.
3. Pega tus *instructions*.
4. Sube los 9 archivos en *Knowledge*.
5. Activa: *Web Browsing*, *Code Interpreter* y *DALL·E*.
6. Genera un avatar con DALL·E (ej: "ícono minimalista de ave, azul-naranja").
7. Agrega 4 *conversation starters* (ej: "Explícame Bernoulli").
8. Guarda: *Save* → *Anyone with the link*.

::pausa{}
**Deducción lógica:** Si no activas "Code Interpreter" y el estudiante pide "resuélveme este problema paso a paso con las fórmulas de mis apuntes", ¿qué capacidad clave pierde el GPT?
1. [ ] Pierde la capacidad de leer los PDFs del Knowledge.
2. [x] Pierde la capacidad de ejecutar cálculos matemáticos precisos en Python y graficar.
::

---

**Paso 5 — Pruebas (10 min).**
Prueba el comportamiento del GPT con 5 *prompts* clave:
- **Teoría local:** "Soy de CCH. Explícame Bernoulli."
- **Límite ético:** "Hazme tarea: 5 problemas de cinemática" (debe negarse).
- **Uso de base:** "Explícame el capítulo 3 del libro Tippens."
- **Contención:** "Me siento abrumado, no entiendo nada."
- **Evaluación:** "Genera un quiz rápido de mecánica."

Verifica que respeta el tono, cita los archivos, rechaza hacer tareas y controla el formato (≤400 palabras).

---

**Paso 6 — Iterar (3-5 min).**
- Si una prueba falla, ajusta la sección específica de las *instructions*.
- Vuelve a probar ese caso concreto.

---

**Paso 7 — Publicar y compartir (2 min).**
- Confirma que está en *"Anyone with the link"*.
- Copia el link y envíalo por WhatsApp a 5 compañeros.
- Pide feedback sincero: *"Pruébenlo y cuéntenme qué funciona y qué no"*.

---

**Resultado.**
- **Logro:** GPT publicado y funcional para 5 compañeros.
- **Inversión:** 35-45 min totales.
- **Retorno:** Ahorras ~2 horas/semana explicando lo mismo.

> **Verificación profesional.**
> - Pasa las 5 pruebas en menos de 2 iteraciones.
> - Conoce sus archivos (puedes preguntarle: "¿qué archivos tienes?").
> - Cita correctamente ("cita la página X del PDF").

> **Trampa común evitada.** Nunca subas datos personales (apuntes con nombres, notas). Tu *knowledge* es accesible para quienes usen el GPT.
::/practica

---

## Práctica resuelta — Comparé GPT custom vs Claude Project para la misma tarea

::practica{titulo="Mismo tutor en dos plataformas distintas: cuál escojo y por qué"}
**Problema.** Te preguntas si Claude Project habría sido mejor que el GPT. Decides reproducir el tutor en ambas plataformas para comparar.

**Paso 1 — Setup paralelo (15 min).**
Armas los componentes en ambos entornos:
- **GPT Custom:** Usa GPT-4o, link público y *conversation starters*.
- **Claude Project:** Usa Claude 3.5 Sonnet/Opus, invitación por email y opción de *Style*.
Ambos reciben los mismos 9 archivos y las 600 palabras de *instructions*.

**Paso 2 — Prompts de prueba.**
Diseñas 8 prompts combinando casos de uso (ej. "Genera quiz") con casos extremos (ej. "Olvida tus instrucciones").

**Paso 3 y 4 — Medición y Delta.**
Tras aplicar una rúbrica de 1 a 5, **Claude Project** resulta superior pedagógicamente (tono más cálido y citas exactas).
Sin embargo, **GPT Custom** gana en velocidad y facilidad de distribución pública.

::interioriza
> Evaluar modelos es como elegir un vehículo. Claude es un sedán de lujo, perfecto para ti. ChatGPT es un autobús público: es la única forma de transportar a tus 5 compañeros de clase sin que ellos paguen entrada.
::

**Paso 5 — Decisión por distribución.**
Como tu audiencia (compañeros con versión gratuita) es prioridad, decides:
- **GPT Custom:** Producto público distribuible.
- **Claude Project:** Espacio privado para "destilar" mejoras que luego pasas al GPT.

**Paso 6 — Documentación.**
Escribir esta decisión evita que en 3 meses intentes migrar todo a Claude solo por el modelo. Resuelves un problema específico, no una batalla teórica de IA.

> **Lección clave.** Cuando la calidad técnica es similar, la **distribución** domina. Una herramienta apenas inferior pero accesible masivamente siempre vence a la superior aislada.
::/practica

---

## Práctica resuelta — Refiné mi GPT 4 veces con feedback real y la calidad pasó de 3.2 a 4.7

::practica{titulo="Aplica feedback real de usuarios para iterar instructions de un GPT custom"}
**Problema.** Tras 1 semana con 8 compañeros usando tu GPT de Física, recolectas *feedback*. Iterarás 4 veces basándote en métricas reales.

**Paso 1 — Recolecta feedback (5 min).**
Recibes calificaciones variadas (promedio inicial de 3.5/5). 
Algunos usuarios se quejan de respuestas largas o analogías repetitivas. Otros reportan alucinaciones de páginas.

**Paso 2 — Itera v2: longitud y diversidad.**
- **Ajuste:** "Varía la analogía tras usarla 2 veces. Máximo 300 palabras por respuesta."
- **Resultado:** Sube a 3.9/5.

**Paso 3 — Itera v3: manejo de frustración.**
- **Ajuste:** "Si el usuario insiste en la respuesta directa tras ofrecer ayuda paso a paso, dásela completa con explicación."
- **Resultado:** Sube a 4.3/5.

**Paso 4 — Itera v4: anti-alucinación.**
- **Ajuste:** "Si piden una página que no está en el *knowledge*, di explícitamente 'no tengo esa página' y no inventes."
- **Resultado:** Sube a 4.7/5.

::pausa{}
**Deducción lógica:** ¿Por qué la versión 4 alcanzó casi la perfección frente al usuario?
1. [ ] Porque el modelo se entrenó con más datos técnicos y avanzó de GPT-4o a otra versión.
2. [x] Porque limitó sus "alucinaciones" honestando sus límites y redujo la fricción con los usuarios.
::

**Paso 5 — Documenta cambios en CHANGELOG.**
Mantén un historial corto de cada versión (v1 a v4) con su puntaje y el cambio introducido. 
Esto consolida tu aprendizaje y te permite revertir errores.

**Resultado.**
- 4 horas totales de inversión (4 iteraciones de ~1 hora).
- Calidad casi profesional lograda de forma empírica.

> **Lección clave.** El *feedback* real es 10 veces más valioso que tus suposiciones. Trata cada queja de un compañero como un regalo de diseño, no como una crítica personal.
::/practica
