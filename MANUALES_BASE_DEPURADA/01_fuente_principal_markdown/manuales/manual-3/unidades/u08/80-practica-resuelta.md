---
unidad: 8
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — 1 idea → 3 piezas publicadas en 90 minutos

::practica{titulo="Aplica el pipeline completo desde 'cómo construí mi GPT' hasta 3 piezas en 4 plataformas"}
**Problema.** 
Tomas la idea "Cómo construí mi GPT como tutor de física en 30 minutos" y la conviertes en un post de LinkedIn, un video de YouTube Short y un carrusel de Instagram. Todo en 90 minutos.

**Paso 1 — Idea + outline (5 min).**
- **Idea:** "Construí mi tutor de física en 30 min y mis compañeros lo usan más que el del profesor".
- **Outline:**
  - Hook: "enseña Bernoulli mejor que mi profesor".
  - Por qué: clase grande, ritmo desigual.
  - Cómo: 5 pasos del pipeline.
  - Resultado: 12 compañeros lo usan.

**Paso 2 — Texto: 3 piezas (15 min).**
- Prompt en Claude: pide 3 formatos (video 60s, post 400 palabras, carrusel 6 slides).
- Establece tono: directo, conversacional, sin clichés.
- Editas los outputs en 5 minutos para asentar tu voz.

::interioriza
**Analogía:** Crear contenido sin pipeline es como cocinar cada plato de un banquete desde cero. 
Usar este flujo es como tener una cocina industrial (IA) que te da los ingredientes picados; tú solo sazonas y sirves.
::/interioriza

**Paso 3 — Imagen: 8 visuales (15 min).**
- Usa DALL·E 3 (ChatGPT Plus) para generar:
- 1 Portada LinkedIn (estilo editorial, paleta azul-naranja).
- 6 Imágenes para carrusel Instagram.
- 1 Thumbnail para el YouTube Short.

**Paso 4 — Voz (10 min).**
- En ElevenLabs: elige voz "latina neutral" o clona la tuya.
- Pega el guion del video.
- Ajusta estabilidad (50) y similitud (75), luego genera el MP3.

**Paso 5 — Video (20 min).**
- Abre CapCut, importa narración e imágenes (7-8s c/u).
- Activa *AI Subtitle* para generar textos dinámicos.
- Sincroniza música y exporta (MP4 1080p, vertical 9:16).

**Paso 6 — Diseño Canva (15 min).**
- Abre tu *Brand Kit* ya configurado.
- Ensambla el carrusel de Instagram.
- Arma la imagen de portada de LinkedIn.

**Paso 7 — Publicación (10 min).**
- Programa todo con Buffer (ej. 7am del día siguiente):
- YouTube Shorts / TikTok / Reels: Mismo video, tags adaptados.
- LinkedIn: Post texto + portada + link en comentarios.

**Resultado:**
- Tiempo total: 90 minutos exactos. 
- Logro: 3 piezas distribuidas en 4 plataformas.

> **Trampa común evitada:** 
> Nunca publiques contenido idéntico letra por letra. 
> Adapta: LinkedIn es más profesional, TikTok más casual, IG más visual.

::pausa{}
**Deducción:**
Si tienes que reducir este pipeline de 90 a 60 minutos, ¿qué paso optimizarías primero?
- a) Escribir el prompt desde cero cada vez.
- b) Crear plantillas base en Canva de antemano.
- c) Grabar el video tú mismo sin IA.
*Pista: ¿Qué tarea repetitiva de diseño se puede hacer una sola vez? (b)*
::/pausa
::/practica

---

## Práctica resuelta — Reescribí un guion con la voz de mi creador favorito

::practica{titulo="Iteración de guion con few-shot de un estilo de referencia"}
**Problema.** 
Generaste un guion para un Reel sobre "qué es un LLM". 
Suena aburrido, como cualquier post de Wikipedia. 
Quieres la voz de **Tim Urban (Wait But Why)**: analogías absurdas y tono curioso.

**Paso 1 — Identifica los rasgos del creador.**
- Lees posts de referencia y extraes su ADN:
- Empieza con preguntas tontas, se sorprende genuinamente.
- Usa analogías exageradas ("comité de 100 monos").
- Personifica conceptos técnicos.

