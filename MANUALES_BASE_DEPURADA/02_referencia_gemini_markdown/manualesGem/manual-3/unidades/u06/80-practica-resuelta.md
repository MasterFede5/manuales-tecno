---
unidad: 6
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Asistente semanal personal

::practica{titulo="Diseña tu rutina automatizada de 1 semana con todas las herramientas de la unidad"}
**Problema.** Tienes una semana cargada: 3 entregas escolares, 2 reuniones de equipo, 5 clases, gym 3x, lectura asignada, presentación viernes. Sin asistente IA estimas 70 horas. ¿Puedes bajarlo a 50?

---

**Paso 1 — Lunes 7am: planeación con Motion (10 min).**

Agregas a Motion:
- "Entrega ensayo Filosofía - 4h - alta - vence martes 10pm".
- "Entrega tarea Cálculo - 2h - alta - vence miércoles".
- "Entrega proyecto Programación - 6h - media - vence sábado".
- "Reunión equipo tesis - lunes 6pm - 1h".
- "Reunión grupo materia - jueves 11am - 1h".
- "Gym - 1h x 3 días".
- "Leer cap 7 libro filosofía - 3h".
- "Preparar presentación viernes - 4h".

Motion calendariza automáticamente respetando tus 5 clases.

---

**Paso 2 — Lunes 8am: correo con Gemini (15 min).**

- Resumen de 30 mails recibidos.
- Respondes a 5 críticos con "Help me write".
- Agendas a tarde los 8 que requieren más tiempo.
- 17 son newsletter/spam → archivar/eliminar.

---

**Paso 3 — Lunes 9am: clase con Otter (1h).**

- Bot conectado a Zoom de la clase.
- Tomas pocas notas a mano (las importantes).
- Otter graba, transcribe, identifica speakers.
- Al final: descargas summary y action items.
- Subes transcript a NotebookLM "Materia X".

---

**Paso 4 — Lunes 1pm: ensayo Filosofía con Claude Project (4h).**

- Project "Tesis Filosofía" ya tiene knowledge base.
- Generas borrador en chat: "redacta ensayo de 1500 palabras sobre X".
- Usas Canvas para iterar 3 párrafos.
- Verificas citas con Perplexity.
- Listo en 4h (vs 8h sin asistente).

---

**Paso 5 — Lunes 5:30pm: prep reunión con Otter (5 min).**

- Otter te muestra resumen de reunión PASADA del equipo.
- Repasas action items abiertos.
- Llegas a la reunión 6pm con contexto.

---

**Paso 6 — Martes 8am: hojas con GPT for Sheets (30 min).**

- 50 papers para tu tesis en Sheets.
- Columna B: =GPT("clasifica como teórico/empírico/mixto", A2).
- Columna C: =GPT("relevancia 1-5 para mi tesis", A2).
- Filtras solo los relevantes 4-5.

---

**Paso 7 — Miércoles: tarea Cálculo con o3 (2h).**

- 10 problemas de cálculo.
- Modelo razonador (o3 o Claude con thinking).
- Pides "*resuelve paso a paso, explica cada paso*".
- Verificas a mano 3 al azar.

---

**Paso 8 — Jueves: presentación con Gamma (40 min).**

- Pegas tu Word de la presentación en Gamma.
- Generate → 12 slides con diseño.
- Iteras 2-3 slides ("hazlo más visual").
- Exportas PDF.

---

**Paso 9 — Viernes: presentación + reflexión (1h).**

- Presentas con Gamma slides.
- Audiencia recibe link compartible.
- Sábado mañana: reflexión sobre la semana.

---

**Resultado: 50 horas en lugar de 70.**

Métricas reales:
- **Correo**: 2.5h (vs 7h normal).
- **Investigación tesis**: 6h (vs 12h normal).
- **Reuniones**: 2.5h (vs 4h normal — Otter te ahorra "rehacer" notas).
- **Calendario**: 0h gestionado por Motion (vs 1.5h/sem normal).
- **Presentación**: 0.7h (vs 4h normal).
- **Lectura asignada**: 1.5h con audio overview de NotebookLM (vs 3h leyendo).

**Ahorro total: 20h/semana. Equivalen a 80h/mes = 2 semanas laborales adicionales/mes.**

> **Verificación profesional.** Si tu calidad académica baja por automatización, **estás haciéndolo mal**. La AI debería **subir tu calidad** además de ahorrarte tiempo. Si bajas calidad para ahorrar tiempo, redefine el balance.

> **Trampa común evitada.** No automatices todo. Conserva 1-2 espacios de **tarea sin AI**: lectura profunda, escritura creativa, conversación humana. Tu cerebro necesita ese trabajo para mantenerse ágil.
::/practica

---

## Práctica resuelta — De Excel manual a hoja con IA: clasifiqué 200 reseñas en 8 minutos

::practica{titulo="Aplica =GPT() en Sheets para una tarea repetitiva real"}
**Problema.** Tu jefa de área te pide clasificar 200 reseñas de un producto en POSITIVA / NEGATIVA / NEUTRA y extraer en otra columna el "tema principal" en 3 palabras. Manualmente son 4 horas. Vas a hacerlo en 8 minutos.

**Paso 1 — Setup (3 min).**

1. Abre la hoja de Sheets con las 200 reseñas en columna A.
2. Instala el complemento "GPT for Sheets and Docs" (Marketplace → buscar → instalar).
3. Configura tu API key de OpenAI o Claude. Si no tienes API, usa la versión Pro del complemento (10 USD/mes con cuota).

**Paso 2 — Fórmula 1: clasificación (2 min).**

En B2 escribes:

```
=GPT("Clasifica esta reseña como POSITIVA, NEGATIVA o NEUTRA. Solo devuelve la palabra, sin explicaciones. Reseña: " & A2)
```

