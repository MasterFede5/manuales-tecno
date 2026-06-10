---
unidad: 8
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 08

---

::act-mcq{titulo="Óptica — conceptos clave"}
1. Cuando la luz pasa de aire a agua, su…
   - [ ] frecuencia disminuye
   - [x] velocidad y longitud de onda disminuyen, pero la frecuencia se mantiene
   - [ ] frecuencia aumenta
   - [ ] energía por fotón cambia drásticamente

2. Un espejo plano forma una imagen…
   - [ ] real, invertida, ampliada
   - [x] virtual, derecha, del mismo tamaño
   - [ ] real, derecha, reducida
   - [ ] virtual, invertida, ampliada

3. Para usar un espejo cóncavo como espejo de maquillaje (verte ampliado y derecho) tienes que poner tu cara…
   - [ ] más allá del centro de curvatura
   - [ ] exactamente en F
   - [x] entre F y el espejo
   - [ ] no es posible con espejo cóncavo

4. Una lente con potencia $-2.5\,\text{D}$ es…
   - [ ] convergente, $f=+0.4\,\text{m}$
   - [x] divergente, $f=-0.4\,\text{m}$
   - [ ] convergente, $f=-2.5\,\text{m}$
   - [ ] divergente, $f=+2.5\,\text{m}$

5. El experimento que **no** se puede explicar con la luz como onda continua es…
   - [ ] reflexión en espejo plano
   - [ ] refracción en una piscina
   - [ ] interferencia de Young
   - [x] efecto fotoeléctrico

6. Si duplicas la frecuencia de la luz incidente en un metal y supera la frecuencia umbral, la energía cinética máxima de los electrones expulsados…
   - [ ] no cambia
   - [ ] se duplica exactamente
   - [x] aumenta en una cantidad que depende de $\varphi$
   - [ ] disminuye
::/act-mcq

---

::act-table{titulo="Aplica las ecuaciones de espejos y lentes"}
| Caso | $p$ (cm) | $f$ (cm) | $q$ (cm) | $M$ | Tipo de imagen |
|---|---:|---:|---:|---:|---|
| Espejo cóncavo | 30 | 10 |  |  |  |
| Espejo cóncavo | 8 | 10 |  |  |  |
| Espejo convexo | 20 | -15 |  |  |  |
| Lente convergente | 30 | 10 |  |  |  |
| Lente divergente | 25 | -10 |  |  |  |
::/act-table

---

::act-match{titulo="Relaciona el fenómeno con su aplicación"}
| Fenómeno | Aplicación |
|---|---|
| 1. Reflexión total interna | a) Anteojos para miopía |
| 2. Refracción | b) Cámara fotográfica |
| 3. Lente divergente | c) Internet por fibra óptica |
| 4. Lente convergente | d) Lupa |
| 5. Espejo cóncavo | e) Telescopio reflector |
| 6. Efecto fotoeléctrico | f) Sensor CMOS de tu teléfono |
::/act-match

---

::act-calc{titulo="Cálculos de óptica geométrica y cuántica" renglones=14}
a) Un rayo de luz pasa de vidrio (n=1.50) a aire (n=1.00) con ángulo de incidencia 35°. Calcula el ángulo de refracción y verifica si hay reflexión total interna.

b) Una lente convergente de $f = 8$ cm forma imagen de un objeto a $p = 12$ cm. Calcula $q$, $M$ y el tipo de imagen.

c) En el experimento de Young con $\lambda = 500$ nm, $d = 0.20$ mm, $L = 1.5$ m. Calcula la posición del primer y segundo máximo.

d) Calcula la energía en eV de un fotón de luz roja ($\lambda = 700$ nm) y de un fotón de luz UV ($\lambda = 250$ nm). ¿Cuál tiene más energía?

e) Un metal tiene función trabajo $\varphi = 2.5$ eV. Calcula la frecuencia umbral $f_0$ y la longitud de onda umbral $\lambda_0$.
::/act-calc

---

::act-tf{titulo="Verdadero o falso (justifica)"}
1. La luz disminuye su velocidad cuando entra al agua, pero su frecuencia sigue siendo la misma. ( ) ____________________________________________
2. Un espejo plano puede formar imágenes reales si lo inclinas correctamente. ( ) ____________________________________________
3. Las lentes divergentes nunca pueden formar imagen real. ( ) ____________________________________________
4. Aumentar la intensidad de la luz por debajo de la frecuencia umbral acaba expulsando electrones del metal. ( ) ____________________________________________
5. La luz roja tiene más energía por fotón que la luz violeta. ( ) ____________________________________________
6. Las lentes de los teléfonos modernos forman imagen invertida en el sensor; el software la voltea antes de mostrarla. ( ) ____________________________________________
::/act-tf

---

::act-label{titulo="Etiqueta el sistema óptico de la cámara on-board"}
::visual{tipo="ilustracion" descripcion="Esquema lateral de cámara on-board del coche F1: caja rectangular con lente biconvexa al frente, plano focal donde se ubica el sensor CMOS, cable saliendo por atrás hacia el ESP32. Pista de fondo con un cono. Rayos del cono entrando por la lente y formando imagen invertida en el sensor." paginas=0.5}
> Marca: a) lente convergente · b) eje óptico · c) plano focal · d) sensor CMOS · e) imagen invertida del cono · f) distancia focal $f$
::/act-label

---

::albatros{titulo="Mide el índice de refracción del agua con tu celular" tipo="experimento" tiempo="40 min"}
**Pregunta detonadora.** ¿Puedes medir tú mismo el índice de refracción del agua con un vaso, un transportador y la cámara de tu teléfono?

