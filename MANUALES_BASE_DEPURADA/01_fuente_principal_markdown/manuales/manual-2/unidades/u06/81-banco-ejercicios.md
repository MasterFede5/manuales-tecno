---
unidad: 6
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Electromagnetismo

Resuelve cada problema con datos, fórmula, sustitución y resultado con unidades. Conecta con el sistema eléctrico del coche F1 cuando aplique.

---

### Bloque A · Electrostática (6.1)

::act-calc{titulo="A1. Coulomb, campo y potencial" renglones=12}
1. Dos cargas de 2 µC y -3 µC están separadas 0.10 m. Calcula la fuerza entre ellas. ¿Es atractiva o repulsiva?
2. Calcula el campo eléctrico a 5 cm de una carga puntual de 1 µC.
3. Una carga puntual de 4 µC genera un potencial $V$ a 0.20 m. Calcula $V$.
4. ¿Qué trabajo realizas para mover una carga de 0.5 µC desde un punto a 100 V hasta otro a 350 V?
::/act-calc

::act-fill{titulo="A2. Vocabulario eléctrico"}
1. La __________________ eléctrica se mide en coulombs (C).
2. El __________________ eléctrico es fuerza por unidad de carga (N/C o V/m).
3. La __________________ es energía por unidad de carga (J/C = V).
4. La constante de Coulomb es $k \approx 9\times 10^9$ N·m²/C² y está relacionada con la __________________ del vacío $\varepsilon_0$.
::/act-fill

---

### Bloque B · Ohm, circuitos serie y paralelo (6.2)

::act-calc{titulo="B1. Ley de Ohm y potencia" renglones=12}
5. Una resistencia de 220 Ω conectada a 12 V. ¿Qué corriente pasa? ¿Qué potencia disipa?
6. Tres resistencias en serie: 100 Ω, 150 Ω, 250 Ω, conectadas a 9 V. Calcula corriente y voltaje en la de 150 Ω.
7. Las mismas tres resistencias ahora en paralelo, mismo voltaje. Calcula resistencia equivalente y corriente total.
8. Tu coche F1 tiene un microcontrolador que consume 100 mA a 3.3 V. ¿Qué potencia consume?
9. Una batería de 9 V·1 200 mAh alimenta el coche. ¿Cuántas horas dura suministrando 200 mA?
::/act-calc

::act-tf{titulo="B2. Verdadero o falso"}
1. En un circuito en serie, la corriente es la misma en todos los componentes. ( ) ____________________________________________
2. En un circuito en paralelo, el voltaje en cada rama es distinto. ( ) ____________________________________________
3. Duplicar el voltaje a una resistencia fija duplica la corriente y cuadruplica la potencia. ( ) ____________________________________________
::/act-tf

---

### Bloque C · Kirchhoff (6.2 avanzado)

::act-calc{titulo="C1. Análisis de mallas" renglones=12}
10. Dos pilas en serie de 9 V y 3 V (sumando) alimentan una resistencia de 60 Ω y otra de 40 Ω en serie. Calcula la corriente.
11. Si las pilas están en oposición (9 V y 3 V con polaridad inversa), ¿qué corriente pasa por la misma red de resistencias?
12. En un nodo entran 0.5 A y 0.3 A; sale una rama de 0.4 A. ¿Cuánto vale la cuarta rama?
::/act-calc

---

### Bloque D · Magnetismo (6.3)

::act-calc{titulo="D1. Fuerzas magnéticas" renglones=10}
13. Un protón ($q = 1.6\times 10^{-19}$ C) entra perpendicular a un campo $B = 0.2$ T a $v = 10^6$ m/s. Calcula la fuerza.
14. Un alambre recto de 0.30 m lleva 5 A perpendicular a un campo de 0.10 T. ¿Qué fuerza siente?
15. Si el alambre se inclina 30° respecto a $B$, ¿cómo cambia la fuerza?
::/act-calc

---

### Bloque E · Inducción (6.4)

::act-calc{titulo="E1. Faraday y Henry" renglones=10}
16. Una bobina de 100 espiras tiene un flujo que cambia de 0.4 Wb a 0.1 Wb en 0.05 s. Calcula la fem inducida.
17. La autoinductancia de un solenoide es 50 mH. Si la corriente cambia a 4 A/s, ¿qué fem aparece?
18. Calcula la inductancia mutua entre dos bobinas si una fem de 1.2 V aparece en la secundaria cuando la primaria cambia su corriente a 6 A/s.
::/act-calc

