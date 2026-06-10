---
unidad: 4
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Pipeline de cápsula educativa multimedia

::practica{titulo="Genera una cápsula educativa de 60 segundos sobre el principio de Bernoulli aplicada al alerón F1"}
**Problema.** Tu profesor te pide entregar una cápsula educativa de 60 segundos sobre Bernoulli aplicado al alerón F1. 
- Debe incluir: voz narrando, imágenes ilustrativas, música de fondo y subtítulos. 
- Lo entregas mañana.

**Tu tarea:** ejecutar el pipeline completo usando IA generativa. 
**Tiempo estimado: 30 minutos.**

---

**Paso 1 — Guion (5 min).**

Pegas en ChatGPT/Claude:
- Eres copywriter educativo. 
- Genera guion para video de 60 s sobre Bernoulli aplicado al alerón F1, audiencia bachillerato. 
- Estructura: Hook (0-5 s), Explicación (5-30 s), Ejemplo F1 (30-50 s), CTA (50-60 s).
- Tono conversacional. Español neutro. ~150 palabras totales.

Output: guion listo. Lo refinas con 1-2 iteraciones.

---

**Paso 2 — Imágenes ilustrativas (8 min).**

Necesitas 6 imágenes (1 cada 10 s aprox). Generas en DALL·E 3 o Midjourney:
1. Coche F1 negro y naranja, vista lateral, alerón trasero destacado.
2. Diagrama del flujo de aire sobre alerón invertido.
3. Comparación: ala de avión arriba vs alerón F1 abajo.
4. Niño aprendiendo física frente a laptop.
5. Render 3D del coche F1 a alta velocidad con flechas de fuerza.
6. Logo Albatros estilizado al cierre.

> **Tiempo:** ~1 min por imagen. Si la primera no convence, iteras estilo o ángulo.

---

**Paso 3 — Voz narrada (3 min).**

Vas a ElevenLabs:
1. Eliges voz "Adam" o clonas la tuya.
2. Pegas el guion del paso 1.
3. Configuras: estabilidad 50, similitud 75.
4. Generas y descargas MP3.

> **Tiempo:** 30 segundos de generación, 1 min de configuración.

---

**Paso 4 — Música de fondo (3 min).**

En Suno:
1. Prompt: upbeat technology background music, electronic synthwave, 60 seconds, no vocals.
2. Generas y eliges la mejor opción.
3. Descargas MP3.

---

**Paso 5 — Avatar opcional (5 min).**

Si quieres tu cara hablando:
1. En HeyGen seleccionas avatar "Female teacher".
2. Pegas guion y eliges voz.
3. Generas video MP4 con avatar.
- Alternativa: Sora/Runway para clip de B-roll del coche F1 en pista.

---

**Paso 6 — Edición y montaje (10 min).**

En **CapCut** o **Descript**:
1. Importa: voz, música, imágenes y video B-roll.
2. Coloca voz como track principal y música a -20 dB.
3. Imágenes con cortes cada 8-10 s y zoom suave (Ken Burns).
4. Genera subtítulos automáticos.
5. Exporta MP4 1080p, 60 s.

---

**Paso 7 — Verificación (3 min).**

Antes de entregar:
- [ ] Voz se escucha clara.
- [ ] Imágenes coinciden con guion.
- [ ] Subtítulos sincronizados y logo visible.

---

**Resultado.** Cápsula educativa lista en ~30 min. 
- Sin IA esto sería 1 día de edición + 100 USD en stock + actor de voz.

> **Trampa común evitada.** No quieras que un solo modelo haga todo. Cada paso requiere la herramienta correcta. Piensa en pipeline.

::interioriza
Imagina que construyes un coche. No usas la misma máquina para hacer el motor, pintar la carrocería y coser los asientos. Cada herramienta tiene su especialidad. Un pipeline de IA es tu línea de ensamblaje multimedia.
::/interioriza

> **Verificación profesional.** Si preguntan qué hiciste tú: estructura, decisiones creativas y validación final. La IA hizo la generación; tú hiciste el criterio.

::pausa{}
**Reflexión activa:**
1. ¿Por qué es un error pedirle a ChatGPT que te devuelva el video ya montado?
2. ¿Qué rol asumes en el proceso: operador de herramientas o director creativo?
::/pausa
::/practica

---

## Práctica resuelta — De prompt de imagen vago a profesional con anatomía 5C

::practica{titulo="Lleva un prompt de imagen de v1 a v5 con anatomía sujeto + acción + estilo + iluminación + modificadores"}
**Problema.** Necesitas la portada para tu cápsula educativa: "agua escolar saludable".
- El prompt naive te dio una imagen mediocre.

**Paso 1 — Prompt v1 (zero-shot vago).**
- `Imagen de agua escolar saludable`
- Resultado: botella genérica, sin contexto. Score: 1/5.

