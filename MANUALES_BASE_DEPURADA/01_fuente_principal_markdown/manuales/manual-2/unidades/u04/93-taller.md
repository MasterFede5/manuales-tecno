---
unidad: 4
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Termografía del cartucho de CO₂ del coche F1

Un taller de 60 minutos donde tu equipo F1 Albatros mide el enfriamiento del cartucho durante el disparo y caracteriza la "huella térmica" del coche para diseñar mejoras de gestión de calor. Aplica los subtemas 4.1 (calor vs T), 4.6 (transferencia de calor), 4.7 (calor latente) y 4.9 (teoría cinética y expansión adiabática).

::albatros{titulo="Taller — Mapa térmico del coche F1 antes y después de la carrera" tipo="experimento" tiempo="60 min"}
**Pregunta detonadora.** Cuando disparas el cartucho de CO₂, ¿cuántos grados se enfría su superficie? ¿Y por qué? ¿Qué nos dice eso sobre el proceso adiabático real dentro del cartucho?

**Lo que harás.** Medirás temperatura antes, durante y después del disparo del cartucho usando un termómetro infrarrojo (o cámara térmica si la tienes), y calcularás el calor latente perdido para validar la 1ª ley.

**Materiales.**
- Cartucho de CO₂ del coche F1 (al menos 2, idealmente 3).
- Coche F1 escolar montado y listo para disparo seguro.
- Termómetro infrarrojo de mano (precisión ±1 °C) o cámara térmica (MLX90640).
- Cronómetro.
- Báscula de cocina (1 g).
- Cinta aislante térmica reflejante (opcional).
- Hoja de registro y plantilla del coche para anotar temperaturas.
- Gafas de seguridad (obligatorias).

**Pasos.**

1. **Pesa los cartuchos.** Cada uno antes y después de uso. Anota $\Delta m$ (masa de CO₂ expulsada).

2. **Termografía inicial.** Mide temperatura de **5 puntos** del coche y del cartucho (cuerpo cartucho, boquilla, chasis delantero, chasis trasero, eje motriz). Usa una plantilla con esos 5 puntos marcados.

3. **Disparo controlado.** Activa el coche en una pista corta y segura. Recoge el coche al final.

4. **Termografía inmediata** (≤ 10 s tras el disparo). Repite las 5 lecturas en los mismos puntos.

5. **Termografía a 30 s** y a **2 min**. Documenta cómo se recupera la temperatura.

6. **Tabla térmica.** Construye:

   | Punto | $T_0$ (°C) | $T$ a 10 s (°C) | $T$ a 30 s (°C) | $T$ a 2 min (°C) | $\Delta T_\text{máx}$ (°C) |
   |---|---:|---:|---:|---:|---:|
   | Cuerpo cartucho | | | | | |
   | Boquilla | | | | | |
   | Chasis del. | | | | | |
   | Chasis tras. | | | | | |
   | Eje motriz | | | | | |

7. **Cálculo del calor cedido por el cartucho.** Asumiendo que el cartucho (acero, $c \approx 460$ J/kg·K, masa cartucho vacío ≈ 24 g) baja $|\Delta T_\text{cartucho}|$:
$$Q_\text{cartucho} = m_\text{cart} \cdot c_\text{acero} \cdot |\Delta T|$$

8. **Comparación con teoría adiabática.** Si la expansión fuera **isoentrópica ideal**, la temperatura del gas caería de 298 K a 233 K (–65 K). Compara con tu medición sobre la boquilla: ¿se acerca? Discute por qué no es exactamente lo mismo.

9. **Velocidad rms antes y después.** Con $T_1=298$ K y $T_2 = T_\text{boquilla}$ medida, calcula $v_\text{rms}$ del gas en cada estado: $v_\text{rms}=\sqrt{3RT/M}$, $M=44$ g/mol.

10. **Identifica fricción térmica.** ¿Algún punto se **calienta** (no enfría)? El eje motriz suele subir 2–5 °C por fricción de rodadura. Cuantifícalo.

11. **Repetibilidad.** Repite con un segundo cartucho. Compara: ¿la "firma térmica" es repetible?

12. **Diseño de mejora.** Cada equipo propone **una** intervención (cinta aislante en cuerpo del cartucho, mejor lubricación del eje, color de chasis para reducir radiación al sol antes de carrera) con predicción del cambio en $\Delta T$.

**Entregable.** Bitácora de 1.5 páginas con: tabla térmica, cálculo de $Q$ del cartucho, comparación con teoría adiabática, $v_\text{rms}$ antes y después, identificación del punto que más se calienta y propuesta de mejora.

**Rúbrica de evaluación.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Mapa térmico | 1 punto | 5 puntos antes/después | + 3 tiempos post-disparo |
| Cálculo de $Q$ | sin valor | con valor numérico | + verificación con teoría adiabática |
| Cálculo de $v_\text{rms}$ | sin fórmula | con valor antes y después | + cifras significativas y unidades |
| Propuesta de mejora | genérica | específica | con predicción cuantitativa de $\Delta T$ |
::/albatros
