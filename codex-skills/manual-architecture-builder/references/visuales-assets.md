# Visuales, Iconos Y Prompts

## Estructura De Assets
El bloque visual debe vivir en:

```text
05_assets_visuales_iconos/
|-- iconos/
|-- prompts-visuales/
|-- visuales/
|-- fondo.png
|-- logo.png
`-- portada.png
```

## Prompts Visuales
La carpeta `prompts-visuales` conserva trazabilidad de cada visual:

```text
prompts-visuales/
|-- INDEX.md
|-- INDEX.csv
|-- por-pagina.md
|-- inject-map.json
|-- manifest.json
|-- anidados-pendientes.md
|-- manual-1-prompts.md
|-- manual-2-prompts.md
|-- manual-3-prompts.md
|-- manual-4-prompts.md
|-- manual-5-prompts.md
`-- manual-N/
```

En la base depurada habia 511 prompts/visuales JPG principales en `05_assets_visuales_iconos/visuales`.

## ID De Visual
Usar el formato:

```text
M{N}-{u|sem}{XX}-{NN}
```

Ejemplos:
- `M1-u01-03`
- `M2-sem1-05`

## Destino De Imagenes
Las imagenes generadas o recuperadas deben entrar en:

```text
05_assets_visuales_iconos/visuales/manual-{N}/u{XX}/M{N}-u{XX}-{NN}.jpg
05_assets_visuales_iconos/visuales/manual-{N}/sem1/M{N}-sem1-{NN}.jpg
05_assets_visuales_iconos/visuales/manual-{N}/sem2/M{N}-sem2-{NN}.jpg
```

Mantener el ID como nombre base para que el converter pueda inyectar la imagen.

## Formatos
Para esta base, priorizar `.jpg` para visuales generados. Aceptar tambien `.jpeg`, `.png`, `.webp` y `.svg` si ya existen.

Si hay conflicto entre documentacion vieja y el estado depurado, usar el estado real de `05_assets_visuales_iconos/visuales` y reportar la diferencia.

## Reglas De Preservacion
- No borrar imagenes de manuales originales durante depuracion.
- Si se reorganiza, copiar antes a una carpeta de recuperacion con conteo verificable.
- Mantener iconos separados de visuales pedagogicos.
- Mantener prompts separados de imagenes finales.
- No convertir imagenes sin necesidad; preservar extension y contenido original.
- Verificar conteos despues de copiar: fuente, destino y fallos.

## Regla De Legibilidad Visual
- Una imagen pedagogica no debe ir encerrada en una tarjeta, marco decorativo o contenedor con borde si eso reduce su lectura.
- Infografias, tablas, mapas mentales, diagramas y capturas deben ocupar ancho completo siempre que sea posible.
- Si una imagen aparece dentro de una grilla de dos columnas y no se puede leer sin zoom, debe salir de la grilla y ocupar una fila completa.
- El caption debe ser breve y sin marco; sirve para trazabilidad, no para competir con la imagen.
- Validar imagen no significa solo verificar ruta existente: tambien hay que revisar legibilidad, escala y match con el concepto inmediato de la pagina.
