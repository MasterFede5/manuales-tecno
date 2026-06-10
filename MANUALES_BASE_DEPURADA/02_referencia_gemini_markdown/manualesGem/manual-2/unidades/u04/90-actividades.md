---
unidad: 4
seccion: actividades
paginas_objetivo: 4
---

## Actividades — Unidad 04

---

::act-mcq{titulo="Termodinámica — conceptos clave"}
1. La temperatura es una medida de…
   - [ ] el calor total del sistema
   - [x] la energía cinética promedio molecular
   - [ ] la masa del sistema
   - [ ] la presión

2. La unidad SI de calor es…
   - [ ] caloría
   - [ ] kelvin
   - [x] joule
   - [ ] grado Celsius

3. Un mecanismo de transferencia de calor que requiere medio material es…
   - [ ] radiación
   - [x] conducción
   - [ ] vacío
   - [ ] luz

4. La eficiencia de Carnot depende de…
   - [ ] la masa del gas
   - [ ] el material del motor
   - [x] las temperaturas de los reservorios
   - [ ] el tiempo de operación

5. ¿En cuál cambio de fase se ABSORBE calor latente?
   - [ ] Solidificación
   - [x] Fusión
   - [ ] Condensación
   - [ ] Deposición
::/act-mcq

---

::act-table{titulo="Conversiones de temperatura — completa"}
| °C | °F | K |
|---:|---:|---:|
| 0 |  | 273.15 |
|  | 32 |  |
| 25 |  |  |
| 100 |  |  |
| -40 | -40 |  |
|  |  | 0 |
::/act-table

---

::act-match{titulo="Mecanismos de transferencia de calor"}
| Situación | Mecanismo dominante |
|---|---|
| 1. Mantener un café caliente en termo | a) Conducción |
| 2. Enfriarte poniendo paño con agua | b) Convección |
| 3. Calentarte al sol | c) Radiación |
| 4. Cuchara metálica que se calienta en sopa | (a) |
| 5. Aire caliente que sube cerca de un radiador | (b) |
| 6. Tu cuerpo emitiendo calor en infrarrojo | (c) |
::/act-match

---

::act-calc{titulo="Cálculos termodinámicos" renglones=14}
a) ¿Cuánto calor se necesita para calentar 1 L de agua de 20 °C a 90 °C?

b) Si tienes 200 g de hielo a 0 °C y le entregas 100 kJ, ¿cuánto se derrite y cuál es la temperatura final?

c) Una varilla de cobre de 1 m de largo a 20 °C se calienta a 80 °C. ¿Cuánto se alarga? (α=17×10⁻⁶/°C)

d) Un motor opera entre 800 K y 300 K. ¿Cuál es su eficiencia máxima de Carnot?

e) Una taza de café (200 g, 80 °C) se enfría hasta equilibrio con aire ambiente (15 m³ a 20 °C). Asume calor específico de aire ≈ 1000 J/kg·K, densidad 1.2 kg/m³. ¿Temperatura final?

f) ¿Cuál es la velocidad rms de una molécula de N₂ a 300 K? (M=28 g/mol)
::/act-calc

---

::act-tf{titulo="Verdadero o falso"}
1. La temperatura es energía. ( ) ____________________________________________
2. Cuando un gas se expande adiabáticamente, su temperatura sube. ( ) ____________________________________________
3. La eficiencia 100 % es teóricamente posible si T_frío = 0 K. ( ) ____________________________________________
4. La 2ª Ley dice que la entropía siempre disminuye en sistemas aislados. ( ) ____________________________________________
5. La conducción solo ocurre en sólidos. ( ) ____________________________________________
::/act-tf

---

::albatros{titulo="Mide el calor específico del agua con un calentador casero" tipo="experimento" tiempo="60 min"}
**Pregunta detonadora.** ¿Cuánta energía eléctrica necesitas para calentar agua? ¿Coincide con la teoría?

**Lo que harás.**
1. Llena un recipiente aislado con 500 mL de agua. Mide T_inicial.
2. Sumerge una resistencia eléctrica conocida (calentador de inmersión, ~150-300 W).
3. Mide la potencia (multiplica V × I si tienes amperímetro y voltímetro, o usa la nominal del calentador).
4. Calienta durante 5 minutos exactos. Mide T_final.
5. Calcula la energía eléctrica entregada: $E = P \times t$.
6. Calcula la energía absorbida por el agua: $Q = m c \Delta T$.
7. Compara: la diferencia es energía perdida (al recipiente, ambiente).

**Materiales.** 500 mL agua · termómetro · cronómetro · calentador eléctrico · vaso aislado.

