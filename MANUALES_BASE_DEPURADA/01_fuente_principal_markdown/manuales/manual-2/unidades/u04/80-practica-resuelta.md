---
unidad: 4
seccion: practica-resuelta
paginas_objetivo: 0.5
---

## Práctica resuelta — Análisis térmico del cartucho de CO₂

::practica{titulo="Análisis termodinámico completo del cartucho del coche F1"}
**Problema:**
Tu cartucho de CO₂ del F1 escolar contiene:
- Masa de CO₂: 8 g.
- Presión y Temp inicial: 60 atm, 25 °C (298 K). Tiempo descarga: 0.4 s.
- Después: Presión final 1 atm, Temperatura boquilla -40 °C (233 K).
Calcula: Volumen del CO₂, Trabajo, Cambio de energía y velocidad, Eficiencia de Carnot.

---

**Paso 1 — Volumen inicial (Ley de Gases Ideales)**
- Moles: $n = 8/44 = 0.182\,\text{mol}$. Fórmula: $V_1 = \frac{nRT_1}{P_1}$
- Sustituyendo: $V_1 = \frac{(0.182)(0.0821)(298)}{60} = 0.0741\,\text{L} = 74.1\,\text{mL}$

**Paso 2 — Volumen final**
- $V_2 = \frac{nRT_2}{P_2} = \frac{(0.182)(0.0821)(233)}{1} = 3.48\,\text{L}$
- **Expansión:** Crece 47 veces su tamaño original.

::interioriza{titulo="El globo que roba calor"}
- Imagina un globo comprimido dentro de una jeringa miniatura.
- Al liberarlo, de repente ocupa el tamaño de un melón.
- Ese cambio tan drástico en tan poco tiempo roba calor de todo su entorno.
::/interioriza

**Paso 3 — Trabajo (Aproximación isotérmica)**
- $W = nRT \ln(V_2/V_1) = 1740\,\text{J}$
- *Realidad:* No es puramente isotérmica ni adiabática, hay intercambio de calor.

**Paso 4 y 5 — Energía y Velocidad**
- Velocidad antes (298 K): $v_{rms,1} = 411\,\text{m/s}$
- Velocidad después (233 K): $v_{rms,2} = 363\,\text{m/s}$
- La velocidad cae un 12% y pierde 147 J de energía cinética molecular.

**Paso 6 — Eficiencia de Carnot**
- $\eta_{Carnot} = 1 - 233/298 = 21.8\%$
- El coche real ronda el 13% debido a fricción y escapes inútiles.

::pausa{tipo="deduccion"}
1. Si calentamos el cartucho antes de la carrera, ¿qué variables aumentan? ¿Afecta el empuje?
::/pausa
::/practica

---

::practica{titulo="Calorimetría — Equilibrio entre eje motriz y agua"}
**Problema:** 
- El eje motriz de acero ($m_e = 25$ g, $c_e = 460$ J/(kg·K)) termina a 80 °C.
- Se sumerge en 200 g de agua a 20 °C ($c_a = 4186$ J/(kg·K)).
Calcula: Temperatura final de equilibrio y Calor transferido.

---

**Paso 1 y 2 — Conservación y Temperatura final**
- Calor cedido por el eje = calor absorbido por el agua.
- $0.025(460)(T_f - 80) + 0.200(4186)(T_f - 20) = 0$
- $11.5(T_f - 80) + 837.2(T_f - 20) = 0 \Rightarrow T_f = 20.81\,\text{°C}$

**Paso 3 — Calor transferido**
- $Q = m_a c_a (T_f - T_a) = 0.200(4186)(0.81) = 678\,\text{J}$

::interioriza{titulo="La esponja térmica"}
- Un clavo al rojo vivo en una piscina no calienta el agua casi nada.
- La gran masa de agua domina al pequeño eje.
- Además el agua actúa como "esponja de calor" (alto calor específico).
::/interioriza

::pausa{tipo="deduccion"}
1. Si usamos aceite de motor (menor calor específico), ¿la $T_f$ sería mayor o menor a 20.81 °C?
::/pausa
::/practica

---

::practica{titulo="Dilatación térmica — Pista de aluminio"}
**Problema:**
- Pista de tubos de aluminio ($\alpha = 23\times 10^{-6}/\text{°C}$).
- Longitud $L_0 = 5.000$ m a 22 °C, sube a 55 °C por el sol.
Calcula: Dilatación de 4 tubos y su impacto en tiempo a 18 m/s.

---

**Paso 1 y 2 — Dilatación lineal total**
- $\Delta L_{tubo} = \alpha \cdot L_0 \cdot \Delta T = 23\times 10^{-6} \times 5 \times 33 = 3.80\,\text{mm}$
- Para 4 tubos: $4 \times 3.80\,\text{mm} = 15.2\,\text{mm}$

**Paso 3 — Impacto temporal**
- $\Delta t = 0.0152\,\text{m} / 18\,\text{m/s} = 0.84\,\text{ms}$

::interioriza{titulo="Meñique insignificante"}
- Las vías del tren en verano se tuercen si no tienen separación.
- Nuestra pista "crece" el ancho de un dedo meñique.
- A 18 m/s, eso no afecta casi nada el cronómetro escolar.
::/interioriza

::pausa{tipo="deduccion"}
1. Si la carrera es en invierno (-5 °C), ¿qué le ocurre a la longitud y cómo afecta la medición?
::/pausa
::/practica