---

### Bloque F · Ondas EM y luz (6.5, 6.6)

::act-calc{titulo="F1. Espectro electromagnético" renglones=10}
19. Un Wi-Fi a 5 GHz se propaga en aire a $c$. Calcula $\lambda$.
20. La luz roja tiene $\lambda = 700$ nm. Calcula su frecuencia.
21. Calcula la energía de un fotón de luz roja de 700 nm en J y en eV ($h = 6.626\times 10^{-34}$ J·s, $1$ eV $= 1.602\times 10^{-19}$ J).
22. Tu coche F1 transmite por Wi-Fi a 2.4 GHz con potencia 100 mW. ¿Cuántos fotones por segundo emite?
::/act-calc

::act-match{titulo="F2. Bandas del espectro EM"}
| Banda | Aplicación |
|---|---|
| 1. Radio AM | a) Visión humana |
| 2. Microondas | b) Comunicación local con la base del coche F1 |
| 3. Visible | c) Comunicación a larga distancia |
| 4. UV | d) Esterilización |
| 5. Rayos X | e) Imágenes médicas |
::/act-match

---

### Bloque G · Mixto / case F1

::act-order{titulo="G1. Ordena los pasos para diseñar el circuito de control del coche F1"}
[ ] Calcular potencia y autonomía con la batería elegida.
[ ] Identificar los componentes y su voltaje/corriente nominales.
[ ] Aplicar Ley de Ohm para dimensionar las resistencias en serie con LEDs.
[ ] Sumar consumos para hallar la corriente total que debe entregar la batería.
[ ] Validar con un multímetro las corrientes reales por rama.
::/act-order

---

## Clave de respuestas

| # | Resultado |
|---:|---|
| 1 | $F = 9\times 10^9 \times 6\times 10^{-12}/0.01 = 5.4$ N atractiva |
| 2 | $E = 9\times 10^9 \times 10^{-6}/0.0025 = 3.6\times 10^6$ N/C |
| 3 | $V = kQ/r = 9\times 10^9\times 4\times 10^{-6}/0.20 = 1.8\times 10^5$ V |
| 4 | $W = q\Delta V = 0.5\times 10^{-6}\times 250 = 1.25\times 10^{-4}$ J |
| 5 | $I = 12/220 = 54.5$ mA; $P=0.65$ W |
| 6 | $I = 9/500 = 18$ mA; $V_{150} = 2.7$ V |
| 7 | $1/R = 1/100+1/150+1/250 = 0.0227 \Rightarrow R \approx 44.0$ Ω; $I=205$ mA |
| 8 | $P = 0.33$ W |
| 9 | $t = 1\,200/200 = 6$ h |
| 10 | $V = 12$ V; $I = 12/100 = 0.12$ A |
| 11 | $V = 6$ V; $I = 0.06$ A |
| 12 | $I_4 = 0.5+0.3-0.4 = 0.4$ A saliente |
| 13 | $F = qvB = 1.6\times 10^{-19}\times 10^6\times 0.2 = 3.2\times 10^{-14}$ N |
| 14 | $F = ILB = 5\times 0.30\times 0.10 = 0.15$ N |
| 15 | $F = ILB\sin\theta$, con $\sin 30°=0.5$ → 0.075 N (la mitad) |
| 16 | $\varepsilon = -N \Delta\Phi/\Delta t = -100(-0.3)/0.05 = 600$ V |
| 17 | $\varepsilon = L\,dI/dt = 0.05\times 4 = 0.2$ V |
| 18 | $M = \varepsilon/(dI/dt) = 1.2/6 = 0.2$ H |
| 19 | $\lambda = 0.06$ m = 6 cm |
| 20 | $f = c/\lambda = 3\times 10^8/7\times 10^{-7} = 4.29\times 10^{14}$ Hz |
| 21 | $E = hf \approx 2.84\times 10^{-19}$ J $\approx 1.77$ eV |
| 22 | Energía por fotón $\approx 1.59\times 10^{-24}$ J; $N \approx 0.1/1.59\times 10^{-24} \approx 6.3\times 10^{22}$ fot/s |
| F2 | 1-c · 2-b · 3-a · 4-d · 5-e |
| G1 | 2 → 4 → 3 → 1 → 5 |
| A2 | carga · campo · diferencia de potencial · permitividad |
| B2 | 1) V · 2) F (mismo voltaje) · 3) V |