**Lo que harás.**
1. Llena un vaso de vidrio cilíndrico hasta la mitad con agua.
2. Pega un transportador detrás del vaso (que se vea claramente desde el otro lado).
3. Apunta un puntero láser (o linterna del celular con cinta opaca para hacer haz fino) horizontalmente hacia el vaso, justo en la línea del agua, con un ángulo conocido $\theta_1$.
4. Toma una foto desde arriba donde se vea el haz entrando al agua y refractándose.
5. Mide $\theta_1$ y $\theta_2$ con el transportador en la foto.
6. Calcula $n_{agua} = \sin\theta_1 / \sin\theta_2$.
7. Repite con $\theta_1 = 30°$, $45°$, $60°$. Promedia.
8. Compara con el valor tabulado (1.33). Calcula el error porcentual.

**Materiales.** Vaso transparente · transportador · láser barato o linterna del celular · cinta opaca · regla · agua.

**Entregable.** Reporte de 1 página con: a) tabla de los 3 ángulos, b) cálculo de $n$ promedio, c) discusión del error y posibles fuentes (paralaje, ángulo del transportador, refracción en las paredes del vaso), d) foto de la medición.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Procedimiento | sin medir | mide pero un solo ángulo | tres ángulos diferentes |
| Resultado | $n$ fuera del rango 1.0-2.0 | $n$ entre 1.2 y 1.5 | $n$ entre 1.30 y 1.36 |
| Análisis del error | sin discutir | menciona alguna fuente | discute paralaje y refracción de pared |
::/albatros

---

::act-fill{titulo="Vocabulario óptico"}
1. La __________________ óptica de una lente se mide en dioptrías y es el inverso de la distancia focal en metros.
2. Una imagen __________________ no se puede proyectar en una pantalla; existe solo en la prolongación geométrica de los rayos.
3. El __________________ lateral $M$ es la razón entre tamaño de imagen y tamaño de objeto.
4. Un fotón con $\lambda = 500$ nm tiene mayor energía que uno con $\lambda = 700$ nm porque $E = h c/\lambda$ es __________________.
::/act-fill

---

::act-order{titulo="Ordena los pasos para resolver un problema con lente"}
[ ] Identificar tipo de lente (signo de $f$).
[ ] Sustituir y despejar $q$.
[ ] Calcular el aumento $M = -q/p$.
[ ] Aplicar la ecuación $1/p + 1/q = 1/f$.
[ ] Describir la imagen (real/virtual, derecha/invertida, ampliada/reducida).
[ ] Verificar signos y unidades.
::/act-order

---

::act-puzzle{titulo="Crucigrama — óptica" tipo="crucigrama" tamano="12x12"}
Horizontales:
1. Apellido del científico que midió la velocidad de la luz con dos espejos giratorios.
3. Lente que diverge los rayos paralelos.
5. Fenómeno por el que la luz cambia de dirección al cambiar de medio.
7. Apellido del autor del experimento de doble rendija.

Verticales:
2. Lente que converge los rayos paralelos.
4. Tipo de imagen que se forma detrás del espejo plano.
6. Unidad de potencia óptica.
8. Magnitud que es inversamente proporcional a $\lambda$ en un fotón.
::/act-puzzle

---

::act-mindmap{titulo="Mapa mental — sistema óptico del coche F1" centro="ÓPTICA EN EL F1" nodos_primarios=4 nodos_secundarios=10}
Para cada nodo (faros · cámara on-board · sensor de línea · señal IR de telemetría) escribe: 1) componente óptico clave · 2) ecuación principal · 3) magnitud característica.
::/act-mindmap

---

::act-case{titulo="Caso para resolver — la cámara que ve borroso a 10 m" lineas=10}
La cámara on-board del coche F1 muestra los conos a 5 m con nitidez pero a 10 m se ven manchas borrosas. Tu equipo evalúa tres mejoras: (a) lente con $f$ doble (8 mm), (b) sensor de doble resolución ($1\,280\times 720$), (c) iluminación adicional con LEDs blancos. Argumenta con cálculos de píxeles por cono cuál mejora más la detección a 10 m y a 15 m.
::/act-case

---

::albatros{titulo="Reto Albatros — espectro con CD y celular" tipo="experimento" tiempo="40 min"}
**Pregunta detonadora.** ¿Qué colores se esconden en la luz blanca del Sol y qué colores faltan al iluminar con un foco LED? ¿Cómo lo descubres con un CD viejo?

**Lo que harás.**
1. Construye un espectroscopio casero con una caja de cartón pequeña, una rendija fina (cinta + cúter) en una cara y un trozo de CD (lado plateado) en la cara opuesta a 45°.
2. Apunta la rendija al Sol indirectamente (luz reflejada en pared blanca, NUNCA al Sol directo) y observa el espectro reflejado en el CD por la otra abertura. Toma foto con celular.
3. Repite con: un foco incandescente, un foco LED blanco, una luz fluorescente.
4. Compara los cuatro espectros. Identifica si hay líneas brillantes/oscuras o si el espectro es continuo.
5. Estima las longitudes de onda extremas (rojo ~700 nm, violeta ~400 nm) y mide proporcionalmente las posiciones de las líneas observadas.

**Materiales.** Caja de cartón, CD viejo, cinta opaca, regla, smartphone.

**Entregable.** Hoja con: 4 fotos de espectros, descripción cualitativa de cada uno (continuo, con bandas, con líneas), comparación con la teoría (Sol = continuo con líneas de Fraunhofer; LED = bandas).

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Construcción | sin separar colores | espectro visible | + rendija fina y rango cubierto |
| Comparación de fuentes | 1 fuente | 3 fuentes | 4 con descripción cualitativa |
| Conexión teórica | descriptiva | menciona continuo vs discreto | + correlación con física atómica |
::/albatros
