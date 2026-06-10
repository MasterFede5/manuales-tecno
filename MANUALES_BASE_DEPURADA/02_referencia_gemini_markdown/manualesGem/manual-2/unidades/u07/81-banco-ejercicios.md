---
unidad: 7
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Fluidos

Resuelve cada problema mostrando datos, fórmula, sustitución y resultado con unidades. Vincúlalos al case del coche F1 cuando sea natural.

---

### Bloque A · Hidrostática (7.1)

::act-calc{titulo="A1. Presión hidrostática y Pascal" renglones=12}
1. Calcula la presión total a 12 m de profundidad en agua dulce ($\rho = 1\,000$ kg/m³). Suma la atmosférica (101 325 Pa).
2. Una prensa hidráulica tiene pistón pequeño $A_1 = 4$ cm² y grande $A_2 = 200$ cm². Si aplicas 60 N en el pequeño, ¿qué fuerza obtienes en el grande?
3. Un tanque cilíndrico de 1.0 m² de base contiene agua a 0.5 m de altura. ¿Qué presión ejerce sobre el fondo?
4. Para soportar el coche F1 (60 g) sobre un balance hidráulico, calcula la presión necesaria en un pistón de área 3 cm².
::/act-calc

::act-fill{titulo="A2. Vocabulario hidrostático"}
1. La __________________ es la fuerza por unidad de área (N/m² = Pa).
2. El __________________ de Arquímedes es el empuje hacia arriba sobre un cuerpo sumergido, igual al peso del fluido desplazado.
3. El principio de __________________ dice que la presión aplicada se transmite íntegramente a todas partes de un fluido cerrado.
4. La __________________ es la elevación o descenso de un líquido en un tubo fino debido a la tensión superficial.
::/act-fill

---

### Bloque B · Empuje de Arquímedes (7.1)

::act-calc{titulo="B1. Flotación" renglones=12}
5. Un cubo de madera ($\rho = 600$ kg/m³, lado 8 cm) flota en agua. ¿Qué fracción de su volumen queda sumergida?
6. Un trozo de plomo ($\rho = 11\,300$ kg/m³, $V = 50\,\text{cm}^3$) se sumerge totalmente en agua. Calcula peso real, empuje y peso aparente.
7. Tu coche F1 (60 g) está flotando sobre una piscina de aceite ($\rho = 920$ kg/m³). ¿Qué volumen del coche queda sumergido?
8. Un globo de helio ($\rho_{He} = 0.18$ kg/m³) de 5 L sostiene una carga. ¿Cuánta masa puede levantar en aire ($\rho = 1.20$ kg/m³)?
::/act-calc

---

### Bloque C · Continuidad (7.2)

::act-calc{titulo="C1. Caudal y velocidad" renglones=10}
9. Una manguera de área $A_1 = 5$ cm² lleva agua a $v_1 = 0.8$ m/s. Si la boquilla tiene $A_2 = 1$ cm², ¿qué velocidad sale?
10. ¿Cuál es el caudal volumétrico en m³/s y en L/min?
11. La toma de aire del coche F1 tiene 4 cm². Si el coche viaja a 22 m/s, ¿cuánto aire (en kg/s) entra al sistema? ($\rho_\text{aire}=1.20$ kg/m³)
::/act-calc

---

### Bloque D · Bernoulli (7.2)

::act-calc{titulo="D1. Bernoulli y aerodinámica" renglones=12}
12. En un Venturi con velocidad de garganta $v_2 = 8$ m/s y velocidad de zona ancha $v_1 = 2$ m/s, ¿cuánta diferencia de presión hay entre ambas? ($\rho = 1\,000$ kg/m³)
13. En la cara superior del alerón el aire se mueve a 22 m/s; en la inferior, a 33 m/s. Calcula la diferencia de presión y el downforce sobre un alerón de 25 cm² ($\rho_\text{aire} = 1.20$ kg/m³).
14. Tu coche F1 a 25 m/s tiene $C_d = 0.7$, $A_f = 30$ cm². Estima el drag.
15. Si la velocidad sube a 35 m/s, ¿en qué factor crece el drag?
::/act-calc