**Paso 2 — Diagnostica las capas faltantes.**

| Capa | ¿Falta? | Diagnóstico |
|---|---|---|
| Sujeto | parcial | "agua escolar" es ambiguo |
| Acción/composición | SÍ | no hay escena ni encuadre |
| Estilo artístico | SÍ | asume default cualquiera |
| Iluminación/cámara | SÍ | no hay tono |
| Modificadores técnicos | SÍ | sin resolución |

**Paso 3 — Itera capa por capa.**

- **v2 (Sujeto + acción):** "Estudiantes en patio llenando termos..." Score: 2/5.
- **v3 (Estilo):** "...estilo ilustración 2D Pixar..." Score: 3/5.
- **v4 (Luz):** "...luz de mediodía, cámara a la altura de los niños..." Score: 4/5.
- **v5 (Técnicos):** "...8K, render PBR, --ar 16:9..." Score: 5/5.

**Prompt final v5:**
- `Estudiantes de primaria en patio de escuela pública mexicana llenando termos... Estilo ilustración 2D Pixar... Luz de mediodía... 8K, alto detalle, render PBR... --ar 16:9`

**Paso 4 — Evolución del score.**

| Versión | Capas presentes | Score visual (1-5) | Aspecto crítico |
|---|---|---|---|
| v1 | 1 | 1 | sin contexto |
| v5 | 5 | 5 | listo para portada |

**Paso 5 — Lección y banco.**

- Ahorraste **45 minutos** porque cada iteración añadió **una sola capa**.
- Si hubieras escrito v5 directo, habrías tardado 15 minutos en descubrir qué faltaba.

::interioriza
Un prompt de 5 capas es como preparar una hamburguesa perfecta. Si echas todos los ingredientes a la vez sin orden, obtienes un desastre. Capa por capa (pan, carne, queso, lechuga, salsas) controlas el resultado final.
::/interioriza

> **Lección clave.** El prompting visual requiere anatomía explícita e iteración capa por capa. Pon los parámetros técnicos en tu banco y reutilízalos.

::pausa{}
**Reflexión activa:**
1. ¿Qué pasaría si intentas ajustar el estilo artístico antes de tener claro el sujeto y la acción?
2. ¿Por qué guardar tus modificadores técnicos es vital para la velocidad?
::/pausa
::/practica

---

## Práctica resuelta — Cómo le saqué un audio overview a un PDF de 200 páginas en 5 minutos

::practica{titulo="Convierte un PDF académico en un podcast tipo NotebookLM y úsalo para estudiar caminando"}
**Problema.** Tienes un PDF de 200 páginas sobre IA para Filosofía.
- No tienes 6 horas para leerlo. 
- Quieres un podcast de 15 minutos para escucharlo caminando.

**Paso 1 — Sube el PDF a NotebookLM.**
- Ve a NotebookLM → New Notebook → Upload Source.
- Arrastra el PDF y espera a que indexe.

**Paso 2 — Verifica el indexado.**
- Haz **una pregunta de control** antes de generar audio.
- Ejemplo: "¿Qué dice sobre el invierno de IA de los 70?". 
- Si responde bien, indexó correctamente.

**Paso 3 — Configura el audio overview.**
- Busca el botón "Audio Overview" → "Generate".
- Usa el modo customizado y pide foco específico, tono y audiencia.
- Ejemplo: "Audiencia bachillerato, foco en hitos 1950-2025, 15 min."

**Paso 4 — Espera y descarga.**
- Tarda 2-4 minutos en generar. 
- Descarga el audio en MP3.

**Paso 5 — Auditoría de calidad.**
- Escucha los primeros 60 segundos y el final.
- Salta al medio para revisar temas intermedios.
- Verifica 2 datos puntuales comparando con el PDF.

**Paso 6 — Resultado.**

| Métrica | Lectura | Audio |
|---|---|---|
| Tiempo | 6 horas | 15 minutos |
| Comprensión | 8 | 6 |
| Coste | tu tiempo | gratis |

**Paso 7 — Cuándo NO sustituye lectura.**
- Si serás examinado en detalles técnicos o fórmulas.
- Si necesitas citar literalmente (el audio interpreta).
- Úsalo como **primera capa** para luego leer con foco.

::interioriza
El audio overview es como ver el tráiler de una película antes de ir al cine. Te da el panorama, los personajes y la trama principal, preparándote para entender mejor los detalles de la obra completa.
::/interioriza

> **Lección clave.** Multimodalidad no es solo crear contenido nuevo, es transformar el existente al formato que mejor te sirva.

::pausa{}
**Reflexión activa:**
1. ¿Por qué es crucial hacer una pregunta de control antes de generar el audio?
2. ¿En qué escenario académico el audio overview sería insuficiente por sí solo?
::/pausa
::/practica
