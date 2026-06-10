---
unidad: 4
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Pipeline de cápsula educativa multimedia

::practica{titulo="Genera una cápsula educativa de 60 segundos sobre el principio de Bernoulli aplicada al alerón F1"}
**Problema.** Tu profesor te pide entregar una "cápsula educativa" de 60 segundos sobre Bernoulli aplicado al alerón F1. Debe incluir: voz narrando, imágenes ilustrativas, música de fondo, subtítulos. Lo entregas mañana.

**Tu tarea:** ejecutar el pipeline completo usando IA generativa. **Tiempo estimado: 30 minutos.**

---

**Paso 1 — Guion (5 min).**

Pegas en ChatGPT/Claude:

```
Eres copywriter educativo. Genera guion para video de 60 s sobre Bernoulli
aplicado al alerón F1, audiencia bachillerato. Estructura:
- Hook (0-5 s): pregunta gancho.
- Explicación (5-30 s): concepto + analogía.
- Ejemplo F1 (30-50 s): cómo funciona el alerón.
- CTA (50-60 s): "comparte si entendiste, sigue para más".
Tono conversacional. Español neutro. ~150 palabras totales.
```

Output: guion listo. Lo refinas con 1-2 iteraciones.

---

**Paso 2 — Imágenes ilustrativas (8 min).**

Necesitas 6 imágenes (1 cada 10 s aprox). Generas en DALL·E 3 (vía ChatGPT) o Midjourney:

1. *"Coche F1 negro y naranja, vista lateral, alerón trasero destacado, pista difuminada, render 3D fotorrealista, paleta tecno"*
2. *"Diagrama del flujo de aire sobre alerón invertido, líneas de corriente azules, presión menor abajo, estilo educativo limpio"*
3. *"Comparación lado a lado: ala de avión arriba (sustentación) vs alerón F1 abajo (downforce), ilustración técnica"*
4. *"Niño aprendiendo física frente a laptop, pizarrón con fórmulas detrás, estilo Pixar warm"*
5. *"Render 3D del coche F1 a alta velocidad con flechas amarillas mostrando fuerza hacia el piso"*
6. *"Logo Albatros estilizado al cierre, paleta azul-naranja"*

> **Tiempo:** ~1 min por imagen. Si la primera no convence, iteras (cambias estilo, ángulo).

---

**Paso 3 — Voz narrada (3 min).**

Vas a ElevenLabs:
1. Eliges voz "Adam" (o clonas la tuya con 3 min de muestra previa).
2. Pegas el guion del paso 1.
3. Configuras: estabilidad 50, similitud 75, velocidad normal.
4. Generas. Descargas MP3.

> **Tiempo:** 30 segundos de generación, 1 min de configuración.

---

**Paso 4 — Música de fondo (3 min).**

En Suno:
1. Prompt: *"upbeat technology background music, electronic synthwave, energetic but not distracting, 60 seconds, no vocals"*.
2. Generas. Eliges la mejor de 2 opciones.
3. Descargas MP3.

> **Tiempo:** 30 s de generación.

---

**Paso 5 — Avatar opcional (5 min).**

Si quieres tu cara hablando:
1. En HeyGen seleccionas avatar "Female teacher" o subes 2 min de tu video.
2. Pegas guion.
3. Eliges voz (en español neutro).
4. Generas video MP4 con avatar.

Alternativa: **Sora/Runway** para clip de 8 s del coche F1 en pista para B-roll.

---

**Paso 6 — Edición y montaje (10 min).**

En **CapCut** (gratuito) o **Descript**:
1. Importa: voz narrada, música, 6 imágenes, video B-roll.
2. Coloca voz como track principal.
3. Música como fondo a -20 dB.
4. Imágenes en el video con cortes cada 8-10 s, con zoom suave (Ken Burns).
5. Si tienes avatar HeyGen, lo intercalas en momentos clave.
6. Genera **subtítulos automáticos** (CapCut tiene función AI; Whisper si Descript).
7. Exporta MP4 1080p, 60 s.

