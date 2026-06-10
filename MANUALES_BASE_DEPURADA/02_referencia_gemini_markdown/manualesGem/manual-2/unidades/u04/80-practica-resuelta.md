---
unidad: 4
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Análisis térmico del cartucho de CO₂

::practica{titulo="Análisis termodinámico completo del cartucho del coche F1"}
**Problema.** Tu cartucho de CO₂ del F1 escolar contiene:
- Masa de CO₂: 8 g.
- Presión inicial: 60 atm.
- Temperatura inicial: 25 °C (298 K).
- Tiempo de descarga: 0.4 s.

Después de descargarse:
- Presión final: 1 atm.
- Temperatura observada en boquilla: -40 °C (233 K).

Calcula:
1. Volumen del CO₂ antes y después.
2. Trabajo realizado por el gas al expandirse.
3. Cambio de energía interna.
4. Velocidad cinética molecular antes y después.
5. Eficiencia de Carnot teórica.

---

**Paso 1 — Volumen inicial usando PV=nRT.**

Moles: $n = 8/44 = 0.182\,\text{mol}$.

$$V_1 = \frac{nRT_1}{P_1} = \frac{(0.182)(0.0821)(298)}{60} = 0.0741\,\text{L} = 74.1\,\text{mL}$$

**Paso 2 — Volumen final.**

$$V_2 = \frac{nRT_2}{P_2} = \frac{(0.182)(0.0821)(233)}{1} = 3.48\,\text{L}$$

**Razón de expansión: 47×.** El gas crece dramáticamente al despresurizarse.

**Paso 3 — Trabajo realizado por el gas (aproximación isotérmica).**

Para una expansión isotérmica:
$$W = nRT \ln(V_2/V_1) = (0.182)(8.314)(298) \ln(47) = 1740\,\text{J}$$

(En realidad la expansión NO es isotérmica — es más compleja. Esta es una aproximación grosera.)

Para una **expansión adiabática** (sin intercambio de calor con el ambiente):
$$T_1 V_1^{\gamma-1} = T_2 V_2^{\gamma-1}$$

con γ = 1.30 para CO₂. Verificación:
$$298 \times (0.074)^{0.30} = 233 \times (3.48)^{0.30}$$

Sustituyendo:
- $298 \times 0.074^{0.30} = 298 \times 0.493 = 147$
- $233 \times 3.48^{0.30} = 233 \times 1.46 = 340$

No coinciden, lo que indica que **el proceso real no es ni isotérmico ni adiabático puro** — es algo intermedio. La diferencia es que el cartucho intercambia algo de calor con su entorno durante los 0.4 s.

**Paso 4 — Velocidad rms del CO₂.**

A 298 K (antes):
$$v_{rms,1} = \sqrt{3RT/M} = \sqrt{3 \times 8.314 \times 298 / 0.044} = 411\,\text{m/s}$$

A 233 K (después):
$$v_{rms,2} = \sqrt{3 \times 8.314 \times 233 / 0.044} = 363\,\text{m/s}$$

**Reducción del 12 %** en velocidad molecular promedio.

**Paso 5 — Cambio de energía cinética molecular.**

$$\Delta E_k = \tfrac{3}{2} n R \Delta T = \tfrac{3}{2}(0.182)(8.314)(233-298) = -147\,\text{J}$$

El gas pierde 147 J de energía cinética molecular durante la expansión.

**Paso 6 — Eficiencia de Carnot teórica.**

$$\eta_{Carnot} = 1 - T_{frío}/T_{caliente} = 1 - 233/298 = 0.218 = 21.8\%$$

**Conclusión:** **incluso un cartucho perfecto** solo podría convertir 21.8 % del trabajo de expansión en trabajo útil. La realidad observada en el coche F1 (~13 %) está limitada por:
1. Pérdidas mecánicas.
2. La mayor parte de la energía la lleva el gas escapado, no el coche.
3. Aproximación adiabática imperfecta.

**Paso 7 — Recomendaciones de diseño térmico.**

| Mejora | Beneficio térmico |
|---|---|
| Cartucho con mayor presión inicial | Mayor expansión, mayor trabajo |
| Cartucho con T inicial más alta (calentar) | Mayor velocidad molecular, mayor empuje |
| Boquilla más estrecha | Mejor conversión de energía cinética molecular en velocidad direccional |
| Aislamiento térmico del cartucho | Reduce pérdida de calor por convección |
| Boquilla con cono divergente | Reduce pérdidas por turbulencia |

Para un coche escolar, el cartucho estándar es la opción óptima por simplicidad. Para misiones espaciales, las boquillas se diseñan con CFD para optimizar cada Joule.

