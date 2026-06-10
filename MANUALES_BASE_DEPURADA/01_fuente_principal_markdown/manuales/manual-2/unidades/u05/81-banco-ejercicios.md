---
unidad: 5
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Ondas

Resuelve cada problema mostrando datos, fórmula, sustitución y resultado con unidades. Conecta con la acústica del coche F1 cuando aplique.

---

### Bloque A · Caracterización y parámetros (5.1, 5.2)

::act-calc{titulo="A1. Relación $v = \\lambda f$" renglones=10}
1. Una onda sonora tiene $f = 440$ Hz (la nota La) y $v = 343$ m/s. ¿Cuánto vale $\lambda$?
2. Una onda en una cuerda de guitarra tiene $\lambda = 1.20$ m y se propaga a 400 m/s. ¿Cuál es su frecuencia?
3. La onda de Wi-Fi a 5 GHz se propaga a $c = 3\times 10^8$ m/s. Calcula $\lambda$.
4. Un silbido del coche F1 tiene $\lambda = 6.86$ cm en aire a 20 °C ($v_s = 343$ m/s). Calcula la frecuencia.
::/act-calc

::act-fill{titulo="A2. Vocabulario de ondas"}
1. Una onda __________________ tiene la oscilación perpendicular a la dirección de propagación.
2. La __________________ de una onda es la distancia entre dos crestas consecutivas.
3. El __________________ es el inverso de la frecuencia y se mide en segundos.
4. La __________________ es la altura máxima de la oscilación; relacionada con la energía.
5. Las ondas __________________ no requieren medio material para propagarse.
::/act-fill

---

### Bloque B · Reflexión, refracción, Snell (5.3)

::act-calc{titulo="B1. Ley de Snell" renglones=10}
5. Una luz pasa de aire ($n=1$) al agua ($n=1.33$) con ángulo de incidencia $\theta_i = 35°$. Calcula el ángulo refractado.
6. Una luz pasa del vidrio ($n = 1.50$) al aire con $\theta_i = 30°$. Calcula $\theta_r$.
7. Calcula el ángulo crítico para reflexión total interna del agua al aire.
8. Una onda sonora se refleja en una pared a 12 m. ¿En cuánto tiempo recibes el eco si $v_s = 340$ m/s?
::/act-calc

---

### Bloque C · Difracción, interferencia (5.4)

::act-calc{titulo="C1. Doble rendija de Young" renglones=10}
9. En un experimento de Young, $d = 0.20$ mm, $L = 2.0$ m y $\lambda = 600$ nm. Calcula la separación entre franjas brillantes consecutivas.
10. Si pasas a $\lambda = 450$ nm con la misma geometría, ¿se separan o se acercan las franjas?
11. Tu coche F1 emite un silbido a 5 kHz que pasa por un hueco de 30 cm. ¿Es mayor o menor que $\lambda$? ¿Habrá difracción importante?
::/act-calc

::act-tf{titulo="C2. Verdadero o falso"}
1. La interferencia constructiva produce máximos en el patrón. ( ) ____________________________________________
2. La difracción es despreciable cuando la abertura es mucho mayor que $\lambda$. ( ) ____________________________________________
3. Las ondas que interfieren deben tener la misma frecuencia para ver patrones estables. ( ) ____________________________________________
::/act-tf

---

### Bloque D · Energía e intensidad (5.5)

::act-calc{titulo="D1. Intensidad y decibelios" renglones=10}
12. Una bocina entrega 0.05 W de potencia acústica. ¿Cuál es la intensidad a 2 m? Asume fuente puntual e isotrópica.
13. Si esa intensidad es $I$, ¿qué nivel en dB tiene? ($I_0 = 10^{-12}$ W/m²).
14. A 1 m de tu coche F1 mides 78 dB. ¿Qué nivel medirás a 4 m, asumiendo decaimiento $1/r^2$?
15. ¿Cuántas veces más intenso es un sonido de 90 dB que uno de 60 dB?
::/act-calc