---

**Paso 7 — Verificación (3 min).**

Antes de entregar:
- [ ] Voz se escucha clara.
- [ ] Imágenes coinciden con guion.
- [ ] Música no tapa voz.
- [ ] Subtítulos sincronizados.
- [ ] Duración entre 55-65 s.
- [ ] Logo final visible.

---

**Resultado.** Cápsula educativa lista. **Tiempo total: ~30 min.** Sin IA esto sería 1 día completo de edición + 100 USD en stock + actor de voz.

> **Trampa común evitada.** No quieras que un solo modelo haga todo. Cada paso requiere la herramienta correcta: texto (LLM), imagen (DALL·E), voz (ElevenLabs), música (Suno), edición (CapCut). Piensa en pipeline.

> **Verificación profesional.** Si lo entregas y el profesor pregunta "¿qué hiciste tú versus la IA?", la respuesta correcta es: **estructura, decisiones creativas, validación final**. La IA hizo la generación; tú hiciste el criterio.
::/practica

---

## Práctica resuelta — De prompt de imagen vago a profesional con anatomía 5C

::practica{titulo="Lleva un prompt de imagen de v1 a v5 con anatomía sujeto + acción + estilo + iluminación + modificadores"}
**Problema.** Necesitas la imagen de portada para tu próxima cápsula educativa: "agua escolar saludable" (proyecto del case study del Manual de Química, pero te sirve como ejercicio). El prompt naive te dio una imagen mediocre.

**Paso 1 — Prompt v1 (zero-shot vago).**

```
Imagen de agua escolar saludable
```

Resultado: una botella genérica con fondo blanco. Cero contexto educativo, cero personalidad. Score visual: 1/5.

**Paso 2 — Diagnostica las capas faltantes.**

| Capa | ¿Está en v1? | ¿Qué falta? |
|---|---|---|
| Sujeto | parcial | "agua escolar" es ambiguo |
| Acción/composición | NO | no hay escena, no hay encuadre |
| Estilo artístico | NO | DALL·E asume default cualquiera |
| Iluminación/cámara | NO | no hay tono |
| Modificadores técnicos | NO | sin resolución, sin aspect ratio |

**Paso 3 — Itera capa por capa.**

**v2 — Sujeto + acción.** "Estudiantes en patio de escuela mexicana llenando termos en bebedero metálico, expresiones contentas, ambiente de recreo." Score: 2/5 (mejor pero plano).

**v3 — Agrego estilo.** "...estilo ilustración 2D Pixar, paleta azul-naranja Albatros." Score: 3/5 (ya tiene personalidad).

**v4 — Agrego iluminación y cámara.** "...luz de mediodía mexicano cálido, cámara a la altura de los niños, profundidad de campo media, fondo difuminado con árboles." Score: 4/5 (cinemático).

**v5 — Modificadores técnicos.** "...8K, alto detalle, render PBR, --ar 16:9, --style raw, --no texto, sin marcas comerciales." Score: 5/5.

**Prompt final v5:**

```
Estudiantes de primaria en patio de escuela pública mexicana llenando termos
en bebedero metálico, expresiones contentas, ambiente de recreo. Estilo
ilustración 2D Pixar, paleta azul-naranja Albatros. Luz de mediodía mexicano
cálido, cámara a la altura de los niños, profundidad de campo media, fondo
difuminado con árboles del patio. 8K, alto detalle, render PBR, sin texto,
sin marcas comerciales. --ar 16:9 --style raw
```

**Paso 4 — Evolución del score.**

| Versión | Capas presentes | Score visual (1-5) | Aspecto crítico |
|---|---|---|---|
| v1 | 1 (sujeto vago) | 1 | sin contexto |
| v2 | 2 | 2 | sin estilo |
| v3 | 3 | 3 | sin atmósfera |
| v4 | 4 | 4 | sin pulido técnico |
| v5 | 5 | 5 | listo para portada |

**Paso 5 — Lección y banco.**

