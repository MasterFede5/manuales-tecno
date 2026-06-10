---
unidad: 6
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 06

---

::act-mcq{titulo="Electromagnetismo — conceptos clave"}
1. Dos cargas iguales se…
   - [ ] atraen
   - [x] repelen
   - [ ] no interactúan
   - [ ] depende de la distancia

2. La unidad SI de corriente es…
   - [ ] watt
   - [ ] volt
   - [x] ampere
   - [ ] coulomb

3. En un circuito en serie, lo que es igual en todas las resistencias es…
   - [ ] el voltaje
   - [x] la corriente
   - [ ] la potencia
   - [ ] la temperatura

4. La luz es una onda…
   - [ ] longitudinal
   - [x] electromagnética transversal
   - [ ] mecánica
   - [ ] gravitacional

5. ¿Qué onda EM se usa para wifi?
   - [ ] visible
   - [x] microondas
   - [ ] rayos X
   - [ ] gamma
::/act-mcq

---

::act-table{titulo="Circuitos — calcula"}
| V (V) | I (A) | R (Ω) | P (W) |
|---:|---:|---:|---:|
| 12 | 2 |  |  |
|  | 0.5 | 100 |  |
| 9 |  | 18 |  |
::/act-table

---

::act-match{titulo="Componentes y leyes"}
| Componente | Ley o fenómeno |
|---|---|
| 1. Pila | a) Genera campo magnético al pasar I |
| 2. Resistencia | b) Almacena energía en campo eléctrico |
| 3. Capacitor | c) Diferencia de potencial constante |
| 4. Inductor | d) V=IR |
| 5. Cable con corriente | e) Almacena energía en campo magnético |
::/act-match

---

::act-calc{titulo="Cálculos electromagnéticos" renglones=14}
a) ¿Qué fuerza ejercen entre sí dos cargas de 1 µC separadas 10 cm?

b) Una pila de 6 V conectada a una bombilla. Pasan 0.3 A. ¿Cuál es la resistencia?

c) Tres resistencias de 6 Ω en paralelo conectadas a 12 V. ¿Cuál es la corriente total?

d) Un imán produce flujo magnético de 0.5 Wb a través de bobina de 100 vueltas. Si el flujo cambia a 0.2 Wb en 0.1 s, ¿qué emf se induce?

e) La luz visible verde tiene λ = 530 nm. ¿Cuál es su frecuencia?
::/act-calc

---

::act-tf{titulo="Verdadero o falso"}
1. Un imán siempre tiene polos N y S. ( ) ____________________________________________
2. La corriente continua va siempre en un solo sentido. ( ) ____________________________________________
3. La luz no necesita medio para propagarse. ( ) ____________________________________________
4. Las microondas y la luz visible son ondas EM diferentes en naturaleza. ( ) ____________________________________________
5. La inducción electromagnética se descubrió por casualidad. ( ) ____________________________________________
::/act-tf

---

::albatros{titulo="Construye un electroimán casero" tipo="experimento" tiempo="30 min"}
**Pregunta detonadora.** ¿Puedes hacer que un clavo se vuelva imán?

**Lo que harás.**
1. Toma un clavo de hierro de 10 cm.
2. Enrolla 50-100 vueltas de alambre de cobre delgado a su alrededor (de un solo extremo).
3. Conecta los extremos del alambre a una pila de 1.5 V.
4. Acerca clips de papel: el clavo los atrae mientras la corriente pasa.
5. Desconecta la pila: el clavo deja de atraer.

**Materiales.** Clavo · alambre cobre · pila · clips.

**Entregable.** Foto del electroimán funcionando, conteo de clips levantados, explicación con la regla de la mano derecha.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Construcción | sin funcionar | atrae 1 clip | atrae 5+ clips |
| Explicación | "es magia" | identifica el campo magnético | aplica regla de mano derecha |
::/albatros

---

::act-fill{titulo="Vocabulario de electromagnetismo"}
1. La __________________ de un material conductor mide su oposición al paso de corriente y se mide en __________________.
2. La __________________ es la unidad SI de capacidad eléctrica.
3. Un solenoide al que se le hace pasar corriente genera un __________________ análogo al de un imán.
4. La __________________ electromagnética es la generación de fem por flujo magnético variable.
5. La velocidad de la luz en el vacío es $c \approx$ __________________ m/s.
::/act-fill

