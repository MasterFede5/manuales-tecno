# Unidad HTML Iterativa

Usar esta referencia cuando el usuario quiera construir una unidad modelo antes de replicar el resto del manual.

## Principio
Trabajar una unidad en un solo documento HTML editable. No generar manuales completos en lote durante la fase de diseno pedagogico. La unidad aprobada se convierte en patron para las demas.

## Flujo
1. Elegir un unico archivo de trabajo, por ejemplo:
   `01_fuente_principal_markdown/manuales/manual-1/unidades/u00/unidad-0-quimica.html`
2. Leer primero las fuentes canonicas de la unidad (`README.md`, portadilla, caso, temas, practica, banco, actividades, taller, fuentes y cierre).
3. Auditar visuales y prompts de esa unidad antes de escribir HTML.
4. Construir el HTML por bloques pequenos y revisar en navegador despues de cambios relevantes.
5. Iterar sobre el mismo HTML. No crear variantes paralelas salvo que el usuario lo pida.
6. Cuando el usuario apruebe la unidad, documentar la estructura final como plantilla y recien entonces replicarla al resto.

## Estructura Pedagogica Base
- Portadilla de unidad con historia y visual principal.
- Historia breve con conflicto concreto.
- Preguntas introductorias antes de teoria.
- Teoria con analogias, formulas, variables y unidades.
- Visuales solo si coinciden con el concepto inmediato de la pagina.
- Actividad especificada con producto verificable.
- Practica guiada y practica abierta.
- Banco de ejercicios en hoja carta, minimo 4 ejercicios por pagina.
- Cierre con rubrica, fuentes y siguiente unidad.

