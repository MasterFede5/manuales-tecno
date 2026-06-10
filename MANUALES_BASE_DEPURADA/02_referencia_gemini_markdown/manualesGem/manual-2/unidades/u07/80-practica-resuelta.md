---
unidad: 7
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Downforce y drag del alerón F1

::practica{titulo="Calcula el downforce y drag del alerón trasero de tu coche F1"}
**Problema.** Tu coche F1 escolar tiene los siguientes datos:

- Velocidad de carrera: $v = 80\,\text{km/h} = 22.2\,\text{m/s}$.
- Densidad del aire (20 °C, 1 atm): $\rho = 1.20\,\text{kg/m}^3$.
- Alerón trasero invertido, perfil simple, área proyectada en planta $A_a = 18\,\text{cm}^2 = 1.8 \times 10^{-3}\,\text{m}^2$.
- El alerón acelera el aire en la cara inferior un 50 % respecto a la velocidad libre del coche.
- Coeficiente de drag del coche (sin alerón): $C_{d0} = 0.45$.
- Penalización del alerón al $C_d$ total: $\Delta C_d = 0.30$ (crece a 0.75 con alerón).
- Área frontal del coche: $A_f = 25\,\text{cm}^2 = 2.5 \times 10^{-3}\,\text{m}^2$.

Calcula:

1. La velocidad del aire bajo el alerón.
2. La diferencia de presión entre la cara superior y la inferior del alerón.
3. El downforce (fuerza hacia abajo) generado.
4. El drag total del coche en carrera.
5. ¿Cuántas veces el peso del coche (50 g) representa el downforce?

---

**Paso 1 — Velocidad bajo el alerón.**

El aire libre llega al alerón a $v_0 = 22.2\,\text{m/s}$. La cara inferior del perfil acelera el flujo un 50 %:

$$v_1 = 1.5 \cdot v_0 = 1.5 \times 22.2 = 33.3\,\text{m/s}$$

**Paso 2 — Diferencia de presión (Bernoulli).**

A la misma altura, la suma $P + \tfrac{1}{2}\rho v^2$ es constante. Llamando $P_0$ a la presión sobre el alerón (donde el aire viaja a $v_0$) y $P_1$ a la presión bajo el alerón ($v_1$):

$$P_0 + \tfrac{1}{2}\rho v_0^2 = P_1 + \tfrac{1}{2}\rho v_1^2$$

$$\Delta P = P_0 - P_1 = \tfrac{1}{2}\rho\, (v_1^2 - v_0^2)$$

$$\Delta P = \tfrac{1}{2}(1.20)(33.3^2 - 22.2^2) = 0.60 \times (1109 - 493) = 370\,\text{Pa}$$

> Bajo el alerón hay 370 Pa **menos** presión que arriba.

**Paso 3 — Downforce.**

La fuerza neta hacia abajo sobre el alerón es la diferencia de presión multiplicada por su área:

$$F_{down} = \Delta P \cdot A_a = 370 \times 1.8 \times 10^{-3} = 0.67\,\text{N}$$

**Paso 4 — Drag total.**

Con el alerón puesto, $C_d = 0.75$:

$$F_{drag} = \tfrac{1}{2}\, C_d\, \rho\, v^2\, A_f$$

$$F_{drag} = 0.5 \times 0.75 \times 1.20 \times (22.2)^2 \times 2.5 \times 10^{-3}$$

$$F_{drag} = 0.555\,\text{N}$$

**Paso 5 — Comparación con el peso.**

Peso del coche: $W = mg = 0.050 \times 9.81 = 0.49\,\text{N}$.

$$\frac{F_{down}}{W} = \frac{0.67}{0.49} \approx 1.4$$

> El alerón añade el equivalente a **1.4 veces** el peso del coche pegándolo al piso. Los neumáticos pasan a tener una fuerza normal total de $0.49 + 0.67 = 1.16\,\text{N}$, lo que multiplica su agarre por ≈ 2.4 en curvas.

**Conclusión y discusión.**

> El alerón cuesta drag (≈ 0.56 N que frena al coche), pero compra agarre extra para curvas. Si tu pista tiene muchas curvas cerradas, **el alerón vale la pena** porque permite frenar menos al entrar y acelerar antes a la salida. Si la pista es una recta larga, conviene minimizar el ángulo del alerón para ganar velocidad punta.

> **Verificación de unidades.** $\Delta P\,[\text{Pa}] \cdot A\,[\text{m}^2] = \text{N}$ ✓; $\rho v^2 A$ tiene unidades de $\text{kg}/\text{m}^3 \cdot \text{m}^2/\text{s}^2 \cdot \text{m}^2 = \text{N}$ ✓.

> **Trampa común evitada.** No basta con que el aire pase "rápido" para generar downforce; tiene que pasar **más rápido por la cara inferior que por la superior**. Por eso el alerón se monta INVERTIDO comparado con un ala de avión.
::/practica