> **Conclusión integradora:** El cartucho de CO₂ es un sistema termodinámico real, sujeto a las leyes de Carnot. Su diseño busca aproximarse al ideal sin nunca alcanzarlo. La teoría termodinámica te permite **predecir** el comportamiento sin necesidad de probar todos los diseños posibles.
::/practica

---

::practica{titulo="Calorimetría — equilibrio entre dos masas de agua y eje del coche"}
**Problema.** Tras la carrera, el eje motriz del coche F1 (acero, $m_e = 25$ g, $c_e = 460$ J/(kg·K)) está a $80\,\text{°C}$ por la fricción de las llantas. Lo sumerges en 200 g de agua a $20\,\text{°C}$ en un recipiente aislado. Calcula:
1. Temperatura final de equilibrio.
2. Calor cedido por el eje y absorbido por el agua.
3. Si el agua estaba a 0 °C como cubo de hielo, ¿cuánto se derretiría con la misma energía?

---

**Paso 1 — Conservación de energía (calorímetro aislado).**

> El calor que cede el eje lo absorbe el agua. Sin pérdidas: $Q_\text{eje} + Q_\text{agua} = 0$, es decir
$$m_e c_e (T_f - T_e) + m_a c_a (T_f - T_a) = 0$$

**Paso 2 — Sustituye datos.**

$m_e = 0.025$ kg, $c_e = 460$, $T_e = 80$ °C; $m_a = 0.200$ kg, $c_a = 4\,186$, $T_a = 20$ °C.

$$0.025\times 460\times (T_f - 80) + 0.200\times 4\,186\times (T_f - 20) = 0$$
$$11.5(T_f - 80) + 837.2(T_f - 20) = 0$$
$$11.5 T_f - 920 + 837.2 T_f - 16\,744 = 0$$
$$848.7 T_f = 17\,664 \Rightarrow T_f = 20.81\,\text{°C}$$

**Paso 3 — Calor transferido.**

$$Q = m_a c_a (T_f - T_a) = 0.200\times 4\,186\times 0.81 = 678\,\text{J}$$

**Paso 4 — Hielo derretido con esa energía.**

> Calor latente de fusión: $L_f = 334\,000$ J/kg.
$$m_\text{hielo} = Q/L_f = 678/334\,000 = 2.03\times 10^{-3}\,\text{kg} \approx 2.0\,\text{g}$$

**Paso 5 — Conclusión.**

> El eje calienta apenas 0.8 °C al agua **porque su masa es 8× menor y su calor específico es 9× menor**. El producto $mc$ del eje es ~1.4 % del producto $mc$ del agua. Para enfriarlo más rápido, se necesitaría más superficie de contacto o un fluido de mayor capacidad térmica.
::/practica

---

::practica{titulo="Dilatación térmica — pista de aluminio del coche F1"}
**Problema.** La pista experimental del coche F1 está hecha de tubos de aluminio ($\alpha = 23\times 10^{-6}/\text{°C}$) de longitud nominal $L_0 = 5.000$ m a 22 °C. La carrera se corre al sol y la temperatura del aluminio sube a 55 °C. Calcula:
1. Cambio de longitud por tubo.
2. Si la pista tiene 4 tubos en serie, ¿cuánto se desplaza la línea de meta?
3. ¿Qué efecto puede tener este desplazamiento en el tiempo de carrera?

---

**Paso 1 — Dilatación lineal.**

$$\Delta L = \alpha \cdot L_0 \cdot \Delta T = 23\times 10^{-6}\times 5.000\times 33 = 3.80\times 10^{-3}\,\text{m} = 3.80\,\text{mm}$$

**Paso 2 — Pista total (4 tubos).**

$$\Delta L_\text{total} = 4\times 3.80 = 15.2\,\text{mm}$$

**Paso 3 — Efecto en el tiempo.** Si el coche llegaba a $v = 18$ m/s, el tiempo extra para recorrer 15.2 mm es:

$$\Delta t = 0.0152/18 = 8.4\times 10^{-4}\,\text{s} \approx 0.84\,\text{ms}$$

**Paso 4 — Comparación con margen de victoria.**

> En F1 escolar, márgenes de victoria típicos son **10–30 ms**. La dilatación, aunque pequeña (1 ms), **no decide la carrera por sí sola**, pero sí podría inclinar la balanza si dos coches están empatados. La buena noticia: como ambos coches corren la misma distancia caliente, el efecto se cancela.

**Paso 5 — Recomendación.**

> Para mediciones científicas, calibrar la longitud de la pista a la temperatura ambiente del momento. Para una pista de 20 m al sol que va de 22 °C a 55 °C, el error en la distancia nominal es 15 mm, lo cual implica 0.075 % de error. Aceptable para la liga escolar; importante para récords oficiales.
::/practica