## Reglas De Imagen
- No encerrar visuales pedagogicos en tarjetas, cajas, marcos pesados ni fondos que reduzcan legibilidad.
- Cada imagen debe tener `data-visual-id` y caption corto.
- Si la imagen no coincide semanticamente con el bloque, no usarla ahi.
- Priorizar imagen grande y legible sobre texto largo alrededor de la imagen.
- No describir literalmente mapas mentales, infografias, cuadros o prompts visuales dentro del texto del manual. Si el visual es un mapa, convertir su contenido en una historia, recorrido narrativo o decision del caso conductor.
- No repetir el mismo texto introductorio debajo o arriba de imagenes consecutivas. Cada visual necesita una entrada distinta, una frase/analogia propia y una mini actividad diferente.
- En impresion carta, los conceptos deben ser legibles: evitar cuerpos menores a 8.8 pt en tarjetas de concepto y usar jerarquia clara en los terminos.
- Cuando una imagen trate clasificacion de materia, no basta con pedir "aplica el visual". Definir sustancias puras, elementos, compuestos, mezclas homogeneas y heterogeneas; despues usar una tabla con sustancias concretas para clasificar.
- La actividad posterior a la imagen debe variar segun el tema: tabla, comparacion, calculo, explicacion corta, diagrama, decision del caso o registro de laboratorio. No repetir la misma consigna generica.
- Evitar abusar del encabezado "Ejercicio de desarrollo". Alternar tipos de practica con nombres especificos: comprobacion con calculos, cuadro comparativo, preguntas abiertas, relacion de columnas, explicacion con evidencia, tabla de clasificacion, registro de laboratorio y mini reto aplicado.
- Para cada 4 a 6 paginas de teoria visual, debe existir variedad evaluable: al menos una actividad de calculo, una de explicacion, una de tabla/cuadro y una de relacion o comparacion.
- Los visuales densos con texto pequeno, como tablas periodicas, nomenclatura, cuadros comparativos, mapas con muchas ramas o infografias con formulas, no deben encerrarse en paginas con demasiados bloques alrededor. Deben ampliarse, ocupar casi toda la hoja o dividirse en lectura visual + practica en pagina siguiente.
- Si una tabla o cuadro no se aprecia en impresion, priorizar legibilidad sobre cantidad de texto: aumentar escala, reducir texto acompanante y mover la actividad a la pagina posterior.
- Requerimiento minimo de letra para impresion: tarjetas de concepto, instrucciones, cuadros, tablas y ejercicios no deben bajar de 10.5 pt; terminos, encabezados de tabla y enunciados principales deben quedar en 11 pt o mas cuando se impriman.
- Las relaciones de columnas deben construirse como ejercicio relacionable real: Columna A con letras (A, B, C...), Columna B con numeros (1, 2, 3...) y un espacio de respuesta para pares como A-2, B-1, C-3. No usar tablas genericas sin correspondencias.
- Toda instruccion de cuadro comparativo debe decir que dos elementos se comparan, bajo que criterios y que producto debe entregar el alumno. Evitar "compara dos casos" si no se nombran los casos.
- Cada unidad debe incluir un banco de ejercicios de calculo separado o claramente identificable, con formula, sustitucion, resultado, unidades y espacio suficiente para operaciones.
- Las instrucciones deben estar semanticamente conectadas con el visual inmediato: Lewis debe pedir electrones de valencia y estructura; nomenclatura debe pedir nombre/formula/sistema; tabla periodica debe pedir grupo, periodo, tendencia o prediccion.
- Ningun cuadro, tabla, actividad, banco o bloque de conceptos debe quedar cortado por el cambio de pagina. Si no cabe completo en la hoja carta, moverlo a la siguiente pagina o dividirlo en una pagina de teoria y otra de actividad.
- La verificacion final debe auditar desbordes visuales: paginas con contenido por debajo del pie, `scrollHeight` mayor que la hoja o elementos `.development-card`, `.exercise-development`, `.classification-task`, `.mini-table`, `.bank-item` y `.concept` que crucen el limite inferior.
- Ninguna actividad debe pedir calculo, relacion de columnas, clasificacion o dibujo tecnico sin teoria minima previa. Antes de la actividad debe existir una explicacion breve, analogia, formula, variables y unidades cuando aplique.
- Si el manual no explica todavia el concepto necesario para resolver una actividad, la consigna debe decir explicitamente "Investiga por tu cuenta..." e indicar que buscar: definicion, regla, formula, ejemplo y fuente consultada.
- En temas de isótopos, explicar antes: mismo elemento = mismo Z/protones; distinto isotopo = distinto numero de neutrones; A = Z + N y N = A - Z. Usar una analogia clara antes del calculo.
- En temas de configuracion electronica, si no se desarrollan Aufbau, Hund y Pauli en la teoria previa, la actividad debe ser de investigacion guiada antes de relacionar columnas.
- En temas de Lewis, explicar antes: electrones de valencia, ubicacion por grupo en tabla periodica, puntos alrededor del simbolo, pares compartidos y pares libres. La actividad debe pedir construir Lewis paso a paso, no solo llenar una tabla.
- El lenguaje editorial debe estar en español latino correcto: acentos, signos de apertura, ñ, términos químicos y tono escolar claro. No entregar texto sin acentuar como "Que", "formula", "calculo", "atomico", "periodica" o "conclusion" cuando corresponda "Qué", "fórmula", "cálculo", "atómico", "periódica" o "conclusión".
- Antes de cerrar un HTML, ejecutar una revisión ortográfica mínima de palabras frecuentes sin acento y corregir el manual generado, no solo la fuente del generador.
- Las infografías, mapas, tablas visuales o cuadros con texto pequeño deben revisarse por legibilidad en impresión. Si el texto no se alcanza a leer, el visual debe ocupar página completa, usar menor texto alrededor o pasar a hoja horizontal cuando su proporción lo favorezca.
- Las imágenes pedagógicas no deben recortarse para llenar la hoja si contienen texto. Usar `object-fit: contain`, centrar, ampliar al máximo posible y mover actividades a otra página si hace falta espacio.
- Para visuales densos, validar con captura o auditoría de navegador que la imagen se vea completa, sin corte y con tamaño suficiente antes de aprobar el manual.

## Control De Calidad
Antes de decir que la unidad esta lista:
- Contar paginas `.page`.
- Contar imagenes y verificar 0 rutas rotas.
- Confirmar que hay historia, teoria, formulas/unidades, practica y ejercicios.
- Abrir o capturar una vista en navegador.
- Reportar pendientes editoriales sin ocultarlos.

## Patron Validado En U0 Quimica
Al construir unidades del Manual 1, replicar este ritmo:
1. Portada y temario solo al iniciar el manual.
2. Introduccion con historia, conceptos previos y preguntas con lineas de respuesta.
3. Cada imagen entra con una funcion pedagogica clara, no como decoracion.
4. Debajo de cada imagen usar una frase/analogia que encuadre la idea, sin mencionar ID ni prompt.
5. Cada imagen aplicada debe tener mini actividad conectada al caso conductor.
6. La pagina siguiente explica de forma general lo que implica la imagen y propone un ejercicio de desarrollo.
7. Cuando haya calculos, primero contar la relevancia historica o practica de las herramientas, unidades y mediciones.
8. Explicar formulas antes del banco: conversiones, promedio, error absoluto, error relativo, error porcentual, precision/exactitud y formulas propias del tema.
9. Los bancos van a 4 ejercicios por pagina cuando sea posible, con espacio de operaciones rotulado.
10. Cerrar cada tramo conectando el calculo con el caso conductor y con una medicion concreta.
