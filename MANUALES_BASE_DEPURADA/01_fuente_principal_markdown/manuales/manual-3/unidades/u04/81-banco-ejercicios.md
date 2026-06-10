---
unidad: 4
seccion: banco-ejercicios
paginas_objetivo: 2
---

## Banco de ejercicios — Unidad 04

> Banco de práctica multimodal:
> - Combina imagen, video, audio y análisis de documentos.
> - Privilegia **redacción de prompts visuales** y **decisiones de herramienta**.
> - Detecta **limitaciones**. Resuelve siempre antes de mirar la clave.

::interioriza
**Elegir la IA correcta es como abrir una caja de herramientas:**
No usas un martillo para apretar un tornillo. 
Igualmente, no usas ChatGPT para clonar tu voz, ni Midjourney para generar textos largos.
Conocer la herramienta exacta te ahorra horas de frustración.
::

::pausa{}
**Reflexiona antes de empezar:**
- ¿Qué harías si necesitas una imagen con texto perfectamente legible?
- ¿Qué herramienta te da más control: una open source o una en la nube?
::

---

### Bloque A — Imagen (4.1)

::act-mcq{titulo="Generadores de imagen — repaso"}
1. Si necesitas una imagen para un **logo comercial** que jamás genere problemas legales, eliges:
   - [ ] DALL·E 3
   - [ ] Midjourney v6
   - [x] Adobe Firefly (entrenado solo con Adobe Stock licenciado)
   - [ ] Stable Diffusion XL

2. Para una **ilustración estilo cinematográfico ultradetallada** con paleta artística, brilla más:
   - [x] Midjourney v6
   - [ ] DALL·E 3
   - [ ] Stable Diffusion 1.5
   - [ ] Adobe Firefly

3. Para iterar **localmente sin pagar y con control técnico (LoRAs, ControlNet)**:
   - [ ] DALL·E 3
   - [ ] Midjourney v6
   - [x] Stable Diffusion (open source)
   - [ ] Firefly
::/act-mcq

::act-fill{titulo="Anatomía de un prompt de imagen"}
Un prompt de imagen profesional tiene 5 capas: 
- **sujeto** y **acción/composición**.
- **estilo artístico** e **iluminación/cámara**.
- **modificadores técnicos**.

Redacta el prompt para "estudiante de bachillerato leyendo bajo un árbol con luz dorada del atardecer, estilo Pixar 3D":

- Sujeto: _____________________________________________________________________
- Acción/composición: _________________________________________________________
- Estilo: _____________________________________________________________________
- Iluminación/cámara: _________________________________________________________
- Modificadores técnicos: _____________________________________________________
::/act-fill

::act-tf{titulo="Mitos sobre imagen generativa"}
1. Las manos en imagen IA ya son perfectas en 2025. ( ) ____________
2. DALL·E 3 puede generar texto legible dentro de la imagen. ( ) ____________
3. La regla del aspect ratio es: 1:1 redes, 16:9 video, 9:16 vertical. ( ) ____________
4. Stable Diffusion requiere GPU para correr localmente con velocidad razonable. ( ) ____________
5. Si una imagen IA se parece mucho a una obra famosa, NO importa porque es generada. ( ) ____________
::/act-tf

---

### Bloque B — Video (4.2)

::act-case{titulo="Decide herramienta de video para 4 escenarios" lineas=10}
Para cada escenario indica qué herramienta usarías y por qué:

1. Necesitas un avatar hablante con tu clon facial para un curso de inglés en YouTube.
2. Quieres un clip de 8 segundos cinematográfico de un coche F1 derrapando para abrir un video.
3. Tienes que generar 30 escenas cortas para un cuento infantil.
4. Necesitas un video corporativo donde un avatar genérico (no tú) presente datos de tu empresa.
::/act-case

