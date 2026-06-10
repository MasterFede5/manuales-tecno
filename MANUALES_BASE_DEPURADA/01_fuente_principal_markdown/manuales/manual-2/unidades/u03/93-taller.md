---
unidad: 3
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Eficiencia energética del coche F1 con rampa y telemetría

Un taller de 60 minutos donde tu equipo F1 Albatros aplica conservación de energía a una rampa real para medir las pérdidas por fricción y validar el balance energético del coche. Aplica los subtemas 3.3 (Ek), 3.4 (Ug), 3.5 (conservación) y 3.8 (fricción).

::albatros{titulo="Taller — Cuánta energía pierde tu coche en cada metro" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** Si dejas caer tu coche F1 (sin cartucho) por una rampa y mides su velocidad al final, ¿esa velocidad coincide con $\sqrt{2gh}$? Si no, ¿adónde se fue la energía que falta?

**Lo que harás.** Construirás una rampa de altura variable, soltarás el coche desde 5 alturas distintas, medirás la velocidad al pie de la rampa y al final de un tramo plano, y calcularás dos cosas: (1) eficiencia rampa→inicio del plano (mide el rozamiento de la rampa), (2) eficiencia inicio→final del plano (mide la rodadura horizontal).

**Materiales.**
- Coche F1 escolar (sin cartucho).
- Tabla rígida de 1.2 m para la rampa.
- Bloques o libros para variar la altura (5 valores: 5, 10, 15, 20, 25 cm).
- Cinta métrica.
- Smartphone con cámara a 60 fps + app Phyphox (o Tracker en compu).
- Cinta adhesiva de color para marcar.
- Báscula de cocina (1 g).

**Pasos.**

1. **Pesa.** Mide la masa $m$ del coche con báscula. Anótala con incertidumbre ±0.5 g.

2. **Marca posiciones.** Pon una cinta justo al pie de la rampa (posición A) y otra a 1.0 m de A sobre el plano (posición B).

3. **Configuración 1: rampa a 10 cm.** Coloca el coche en lo alto de la rampa. Mide la altura $h$ del centro del coche con cinta. Suéltalo sin empujar.

4. **Filma de lado.** Encuadre que cubra A y B. 60 fps, idealmente.

5. **Repite 3 veces.** Promedia para reducir error humano.

6. **Mide velocidades por video.** En Phyphox o Tracker, calcula:
   - $v_A$: velocidad al cruzar A (al pie de la rampa).
   - $v_B$: velocidad al cruzar B (1 m después).
   Trackea 3 frames antes y después de cada marca para sacar pendiente x-t local.

7. **Calcula energías.**
   - $E_0 = m g h$ (energía al inicio, en reposo arriba).
   - $E_A = \tfrac{1}{2} m v_A^2$.
   - $E_B = \tfrac{1}{2} m v_B^2$.

8. **Eficiencia de la rampa.** $\eta_\text{rampa} = E_A / E_0$. Calcula el coeficiente equivalente $\mu_\text{rampa}$ de $W_\text{fric} = \mu m g \cos\theta \cdot L$, con $L$ = longitud de la rampa.

9. **Pérdidas en el plano.** $\Delta E = E_A - E_B$. Asumiendo que es solo rodadura: $\mu_r = \Delta E / (m g \cdot 1.0)$.

10. **Repite con 5 alturas.** Construye la tabla:

    | h (cm) | $E_0$ (J) | $v_A$ (m/s) | $E_A$ (J) | $v_B$ (m/s) | $E_B$ (J) | $\eta_\text{rampa}$ | $\mu_r$ |
    |---:|---:|---:|---:|---:|---:|---:|---:|
    | 5 | | | | | | | |
    | 10 | | | | | | | |
    | 15 | | | | | | | |
    | 20 | | | | | | | |
    | 25 | | | | | | | |

11. **Gráfica $v_A^2$ vs $h$.** Si la rampa fuera ideal sin fricción, debería ser una línea $v_A^2 = 2gh$ (pendiente 19.6). Compara la pendiente real vs la ideal y deduce el porcentaje de pérdida.

12. **Diagnóstico de mejora.** Cada equipo identifica si pierde más en la rampa (alineación, rozamiento de las llantas) o en el plano (rodadura) y propone **una** modificación con predicción cuantitativa.

**Entregable.** Bitácora de 1.5 páginas con: tabla con 5 alturas, dos gráficas ($v_A^2$ vs $h$ y $\Delta E$ vs $h$), valores de $\mu_\text{rampa}$ y $\mu_r$, propuesta de mejora numérica.

**Rúbrica de evaluación.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Mediciones | 2 alturas | 5 alturas con 3 corridas | + incertidumbre estadística |
| Cálculo de eficiencias | sin valores | $\eta$ y $\mu$ con números | + cifras significativas y unidades |
| Gráficas | una gráfica | dos gráficas con ejes correctos | + regresión lineal y desviaciones |
| Propuesta de mejora | sin valor numérico | con valor cualitativo | con predicción cuantitativa |
::/albatros
