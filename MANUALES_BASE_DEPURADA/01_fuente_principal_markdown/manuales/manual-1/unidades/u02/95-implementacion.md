---
unidad: 2
seccion: implementacion
paginas_objetivo: 4
---

::implementacion{titulo="Implementación Albatros — Sensor IoT de pH y conductividad para el bebedero"}
**Objetivo.** Construir un sistema autónomo basado en Arduino o ESP32 que mida pH y conductividad eléctrica del agua del bebedero **cada 30 segundos durante 24 horas**, transmita los datos a un dashboard web (Google Sheets, Thingspeak o Adafruit IO) y genere alertas si los valores salen de la NOM-127.

**¿Por qué hacerla?** Una sola medición de pH puede engañar (puede coincidir con un buen momento del día). Un sensor continuo te muestra **patrones**: si el pH baja al final de un día caluroso, si el cloro residual decae después de 6 horas sin uso, si la conductividad sube después de un mantenimiento. Construir el sensor te enseña **electrónica básica**, **protocolos IoT** y **química acuosa aplicada** al mismo tiempo.

---

### Materiales

- Microcontrolador ESP32 (≈ \$200 MXN) o Arduino UNO + módulo WiFi (≈ \$300).
- Sonda de pH analógica con módulo (≈ \$400) — buscar "pH Sensor Atlas Scientific" o equivalente DFRobot.
- Sonda de conductividad TDS (≈ \$200).
- Protoboard + jumpers + fuente de 5V.
- Soluciones buffer pH 4.0, 7.0 y 10.0 para calibración (≈ \$200).
- Cable micro-USB y computadora con Arduino IDE.
- Cuenta gratuita en Adafruit IO o Thingspeak.

### Pasos

**1. Cableado.**
```
ESP32:
  GPIO34 ← salida analógica del módulo pH
  GPIO35 ← salida analógica del módulo TDS
  3V3   → VCC de ambos módulos
  GND   → GND común
```

**2. Calibración del pH.** Sumerge la sonda en buffer 7.0 → ajusta offset; en buffer 4.0 → ajusta pendiente; en buffer 10.0 → verifica linealidad.

**3. Código Arduino (esqueleto).**
```cpp
#include <WiFi.h>
#include <HTTPClient.h>

const float pH_OFFSET = -0.18;     // ajuste por calibración
const float pH_SLOPE  = 5.70;      // pendiente medida
const int   READ_PERIOD = 30000;   // ms

void setup() {
  Serial.begin(115200);
  WiFi.begin("MI_RED", "MI_PASS");
  while (WiFi.status() != WL_CONNECTED) delay(500);
}

void loop() {
  float pH = pH_SLOPE * (analogRead(34) / 4095.0 * 3.3) + pH_OFFSET;
  float tds = analogRead(35) / 4095.0 * 1000;
  enviarAdafruitIO(pH, tds);
  delay(READ_PERIOD);
}
```

**4. Dashboard.** Configura un feed en Adafruit IO con dos campos (pH y TDS). El ESP32 publica cada 30 s. Crea un dashboard con dos gráficas en tiempo real y un panel de alertas.

**5. Reglas de alerta.**
- pH < 6.5 o pH > 8.5 → alerta amarilla.
- pH < 6.0 o pH > 9.0 → alerta roja (cierre inmediato).
- TDS > 1000 mg/L → alerta amarilla.
- TDS > 1500 mg/L → alerta roja.

**6. Período de monitoreo.** 24 h continuas. Después analiza:
- Variación diurna del pH (¿sube o baja con el calor?).
- Estabilidad del TDS.
- Eventos anómalos (¿llenado de cisterna a las 4 a.m.?).

::visual{tipo="interfaz" descripcion="Captura del dashboard final en Adafruit IO mostrando dos gráficas en tiempo real (pH y TDS) con datos de 24 horas, con líneas horizontales que marcan los límites de la NOM-127, y un panel lateral con estadísticas (media, máximo, mínimo) y alertas activas." paginas=0.5}

---

### Entregable

Un reporte técnico de 4-6 páginas con:
1. Hardware utilizado (lista y diagrama).
2. Código del firmware (subido a GitHub público).
3. Calibración (gráfica y ecuación de regresión).
4. Datos de 24 horas (gráficas + tabla con eventos relevantes).
5. Diagnóstico (¿el bebedero cumple la NOM-127 a lo largo del día?).
6. Recomendaciones operativas para la directora.

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| **Cableado y montaje** | sin foto del montaje | foto + funcionamiento básico | foto + diagrama Fritzing + buenas prácticas (resistencias pull-up, blindaje) |
| **Calibración** | sin calibrar | calibrado con 2 buffers | con 3 buffers + cálculo de error de la curva |
| **Datos** | menos de 6 horas | 24 horas continuas | 24 horas + análisis estadístico |
| **Análisis** | descripción superficial | identifica patrones | propone causas físico-químicas con base en U2 |
| **Recomendaciones** | sin recomendaciones | sugiere mejoras | plan operativo concreto con costos |

### Reto bonus (+1 punto)

Agrega un tercer sensor (turbidez óptica o cloro residual con sensor electroquímico) para cubrir 3 parámetros simultáneos. Conecta también un actuador (LED RGB o pequeña bocina) que emita una alerta visual/sonora local cuando un parámetro salga de norma.

---

### Hitos intermedios

| Sprint | Entregable | Día |
|---|---|---|
| 1 | Cableado en protoboard + lectura de pH en monitor serie | 3 |
| 2 | Calibración de pH con 3 buffers + ecuación de regresión documentada | 6 |
| 3 | Conexión WiFi + publicación en Adafruit IO con datos cada 30 s | 10 |
| 4 | Dashboard con alertas y reporte de 24 h de datos reales | 15 |

### Reto bonus extendido (+2 puntos cada uno)

1. **Reto A:** integra una pantalla OLED al ESP32 que muestre, sin necesidad de WiFi, los valores en vivo y el código de color de norma (verde/amarillo/rojo).
2. **Reto B:** programa una rutina que envíe un correo (vía IFTTT o webhook) a la dirección escolar cuando se dispare una alerta roja, con captura del último minuto de datos.
3. **Reto C:** entrena un modelo simple en Google Sheets (regresión lineal o clasificación por umbral) que prediga el pH 30 min adelante con base en los últimos 10 datos. Publica el cálculo y compáralo con la medición real.
::/implementacion

---

::albatros{titulo="Sprint corto — auditoría diaria firmada del bebedero" tipo="reto" tiempo="30 min"}
**Pregunta detonadora.** ¿Puedes diseñar un protocolo de 30 min que un alumno de servicio social ejecute cada lunes para certificar el bebedero ante la dirección?

**Lo que harás.**
1. Diseña una hoja de auditoría A4 con 5 parámetros (pH, dureza, cloro, turbidez visual, temperatura).
2. Define para cada parámetro: instrumento, rango aceptable (NOM-127), acción correctiva.
3. Toma una medición real del bebedero, llena la hoja y firma como auditor.
4. Documenta con foto y archiva en una carpeta de seguimiento.
5. Compara los datos de tres semanas para detectar tendencias.

**Materiales.** Hoja A4 con plantilla · tira de pH · kit DPD · termómetro · cronómetro · tu bitácora de la U0.

**Entregable.** Hoja firmada + foto del bebedero + 3 lecturas semanales tabuladas.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Plantilla | desordenada | 5 parámetros con rango | 5 parámetros + acción correctiva por cada uno |
| Repeticiones | 1 lectura | 1 semana | 3 semanas con tendencia |
| Cierre | sin firma | firma de auditor | firma + recomendación a dirección |
::/albatros
