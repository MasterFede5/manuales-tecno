---
unidad: 1
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Cinemática del coche F1 con cronómetro y celular

Un taller de 60 minutos para que tu equipo F1 Albatros mida con instrumentos reales la velocidad media y la aceleración del prototipo, compare con un modelo MRUA y descubra dónde se pierde tiempo. Aplica los subtemas 1.3 (MRU), 1.4 (MRUA) y 1.7 (MCU).

::albatros{titulo="Taller — Tu primera telemetría del coche F1" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Tu coche F1 acelera todo el tiempo o entra en MRU después de cierto punto? ¿Cuánto tiempo gana o pierde respecto al modelo teórico de aceleración constante?

**Lo que harás.** Mediremos posición vs tiempo con dos métodos (cronómetro humano y video del celular) y construiremos las gráficas x-t y v-t para detectar las dos fases del movimiento.

**Materiales.**
- Coche F1 escolar o cualquier carrito con propulsión simple (resorte, gravedad por rampa, CO₂).
- Cinta métrica de 5 m o flexómetro.
- Cinta adhesiva de color para marcar posiciones.
- 4 cronómetros (los del celular sirven) y 4 cronometristas.
- Smartphone con cámara a 60 fps (o 30 fps mínimo).
- Hoja de registro con tabla preimpresa.

**Pasos.**

1. **Pista.** Marquen 5 posiciones con cinta sobre el piso: 0 m, 4 m, 8 m, 12 m y 16 m desde la línea de salida. Cada cronometrista se coloca en una marca a partir de los 4 m.

2. **Filmación.** Coloquen el celular sobre un tripié o caja a ~3 m de la pista, lateral, encuadre que cubra los 16 m. Pongan en grabación a 60 fps.

3. **Lanzamiento 1.** Liberen el coche; al pasar por cada marca, el cronometrista correspondiente detiene su cronómetro. Anoten en la tabla los 4 tiempos.

4. **Repitan tres veces** con la misma configuración. Saquen el promedio de tiempo a cada distancia.

5. **Tabla de datos.** Construyan en cuaderno o Sheets:

   | x (m) | t₁ (s) | t₂ (s) | t₃ (s) | t̄ (s) | v̄ tramo (m/s) |
   |---:|---:|---:|---:|---:|---:|
   | 0 | 0 | 0 | 0 | 0 | — |
   | 4 |  |  |  |  |  |
   | 8 |  |  |  |  |  |
   | 12 |  |  |  |  |  |
   | 16 |  |  |  |  |  |

   La velocidad media de cada tramo se calcula como $\bar v = \Delta x / \Delta t$.

6. **Gráfica x-t.** Plotear (papel milimétrico o GeoGebra) los puntos $(\bar t, x)$. Identifiquen visualmente qué tramo es **parabólico** (MRUA) y cuál se vuelve **lineal** (MRU).

7. **Gráfica v-t.** Plotear $(\bar t, \bar v_\text{tramo})$ en el punto medio del intervalo. La pendiente del primer tramo será la **aceleración promedio** del arranque.

8. **Cálculo de la aceleración.** Si el coche llega a velocidad pico $v_p$ a los $t_p$ s, calculen $a = v_p / t_p$. Comparen con la aceleración nominal del CO₂ (~30 m/s²).

9. **Análisis con video.** Reviendo el video frame por frame en una app como Phyphox o Tracker, refinen la posición a t = 0.1 s, 0.2 s, 0.3 s. Comparen con los datos del cronómetro: ¿cuántos % de error humano hay?

10. **Identifiquen pérdidas.** ¿Hay un tramo donde la velocidad **decrece**? Eso es fricción dominando. ¿Hay un tramo de MRU "casi perfecto"? Anoten dónde inicia y termina.

11. **Diagnóstico de mejora.** Cada equipo propone **una** modificación al coche (peso, ruedas, alineación, ángulo de salida) y predice el impacto numérico esperado.

12. **Mini-bitácora.** Escriban media página con: configuración, tabla, gráficas, aceleración medida, fase MRU detectada y propuesta de mejora.

**Entregable.** Mini-bitácora de 1 página con tabla, dos gráficas (x-t y v-t) y propuesta de mejora numérica.

**Rúbrica de evaluación.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Toma de datos (3 corridas, 4 marcas) | datos parciales o sin promedio | 3 corridas con promedios | + incertidumbre estadística (desviación) |
| Gráficas x-t y v-t | 1 gráfica o sin escalas | 2 gráficas con ejes correctos | + identificación clara de fase MRUA y MRU |
| Cálculo de aceleración | sin cálculo | $a$ numérico con unidades | $a$ con cifras significativas + comparación con teórico |
| Propuesta de mejora | sin propuesta | propuesta cualitativa | propuesta con predicción numérica de impacto |
::/albatros
