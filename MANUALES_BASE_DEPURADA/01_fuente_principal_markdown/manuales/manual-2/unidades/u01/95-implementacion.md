---
unidad: 1
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Análisis de video del coche F1 con Tracker"}
**Objetivo.** Usar el software gratuito **Tracker** para analizar un video real (filmado por ti) del prototipo de coche F1 en pista. Extraer posición, velocidad y aceleración instantáneas a partir del video, generar las gráficas x-t, v-t, a-t, y comparar con un modelo teórico de cinemática.

**¿Por qué hacerla?** Tracker convierte tu celular en un instrumento de telemetría profesional. Filmas el coche, marcas su posición frame por frame, y obtienes datos cuantitativos de calidad de laboratorio. Es la mejor manera de validar predicciones cinemáticas reales.

---

### Materiales

- Computadora con Tracker (gratuito, multiplataforma).
- Smartphone para filmar (60 fps preferiblemente).
- Cinta métrica para calibrar la escala del video.
- Coche F1 (o cualquier objeto en movimiento: pelota, carrito, bicicleta).
- Pista o trayecto de al menos 10 m con buena iluminación.

### Pasos

**1. Filma el movimiento.** Cámara perpendicular al plano de movimiento, distancia ~3 m, encuadre cubre toda la trayectoria. Coloca una regla o cinta visible para calibración.

**2. Importa a Tracker.** Abre el video en Tracker. Define el origen y los ejes (clic izquierdo en el origen, arrastra para alinear ejes con la pista).

**3. Calibra la escala.** Marca la cinta visible en el video; di a Tracker su longitud real. Esto convierte píxeles a metros.

**4. Marca el objeto.** Crea un "Point Mass" y marca la posición del coche en cada frame (puedes saltar 2-3 frames si la velocidad es alta).

**5. Genera datos automáticamente.** Tracker calcula posición, velocidad y aceleración instantáneas mediante derivación numérica. Las gráficas x-t, v-t, a-t aparecen en tiempo real.

**6. Exporta a Excel.** Guarda los datos como CSV y abre en Excel/Sheets para análisis estadístico.

**7. Compara con teoría.** Modela el movimiento como MRUA con la aceleración medida. Calcula tiempo total predicho. Compara con tiempo real.

**8. Identifica desviaciones.** ¿Hay regiones donde el modelo MRUA falla? ¿Ahí pasa qué? (fricción cambiante, vibraciones, etc.)

::visual{tipo="interfaz" descripcion="Captura del software Tracker mostrando: lado izquierdo el video del coche F1 con marcadores de posición en cada frame y vectores velocidad/aceleración superpuestos; lado derecho tres gráficas en tiempo real (x-t parabólica, v-t recta, a-t aproximadamente constante); abajo tabla con datos numéricos exportables. Color azul Albatros." paginas=0.5}

---

### Entregable

Documento de 2-4 páginas con:
1. Foto del setup experimental.
2. Captura de Tracker con video y datos.
3. Gráficas x-t, v-t, a-t.
4. Aceleración medida (con incertidumbre).
5. Comparación con predicción teórica del modelo cinemático.
6. Discusión de errores y mejoras al diseño.

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Calidad del video** | borroso o mal encuadre | clara y calibrable | 60+ fps, calibración con escala visible |
| **Análisis con Tracker** | <10 puntos marcados | >30 puntos en trayectoria completa | datos exportados con gráficas |
| **Comparación teoría-experimento** | sin comparación | qualitativa | cuantitativa con error porcentual |
| **Identificación de mejoras** | sin propuestas | 1-2 mejoras | 3+ basadas en datos |

### Reto bonus (+1 punto)

Filma 3 corridas del coche con **distintas configuraciones** (con/sin alerón, con/sin carga adicional, en distintas pistas) y compara cinemática. Identifica el mejor diseño con base en aceleración promedio.

---

### Hitos intermedios

| Sprint | Semana | Meta concreta | Evidencia |
|---|---|---|---|
| 1. Setup | 1 | Tracker instalado, pista filmada con calibración visible | foto del setup + video de prueba 5 s |
| 2. Datos crudos | 2 | 30+ puntos marcados en Tracker para 1 corrida | captura de pantalla con marcadores |
| 3. Análisis | 3 | Gráficas x-t, v-t, a-t exportadas + aceleración promedio numérica | hoja Excel con datos y gráficas |
| 4. Comparación y mejora | 4 | Comparación cuantitativa con modelo MRUA + 3 propuestas justificadas | reporte final 2-4 pp |

### Reto bonus extendido (+2 puntos cada uno)

1. **Telemetría con sensores reales.** Monta un acelerómetro Arduino (MPU-6050) sobre el chasis del coche, registra la aceleración a 100 Hz durante la corrida y compara la curva $a(t)$ del sensor con la $a(t)$ deducida del video con Tracker.
2. **Modelado por tramos.** Ajusta dos modelos diferentes (MRUA + MRU) por tramo, encuentra el instante exacto en que termina la fase de empuje del CO₂ y reporta la aceleración pico.
3. **Optimización dirigida.** Usando los datos de tres corridas con masas distintas (45 g, 60 g, 80 g), grafica $a$ promedio vs masa y verifica si sigue $a = F/m$ (anticipo de la 2ª ley de Newton, unidad 2).
::/implementacion

---

::albatros{titulo="Caso integrador — el podio que se decide por décimas" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Tu equipo y el rival cruzan la meta separados por 0.12 s. ¿En qué fase del recorrido se decidió la carrera?

**Lo que harás.**
1. Recibirás dos sets de datos (proporcionados por el docente o generados con Tracker) de las gráficas x-t de tu coche y del rival.
2. Calcula la velocidad media por tramo (cada 2 m) para ambos coches.
3. Construye la gráfica de **diferencia de tiempos** $\Delta t(x) = t_\text{tu}(x) - t_\text{rival}(x)$.
4. Identifica la **zona crítica** donde el rival ganó la mayor ventaja.
5. Propón **dos** intervenciones específicas en el coche (no genéricas) basadas en esa zona crítica.

**Entregable.** Hoja con tabla de tiempos por tramo, gráfica $\Delta t(x)$ y media página de propuestas justificadas.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cálculo de tiempos por tramo | parcial | completo | con cifras significativas |
| Identificación de zona crítica | sin justificar | identificada visualmente | identificada con valor numérico |
| Propuestas de mejora | genéricas | específicas | específicas + predicción cuantitativa |
::/albatros
