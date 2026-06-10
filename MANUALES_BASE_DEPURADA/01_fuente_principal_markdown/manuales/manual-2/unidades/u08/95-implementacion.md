---
unidad: 8
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Telescopio refractor casero + cámara on-board"}
**Objetivo.** Construir dos sistemas ópticos a escala distinta: 1) un telescopio refractor casero usando dos lentes de "Dollar Store" para observar la Luna y planetas; 2) una mini-cámara on-board para tu coche F1 con un sensor OV2640 + módulo ESP32-CAM. Ambos proyectos te entrenan en alineación óptica, distancia focal y manejo del plano imagen.

**¿Por qué hacerla?** El primer telescopio (Galileo, 1609) era exactamente esto: dos lentes en un tubo. Construirlo te conecta con 400 años de ciencia y te da intuición real de focos y aumentos. La cámara on-board te lleva al otro extremo: óptica electrónica moderna lista para integrarse al coche del case study.

---

### Materiales

**Telescopio refractor:**
- Lente convergente grande de $f \approx 50$ cm (lupa de papelería o lente de proyector viejo).
- Lente convergente pequeña de $f \approx 5$ cm (lupa de joyero o lente del ojo de un teléfono desarmado).
- Tubo de cartón de 30-50 cm (rollo de papel de aluminio o de toallas).
- Cinta adhesiva, pegamento, tijeras.
- Tripié o soporte (puede ser una cámara fotográfica vieja).

**Cámara on-board:**
- Módulo ESP32-CAM con cámara OV2640 (≈ 150 MXN).
- Cable FTDI USB-Serial para programarlo.
- Soporte impreso en 3D o cartón rígido.
- Batería 3.7 V LiPo + módulo de carga.

### Pasos — Telescopio

1. **Calcula el aumento esperado.** $M = f_{obj}/f_{ocular} = 50/5 = 10\times$.
2. **Mide las distancias focales reales** de tus dos lentes con la prueba del Sol (enfocas el sol en un papel y mides la distancia lente-papel).
3. **Corta el tubo** de longitud $L = f_{obj} + f_{ocular} = 55$ cm.
4. **Pega la lente grande** en uno de los extremos del tubo (objetivo).
5. **Inserta la lente pequeña** en el otro extremo, con un pequeño tubo deslizable para enfocar (ocular).
6. **Apunta a la Luna** una noche despejada. Ajusta el ocular hasta que veas nítido. Verás los cráteres principales.
7. **Documenta:** toma una foto a través del ocular con tu celular y compara con la Luna a simple vista.

### Pasos — Cámara on-board

1. **Conecta el ESP32-CAM** al FTDI según el diagrama oficial (RX-TX cruzado, GPIO0-GND para programación).
2. **Carga el ejemplo** "CameraWebServer" desde el IDE de Arduino. Configura SSID y contraseña de tu wifi.
3. **Abre el navegador** en la IP que aparece en el monitor serie. Verás el video en vivo.
4. **Mide el campo de visión** apuntando a una regla a 1 m: cuántos cm cubre el ancho del frame.
5. **Calcula el $f$ de la lente** del OV2640 a partir de tus mediciones (FOV horizontal típico es 65°).
6. **Monta la cámara** en tu coche F1. Filma una vuelta de pista.
7. **Analiza la grabación**: ¿se ven los conos? ¿La aceleración del coche se nota? ¿Hay vibración?

::visual{tipo="ilustracion" descripcion="Dos viñetas: 1) TELESCOPIO REFRACTOR casero — tubo de cartón con lente grande de objetivo en un extremo y lente pequeña ocular en el otro, soporte de tripié, ojo del observador en el ocular y la Luna como objeto distante. Anotaciones: f_objetivo=50 cm, f_ocular=5 cm, M=10×. 2) ESP32-CAM montado sobre coche F1 escolar con batería LiPo y antena wifi visible; flecha de transmisión inalámbrica hacia un laptop con la transmisión en pantalla. Pista con conos de fondo." paginas=0.5}

---

### Entregable

