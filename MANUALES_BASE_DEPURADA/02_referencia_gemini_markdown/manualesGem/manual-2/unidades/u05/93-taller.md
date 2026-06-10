---
unidad: 5
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Espectro Doppler y huella acústica del coche F1

Un taller de 60 minutos donde tu equipo F1 Albatros graba con dos micrófonos sincronizados el paso del coche, mide el corrimiento Doppler real, deduce la velocidad del coche solo con audio y caracteriza la "firma sonora" del cartucho. Aplica los subtemas 5.2 (parámetros de onda), 5.5 (intensidad) y 5.6 (Doppler).

::albatros{titulo="Taller — Velocímetro acústico Doppler con dos celulares" tipo="experimento" tiempo="60 min"}
**Pregunta detonadora.** ¿Puedes deducir la velocidad de tu coche F1 sin usar cronómetro ni cinta métrica, **solo con el audio del paso**? ¿Y qué tan precisa es la medición comparada con un cronómetro tradicional?

**Lo que harás.** Grabarás el paso del coche con dos celulares colocados en la pista; aplicarás FFT en Audacity para extraer la frecuencia antes y después del paso; despejarás la velocidad del Doppler bidireccional.

**Materiales.**
- Coche F1 escolar funcional con cartucho.
- 2 smartphones con grabadora (idealmente con app **Phyphox** o **Audacity for Android**).
- 1 laptop con **Audacity** instalado.
- Cinta métrica (10 m).
- Cinta adhesiva, marcadores.
- Cronómetro adicional para validar.
- Hoja de registro con plantilla de tabla.

**Pasos.**

1. **Setup.** Coloquen el coche en la salida. A 8 m, instalen el celular A justo en la línea de paso, lateral. A 2 m del A, otro celular B en línea. Ambos a la misma altura (~1 m).

2. **Sincronicen.** Pongan ambos celulares a grabar simultáneamente. Den una palmada fuerte para tener un marcador audible común que después permita alinear los audios en Audacity.

3. **Lancen el coche.** Anoten el momento exacto del disparo. Permitan que cruce la zona de los dos micrófonos.

4. **Recojan el coche** y detengan ambas grabaciones.

5. **Importen a Audacity.** Carguen el audio del celular A en pista 1 y el del B en pista 2. Alineen usando la palmada de sincronización.

6. **Identifiquen el silbido del cartucho.** En el celular A (más alejado de la salida), el coche **se acerca** durante una porción del audio (frecuencia más alta) y **se aleja** después de pasar (frecuencia más baja).

7. **Recorten dos fragmentos de 0.3 s cada uno** del celular A: uno **antes** de pasar (acercándose) y uno **después** de pasar (alejándose). Apliquen Analyze → Plot Spectrum (FFT) y registren la frecuencia pico $f_+$ y $f_-$.

8. **Calculen la velocidad por Doppler.**
   $$f_+ = f_0 \frac{v_s}{v_s - v}, \quad f_- = f_0 \frac{v_s}{v_s + v}$$
   Dividiendo: $\frac{f_+}{f_-} = \frac{v_s + v}{v_s - v}$ → despejen $v$.
   $$v = v_s \cdot \frac{f_+ - f_-}{f_+ + f_-}$$
   Con $v_s = 343$ m/s a 20 °C (corrijan si la temperatura ambiente difiere mucho).

9. **Calculen también la frecuencia emitida $f_0$** como media geométrica $f_0 = \sqrt{f_+ \cdot f_-}$.

10. **Validación con cronómetro.** Calculen la velocidad como $v_\text{cron} = 2/t_{AB}$, donde $t_{AB}$ es el tiempo entre el pico de amplitud del audio en celular A y el pico en celular B (separación 2 m). Comparen $v_\text{Doppler}$ vs $v_\text{cron}$.

11. **Tabla resumen.**

    | Corrida | $f_+$ (Hz) | $f_-$ (Hz) | $f_0$ (Hz) | $v_\text{Doppler}$ (m/s) | $v_\text{cron}$ (m/s) | Error % |
    |---:|---:|---:|---:|---:|---:|---:|
    | 1 | | | | | | |
    | 2 | | | | | | |
    | 3 | | | | | | |

12. **Análisis y mejora.** Discutan: ¿de qué orden son los errores? ¿Qué los causa (ruido de fondo, FFT con ventana corta, ángulo de paso)? Propongan una mejora del setup (mayor separación, micrófono más sensible, ventana de FFT más larga).

**Entregable.** Bitácora de 1.5 páginas con: capturas de los espectros (antes y después), tabla de 3 corridas con velocidades por dos métodos, error porcentual, propuesta de mejora.

**Rúbrica de evaluación.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Grabación y sincronización | un solo audio | dos audios sincronizados | + 3 corridas |
| Análisis FFT | espectro mostrado | $f_+$ y $f_-$ identificadas | + valor de $f_0$ con media geométrica |
| Cálculo de $v$ | sin valor | $v_\text{Doppler}$ con unidades | + comparación con $v_\text{cron}$ y error |
| Discusión y mejora | genérica | identifica fuente de error | + propuesta cuantitativa de mejora |
::/albatros
