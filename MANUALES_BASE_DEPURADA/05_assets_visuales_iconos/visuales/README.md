# `assets/visuales/`

Carpeta destino para las imágenes de los manuales Albatros.

## Convención de nombres

```
assets/visuales/manual-{N}/u{XX}/M{N}-u{XX}-{NN}.jpg
```

- **N** = número de manual (1..5)
- **XX** = unidad con dos dígitos (00, 01, ... 10)
- **NN** = ordinal del visual dentro de la unidad (01, 02, ...)

Cada `M{N}-u{XX}-{NN}` corresponde a un `::visual{}` del .md fuente.
El mapeo exacto está en `assets/prompts-visuales/inject-map.json`.

## Formatos aceptados (en este orden)

`.jpg` > `.jpeg` > `.png` > `.webp` > `.svg`

## Inyección automática

`build/converter.py` busca la imagen cuando construye el HTML. Si existe,
inyecta `<img src="...">` con el atributo `id="M{N}-u{XX}-{NN}"` en
el `<figure>` correspondiente. Si no existe, deja el placeholder generado
(SVG simbólico).

Para regenerar:

```
python build/converter.py manuales/manual-1 dist/manual-1.html
python print_to_pdf.py --manual 1
```

## Imágenes pendientes

Total de IDs asignados a través de los 5 manuales: ver
`assets/prompts-visuales/INDEX.md`.
