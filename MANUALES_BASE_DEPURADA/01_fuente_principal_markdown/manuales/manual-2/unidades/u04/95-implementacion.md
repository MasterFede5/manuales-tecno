---
unidad: 4
seccion: implementacion
paginas_objetivo: 2
---

::implementacion{titulo="Implementación Albatros — Cámara térmica con sensor MLX90640 + diagnóstico de aislamiento"}
**Objetivo.** Construir una cámara térmica de bajo costo con un sensor MLX90640 (matriz 32×24 píxeles infrarrojos) conectado a Arduino o ESP32, y usarla para mapear el desempeño térmico de tu casa, escuela o coche. Identificar zonas de pérdida de calor y proponer mejoras de aislamiento.

**¿Por qué hacerla?** Las cámaras térmicas profesionales cuestan miles de pesos, pero un sensor MLX90640 cuesta ~\$700-1500 MXN. Con un microcontrolador y una pantalla, construyes un instrumento de diagnóstico térmico que te da datos cuantitativos. Es ingeniería térmica aplicada en miniatura.

---

### Materiales

- ESP32 o Arduino Mega (≈ \$200-400).
- Sensor MLX90640 (matriz IR 32×24).
- Pantalla TFT 2.8" o superior (≈ \$300).
- Protoboard, jumpers.
- (Opcional) batería USB para portabilidad.

### Pasos

**1. Conexión y librería.** Conecta el sensor por I²C (SDA, SCL, VCC, GND). Instala librerías: `Adafruit_MLX90640`.

**2. Mapa térmico básico.** El código lee 768 píxeles cada ~4 Hz, los grafica con paleta de colores (azul-rojo).

**3. Calibración.** Apunta a una superficie de temperatura conocida (cubo de hielo, taza de agua hervida) para verificar lectura.

**4. Inspección.** Recorre tu casa o escuela buscando:
- Ventanas con marcos fríos (mal sellado).
- Tomas eléctricas con paredes frías (puentes térmicos).
- Refrigerador con motor caliente.
- Tu cuerpo (debe verse como mancha brillante a 33 °C).
- Llantas del coche tras manejar.

**5. Cuantificación de pérdidas.**
   - Si una ventana está a 5 °C en invierno y la pared a 20 °C, hay un puente térmico.
   - Mide área y calcula tasa de pérdida usando $\dot{Q} = h A \Delta T$.

**6. Recomendaciones.** Para cada problema detectado, proponer mejora de aislamiento (selladores, doble vidrio, aislamiento térmico).

::visual{tipo="interfaz" descripcion="Captura de pantalla de la cámara térmica casera mostrando una imagen 32x24 píxeles con paleta azul-rojo, una persona iluminando una pared con su silueta caliente. Anexo con valores numéricos de temperaturas medidas, regla con escala térmica, y panel lateral identificando 'puentes térmicos' (zonas frías inesperadas)." paginas=0.5}

---

### Entregable

Reporte de 2-4 páginas con:
1. Foto del setup y diagrama de conexión.
2. Captura de funcionamiento.
3. 5+ inspecciones distintas con interpretación.
4. Cálculo de pérdidas térmicas en al menos un caso.
5. Recomendaciones cuantificadas (potencial de ahorro energético).

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Implementación** | sin funcionamiento | imágenes térmicas básicas | con calibración y precisión |
| **Inspecciones** | <3 | 5 inspecciones | con cuantificación |
| **Análisis** | qualitativo | identifica problemas | propone soluciones con ahorro estimado |

### Reto bonus (+1 punto)

Configura la cámara para alertas automáticas: si detecta una zona >50 °C, suena una alarma. Útil para detectar sobrecalentamiento de equipos.

---

### Hitos intermedios

| Sprint | Semana | Meta concreta | Evidencia |
|---|---|---|---|
| 1. Hardware | 1 | Sensor MLX90640 leyendo y mostrando 32×24 píxeles en pantalla | foto + video 10 s |
| 2. Calibración | 2 | Lecturas verificadas con 3 referencias (hielo, ambiente, agua hervida) | tabla de calibración |
| 3. Inspección | 3 | 5 escenas térmicas distintas con interpretación cuantitativa | reporte parcial 2 pp |
| 4. Diagnóstico y reporte | 4 | Recomendaciones cuantificadas con potencial de ahorro | reporte final 4 pp |

### Reto bonus extendido (+2 puntos cada uno)

1. **Cámara térmica del coche F1.** Filma el coche desde 1 m de distancia justo después de un disparo de CO₂ y documenta el enfriamiento del cartucho frame por frame durante 30 s. Calcula el coeficiente de transferencia $h$ entre cartucho y aire.
2. **Mapa térmico georreferenciado.** Conecta el ESP32 a un GPS (módulo NEO-6M) y registra las inspecciones con coordenadas. Genera un mapa interactivo (Leaflet) con la huella térmica de tu escuela.
3. **Comparación con la teoría adiabática.** Mide $T$ del cartucho a 0, 5, 15, 30 y 60 s tras el disparo. Ajusta una exponencial $T(t) = T_\infty + (T_0 - T_\infty)e^{-t/\tau}$ y deduce la constante térmica $\tau$. Compara con el cálculo $\tau = mc/(hA)$.
::/implementacion

---

::albatros{titulo="Caso integrador — coche F1 sin sobrecalentar" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Tras 3 carreras seguidas, ¿cuánto sube la temperatura del eje motriz del coche F1 si la fricción disipa 1.0 J por carrera y no hay enfriamiento entre ellas?

**Lo que harás.**
1. Toma datos: $m_\text{eje} = 25$ g, $c_\text{acero} = 460$ J/(kg·K), 3 carreras, energía disipada por carrera $E_d = 1.0$ J.
2. Aplica $\Delta T = E_\text{total}/(m c)$ asumiendo todo el calor permanece en el eje (sin pérdidas al aire entre carreras).
3. Repite el cálculo asumiendo que entre carreras se cede 30 % del calor al aire (modelo realista).
4. Compara los dos resultados.
5. Si la balsa se deforma a 60 °C y el eje arranca a 25 °C, ¿cuántas carreras consecutivas tolera el coche bajo cada modelo?

**Entregable.** Hoja con cálculos paso a paso y tabla con: $\Delta T$ por carrera (modelo aislado y modelo realista), número máximo de carreras tolerables, recomendación operativa.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cálculo modelo aislado | sin valor | con valor numérico | + cifras significativas |
| Cálculo modelo realista | ausente | con valor numérico | + comparación |
| Recomendación operativa | genérica | con número de carreras | con criterio cuantitativo |
::/albatros
