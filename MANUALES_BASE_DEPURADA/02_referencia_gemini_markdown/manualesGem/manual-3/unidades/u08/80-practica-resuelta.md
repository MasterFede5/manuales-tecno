---
unidad: 8
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — 1 idea → 3 piezas publicadas en 90 minutos

::practica{titulo="Aplica el pipeline completo desde 'cómo construí mi GPT' hasta 3 piezas en 4 plataformas"}
**Problema.** Tomas la idea "Cómo construí mi GPT como tutor de física en 30 minutos" y la conviertes en post LinkedIn + video YouTube Short + carrusel Instagram, todo en 90 min.

---

**Paso 1 — Idea + outline (5 min).**

Idea: "Construí mi tutor de física como GPT en 30 min y mis compañeros lo usan más que el del profesor".

Outline:
- Hook: "construí un tutor que enseña Bernoulli mejor que mi profesor".
- Por qué: explica el problema (clase grande, ritmo desigual).
- Cómo: 5 pasos del pipeline.
- Resultado: 12 compañeros lo usan.
- Lección: la barrera para crear desapareció.

---

**Paso 2 — Texto: 3 piezas (15 min).**

Prompt en Claude:
```
Eres editor. Tema: "Construí mi GPT tutor de física en 30 min".

Genera 3 piezas con voz: directa, conversacional, mexicana neutra,
sin clichés ("game changer", "transforma tu vida").

A) GUION VIDEO 60s — hook punzante, 5 pasos rápidos, CTA.
B) POST LINKEDIN 400 palabras — hook, narrativa, 5 bullets de pasos, CTA.
C) CARRUSEL INSTAGRAM 6 slides — slide 1 portada hook, slides 2-5
   un paso cada uno, slide 6 CTA.
```

Recibes los 3 textos. Editas 5 minutos para reforzar tu voz.

---

**Paso 3 — Imagen: 8 visuales (15 min).**

DALL·E 3 (vía ChatGPT Plus):
1. Portada LinkedIn: "ilustración estudiante construyendo robot tutor, paleta azul-naranja, estilo editorial".
2-7. Carrusel Instagram (6 imágenes, una por slide).
8. Thumbnail YouTube Short.

---

**Paso 4 — Voz (10 min).**

ElevenLabs:
- Voz "Manuel" (latino neutral) o tu voz clonada.
- Pegas guion.
- Estabilidad 50, similitud 75.
- Genera MP3.

---

**Paso 5 — Video (20 min).**

CapCut:
- Importa narración.
- Importa 8 imágenes.
- Cada imagen 7-8 s.
- AI Subtitle activado.
- Music sync con beat motivacional.
- Export MP4 1080p, 60 s vertical 9:16.

---

**Paso 6 — Diseño Canva (15 min).**

Brand Kit ya configurado.
- Carrusel Instagram con paleta tuya.
- Post LinkedIn portada.

---

**Paso 7 — Publicación (10 min).**

- YouTube Shorts: video + descripción + tags.
- TikTok: mismo video + hashtags.
- Instagram Reels: mismo video.
- Instagram carrusel: 6 slides separadas.
- LinkedIn: post con imagen portada + link al video.

Programado para publicarse a las 7am del día siguiente con Buffer.

---

**Resultado.** 90 minutos exactos. **3 piezas en 4 plataformas**.

Métricas a 1 semana (objetivo): 100+ views totales, 5+ comentarios, 1 conexión LinkedIn por el contenido.

> **Verificación.** Al final del flujo:
> - Identidad visual coherente (paleta, tipografía, tono).
> - Voz consistente entre piezas.
> - Hooks distintos pero misma idea central.
> - Subtítulos en video (importante para retención).

> **Trampa común evitada.** No publiques contenido idéntico letra por letra en las 4 plataformas. **Adapta** al formato y audiencia: LinkedIn más profesional, TikTok más casual, IG más visual.
::/practica

---

## Práctica resuelta — Reescribí un guion mediocre con la voz de mi creador favorito

