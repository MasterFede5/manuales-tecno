---
unidad: 6
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Motor DC casero + carga inalámbrica Qi"}
**Objetivo.** Construir un motor DC simple a partir de un imán, un alambre y una pila, y luego un cargador inalámbrico básico que demuestre la inducción electromagnética. Ambos proyectos demuestran principios fundamentales de la unidad.

**¿Por qué hacerla?** Construir un motor a mano enseña por qué la corriente y el campo magnético interactúan. Construir un cargador inalámbrico demuestra inducción de Faraday en acción.

---

### Materiales

- 1 alambre de cobre delgado (~5 m).
- 2 pilas de 1.5 V o 9 V.
- 2 imanes de neodimio.
- 1 LED.
- Tornillo o clavo grande.
- Tijeras y cinta aislante.

### Pasos — Motor DC casero

1. Enrolla 30 vueltas de alambre alrededor de un objeto cilíndrico (puede ser una pila).
2. Saca los extremos del alambre como ejes.
3. Coloca el bobinado entre dos imanes en una base.
4. Conecta los extremos a la pila.
5. Empújalo: empezará a girar continuamente.

### Pasos — Cargador inalámbrico simple

1. Enrolla dos bobinas de 50 vueltas cada una (transmisora y receptora).
2. Conecta una a una pila de 9 V con interruptor (transmisora).
3. Conecta la otra a un LED (receptora).
4. Acerca las bobinas; abre y cierra el interruptor.
5. El LED parpadea — recibe energía por inducción.

::visual{tipo="ilustracion" descripcion="Dos viñetas: 1) MOTOR DC — bobinado con eje horizontal entre dos imanes (N y S enfrentados), pila conectada con dos cables, flecha de rotación visible. 2) CARGADOR INALÁMBRICO — bobina transmisora conectada a pila con interruptor a la izquierda, bobina receptora a la derecha conectada a LED, ambas separadas por 1-2 cm. LED encendido cuando hay flujo magnético variable." paginas=0.5}

---

### Entregable

Reporte con fotos de ambos experimentos, explicación física de cada uno (motor: F = IL × B; cargador: ley de Faraday), y respuesta a por qué la pila se descarga al usar el motor.

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Motor** | no funciona | gira | gira a alta velocidad |
| **Cargador** | LED apagado | LED parpadea | LED brillante |
| **Explicación** | "es magia" | menciona campos | usa ecuaciones de la unidad |

---

### Hitos intermedios

| Sprint | Semana | Meta concreta | Evidencia |
|---|---|---|---|
| 1. Bobinado | 1 | Bobina del motor con 30+ vueltas y eje balanceado | foto + medición |
| 2. Motor funcional | 2 | Motor gira de forma estable con pila de 1.5 V | video 10 s |
| 3. Cargador inalámbrico | 3 | LED parpadea con bobina secundaria a ≤ 5 cm | foto + esquema |
| 4. Reporte | 4 | Reporte con ecuaciones, fotos y propuesta de mejora | reporte 4 pp |

### Reto bonus extendido (+2 puntos cada uno)

1. **Caracterización del motor.** Mide la corriente del motor en idle (girando libremente) y bajo carga (con un dedo presionando suavemente). Relaciona el aumento de corriente con la fuerza contraelectromotriz reducida (Ley de Lenz).
2. **Eficiencia del cargador.** Mide la potencia entregada por la pila al primario y la potencia recibida por el LED en el secundario. Calcula la eficiencia de transferencia y discute por qué es baja (alineación, distancia, ferrita).
3. **Generador desde el coche.** Adapta el motor para que funcione **a la inversa**: gírelo manualmente y mide la fem inducida con multímetro. Construye gráfica fem vs velocidad angular y verifica $\varepsilon \propto \omega$.
::/implementacion

---

::albatros{titulo="Caso integrador — diagnóstico de un cortocircuito en el coche F1" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Tu coche F1 deja de transmitir y la batería se calienta. ¿Cómo identificas con un multímetro si hay cortocircuito, fuga o sobreconsumo, sin desarmar el coche entero?

**Lo que harás.**
1. Define qué resistencia esperarías ver entre VCC y GND con el coche apagado (idealmente alta, > 1 kΩ).
2. Mide con multímetro en modo Ω. Si la lectura es < 50 Ω, hay corto.
3. Mide la corriente con multímetro en modo mA en serie con la batería. Compara con el consumo nominal (~120 mA).
4. Si excede 200 mA con el coche apagado, identifica el subsistema sospechoso (sensor IR, regulador, ESP32) desconectándolos uno por uno.
5. Diagnóstico final: indica el componente y la acción correctiva.

**Entregable.** Hoja con: diagrama de bloques con puntos de medición, tabla con $V$ y $I$ esperados y medidos, identificación del problema y plan de reparación.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Diagrama con puntos de medición | impreciso | claro con 4 puntos | + valores esperados |
| Tabla esperado vs medido | sin valores | con valores | + diferencias señaladas |
| Diagnóstico | genérico | identifica subsistema | + plan correctivo cuantitativo |
::/albatros