**Entregable.** Tabla con datos, cálculo de eficiencia ($Q/E$), análisis de pérdidas.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Mediciones | sin precisión | datos correctos | con incertidumbre |
| Cálculo | sin teoría | Q calculado | comparación con E eléctrica |
| Análisis | "perdió calor" | identifica pérdidas | propone mejora del aislamiento |
::/albatros

---

::act-fill{titulo="Vocabulario termodinámico"}
1. La __________________ es la cantidad de calor necesaria para elevar 1 K la temperatura de 1 kg de sustancia.
2. El calor __________________ es la energía absorbida o cedida durante un cambio de fase.
3. La __________________ es el mecanismo de transferencia de calor sin necesidad de medio material.
4. La eficiencia de __________________ depende solo de las temperaturas de los reservorios.
5. La 2ª ley afirma que la __________________ del universo nunca disminuye en procesos espontáneos.
::/act-fill

---

::act-order{titulo="Ordena el procedimiento del calorímetro"}
[ ] Aplicar $Q_\text{cedido} + Q_\text{absorbido} = 0$.
[ ] Pesar e identificar masa y calor específico de cada cuerpo.
[ ] Esperar al equilibrio térmico y registrar $T_f$.
[ ] Sustituir y despejar la incógnita.
[ ] Mezclar los cuerpos en el recipiente aislado.
[ ] Medir temperaturas iniciales por separado.
::/act-order

---

::act-label{titulo="Etiqueta el ciclo de Carnot en el diagrama PV"}
> Marca: a) isoterma caliente · b) isoterma fría · c) expansión adiabática · d) compresión adiabática · e) área = trabajo neto.
::/act-label


::visual{tipo="diagrama-flujo" descripcion="Diagrama PV de un ciclo de Carnot ideal: dos isotermas (T caliente arriba y T fría abajo) y dos adiabáticas conectándolas. Se identifican los cuatro estados A, B, C, D, y se marca el sentido de avance horario para máquina térmica. Áreas y trabajos se etiquetan con flechas." paginas="0.5" src="../manualesGem/assets/visuales/manual-2/u04/90-actividades-v01.svg"}
---

::act-puzzle{titulo="Crucigrama — termodinámica" tipo="crucigrama" tamano="12x12"}
Horizontales:
1. Mecanismo de calor que requiere medio material y movimiento de fluido.
4. Cambio de líquido a gas.
6. Sistema en el que no hay intercambio de materia ni de energía con el ambiente.

Verticales:
2. Ciclo ideal de máxima eficiencia.
3. Magnitud que mide el desorden estadístico.
5. Cantidad conservada según la 1ª ley (energía total del sistema más entorno).
::/act-puzzle

---

::act-case{titulo="Caso para resolver — el coche que se sobrecalienta" lineas=10}
Después de tres carreras seguidas, el chasis del coche F1 alcanza 70 °C y la balsa empieza a deformarse. Tu equipo evalúa tres soluciones: (a) pintar el chasis de blanco para reducir absorción radiativa, (b) instalar mini-radiadores de aluminio, (c) esperar 5 min entre carreras. Argumenta con cálculos cuál baja más la temperatura entre carreras y a qué costo en tiempo de operación.
::/act-case

---

::albatros{titulo="Reto Albatros — auditoría térmica de tu salón con cámara IR" tipo="investigacion-corta" tiempo="40 min"}
**Pregunta detonadora.** ¿Dónde se "fuga" el calor (o el frío) de tu salón de clases? ¿Cuántos pesos al año podrías ahorrar identificando esas fugas?

**Lo que harás.**
1. Pide prestada una cámara IR (smartphone con accesorio FLIR/Seek o el MLX90640 de la implementación) o usa termómetro IR de mano si no hay cámara.
2. Recorre tu salón y mide temperatura en al menos **8 zonas**: marco de ventana, puerta, pared exterior, pared interior, contacto eléctrico, ducto de aire, suelo, techo.
3. Construye un mapa esquemático del salón con las temperaturas anotadas.
4. Identifica al menos **3 puentes térmicos** (zonas con $\Delta T > 5$ °C respecto a su entorno).
5. Estima la potencia de pérdida con $\dot Q = U A \Delta T$, asumiendo $U \approx 3\,\text{W/(m}^2\text{·K)}$ para vidrio simple.
6. Convierte a costo anual asumiendo \$2.5/kWh y 8 h/día de uso del aire acondicionado o calefactor.

**Entregable.** Mapa esquemático con temperaturas, lista de 3 fugas con potencia y costo, propuesta de mejora con costo estimado.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Mapa térmico | <5 puntos | 8 puntos | + leyenda y escala |
| Identificación de fugas | ausente | identifica 3 | + cálculo de $\dot Q$ |
| Cálculo de costo | sin valor | con valor anual | + propuesta con ROI |
::/albatros