---

::act-order{titulo="Ordena los pasos para resolver un circuito serie-paralelo"}
[ ] Dibujar el esquema y etiquetar cada componente.
[ ] Calcular corrientes en cada rama con Ley de Ohm.
[ ] Identificar bloques en serie y bloques en paralelo.
[ ] Reducir cada bloque a una sola resistencia equivalente.
[ ] Verificar con Kirchhoff de corrientes en cada nodo.
[ ] Calcular la corriente total a partir del voltaje de la fuente.
::/act-order

---

::act-label{titulo="Etiqueta el sistema eléctrico del coche F1"}
::visual{tipo="diagrama-flujo" descripcion="Diagrama de bloques del sistema eléctrico del coche F1: batería LiPo a la izquierda, regulador 3.3 V, ESP32 con dos salidas (sensor IR y LED indicador), antena Wi-Fi en la parte superior, todos conectados con cables etiquetados con el voltaje y la corriente típica. Tierra común mostrada con símbolo GND." paginas=0.5}
> Marca: a) batería · b) regulador · c) microcontrolador · d) sensor · e) actuador (LED) · f) antena Wi-Fi · g) tierra común.
::/act-label

---

::act-puzzle{titulo="Crucigrama — circuitos y EM" tipo="crucigrama" tamano="12x12"}
Horizontales:
1. Componente que almacena energía en campo eléctrico.
3. Apellido del científico de la ley I = V/R.
6. Onda EM con $\lambda$ entre 1 mm y 1 m.

Verticales:
2. Apellido del descubridor de la inducción electromagnética.
4. Componente que almacena energía en campo magnético.
5. Cantidad de carga por unidad de tiempo.
7. Magnitud que se conserva en cada nodo de un circuito.
::/act-puzzle

---

::act-case{titulo="Caso para resolver — la batería que dura la mitad" lineas=10}
Tu equipo cambia la batería del coche F1 de 1 200 mAh por una de 2 400 mAh sin modificar nada más, y la autonomía aumenta solo 30 % en lugar del 100 % esperado. Argumenta con cálculos qué efectos no lineales pueden estar pasando (caída de voltaje por resistencia interna, eficiencia del regulador, deep-sleep mal configurado) y propón un plan de tres mediciones para identificar el culpable.
::/act-case

---

::albatros{titulo="Reto Albatros — mini-generador eólico para la base del F1" tipo="reto" tiempo="50 min"}
**Pregunta detonadora.** ¿Cuántos LEDs puedes encender con una bobina y un imán girando a la velocidad de tu boca soplándole?

**Lo que harás.**
1. Construye una bobina con 200 vueltas de alambre fino sobre un cilindro de 3 cm de diámetro.
2. Pega un imán de neodimio en un eje (palo de paleta + base).
3. Conecta la bobina a un puente de diodos sencillo (4 diodos) para rectificar la corriente, y a un capacitor de filtrado de 100 µF.
4. Conecta un LED rojo en serie con resistencia de 220 Ω a la salida del capacitor.
5. Sopla el imán para hacerlo girar; observa el LED.
6. Mide con multímetro el voltaje de salida promedio en función de la velocidad angular (estimada).
7. Calcula la fem máxima esperada y compara con la medida.

**Materiales.** Alambre de cobre fino, imán de neodimio, palo de paleta, 4 diodos 1N4148, capacitor 100 µF, LED rojo, resistencia 220 Ω, multímetro.

**Entregable.** Hoja con esquema, tabla de fem en función de velocidad, comparación con teoría ($\varepsilon = NBA\omega$), recomendación para encender más LEDs.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Construcción | bobina sin contar vueltas | bobina con $N$ documentado | + medición de $A$ y $B$ |
| Mediciones | sin tabla | 3 puntos en tabla | + comparación con teoría |
| Recomendación | genérica | con un cambio | con cambio + estimación cuantitativa |
::/albatros