::practica{titulo="Iteración de guion con few-shot de un estilo de referencia"}
**Problema.** Generaste un guion para un Reel sobre "qué es un LLM" y suena genérico, como cualquier post de divulgación. Quieres que tenga la voz **de Tim Urban (Wait But Why)**: analogías absurdas, tono curioso, personificación de conceptos.

**Paso 1 — Identifica los rasgos del creador de referencia.**

Lees 2 posts de Tim Urban y anotas:
- Empieza con una pregunta tonta y se sorprende del descubrimiento.
- Usa analogías exageradas ("imagínate un mono con 8 brazos").
- Personifica conceptos abstractos ("el cerebro decide algo y le avisa al consciente después").
- Tono: yo descubriendo contigo, no yo enseñándote.
- Frases cortas mezcladas con frases largas.

**Paso 2 — Prompt few-shot al modelo.**

```
Eres copywriter de divulgación. Tu estilo de referencia es Tim Urban
(Wait But Why). Aquí van 2 ejemplos de su estilo:

EJEMPLO 1:
"Tu cerebro es como un comité de 100 monos en una sala. Cada mono tiene
una opinión. Algunos gritan, otros duermen. Y el 'tú' que crees ser es
solo el portavoz que les explica a otros lo que el comité decidió hace
3 milisegundos sin consultarte."

EJEMPLO 2:
"Imagínate que un día te dicen que existe una galleta que sabe a TODAS
las galletas que existieron y existirán. Suena imposible. Pues los LLMs
son medio así: una galleta gigante hecha de TODO el texto de internet."

TAREA: redacta guion de 60 segundos sobre 'qué es un LLM' siguiendo
exactamente este estilo. Estructura AIDA. Empieza con una pregunta
tonta. Usa al menos 2 analogías absurdas. Personifica al modelo.
```

**Paso 3 — Output v1.**

```
¿Te has preguntado qué pasa cuando le escribes a ChatGPT?

Imagínatelo así. Hay un duendecillo gigante atrapado en una caja.
El duendecillo leyó TODO. Wikipedia, libros, Reddit, blogs de cocina,
papers de física, hasta el manual de tu microondas. Todo.

Pero el duendecillo no entiende NADA. Solo es muy bueno en una cosa:
adivinar la siguiente palabra de cualquier frase. Le tapas el final
y él, con cara de obsesivo, calcula cuál palabra es más probable.

Tú escribes "Hoy comí" y el duendecillo dice "tacos" porque vio mil
millones de oraciones que terminan en "tacos". Y ya. Eso es un LLM.

Lo loco es que adivinar la siguiente palabra suficientes veces se ve
exactamente como pensar. Pero no lo es.

Sigue para más cosas que parecen mágicas pero son matemáticas.
```

**Paso 4 — Compara v1 vs guion original genérico.**

| Criterio | Guion genérico | Guion v1 con voz Tim Urban |
|---|---|---|
| Tono | enseñador | curioso descubriendo |
| Analogía | una sola, técnica | dos absurdas |
| Personificación | ninguna | duendecillo obsesivo |
| Engagement esperado | bajo | alto |

**Paso 5 — Refinamiento estructural.**

V1 está bien pero tiene un problema: el "sigue para más" al final es flojo. Iteras pidiendo: "agrega un cierre que te despierte una pregunta nueva, no un CTA genérico". Output v2 cierra con: *"Y ahora viene lo verdaderamente raro: nadie sabe por qué adivinar palabras a esa escala se siente tanto como pensar. Spoiler: ni los que lo construyen lo saben"*.

**Paso 6 — Lección.**

El few-shot con un estilo de creador concreto es **mucho más eficaz** que pedirle a la IA "haz un guion atractivo". Tres ejemplos puntuales de tu creador favorito convierten output gris en output con personalidad.

> **Lección clave.** Si quieres voz auténtica con IA, **no le pidas creatividad — pídele imitación específica**. La creatividad emergente sale de la combinación de tu criterio + estilos de referencia que tú eliges.
::/practica

