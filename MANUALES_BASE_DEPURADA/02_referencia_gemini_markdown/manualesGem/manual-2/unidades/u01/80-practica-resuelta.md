---
unidad: 1
seccion: practica-resuelta
paginas_objetivo: 1
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

$$v_1 = v_0 + a_1 t_1 = 0 + 25 \times 0.5 = 12.5\,\text{m/s}$$

**Paso 2 — Distancia en fase 1 (MRUA desde reposo).**

$$x_1 = \tfrac{1}{2} a_1 t_1^2 = \tfrac{1}{2}(25)(0.5)^2 = 3.13\,\text{m}$$

**Paso 3 — Distancia restante para llegar a la meta.**

$$x_2 = 20.0 - 3.13 = 16.87\,\text{m}$$

**Paso 4 — Tiempo en fase 2 (MRU a 12.5 m/s).**

$$t_2 = \frac{x_2}{v_1} = \frac{16.87}{12.5} = 1.35\,\text{s}$$

**Paso 5 — Tiempo total.**

$$t_\text{total} = t_1 + t_2 = 0.5 + 1.35 = 1.85\,\text{s}$$

**Paso 6 — Frecuencia de rotación de llantas a 12.5 m/s.**

$$f = \frac{v}{2\pi r} = \frac{12.5}{2\pi \times 0.015} = 132.6\,\text{Hz} = 7,956\,\text{rpm}$$

**Paso 7 — Conclusión y recomendaciones.**

> El coche F1 actual completa la pista en **1.85 s** con velocidad pico de **12.5 m/s** (= 45 km/h). Las llantas giran a casi **8,000 rpm**.
>
> **Para mejorar el tiempo a < 1 s:**
> - Aumentar aceleración inicial (mayor diámetro de boquilla del CO₂, o cartucho con más presión): si $a_1 = 60\,\text{m/s}^2$ durante 0.6 s → velocidad = 36 m/s, tiempo total ≈ 0.8 s.
> - Reducir fricción para mantener velocidad pico: ruedas con rodamientos de bolas, alineación perfecta.
> - Reducir masa del coche: una masa menor con la misma fuerza de empuje (F = ma) → mayor aceleración.

> **Verificación experimental:** los datos reales del sensor de telemetría mostrarán la velocidad instantánea cada 10 ms. Compara los datos con esta predicción: la diferencia te dirá la eficiencia real del cartucho de CO₂ y la magnitud de la fricción.
::/practica

---

::practica{titulo="Tiro parabólico — caída del coche F1 fuera de la rampa final"}
**Problema.** En una pista experimental, tu coche F1 sale por una rampa horizontal a $v_0 = 16\,\text{m/s}$, situada a $h = 0.60\,\text{m}$ sobre un piso liso. Calcula:
1. Tiempo de vuelo hasta tocar el suelo.
2. Alcance horizontal a partir del borde.
3. Velocidad vertical al impacto.
4. Magnitud y ángulo del vector velocidad al impacto.

---

**Paso 1 — Identifica el modelo.** Tiro parabólico horizontal: descomponemos en MRU horizontal y caída libre vertical (independientes).

**Paso 2 — Datos.** $v_{0x}=16\,\text{m/s}$, $v_{0y}=0$, $h=0.60\,\text{m}$, $g=9.8\,\text{m/s}^2$.

**Paso 3 — Tiempo de vuelo (eje y).**

$$h = \tfrac{1}{2} g t^2 \Rightarrow t = \sqrt{\tfrac{2h}{g}} = \sqrt{\tfrac{1.2}{9.8}} = 0.350\,\text{s}$$

**Paso 4 — Alcance horizontal (eje x, MRU).**

$$x = v_{0x} \cdot t = 16 \times 0.350 = 5.60\,\text{m}$$

**Paso 5 — Velocidad vertical al impacto.**

$$v_y = g \cdot t = 9.8 \times 0.350 = 3.43\,\text{m/s}$$

**Paso 6 — Magnitud del vector velocidad al impacto.**

$$|v| = \sqrt{v_{0x}^2 + v_y^2} = \sqrt{16^2 + 3.43^2} = 16.36\,\text{m/s}$$

**Paso 7 — Ángulo bajo la horizontal.**

$$\theta = \arctan\!\left(\frac{v_y}{v_{0x}}\right) = \arctan(3.43/16) = 12.1°$$

**Paso 8 — Conclusión.**

> El coche aterriza a **5.6 m del borde**, con velocidad de **16.4 m/s** inclinada **12° bajo la horizontal**, en **0.35 s**. Diseñen una zona de aterrizaje de al menos 6.5 m con material amortiguador para no destrozar el chasis.
::/practica

---

::practica{titulo="MCU — fuerza centrípeta en la curva final del circuito F1"}
**Problema.** Tu coche F1 toma una curva de radio $r = 4.0\,\text{m}$ a velocidad $v = 12\,\text{m/s}$. Su masa es $m = 0.060\,\text{kg}$ (60 g, balsa con ruedas y cartucho). Calcula:
1. Aceleración centrípeta y compárala con $g$.
2. Fuerza centrípeta sobre el coche.
3. Coeficiente de fricción mínimo necesario para que la llanta no derrape (anticipo a la unidad 2).

---

**Paso 1 — Aceleración centrípeta.**

$$a_c = \frac{v^2}{r} = \frac{12^2}{4.0} = 36\,\text{m/s}^2$$

En unidades de g: $a_c / g = 36/9.8 \approx 3.67\,g$.

**Paso 2 — Fuerza centrípeta.**

$$F_c = m \cdot a_c = 0.060 \times 36 = 2.16\,\text{N}$$

**Paso 3 — Fricción mínima.** Para no derrapar, la fricción debe igualar a $F_c$. Usando $f = \mu \cdot N = \mu \cdot m \cdot g$:

$$\mu_\text{mín} = \frac{a_c}{g} = \frac{36}{9.8} = 3.67$$

**Paso 4 — Diagnóstico.**

> Un coeficiente de **3.67** es **imposible** en una llanta normal (μ típica < 1.0). El coche **derrapará** sin remedio en esa curva a esa velocidad. Soluciones:
> - Reducir velocidad a $v = \sqrt{\mu \cdot g \cdot r}$. Con μ = 0.7: $v_\text{máx} = \sqrt{0.7 \times 9.8 \times 4.0} = 5.24\,\text{m/s}$.
> - Aumentar el radio de la curva (reducir cerradura).
> - Inclinar el peralte (peraltar la curva) para que parte de la fuerza normal aporte componente centrípeta.

**Paso 5 — Aplicación de diseño.**

> El equipo debe rediseñar el circuito o reducir velocidad antes de la curva. El cálculo cinemático **dicta** el diseño mecánico.
::/practica