::act-tf{titulo="D2. Verdadero o falso"}
1. Bernoulli aplica solo a líquidos, no a gases. ( ) ____________________________________________
2. La fuerza de drag es proporcional al cuadrado de la velocidad. ( ) ____________________________________________
3. En un Venturi, la presión es mayor en la zona estrecha. ( ) ____________________________________________
::/act-tf

---

### Bloque E · Reynolds, viscosidad (7.2)

::act-calc{titulo="E1. Régimen de flujo" renglones=10}
16. Calcula el número de Reynolds para agua ($\rho = 1\,000$, $\mu = 10^{-3}$ Pa·s) en una manguera de 2 cm de diámetro a 0.5 m/s.
17. ¿Es laminar o turbulento? (laminar si Re < 2 300; turbulento si Re > 4 000).
18. Tu coche F1 (longitud 0.30 m) viaja a 22 m/s en aire ($\rho=1.20$, $\mu = 1.8\times 10^{-5}$). Calcula Re y comenta el régimen.
::/act-calc

---

### Bloque F · Mixto / case F1

::act-order{titulo="F1. Ordena los pasos para optimizar el alerón del F1"}
[ ] Predecir downforce y drag para cada variante con Bernoulli.
[ ] Construir tres variantes en CAD con distintos ángulos.
[ ] Calcular la eficiencia DF/Drag y elegir la óptima.
[ ] Validar en pista con datos del coche.
[ ] Simular CFD las tres variantes con SimScale.
::/act-order

::act-match{titulo="F2. Magnitud y unidad SI"}
| Magnitud | Unidad |
|---|---|
| 1. Presión | a) m³/s |
| 2. Caudal | b) Pa |
| 3. Densidad | c) kg/m³ |
| 4. Viscosidad dinámica | d) Pa·s |
::/act-match

---

## Clave de respuestas

| # | Resultado |
|---:|---|
| 1 | $P = 101\,325 + 1\,000\times 9.81\times 12 \approx 219\,045$ Pa |
| 2 | $F_2 = 60\times 200/4 = 3\,000$ N |
| 3 | $P = 1\,000\times 9.81\times 0.5 = 4\,905$ Pa |
| 4 | $P = mg/A = 0.060\times 9.81/3\times 10^{-4} = 1\,962$ Pa |
| 5 | $V_\text{sum}/V = 600/1\,000 = 60\%$ |
| 6 | $W = 5.54$ N; $E = 0.49$ N; $W_\text{ap}=5.05$ N |
| 7 | $V_\text{sum} = m/\rho_f = 0.060/920 = 6.52\times 10^{-5}$ m³ = 65 mL |
| 8 | $m_\text{máx} = (1.20-0.18)\times 0.005 = 5.1\times 10^{-3}$ kg = 5.1 g |
| 9 | $v_2 = A_1 v_1/A_2 = 5\times 0.8/1 = 4$ m/s |
| 10 | $Q = A_1 v_1 = 4\times 10^{-4}$ m³/s = 24 L/min |
| 11 | $\dot m = \rho A v = 1.20\times 4\times 10^{-4}\times 22 = 0.01056$ kg/s |
| 12 | $\Delta P = \tfrac{1}{2}\rho(v_2^2-v_1^2)= 30\,000$ Pa |
| 13 | $\Delta P = 0.5\times 1.20\times (33^2-22^2)=363$ Pa; $F_d = 363\times 25\times 10^{-4}\approx 0.91$ N |
| 14 | $F = 0.5\times 0.7\times 1.20\times 25^2\times 30\times 10^{-4}=0.788$ N |
| 15 | Factor $(35/25)^2 = 1.96$ |
| 16 | $Re = \rho v D/\mu = 1\,000\times 0.5\times 0.02/10^{-3} = 10\,000$ |
| 17 | Turbulento |
| 18 | $Re = 1.20\times 22\times 0.30/1.8\times 10^{-5}\approx 4.4\times 10^5$ → turbulento (esperable en aerodinámica de F1) |
| F1 | 2 → 1 → 5 → 3 → 4 |
| F2 | 1-b · 2-a · 3-c · 4-d |
| A2 | presión · principio · Pascal · capilaridad |
| D2 | 1) F · 2) V · 3) F (es menor) |
