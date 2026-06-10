# Error editorial: imagenes pedagogicas encerradas en cuadros

## Error detectado
Se colocaron imagenes pedagogicas dentro de figuras con borde, fondo blanco, caption separado por linea y altura limitada. El resultado fue que varias imagenes, especialmente infografias y tablas, quedaron visualmente encerradas y reducidas. Aunque la ruta de imagen era correcta, el estudiante no alcanzaba a leer el contenido con comodidad.

## Por que es un problema
- Una infografia pequena pierde funcion pedagogica.
- El borde del contenedor compite con el contenido de la imagen.
- En paginas con dos columnas, la imagen se reduce demasiado.
- El caption de match ayuda editorialmente, pero no debe encerrar ni cortar el visual.
- La validacion de rutas no garantiza legibilidad.

## Regla para futuros manuales
Las imagenes de contenido deben tratarse como material pedagogico principal, no como tarjetas decorativas.

## Correccion aplicada
- Quitar borde y fondo del contenedor `.visual`.
- Quitar linea superior del `figcaption`.
- Aumentar altura maxima de imagenes `full`, `half` y `compact`.
- Forzar que imagenes dentro de `.grid-2` ocupen todo el ancho disponible.
- Mantener caption breve, sin marco, solo como referencia editorial.

## Checklist antes de aprobar una pagina con imagen
1. La imagen se puede leer sin hacer zoom.
2. La imagen no esta encerrada en una tarjeta o marco decorativo.
3. Si la imagen es infografia, tabla o diagrama, ocupa ancho completo.
4. El caption no compite con el contenido visual.
5. La imagen coincide con el concepto inmediato de la pagina.
6. La revision incluye legibilidad visual, no solo existencia de archivo.

## Frase de control
No basta con que la imagen matchee: debe verse grande, limpia y sin encierro visual.
