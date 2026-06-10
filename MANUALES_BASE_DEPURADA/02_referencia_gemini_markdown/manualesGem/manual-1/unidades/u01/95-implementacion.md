---
unidad: 1
seccion: implementacion
paginas_objetivo: 4
---

::implementacion{titulo="Implementación Albatros — Tabla periódica interactiva personal"}
**Objetivo.** Construir tu propia tabla periódica interactiva en formato HTML/JavaScript (sin librerías externas) o en una hoja de cálculo enriquecida, con cada elemento mostrando: símbolo, número atómico, masa atómica, configuración electrónica, electronegatividad, radio atómico, EI y un dato curioso. Al hacer clic (o pasar el mouse) en cualquier elemento, se despliega su ficha completa.

**¿Por qué hacerla?** Porque memorizar la tabla es inútil; **construirla** te obliga a entender cada columna y cada bloque. Tu producto final será una herramienta que te servirá durante todo el bachillerato.

---

### Materiales y recursos

- Computadora con editor de texto (VS Code recomendado) o Google Sheets.
- Acceso a internet para verificar datos numéricos.
- Plantilla base que puedes encontrar en simuladores PhET (referencia visual).
- 1 hora de tiempo enfocado.

### Pasos

**1. Estructura los datos en CSV.** Crea un archivo `elementos.csv` con columnas:
```
Z, simbolo, nombre, masa_atomica, grupo, periodo, bloque, configuracion, EN, radio_pm, EI_kJmol, dato_curioso
```
Llena los datos para los **20 primeros elementos** (H a Ca). Verifica con dos fuentes distintas.

**2. Diseña la cuadrícula HTML.** Usa CSS Grid con 18 columnas y 7 filas:
```html
<div class="tabla">
  <div class="elemento" data-z="1" style="grid-column: 1; grid-row: 1;">H</div>
  <div class="elemento" data-z="2" style="grid-column: 18; grid-row: 1;">He</div>
  ...
</div>
```

**3. Colorea por bloque.** Aplica clases CSS distintas para bloque-s, bloque-p, bloque-d, bloque-f. Usa los colores oficiales Albatros (azul para s, naranja para p, verde para d).

**4. Agrega interactividad.** Con JavaScript vanilla:
```js
document.querySelectorAll('.elemento').forEach(el => {
  el.addEventListener('click', () => mostrarFicha(el.dataset.z));
});
```

**5. Diseña el panel de ficha.** Al hacer clic, muestra:
- Encabezado con símbolo y nombre.
- Datos numéricos (Z, A, EN, radio, EI).
- Configuración electrónica con código de color por subnivel.
- Dato curioso de aplicación cotidiana.

**6. Validación.** Tu compañero/a debería poder, sin ayuda, encontrar:
- El elemento con mayor electronegatividad → debe llegar al flúor.
- Un metal alcalinotérreo de periodo 4 → calcio.
- Un halógeno con configuración terminada en 4p⁵ → bromo.
::/implementacion

::visual{tipo="interfaz" descripcion="Captura de pantalla de la tabla periódica interactiva terminada: cuadrícula 18×7 con elementos coloreados por bloque (s azul, p naranja, d verde), un elemento seleccionado destaca con borde azul Albatros y a la derecha aparece su ficha con todos los datos. Estilo limpio con fondo blanco." paginas="0.5" src="../manualesGem/assets/visuales/manual-1/u01/95-implementacion-v01.svg"}

::implementacion{titulo="Evidencia, entregable y seguimiento"}
### Entregable

URL pública (GitHub Pages, Netlify o CodePen) o archivo HTML descargable con tu tabla funcionando. Debe cubrir los **20 primeros elementos** completos. Bonus: completar los 36 primeros (hasta el kriptón).

### Rúbrica de evaluación

| Criterio | 1 — Inicial | 3 — Suficiente | 5 — Excelente |
|---|---|---|---|
| **Datos correctos** | errores frecuentes | datos correctos para los 10 primeros | datos correctos verificados con 2 fuentes |
| **Posición en la tabla** | algunos elementos mal ubicados | grupo y periodo correctos | bloques diferenciados visualmente con código de color |
| **Interactividad** | estática | clic muestra ficha simple | clic muestra ficha completa con animación suave |
| **Configuración electrónica** | ausente o incorrecta | correcta para los 10 primeros | correcta y formateada con superíndices |
| **Dato curioso** | ausente o copiado | un hecho por elemento | hecho conectado a aplicación cotidiana |

### Reto bonus (+1 punto)

Agrega un **modo predicción**: el usuario ingresa Z y el programa predice automáticamente periodo, grupo, bloque y configuración antes de mostrar el dato real. Es una forma de demostrar que **entendiste la lógica** de la tabla, no solo la copiaste.

---

### Hitos intermedios

| Sprint | Entregable | Día |
|---|---|---|
| 1 | CSV con los 20 primeros elementos verificados con dos fuentes | 3 |
| 2 | Cuadrícula HTML con elementos visibles y posición correcta | 6 |
| 3 | Coloreo por bloques + clic con ficha mínima funcionando | 9 |
| 4 | Ficha completa con configuración, dato curioso y validación con compañero | 14 |

### Reto bonus extendido (+2 puntos cada uno)

1. **Reto A:** integra una capa adicional que muestre, sobre la tabla, la **electronegatividad** de cada elemento como un mapa de calor (gradiente de color). Permite alternar entre EN, radio atómico y EI.
2. **Reto B:** agrega un buscador por nombre, símbolo o configuración. Por ejemplo: si el usuario teclea "[He] 2s² 2p²" tu app debe iluminar el carbono.
3. **Reto C:** crea un modo "predicción de iones": al hacer clic, ofrece el ion más probable con su explicación basada en regla del octeto y muestra al menos un compuesto cotidiano donde aparezca ese ion (Na⁺ → sal de mesa, Ca²⁺ → leche, Cl⁻ → cloro de alberca).
::/implementacion
---

::albatros{titulo="Sprint corto — el dataset del bebedero en tu tabla" tipo="caso" tiempo="30 min"}
**Pregunta detonadora.** Si tu tabla periódica interactiva ya funciona, ¿podrías cruzarla con el reporte real del bebedero y resaltar exactamente los elementos presentes en tu agua escolar?

**Lo que harás.**
1. Toma el reporte del laboratorio (Na, Ca, Mg, Cl, K, F, S, etc.).
2. Carga las concentraciones en una hoja secundaria de tu app o en un objeto JSON.
3. Programa una visualización: cada elemento del agua aparece resaltado con un círculo cuyo radio es proporcional a su ppm.
4. Permite al usuario hacer clic en el elemento para ver: ppm, ion correspondiente, función biológica.
5. Documenta las decisiones de diseño y publica el cambio en tu repo.

**Materiales.** Tu app de la implementación principal · datos del bebedero · 30 minutos.

**Entregable.** Captura o video de 30 s mostrando la nueva capa funcionando + commit con mensaje descriptivo.

**Rúbrica corta.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Datos cargados | 1–2 elementos | todos los del reporte | reporte + comparación con norma |
| Resaltado visual | constante | proporcional | proporcional + leyenda interactiva |
| Información del ion | solo nombre | ion y carga | ion, carga, función biológica y rango sano |
::/albatros
