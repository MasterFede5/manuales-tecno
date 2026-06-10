---
unidad: 0
seccion: implementacion
paginas_objetivo: 3
---

::implementacion{titulo="Implementación Albatros — Bitácora digital de laboratorio"}
**Objetivo.** Crear tu propia plantilla en Google Sheets (o Notion) para registrar mediciones químicas con cálculo automático de media, desviación estándar e incertidumbre combinada. Esta bitácora será tu compañera durante **todas** las unidades siguientes del manual: cuando midas pH, dureza, conductividad o cualquier otra variable, vas a vaciar tus repeticiones aquí y obtendrás el reporte listo en segundos.

**¿Por qué hacerla ahora?** Porque automatizar **una vez** los cálculos te ahorra cientos de operaciones manuales en las siguientes 6 unidades, y porque construir la herramienta te obliga a entender la fórmula desde adentro.

---

### Materiales y recursos

- Cuenta de Google (Sheets gratuito) **o** cuenta de Notion.
- Navegador en cualquier dispositivo.
- Una calculadora de respaldo para verificar tus fórmulas.
- Un dato real para la primera prueba (sirve la práctica resuelta del bebedero).

### Pasos

**1. Estructura la hoja.** Crea las siguientes columnas en la fila 1:

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Medición # | Valor | Unidad | Resolución | Fecha | Comentario |

**2. Agrega un bloque de cálculo automatizado.** En las celdas H1:I8 escribe:

| H | I |
|---|---|
| n (número de mediciones) | `=COUNTA(B2:B100)` |
| Media $\bar{x}$ | `=AVERAGE(B2:B100)` |
| Desviación estándar $s$ | `=STDEV(B2:B100)` |
| Incertidumbre tipo A $u_A$ | `=I3/SQRT(I1)` |
| Resolución del instrumento | (la copias de la columna D) |
| Incertidumbre tipo B $u_B$ | `=I5/2` |
| Incertidumbre combinada $u_c$ | `=SQRT(I4^2+I6^2)` |
| Reporte | `=I2 & " ± " & I7` |

**3. Sección de cifras significativas.** En J1:J3 agrega:
- Número de cs sugeridas: `=IF(I7<0.1; 3; IF(I7<1; 2; 1))`
- Reporte redondeado: `=ROUND(I2; -INT(LOG(I7)))` con su `±` correspondiente.

**4. Validación con un dato real.** Vacía las 5 mediciones de pH del bebedero (subtema 0.4 — práctica resuelta) y verifica que tu hoja produzca **pH = 7.06 ± 0.01**. Si no coincide, depura.

**5. Compártelo.** Genera un enlace público de solo lectura y entrégaselo a tu docente para que valide el funcionamiento.
::/implementacion

::visual{tipo="interfaz" descripcion="Captura de la plantilla terminada en Google Sheets: lado izquierdo con la tabla de mediciones (columnas A-F llenas con 5 datos del pH del bebedero), lado derecho con el bloque de fórmulas (H1:I8) mostrando los resultados calculados automáticamente y celda final destacada con 'pH = 7.06 ± 0.01'. Paleta azul-naranja Albatros." paginas="0.5" src="../manualesGem/assets/visuales/manual-1/u00/95-implementacion-v01.svg"}

::implementacion{titulo="Evidencia, entregable y seguimiento"}
### Entregable

URL pública de tu bitácora con al menos un dataset cargado (mínimo 3 mediciones reales — pueden ser de la actividad Albatros del lápiz, la práctica del bebedero o cualquier otra de tu elección). Documenta en una nota dentro del archivo: instrumento usado, resolución, fecha y conclusión metrológica.

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| **Estructura de columnas** | columnas faltantes o desordenadas | las 6 columnas presentes | columnas formateadas con color y validación de datos |
| **Fórmulas automatizadas** | una o ninguna funcionando | media y desviación correctas | todas las incertidumbres + redondeo automático |
| **Validación con caso real** | datos copiados sin verificar | dataset coincide con el del manual | dataset propio cargado y verificado contra teoría |
| **Cifras significativas** | reporte sin cs | cs correctas en valor, no en incertidumbre | cs consistentes en valor e incertidumbre |
| **Documentación** | sin notas | encabezados claros | notas técnicas + autor + fecha + revisor |

### Reto bonus (+1 punto)

Agrega un gráfico de dispersión que muestre las repeticiones con su barra de error ($\pm u_c$) y una línea horizontal que represente el límite normativo (en el caso del bebedero, 6.5 y 8.5). Esto convierte tu bitácora en un **instrumento de toma de decisiones**, no solo de cálculo.

---

### Hitos intermedios

| Sprint | Entregable | Día |
|---|---|---|
| 1 | Hoja inicial con columnas A–F y tres mediciones de prueba cargadas | 2 |
| 2 | Bloque de fórmulas (media, $s$, $u_A$, $u_B$, $u_c$) verificado con la práctica del bebedero | 5 |
| 3 | Sección de cifras significativas funcionando con redondeo automático | 8 |
| 4 | Versión final compartida con el docente, gráfico de dispersión y nota de uso | 12 |

### Reto bonus extendido (+2 puntos cada uno)

1. **Reto A:** agrega una hoja secundaria que reciba la **resolución** de cualquier instrumento y devuelva, automáticamente, la cs sugerida y la $u_B$ correspondiente. Documenta la fórmula usada.
2. **Reto B:** programa una alerta condicional que cambie el color de la celda "Reporte" a rojo si el intervalo $\bar{x} \pm u_c$ **no** queda dentro del rango normativo elegido (por ejemplo NOM-127 para pH).
3. **Reto C:** convierte la bitácora en una plantilla pública (template) y publícala en el drive del salón con instrucciones para que cualquier compañero la duplique antes de empezar su práctica.
::/implementacion
---

::albatros{titulo="Sprint corto — calibración rápida del termómetro" tipo="reto" tiempo="30 min"}
**Pregunta detonadora.** ¿Cómo verificas en 30 minutos que el termómetro escolar mide bien antes de usarlo en el bebedero?

**Lo que harás.**
1. Prepara dos baños de referencia: agua con hielo en equilibrio (~0 °C) y agua hirviendo a presión local (~100 °C, ajusta por altitud si tienes el dato).
2. Mide **3 veces** en cada baño con tu termómetro.
3. Calcula media y desviación. Identifica si hay sesgo (error sistemático).
4. Si el sesgo es mayor que la $u_c$, anota la corrección a aplicar a futuras mediciones (offset).
5. Carga los datos en tu bitácora del sprint principal y guarda como "calibración del [fecha]".

**Materiales.** Hielo · cazuela · termómetro · cronómetro · bitácora.

**Entregable.** Mini-reporte de media página con los 6 datos, el cálculo del offset y la decisión: ¿usas el termómetro tal cual o aplicas corrección?

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Toma de datos | 1 baño solamente | 2 baños con 1 dato | 2 baños con 3 datos cada uno |
| Identificación del sesgo | no calcula | calcula media | calcula media y compara con $u_c$ |
| Decisión documentada | sin decisión | "está bien" sin argumento | offset propuesto o validación con cifras |
::/albatros
