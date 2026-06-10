---
unidad: 8
seccion: practica-resuelta
paginas_objetivo: 1
---

## Práctica resuelta — Diseño óptico de la cámara on-board

::practica{titulo="Calcula el campo de visión y la resolución por píxel de la cámara del coche F1"}
**Problema.** Tu cámara on-board tiene los siguientes datos:

- Lente convergente delgada con $f = 4.0\,\text{mm}$ y apertura efectiva $D = 1.5\,\text{mm}$.
- Sensor CMOS rectangular de $4.8\,\text{mm} \times 3.6\,\text{mm}$, con resolución de $640 \times 480$ píxeles (cada píxel cuadrado).
- La cámara está a $h = 0.8\,\text{m}$ sobre el piso de la pista.
- Las marcas de pista (conos) miden $5\,\text{cm}$ de alto.

Calcula:

1. La distancia focal en dioptrías y verifica que es lente convergente.
2. La distancia $q$ a la que se forma la imagen de un cono que está a $5\,\text{m}$ de la cámara.
3. El tamaño de la imagen del cono sobre el sensor.
4. La cantidad de píxeles de altura que cubre ese cono.
5. El campo de visión angular horizontal de la cámara.
6. ¿Sería suficiente la resolución para que un algoritmo detecte el cono confiablemente?

---

**Paso 1 — Potencia óptica.**

$$\text{P} = 1/f = 1/0.004\,\text{m} = 250\,\text{D}$$

Como P > 0, la lente es convergente. ✓

**Paso 2 — Distancia imagen.**

Aplicando la ecuación de la lente delgada con $p = 5\,\text{m}$ y $f = 4 \times 10^{-3}\,\text{m}$:

$$\frac{1}{q} = \frac{1}{f} - \frac{1}{p} = \frac{1}{0.004} - \frac{1}{5} = 250 - 0.2 = 249.8\,\text{m}^{-1}$$

$$q = 1/249.8 = 4.003\,\text{mm} \approx 4.0\,\text{mm}$$

> Como $p \gg f$, la imagen se forma prácticamente en el plano focal. Por eso un sensor montado a 4 mm de la lente capta nítidamente objetos lejanos.

**Paso 3 — Tamaño de la imagen del cono.**

Aumento $M = -q/p = -0.004/5 = -8 \times 10^{-4}$.

Tamaño del cono en el sensor:
$$|y'| = |M| \cdot y = 8 \times 10^{-4} \times 0.05\,\text{m} = 4 \times 10^{-5}\,\text{m} = 0.04\,\text{mm}$$

**Paso 4 — Píxeles cubiertos.**

Tamaño de cada píxel del sensor:
$$\text{px} = 3.6\,\text{mm}/480 = 7.5\,\mu\text{m}$$

Número de píxeles que cubre el cono:
$$N = 0.04\,\text{mm} / 0.0075\,\text{mm/px} \approx 5.3\,\text{px}$$

> El cono se ve como una mancha de ≈ 5 píxeles de alto. Para un algoritmo de detección por color simple es suficiente, pero apenas: si quisieras leer algún número impreso en el cono, no podrías.

**Paso 5 — Campo de visión horizontal.**

El sensor mide 4.8 mm de ancho y la lente tiene $f = 4$ mm. El semiángulo es:
$$\tan(\alpha/2) = (4.8/2)/4 = 0.6 \Rightarrow \alpha/2 = 31° \Rightarrow \alpha = 62°$$

> La cámara cubre un cono horizontal de **62°**. Es un ángulo amplio, similar al del ojo humano sin moverlo (60°-70°).

**Paso 6 — Discusión.**

> Con 5 píxeles por cono a 5 m, el algoritmo puede detectar conos por color (saturación + tono) pero **no** distinguir uno de otro a esa distancia. Si quisieras leer la pista a 10 m, los conos solo cubrirían ≈ 2.5 píxeles — insuficiente. Soluciones: cámara con más resolución (1920×1080 = factor 3 mejor), lente con $f$ más larga (teleobjetivo, pero pierdes campo de visión), o IA con super-resolución.

> **Verificación de unidades.** $|y'| = |M| \cdot y$, con $M$ adimensional, $y$ en m → $y'$ en m ✓.
::/practica

---

