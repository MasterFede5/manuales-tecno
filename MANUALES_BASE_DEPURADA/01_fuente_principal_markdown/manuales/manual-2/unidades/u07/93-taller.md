---
unidad: 7
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Túnel de viento casero para el alerón del F1

Un taller de 60 minutos donde tu equipo F1 Albatros construye un túnel de viento de bajo costo, mide downforce y drag de tres variantes de alerón con un dinamómetro casero y elige la mejor para tu pista. Aplica los subtemas 7.2 (Bernoulli, continuidad) y conecta con la implementación CFD.

::albatros{titulo="Taller — Túnel de viento de cartón y mediciones de fuerzas aerodinámicas" tipo="experimento" tiempo="60 min"}
**Pregunta detonadora.** ¿La predicción CFD de tu alerón coincide con la realidad? ¿Cómo lo verificarías sin un túnel de viento profesional?

**Lo que harás.** Construirás un túnel de viento sencillo con caja de cartón y un ventilador de mesa o secadora de aire. Montarás tres alerones de prueba sobre un balance hecho con resorte calibrado y medirás downforce y drag para tres ángulos de ataque (5°, 15° y 25°). Compararás con la teoría de Bernoulli.

**Materiales.**
- Caja de cartón de ~50 × 30 × 30 cm.
- Ventilador de mesa o secadora de pelo.
- 3 alerones de cartón rígido o foamboard del mismo ancho (8 cm) con ángulos de ataque distintos (5°, 15°, 25°).
- Dos resortes calibrados (ver U2) o ligas elásticas.
- Hilo, regla, transportador, marcadores.
- Anemómetro de mano o app **Anemómetro** (mide velocidad del aire) o medición indirecta con bola de ping-pong colgada.
- Báscula de cocina (1 g) y báscula de gancho.

**Pasos.**

1. **Construye el túnel.** Quita una tapa de la caja y abre orificios en las dos caras opuestas más cortas: una para el ventilador (entrada), otra para la salida. Instala el ventilador a la entrada.

2. **Mide la velocidad del flujo.** Con anemómetro o estimando con una pelota colgada del techo del túnel: si la pelota se inclina θ con un péndulo de hilo, $v \approx \sqrt{(g\tan\theta) L}$ con $L$ longitud del hilo. Apunta a $v \geq 5$ m/s.

3. **Monta el balance de fuerzas.** Sostén el alerón con dos hilos pegados al techo del túnel: uno vertical (mide downforce con resorte 1) y uno horizontal (mide drag con resorte 2). Calibra ambos resortes antes con masas de 5–50 g (ver Hooke, U2.6).

4. **Variante A (ángulo 5°).** Coloca el alerón en el túnel, prende el ventilador y mide:
   - Elongación del resorte vertical → $F_\text{down}$.
   - Elongación del resorte horizontal → $F_\text{drag}$.
   Repite 3 veces y promedia.

5. **Variantes B (15°) y C (25°).** Repite el procedimiento.

6. **Tabla experimental.**

   | Variante | Ángulo | $v$ (m/s) | $F_\text{down}$ (N) | $F_\text{drag}$ (N) | DF/Drag |
   |---|---:|---:|---:|---:|---:|
   | A | 5° | | | | |
   | B | 15° | | | | |
   | C | 25° | | | | |

7. **Cálculo teórico (Bernoulli).** Para la variante A, asume que el alerón acelera el aire un $k$ % en la cara inferior. Con $v_1 = (1+k)v_0$, calcula:
   $$\Delta P = \tfrac{1}{2}\rho(v_1^2 - v_0^2), \quad F_\text{down} = \Delta P \cdot A_a$$
   Ajusta $k$ para que coincida con tu medición. Hazlo para las tres variantes.

8. **Drag teórico.** $F_\text{drag} = \tfrac{1}{2}C_d \rho v^2 A_f$ con $C_d \approx 0.05 + 0.02\theta°$ (modelo lineal aproximado para alerones simples). Compara con la medición.

9. **Eficiencia.** Calcula DF/Drag para cada variante y grafícalo vs ángulo de ataque. Identifica el máximo.

10. **Decisión de equipo.** Para una pista con 70 % de curvas y 30 % de rectas: prioriza DF. Para 30 %/70 %: prioriza minimizar drag. Recomendar la variante adecuada en cada escenario con justificación numérica.

11. **Validación cruzada.** Si tu equipo hizo CFD en SimScale (ver implementación), compara los tres valores experimentales con los tres simulados. Discute el error porcentual.

12. **Cierre.** Cada equipo entrega la bitácora.

**Entregable.** Bitácora de 1.5 páginas con: foto del túnel y del balance, tabla experimental con tres variantes, cálculo teórico con Bernoulli para una variante, gráfica DF/Drag vs ángulo, recomendación con justificación numérica.

**Rúbrica de evaluación.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Túnel y balance | sin medir $v$ ni calibrar | con $v$ medido y resortes calibrados | + 3 corridas por variante |
| Tabla de fuerzas | una variante | tres variantes con DF y drag | + cifras significativas y unidades |
| Comparación con teoría | sin cálculo | Bernoulli para una variante | + comparación con CFD si aplica |
| Recomendación | genérica | específica para una pista | + dos escenarios con justificación |
::/albatros
