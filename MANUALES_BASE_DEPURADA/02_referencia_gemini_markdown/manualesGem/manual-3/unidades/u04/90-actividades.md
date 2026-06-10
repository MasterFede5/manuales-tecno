---
unidad: 4
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 04

---

::act-mcq{titulo="Multimodal — repaso"}
1. ¿Qué generador de imagen tiene **licencia comercial limpia** porque solo se entrenó con Adobe Stock?
   - [ ] DALL·E 3
   - [ ] Midjourney v6
   - [x] Adobe Firefly
   - [ ] Stable Diffusion XL

2. La duración máxima típica de un video generado por Sora en 2025 es:
   - [ ] 5 segundos
   - [ ] 30 segundos
   - [x] 60 segundos
   - [ ] 5 minutos

3. ¿Qué herramienta usarías para clonar tu voz y narrar texto en otro idioma?
   - [ ] Sora
   - [ ] Whisper
   - [x] ElevenLabs
   - [ ] Suno

4. La función principal de Whisper es:
   - [ ] Generar voz desde texto
   - [x] Transcribir audio a texto en 99 idiomas
   - [ ] Generar música
   - [ ] Editar video

5. ¿Cuál NO es una limitación común de los videos generados por IA en 2025?
   - [ ] Coherencia entre cortes
   - [ ] Texto dentro del video
   - [x] Resolución máxima de 720p
   - [ ] Manos y dedos
::/act-mcq

---

::act-table{titulo="Mapa de herramientas multimedia"}
| Necesidad | Herramienta principal | Plan recomendado | Tiempo de generación |
|---|---|---|---|
| Imagen para infografía |  |  |  |
| Video con avatar hablante |  |  |  |
| Música de fondo libre |  |  |  |
| Transcribir clase grabada |  |  |  |
| Resumir PDF de 100 pp |  |  |  |
| Clonar mi voz para idioma extranjero |  |  |  |
::/act-table

---

::act-match{titulo="Relaciona herramienta con función"}
| Herramienta | Función principal |
|---|---|
| 1. Sora | a) Música desde texto |
| 2. ElevenLabs | b) Edición de audio/video por texto |
| 3. Suno | c) Voz sintética + clonación |
| 4. Whisper | d) Avatar hablante con clonación de rostro |
| 5. Descript | e) Video text-to-video calidad cinematográfica |
| 6. HeyGen | f) Transcripción de audio multilingüe |
::/act-match

---

::act-tf{titulo="Verdadero o falso (justifica)"}
1. Todos los modelos de imagen IA permiten uso comercial sin restricciones. ( ) ____________________________________________
2. Sora puede generar videos de 10 minutos en una sola toma. ( ) ____________________________________________
3. Whisper es gratuito y open source. ( ) ____________________________________________
4. ElevenLabs puede clonar tu voz con solo 5 minutos de muestra. ( ) ____________________________________________
5. Adobe Firefly tiene licencia limpia porque solo se entrenó con imágenes Adobe Stock. ( ) ____________________________________________
6. La calidad de las manos en imagen IA ya es perfecta en 2025. ( ) ____________________________________________
::/act-tf

---

::act-fill{titulo="Completa el pipeline multimedia"}
Para crear una cápsula educativa de 60 segundos, sigues 6 pasos:
1. Genera el _____________ con un LLM (ChatGPT, Claude).
2. Genera _____________ con DALL·E o Midjourney.
3. Convierte texto en _____________ con ElevenLabs.
4. Genera música de fondo con _____________.
5. Si quieres avatar hablante, usas _____________.
6. Editas y montas en _____________ o Descript.

La función _____________ de Descript permite editar audio/video escribiendo en el transcript. La herramienta open source _____________ transcribe audio en 99 idiomas gratis.
::/act-fill

---

::act-order{titulo="Ordena los pasos del pipeline cápsula educativa"}
[ ] Editar y montar en CapCut o Descript con cortes cada 8-10 s
[ ] Escribir guion con LLM (60 s = ~150 palabras)
[ ] Generar 6 imágenes ilustrativas con DALL·E o Midjourney
[ ] Generar voz narrada con ElevenLabs
[ ] Generar música de fondo con Suno
[ ] Verificar duración, sincronización y calidad antes de exportar
::/act-order

---

::albatros{titulo="Construye tu cápsula educativa multimedia de 60 s" tipo="taller" tiempo="90 min"}
**Pregunta detonadora.** ¿Puedes producir contenido educativo profesional en 1 hora usando solo IA generativa?

**Lo que harás.**
1. Elige un tema de tu materia favorita (1-2 conceptos clave).
2. Sigue el pipeline de la práctica resuelta paso a paso.
3. Genera: guion, 6 imágenes, voz, música, opcionalmente avatar HeyGen.
4. Edita en CapCut o Descript (60 s exacto).
5. Exporta MP4 con subtítulos.
6. Publica en redes (YouTube Shorts, TikTok, Instagram) con hashtags #IAEducativa.
7. Recolecta retroalimentación de 3 personas (qué entendieron, qué les gustó).
8. Documenta el proceso.

