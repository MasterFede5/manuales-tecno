---
unidad: 7
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Diseño y simulación CFD del alerón en SimScale"}
**Objetivo.** Diseñar tres variantes de alerón trasero para tu coche F1 escolar, simular el flujo de aire alrededor de cada una con CFD (Computational Fluid Dynamics) gratuito en SimScale, comparar el downforce y el drag de cada variante, y elegir la mejor para tu pista.

**¿Por qué hacerla?** Antes de construir físicamente cualquier alerón —que toma horas de impresión 3D o de mecanizado— una simulación CFD te dice en minutos qué geometría funciona. Es exactamente cómo trabajan los equipos profesionales de F1: prueban miles de variantes en computadora antes de tocar materiales. Esta práctica te entrena en CFD básico.

---

### Materiales y software

- Computadora con navegador moderno (Chrome o Firefox actualizado).
- Cuenta gratuita en **SimScale** (https://simscale.com — registro académico gratis).
- **Tinkercad** o **Onshape** (también gratuitos) para modelar los alerones en 3D.
- Calibrador o regla para medir tu coche real.
- Hoja de cálculo (Google Sheets o Excel) para tabular resultados.

### Pasos

1. **Modelar tres variantes.** En Tinkercad, crea tres alerones del mismo ancho (8 cm) pero con distintos ángulos de ataque: 5°, 15° y 25°. Mismo perfil (NACA 0012 invertido o caja simple inclinada).
2. **Importar a SimScale.** Sube los STL de cada variante a un proyecto de "External flow analysis".
3. **Configurar la simulación.** Velocidad del flujo de aire = 22 m/s (80 km/h). Densidad 1.20 kg/m³. Volumen de control alrededor del alerón ≥ 5 veces su tamaño.
4. **Ejecutar.** Cada simulación tarda 5-15 minutos en la nube gratuita. Repite con las 3 variantes.
5. **Extraer resultados.** En el postproceso obtén: $F_{drag}$ horizontal, $F_{lift}$ vertical (negativo en alerón = downforce), distribución de presión sobre el perfil.
6. **Tabular y comparar.** Llena la tabla siguiente y elige la mejor variante para una pista con 70 % de curvas y 30 % de rectas.
7. **Validar con cálculo manual.** Aplica la fórmula de Bernoulli aproximada y compara con SimScale (deben dar el mismo orden de magnitud).

::visual{tipo="ilustracion" descripcion="Esquema en tres pasos del flujo de trabajo: 1) MODELADO — tres alerones con ángulos 5°/15°/25° en vista isométrica, mismo ancho y cuerda. 2) SIMULACIÓN CFD — captura del entorno SimScale con el alerón inmerso en un volumen de control y líneas de corriente coloreadas por velocidad. 3) RESULTADO — gráfico de barras con downforce y drag de las tres variantes, indicando con flecha la elección óptima." paginas=0.5}

### Tabla de resultados a entregar

| Variante | Ángulo | Downforce (N) | Drag (N) | Eficiencia (DF/Drag) |
|---|---:|---:|---:|---:|
| A | 5° | | | |
| B | 15° | | | |
| C | 25° | | | |

---

### Entregable

Reporte de 3 páginas con:
1. Capturas del modelado y de la simulación CFD de cada variante.
2. Tabla de resultados completada.
3. Decisión justificada: cuál variante usarías y por qué para una pista con 70 % curvas / 30 % rectas. Cambia el porcentaje al revés y vuelve a justificar.
4. Cálculo manual de Bernoulli para la variante elegida; compara con el valor que dio SimScale y explica las diferencias (efectos viscosos, turbulencia, separación de flujo, etc.).
5. Reflexión: ¿qué pasaría si duplicas la velocidad del coche? Recalcula downforce esperado.

### Rúbrica de evaluación

| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| **Modelado 3D** | una sola variante | tres variantes pero mal proporcionadas | tres variantes bien hechas con el mismo ancho |
| **Simulación CFD** | no logra correr | corre y obtiene un valor | corre las 3 y compara coherentemente |
| **Cálculo manual** | no aplica fórmulas | aplica con errores | aplica correctamente y discute la diferencia con CFD |
| **Decisión justificada** | "el más grande" | menciona compromiso DF/drag | razona ambos escenarios de pista |
| **Reflexión** | sin reflexión | menciona escalado | calcula nuevo downforce con $v^2$ |

---

### Hitos intermedios

| Sprint | Semana | Meta concreta | Evidencia |
|---|---|---|---|
| 1. Modelado | 1 | Tres alerones STL listos en Tinkercad o Onshape | archivos STL |
| 2. Simulación | 2 | Las tres variantes corridas en SimScale con malla y volumen de control | capturas de SimScale |
| 3. Análisis | 3 | Tabla DF/Drag completa + cálculo manual con Bernoulli | hoja de cálculo |
| 4. Reporte y validación | 4 | Reporte con decisión justificada para dos escenarios de pista | reporte 4 pp |

### Reto bonus extendido (+2 puntos cada uno)

1. **Validación con túnel de viento casero.** Construye el túnel del taller (93-taller.md) y compara los valores experimentales con los de SimScale para las tres variantes. Discute discrepancias por turbulencia, separación de flujo y rugosidad.
2. **Optimización paramétrica.** Corre simulaciones para 5 ángulos (5°, 10°, 15°, 20°, 25°) y grafica DF/Drag vs ángulo. Encuentra el ángulo óptimo numéricamente.
3. **Efecto de la velocidad.** Repite la simulación de la mejor variante a velocidades de 15, 22 y 30 m/s. Verifica que DF y Drag escalan como $v^2$ (regresión cuadrática) y reporta el coeficiente.
::/implementacion

---

::albatros{titulo="Caso integrador — el coche que vuela por exceso de drag" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Tu coche F1 a 25 m/s tiene un drag medido de 0.78 N pero el teórico debería ser 0.55 N. ¿De dónde vienen los 0.23 N extra y cómo los reduces?

**Lo que harás.**
1. Calcula $C_d$ efectivo a partir del drag medido: $C_d = 2F/(\rho v^2 A_f)$ con $A_f = 30$ cm².
2. Compara con $C_d$ teórico (~0.45 para coche aerodinámico).
3. Identifica tres fuentes posibles de drag extra: rugosidad superficial, alerón mal alineado, separación de flujo en la cola.
4. Propón un experimento sencillo (por ejemplo lijar la superficie, alinear el alerón con un transportador, agregar un difusor cónico atrás) para reducir cada una y predice cuántos newtons de drag bajan.
5. Si reduces el drag a 0.55 N, ¿cuánto tiempo ganas en una recta de 18 m? Suponiendo aceleración aproximada $a \approx -F/m$ post-empuje.

**Entregable.** Hoja con cálculos paso a paso y tabla con: $C_d$ medido, $C_d$ teórico, tres fuentes con reducción esperada, ganancia de tiempo en recta.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Cálculo de $C_d$ efectivo | sin valor | con valor numérico | + comparación con teórico |
| Tres fuentes de drag extra | una | tres | + intervención cuantitativa |
| Ganancia de tiempo | sin valor | con valor numérico | + cifras significativas |
::/albatros
