---
unidad: 6
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Circuito y comunicación del coche F1

::practica{titulo="Diseña el circuito y red de comunicación del coche F1"}
**Problema.** El coche F1 tiene los siguientes componentes:
- Microcontrolador ESP32 (3.3 V, 80 mA).
- Sensor IR de línea (5 V, 20 mA).
- LED indicador (3 V, 10 mA).
- Batería de litio LiPo (3.7 V, 1000 mAh).
- Wifi a 2.4 GHz con potencia 100 mW.

Calcula:
1. Resistencia total y consumo del circuito.
2. Tiempo de operación con la batería.
3. Longitud de onda del wifi.
4. Energía por fotón emitido.

---

**Paso 1 — Análisis del circuito en paralelo.**

Cada componente conectado en paralelo recibe el mismo voltaje (3.7 V de la batería). La corriente total es la suma de cada uno:
$$I_{total} = 80 + 20 + 10 = 110\,\text{mA}$$

(Asumimos reguladores que adaptan los voltajes; en realidad cada componente puede requerir resistencias específicas).

**Paso 2 — Tiempo de operación.**

$$t = \frac{1000\,\text{mAh}}{110\,\text{mA}} = 9.1\,\text{horas}$$

Tiempo de operación a corriente constante.

**Paso 3 — Longitud de onda del wifi.**

$$\lambda = c/f = (3 \times 10^8)/(2.4 \times 10^9) = 0.125\,\text{m} = 12.5\,\text{cm}$$

**Paso 4 — Energía por fotón.**

$$E = hf = (6.626 \times 10^{-34})(2.4 \times 10^9) = 1.59 \times 10^{-24}\,\text{J}$$

Equivale a $9.9 \times 10^{-6}$ eV. Energía minúscula por fotón, pero billones de fotones por segundo dan los 100 mW totales.

**Paso 5 — Conclusión.**

> El coche F1 con sus 4 componentes electrónicos básicos opera ~9 horas con una batería LiPo de 1000 mAh. La comunicación wifi a 12.5 cm de longitud de onda transmite datos a la base sin cables.
>
> **Recomendaciones:**
> - El consumo dominante es el ESP32 (73 % del total). Usar modos de bajo consumo cuando no transmite reduciría dramáticamente el consumo.
> - Para extender autonomía, considerar batería de 2000 mAh (operación 18 h).
::/practica

---

::practica{titulo="Análisis de un divisor de tensión para el sensor IR del coche F1"}
**Problema.** El sensor IR del coche F1 entrega una salida analógica de 0 a 5 V, pero el ADC del ESP32 solo tolera hasta 3.3 V. Necesitas un divisor de tensión con dos resistencias para llevar 5 V a 3.0 V con corriente máxima de 1 mA. Calcula:
1. Razón de división requerida.
2. Valores de las dos resistencias.
3. Potencia disipada en cada una.

---

**Paso 1 — Razón de división.**

$$\frac{V_\text{out}}{V_\text{in}} = \frac{R_2}{R_1+R_2} = \frac{3.0}{5.0} = 0.6$$

**Paso 2 — Restricción de corriente.** Para $I_\text{máx} = 1$ mA con $V_\text{in} = 5$ V:

$$R_1 + R_2 = V/I = 5/0.001 = 5\,000\,\Omega = 5\,\text{k}\Omega$$

**Paso 3 — Sistema de dos ecuaciones.**

> $R_2 = 0.6(R_1+R_2) = 0.6\times 5\,000 = 3\,000\,\Omega$
> $R_1 = 5\,000 - 3\,000 = 2\,000\,\Omega$

**Paso 4 — Valores estándar disponibles.**

> Usar 2 kΩ y 3 kΩ (estándar). $V_\text{out}$ real = $5\times 3/(2+3) = 3.0$ V ✓.

**Paso 5 — Potencia disipada.**

$$P_1 = I^2 R_1 = (10^{-3})^2 \times 2\,000 = 2\times 10^{-3}\,\text{W} = 2\,\text{mW}$$
$$P_2 = I^2 R_2 = 10^{-6}\times 3\,000 = 3\,\text{mW}$$

**Paso 6 — Conclusión.**

> Resistencias de 1/8 W toleran sin problema. La corriente de 1 mA es despreciable en términos de batería (extrae ~0.1 % de la capacidad por hora). Si el sensor tiene impedancia de salida significativa, considerar un buffer de op-amp.
::/practica

---

::practica{titulo="Inducción de Faraday — generador casero del coche F1"}
**Problema.** Un equipo decide instalar un mini-generador en el eje del coche F1: una bobina de $N = 200$ vueltas y área $A = 4\,\text{cm}^2$ que gira a $\omega = 250$ rad/s en un campo $B = 0.05$ T. Calcula:
1. Flujo magnético máximo en la bobina.
2. fem máxima inducida.
3. Si la bobina alimenta un LED indicador (2 V, 10 mA), ¿enciende?

---

**Paso 1 — Flujo máximo.**

$$\Phi_\text{máx} = N B A = 200 \times 0.05 \times 4\times 10^{-4} = 4\times 10^{-3}\,\text{Wb}$$

**Paso 2 — fem máxima (rotación uniforme).**

$$\varepsilon_\text{máx} = N B A \omega = 200 \times 0.05 \times 4\times 10^{-4} \times 250 = 1.0\,\text{V}$$

**Paso 3 — fem RMS.**

$$\varepsilon_\text{rms} = \varepsilon_\text{máx}/\sqrt{2} \approx 0.71\,\text{V}$$

**Paso 4 — ¿Alimenta el LED?**

> No. Para un LED rojo (umbral ≥ 1.8 V) la fem está por debajo. Soluciones: aumentar $N$, $A$, $B$ o $\omega$. Por ejemplo, duplicando $N$ a 400 → $\varepsilon_\text{máx}=2$ V (apenas suficiente). Multiplicar $\omega$ a 500 rad/s también funciona.

**Paso 5 — Conclusión.**

> Para autoalimentar un LED desde el eje del coche, se requieren al menos **400 vueltas** o un imán más fuerte. Como el coche F1 dura ~2 s en pista, el generador serviría de demostración pero no para alimentar instrumentación durante la carrera (mejor batería LiPo).
::/practica
