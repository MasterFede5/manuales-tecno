---
unidad: 1
seccion: practica-resuelta
paginas_objetivo: 0.5
---

## Práctica resuelta — Análisis cinemático completo del coche F1

::practica{titulo="Predice el tiempo de carrera del coche F1 escolar"}
**Problema.** Tu coche F1 tiene las siguientes características de telemetría:
- Aceleración inicial por CO₂: $a_1 = 25\,\text{m/s}^2$ durante $t_1 = 0.5\,\text{s}$.
- Después de los 0.5 s, la velocidad se mantiene aproximadamente constante (asumiendo fricción mínima).
- Pista: 20.0 m de longitud.
- Radio de las llantas: 15 mm.

Calcula:
1. Velocidad alcanzada al fin de la fase de aceleración.
2. Distancia recorrida en la fase de aceleración.
3. Tiempo total de carrera.
4. Frecuencia de rotación de las llantas a velocidad de crucero.

---

**Paso 1 — Velocidad al fin de fase 1 (MRUA desde reposo).**
- $v_1 = v_0 + a_1 t_1$
- $v_1 = 0 + 25 \times 0.5 = 12.5\,\text{m/s}$

**Paso 2 — Distancia en fase 1 (MRUA desde reposo).**
- $x_1 = \tfrac{1}{2} a_1 t_1^2$
- $x_1 = \tfrac{1}{2}(25)(0.5)^2 = 3.13\,\text{m}$

**Paso 3 — Distancia restante para llegar a la meta.**
- $x_2 = 20.0 - 3.13 = 16.87\,\text{m}$

**Paso 4 — Tiempo en fase 2 (MRU a 12.5 m/s).**
- $t_2 = \frac{x_2}{v_1} = \frac{16.87}{12.5} = 1.35\,\text{s}$

**Paso 5 — Tiempo total.**
- $t_\text{total} = t_1 + t_2 = 0.5 + 1.35 = 1.85\,\text{s}$

**Paso 6 — Frecuencia de rotación de llantas a 12.5 m/s.**
- $f = \frac{v}{2\pi r} = \frac{12.5}{2\pi \times 0.015} = 132.6\,\text{Hz} = 7,956\,\text{rpm}$

**Paso 7 — Conclusión y recomendaciones.**
> El coche F1 actual completa la pista en **1.85 s** con velocidad pico de **12.5 m/s**.
> 
> **Para mejorar el tiempo a < 1 s:**
> - Aumentar aceleración inicial: usar cartucho con más presión.
> - Reducir fricción: ruedas con rodamientos de bolas.
> - Reducir masa: misma fuerza, mayor aceleración.
::/practica

::interioriza
**El efecto "cohete y tren"**
Imagina tu coche F1 en dos etapas: primero actúa como un **cohete espacial** (acelerando violentamente mientras se quema el CO₂) y luego viaja como un **tren bala** (manteniendo su velocidad por inercia el resto de la pista). 
::/interioriza

::pausa{tipo="deduccion"}
1. Si el coche perdiera una rueda a mitad de camino, ¿qué pasaría con la "fase de tren bala"?
2. ¿Por qué es más importante una aceleración altísima al principio que al final?
::/pausa

---

::practica{titulo="Tiro parabólico — caída del coche F1 fuera de la rampa final"}
**Problema.** En una pista experimental, tu coche F1 sale por una rampa horizontal a $v_0 = 16\,\text{m/s}$, situada a $h = 0.60\,\text{m}$ sobre un piso liso. Calcula el tiempo de vuelo, alcance horizontal, y velocidad de impacto.

**Paso 1 — Identifica el modelo.** 
- Tiro parabólico horizontal: MRU en X, caída libre en Y.

**Paso 2 — Datos.** 
- $v_{0x}=16\,\text{m/s}$, $v_{0y}=0$, $h=0.60\,\text{m}$, $g=9.8\,\text{m/s}^2$.

**Paso 3 — Tiempo de vuelo (eje y).**
- $t = \sqrt{\tfrac{2h}{g}} = \sqrt{\tfrac{1.2}{9.8}} = 0.350\,\text{s}$

**Paso 4 — Alcance horizontal (eje x, MRU).**
- $x = v_{0x} \cdot t = 16 \times 0.350 = 5.60\,\text{m}$

**Paso 5 — Velocidad vertical al impacto.**
- $v_y = g \cdot t = 9.8 \times 0.350 = 3.43\,\text{m/s}$

**Paso 6 — Magnitud y Ángulo.**
- $|v| = \sqrt{16^2 + 3.43^2} = 16.36\,\text{m/s}$
- $\theta = \arctan(3.43/16) = 12.1°$

**Paso 8 — Conclusión.**
> El coche aterriza a **5.6 m del borde**, con velocidad de **16.4 m/s** inclinada **12° bajo la horizontal**. Diseñen una zona de aterrizaje de al menos 6.5 m.
::/practica

::interioriza
**El salto del acantilado**
Lanzar una moneda horizontalmente desde un acantilado o dejarla caer verticalmente toman el mismo tiempo en llegar al suelo. La gravedad empuja por igual sin importar la velocidad frontal.
::/interioriza

::pausa{tipo="deduccion"}
1. Si el coche F1 pesara el doble, ¿caería más rápido?
2. ¿Aumentar la velocidad inicial de $16\,\text{m/s}$ a $30\,\text{m/s}$ afecta el tiempo en el aire?
::/pausa

---

::practica{titulo="MCU — fuerza centrípeta en curva F1"}
**Problema.** Tu coche toma una curva de radio $r = 4.0\,\text{m}$ a velocidad $v = 12\,\text{m/s}$. Masa $m = 0.060\,\text{kg}$. Calcula aceleración, fuerza centrípeta y coeficiente de fricción necesario.

**Paso 1 — Aceleración centrípeta.**
- $a_c = \frac{v^2}{r} = \frac{12^2}{4.0} = 36\,\text{m/s}^2 \approx 3.67\,g$

**Paso 2 — Fuerza centrípeta.**
- $F_c = m \cdot a_c = 0.060 \times 36 = 2.16\,\text{N}$

**Paso 3 — Fricción mínima.**
- $\mu_\text{mín} = \frac{a_c}{g} = \frac{36}{9.8} = 3.67$

**Paso 4 — Diagnóstico y aplicación.**
> Un coeficiente de **3.67** es imposible en llanta normal. Derrapará.
> **Soluciones:** Reducir velocidad antes de curva, aumentar radio, o inclinar (peraltar) la pista.
::/practica

::interioriza
Imagínate tomando una curva muy cerrada en bicicleta mientras vas a toda velocidad sobre piso mojado. 
Exactamente eso le pasaría al F1 de 60g si la pista fuera plana.
::/interioriza

::pausa{}
**Pregunta de deducción:** 
¿Por qué en los velódromos o en pistas de NASCAR las curvas están fuertemente inclinadas (peraltadas)?
::/pausa
