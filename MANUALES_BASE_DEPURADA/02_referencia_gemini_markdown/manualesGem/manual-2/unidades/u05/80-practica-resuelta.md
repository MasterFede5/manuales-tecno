---
unidad: 5
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Análisis acústico del coche F1

::practica{titulo="Caracteriza el sonido del coche F1 al pasar"}
**Problema.** Tu coche F1 se mueve a 19.8 m/s emitiendo un silbido de 5,000 Hz desde el cartucho. Estás parado a 3 m de la pista. La temperatura del aire es 25 °C (v_sonido = 346 m/s).

Calcula:
1. Frecuencia que percibes cuando el coche se acerca.
2. Frecuencia cuando se aleja.
3. Tiempo entre estos dos extremos (longitud aproximada de la pista frente a ti).
4. Intensidad del sonido a 3 m si la potencia es 10⁻³ W.
5. Nivel en decibeles.

---

**Paso 1 — Doppler acercándose.**

$$f'_1 = f \frac{v}{v - v_f} = 5000 \times \frac{346}{346 - 19.8} = 5000 \times 1.0608 = 5,304\,\text{Hz}$$

**Paso 2 — Doppler alejándose.**

$$f'_2 = f \frac{v}{v + v_f} = 5000 \times \frac{346}{346 + 19.8} = 5000 \times 0.9458 = 4,729\,\text{Hz}$$

**Paso 3 — Cambio total al pasar.**

$$\Delta f = f'_1 - f'_2 = 5304 - 4729 = 575\,\text{Hz}$$

Esto es el "barrido" perceptible: empieza en 5,304 Hz, baja gradualmente conforme el coche pasa, y termina en 4,729 Hz al alejarse.

**Paso 4 — Intensidad a 3 m.**

$$I = \frac{P}{4\pi r^2} = \frac{10^{-3}}{4\pi (3)^2} = 8.84 \times 10^{-6}\,\text{W/m}^2$$

**Paso 5 — Nivel en decibeles.**

$$\beta = 10 \log(I/I_0) = 10 \log(8.84 \times 10^{-6} / 10^{-12}) = 10 \log(8.84 \times 10^6) = 69.5\,\text{dB}$$

**Paso 6 — Interpretación.**

> Estás expuesto a un sonido de **70 dB** a 3 m del coche, con un barrido Doppler de **575 Hz** (de 5,304 a 4,729 Hz) durante el segundo que el coche pasa frente a ti. Es similar al sonido de tráfico moderado: perceptible pero no peligroso.
>
> Si el coche pasara a 1 m (en lugar de 3): área 9× menor, intensidad 9× mayor → **80 dB**, ya elevado pero aún seguro a corto plazo.
>
> Si estuvieras a 30 m: 100× menos intensidad → 50 dB, casi inaudible.

> **Aplicación al diseño:** los amortiguadores de sonido en coches reales reducen la intensidad emitida sin afectar el rendimiento. Para tu F1 escolar, no es preocupación significativa.
::/practica

---

::practica{titulo="Onda estacionaria — diseño del tubo silenciador del coche F1"}
**Problema.** Para "afinar" el silbido del coche F1 a una frecuencia más agradable, instalas un pequeño tubo cerrado por un extremo (atrás del cartucho) que actúa como resonador. Quieres que su frecuencia fundamental coincida con la del cartucho ($f_0 = 5\,000$ Hz) para amplificar selectivamente. La temperatura del aire es 25 °C ($v_s = 346$ m/s). Calcula:
1. Longitud necesaria del tubo cerrado.
2. Si el tubo está abierto en ambos extremos, ¿cuánto cambia la longitud requerida?
3. Frecuencias de los dos primeros sobretonos del tubo cerrado.

---

**Paso 1 — Tubo cerrado por un extremo.**

> En tubo cerrado-abierto, el modo fundamental tiene un nodo en el extremo cerrado y un antinodo en el abierto. La longitud equivale a $\lambda/4$:
$$L = \frac{\lambda}{4} = \frac{v_s}{4 f_0} = \frac{346}{4\times 5\,000} = 0.0173\,\text{m} = 1.73\,\text{cm}$$

**Paso 2 — Tubo abierto en ambos extremos.**

> En tubo abierto-abierto, $L = \lambda/2$:
$$L_\text{ab} = \frac{v_s}{2 f_0} = \frac{346}{10\,000} = 0.0346\,\text{m} = 3.46\,\text{cm}$$

> **Conclusión:** abrir ambos extremos duplica la longitud necesaria.

**Paso 3 — Sobretonos del tubo cerrado.** Solo armónicos impares: $f_n = (2n-1) f_0$.

- 1er sobretono ($n=2$): $f_1 = 3\times 5\,000 = 15\,000$ Hz.
- 2º sobretono ($n=3$): $f_2 = 5\times 5\,000 = 25\,000$ Hz (ya inaudible para humanos).

**Paso 4 — Recomendación de diseño.**

> El tubo cerrado de **1.73 cm** amplifica el silbido fundamental sin agregar mucha longitud al chasis. Como solo amplifica armónicos impares, no genera "armónicos pares parásitos" que enturbiarían el sonido. Es la opción óptima si buscas un sonido limpio y resonante.
::/practica

---

::practica{titulo="Difracción y diseño de barrera acústica para la pista F1"}
**Problema.** Quieres construir una barrera acústica de 0.50 m de altura para reducir el ruido del coche F1 hacia las gradas, situadas a 4 m. El silbido tiene $f = 4\,000$ Hz. Calcula:
1. Longitud de onda del silbido.
2. ¿La barrera difracta significativamente el sonido?
3. ¿Qué frecuencia mínima quedaría "tapada" por la barrera (es decir, no difractaría apreciablemente)?

---

**Paso 1 — Longitud de onda.**

$$\lambda = v_s/f = 343/4\,000 = 0.0858\,\text{m} = 8.58\,\text{cm}$$

**Paso 2 — Compara con la altura de la barrera.**

$$\frac{\lambda}{h} = \frac{0.086}{0.50} = 0.17$$

> Como $\lambda \ll h$, la difracción es **moderada-pequeña**: la barrera **sí** bloquea apreciablemente el sonido directo, pero deja pasar parte por difracción y reflexión en el suelo. Reducción típica: 5–10 dB.

**Paso 3 — Frecuencia umbral.** Diremos que la barrera "tapa" el sonido cuando $\lambda < h/5$, es decir $\lambda < 0.10$ m.

$$f_\text{umbral} > v_s/0.10 = 3\,430\,\text{Hz}$$

**Paso 4 — Conclusión.**

> Frecuencias por encima de **3 430 Hz** quedan razonablemente bloqueadas por la barrera. El silbido a 4 000 Hz se reduce, pero el ruido de baja frecuencia del impacto (graves) **no se atenúa**. Para reducir graves, necesitarías una barrera mucho más alta (≥ 1.5 m). Diseñen la barrera con material absorbente (espuma, fibra) para reducir reflexiones internas.
::/practica
