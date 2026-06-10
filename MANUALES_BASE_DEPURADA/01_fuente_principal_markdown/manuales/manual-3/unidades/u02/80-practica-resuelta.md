---
unidad: 2
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Reto del prompt idéntico en las 4 plataformas

::practica{titulo="Aplica el mismo prompt en ChatGPT, Claude, Gemini y Copilot — compara y elige tu base"}
**Problema.** 
- Tienes que decidir cuál plataforma será la base de tu tutor IA personal. 
- La forma rigurosa de hacerlo es **comparar respuestas** al mismo prompt en las cuatro.
- Evalúalas con criterios objetivos.

**Tu tarea:** 
- Abrir las cuatro plataformas.
- Pegar el mismo prompt.
- Recolectar resultados y decidir.

::interioriza
Imagina que vas a contratar a un asistente para tu negocio. 
No le das el trabajo al primero que saluda; les haces la misma entrevista a todos y comparas sus respuestas.
::/interioriza

---

**Paso 1 — Define el prompt de evaluación.**

Usa este prompt **idéntico** en las 4:

```text
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

Para cada plataforma, escribe en viñetas:
- Lo que **mejor hizo**.
- Lo que **falló**.
- Qué te dio una **sensación cualitativa** distinta.

**Paso 5 — Decisión.**

Elige tu base con base en:
- Score numérico total.
- Sensación cualitativa.
- **Adecuación a tu ecosistema** (¿usas Google? ¿Microsoft?).
- **Funciones distintivas** que necesitas (Artifacts, GPTs, Voice).

---

**Resultado esperado (ejemplo).**

Probablemente encuentres patrones como:
- **Claude:** redacta más extenso y cuidado, con analogías más elaboradas.
- **ChatGPT:** es más conciso y dinámico; usa formato visual.
- **Gemini:** tiende a integrar más datos y referencias actuales.
- **Copilot:** se siente más "corporativo", a veces más cauteloso.

**Conclusión típica:** 
- Para estudiar/redactar, **Claude o ChatGPT** son los favoritos. 
- Si vives en Google Workspace, **Gemini**.
- Si en Microsoft 365, **Copilot**.

> **Verificación.** Repite el ejercicio dentro de 1 mes. Los modelos cambian.
> **Trampa común evitada.** No elijas por hype. Tu uso es único.

::pausa{}
**Deducción:** ¿Por qué es importante repetir el reto del prompt en un mes?
*Pista: piensa en cómo se actualizan y cambian los modelos de lenguaje.*
::/pausa
::/practica

---

## Práctica resuelta — Cómo detecté una alucinación con un caso real

::practica{titulo="Atrapa al modelo inventándose una fuente y aprende a verificar"}
**Problema.** 
- Le pides a ChatGPT "5 papers académicos sobre el efecto de Bernoulli en F1".
- Quieres autor, año, journal y DOI.

Te entrega esto:

```text
1. Smith, J. (2018). "Aerodynamic Analysis of Front Wings in Formula 1".
   Journal of Aerospace Engineering, 12(4), pp. 234-245. DOI: 10.1016/jaero.2018.04.012

2. González, M. (2020). "CFD Simulation of Bernoulli Effects in F1".
   Mexican Journal of Fluid Dynamics, 5(2), pp. 87-99. DOI: 10.5555/mjfd.2020.0507