---

## Práctica resuelta — Calendario editorial mensual con 12 piezas y matriz temática

::practica{titulo="De lanzamiento aislado a calendario sostenido: 4 semanas, 12 piezas, 1 hora de planeación"}
**Problema.** Hiciste tu primer lanzamiento en el taller. Ahora quieres convertirte en alguien con presencia en redes con publicaciones consistentes durante 4 semanas. Vas a planear las 12 piezas en 1 hora.

**Paso 1 — Define tus 3 pilares temáticos (10 min).**

Para tener consistencia, todos tus contenidos deben girar sobre 3 pilares. Para tu caso (estudiante de bachillerato + IA + estudios):

- **Pilar A: Estudios con IA** (cómo uso IA para estudiar mejor).
- **Pilar B: Reflexiones académicas** (lecciones de bachillerato, dudas existenciales del estudiante).
- **Pilar C: Tutoriales prácticos** (paso a paso de algo que aprendí).

**Paso 2 — Matriz temática × formato (15 min).**

Diseñas una matriz de 4 semanas × 3 piezas/semana:

| Semana | Lunes (post LinkedIn 800 palabras) | Miércoles (carrusel IG 8 slides) | Viernes (video corto 60 s) |
|---|---|---|---|
| 1 | A: "Cómo NotebookLM cambió mi forma de leer libros" | B: "5 mitos de la IA" | C: "Tutorial: tu primer GPT custom" |
| 2 | A: "Mi setup de productividad con IA" | B: "¿Es plagio usar IA?" | C: "Tutorial: detectar alucinaciones" |
| 3 | A: "Cómo aprendo cálculo con un Project de Claude" | B: "El error más común al pedirle algo a ChatGPT" | C: "Tutorial: GPT for Sheets" |
| 4 | A: "Cómo escribí un ensayo en 1 hora con 5 citas verificadas" | B: "Mi código ético de uso de IA" | C: "Tutorial: pipeline multimedia 90 min" |

**Paso 3 — Banco de hooks (10 min).**

Para cada pieza, redactas el **hook en una sola frase**. Tu modelo te ayuda. Algunos ejemplos:

- "Pasé 6 horas leyendo un libro. Después le pedí a una IA un audio overview de 12 minutos. Esto fue lo que cambió en mi cabeza."
- "5 cosas que la gente cree de la IA y que cualquier ingeniero te desmonta en 30 segundos."
- "Construí un tutor de física como GPT en 30 minutos. Mis compañeros ahora lo usan más que al del profesor."

**Paso 4 — Plantilla por formato (15 min).**

Diseñas 3 plantillas reutilizables:

- **Plantilla post LinkedIn:** hook (1 frase) → contexto personal (2 párrafos) → 3 lecciones (3 bullets) → CTA reflexivo.
- **Plantilla carrusel IG:** slide 1 hook → slides 2-7 una idea por slide con visual + 20 palabras → slide 8 CTA.
- **Plantilla video 60 s:** 0-5s hook → 5-30s concepto → 30-50s ejemplo → 50-60s pregunta para comentarios.

**Paso 5 — Calendario en Notion/Airtable (10 min).**

Creas una base de datos con columnas: fecha · título · pilar · formato · plataforma · estatus · link público · métricas a 24h · métricas a 7 días.

**Resultado.** En **1 hora de planeación**, tienes 12 piezas listas para producir durante 4 semanas. Cada pieza ahora cuesta solo **1 hora de producción** (no 2 horas como sin planear) porque ya sabes hook, formato, plantilla y plataforma.

**Total al cabo del mes:** 12 piezas × 1 hora = **12 horas de producción** + 1 hora de planeación = **13 horas para mes entero de presencia consistente**.

> **Lección clave.** La diferencia entre un creador esporádico y uno consistente no es talento — es **planeación temática previa**. La hora que invertiste hoy te ahorra 12 horas de "qué publico mañana" durante el mes.
::/practica
