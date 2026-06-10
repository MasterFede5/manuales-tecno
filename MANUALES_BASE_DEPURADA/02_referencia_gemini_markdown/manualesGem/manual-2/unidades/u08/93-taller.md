---
unidad: 8
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Calibración de la cámara on-board del coche F1

Un taller de 60 minutos donde tu equipo F1 Albatros calibra la cámara on-board del coche, mide su campo de visión real, determina la resolución espacial en metros por píxel, y verifica si puede detectar conos a las distancias críticas de pista. Aplica los subtemas 8.1 (refracción), 8.3 (lentes) y 8.4 (sensores CMOS).

::albatros{titulo="Taller — Calibración óptica y resolución de la cámara on-board" tipo="experimento" tiempo="60 min"}
**Pregunta detonadora.** Si pones la cámara on-board del coche F1 en pista, ¿logra distinguir un cono naranja (5 cm) a 5 m? ¿Y a 10 m? ¿Cuál es la distancia máxima útil de detección?

**Lo que harás.** Calibrarás la cámara con un patrón impreso, medirás su campo de visión angular, calcularás la resolución en m/píxel a distintas distancias y verificarás experimentalmente la distancia máxima a la que un cono ocupa al menos 5 píxeles.

**Materiales.**
- Cámara on-board del coche F1 (ESP32-CAM con OV2640 o cualquier celular con cámara fija).
- Una hoja de papel con un patrón de cuadros impresos (ajedrez 5 × 5 cm, 6 × 6 casillas) o regla.
- Cinta métrica (10 m).
- Computadora con software de visualización (navegador para ESP32-CAM o cualquier visor de imágenes).
- Cono naranja de prueba (5 cm de altura, puede ser de cartulina enrollada).
- Cinta adhesiva de color.
- Software de medición de píxeles (GIMP, Paint, o el conteo del navegador).

**Pasos.**

1. **Setup.** Coloquen la cámara fija a una altura de 0.10 m del piso (igual que en el coche). Conéctenla y verifiquen que reciben imagen estable.

2. **Patrón de calibración.** Coloquen el patrón de ajedrez perpendicular al eje óptico de la cámara, a 1.0 m de distancia exacta.

3. **Captura.** Tomen una foto. Anoten la resolución del frame (típicamente $640\times 480$ o $1\,280\times 720$).

4. **Mide el FOV horizontal.** En la foto, midan en píxeles el ancho del patrón (que mide 30 cm en realidad) y multipliquen por la razón. Si el patrón completo ocupa todo el ancho, el FOV horizontal cubre 30 cm a 1.0 m, es decir:
$$\tan(\alpha/2) = (0.30/2)/1.0 = 0.15 \Rightarrow \alpha = 2\arctan(0.15) \approx 17.1°$$
(Si el patrón cubre solo parte del frame, regla de tres con la fracción ocupada.)

5. **Distancia focal efectiva.** Si el sensor mide $W_s$ mm horizontal:
$$f = \frac{W_s/2}{\tan(\alpha/2)}$$
Para OV2640 con sensor de 2.51 mm: $f = 1.255/\tan(8.55°)\approx 8.34$ mm. Verifiquen con datasheet.

6. **Resolución espacial.** A 1.0 m la resolución es $0.30/640 \approx 4.7\times 10^{-4}$ m/píxel = 0.47 mm/píxel. A distancia $d$: $r(d) = 0.30 \cdot d / 640$ (asumiendo FOV escala lineal).

7. **Tabla de resolución vs distancia.**

   | $d$ (m) | Ancho FOV (m) | Resolución (mm/px) | Píxeles por cono (5 cm) |
   |---:|---:|---:|---:|
   | 1 | 0.30 | 0.47 | 106 |
   | 2 | 0.60 | 0.94 | 53 |
   | 3 | 0.90 | 1.41 | 36 |
   | 5 | 1.50 | 2.34 | 21 |
   | 8 | 2.40 | 3.75 | 13 |
   | 10 | 3.00 | 4.69 | 11 |
   | 15 | 4.50 | 7.03 | 7 |
   | 20 | 6.00 | 9.38 | 5 |
   | 30 | 9.00 | 14.1 | 3.5 |

8. **Verificación experimental.** Coloquen el cono real a 1, 5, 10, 15 y 20 m. Capturen foto en cada distancia y midan los píxeles que ocupa el cono.

9. **Comparación.** Construyan tabla con (distancia, píxeles teóricos, píxeles medidos, error %). Discutan por qué el valor real puede ser menor (anti-aliasing, contraste, ruido).

10. **Distancia máxima útil.** Definan "útil" como ≥ 5 píxeles de altura para que un algoritmo de visión por color funcione confiable. Identifiquen la distancia $d_\text{máx}$ donde se cumple.

11. **Ajuste recomendado.** Si $d_\text{máx} < 15$ m, recomienden cambiar a una lente más larga (mayor $f$) o un sensor de mayor resolución. Calculen el nuevo $f$ requerido.

12. **Cierre.** Cada equipo entrega el reporte.

**Entregable.** Bitácora de 1.5 páginas con: foto de calibración, tabla de resolución vs distancia (teórica y experimental), gráfica píxeles por cono vs distancia, $d_\text{máx}$ útil, recomendación de hardware con cálculo.

**Rúbrica de evaluación.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cálculo de FOV y $f$ | sin valores | con valores numéricos | + verificación con datasheet |
| Tabla resolución vs distancia | <3 puntos | 5 puntos | 8 puntos teórica + 5 experimental |
| Comparación teórica/experimental | sin tabla | con tabla | + análisis de error porcentual |
| Recomendación | genérica | con un cambio | con cálculo del nuevo $f$ requerido |
::/albatros