::act-mcq{titulo="Limitaciones de video generativo"}
1. La limitación **más común** de Sora/Veo/Runway en 2025 es:
   - [ ] Resolución (ya alcanza 4K)
   - [x] Coherencia entre cortes y consistencia de personajes
   - [ ] No pueden generar agua
   - [ ] No pueden generar humanos

2. ¿Cuál herramienta tiene control fino (frame-by-frame, keyframes)?
   - [ ] Sora (consumer)
   - [x] Runway Gen-3 con Director Mode
   - [ ] Veo
   - [ ] Synthesia
::/act-mcq

---

### Bloque C — Audio y voz (4.3)

::act-match{titulo="Relaciona necesidad con herramienta de audio"}
| Necesidad | Herramienta |
|---|---|
| 1. Transcribir 2 h de clase grabada | a) Suno |
| 2. Clonar tu voz y hacerla narrar texto | b) Whisper |
| 3. Generar canción de 2 min con letra propia | c) ElevenLabs |
| 4. Editar podcast eliminando muletillas en transcript | d) Descript |
| 5. Mejorar audio ruidoso de una grabación de celular | e) Adobe Podcast Enhance |
::/act-match

::act-fill{titulo="ElevenLabs y Whisper en la práctica"}
- ElevenLabs requiere mínimo _____________ de voz para clonarla con calidad. 
- "Voice Lab" ajusta parámetros como _____________, _____________ y _____________. 
- Whisper es _____________ (modelo de OpenAI en _____________ como open source). 
- Soporta transcripción en _____________ idiomas. 
- Para uso local, instalas la versión _____________ o usas el wrapper _____________.
::/act-fill

---

### Bloque D — Documentos (4.4)

::act-tf{titulo="Análisis de documentos con IA"}
1. Subir un PDF a Claude/ChatGPT lo lee página por página secuencialmente. ( ) ____________
2. NotebookLM puede generar un audio overview tipo podcast a partir de tus PDFs. ( ) ____________
3. Si tu PDF tiene OCR malo, el modelo lo arregla automáticamente. ( ) ____________
4. ChatGPT con visión puede leer imágenes pegadas en el chat (capturas, fotos de pizarrón). ( ) ____________
5. Para PDFs de más de 500 páginas, lo más eficaz es subirlos completos a un solo chat. ( ) ____________
::/act-tf

::act-order{titulo="Ordena el flujo de análisis de un PDF académico"}
[ ] Define qué pregunta específica buscas responder (no "resumen general")
[ ] Sube el PDF a tu plataforma con contexto largo (Claude, NotebookLM, Gemini)
[ ] Verifica que el OCR del PDF sea legible (si no, conviértelo)
[ ] Pide al modelo que cite página y párrafo de cada respuesta
[ ] Verifica al menos 2 citas abriendo el PDF en la página citada
[ ] Documenta los hallazgos en un mapa mental o resumen estructurado
::/act-order

---

## Clave de respuestas

**Bloque A**
- **MCQ:** 1-c · 2-a · 3-c. 
- **Fill:** sujeto="estudiante...", acción="sentado...", estilo="Pixar 3D...", iluminación="luz dorada...", modificadores="8K...". 
- **V/F:** 1-F · 2-V · 3-V · 4-V · 5-F (hay riesgos legales).

**Bloque B**
- **Caso:** 1) HeyGen/Synthesia. 2) Runway Gen-3. 3) Sora o Veo. 4) Synthesia. 
- **MCQ:** 1-b · 2-b.

**Bloque C**
- **Match:** 1-b · 2-c · 3-a · 4-d · 5-e. 
- **Fill:** 1-3 minutos · estabilidad · claridad · estilo · open source · 2022 · 99 · whisper · WhisperX o pyannote.

**Bloque D**
- **V/F:** 1-F · 2-V · 3-F · 4-V · 5-F (lost-in-the-middle). 
- **Order:** define pregunta → verifica OCR → sube → pide citas → verifica citas → documenta.