---

### Bloque E · Sonido, ondas estacionarias y Doppler (5.6)

::act-calc{titulo="E1. Cuerdas, tubos y Doppler" renglones=12}
16. Una cuerda de guitarra de 0.65 m fija en ambos extremos vibra en su modo fundamental. La velocidad de la onda es 360 m/s. ¿Cuál es la frecuencia?
17. Un tubo cerrado por un extremo tiene 0.5 m. Calcula la frecuencia fundamental con $v_s = 343$ m/s.
18. Una sirena de 1 200 Hz se acerca a ti a 25 m/s. ¿Qué frecuencia escuchas?
19. La misma sirena se aleja a 25 m/s. ¿Qué frecuencia escuchas?
20. Tu coche F1 emite 5 kHz mientras se acerca a 18 m/s. ¿Qué frecuencia escucha un espectador parado en la pista?
::/act-calc

---

### Bloque F · Mixto / case F1

::act-order{titulo="F1. Ordena los pasos para diagnosticar la firma acústica del coche F1"}
[ ] Identificar pico fundamental y armónicos en el espectro.
[ ] Comparar espectros antes y después del paso (efecto Doppler).
[ ] Grabar audio del disparo del cartucho con micrófono cercano.
[ ] Aplicar FFT (Plot Spectrum en Audacity) al fragmento de 1 s.
[ ] Recortar el fragmento de 1 s correspondiente al cartucho activo.
::/act-order

::act-match{titulo="F2. Tipo de onda y ejemplo cotidiano"}
| Tipo | Ejemplo |
|---|---|
| 1. Mecánica longitudinal | a) Luz solar |
| 2. Mecánica transversal | b) Sonido en aire |
| 3. Electromagnética | c) Wave en cuerda |
| 4. Estacionaria | d) Cuerda de guitarra fija |
::/act-match

---

## Clave de respuestas

| # | Resultado |
|---:|---|
| 1 | $\lambda = 343/440 = 0.78$ m |
| 2 | $f = 400/1.20 = 333.3$ Hz |
| 3 | $\lambda = 0.06$ m = 6 cm |
| 4 | $f = 343/0.0686 = 5\,000$ Hz |
| 5 | $\theta_r = \arcsin(\sin 35°/1.33)\approx 25.5°$ |
| 6 | $\theta_r \approx 48.6°$ |
| 7 | $\theta_c = \arcsin(1/1.33) \approx 48.8°$ |
| 8 | $t = 2\times 12/340 = 0.0706$ s |
| 9 | $\Delta y = \lambda L / d = 6\,\text{mm}$ |
| 10 | Se acercan ($\Delta y \propto \lambda$, baja a 4.5 mm) |
| 11 | $\lambda = 343/5\,000 \approx 6.9$ cm; abertura mucho mayor → difracción débil |
| 12 | $I = P/(4\pi r^2) = 0.05/(4\pi 4) = 9.95\times 10^{-4}$ W/m² |
| 13 | $\beta = 10\log(I/I_0)\approx 90$ dB |
| 14 | $\beta = 78 - 20\log(4) \approx 65.96$ dB |
| 15 | $10^3$ = 1 000 veces |
| 16 | $f = v/(2L) = 360/1.30 = 277$ Hz |
| 17 | $f = v/(4L) = 343/2 = 171.5$ Hz |
| 18 | $f' = 1\,200\times 343/(343-25) = 1\,294$ Hz |
| 19 | $f' = 1\,200\times 343/(343+25) = 1\,118$ Hz |
| 20 | $f' = 5\,000\times 343/(343-18) = 5\,277$ Hz |
| F1 | 3 → 5 → 4 → 1 → 2 |
| F2 | 1-b · 2-c · 3-a · 4-d |
| A2 | transversal · longitud de onda · período · amplitud · electromagnéticas |
| C2 | 1) V · 2) V · 3) V |
