---
unidad: 3
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — De prompt malo a prompt profesional

::practica{titulo="Refina un prompt vago con anatomía completa"}
**Problema:** Tu compañero recibe respuestas inútiles de ChatGPT con este prompt:
`Hazme un resumen del libro de física de bachillerato.`

Tu tarea:
- Identificar antipatrones.
- Aplicar anatomía R-T-C-R-F-E.
- Evaluar técnicas avanzadas (Few-shot/CoT).

**1. Antipatrones identificados**
- **Vaguedad:** ¿Cuál libro? ¿Qué edición?
- **Sin contexto:** ¿Para qué nivel? ¿Qué profundidad?
- **Sin formato:** ¿Texto, viñetas, palabras?
- **Suposiciones:** Asume el más popular.
- **Sin métrica de éxito:** ¿Qué es un "buen" resumen?

**2. Anatomía completa aplicada**
```text
[ROL] Eres tutor de física (SEP/UNAM).
[TAREA] Resume "Física General" de Tippens (unidades 1-5).
[CONTEXTO] Alumno CCH para examen. Prioriza conceptos.
[RESTRICCIONES] Max 1500 palabras, sin cálculo.
[FORMATO] Markdown por unidad (Concepto, fórmulas, ejemplo, pregunta).
[EJEMPLO ÚNICO] (Formato de la Unidad 1 como Few-shot).
```

::interioriza
Imagina que vas a la peluquería y pides "corte de cabello".
Si no especificas el estilo, el peluquero asume y te corta al ras.
Un prompt sin contexto es dejar tu corte al azar.
::/interioriza

**3. Reflexión y Mejora**
- Pasamos de 9 palabras a 320 palabras.
- Invertir 5 min en el prompt ahorra 30 min de iteraciones.
- Se vuelve una plantilla reutilizable.

::pausa{}
**Deduce:** ¿Por qué no usamos *Chain of Thought* aquí?
*Respuesta:* La tarea es de estructuración y resumen, no requiere razonamiento lógico paso a paso.
::/pausa
::/practica

---

## Práctica resuelta — Few-shot para clasificación

::practica{titulo="Diseña clasificador de correos con Few-shot"}
**Problema:** Zero-shot da baja precisión al clasificar correos personales.

**1. Definir categorías**
- Familia: Pareja y parientes.
- Escuela: Dominio institucional.
- Trabajo: Empleador, clientes.
- Suscripciones: Newsletters, marketing.
- Basura: Spam.

**2. Selección de ejemplos clave (Casos límite)**
- `profe@unam.mx` (Escuela, no suscripción).
- `ofertas@platzi.com` (Suscripciones, no escuela).
- `tia@gmail.com` (Familia).
- `soporte@banco.com` (Trabajo).

**3. Resultado**
- **Zero-shot:** 70% precisión.
- **Few-shot (4 ejemplos):** 95% precisión.

::interioriza
El modelo tiene "sentido común" genérico, no el tuyo.
Few-shot es como mostrarle a un nuevo empleado 4 ejemplos de cómo te gusta tu café.
Sin probarlo antes, ajusta su criterio al tuyo.
::/interioriza

::pausa{}
**Deduce:** Si la precisión no mejora con 4 ejemplos, ¿qué harías?
*Respuesta:* Agregar ejemplos específicos de los errores persistentes (casos borde).
::/pausa
::/practica

---

## Práctica resuelta — Chain of Thought salva problemas matemáticos

::practica{titulo="CoT para resolver edades"}
**Problema:** Acertijo de edades donde Zero-shot falla matemáticamente.

**1. Prompt Zero-shot**
- Respuesta directa: "35 y 35 años".
- Resultado: **Error**. Falla las condiciones del problema.

**2. Prompt CoT**
- Se obliga a definir variables, tiempos, y ecuaciones paso a paso.
- Resultado: 40 y 30 años. **Correcto**.

**3. Análisis de impacto**
- **Costo:** 4x más tokens y más tiempo (8s vs 2s).
- **Beneficio:** Precisión absoluta.

::interioriza
CoT es como pedirle a un estudiante que muestre su procedimiento en el examen.
Si solo pone el resultado, la probabilidad de error al calcular mentalmente es alta.
Obligarlo a escribir los pasos, fuerza la lógica.
::/interioriza

::pausa{}
**Deduce:** ¿En qué casos NO usarías CoT?
*Respuesta:* Tareas creativas, traducciones simples, o cuando el tiempo de respuesta es crítico.
::/pausa
::/practica
