---
unidad: 2
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Análisis dinámico completo del coche F1

::practica{titulo="Calcula la fuerza, aceleración y comportamiento del coche F1"}
**Problema.** Tu coche F1 tiene:
- Masa total (incluyendo cartucho): 60 g.
- Cartucho de CO₂: 8 g, libera gas a 150 m/s durante 0.4 s.
- Coeficiente de fricción de rodamiento: μₖ = 0.05.
- Masa del coche sin cartucho descargado: 52 g.
- Pista horizontal de 20 m.

Calcula:
1. Empuje promedio del cartucho (fuerza).
2. Aceleración del coche durante la fase de empuje.
3. Velocidad alcanzada al fin de la fase de empuje.
4. Verificación con conservación de momento.
5. ¿Cuánta energía aporta el cartucho?

---

**Paso 1 — Empuje promedio del cartucho (Tercera Ley + impulso).**

Por conservación de momento, el momento entregado al gas es igual al momento entregado al coche en sentido opuesto:
$$F \cdot \Delta t = m_{gas} \cdot v_{gas}$$
$$F = (0.008)(150) / 0.4 = 3.0\,\text{N}$$

**Empuje promedio del cartucho: 3.0 N.**

**Paso 2 — Aceleración durante el empuje.**

Fuerzas sobre el coche:
- Empuje: 3.0 N hacia adelante.
- Fricción de rodamiento: $F_r = \mu_k \cdot N = 0.05 \times (0.060)(9.8) = 0.029\,\text{N}$ hacia atrás.
- Resistencia del aire: a velocidades iniciales bajas, despreciable.

Fuerza neta: $F_{neta} = 3.0 - 0.029 = 2.97\,\text{N}$.

Aceleración: $a = F_{neta}/m = 2.97/0.060 = 49.5\,\text{m/s}^2$ ≈ 5g.

**Paso 3 — Velocidad al fin de la fase de empuje (MRUA, U1).**

Asumiendo aceleración constante durante 0.4 s:
$$v = at = 49.5 \times 0.4 = 19.8\,\text{m/s}$$

**Velocidad pico: 19.8 m/s ≈ 71 km/h.**

**Paso 4 — Verificación con conservación de momento.**

Momento del gas: $p_{gas} = (0.008)(150) = 1.2\,\text{kg·m/s}$.
Si todo se transfiere idealmente al coche: $v_{coche} = 1.2 / 0.060 = 20\,\text{m/s}$. ✓

(La pequeña diferencia con el paso 3 es porque la fricción consume una pequeña fracción del impulso.)

**Paso 5 — Energía aportada por el cartucho.**

Energía cinética del gas saliente:
$$E_{gas} = \tfrac{1}{2}(0.008)(150)^2 = 90\,\text{J}$$

Energía cinética del coche al fin de la fase de empuje:
$$E_{coche} = \tfrac{1}{2}(0.060)(19.8)^2 = 11.8\,\text{J}$$

**Eficiencia de transferencia: $E_{coche}/E_{gas} = 11.8/90 = 13\%$.** El resto se queda como energía cinética en los gases que escaparon (lo cual es inevitable: la mayor parte de la energía la lleva el gas, no el coche).

**Paso 6 — Distancia recorrida durante el empuje.**

Por MRUA: $x = \tfrac{1}{2}at^2 = \tfrac{1}{2}(49.5)(0.4)^2 = 3.96\,\text{m}$.

**Paso 7 — Tiempo total de la carrera (después del empuje).**

Distancia restante: $20 - 3.96 = 16.04\,\text{m}$.

Después del empuje, fricción frena al coche con desaceleración:
$$a_{frenado} = -\mu_k g = -(0.05)(9.8) = -0.49\,\text{m/s}^2$$

Velocidad final tras recorrer 16.04 m:
$$v_f^2 = (19.8)^2 + 2(-0.49)(16.04) = 392 - 15.7 = 376.3$$
$$v_f = 19.4\,\text{m/s}$$

Casi sin pérdida de velocidad. Tiempo en fase 2:
$$t_2 = \frac{v_f - v_0}{a} = \frac{19.4 - 19.8}{-0.49} = 0.82\,\text{s}$$

(Aproximadamente $t_2 \approx 16.04/19.6 = 0.82\,\text{s}$ usando velocidad media.)

**Tiempo total: $0.4 + 0.82 = 1.22\,\text{s}$.**

**Paso 8 — Conclusión y mejoras.**

> El coche F1 actual completa la pista en **1.22 s** con velocidad pico de 19.8 m/s y eficiencia de transferencia de energía del 13 %. Aceleración máxima: ~5g.
>
> **Mejoras para reducir tiempo:**
> 1. **Reducir masa**: si bajas a 30 g (sin cartucho descargado a 22 g), $a = 3.0/0.030 = 100\,\text{m/s}^2$. Tiempo total ~0.7 s.
> 2. **Reducir fricción**: rodamientos de bolas pueden bajar μₖ a 0.01, recuperando 80 % del frenado.
> 3. **Mejor boquilla**: una boquilla más estrecha aumenta la velocidad del gas y por tanto el empuje.
> 4. **Aerodinámica** (más fuerte a velocidades altas, ver U7).