**Paso 2 — Prompt few-shot al modelo.**
- Le das rol: "copywriter de divulgación".
- Entregas 2 **ejemplos literales** del estilo de Tim Urban.
- Pides: guion de 60s, estructura AIDA, 2 analogías absurdas.

**Paso 3 — Output v1.**
- La IA crea un "duendecillo gigante" atrapado que adivina palabras compulsivamente.
- Ya no suena a profesor, suena a alguien descubriendo el mundo contigo.

**Paso 4 — Refinamiento estructural.**
- El cierre "sigue para más" es muy genérico.
- Iteras: "agrega un cierre que despierte una pregunta nueva".
- Resultado: un remate sobre lo extraño que es que la IA parezca pensar.

::interioriza
**Analogía:** Pedirle a la IA que sea "creativa" es como decirle a un peluquero "hazme algo bonito" (es una lotería). 
Usar *few-shot* (darle ejemplos concretos) es como llevar la foto exacta del corte que quieres.
::/interioriza

> **Lección clave.** 
> Si buscas una voz auténtica con IA, no le pidas creatividad genérica. 
> Pídele **imitación específica** de tus referencias curadas.

::pausa{}
**Deducción:**
¿Por qué el *few-shot* (dar ejemplos) funciona mejor que un adjetivo como "escribe divertido"?
- a) La IA entiende mejor la gramática que las emociones.
- b) "Divertido" es subjetivo; un texto de ejemplo le da un patrón matemático claro que puede replicar. *(b)*
::/pausa
::/practica

---

## Práctica resuelta — Calendario editorial de 12 piezas

::practica{titulo="De lanzamiento aislado a presencia sostenida: 4 semanas en 1 hora de planeación"}
**Problema.** 
Quieres dejar de improvisar y tener publicaciones consistentes por 4 semanas. 
Vas a planear 12 piezas en solo 1 hora.

**Paso 1 — Define tus 3 pilares temáticos (10 min).**
- **Pilar A:** Estudios con IA (cómo estudio mejor).
- **Pilar B:** Reflexiones académicas (dudas, lecciones).
- **Pilar C:** Tutoriales prácticos (paso a paso rápido).

**Paso 2 — Matriz temática × formato (15 min).**
- Cruza tus semanas con formatos:
- Lunes: Post en LinkedIn (Pilar A).
- Miércoles: Carrusel en Instagram (Pilar B).
- Viernes: Video de 60s (Pilar C).

**Paso 3 — Banco de hooks (10 min).**
- Usa IA para redactar solo el *hook* (gancho inicial) de las 12 piezas.
- Ej: "5 cosas que crees de la IA y que un ingeniero desmonta en 30s".

**Paso 4 — Plantilla por formato (15 min).**
- Define estructuras fijas.
- **LinkedIn:** Hook → Contexto → 3 viñetas → CTA.
- **Video:** Hook (5s) → Concepto (25s) → Ejemplo (20s) → Pregunta (10s).

**Paso 5 — Calendario (10 min).**
- Monta un tablero en Notion o Airtable.
- Columnas: fecha, título, pilar, formato, plataforma, y métricas.

::interioriza
**Analogía:** Crear contenido sin matriz es como ir al supermercado sin lista cuando tienes hambre. 
Con matriz y plantillas pre-hechas, es como armar un set de Lego que ya tiene las piezas separadas por color.
::/interioriza

**Resultado:**
- En 1 hora de planeación tienes todo un mes estructurado.
- Producir cada pieza te tomará solo 1 hora (ya sabes qué y cómo).
- Total: 13 horas para dominar el mes.

> **Lección clave.** 
> La diferencia entre un creador esporádico y uno consistente no es talento. 
> Es la reducción de fricción mediante la **planeación temática previa**.

::pausa{}
**Deducción:**
¿Cuál es el beneficio principal de usar plantillas por formato?
- a) Eliminas la fatiga de decisión ("¿cómo empiezo hoy?") y aceleras brutalmente la producción. *(a)*
- b) Le gusta más al algoritmo porque publicas siempre lo mismo.
::/pausa
::/practica
