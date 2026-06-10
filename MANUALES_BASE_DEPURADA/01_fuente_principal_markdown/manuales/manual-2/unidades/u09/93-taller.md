---
unidad: 9
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Curva I-V de una mini celda solar para la flota F1

Un taller de 60 minutos donde tu equipo F1 Albatros caracteriza experimentalmente la curva corriente-voltaje (I-V) de un panel solar pequeño y deduce el punto de máxima potencia (MPP), la eficiencia y los efectos de sombra parcial. Aplica los subtemas 9.1 (efecto fotoeléctrico en celdas Si) y 9.3 (energías renovables).

::albatros{titulo="Taller — Caracterización I-V y eficiencia de mini celda solar" tipo="experimento" tiempo="60 min"}
**Pregunta detonadora.** ¿Tu mini celda solar entrega realmente lo que dice la etiqueta? ¿Qué tan alejado está el punto de operación real del MPP teórico?

**Lo que harás.** Mediré sistemáticamente $V$ e $I$ con cargas variables (resistencias decadas), construirás la curva I-V completa, identificarás $V_\text{oc}$, $I_\text{sc}$ y MPP, calcularás la eficiencia real y simularás el efecto de sombra cubriendo parte del panel.

**Materiales.**
- Mini celda solar de 5–6 V / 1–2 W (Steren o similar, ≈ 60 MXN).
- Multímetro digital con rangos $V$ y $mA$.
- Caja de resistencias decadas o set de 10 resistencias entre 10 Ω y 10 kΩ (10, 47, 100, 220, 470, 1k, 2.2k, 4.7k, 6.8k, 10k Ω).
- Luxómetro de mano o app de luxómetro de smartphone.
- Cinta opaca para simular sombras.
- Hoja de registro y plantilla de tabla.

**Pasos.**

1. **Setup.** Coloca la celda solar bajo iluminación estable (Sol pleno, mediodía). Mide la irradiancia en lux (1 sol pleno ≈ 100 000 lux). Anota condiciones (hora, día, nubosidad).

2. **Circuito abierto.** Mide $V_\text{oc}$ con el multímetro en modo voltímetro (alta impedancia). Anota.

3. **Cortocircuito.** Cambia el multímetro al modo amperímetro y conecta directamente terminal a terminal. Mide $I_\text{sc}$. Anota.

4. **Curva I-V.** Para cada resistencia $R_i$ del set:
   - Conecta la celda a la resistencia.
   - Mide $V_i$ (en paralelo con la resistencia) y $I_i$ (en serie con el multímetro en mA).
   - Calcula $P_i = V_i \cdot I_i$.

5. **Tabla de datos.**

   | $R$ (Ω) | $V$ (V) | $I$ (mA) | $P$ (mW) |
   |---:|---:|---:|---:|
   | $\infty$ (oc) | $V_\text{oc}$ | 0 | 0 |
   | 10 000 | | | |
   | 6 800 | | | |
   | 4 700 | | | |
   | 2 200 | | | |
   | 1 000 | | | |
   | 470 | | | |
   | 220 | | | |
   | 100 | | | |
   | 47 | | | |
   | 10 | | | |
   | 0 (sc) | 0 | $I_\text{sc}$ | 0 |

6. **Gráfica I-V y P-V.** En papel milimétrico o GeoGebra:
   - I vs V: empieza en (0, $I_\text{sc}$), termina en ($V_\text{oc}$, 0); típicamente forma de "rodilla".
   - P vs V: parábola con máximo en MPP.

7. **Identifica MPP.** Marca el punto $(V_\text{mpp}, I_\text{mpp})$ donde $P$ es máxima. Anota $P_\text{mpp}$.

8. **Eficiencia.** Estima el área $A$ de la celda y la potencia luminosa que recibe: $P_\text{luz} = E \cdot A$, con $E$ la irradiancia (≈ 1 000 W/m² al sol pleno).
$$\eta = P_\text{mpp}/P_\text{luz}\times 100\%$$
Compara con el rating del fabricante.

9. **Efecto de sombra.** Cubre con cinta opaca el 25 % de la celda (en una franja). Repite la medida de $V_\text{oc}$ e $I_\text{sc}$. Compara: ¿la corriente cae 25 %, más, o menos?

10. **Discute "el celda más débil manda".** En una conexión en serie, la celda con más sombra **limita** la corriente del conjunto. Explica con tus datos.

11. **Aplicación al case F1.** Con $P_\text{mpp}$ medido, calcula cuántas celdas necesitas para cargar una batería 3.7 V·1 200 mAh en 1 hora ($E = V \cdot I \cdot t$).

12. **Recomendación.** Cada equipo escribe la ubicación y orientación óptimas en el techo de la escuela y propone un protocolo de limpieza para evitar pérdidas por polvo (típicamente 5–15 %).

**Entregable.** Bitácora de 1.5 páginas con: tabla I-V completa, gráficas I-V y P-V, valores de $V_\text{oc}$, $I_\text{sc}$, MPP y $\eta$, comparación con sombra parcial, número de celdas necesarias para cargar una batería F1 en 1 h.

**Rúbrica de evaluación.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Tabla I-V | <5 puntos | 8 puntos | 11 puntos con $V_\text{oc}$ e $I_\text{sc}$ |
| Gráficas | una gráfica | dos gráficas | + identificación gráfica de MPP |
| Cálculo de eficiencia | sin valor | con valor numérico | + comparación con datasheet |
| Sombra y aplicación | una observación | medición con sombra | + cálculo del número de celdas para carga |
::/albatros