Arrastras hacia abajo hasta B201. Sheets ejecuta una llamada API por celda. Cada llamada cuesta ~0.0002 USD con GPT-4o-mini. Total: 200 × 0.0002 = **0.04 USD**.

Tiempo de ejecución: 2-3 minutos para las 200 filas (paralelizado).

**Paso 3 — Fórmula 2: tema principal (2 min).**

En C2:

```
=GPT("Extrae el tema principal de esta reseña en exactamente 3 palabras. Solo devuelve las 3 palabras separadas por espacios. Reseña: " & A2)
```

Arrastras. Otros 2-3 minutos.

**Paso 4 — Auditoría rápida (1 min).**

Verifica 5 filas al azar comparando contra la reseña original. Si las 5 están bien, el batch general probablemente tiene 95%+ de precisión. Si 1 está mal, audita 10 más.

**Paso 5 — Análisis con tabla dinámica (NO necesita IA, 30 segundos).**

- Tabla dinámica con conteo de POSITIVA / NEGATIVA / NEUTRA → 60% positiva, 25% negativa, 15% neutra.
- Tabla dinámica con conteo de temas → top 5 temas: "calidad construcción", "atención cliente", "precio alto", "tiempo entrega", "instrucciones confusas".

**Paso 6 — Entrega.**

Subes la hoja con análisis a tu jefa, con un párrafo de hallazgos y 3 recomendaciones.

**Resultado:**

| Métrica | Manual | Con =GPT() |
|---|---|---|
| Tiempo total | 4 horas | 8 minutos |
| Costo | 0 USD (tu tiempo) | 0.04 USD + tu tiempo |
| Precisión | 100% (humana) | ~95% (IA) |
| Repetibilidad | baja | alta (puedes correrlo cada semana) |

**Trade-off real.** Pierdes 5% de precisión. Ganas **30× tiempo** y **repetibilidad infinita** (la próxima semana corres lo mismo en 8 min, no 4 horas más).

> **Lección clave.** Cualquier tarea de Sheets que sea **repetitiva, clasificatoria o extractiva** es candidata para `=GPT()`. Antes de hacerlo manual una segunda vez, monta el flujo. La inversión de 8 minutos paga en la primera semana.
::/practica

---

## Práctica resuelta — Convertí mi reunión semanal de equipo en action items automáticos

::practica{titulo="Pipeline Otter + ChatGPT para extraer compromisos sin perder ninguno"}
**Problema.** Tienes reuniones semanales de equipo de 1 hora donde se acuerdan 6-10 compromisos. Antes los olvidabas o tomabas notas a medias. Vas a montar un pipeline que captura todo y lo entrega listo en Slack/correo a las 5 minutos de terminar.

**Paso 1 — Setup ético previo (5 min).**

- Aviso al equipo en correo: *"a partir de la siguiente reunión voy a usar Otter para transcripción. Si alguien se opone, lo apago. Las transcripciones son privadas y se borran tras procesar action items."*
- Configura Otter para conectarse automáticamente a tu Zoom/Meet/Teams cuando inicia la reunión.

**Paso 2 — Durante la reunión.**

- Otter graba en background.
- Tú participas activamente. **No** intentes tomar notas exhaustivas; eso lo hace Otter.
- Solo anotas a mano insights críticos o decisiones que sospechas el modelo no va a entender.

**Paso 3 — Justo al terminar (5 min).**

1. Abre la transcripción en Otter.
2. Genera el "Outline" automático.
3. Copia la transcripción completa (Ctrl+A → Ctrl+C).

**Paso 4 — Procesamiento con prompt estructurado.**

Pegas en Claude o ChatGPT con este prompt:

```
Eres mi asistente ejecutivo. Te paso la transcripción de una reunión de
equipo. Extrae:

1. Resumen ejecutivo (3-4 oraciones).
2. Decisiones tomadas (lista numerada con responsable si lo dice).
3. Action items en formato:
   - [TAREA] - [RESPONSABLE] - [DEADLINE si se mencionó]
4. Temas que quedaron pendientes para la próxima reunión.
5. Riesgos o bloqueos mencionados.

Devuelve en Markdown limpio, listo para pegar en Slack/Notion.

TRANSCRIPCIÓN:
[pegar]
```

Output: documento estructurado en 30-60 segundos.

**Paso 5 — Auditoría (2 min).**

- Verifica que los **action items y responsables** coincidan con tu memoria.
- Si Otter confundió speakers, corrige.
- Si el modelo se inventó un compromiso (raro pero pasa), elimínalo.

**Paso 6 — Distribución (3 min).**

- Pegas en Slack del equipo o en correo a los participantes.
- Cada quien confirma su action item con emoji ✅ o pregunta.
- Tú agregas los action items propios a Motion/Notion con deadline.

**Resultado:**

| Métrica | Antes | Después |
|---|---|---|
| Tiempo en notas durante reunión | 30 min divididos | 0 min (participas más) |
| Tiempo en post-procesar | 30 min | 10 min |
| Action items capturados | ~70% | ~95% |
| Distribución a equipo | manual a veces | automática siempre |
| Confiabilidad ante "yo no me comprometí a eso" | discutible | tienes transcript |

**Bonus inesperado.** Después de 4 reuniones tienes **un corpus de transcripciones** de tu equipo. Puedes pedirle a Claude: "*analiza estas 4 reuniones y dime qué temas se repiten sin avanzar*". Diagnosticas patrones de bloqueo del equipo.

> **Lección clave.** La automatización de reuniones no es solo eficiencia — es **memoria institucional**. Tu yo de hace 3 meses queda documentado en transcripciones procesadas, lo cual cambia las dinámicas de equipo más de lo que parece.
::/practica
