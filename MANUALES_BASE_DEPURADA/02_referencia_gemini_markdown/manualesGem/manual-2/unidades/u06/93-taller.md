---
unidad: 6
seccion: taller
paginas_objetivo: 2
---

## Taller práctico — Telemetría inalámbrica del coche F1 con ESP32

Un taller de 60 minutos donde tu equipo F1 Albatros monta un circuito de telemetría real con un ESP32, un sensor IR y un LED indicador, mide consumos con un multímetro y caracteriza la transmisión Wi-Fi al banco. Aplica los subtemas 6.2 (Ohm, circuitos), 6.4 (inducción) y 6.6 (luz/EM).

::albatros{titulo="Taller — Sistema eléctrico y enlace de radio del coche F1" tipo="taller" tiempo="60 min"}
**Pregunta detonadora.** ¿Qué corriente real consume tu coche F1 con sensores y radio activos? ¿Cuántas horas dura tu batería LiPo de 1 200 mAh? ¿Cuántos metros llega la señal Wi-Fi sin pérdida grave?

**Lo que harás.** Montarás un circuito de prueba con ESP32, sensor IR y LED indicador. Medirás voltajes y corrientes con un multímetro, calcularás autonomía y potencia, y caracterizarás el alcance de la señal Wi-Fi midiendo la potencia recibida (RSSI) en función de la distancia.

**Materiales.**
- ESP32 DevKit V1 (o cualquier compatible Wi-Fi).
- Sensor IR de línea (TCRT5000 o similar) o sensor ultrasónico HC-SR04.
- LED rojo + resistencia 220 Ω.
- Batería LiPo 1S 3.7 V·1 200 mAh (o protoboard con cable USB).
- Multímetro digital (rango mA y V).
- Protoboard, jumpers macho-macho.
- Smartphone con app **Wi-Fi Analyzer** (Android) o **AirPort Utility** (iOS) para medir RSSI.
- Cinta métrica.

**Pasos.**

1. **Esquemático.** Dibujen el circuito en papel: VCC del ESP32 → batería; sensor IR → 3.3 V y GND, salida a un GPIO; LED → GPIO con resistencia en serie a GND.

2. **Cálculo de la resistencia del LED.** $R = (V_\text{GPIO} - V_\text{LED})/I_\text{LED}$. Con $V_\text{GPIO}=3.3$ V, $V_\text{LED}=2.0$ V (rojo), $I_\text{LED}=10$ mA:
$$R = (3.3 - 2.0)/0.010 = 130\,\Omega$$
Como no hay 130 exactos, usen 220 Ω (más segura, baja la corriente a ~6 mA, brillo aceptable).

3. **Montaje.** Armen en protoboard. Carguen un sketch que parpadee el LED a 2 Hz y publique la lectura del IR por Wi-Fi.

4. **Mediciones de voltaje.** Con multímetro en modo voltímetro, midan: $V_\text{batería}$, $V_\text{VCC ESP32}$, $V_\text{LED activo}$. Verifiquen Kirchhoff de voltajes en la malla del LED.

5. **Mediciones de corriente.** Pongan el multímetro **en serie** entre la batería y el VCC del ESP32. Anoten la corriente total $I_t$ en tres modos:
   - Modo idle (sin Wi-Fi).
   - Modo conectado pero sin transmitir.
   - Modo transmitiendo (5 transmisiones por segundo).

6. **Tabla de consumos.**

   | Modo | $I_t$ (mA) | $P = V\cdot I$ (W) | Autonomía (h) = 1.2/$I_t$(A) |
   |---|---:|---:|---:|
   | Idle | | | |
   | Conectado | | | |
   | Transmitiendo | | | |

7. **Caracterización del enlace Wi-Fi.** Con el ESP32 anunciando un SSID propio o publicando datos a un servidor en el laptop, midan el RSSI (potencia recibida en dBm) a las distancias **1, 3, 6, 10, 15 y 20 m** dentro del salón.

8. **Tabla de RSSI vs distancia.**

   | $d$ (m) | RSSI (dBm) | Pérdida vs 1 m (dB) |
   |---:|---:|---:|
   | 1 | | 0 (referencia) |
   | 3 | | |
   | 6 | | |
   | 10 | | |
   | 15 | | |
   | 20 | | |

9. **Comparación con teoría.** En espacio libre, la pérdida varía como $20\log(d/d_0)$. Calculen la pérdida teórica esperada y comparen con la medida (en interior la pérdida es mayor por paredes y reflexiones).

10. **Determinen el alcance útil.** El umbral de funcionamiento típico es −80 dBm. ¿A qué distancia están en el límite?

11. **Diagnóstico.** ¿Cuál es el cuello de botella del coche F1: la corriente o el alcance? Recomienden una mejora cuantitativa (batería 2 000 mAh, antena externa, modo deep-sleep entre transmisiones).

12. **Cierre.** Entreguen el reporte con los hallazgos.

**Entregable.** Bitácora de 1.5 páginas con: esquemático del circuito, cálculo de la R del LED, tabla de consumos, tabla de RSSI con gráfica RSSI vs $\log d$, alcance útil, recomendación cuantitativa.

**Rúbrica de evaluación.**

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cálculo de R del LED | sin valor | con valor numérico | + verificación experimental |
| Tabla de consumos | un modo | tres modos con $I$ y $P$ | + autonomía calculada para cada modo |
| Tabla de RSSI | <3 puntos | 6 puntos con gráfica | + comparación con teoría $20\log d$ |
| Recomendación | genérica | específica | con predicción cuantitativa de mejora |
::/albatros
