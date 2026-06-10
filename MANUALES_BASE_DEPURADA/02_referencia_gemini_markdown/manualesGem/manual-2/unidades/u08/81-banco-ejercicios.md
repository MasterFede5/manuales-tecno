---
unidad: 8
seccion: banco-ejercicios
paginas_objetivo: 4
---

## Banco de ejercicios — Óptica

Resuelve cada problema con datos, fórmula, sustitución y resultado con unidades. Aplica al sistema de visión del coche F1 cuando puedas.

---

### Bloque A · Reflexión y refracción · Snell (8.1)

::act-calc{titulo="A1. Ley de Snell" renglones=12}
1. Luz pasa de aire ($n=1$) a agua ($n=1.33$) con $\theta_1 = 40°$. Calcula $\theta_2$.
2. Luz pasa de agua a aire con $\theta_1 = 60°$. ¿Refracta o se refleja totalmente?
3. Calcula el ángulo crítico de un vidrio ($n=1.50$) al aire.
4. Luz pasa del agua a aceite ($n=1.45$) con $\theta_1 = 35°$. Calcula $\theta_2$.
5. Una fibra óptica de $n_\text{núcleo}=1.50$ y $n_\text{recubrimiento}=1.45$. Calcula el ángulo crítico para reflexión total interna en su interfaz.
::/act-calc

::act-fill{titulo="A2. Reflexión y refracción"}
1. La __________________ es el cambio de dirección al cambiar de medio óptico.
2. La __________________ total interna ocurre cuando la luz va de un medio más denso a uno menos denso con $\theta > \theta_c$.
3. El __________________ de refracción de un medio se define como $n = c/v$.
4. Cuando la luz se refleja, el ángulo de __________________ es igual al de __________________.
::/act-fill

---

### Bloque B · Espejos planos y esféricos (8.2)

::act-calc{titulo="B1. Espejos" renglones=12}
6. Un objeto está a 25 cm frente a un espejo plano. ¿Dónde y cómo es la imagen?
7. Un espejo cóncavo tiene $f = 12$ cm. Un objeto está a $p = 30$ cm. Calcula $q$, $M$ y describe la imagen.
8. Mismo espejo con objeto a $p = 6$ cm. Calcula $q$, $M$ y descripción.
9. Un espejo convexo de $f = -20$ cm tiene un objeto a $p = 25$ cm. Calcula $q$, $M$ y describe.
10. Para tu coche F1, montas un espejo retrovisor convexo de $f = -8$ cm. Si un coche rival está a 1 m detrás, ¿dónde aparece su imagen?
::/act-calc

---

### Bloque C · Lentes (8.3)

::act-calc{titulo="C1. Lentes convergentes y divergentes" renglones=14}
11. Una lente de $f = 10$ cm forma imagen de un objeto a $p = 25$ cm. Calcula $q$, $M$ y tipo de imagen.
12. Misma lente con $p = 8$ cm. Calcula $q$, $M$ y tipo (¿imagen virtual o real?).
13. Una lente divergente de $f = -15$ cm con objeto a $p = 30$ cm. Calcula $q$, $M$ y tipo.
14. Calcula la potencia (en dioptrías) de una lente con $f = 50$ cm.
15. La cámara on-board del coche F1 tiene lente de $f = 4$ mm. Si un cono está a 5 m, ¿a qué distancia del sensor se forma la imagen? Aplica $1/f = 1/p + 1/q$.
::/act-calc

::act-tf{titulo="C2. Verdadero o falso"}
1. Una lente divergente forma imagen real cuando el objeto está dentro del foco. ( ) ____________________________________________
2. La potencia óptica se mide en dioptrías (1/m). ( ) ____________________________________________
3. El aumento $M < 0$ indica imagen invertida. ( ) ____________________________________________
::/act-tf

---

### Bloque D · Dualidad onda-partícula (8.4)

::act-calc{titulo="D1. Energía de fotones y fotoeléctrico" renglones=12}
16. Calcula la energía de un fotón de luz roja ($\lambda = 650$ nm) en J y eV.
17. Calcula la energía de un fotón de UV ($\lambda = 250$ nm) en eV.
18. Un metal tiene $\varphi = 2.0$ eV. Calcula la frecuencia umbral $f_0$ y $\lambda_0$.
19. Si lo iluminas con luz de 350 nm, ¿cuál es la energía cinética máxima del fotoelectrón?
20. Para el sensor CMOS del coche F1, asumiendo umbral fotoeléctrico equivalente $\varphi = 1.1$ eV (Si), ¿qué $\lambda$ máxima detecta?
::/act-calc