Reporte de 3 páginas con:
1. **Telescopio:** cálculo del aumento esperado vs el observado en la Luna, foto a través del ocular, lista de los 3 cráteres principales que viste.
2. **Cámara:** captura de pantalla del feed en vivo del ESP32-CAM, video grabado de 30 s del coche F1 en pista, cálculo del FOV y comparativa con la práctica resuelta de esta unidad.
3. **Reflexión:** ¿qué problema óptico te dio más trabajo (alineación, enfoque, vibración) y cómo lo resolviste? ¿Qué aplicarías al diseño de un sistema profesional?

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Telescopio funcional** | no se ve nada | se ve la Luna borrosa | se ven cráteres reconocibles |
| **Cálculo del aumento** | sin calcular | calcula $M$ teórico | mide $M$ real y compara |
| **Cámara funcional** | no transmite | transmite imagen estática | video fluido en tiempo real |
| **FOV calculado** | sin medir | mide pero sin compararlo con teoría | mide y aplica $\tan(\alpha/2) = (\text{ancho}/2)/d$ |
| **Reflexión técnica** | sin discutir | menciona dificultades | propone mejoras concretas |

---

### Hitos intermedios

| Sprint | Semana | Meta concreta | Evidencia |
|---|---|---|---|
| 1. Telescopio | 1 | Tubo armado y enfocando objetos a 50 m | foto a través del ocular |
| 2. ESP32-CAM | 2 | Cámara transmitiendo imagen estable a navegador | URL + captura |
| 3. FOV y resolución | 3 | FOV medido + tabla resolución vs distancia | reporte parcial 2 pp |
| 4. Cámara montada | 4 | Cámara fija al coche con video de vuelta de pista | video 30 s |

### Reto bonus extendido (+2 puntos cada uno)

1. **Detección por color en tiempo real.** Programa el ESP32-CAM (o un Raspberry Pi recibiendo el stream) para que detecte conos naranjas usando OpenCV: convierte a HSV, filtra rango de naranja, dibuja bounding boxes. Mide cuántos FPS logras.
2. **Doble cámara estereoscópica.** Monta dos ESP32-CAM separadas 10 cm y captura sincronizadamente. Calcula la disparidad para deducir la distancia de un cono. Verifica con cinta métrica.
3. **Calibración con tablero de ajedrez.** Usa OpenCV `cv2.calibrateCamera` para deducir la matriz intrínseca y los coeficientes de distorsión de la lente. Aplica la corrección y compara antes/después.
::/implementacion

---

::albatros{titulo="Caso integrador — semáforo de salida del F1 con sensor de luz" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Diseña un sistema que detecte el momento en que se enciende la luz verde de salida y mande la señal de disparo al cartucho del coche. ¿Qué fototransistor o LDR usarías y a qué umbral lo configurarías?

**Lo que harás.**
1. Caracteriza tres sensores de luz (fototransistor, LDR, fotodiodo) en términos de tiempo de respuesta, sensibilidad espectral y costo.
2. Calcula el flujo luminoso (en lux) que llega al sensor cuando una bombilla de 2 W (eficiencia ~90 lm/W) se enciende a 0.5 m de distancia. Usa $E = \Phi/(4\pi r^2)$ con $\Phi = 180$ lm.
3. Determina el umbral de disparo: por ejemplo, > 80 % del valor estable en 50 ms.
4. Calcula el retraso total: detección + procesamiento + activación del actuador. Apunta a < 100 ms.
5. Recomienda el sensor con justificación (precio + velocidad + sensibilidad espectral coincidente con LED verde, ~520 nm).

**Entregable.** Hoja con: tabla comparativa de los 3 sensores, cálculo del flujo en lux, definición de umbral y diagrama del circuito de disparo.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Tabla comparativa | <3 columnas | 3 sensores con 3 atributos | + valores numéricos |
| Cálculo del flujo | sin valor | con valor en lux | + cifras significativas |
| Recomendación | genérica | con justificación | con justificación + diagrama de circuito |
::/albatros
