# Pipeline De Construccion

## Motor Minimo
El bloque de compilacion vive en:

```text
06_motor_compilacion_minimo/
|-- build/
|-- build_docx.py
|-- build_semestres.py
|-- convert_html_to_docx.py
|-- diagnostico_pedagogico.py
|-- extract_visual_prompts.py
|-- print_to_pdf.py
|-- scaffold_semestres.py
`-- verify_spec.py
```

## Build
El subdirectorio `build` contiene el motor Markdown a HTML:

```text
build/
|-- converter.py
|-- print-letter.css
|-- digital.css
|-- template.html
|-- iconografia.py
|-- iconos.py
|-- scaffold.py
`-- validate.py
```

## Comandos Base
Desde una base equivalente a `manual tecno`:

```powershell
python 06_motor_compilacion_minimo/build/converter.py 01_fuente_principal_markdown/manuales/manual-1 dist/manual-1.html
python 06_motor_compilacion_minimo/print_to_pdf.py --manual 1
python 06_motor_compilacion_minimo/build_docx.py
python 06_motor_compilacion_minimo/verify_spec.py
```

Adaptar rutas si los scripts esperan layout corto (`manuales/`, `build/`, `assets/`, `dist/`). Si se trabaja dentro de `MANUALES_BASE_DEPURADA`, confirmar la ruta esperada antes de ejecutar.

## Bloques Semanticos Markdown
El converter espera directivas como:

```text
::concepto::
::interioriza::
::pausa::
::practica::
::caso::
::implementacion::
::albatros::
::investiga::
::fuentes::
::visual::
```

Tambien acepta actividades:

```text
::act-fill::
::act-mcq::
::act-table::
::act-calc::
::act-match::
::act-tf::
::act-order::
::act-case::
::act-puzzle::
::act-mindmap::
::act-label::
::act-challenge::
```

## Validacion
Antes de cerrar una construccion:
1. Verificar estructura de manuales y semestres.
2. Verificar que los `::visual{}` tengan ID e imagen destino si ya fueron generados.
3. Validar que las fuentes canonicas no mezclen HTML viejo.
4. Ejecutar `verify_spec.py` si las dependencias estan disponibles.
5. Generar HTML de prueba antes de PDF/DOCX.
6. Reportar errores con archivo, linea y accion concreta.