```

Suena bien, demasiado bien. **Vamos a auditarlo.**

**Paso 1 — Identifica afirmaciones verificables.**

- Cada cita tiene 4 datos verificables: autor, journal, año, DOI. 
- Esa es tu superficie de auditoría.

**Paso 2 — Verifica el DOI primero (es el más rápido).**

- Pega `10.1016/jaero.2018.04.012` en doi.org. 
- Resultado: **DOI no encontrado**. Mala señal #1.
- Pega `10.5555/mjfd.2020.0507`. Resultado: **DOI no encontrado**. 
- El prefijo `10.5555` es de prueba — **no se asigna a publicaciones reales**. Confirmado: DOI inventado.

**Paso 3 — Verifica el journal.**

- Busca "Mexican Journal of Fluid Dynamics" en Google y en Scopus. 
- Resultado: **no existe** ese journal. Mala señal #2 confirmada.

**Paso 4 — Confronta al modelo con tu hallazgo.**

Le respondes:
> *"Verifiqué los DOIs que me diste y ninguno existe. ¿De dónde sacaste estas referencias?"*

Respuesta típica del modelo:
> *"Tienes razón, me disculpo. Los DOIs eran ilustrativos y no corresponden a publicaciones reales..."*

::interioriza
Las alucinaciones son como un estudiante que inventa nombres de libros para que su ensayo parezca más pro.
Se leen convincentes, pero si vas a la biblioteca, los libros no existen.
::/interioriza

**Paso 5 — Documenta el patrón.**

| Tarea pedida | Riesgo de alucinación | Cómo verificar |
|---|---|---|
| Citas académicas con DOI | **Muy alto** | DOI.org + Crossref |
| Citas a leyes con artículo | Alto | Diario Oficial |
| Datos estadísticos | Alto | Sitios oficiales (INEGI, OMS) |
| Quotes históricos | Medio | Wikiquote |
| Código que use librerías | Medio-alto | Probarlo en local |
| Resúmenes de un PDF | Bajo | Verificar páginas citadas |

**Paso 6 — Ajusta tu próximo prompt.**

En lugar de "dame 5 papers", pide:
> *"Busca en Perplexity o Google Scholar y devuélveme solo papers cuyos DOI puedas verificar. Si no puedes, dímelo."*

- **Resultado:** bajas la frecuencia de alucinación de 80% a menos de 20%.

> **Lección clave.** Las alucinaciones son un **subproducto del entrenamiento**. 
> La defensa es **diseñar tu workflow** para que todo hecho citable pase por verificación externa.

::pausa{}
**Deducción:** ¿Por qué un modelo de lenguaje puede inventar un DOI de prueba (10.5555) que luce tan realista?
*Pista: recuerda cómo el modelo predice tokens basados en patrones estadísticos.*
::/pausa
::/practica

---

## Práctica resuelta — Configuré un Project con knowledge base y rebajé mis dudas un 70%

::practica{titulo="De ChatGPT vacío a tutor personalizado: el setup paso a paso"}
**Problema.** 
- Llevas 3 semanas usando ChatGPT para estudiar Cálculo.
- Sientes que cada chat empieza de cero.
- Tienes que explicar tu nivel, estilo y temario cada vez.

Vas a configurar un Claude Project (o ChatGPT Project) que **resuelva esto en una sola configuración**.

**Paso 1 — Reúne 3 archivos clave.**

- `temario-calculo-i.pdf` — de tu facultad.
- `apuntes-mias.md` — tus apuntes propios de las 3 unidades.
- `examen-parcial-corregido.pdf` — tu examen con errores marcados.

**Paso 2 — Crea el Project.**

- En Claude.ai → New Project → "Tutor Cálculo I — [tu nombre]". 
- Sube los 3 archivos a Knowledge.

**Paso 3 — Redacta las instrucciones del sistema.**

```text
Eres mi tutor de Cálculo I. Soy estudiante de [nivel].
Usa "temario-calculo-i.pdf" para dudas de notación.

Estilo:
- Empieza con la intuición geométrica.
- Usa analogías cotidianas.
- Haz UNA pregunta socrática al final.

Mis errores (ver examen):
- Confundo regla de la cadena y producto.
- Olvido el dominio al sacar derivada con raíz.
- Me cuesta la segunda derivada.
ALERTA si estoy cerca de cometer estos errores.

Restricciones:
- Nunca des la respuesta directa.
- Si pido resolver, pídeme MI intento primero.
```

**Paso 4 — Prueba con 5 preguntas reales.**

Pega 5 dudas reales de la semana. Mides:

| Pregunta | ¿Usó tu temario? | ¿Aplicó tu estilo? | ¿Te alertó de tus errores? |
|---|---|---|---|
| 1. Derivada de sin(x²) | Sí | Sí | Sí — alertó cadena vs producto |
| 2. Lim de (sin x)/x | Sí | Sí | N/A — fuera de errores típicos |
| 3. Dominio de √(x-3) | Sí | Sí | Sí — recordó el dominio |
| 4. Concavidad de f(x)=x³ | Sí | Parcial | Sí — segunda derivada |
| 5. Regla de cadena triple | Sí | Sí | Sí — alertó explícitamente |

**Paso 5 — Itera.**

- ¿En la pregunta 4 saltó la intuición? 
- Ajustas instrucciones: *"NUNCA saltes la intuición geométrica."*

::interioriza
Un Project es como darle a un tutor particular todo tu historial de exámenes antes de la primera clase.
No pierden tiempo conociéndose, van directo a resolver lo que más te cuesta.
::/interioriza

**Paso 6 — Mide el efecto.**

Una semana después, notas:
- Tiempo de inicio: bajó de 5 min a **30 segundos**.
- Respuestas rechazadas por estilo: de 30% a **menos de 10%**.
- Tutor se anticipa a errores: pasó de **0%** a **70%**.

> **Lección clave.** Un Project bien configurado **multiplica por 3 la utilidad** del LLM. 
> La inversión inicial de 30 min te ahorra unas 8 horas mensuales.

::pausa{}
**Deducción:** ¿Por qué incluir tu examen con errores es el archivo más valioso en Knowledge?
*Pista: piensa en cómo la IA puede usar un patrón de errores pasados para personalizar su ayuda.*
::/pausa
::/practica