**Materiales.** Cuentas: ChatGPT/Claude (free), DALL·E o Midjourney, ElevenLabs (free), Suno (free), CapCut (free) · 90 min.

**Entregable.** Reporte de 1 página + link al video publicado + capturas de cada paso.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Calidad técnica del video | borroso, mal audio | aceptable | profesional, sincrónico |
| Coherencia con tema | imprecisa | correcta | atractiva y clara |
| Uso del pipeline | 2-3 herramientas | 4-5 herramientas | pipeline completo + edición |
| Publicación | privada | público sin difusión | público con engagement |
| Reflexión | sin documentar | menciona pasos | discute decisiones creativas |
::/albatros

---

::act-case{titulo="Audita 3 piezas multimodales y detecta señales de IA" lineas=12}
Tu tarea: a tres compañeros les pides que te muestren 3 imágenes y 3 videos cualesquiera de redes sociales recientes. Tu trabajo: detectar cuáles son generados por IA. Para cada pieza:

1. Anota 3 señales visuales o auditivas que **delataron** la generación por IA (manos defectuosas, texto ilegible, sombras inconsistentes, voz con cadencia no natural, parpadeos faciales, fondos demasiado simétricos).
2. Decide tu nivel de confianza (alto / medio / bajo).
3. Verifica con metadatos (algunos archivos llevan tags C2PA, Content Credentials) o con detectores como AI or Not.
4. Reflexiona: ¿qué piezas te engañaron? ¿qué hubieras necesitado para detectarlas?
::/act-case

---

::act-mindmap{titulo="Mapa mental — Pipeline multimedia con IA" centro="PIPELINE IDEA → VIDEO" nodos_primarios=6 nodos_secundarios=18}
6 ramas: guion · imagen · voz · música · avatar · edición. 3 hojas por rama: herramienta principal, plan recomendado, limitación a recordar.
::/act-mindmap

---

::act-label{titulo="Etiqueta el flujo de producción multimedia"}

> Etiqueta cada caja con la herramienta y el formato de salida. Suma los tiempos para tener el budget total del pipeline.
::/act-label


::visual{tipo="diagrama-flujo" descripcion="Diagrama de flujo horizontal con 6 cajas vacías que representan los pasos de un pipeline multimedia: idea → guion → imagen → voz → música → edición → video final. Cada caja tiene espacio para que el estudiante anote la herramienta usada, el tiempo aproximado y el formato del archivo de salida. Debajo del diagrama, una línea de tiempo total con marcadores cada 15 minutos." paginas="0.5" src="../manualesGem/assets/visuales/manual-3/u04/90-actividades-v01.svg"}
---

::act-puzzle{titulo="Sopa de letras — Multimodal" tipo="sopa-letras" tamano="14x14"}
Encuentra 14 términos: SORA · MIDJOURNEY · DALLE · FIREFLY · ELEVENLABS · WHISPER · SUNO · RUNWAY · HEYGEN · DESCRIPT · CAPCUT · CONTROLNET · LORA · UPSCALER.

Después escribe en la parte de abajo qué término crees que va a desaparecer en 2 años.
::/act-puzzle

---

::albatros{titulo="Reto — pipeline en 2 plataformas con presupuesto cero" tipo="reto" tiempo="45 min"}
**Pregunta detonadora.** ¿Cuánto contenido multimedia puedes producir con presupuesto cero (cero suscripciones, cero pagos)?

**Lo que harás.**
1. **Identifica 5 herramientas** con plan free generoso: por ejemplo Bing Image Creator, Adobe Firefly Free, ElevenLabs Free 10 min, Suno Free, CapCut.
2. **Reproduce el pipeline** del taller pero usando solo herramientas gratis.
3. **Documenta los límites**: cuántas imágenes pudiste generar, calidad obtenida, tiempo gastado en esperas (algunas free tienen colas).
4. **Compara contra una pieza producida con plan pago** (puede ser una de tus piezas previas en el manual): ¿cuánto perdiste de calidad?
5. **Calcula el "umbral"**: ¿en qué punto vale la pena pagar suscripción?

**Materiales.** Internet, planes free de las 5 herramientas, cronómetro.

**Entregable.** a) tabla de las 5 herramientas free con cuotas, b) pieza producida (video corto), c) comparativa con pieza paga, d) recomendación: ¿pagas o no? Justifica.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cobertura | 2-3 herramientas free | 4 herramientas | 5 herramientas + alternativas |
| Análisis de límites | impresionista | nota cuotas | mide tiempo, calidad y disponibilidad |
| Recomendación | "paga" o "no pagues" | con criterio | con criterio + condiciones específicas |
::/albatros