::practica{titulo="Faros del coche F1 — diseño con espejo cóncavo"}
**Problema.** Quieres instalar un mini-faro en el coche F1 para iluminación nocturna. Usas un espejo cóncavo de radio de curvatura $R = 4$ cm con una bombilla LED puntual ubicada en el foco. Calcula:
1. Distancia focal del espejo.
2. Tipo de haz emitido.
3. Si la bombilla se mueve a 1 cm del espejo, ¿qué imagen forma?
4. Con el LED en el foco y el espejo apuntando hacia adelante, ¿qué área ilumina a 5 m de distancia si el espejo tiene 3 cm de diámetro?

---

**Paso 1 — Distancia focal.**

$$f = R/2 = 4/2 = 2\,\text{cm}$$

**Paso 2 — Haz al colocar la fuente en el foco.**

> Si $p = f$, la imagen está en el infinito ($1/q = 1/f - 1/p = 0$ → $q\to\infty$). Es decir, **el espejo refleja un haz paralelo**: ideal para faro de largo alcance.

**Paso 3 — Bombilla a 1 cm del espejo ($p = 1 < f$).**

$$1/q = 1/f - 1/p = 1/2 - 1/1 = -0.5 \Rightarrow q = -2\,\text{cm}$$

> Imagen virtual a 2 cm detrás del espejo, derecha y aumentada ($M = -q/p = 2$). Esto produce un haz **divergente**, no útil para faro.

**Paso 4 — Área iluminada a 5 m.**

> Como el haz es paralelo (con LED en foco), conserva el diámetro del espejo: $\approx 3$ cm. En la práctica, las pequeñas imperfecciones difunden el haz un poco; estimemos un cono con divergencia 1°. Diámetro a 5 m:
$$D \approx 3\,\text{cm} + 5\,\text{m} \times \tan 1° = 3 + 5\,000\times 0.01745 = 3 + 87.3 \approx 90\,\text{cm}$$

> Una mancha luminosa de **~90 cm de diámetro a 5 m**: pista bien iluminada al frente.

**Paso 5 — Recomendación.**

> Para un faro estable, fijar el LED **exactamente** en el foco. Una desviación de 1 mm cambia el haz a divergente (mancha mucho más grande a distancia, menor brillo por área).
::/practica

---

::practica{titulo="Sensor de línea por reflexión — IR del coche F1"}
**Problema.** El sensor de línea TCRT5000 del coche F1 emite luz IR a 950 nm desde un LED y recibe el reflejo en un fototransistor. Está montado a 8 mm del piso. Su lente del receptor tiene $f = 5$ mm. Calcula:
1. Energía por fotón IR.
2. ¿A qué distancia del fototransistor se forma la imagen del piso? (objeto a 8 mm del lente)
3. Si el piso es negro vs blanco y el sensor recibe 0.1 µW vs 5 µW, ¿cuál es el contraste relativo?
4. Si quieres detectar una línea de 8 mm de ancho, ¿qué tamaño tiene su imagen sobre el fototransistor?

---

**Paso 1 — Energía por fotón.**

$$E = hc/\lambda = \frac{6.626\times 10^{-34}\times 3\times 10^8}{950\times 10^{-9}} = 2.09\times 10^{-19}\,\text{J} = 1.31\,\text{eV}$$

**Paso 2 — Imagen del piso.**

$$1/q = 1/f - 1/p = 1/0.005 - 1/0.008 = 200 - 125 = 75\,\text{m}^{-1}$$
$$q = 1/75 = 0.0133\,\text{m} = 13.3\,\text{mm}$$

> El receptor debe estar a 13.3 mm de la lente.

**Paso 3 — Contraste.**

$$\text{contraste} = (5 - 0.1)/(5 + 0.1)\times 100\% = 96.1\%$$

> Excelente para detección por umbral.

**Paso 4 — Tamaño de imagen de línea.**

$$M = -q/p = -13.3/8 = -1.66$$
$$|y'| = 1.66\times 8 = 13.3\,\text{mm}$$

> La línea se proyecta a 13.3 mm sobre el receptor. Si el detector mide 5 mm, **toda la línea no cabe** sino que detecta solo una parte. Eso está bien: lo importante es que **alguna parte** de la línea ilumine el detector y la señal sea distinta del piso oscuro.

**Paso 5 — Recomendación.**

> Mantener el sensor a 8 mm del piso para buena resolución. Si lo subes a 15 mm, $q$ baja a $\approx 7.5$ mm (lente más cerca), $M$ baja a 0.5, y la imagen de la línea se vuelve más pequeña. La luz por unidad de área aumenta, pero el área cubierta por la línea disminuye: la señal puede saturar o perderse según el detector. La altura óptima depende del tamaño del fototransistor.
::/practica
