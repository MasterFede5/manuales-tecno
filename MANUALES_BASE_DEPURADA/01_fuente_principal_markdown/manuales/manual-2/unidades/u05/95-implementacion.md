---
unidad: 5
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Análisis espectral del sonido del coche con Audacity"}
**Objetivo.** Grabar el sonido del coche F1 en operación, importarlo a **Audacity** (gratuito) y analizar su espectro de frecuencias para identificar las componentes dominantes y compararlas con la teoría.

**¿Por qué hacerla?** Muchas veces, el "sonido" parece amorfo, pero al analizarlo en frecuencias revelas estructura interna: notas dominantes, ruido de fondo, armónicos. Es la base del análisis espectral usado en ingeniería acústica, telecomunicaciones, música y diagnóstico mecánico.

---

### Materiales

- Computadora con Audacity (descarga gratuita).
- Smartphone para grabar.
- Coche F1 funcionando (o cualquier objeto con sonido característico).
- Cuaderno para notas.

### Pasos

**1. Graba el sonido.** Pon el celular cerca del coche. Activa la grabadora. Lanza el coche. Detén la grabación.

**2. Importa a Audacity.** Abre el archivo. Visualiza la forma de onda.

**3. Espectro de Fourier.** Selecciona un fragmento (~1 s del cartucho activo). Menú Analyze → Plot Spectrum. Aparece la distribución de energía por frecuencia.

**4. Identifica las componentes.**
   - Pico fundamental (frecuencia principal): ~3-8 kHz para el silbido del CO₂.
   - Armónicos: múltiplos enteros del fundamental.
   - Ruido blanco/rosa de fondo (chasis, llantas).

**5. Compara con teoría.** ¿La frecuencia principal coincide con la longitud de onda esperada por la geometría de la boquilla?

**6. Doppler experimental.** Graba el coche pasando frente al micrófono y compara el espectro antes vs después del paso. Verás corrimiento de frecuencia.

::visual{tipo="interfaz" descripcion="Captura de Audacity con tres paneles: arriba forma de onda completa del sonido del coche, centro selección de un fragmento de 1 segundo, abajo espectro de Fourier mostrando un pico dominante a ~5 kHz con armónicos secundarios y ruido de fondo. Anotaciones identificando cada componente." paginas=0.5}

---

### Entregable

Documento con:
1. Captura del audio crudo y del espectro.
2. Identificación de la frecuencia fundamental.
3. Verificación de Doppler (si el coche pasó por el micrófono).
4. Recomendaciones para reducir ruido o mejorar acústica.

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Grabación** | distorsionada | clara | múltiples ensayos |
| **Análisis espectral** | sin gráfica | espectro mostrado | componentes identificadas |
| **Conexión teoría** | sin comparar | observación cualitativa | con frecuencias predichas |

### Reto bonus (+1 punto)

Compara el espectro del coche con el de otros objetos: tu voz, una guitarra, un silbato. Discute las diferencias en términos de armónicos y timbres.

---

### Hitos intermedios

| Sprint | Semana | Meta concreta | Evidencia |
|---|---|---|---|
| 1. Audio limpio | 1 | Grabación a SNR alto del paso del coche | archivo .wav 5 s |
| 2. FFT y firma | 2 | Espectro con pico fundamental e identificación de armónicos | captura de Audacity |
| 3. Doppler | 3 | $f_+$, $f_-$ medidas con dos celulares y velocidad deducida | tabla 3 corridas |
| 4. Reporte | 4 | Reporte con propuesta de modificación acústica del cartucho | reporte 4 pp |

### Reto bonus extendido (+2 puntos cada uno)

1. **Identificación de defectos.** Toma 3 cartuchos: uno nuevo, uno con boquilla parcialmente obstruida, uno con boquilla deformada. Compara los tres espectros y describe cómo cada defecto cambia la firma acústica. Construye una tabla de "diagnóstico por sonido".
2. **Filtro digital.** Usa el filtro pasa-bajos de Audacity para silenciar el silbido por encima de 6 kHz. Reproduce el resultado y discute qué se pierde y qué se gana.
3. **Sonograma temporal.** Genera un espectrograma 2D (Analyze → Spectrogram) del paso del coche. Identifica la **rampa Doppler**: cómo la frecuencia baja gradualmente al pasar. Mide la pendiente de la rampa.
::/implementacion

---

::albatros{titulo="Caso integrador — el coche que silba demasiado fuerte" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Tu coche F1 mide 95 dB a 1 m del cartucho. La normativa escolar limita la exposición a 85 dB para el público a 4 m. ¿Cumple? Si no, ¿cuántos dB necesitas reducir y cómo?

**Lo que harás.**
1. Calcula la intensidad a 1 m: $I_1 = I_0 \cdot 10^{\beta_1/10}$.
2. Aplica la ley del cuadrado inverso para hallar $I_4$ a 4 m: $I_4 = I_1 (1/4)^2$.
3. Calcula $\beta_4 = 10\log(I_4/I_0)$.
4. Compara con el límite de 85 dB. ¿Por cuántos dB falta?
5. Calcula el factor de reducción de intensidad necesario y propón **tres** estrategias (barrera acústica, espuma absorbente, distancia adicional) con su efecto cuantitativo estimado.

**Entregable.** Hoja con cálculos paso a paso y tabla con: $\beta_1$, $\beta_4$, déficit en dB, tres estrategias con reducción esperada.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cálculo de $\beta_4$ | sin valor | con valor numérico | + cifras significativas |
| Comparación con normativa | ausente | identifica déficit | + valor en dB |
| Tres estrategias | genéricas | específicas | con reducción cuantitativa estimada |
::/albatros