---

::practica{titulo="Hidrostática — flotación del coche F1 sobre un foso de agua"}
**Problema.** Tu equipo construye un foso de agua para que el coche F1 flote en lugar de rodar (modo "navegación"). El coche tiene masa $m = 60$ g y un casco de balsa con dimensiones 30 cm × 4 cm × 2 cm (volumen interior 240 cm³). La densidad del agua es $\rho = 1\,000$ kg/m³. Calcula:
1. ¿Flota el coche?
2. ¿Qué altura del casco queda sumergida?
3. Si agregas 100 g extra de instrumentación, ¿sigue flotando?

---

**Paso 1 — Densidad efectiva del coche con casco.**

> Si el casco está hueco y solo tiene el coche dentro, $\rho_\text{efectiva} = m/V = 0.060/2.4\times 10^{-4} = 250$ kg/m³.

> Como $\rho_\text{ef} < \rho_\text{agua}$, **flota** ✓.

**Paso 2 — Altura sumergida.** Para flotación libre, peso = empuje:

$$mg = \rho_a V_\text{sum} g \Rightarrow V_\text{sum} = m/\rho_a = 0.060/1\,000 = 6\times 10^{-5}\,\text{m}^3 = 60\,\text{mL}$$

> Si la base del casco mide $0.30 \times 0.04 = 0.012$ m², la altura sumergida es:
$$h = V_\text{sum}/A_\text{base} = 6\times 10^{-5}/0.012 = 5\times 10^{-3}\,\text{m} = 5\,\text{mm}$$

**Paso 3 — Con 100 g extra.**

> Masa total = 160 g. $V_\text{sum} = 0.160/1\,000 = 1.6\times 10^{-4}\,\text{m}^3 = 160\,\text{mL}$. Altura sumergida $= 1.6\times 10^{-4}/0.012 = 0.0133$ m = 13.3 mm.

> Como el casco solo tiene 20 mm de altura, **aún flota con margen de 6.7 mm**. Si agregas otros 100 g (260 g totales): $h = 0.022$ m > 20 mm → **se hunde**.

**Paso 4 — Margen de carga útil.** Carga máxima antes de hundir:

$$m_\text{máx} = \rho_a V_\text{casco} = 1\,000\times 2.4\times 10^{-4} = 0.24\,\text{kg} = 240\,\text{g}$$

> El casco soporta hasta 240 g totales. Tu coche pesa 60 g, así que la **carga útil máxima es 180 g** (sensores, batería, lastre).
::/practica

---

::practica{titulo="Continuidad y conducto del cartucho de CO₂"}
**Problema.** El cartucho de CO₂ tiene una boquilla con dos secciones: cuerpo principal de área $A_1 = 30$ mm² y boquilla estrecha de área $A_2 = 3$ mm². El gas en el cuerpo viaja a $v_1 = 15$ m/s. Calcula:
1. Velocidad del gas en la boquilla.
2. Diferencia de presión entre cuerpo y boquilla (Bernoulli, $\rho_{\text{CO}_2} \approx 110$ kg/m³ a 60 atm).
3. ¿Por qué se enfría la boquilla? (relaciona con U4).

---

**Paso 1 — Continuidad.**

$$A_1 v_1 = A_2 v_2 \Rightarrow v_2 = (A_1/A_2) v_1 = 10\times 15 = 150\,\text{m/s}$$

**Paso 2 — Bernoulli (a la misma altura).**

$$P_1 + \tfrac{1}{2}\rho v_1^2 = P_2 + \tfrac{1}{2}\rho v_2^2$$
$$P_1 - P_2 = \tfrac{1}{2}\rho(v_2^2 - v_1^2) = 0.5\times 110\times (22\,500 - 225) = 1.225\times 10^6\,\text{Pa} \approx 12.1\,\text{atm}$$

> En la boquilla la presión es **12 atm menos** que en el cuerpo: el gas se acelera porque cae al ambiente de baja presión.

**Paso 3 — Enfriamiento (relación con termodinámica, U4).**

> La rápida expansión del gas al pasar por la boquilla es prácticamente adiabática (no le da tiempo de intercambiar calor con el cartucho). Una expansión adiabática **enfría** el gas: $T_2/T_1 = (P_2/P_1)^{(\gamma-1)/\gamma}$. Para CO₂ con γ=1.30 y caída de 60 a 1 atm, $T_2 \approx T_1\times (1/60)^{0.23} \approx 0.42 T_1$. Si $T_1 = 298$ K, $T_2 \approx 125$ K (–148 °C). Por eso la boquilla se cubre de escarcha al disparar.

**Paso 4 — Implicación de diseño.**

> El enfriamiento extremo afecta la junta de la boquilla (puede contraerse y filtrar). Materiales que mantienen sus propiedades a -100 °C (latón, acero inoxidable) son apropiados; plásticos comunes pueden volverse frágiles.
::/practica