---

### Bloque E · Young e interferencia (8.4)

::act-calc{titulo="E1. Doble rendija" renglones=10}
21. Young con $d = 0.30$ mm, $L = 1.5$ m, $\lambda = 550$ nm. Calcula $\Delta y$.
22. ¿Cuántas franjas brillantes caben en un pantalla de 5 cm centrada?
23. Si cambias a $\lambda = 633$ nm (láser rojo), recalcula $\Delta y$.
::/act-calc

---

### Bloque F · Mixto / case F1

::act-order{titulo="F1. Ordena los pasos para diseñar la cámara on-board"}
[ ] Calcular el campo de visión angular: $\tan(\alpha/2) = (\text{ancho}/2)/f$.
[ ] Determinar el tamaño y resolución del sensor.
[ ] Elegir distancia focal según el ángulo deseado.
[ ] Verificar que la imagen del objeto más pequeño cubra ≥ 5 píxeles.
[ ] Validar con foto de una regla a distancia conocida.
::/act-order

::act-match{titulo="F2. Componente y función"}
| Componente | Función |
|---|---|
| 1. Lente convergente | a) Sensor de imagen |
| 2. Lente divergente | b) Forma imagen real para cámara |
| 3. Espejo cóncavo | c) Anteojos para miopía |
| 4. CMOS | d) Telescopio reflector |
::/act-match

---

## Clave de respuestas

| # | Resultado |
|---:|---|
| 1 | $\theta_2 = \arcsin(\sin 40°/1.33)\approx 28.9°$ |
| 2 | $\theta_c = \arcsin(1/1.33)=48.8°$. Como 60°>48.8° → reflexión total |
| 3 | $\theta_c = \arcsin(1/1.50)\approx 41.8°$ |
| 4 | $\theta_2 = \arcsin(1.33\sin 35°/1.45)\approx 31.7°$ |
| 5 | $\theta_c = \arcsin(1.45/1.50)\approx 75.2°$ |
| 6 | Imagen a 25 cm detrás del espejo, virtual, derecha, mismo tamaño |
| 7 | $q=20$ cm; $M=-2/3$; real, invertida, reducida |
| 8 | $1/q=1/12-1/6=-1/12$ → $q=-12$ cm; $M=2$; virtual, derecha, ampliada |
| 9 | $1/q=-1/20-1/25=-0.09$ → $q=-11.1$ cm; $M=0.444$; virtual, derecha, reducida |
| 10 | $1/q = -1/8-1/100=-0.135$ → $q\approx -7.4$ cm; $M\approx 0.074$ |
| 11 | $q=16.67$ cm; $M=-0.67$; real, invertida, reducida |
| 12 | $1/q=1/10-1/8=-0.025$ → $q=-40$ cm; $M=5$; virtual, derecha, ampliada |
| 13 | $q\approx -10$ cm; $M\approx 0.33$; virtual, derecha, reducida |
| 14 | $P = 1/0.50 = 2$ D |
| 15 | $1/q=1/0.004 - 1/5=249.8$; $q=4.003$ mm |
| 16 | $E=hc/\lambda=3.06\times 10^{-19}$ J = 1.91 eV |
| 17 | $E\approx 4.97$ eV |
| 18 | $f_0 = 4.83\times 10^{14}$ Hz; $\lambda_0=620$ nm |
| 19 | $E_k = h c/\lambda - \varphi = 3.55-2.0 = 1.55$ eV |
| 20 | $\lambda_\text{máx} = hc/\varphi = 1\,127$ nm (infrarrojo cercano) |
| 21 | $\Delta y = \lambda L/d = 2.75\times 10^{-3}$ m = 2.75 mm |
| 22 | $\approx 18$ franjas |
| 23 | $\Delta y = 633\times 10^{-9}\times 1.5/3\times 10^{-4}=3.17$ mm |
| F1 | 2 → 3 → 1 → 4 → 5 |
| F2 | 1-b · 2-c · 3-d · 4-a |
| A2 | refracción · reflexión · índice · incidencia / reflexión |
| C2 | 1) F · 2) V · 3) V |
