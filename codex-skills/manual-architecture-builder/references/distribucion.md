# Distribucion Fiel Del Manual

## Raiz Depurada
La estructura base usada para construir manuales queda asi:

```text
MANUALES_BASE_DEPURADA/
|-- 00_temario_estructura/
|-- 01_fuente_principal_markdown/
|-- 02_referencia_gemini_markdown/
|-- 03_referencias_quimica/
|-- 04_referencia_diseno/
|-- 05_assets_visuales_iconos/
|-- 06_motor_compilacion_minimo/
|-- 07_docs_pedagogicos/
`-- 08_fuentes_externas/
```

## Funcion De Cada Bloque
- `00_temario_estructura`: arquitectura, manifiestos, mapas curriculares, ensamblaje general.
- `01_fuente_principal_markdown`: fuente canonica doc-as-code para producir manuales nuevos.
- `02_referencia_gemini_markdown`: referencia historica Markdown generada; no debe mezclarse con la fuente canonica sin revision.
- `03_referencias_quimica`: manual de quimica previo, HTML, imagenes y anexos usados como referencia.
- `04_referencia_diseno`: manual de fisica y archivos visuales/HTML usados como referencia de diseno.
- `05_assets_visuales_iconos`: identidad visual, iconografia, prompts visuales e imagenes generadas.
- `06_motor_compilacion_minimo`: scripts y plantillas para convertir Markdown a HTML/PDF/DOCX.
- `07_docs_pedagogicos`: diagnosticos, reportes, verificacion de especificacion y documentacion de arquitectura.
- `08_fuentes_externas`: guias, PDFs y fuentes externas de apoyo.

## Estructura Canonica De Manual
Dentro de `01_fuente_principal_markdown/manuales`:

```text
manuales/
|-- manual-1/
|-- manual-2/
|-- manual-3/
|-- manual-4/
`-- manual-5/
```

Cada `manual-N` debe seguir:

```text
manual-N/
|-- manifest.md
|-- semestre-1/
|   |-- 00-portada.md
|   |-- 01-carta-estudiante.md
|   |-- 02-carta-docente.md
|   |-- 03-mapa-contenidos.md
|   |-- 04-hilo-conductor.md
|   |-- 05-competencias.md
|   |-- 06-diagnostica.md
|   |-- 90-cierre-semestre.md
|   |-- 91-material-extra.md
|   |-- 92-glosario-semestre.md
|   |-- 93-bibliografia-semestre.md
|   `-- 94-indice-analitico.md
|-- semestre-2/
|   `-- mismos archivos que semestre-1
`-- unidades/
    |-- u01/
    |   |-- README.md
    |   |-- 00-portadilla.md
    |   |-- 01-mapa-mental.md
    |   |-- 02-caso-episodio.md
    |   |-- 10-tema-1-1.md
    |   |-- 10-tema-1-2.md
    |   |-- 80-practica-resuelta.md
    |   |-- 81-banco-ejercicios.md
    |   |-- 90-actividades.md
    |   |-- 92-investigacion.md
    |   |-- 93-taller.md
    |   |-- 94-fuentes.md
    |   |-- 95-implementacion.md
    |   `-- 99-cierre.md
    `-- uXX/
```

## Division Por Semestres
Usar esta division mientras no haya un temario nuevo aprobado:

| Manual | Semestre 1 | Semestre 2 |
|---|---|---|
| M1 Quimica | u00, u01, u02, u03 | u04, u05, u06 |
| M2 Fisica | u01, u02, u03, u04, u05 | u06, u07, u08, u09 |
| M3 IA Basica | u01, u02, u03, u04, u05 | u06, u07, u08, u09 |
| M4 IA Avanzada | u01, u02, u03, u04, u05 | u06, u07, u08, u09, u10 |
| M5 IA con Programacion | u01, u02, u03, u04 | u05, u06, u07, u08 |

## Orden De Ensamblaje
Para compilar un semestre:
1. Leer front matter de `semestre-X` de `00` a `06`.
2. Leer unidades del semestre en orden ascendente.
3. Dentro de cada unidad, respetar orden numerico de archivos.
4. Cerrar con archivos `90` a `94` del semestre.

No saltar archivos por conveniencia. Si falta una pieza, reportarla.
