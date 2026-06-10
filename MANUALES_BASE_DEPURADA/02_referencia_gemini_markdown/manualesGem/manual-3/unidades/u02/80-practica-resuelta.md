---
unidad: 2
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Reto del prompt idéntico en las 4 plataformas

::practica{titulo="Aplica el mismo prompt en ChatGPT, Claude, Gemini y Copilot — compara y elige tu base"}
**Problema.** Tienes que decidir cuál plataforma será la base de tu tutor IA personal. La forma rigurosa de hacerlo es **comparar respuestas** al mismo prompt en las cuatro y evaluarlas con criterios objetivos.

**Tu tarea:** abrir las cuatro plataformas, pegar el mismo prompt, recolectar resultados y decidir.

---

**Paso 1 — Define el prompt de evaluación.**

Usa este prompt **idéntico** en las 4:

```
Soy estudiante de bachillerato/universidad. Quiero que me expliques el principio de
Bernoulli aplicado al alerón de un coche F1. Necesito:

1. Explicación clara de la física en 3 párrafos.
2. Una analogía cotidiana que mi mamá entendería.
3. Un ejemplo numérico simple (con velocidades realistas).
4. Una pregunta de comprensión que me hagas para verificar que entendí.
5. Una recomendación de qué leer si quiero profundizar.

Tono: amable, claro, sin jerga innecesaria. Idioma: español neutro.
```

**Paso 2 — Aplícalo en las 4 plataformas.**

| Plataforma | URL | Modelo a usar |
|---|---|---|
| ChatGPT | chatgpt.com | GPT-4o (gratis) |
| Claude | claude.ai | Claude Sonnet 4.6 (gratis) |
| Gemini | gemini.google.com | Gemini Flash (gratis) |
| Copilot | copilot.microsoft.com | Default (gratis) |

**Paso 3 — Recolecta y tabula.**

| Criterio | ChatGPT | Claude | Gemini | Copilot |
|---|---|---|---|---|
| Claridad de la explicación (1-5) | | | | |
| Calidad de la analogía (1-5) | | | | |
| Ejemplo numérico correcto (sí/no) | | | | |
| Pregunta pertinente (1-5) | | | | |
| Recomendación útil (1-5) | | | | |
| Tono (1-5) | | | | |
| Tiempo de respuesta (s) | | | | |
| Caracteres totales | | | | |
| **TOTAL (max 30)** | | | | |

**Paso 4 — Análisis cualitativo.**

Para cada plataforma, escribe en 2-3 oraciones:
- Lo que **mejor hizo**.
- Lo que **falló**.
- Qué te dio una **sensación cualitativa** distinta.

**Paso 5 — Decisión.**

Elige tu base con base en:
1. Score numérico total.
2. Sensación cualitativa.
3. **Adecuación a tu ecosistema** (¿usas Google? ¿Microsoft?).
4. **Funciones distintivas** que necesitas (Artifacts, GPTs, Voice).

---

**Resultado esperado (ejemplo).**

Probablemente encuentres patrones como:
- **Claude** redacta más extenso y cuidado, con analogías más elaboradas.
- **ChatGPT** es más conciso y dinámico; usa formato visual (negritas, listas) consistentemente.
- **Gemini** tiende a integrar más datos y referencias actuales (búsqueda web por defecto).
- **Copilot** se siente más "corporativo", a veces más cauteloso.

**Conclusión típica para este caso:** si vas a usar la IA principalmente para estudiar/redactar/explicarte, **Claude o ChatGPT** son los favoritos. Si vives en Google Workspace, **Gemini** puede compensar; si en Microsoft 365, **Copilot**.

> **Verificación.** Repite el ejercicio dentro de 1 mes. Los modelos cambian; tu evaluación debe ser dinámica, no eterna.

> **Trampa común evitada.** No elijas la plataforma "porque me la recomendaron". Tu uso es único. Las decisiones basadas en evidencia personal son mejores que las basadas en hype.
::/practica

---

## Práctica resuelta — Cómo detecté una alucinación con un caso real

::practica{titulo="Atrapa al modelo inventándose una fuente y aprende a verificar"}
**Problema.** Le pides a ChatGPT que te dé "5 papers académicos sobre el efecto de Bernoulli en F1 con autor, año, journal y DOI". Te entrega esto:

```
1. Smith, J. (2018). "Aerodynamic Analysis of Front Wings in Formula 1".
   Journal of Aerospace Engineering, 12(4), pp. 234-245. DOI: 10.1016/jaero.2018.04.012

2. González, M. (2020). "CFD Simulation of Bernoulli Effects in F1".
   Mexican Journal of Fluid Dynamics, 5(2), pp. 87-99. DOI: 10.5555/mjfd.2020.0507
```

Suena bien. Suena demasiado bien. **Vamos a auditarlo.**

**Paso 1 — Identifica afirmaciones verificables.**

Cada cita tiene 4 datos verificables: autor, journal, año, DOI. Esa es tu superficie de auditoría.

**Paso 2 — Verifica el DOI primero (es el más rápido).**

Pega `10.1016/jaero.2018.04.012` en https://doi.org. Resultado: **DOI no encontrado**. Mala señal #1.

Pega `10.5555/mjfd.2020.0507`. Resultado: **DOI no encontrado**. El prefijo `10.5555` además es el rango oficial de DOIs de prueba de la fundación Crossref — **no se asigna a publicaciones reales**. Confirmado: este DOI es inventado.

**Paso 3 — Verifica el journal.**

Busca "Mexican Journal of Fluid Dynamics" en Google y en Scopus. Resultado: **no existe** ese journal. Mala señal #2 confirmada.

**Paso 4 — Confronta al modelo con tu hallazgo.**

Le respondes:

> *"Verifiqué los DOIs que me diste y ninguno existe. ¿De dónde sacaste estas referencias?"*

Respuesta típica del modelo:

> *"Tienes razón, me disculpo. Los DOIs y referencias proporcionados eran ilustrativos y no corresponden a publicaciones reales. Te sugiero buscar en Google Scholar..."*

Esa es la **firma de la alucinación**: el modelo inventó datos plausibles, no falsos al azar. Por eso son peligrosos.

**Paso 5 — Documenta el patrón.**

| Tarea pedida | Riesgo de alucinación | Cómo verificar |
|---|---|---|
| Citas académicas con DOI | **Muy alto** | DOI.org + Crossref |
| Citas a leyes con artículo y fecha | Alto | Diario Oficial + sitio del organismo |
| Datos estadísticos con fuente | Alto | Sitio del organismo (INEGI, OMS) |
| Quotes históricos | Medio | Wikiquote + búsqueda en libros |
| Código que use librerías | Medio-alto | Probarlo en local; correr `pip install` |
| Resúmenes de un PDF que subiste | Bajo | Verificar páginas citadas |

**Paso 6 — Ajusta tu próximo prompt.**

En lugar de "dame 5 papers", pide:

> *"Busca en Perplexity o en Google Scholar y devuélveme solo papers cuyos DOI puedas verificar abriendo doi.org. Si no tienes acceso a búsqueda real, dime explícitamente 'no puedo verificar' en lugar de inventar."*

Diferencia: del prompt original al ajustado, **bajas la frecuencia de alucinación de 80% a menos de 20%** en este tipo de tarea.

> **Lección clave.** Las alucinaciones no son un bug, son un **subproducto del entrenamiento por predicción de tokens**. La defensa NO es "pedirle que no alucine" — es **diseñar tu workflow** para que cualquier hecho citable pase por una verificación externa.
::/practica

---

## Práctica resuelta — Configuré un Project con knowledge base y rebajé mis dudas un 70%

::practica{titulo="De ChatGPT vacío a tutor personalizado: el setup paso a paso"}
**Problema.** Llevas 3 semanas usando ChatGPT free para estudiar Cálculo y sientes que cada chat empieza de cero: tienes que explicar tu nivel, tu estilo, qué temario usa tu escuela, qué examen viene. Cansa.

Vas a configurar un Claude Project (o ChatGPT Project si tienes Plus) que **resuelva esto en una sola configuración**.

**Paso 1 — Reúne 3 archivos clave.**

- `temario-calculo-i.pdf` — descargado del sitio de tu facultad/CCH.
- `apuntes-mias.md` — tus apuntes propios de las 3 unidades vistas.
- `examen-parcial-corregido.pdf` — el examen anterior con tus errores marcados (esto es **oro**: el modelo aprende dónde fallas).

**Paso 2 — Crea el Project.**

En Claude.ai → New Project → "Tutor Cálculo I — [tu nombre]". Sube los 3 archivos a Knowledge.

**Paso 3 — Redacta las instrucciones del sistema.**

```
Eres mi tutor de Cálculo I. Yo soy estudiante de [tu nivel] en [tu institución].
Mi temario oficial está en el archivo "temario-calculo-i.pdf"; consúltalo siempre
que dudes qué notación o método debo usar.

Estilo:
- Empiezas cada explicación con la intuición geométrica antes de la fórmula.
- Usas analogías cotidianas (no físicas teóricas).
- Después de cada concepto haces UNA pregunta socrática para verificar.

Errores típicos míos (ver "examen-parcial-corregido.pdf"):
- Confundo regla de la cadena con la del producto cuando hay anidamiento.
- Olvido el dominio al sacar derivada con raíz.
- Me cuesta interpretar gráficamente la segunda derivada.
Cuando detectes que estoy en zona de uno de estos errores, ALERTA explícitamente.

Restricciones:
- Nunca des la respuesta directa de un ejercicio sin antes pedirme MI intento.
- Si te pido "resuélvemelo", primero pídeme que intente y solo si me niego, resuelve.
- Idioma: español neutro, sin jerga del Reino Unido.
```

**Paso 4 — Prueba con 5 preguntas reales.**

Tomas 5 dudas reales que tuviste esta semana. Las pegas. Mides:

| Pregunta | ¿Usó tu temario? | ¿Aplicó tu estilo? | ¿Te alertó de tus errores? |
|---|---|---|---|
| 1. Derivada de sin(x²) | Sí | Sí (intuición primero) | Sí — alertó cadena vs producto |
| 2. Lim cuando x→0 de (sin x)/x | Sí | Sí | N/A — fuera de tus errores típicos |
| 3. Dominio de √(x-3) | Sí | Sí | Sí — recordó el dominio |
| 4. Concavidad de f(x)=x³ | Sí | Parcial — saltó intuición | Sí — segunda derivada |
| 5. Regla de la cadena con 3 anidamientos | Sí | Sí | Sí — alertó explícitamente |

**Paso 5 — Itera.**

Detectaste que en la pregunta 4 saltó la intuición. Ajustas instrucciones agregando: *"NUNCA saltes la intuición geométrica, ni siquiera cuando la pregunta parece directa."*

**Paso 6 — Mide el efecto.**

Una semana después, notas:
- Tiempo de iniciar una sesión de estudio: bajó de 5 min explicando contexto a **30 segundos**.
- Cantidad de respuestas que tuviste que rechazar por estilo equivocado: bajó de 30% a **menos de 10%**.
- Frecuencia con que el tutor se anticipa a tus errores: pasó de **0%** a **70%**.

> **Lección clave.** Un Project bien configurado **multiplica por 3 la utilidad** del LLM en un dominio específico. La inversión inicial de 30 minutos te ahorra 5 minutos por chat × 100 chats al mes = 8 horas mensuales.
::/practica