> **Verificación experimental con Tracker** (U1) confirmará si los datos reales se aproximan a esta predicción.
::/practica

---

::practica{titulo="Equilibrio rotacional — chasis del F1 sobre el balance"}
**Problema.** El chasis del coche F1 se apoya en dos llantas separadas $L = 0.20$ m. La masa total es $m = 0.060$ kg. El centro de masa está a $d = 0.07$ m de la llanta delantera. Calcula:
1. Fuerza normal en cada eje.
2. ¿Qué pasa si el centro de masa se mueve a $d = 0.13$ m?
3. ¿Cuánto torque máximo del motor se puede aplicar al eje trasero antes de que la llanta delantera levante (despegue)?

---

**Paso 1 — Diagrama y datos.**

> El chasis está en equilibrio: $\sum F = 0$ y $\sum \tau = 0$. Llamamos $N_1$ a la normal delantera y $N_2$ a la trasera. Peso $W = mg = 0.060 \times 9.8 = 0.588\,\text{N}$.

**Paso 2 — Suma de fuerzas (vertical).**

$$N_1 + N_2 = W = 0.588\,\text{N}$$

**Paso 3 — Suma de torcas en torno a la llanta delantera.**

$$N_2 \cdot L = W \cdot d \Rightarrow N_2 = \frac{W d}{L} = \frac{0.588 \times 0.07}{0.20} = 0.206\,\text{N}$$

**Paso 4 — Normal delantera.**

$$N_1 = W - N_2 = 0.588 - 0.206 = 0.382\,\text{N}$$

> Reparto: 65 % delantera, 35 % trasera. Coherente con un centro de masa adelantado.

**Paso 5 — Caso $d = 0.13$ m (centro de masa atrás).**

$$N_2 = \frac{0.588\times 0.13}{0.20} = 0.382\,\text{N}; \quad N_1 = 0.206\,\text{N}$$

> El reparto se invierte (35 %/65 %). Tracción mejora, pero estabilidad direccional empeora.

**Paso 6 — Torque máximo antes de levantar la llanta delantera.**

> El coche levanta la llanta delantera cuando $N_1 = 0$. Esto sucede cuando la torca debida al empuje del motor (aplicado a altura $h$ del eje del piso, asumamos $h = 0.03$ m) compensa la torca del peso respecto a la llanta trasera:
$$F_\text{empuje}\cdot h = W\cdot(L - d)$$
$$F_\text{empuje} = \frac{0.588\times (0.20-0.07)}{0.03} = 2.55\,\text{N}$$

**Paso 7 — Conclusión de diseño.**

> Con $d=0.07$ m, un empuje de 2.55 N basta para levantar la llanta delantera. Como el cartucho entrega ~3 N, **el coche tenderá a hacer caballito**. Soluciones: bajar la altura $h$ del eje de empuje, mover el centro de masa hacia atrás, agregar peso delante o un alerón con downforce.
::/practica

---

::practica{titulo="Resorte y oscilación — sistema de suspensión del coche F1"}
**Problema.** Tu coche F1 incorpora un resorte amortiguador en el eje delantero con $k = 250\,\text{N/m}$. La masa que sostiene cada resorte es $m = 0.025$ kg (un cuarto del coche cargado). Calcula:
1. Compresión estática del resorte por el peso.
2. Período y frecuencia natural de oscilación vertical.
3. Si pasa una imperfección de 4 mm a 12 m/s, ¿cuántas oscilaciones completa antes de cruzar 1.0 m?

---

**Paso 1 — Compresión estática (Hooke).**

$$F = kx \Rightarrow x_\text{est} = \frac{mg}{k} = \frac{0.025 \times 9.8}{250} = 9.8\times 10^{-4}\,\text{m} = 0.98\,\text{mm}$$

**Paso 2 — Período natural (oscilador armónico).**

$$T = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{0.025}{250}} = 2\pi\sqrt{10^{-4}} = 0.0628\,\text{s}$$

**Paso 3 — Frecuencia natural.**

$$f = 1/T = 1/0.0628 = 15.9\,\text{Hz}$$

**Paso 4 — Tiempo en cruzar 1.0 m a 12 m/s.**

$$\Delta t = 1.0/12 = 0.0833\,\text{s}$$

**Paso 5 — Número de oscilaciones.**

$$n = \Delta t / T = 0.0833 / 0.0628 = 1.33$$

**Paso 6 — Conclusión.**

> El resorte completa **~1.3 oscilaciones** antes de cruzar la zona afectada. Si la frecuencia de las imperfecciones de la pista coincide con $f_\text{nat}\approx 16$ Hz (es decir, baches separados ~0.75 m a 12 m/s), entrarías en **resonancia**: el coche brincaría salvajemente. Solución: cambiar $k$ o agregar amortiguador.
::/practica