Ahorraste **45 minutos** porque cada iteración añadió **una sola capa**. Si hubieras escrito v5 directamente en el primer intento, te habría tomado 15 minutos descubrir qué faltaba; y si hubieras seguido cambiando todo a la vez, no habrías sabido qué movía la aguja.

> **Lección clave.** El prompting visual sigue exactamente la misma regla del prompting textual: **anatomía explícita + iteración capa por capa**. Tu mente no inventa "8K, render PBR" sola; la pones en el banco una vez y la reutilizas siempre.
::/practica

---

## Práctica resuelta — Cómo le saqué un audio overview a un PDF de 200 páginas en 5 minutos

::practica{titulo="Convierte un PDF académico en un podcast tipo NotebookLM y úsalo para estudiar caminando"}
**Problema.** Tienes un PDF de 200 páginas sobre "historia de la inteligencia artificial" que tu profesor de Filosofía de la Tecnología pidió leer. No tienes 6 horas para leerlo. Quieres convertirlo en un podcast de 15 minutos para escucharlo mientras caminas al trabajo.

**Paso 1 — Sube el PDF a NotebookLM.**

Ve a https://notebooklm.google.com → New Notebook → Upload Source → arrastra el PDF. Espera 30 segundos a que indexe.

**Paso 2 — Verifica el indexado.**

Antes de generar el audio, haz **una pregunta de control** al notebook: "¿Qué dice el documento sobre el invierno de IA de los 70?". Si responde con cita de página correcta, indexó bien. Si dice "no encuentro información", el PDF puede estar mal escaneado u OCR roto.

**Paso 3 — Configura el audio overview.**

En NotebookLM, busca el botón "Audio Overview" → "Generate". Hay dos modos:

- **Modo deep dive** (default): podcast tipo conversación entre 2 hosts, 8-15 min.
- **Modo customizado:** puedes pedir foco específico ("céntrate en hitos 1990-2025"), tono ("académico", "casual"), audiencia ("estudiantes de bachillerato").

Para tu caso, elige el modo customizado y pide:

```
Audiencia: estudiante de bachillerato sin background técnico.
Tono: conversacional, con analogías cotidianas.
Foco: los 5 hitos más relevantes desde 1950 hasta 2025.
Duración objetivo: 15 minutos.
Idioma: español si la versión soporta, si no inglés con velocidad lenta.
```

**Paso 4 — Espera y descarga.**

NotebookLM tarda 2-4 minutos en generar. Cuando termina, te da un audio reproducible y descargable en MP3.

**Paso 5 — Auditoría de calidad.**

Antes de confiar el audio:

- Escucha los **primeros 60 segundos**: ¿está coherente con el documento?
- Salta al **medio**: ¿menciona temas del medio del PDF?
- Escucha el **final**: ¿cierra el contenido?
- Verifica **2 datos puntuales** abriendo el PDF y comparando.

**Paso 6 — Resultado.**

| Métrica | Lectura tradicional | Audio overview |
|---|---|---|
| Tiempo | 6 horas | 15 minutos |
| Comprensión profunda (1-10) | 8 | 6 |
| Recordación a 1 semana | 5 | 7 (auditivo se memoriza distinto) |
| Esfuerzo | alto | medio (puedes caminar) |
| Coste | tu tiempo | gratis |

**Paso 7 — Cuándo NO sustituye lectura.**

El audio overview **no reemplaza** la lectura cuando:
- Vas a ser examinado sobre detalles técnicos específicos.
- El PDF tiene fórmulas matemáticas o tablas de datos.
- Necesitas citar literalmente (el audio interpreta, no transcribe).

Para esos casos, usa el audio como **primera capa** y luego lee con foco las secciones críticas.

> **Lección clave.** Multimodalidad **no es solo generar contenido nuevo**, es también **transformar formato** existente. El mismo PDF puede ser texto, audio, mapa mental, infografía. Cada formato te conviene en un momento distinto del estudio.
::/practica
