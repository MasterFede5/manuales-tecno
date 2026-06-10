---
unidad: 4
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Da voz e imagen a tu tutor IA en 60 minutos

> Este taller le pone cara y voz a tu tutor IA personal. Hasta ahora era solo texto; al final de esta hora tu tutor habla con voz clonada (o sintética) y se presenta con un avatar visual, formando tu **identidad visual de tutor v0.4**.

::albatros{titulo="Crea identidad visual y de voz de tu tutor IA personal" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Cómo logras que tu tutor IA tenga **personalidad visual y vocal coherente** sin invertir 20 horas en diseño?

**Lo que harás (10 pasos).**

1. **Define la "personalidad visual"** de tu tutor en 5 atributos: género/no-género, edad aparente, paleta de colores, vestimenta, estilo gráfico (3D Pixar, ilustración 2D, fotorrealista, anime). Anota en una hoja.
2. **Genera 4 avatares candidatos** con DALL·E 3 o Midjourney usando un prompt detallado con la anatomía de prompt visual (sujeto + acción + estilo + iluminación + modificadores). Genera 4 variaciones cambiando un solo atributo cada vez.
3. **Elige el avatar definitivo** y guárdalo en formato cuadrado 1024×1024 px. Ese será el "rostro" de tu tutor.
4. **Genera 3 imágenes complementarias** del tutor en distintas situaciones (explicando con pizarrón, leyendo, pensando) para usar como assets en futuras producciones.
5. **Define la "personalidad vocal"** en 4 atributos: género de voz, edad, tono (cálido/profesional/juvenil), velocidad. Anota.
6. **Genera 3 voces candidatas** en ElevenLabs (versión gratuita). Usa 3 voces de la biblioteca o configura con el "Voice Designer". Hazlas leer la misma frase de 30 segundos.
7. **Elige la voz definitiva.** Guarda el "Voice ID" en tu archivo `tutor-vN.md`.
8. **Crea una "presentación oficial"** del tutor: un video de 30 segundos donde el avatar fijo aparece y la voz narra la presentación ("Hola, soy [nombre], tu tutor de [materias]. Mi estilo es… mi compromiso es…"). Usa CapCut, Descript o HeyGen.
9. **Documenta** en el archivo `tutor-vN.md`: avatar PNG, voz ID, presentación MP4, prompts usados (reproducibles), decisiones de diseño (qué descartaste y por qué).
10. **Comparte** con un compañero. Pídele feedback: "¿esta personalidad transmite paciencia y rigor?". Itera si hace falta.

**Materiales.**
- Acceso a un generador de imagen (DALL·E 3 incluido en ChatGPT Plus, Midjourney, Adobe Firefly Free, Bing Image Creator).
- Cuenta gratuita de ElevenLabs (10 minutos de generación al mes).
- CapCut, Descript o HeyGen para montar el video.
- Editor de imagen ligero (Canva, Photopea, Figma) para crops y ajustes.

**Entregable.**
1. Archivo `tutor-v0.4.md` con la documentación completa.
2. PNG del avatar definitivo + 3 imágenes complementarias.
3. MP3 con la voz leyendo 3 frases de prueba.
4. MP4 de 30 segundos con la presentación del tutor.
5. Reflexión escrita de 150 palabras: ¿cuántas iteraciones hicieron falta? ¿qué te enseñó sobre tu propia preferencia visual y vocal?

**Rúbrica corta.**

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| Coherencia visual | imágenes inconexas | mismo estilo en 2-3 | 4 imágenes con misma identidad |
| Calidad del avatar | ruidoso, manos defectuosas | aceptable | profesional sin defectos visibles |
| Personalidad vocal | voz sin ajustar | 1 voz elegida | 3 voces probadas + decisión justificada |
| Presentación final | sin video | video básico | video con sincronía y calidad pro |
| Documentación | suelta | reproducible | un compañero la ejecutaría sin tu ayuda |

**Tip Albatros.** El paquete que armas aquí (avatar + voz + presentación) es la **identidad oficial** de tu tutor. Cuando llegues a U07 y publiques tu GPT custom, vas a usar este avatar. Cuando hagas videos educativos en U08, vas a usar esta voz. **Guarda los archivos en una carpeta `tutor-identidad/` con backup**.
::/albatros
