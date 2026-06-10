# Error editorial: imagen que existe pero no corresponde al tema inmediato

## Error detectado
En Manual 1 se usaron varias imagenes correctas como assets, pero en paginas equivocadas. El problema no era la ruta ni la calidad del JPG; el problema era semantico: la imagen no enlazaba con el tema inmediato de la pagina.

## Ejemplos del error
- Una imagen de fuerzas intermoleculares se uso como si fuera enlace quimico general.
- Una imagen de hidratacion de iones en agua se uso como si fuera residuo de evaporacion.
- Visuales de configuracion electronica, Lewis, tendencias periodicas y nomenclatura quedaron fuera aunque eran los que correspondian a esos temas.

## Por que es grave
- El estudiante mira una imagen esperando apoyo conceptual y recibe otra idea.
- La pagina pierde coherencia entre historia, teoria, visual y practica.
- El caption puede parecer correcto, pero si contradice el prompt original de la imagen genera confusion.
- Verificar que el archivo existe no valida que la imagen sea pedagogicamente correcta.

## Regla para futuros manuales
Cada visual debe ubicarse segun su prompt original y su funcion didactica, no solo por el ID o por parecido superficial.

## Procedimiento obligatorio antes de insertar imagen
1. Leer el prompt o descripcion original del visual.
2. Identificar el concepto exacto que representa.
3. Insertarlo solo en la pagina donde ese concepto se explica.
4. Si el tema de la pagina no existe todavia, no usar la imagen.
5. El caption debe describir el tema real de la imagen, no reinterpretarla.
6. Verificar ruta, legibilidad y correspondencia semantica.

## Frase de control
Una imagen no se aprueba porque sea bonita ni porque exista: se aprueba porque ensena exactamente el concepto de esa pagina.
