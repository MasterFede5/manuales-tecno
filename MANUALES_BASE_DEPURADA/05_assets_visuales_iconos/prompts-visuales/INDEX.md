# Índice maestro de prompts visuales

**Total:** 511 prompts. Cada uno con ID estable, página PDF estimada, archivo fuente y destino.

## Cómo buscar

- Por ID: `Ctrl+F` con `M1-u02-05`.
- Por página del PDF: revisa el bloque del manual y semestre correspondiente abajo.
- Por nombre de archivo: cada prompt vive en `assets/prompts-visuales/manual-N/sem-X/uXX/<ID>__<tipo>__<rol>__pp<P>.md`.
- Machine-readable: `INDEX.csv` (mismas columnas).

## Convenciones de nombre

```
M{N}-{u|sem}{XX}-{NN}__{tipo}__{rol}__pp{P}.md
```

- `N` = manual (1..5)
- `uXX` = unidad (u00..u10) o `semXX` para front/back matter del semestre
- `NN` = ordinal dentro de la unidad (01, 02, …)
- `tipo` = ilustracion, infografia, mapa-mental, cuadro-comparativo, diagrama-flujo, linea-tiempo, grafica, tabla-grande, interfaz
- `rol` = portadilla, mapa-mental-de-unidad, episodio-del-case-study, desarrollo-de-subtema, practica-resuelta, banco-de-ejercicios, catalogo-de-actividades, apartado-de-investigacion, taller-practico, proyecto-integrador, cierre-y-autoevaluacion, contenido-del-manual
- `pp` = páginas que ocupa (0p5 = ½ página, 1 = página completa, 2 = doble)

## Imágenes generadas

- **Listas:** 511/511
- **Pendientes:** 0/511

Las imágenes deben colocarse en `assets/visuales/manual-N/uXX/<ID>.jpg`.

## Manual 1

### Semestre 1 — `dist/manual-1-sem-1.pdf`

| Pág PDF | ID | Tipo | pp | Unidad | Rol | Prompt | Imagen |
|---:|---|---|---:|---|---|---|---|
| **1** | `M1-sem1-01` | ilustracion | 1 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-01__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **1** | `M1-sem1-02` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-02__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **3** | `M1-sem1-03` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-03__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **5** | `M1-sem1-04` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-04__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **6** | `M1-sem1-05` | infografia | 1 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-05__infografia__contenido-del-manual__pp1.md) | ✓ |
| **8** | `M1-sem1-06` | linea-tiempo | 1 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-06__linea-tiempo__contenido-del-manual__pp1.md) | ✓ |
| **10** | `M1-sem1-07` | cuadro-comparativo | 1 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-07__cuadro-comparativo__contenido-del-manual__pp1.md) | ✓ |
| **12** | `M1-sem1-08` | grafica | 0.5 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-08__grafica__contenido-del-manual__pp0p5.md) | ✓ |
| **13** | `M1-u00-01` | ilustracion | 1 | u00 | portadilla | [md](manual-1/sem-1/u00/M1-u00-01__ilustracion__portadilla__pp1.md) | ✓ |
| **13** | `M1-u00-02` | mapa-mental | 1 | u00 | mapa mental de unidad | [md](manual-1/sem-1/u00/M1-u00-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **18** | `M1-u00-03` | diagrama-flujo | 0.5 | u00 | desarrollo de subtema | [md](manual-1/sem-1/u00/M1-u00-03__diagrama-flujo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **22** | `M1-u00-04` | tabla-grande | 1 | u00 | desarrollo de subtema | [md](manual-1/sem-1/u00/M1-u00-04__tabla-grande__desarrollo-de-subtema__pp1.md) | ✓ |
| **26** | `M1-u00-05` | cuadro-comparativo | 0.5 | u00 | desarrollo de subtema | [md](manual-1/sem-1/u00/M1-u00-05__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **32** | `M1-u00-06` | ilustracion | 0.5 | u00 | desarrollo de subtema | [md](manual-1/sem-1/u00/M1-u00-06__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **59** | `M1-u00-07` | diagrama-flujo | 0.5 | u00 | taller práctico | [md](manual-1/sem-1/u00/M1-u00-07__diagrama-flujo__taller-pr-ctico__pp0p5.md) | ✓ |
| **68** | `M1-u01-01` | ilustracion | 1 | u01 | portadilla | [md](manual-1/sem-1/u01/M1-u01-01__ilustracion__portadilla__pp1.md) | ✓ |
| **68** | `M1-u01-02` | mapa-mental | 1 | u01 | mapa mental de unidad | [md](manual-1/sem-1/u01/M1-u01-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **72** | `M1-u01-03` | cuadro-comparativo | 0.5 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-03__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **74** | `M1-u01-04` | linea-tiempo | 1 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-04__linea-tiempo__desarrollo-de-subtema__pp1.md) | ✓ |
| **76** | `M1-u01-05` | ilustracion | 0.5 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-05__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **80** | `M1-u01-06` | ilustracion | 0.5 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-06__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **84** | `M1-u01-07` | tabla-grande | 1 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-07__tabla-grande__desarrollo-de-subtema__pp1.md) | ✓ |
| **84** | `M1-u01-08` | ilustracion | 0.5 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-08__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **89** | `M1-u01-09` | infografia | 1 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-09__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **92** | `M1-u01-10` | ilustracion | 1 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-10__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **93** | `M1-u01-11` | cuadro-comparativo | 0.5 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-11__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **99** | `M1-u01-12` | cuadro-comparativo | 1 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-12__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **103** | `M1-u01-13` | infografia | 0.5 | u01 | desarrollo de subtema | [md](manual-1/sem-1/u01/M1-u01-13__infografia__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **126** | `M1-u01-14` | ilustracion | 0.5 | u01 | taller práctico | [md](manual-1/sem-1/u01/M1-u01-14__ilustracion__taller-pr-ctico__pp0p5.md) | ✓ |
| **134** | `M1-u02-01` | ilustracion | 1 | u02 | portadilla | [md](manual-1/sem-1/u02/M1-u02-01__ilustracion__portadilla__pp1.md) | ✓ |
| **134** | `M1-u02-02` | mapa-mental | 1 | u02 | mapa mental de unidad | [md](manual-1/sem-1/u02/M1-u02-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **138** | `M1-u02-03` | ilustracion | 0.5 | u02 | desarrollo de subtema | [md](manual-1/sem-1/u02/M1-u02-03__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **140** | `M1-u02-04` | ilustracion | 0.5 | u02 | desarrollo de subtema | [md](manual-1/sem-1/u02/M1-u02-04__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **144** | `M1-u02-05` | grafica | 0.5 | u02 | desarrollo de subtema | [md](manual-1/sem-1/u02/M1-u02-05__grafica__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **148** | `M1-u02-06` | infografia | 1 | u02 | desarrollo de subtema | [md](manual-1/sem-1/u02/M1-u02-06__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **152** | `M1-u02-07` | cuadro-comparativo | 1 | u02 | desarrollo de subtema | [md](manual-1/sem-1/u02/M1-u02-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **156** | `M1-u02-08` | infografia | 1 | u02 | desarrollo de subtema | [md](manual-1/sem-1/u02/M1-u02-08__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **158** | `M1-u02-09` | diagrama-flujo | 0.5 | u02 | desarrollo de subtema | [md](manual-1/sem-1/u02/M1-u02-09__diagrama-flujo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **185** | `M1-u02-10` | cuadro-comparativo | 0.5 | u02 | taller práctico | [md](manual-1/sem-1/u02/M1-u02-10__cuadro-comparativo__taller-pr-ctico__pp0p5.md) | ✓ |
| **192** | `M1-u03-01` | ilustracion | 1 | u03 | portadilla | [md](manual-1/sem-1/u03/M1-u03-01__ilustracion__portadilla__pp1.md) | ✓ |
| **193** | `M1-u03-02` | mapa-mental | 1 | u03 | mapa mental de unidad | [md](manual-1/sem-1/u03/M1-u03-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **195** | `M1-u03-03` | grafica | 0.5 | u03 | desarrollo de subtema | [md](manual-1/sem-1/u03/M1-u03-03__grafica__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **197** | `M1-u03-04` | cuadro-comparativo | 0.5 | u03 | desarrollo de subtema | [md](manual-1/sem-1/u03/M1-u03-04__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **204** | `M1-u03-05` | diagrama-flujo | 1 | u03 | desarrollo de subtema | [md](manual-1/sem-1/u03/M1-u03-05__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **209** | `M1-u03-06` | diagrama-flujo | 1 | u03 | desarrollo de subtema | [md](manual-1/sem-1/u03/M1-u03-06__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **213** | `M1-u03-07` | cuadro-comparativo | 1 | u03 | desarrollo de subtema | [md](manual-1/sem-1/u03/M1-u03-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **216** | `M1-u03-08` | ilustracion | 1 | u03 | desarrollo de subtema | [md](manual-1/sem-1/u03/M1-u03-08__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **242** | `M1-u03-09` | diagrama-flujo | 0.5 | u03 | taller práctico | [md](manual-1/sem-1/u03/M1-u03-09__diagrama-flujo__taller-pr-ctico__pp0p5.md) | ✓ |
| **250** | `M1-sem1-09` | ilustracion | 1 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-09__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **253** | `M1-sem1-10` | infografia | 1 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-10__infografia__contenido-del-manual__pp1.md) | ✓ |
| **255** | `M1-sem1-11` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-11__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **257** | `M1-sem1-12` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-12__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **258** | `M1-sem1-13` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-1/sem-1/sem1/M1-sem1-13__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |

### Semestre 2 — `dist/manual-1-sem-2.pdf`

| Pág PDF | ID | Tipo | pp | Unidad | Rol | Prompt | Imagen |
|---:|---|---|---:|---|---|---|---|
| **1** | `M1-sem2-01` | ilustracion | 1 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-01__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **1** | `M1-sem2-02` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-02__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **3** | `M1-sem2-03` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-03__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **5** | `M1-sem2-04` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-04__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **6** | `M1-sem2-05` | infografia | 1 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-05__infografia__contenido-del-manual__pp1.md) | ✓ |
| **8** | `M1-sem2-06` | linea-tiempo | 1 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-06__linea-tiempo__contenido-del-manual__pp1.md) | ✓ |
| **10** | `M1-sem2-07` | cuadro-comparativo | 1 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-07__cuadro-comparativo__contenido-del-manual__pp1.md) | ✓ |
| **13** | `M1-sem2-08` | grafica | 0.5 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-08__grafica__contenido-del-manual__pp0p5.md) | ✓ |
| **13** | `M1-u04-01` | ilustracion | 1 | u04 | portadilla | [md](manual-1/sem-2/u04/M1-u04-01__ilustracion__portadilla__pp1.md) | ✓ |
| **14** | `M1-u04-02` | mapa-mental | 1 | u04 | mapa mental de unidad | [md](manual-1/sem-2/u04/M1-u04-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **18** | `M1-u04-03` | ilustracion | 0.5 | u04 | desarrollo de subtema | [md](manual-1/sem-2/u04/M1-u04-03__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **21** | `M1-u04-04` | cuadro-comparativo | 0.5 | u04 | desarrollo de subtema | [md](manual-1/sem-2/u04/M1-u04-04__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **24** | `M1-u04-05` | ilustracion | 1 | u04 | desarrollo de subtema | [md](manual-1/sem-2/u04/M1-u04-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **28** | `M1-u04-06` | cuadro-comparativo | 0.5 | u04 | desarrollo de subtema | [md](manual-1/sem-2/u04/M1-u04-06__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **33** | `M1-u04-07` | infografia | 1 | u04 | desarrollo de subtema | [md](manual-1/sem-2/u04/M1-u04-07__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **60** | `M1-u04-08` | cuadro-comparativo | 0.5 | u04 | taller práctico | [md](manual-1/sem-2/u04/M1-u04-08__cuadro-comparativo__taller-pr-ctico__pp0p5.md) | ✓ |
| **67** | `M1-u05-01` | ilustracion | 1 | u05 | portadilla | [md](manual-1/sem-2/u05/M1-u05-01__ilustracion__portadilla__pp1.md) | ✓ |
| **67** | `M1-u05-02` | mapa-mental | 1 | u05 | mapa mental de unidad | [md](manual-1/sem-2/u05/M1-u05-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **73** | `M1-u05-03` | diagrama-flujo | 0.5 | u05 | desarrollo de subtema | [md](manual-1/sem-2/u05/M1-u05-03__diagrama-flujo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **77** | `M1-u05-04` | ilustracion | 0.5 | u05 | desarrollo de subtema | [md](manual-1/sem-2/u05/M1-u05-04__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **83** | `M1-u05-05` | grafica | 0.5 | u05 | desarrollo de subtema | [md](manual-1/sem-2/u05/M1-u05-05__grafica__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **88** | `M1-u05-06` | ilustracion | 0.5 | u05 | desarrollo de subtema | [md](manual-1/sem-2/u05/M1-u05-06__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **92** | `M1-u05-07` | diagrama-flujo | 1 | u05 | desarrollo de subtema | [md](manual-1/sem-2/u05/M1-u05-07__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **97** | `M1-u05-08` | ilustracion | 0.5 | u05 | desarrollo de subtema | [md](manual-1/sem-2/u05/M1-u05-08__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **103** | `M1-u05-09` | ilustracion | 0.5 | u05 | desarrollo de subtema | [md](manual-1/sem-2/u05/M1-u05-09__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **108** | `M1-u05-10` | infografia | 1 | u05 | desarrollo de subtema | [md](manual-1/sem-2/u05/M1-u05-10__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **134** | `M1-u05-11` | grafica | 0.5 | u05 | taller práctico | [md](manual-1/sem-2/u05/M1-u05-11__grafica__taller-pr-ctico__pp0p5.md) | ✓ |
| **142** | `M1-u06-01` | ilustracion | 1 | u06 | portadilla | [md](manual-1/sem-2/u06/M1-u06-01__ilustracion__portadilla__pp1.md) | ✓ |
| **142** | `M1-u06-02` | mapa-mental | 1 | u06 | mapa mental de unidad | [md](manual-1/sem-2/u06/M1-u06-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **146** | `M1-u06-03` | infografia | 1 | u06 | desarrollo de subtema | [md](manual-1/sem-2/u06/M1-u06-03__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **149** | `M1-u06-04` | cuadro-comparativo | 1 | u06 | desarrollo de subtema | [md](manual-1/sem-2/u06/M1-u06-04__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **152** | `M1-u06-05` | diagrama-flujo | 1 | u06 | desarrollo de subtema | [md](manual-1/sem-2/u06/M1-u06-05__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **156** | `M1-u06-06` | cuadro-comparativo | 1 | u06 | desarrollo de subtema | [md](manual-1/sem-2/u06/M1-u06-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **183** | `M1-u06-07` | cuadro-comparativo | 0.5 | u06 | taller práctico | [md](manual-1/sem-2/u06/M1-u06-07__cuadro-comparativo__taller-pr-ctico__pp0p5.md) | ✓ |
| **192** | `M1-sem2-09` | ilustracion | 1 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-09__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **196** | `M1-sem2-10` | infografia | 1 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-10__infografia__contenido-del-manual__pp1.md) | ✓ |
| **198** | `M1-sem2-11` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-11__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **200** | `M1-sem2-12` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-12__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **201** | `M1-sem2-13` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-1/sem-2/sem2/M1-sem2-13__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |

## Manual 2

### Semestre 1 — `dist/manual-2-sem-1.pdf`

| Pág PDF | ID | Tipo | pp | Unidad | Rol | Prompt | Imagen |
|---:|---|---|---:|---|---|---|---|
| **1** | `M2-sem1-01` | ilustracion | 1 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-01__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **1** | `M2-sem1-02` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-02__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **3** | `M2-sem1-03` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-03__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **4** | `M2-sem1-04` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-04__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **5** | `M2-sem1-05` | infografia | 1 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-05__infografia__contenido-del-manual__pp1.md) | ✓ |
| **7** | `M2-sem1-06` | linea-tiempo | 1 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-06__linea-tiempo__contenido-del-manual__pp1.md) | ✓ |
| **9** | `M2-sem1-07` | cuadro-comparativo | 1 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-07__cuadro-comparativo__contenido-del-manual__pp1.md) | ✓ |
| **11** | `M2-sem1-08` | grafica | 0.5 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-08__grafica__contenido-del-manual__pp0p5.md) | ✓ |
| **11** | `M2-u01-01` | ilustracion | 1 | u01 | portadilla | [md](manual-2/sem-1/u01/M2-u01-01__ilustracion__portadilla__pp1.md) | ✓ |
| **12** | `M2-u01-02` | mapa-mental | 1 | u01 | mapa mental de unidad | [md](manual-2/sem-1/u01/M2-u01-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **14** | `M2-u01-03` | cuadro-comparativo | 0.5 | u01 | desarrollo de subtema | [md](manual-2/sem-1/u01/M2-u01-03__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **19** | `M2-u01-04` | ilustracion | 0.5 | u01 | desarrollo de subtema | [md](manual-2/sem-1/u01/M2-u01-04__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **23** | `M2-u01-05` | grafica | 0.5 | u01 | desarrollo de subtema | [md](manual-2/sem-1/u01/M2-u01-05__grafica__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **29** | `M2-u01-06` | grafica | 1 | u01 | desarrollo de subtema | [md](manual-2/sem-1/u01/M2-u01-06__grafica__desarrollo-de-subtema__pp1.md) | ✓ |
| **33** | `M2-u01-07` | ilustracion | 0.5 | u01 | desarrollo de subtema | [md](manual-2/sem-1/u01/M2-u01-07__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **37** | `M2-u01-08` | ilustracion | 0.5 | u01 | desarrollo de subtema | [md](manual-2/sem-1/u01/M2-u01-08__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **41** | `M2-u01-09` | ilustracion | 0.5 | u01 | desarrollo de subtema | [md](manual-2/sem-1/u01/M2-u01-09__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **71** | `M2-u02-01` | ilustracion | 1 | u02 | portadilla | [md](manual-2/sem-1/u02/M2-u02-01__ilustracion__portadilla__pp1.md) | ✓ |
| **71** | `M2-u02-02` | mapa-mental | 1 | u02 | mapa mental de unidad | [md](manual-2/sem-1/u02/M2-u02-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **76** | `M2-u02-03` | ilustracion | 1 | u02 | desarrollo de subtema | [md](manual-2/sem-1/u02/M2-u02-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **79** | `M2-u02-04` | ilustracion | 0.5 | u02 | desarrollo de subtema | [md](manual-2/sem-1/u02/M2-u02-04__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **84** | `M2-u02-05` | cuadro-comparativo | 1 | u02 | desarrollo de subtema | [md](manual-2/sem-1/u02/M2-u02-05__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **87** | `M2-u02-06` | ilustracion | 0.5 | u02 | desarrollo de subtema | [md](manual-2/sem-1/u02/M2-u02-06__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **93** | `M2-u02-07` | ilustracion | 1 | u02 | desarrollo de subtema | [md](manual-2/sem-1/u02/M2-u02-07__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **98** | `M2-u02-08` | grafica | 0.5 | u02 | desarrollo de subtema | [md](manual-2/sem-1/u02/M2-u02-08__grafica__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **101** | `M2-u02-09` | ilustracion | 0.5 | u02 | desarrollo de subtema | [md](manual-2/sem-1/u02/M2-u02-09__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **105** | `M2-u02-10` | ilustracion | 0.5 | u02 | desarrollo de subtema | [md](manual-2/sem-1/u02/M2-u02-10__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **139** | `M2-u03-01` | ilustracion | 1 | u03 | portadilla | [md](manual-2/sem-1/u03/M2-u03-01__ilustracion__portadilla__pp1.md) | ✓ |
| **139** | `M2-u03-02` | mapa-mental | 1 | u03 | mapa mental de unidad | [md](manual-2/sem-1/u03/M2-u03-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **143** | `M2-u03-03` | ilustracion | 0.5 | u03 | desarrollo de subtema | [md](manual-2/sem-1/u03/M2-u03-03__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **146** | `M2-u03-04` | cuadro-comparativo | 0.5 | u03 | desarrollo de subtema | [md](manual-2/sem-1/u03/M2-u03-04__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **148** | `M2-u03-05` | grafica | 0.5 | u03 | desarrollo de subtema | [md](manual-2/sem-1/u03/M2-u03-05__grafica__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **152** | `M2-u03-06` | ilustracion | 0.5 | u03 | desarrollo de subtema | [md](manual-2/sem-1/u03/M2-u03-06__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **156** | `M2-u03-07` | ilustracion | 1 | u03 | desarrollo de subtema | [md](manual-2/sem-1/u03/M2-u03-07__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **161** | `M2-u03-08` | ilustracion | 0.5 | u03 | desarrollo de subtema | [md](manual-2/sem-1/u03/M2-u03-08__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **166** | `M2-u03-09` | cuadro-comparativo | 1 | u03 | desarrollo de subtema | [md](manual-2/sem-1/u03/M2-u03-09__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **170** | `M2-u03-10` | ilustracion | 0.5 | u03 | desarrollo de subtema | [md](manual-2/sem-1/u03/M2-u03-10__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **204** | `M2-u04-01` | ilustracion | 1 | u04 | portadilla | [md](manual-2/sem-1/u04/M2-u04-01__ilustracion__portadilla__pp1.md) | ✓ |
| **204** | `M2-u04-02` | mapa-mental | 1 | u04 | mapa mental de unidad | [md](manual-2/sem-1/u04/M2-u04-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **207** | `M2-u04-03` | cuadro-comparativo | 0.5 | u04 | desarrollo de subtema | [md](manual-2/sem-1/u04/M2-u04-03__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **209** | `M2-u04-04` | ilustracion | 0.5 | u04 | desarrollo de subtema | [md](manual-2/sem-1/u04/M2-u04-04__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **212** | `M2-u04-05` | grafica | 0.5 | u04 | desarrollo de subtema | [md](manual-2/sem-1/u04/M2-u04-05__grafica__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **216** | `M2-u04-06` | ilustracion | 0.5 | u04 | desarrollo de subtema | [md](manual-2/sem-1/u04/M2-u04-06__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **220** | `M2-u04-07` | cuadro-comparativo | 0.5 | u04 | desarrollo de subtema | [md](manual-2/sem-1/u04/M2-u04-07__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **223** | `M2-u04-08` | ilustracion | 1 | u04 | desarrollo de subtema | [md](manual-2/sem-1/u04/M2-u04-08__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **226** | `M2-u04-09` | grafica | 0.5 | u04 | desarrollo de subtema | [md](manual-2/sem-1/u04/M2-u04-09__grafica__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **229** | `M2-u04-10` | ilustracion | 1 | u04 | desarrollo de subtema | [md](manual-2/sem-1/u04/M2-u04-10__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **232** | `M2-u04-11` | ilustracion | 0.5 | u04 | desarrollo de subtema | [md](manual-2/sem-1/u04/M2-u04-11__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **263** | `M2-u05-01` | ilustracion | 1 | u05 | portadilla | [md](manual-2/sem-1/u05/M2-u05-01__ilustracion__portadilla__pp1.md) | ✓ |
| **264** | `M2-u05-02` | mapa-mental | 1 | u05 | mapa mental de unidad | [md](manual-2/sem-1/u05/M2-u05-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **266** | `M2-u05-03` | ilustracion | 0.5 | u05 | desarrollo de subtema | [md](manual-2/sem-1/u05/M2-u05-03__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **268** | `M2-u05-04` | ilustracion | 0.5 | u05 | desarrollo de subtema | [md](manual-2/sem-1/u05/M2-u05-04__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **271** | `M2-u05-05` | ilustracion | 0.5 | u05 | desarrollo de subtema | [md](manual-2/sem-1/u05/M2-u05-05__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **274** | `M2-u05-06` | ilustracion | 0.5 | u05 | desarrollo de subtema | [md](manual-2/sem-1/u05/M2-u05-06__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **277** | `M2-u05-07` | grafica | 0.5 | u05 | desarrollo de subtema | [md](manual-2/sem-1/u05/M2-u05-07__grafica__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **281** | `M2-u05-08` | ilustracion | 0.5 | u05 | desarrollo de subtema | [md](manual-2/sem-1/u05/M2-u05-08__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **314** | `M2-sem1-09` | ilustracion | 1 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-09__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **317** | `M2-sem1-10` | infografia | 1 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-10__infografia__contenido-del-manual__pp1.md) | ✓ |
| **319** | `M2-sem1-11` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-11__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **320** | `M2-sem1-12` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-12__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **321** | `M2-sem1-13` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-2/sem-1/sem1/M2-sem1-13__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |

### Semestre 2 — `dist/manual-2-sem-2.pdf`

| Pág PDF | ID | Tipo | pp | Unidad | Rol | Prompt | Imagen |
|---:|---|---|---:|---|---|---|---|
| **1** | `M2-sem2-01` | ilustracion | 1 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-01__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **1** | `M2-sem2-02` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-02__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **2** | `M2-sem2-03` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-03__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **4** | `M2-sem2-04` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-04__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **5** | `M2-sem2-05` | infografia | 1 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-05__infografia__contenido-del-manual__pp1.md) | ✓ |
| **6** | `M2-sem2-06` | linea-tiempo | 1 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-06__linea-tiempo__contenido-del-manual__pp1.md) | ✓ |
| **8** | `M2-sem2-07` | cuadro-comparativo | 1 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-07__cuadro-comparativo__contenido-del-manual__pp1.md) | ✓ |
| **10** | `M2-sem2-08` | grafica | 0.5 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-08__grafica__contenido-del-manual__pp0p5.md) | ✓ |
| **10** | `M2-u06-01` | ilustracion | 1 | u06 | portadilla | [md](manual-2/sem-2/u06/M2-u06-01__ilustracion__portadilla__pp1.md) | ✓ |
| **11** | `M2-u06-02` | mapa-mental | 1 | u06 | mapa mental de unidad | [md](manual-2/sem-2/u06/M2-u06-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **14** | `M2-u06-03` | ilustracion | 1 | u06 | desarrollo de subtema | [md](manual-2/sem-2/u06/M2-u06-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **17** | `M2-u06-04` | ilustracion | 1 | u06 | desarrollo de subtema | [md](manual-2/sem-2/u06/M2-u06-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **19** | `M2-u06-05` | ilustracion | 0.5 | u06 | desarrollo de subtema | [md](manual-2/sem-2/u06/M2-u06-05__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **21** | `M2-u06-06` | ilustracion | 0.5 | u06 | desarrollo de subtema | [md](manual-2/sem-2/u06/M2-u06-06__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **23** | `M2-u06-07` | cuadro-comparativo | 1 | u06 | desarrollo de subtema | [md](manual-2/sem-2/u06/M2-u06-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **25** | `M2-u06-08` | infografia | 1 | u06 | desarrollo de subtema | [md](manual-2/sem-2/u06/M2-u06-08__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **53** | `M2-u07-01` | ilustracion | 1 | u07 | portadilla | [md](manual-2/sem-2/u07/M2-u07-01__ilustracion__portadilla__pp1.md) | ✓ |
| **53** | `M2-u07-02` | mapa-mental | 1 | u07 | mapa mental de unidad | [md](manual-2/sem-2/u07/M2-u07-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **58** | `M2-u07-03` | ilustracion | 1 | u07 | desarrollo de subtema | [md](manual-2/sem-2/u07/M2-u07-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **59** | `M2-u07-04` | ilustracion | 0.5 | u07 | desarrollo de subtema | [md](manual-2/sem-2/u07/M2-u07-04__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **61** | `M2-u07-05` | infografia | 1 | u07 | desarrollo de subtema | [md](manual-2/sem-2/u07/M2-u07-05__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **63** | `M2-u07-06` | infografia | 1 | u07 | desarrollo de subtema | [md](manual-2/sem-2/u07/M2-u07-06__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **67** | `M2-u07-07` | ilustracion | 1 | u07 | desarrollo de subtema | [md](manual-2/sem-2/u07/M2-u07-07__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **70** | `M2-u07-08` | infografia | 1 | u07 | desarrollo de subtema | [md](manual-2/sem-2/u07/M2-u07-08__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **73** | `M2-u07-09` | ilustracion | 0.5 | u07 | desarrollo de subtema | [md](manual-2/sem-2/u07/M2-u07-09__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **112** | `M2-u08-01` | ilustracion | 1 | u08 | portadilla | [md](manual-2/sem-2/u08/M2-u08-01__ilustracion__portadilla__pp1.md) | ✓ |
| **113** | `M2-u08-02` | mapa-mental | 1 | u08 | mapa mental de unidad | [md](manual-2/sem-2/u08/M2-u08-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **117** | `M2-u08-03` | ilustracion | 0.5 | u08 | desarrollo de subtema | [md](manual-2/sem-2/u08/M2-u08-03__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **118** | `M2-u08-04` | infografia | 0.5 | u08 | desarrollo de subtema | [md](manual-2/sem-2/u08/M2-u08-04__infografia__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **121** | `M2-u08-05` | ilustracion | 1 | u08 | desarrollo de subtema | [md](manual-2/sem-2/u08/M2-u08-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **123** | `M2-u08-06` | infografia | 1 | u08 | desarrollo de subtema | [md](manual-2/sem-2/u08/M2-u08-06__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **126** | `M2-u08-07` | ilustracion | 1 | u08 | desarrollo de subtema | [md](manual-2/sem-2/u08/M2-u08-07__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **128** | `M2-u08-08` | infografia | 1 | u08 | desarrollo de subtema | [md](manual-2/sem-2/u08/M2-u08-08__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **131** | `M2-u08-09` | ilustracion | 1 | u08 | desarrollo de subtema | [md](manual-2/sem-2/u08/M2-u08-09__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **133** | `M2-u08-10` | ilustracion | 0.5 | u08 | desarrollo de subtema | [md](manual-2/sem-2/u08/M2-u08-10__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **134** | `M2-u08-11` | infografia | 1 | u08 | desarrollo de subtema | [md](manual-2/sem-2/u08/M2-u08-11__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **175** | `M2-u09-01` | ilustracion | 1 | u09 | portadilla | [md](manual-2/sem-2/u09/M2-u09-01__ilustracion__portadilla__pp1.md) | ✓ |
| **176** | `M2-u09-02` | mapa-mental | 1 | u09 | mapa mental de unidad | [md](manual-2/sem-2/u09/M2-u09-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **178** | `M2-u09-03` | linea-tiempo | 1 | u09 | desarrollo de subtema | [md](manual-2/sem-2/u09/M2-u09-03__linea-tiempo__desarrollo-de-subtema__pp1.md) | ✓ |
| **179** | `M2-u09-04` | ilustracion | 0.5 | u09 | desarrollo de subtema | [md](manual-2/sem-2/u09/M2-u09-04__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **180** | `M2-u09-05` | infografia | 1 | u09 | desarrollo de subtema | [md](manual-2/sem-2/u09/M2-u09-05__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **185** | `M2-u09-06` | ilustracion | 1 | u09 | desarrollo de subtema | [md](manual-2/sem-2/u09/M2-u09-06__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **187** | `M2-u09-07` | ilustracion | 0.5 | u09 | desarrollo de subtema | [md](manual-2/sem-2/u09/M2-u09-07__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **188** | `M2-u09-08` | ilustracion | 0.5 | u09 | desarrollo de subtema | [md](manual-2/sem-2/u09/M2-u09-08__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **189** | `M2-u09-09` | grafica | 1 | u09 | desarrollo de subtema | [md](manual-2/sem-2/u09/M2-u09-09__grafica__desarrollo-de-subtema__pp1.md) | ✓ |
| **194** | `M2-u09-10` | infografia | 1 | u09 | desarrollo de subtema | [md](manual-2/sem-2/u09/M2-u09-10__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **195** | `M2-u09-11` | cuadro-comparativo | 1 | u09 | desarrollo de subtema | [md](manual-2/sem-2/u09/M2-u09-11__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **195** | `M2-u09-12` | diagrama-flujo | 1 | u09 | desarrollo de subtema | [md](manual-2/sem-2/u09/M2-u09-12__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **227** | `M2-sem2-09` | ilustracion | 1 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-09__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **229** | `M2-sem2-10` | infografia | 1 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-10__infografia__contenido-del-manual__pp1.md) | ✓ |
| **231** | `M2-sem2-11` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-11__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **232** | `M2-sem2-12` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-12__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **233** | `M2-sem2-13` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-2/sem-2/sem2/M2-sem2-13__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |

## Manual 3

### Semestre 1 — `dist/manual-3-sem-1.pdf`

| Pág PDF | ID | Tipo | pp | Unidad | Rol | Prompt | Imagen |
|---:|---|---|---:|---|---|---|---|
| **1** | `M3-sem1-01` | ilustracion | 1 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-01__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **2** | `M3-sem1-02` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-02__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **3** | `M3-sem1-03` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-03__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **6** | `M3-sem1-04` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-04__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **7** | `M3-sem1-05` | infografia | 1 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-05__infografia__contenido-del-manual__pp1.md) | ✓ |
| **10** | `M3-sem1-06` | linea-tiempo | 1 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-06__linea-tiempo__contenido-del-manual__pp1.md) | ✓ |
| **12** | `M3-sem1-07` | cuadro-comparativo | 1 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-07__cuadro-comparativo__contenido-del-manual__pp1.md) | ✓ |
| **15** | `M3-sem1-08` | grafica | 0.5 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-08__grafica__contenido-del-manual__pp0p5.md) | ✓ |
| **16** | `M3-u01-01` | ilustracion | 1 | u01 | portadilla | [md](manual-3/sem-1/u01/M3-u01-01__ilustracion__portadilla__pp1.md) | ✓ |
| **17** | `M3-u01-02` | mapa-mental | 1 | u01 | mapa mental de unidad | [md](manual-3/sem-1/u01/M3-u01-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **20** | `M3-u01-03` | cuadro-comparativo | 1 | u01 | desarrollo de subtema | [md](manual-3/sem-1/u01/M3-u01-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **22** | `M3-u01-04` | infografia | 1 | u01 | desarrollo de subtema | [md](manual-3/sem-1/u01/M3-u01-04__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **26** | `M3-u01-05` | ilustracion | 1 | u01 | desarrollo de subtema | [md](manual-3/sem-1/u01/M3-u01-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **29** | `M3-u01-06` | infografia | 1 | u01 | desarrollo de subtema | [md](manual-3/sem-1/u01/M3-u01-06__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **32** | `M3-u01-07` | ilustracion | 0.5 | u01 | desarrollo de subtema | [md](manual-3/sem-1/u01/M3-u01-07__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **35** | `M3-u01-08` | cuadro-comparativo | 1 | u01 | desarrollo de subtema | [md](manual-3/sem-1/u01/M3-u01-08__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **67** | `M3-u02-01` | ilustracion | 1 | u02 | portadilla | [md](manual-3/sem-1/u02/M3-u02-01__ilustracion__portadilla__pp1.md) | ✓ |
| **68** | `M3-u02-02` | mapa-mental | 1 | u02 | mapa mental de unidad | [md](manual-3/sem-1/u02/M3-u02-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **70** | `M3-u02-03` | infografia | 1 | u02 | desarrollo de subtema | [md](manual-3/sem-1/u02/M3-u02-03__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **72** | `M3-u02-04` | ilustracion | 0.5 | u02 | desarrollo de subtema | [md](manual-3/sem-1/u02/M3-u02-04__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **76** | `M3-u02-05` | interfaz | 1 | u02 | desarrollo de subtema | [md](manual-3/sem-1/u02/M3-u02-05__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **80** | `M3-u02-06` | interfaz | 1 | u02 | desarrollo de subtema | [md](manual-3/sem-1/u02/M3-u02-06__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **82** | `M3-u02-07` | interfaz | 1 | u02 | desarrollo de subtema | [md](manual-3/sem-1/u02/M3-u02-07__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **85** | `M3-u02-08` | interfaz | 1 | u02 | desarrollo de subtema | [md](manual-3/sem-1/u02/M3-u02-08__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **87** | `M3-u02-09` | cuadro-comparativo | 1 | u02 | desarrollo de subtema | [md](manual-3/sem-1/u02/M3-u02-09__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **88** | `M3-u02-10` | ilustracion | 0.5 | u02 | desarrollo de subtema | [md](manual-3/sem-1/u02/M3-u02-10__ilustracion__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **94** | `M3-u02-11` | infografia | 1 | u02 | desarrollo de subtema | [md](manual-3/sem-1/u02/M3-u02-11__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **131** | `M3-u03-01` | ilustracion | 1 | u03 | portadilla | [md](manual-3/sem-1/u03/M3-u03-01__ilustracion__portadilla__pp1.md) | ✓ |
| **131** | `M3-u03-02` | mapa-mental | 1 | u03 | mapa mental de unidad | [md](manual-3/sem-1/u03/M3-u03-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **135** | `M3-u03-03` | infografia | 1 | u03 | desarrollo de subtema | [md](manual-3/sem-1/u03/M3-u03-03__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **136** | `M3-u03-04` | cuadro-comparativo | 1 | u03 | desarrollo de subtema | [md](manual-3/sem-1/u03/M3-u03-04__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **139** | `M3-u03-05` | ilustracion | 1 | u03 | desarrollo de subtema | [md](manual-3/sem-1/u03/M3-u03-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **141** | `M3-u03-06` | ilustracion | 1 | u03 | desarrollo de subtema | [md](manual-3/sem-1/u03/M3-u03-06__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **143** | `M3-u03-07` | infografia | 1 | u03 | desarrollo de subtema | [md](manual-3/sem-1/u03/M3-u03-07__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **145** | `M3-u03-08` | cuadro-comparativo | 0.5 | u03 | desarrollo de subtema | [md](manual-3/sem-1/u03/M3-u03-08__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md) | ✓ |
| **147** | `M3-u03-09` | diagrama-flujo | 1 | u03 | desarrollo de subtema | [md](manual-3/sem-1/u03/M3-u03-09__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **151** | `M3-u03-10` | cuadro-comparativo | 1 | u03 | desarrollo de subtema | [md](manual-3/sem-1/u03/M3-u03-10__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **187** | `M3-u04-01` | ilustracion | 1 | u04 | portadilla | [md](manual-3/sem-1/u04/M3-u04-01__ilustracion__portadilla__pp1.md) | ✓ |
| **187** | `M3-u04-02` | mapa-mental | 1 | u04 | mapa mental de unidad | [md](manual-3/sem-1/u04/M3-u04-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **190** | `M3-u04-03` | cuadro-comparativo | 1 | u04 | desarrollo de subtema | [md](manual-3/sem-1/u04/M3-u04-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **191** | `M3-u04-04` | infografia | 1 | u04 | desarrollo de subtema | [md](manual-3/sem-1/u04/M3-u04-04__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **196** | `M3-u04-05` | cuadro-comparativo | 1 | u04 | desarrollo de subtema | [md](manual-3/sem-1/u04/M3-u04-05__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **200** | `M3-u04-06` | cuadro-comparativo | 1 | u04 | desarrollo de subtema | [md](manual-3/sem-1/u04/M3-u04-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **204** | `M3-u04-07` | ilustracion | 1 | u04 | desarrollo de subtema | [md](manual-3/sem-1/u04/M3-u04-07__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **239** | `M3-u05-01` | ilustracion | 1 | u05 | portadilla | [md](manual-3/sem-1/u05/M3-u05-01__ilustracion__portadilla__pp1.md) | ✓ |
| **240** | `M3-u05-02` | mapa-mental | 1 | u05 | mapa mental de unidad | [md](manual-3/sem-1/u05/M3-u05-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **243** | `M3-u05-03` | interfaz | 1 | u05 | desarrollo de subtema | [md](manual-3/sem-1/u05/M3-u05-03__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **244** | `M3-u05-04` | ilustracion | 1 | u05 | desarrollo de subtema | [md](manual-3/sem-1/u05/M3-u05-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **248** | `M3-u05-05` | interfaz | 1 | u05 | desarrollo de subtema | [md](manual-3/sem-1/u05/M3-u05-05__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **251** | `M3-u05-06` | interfaz | 1 | u05 | desarrollo de subtema | [md](manual-3/sem-1/u05/M3-u05-06__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **255** | `M3-u05-07` | interfaz | 1 | u05 | desarrollo de subtema | [md](manual-3/sem-1/u05/M3-u05-07__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **259** | `M3-u05-08` | interfaz | 1 | u05 | desarrollo de subtema | [md](manual-3/sem-1/u05/M3-u05-08__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **263** | `M3-u05-09` | cuadro-comparativo | 1 | u05 | desarrollo de subtema | [md](manual-3/sem-1/u05/M3-u05-09__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **296** | `M3-sem1-09` | ilustracion | 1 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-09__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **300** | `M3-sem1-10` | infografia | 1 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-10__infografia__contenido-del-manual__pp1.md) | ✓ |
| **303** | `M3-sem1-11` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-11__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **305** | `M3-sem1-12` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-12__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **306** | `M3-sem1-13` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-3/sem-1/sem1/M3-sem1-13__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |

### Semestre 2 — `dist/manual-3-sem-2.pdf`

| Pág PDF | ID | Tipo | pp | Unidad | Rol | Prompt | Imagen |
|---:|---|---|---:|---|---|---|---|
| **1** | `M3-sem2-01` | ilustracion | 1 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-01__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **2** | `M3-sem2-02` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-02__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **3** | `M3-sem2-03` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-03__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **6** | `M3-sem2-04` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-04__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **7** | `M3-sem2-05` | infografia | 1 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-05__infografia__contenido-del-manual__pp1.md) | ✓ |
| **10** | `M3-sem2-06` | linea-tiempo | 1 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-06__linea-tiempo__contenido-del-manual__pp1.md) | ✓ |
| **12** | `M3-sem2-07` | cuadro-comparativo | 1 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-07__cuadro-comparativo__contenido-del-manual__pp1.md) | ✓ |
| **15** | `M3-sem2-08` | grafica | 0.5 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-08__grafica__contenido-del-manual__pp0p5.md) | ✓ |
| **16** | `M3-u06-01` | ilustracion | 1 | u06 | portadilla | [md](manual-3/sem-2/u06/M3-u06-01__ilustracion__portadilla__pp1.md) | ✓ |
| **16** | `M3-u06-02` | mapa-mental | 1 | u06 | mapa mental de unidad | [md](manual-3/sem-2/u06/M3-u06-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **20** | `M3-u06-03` | interfaz | 1 | u06 | desarrollo de subtema | [md](manual-3/sem-2/u06/M3-u06-03__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **24** | `M3-u06-04` | interfaz | 1 | u06 | desarrollo de subtema | [md](manual-3/sem-2/u06/M3-u06-04__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **28** | `M3-u06-05` | interfaz | 1 | u06 | desarrollo de subtema | [md](manual-3/sem-2/u06/M3-u06-05__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **33** | `M3-u06-06` | interfaz | 1 | u06 | desarrollo de subtema | [md](manual-3/sem-2/u06/M3-u06-06__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **37** | `M3-u06-07` | interfaz | 1 | u06 | desarrollo de subtema | [md](manual-3/sem-2/u06/M3-u06-07__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **41** | `M3-u06-08` | interfaz | 1 | u06 | desarrollo de subtema | [md](manual-3/sem-2/u06/M3-u06-08__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **75** | `M3-u07-01` | ilustracion | 1 | u07 | portadilla | [md](manual-3/sem-2/u07/M3-u07-01__ilustracion__portadilla__pp1.md) | ✓ |
| **75** | `M3-u07-02` | mapa-mental | 1 | u07 | mapa mental de unidad | [md](manual-3/sem-2/u07/M3-u07-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **78** | `M3-u07-03` | ilustracion | 1 | u07 | desarrollo de subtema | [md](manual-3/sem-2/u07/M3-u07-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **83** | `M3-u07-04` | interfaz | 1 | u07 | desarrollo de subtema | [md](manual-3/sem-2/u07/M3-u07-04__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **86** | `M3-u07-05` | interfaz | 1 | u07 | desarrollo de subtema | [md](manual-3/sem-2/u07/M3-u07-05__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **90** | `M3-u07-06` | interfaz | 1 | u07 | desarrollo de subtema | [md](manual-3/sem-2/u07/M3-u07-06__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **95** | `M3-u07-07` | cuadro-comparativo | 1 | u07 | desarrollo de subtema | [md](manual-3/sem-2/u07/M3-u07-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **134** | `M3-u08-01` | ilustracion | 1 | u08 | portadilla | [md](manual-3/sem-2/u08/M3-u08-01__ilustracion__portadilla__pp1.md) | ✓ |
| **134** | `M3-u08-02` | mapa-mental | 1 | u08 | mapa mental de unidad | [md](manual-3/sem-2/u08/M3-u08-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **138** | `M3-u08-03` | cuadro-comparativo | 1 | u08 | desarrollo de subtema | [md](manual-3/sem-2/u08/M3-u08-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **141** | `M3-u08-04` | ilustracion | 1 | u08 | desarrollo de subtema | [md](manual-3/sem-2/u08/M3-u08-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **144** | `M3-u08-05` | interfaz | 1 | u08 | desarrollo de subtema | [md](manual-3/sem-2/u08/M3-u08-05__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **147** | `M3-u08-06` | interfaz | 1 | u08 | desarrollo de subtema | [md](manual-3/sem-2/u08/M3-u08-06__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **150** | `M3-u08-07` | ilustracion | 1 | u08 | desarrollo de subtema | [md](manual-3/sem-2/u08/M3-u08-07__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **153** | `M3-u08-08` | diagrama-flujo | 1 | u08 | desarrollo de subtema | [md](manual-3/sem-2/u08/M3-u08-08__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **189** | `M3-u09-01` | ilustracion | 1 | u09 | portadilla | [md](manual-3/sem-2/u09/M3-u09-01__ilustracion__portadilla__pp1.md) | ✓ |
| **190** | `M3-u09-02` | mapa-mental | 1 | u09 | mapa mental de unidad | [md](manual-3/sem-2/u09/M3-u09-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **194** | `M3-u09-03` | cuadro-comparativo | 1 | u09 | desarrollo de subtema | [md](manual-3/sem-2/u09/M3-u09-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **196** | `M3-u09-04` | infografia | 1 | u09 | desarrollo de subtema | [md](manual-3/sem-2/u09/M3-u09-04__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **200** | `M3-u09-05` | cuadro-comparativo | 1 | u09 | desarrollo de subtema | [md](manual-3/sem-2/u09/M3-u09-05__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **203** | `M3-u09-06` | infografia | 1 | u09 | desarrollo de subtema | [md](manual-3/sem-2/u09/M3-u09-06__infografia__desarrollo-de-subtema__pp1.md) | ✓ |
| **207** | `M3-u09-07` | cuadro-comparativo | 1 | u09 | desarrollo de subtema | [md](manual-3/sem-2/u09/M3-u09-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **211** | `M3-u09-08` | linea-tiempo | 1 | u09 | desarrollo de subtema | [md](manual-3/sem-2/u09/M3-u09-08__linea-tiempo__desarrollo-de-subtema__pp1.md) | ✓ |
| **245** | `M3-sem2-09` | ilustracion | 1 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-09__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **249** | `M3-sem2-10` | infografia | 1 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-10__infografia__contenido-del-manual__pp1.md) | ✓ |
| **252** | `M3-sem2-11` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-11__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **254** | `M3-sem2-12` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-12__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **255** | `M3-sem2-13` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-3/sem-2/sem2/M3-sem2-13__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |

## Manual 4

### Semestre 1 — `dist/manual-4-sem-1.pdf`

| Pág PDF | ID | Tipo | pp | Unidad | Rol | Prompt | Imagen |
|---:|---|---|---:|---|---|---|---|
| **1** | `M4-sem1-01` | ilustracion | 1 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-01__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **2** | `M4-sem1-02` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-02__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **5** | `M4-sem1-03` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-03__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **8** | `M4-sem1-04` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-04__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **10** | `M4-sem1-05` | infografia | 1 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-05__infografia__contenido-del-manual__pp1.md) | ✓ |
| **13** | `M4-sem1-06` | linea-tiempo | 1 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-06__linea-tiempo__contenido-del-manual__pp1.md) | ✓ |
| **16** | `M4-sem1-07` | cuadro-comparativo | 1 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-07__cuadro-comparativo__contenido-del-manual__pp1.md) | ✓ |
| **19** | `M4-sem1-08` | grafica | 0.5 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-08__grafica__contenido-del-manual__pp0p5.md) | ✓ |
| **21** | `M4-u01-01` | ilustracion | 1 | u01 | portadilla | [md](manual-4/sem-1/u01/M4-u01-01__ilustracion__portadilla__pp1.md) | ✓ |
| **22** | `M4-u01-02` | mapa-mental | 1 | u01 | mapa mental de unidad | [md](manual-4/sem-1/u01/M4-u01-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **31** | `M4-u01-03` | ilustracion | 1 | u01 | desarrollo de subtema | [md](manual-4/sem-1/u01/M4-u01-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **34** | `M4-u01-04` | diagrama-flujo | 1 | u01 | desarrollo de subtema | [md](manual-4/sem-1/u01/M4-u01-04__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **40** | `M4-u01-05` | diagrama-flujo | 1 | u01 | desarrollo de subtema | [md](manual-4/sem-1/u01/M4-u01-05__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **44** | `M4-u01-06` | ilustracion | 1 | u01 | desarrollo de subtema | [md](manual-4/sem-1/u01/M4-u01-06__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **48** | `M4-u01-07` | diagrama-flujo | 1 | u01 | desarrollo de subtema | [md](manual-4/sem-1/u01/M4-u01-07__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **54** | `M4-u01-08` | ilustracion | 1 | u01 | desarrollo de subtema | [md](manual-4/sem-1/u01/M4-u01-08__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **58** | `M4-u01-09` | cuadro-comparativo | 1 | u01 | desarrollo de subtema | [md](manual-4/sem-1/u01/M4-u01-09__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **62** | `M4-u01-10` | cuadro-comparativo | 1 | u01 | desarrollo de subtema | [md](manual-4/sem-1/u01/M4-u01-10__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **98** | `M4-u02-01` | ilustracion | 1 | u02 | portadilla | [md](manual-4/sem-1/u02/M4-u02-01__ilustracion__portadilla__pp1.md) | ✓ |
| **100** | `M4-u02-02` | mapa-mental | 1 | u02 | mapa mental de unidad | [md](manual-4/sem-1/u02/M4-u02-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **107** | `M4-u02-03` | ilustracion | 1 | u02 | desarrollo de subtema | [md](manual-4/sem-1/u02/M4-u02-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **112** | `M4-u02-04` | cuadro-comparativo | 1 | u02 | desarrollo de subtema | [md](manual-4/sem-1/u02/M4-u02-04__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **116** | `M4-u02-05` | ilustracion | 1 | u02 | desarrollo de subtema | [md](manual-4/sem-1/u02/M4-u02-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **120** | `M4-u02-06` | ilustracion | 1 | u02 | desarrollo de subtema | [md](manual-4/sem-1/u02/M4-u02-06__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **126** | `M4-u02-07` | diagrama-flujo | 1 | u02 | desarrollo de subtema | [md](manual-4/sem-1/u02/M4-u02-07__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **131** | `M4-u02-08` | ilustracion | 1 | u02 | desarrollo de subtema | [md](manual-4/sem-1/u02/M4-u02-08__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **164** | `M4-u03-01` | ilustracion | 1 | u03 | portadilla | [md](manual-4/sem-1/u03/M4-u03-01__ilustracion__portadilla__pp1.md) | ✓ |
| **166** | `M4-u03-02` | mapa-mental | 1 | u03 | mapa mental de unidad | [md](manual-4/sem-1/u03/M4-u03-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **172** | `M4-u03-03` | cuadro-comparativo | 1 | u03 | desarrollo de subtema | [md](manual-4/sem-1/u03/M4-u03-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **177** | `M4-u03-04` | interfaz | 1 | u03 | desarrollo de subtema | [md](manual-4/sem-1/u03/M4-u03-04__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **179** | `M4-u03-05` | diagrama-flujo | 1 | u03 | desarrollo de subtema | [md](manual-4/sem-1/u03/M4-u03-05__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **185** | `M4-u03-06` | cuadro-comparativo | 1 | u03 | desarrollo de subtema | [md](manual-4/sem-1/u03/M4-u03-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **191** | `M4-u03-07` | ilustracion | 1 | u03 | desarrollo de subtema | [md](manual-4/sem-1/u03/M4-u03-07__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **196** | `M4-u03-08` | cuadro-comparativo | 1 | u03 | desarrollo de subtema | [md](manual-4/sem-1/u03/M4-u03-08__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **201** | `M4-u03-09` | diagrama-flujo | 1 | u03 | desarrollo de subtema | [md](manual-4/sem-1/u03/M4-u03-09__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **236** | `M4-u04-01` | ilustracion | 1 | u04 | portadilla | [md](manual-4/sem-1/u04/M4-u04-01__ilustracion__portadilla__pp1.md) | ✓ |
| **237** | `M4-u04-02` | mapa-mental | 1 | u04 | mapa mental de unidad | [md](manual-4/sem-1/u04/M4-u04-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **245** | `M4-u04-03` | diagrama-flujo | 1 | u04 | desarrollo de subtema | [md](manual-4/sem-1/u04/M4-u04-03__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **250** | `M4-u04-04` | ilustracion | 1 | u04 | desarrollo de subtema | [md](manual-4/sem-1/u04/M4-u04-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **255** | `M4-u04-05` | cuadro-comparativo | 1 | u04 | desarrollo de subtema | [md](manual-4/sem-1/u04/M4-u04-05__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **261** | `M4-u04-06` | cuadro-comparativo | 1 | u04 | desarrollo de subtema | [md](manual-4/sem-1/u04/M4-u04-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **262** | `M4-u04-07` | interfaz | 1 | u04 | desarrollo de subtema | [md](manual-4/sem-1/u04/M4-u04-07__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **267** | `M4-u04-08` | ilustracion | 1 | u04 | desarrollo de subtema | [md](manual-4/sem-1/u04/M4-u04-08__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **272** | `M4-u04-09` | cuadro-comparativo | 1 | u04 | desarrollo de subtema | [md](manual-4/sem-1/u04/M4-u04-09__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **311** | `M4-u05-01` | ilustracion | 1 | u05 | portadilla | [md](manual-4/sem-1/u05/M4-u05-01__ilustracion__portadilla__pp1.md) | ✓ |
| **312** | `M4-u05-02` | mapa-mental | 1 | u05 | mapa mental de unidad | [md](manual-4/sem-1/u05/M4-u05-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **320** | `M4-u05-03` | interfaz | 1 | u05 | desarrollo de subtema | [md](manual-4/sem-1/u05/M4-u05-03__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **325** | `M4-u05-04` | interfaz | 1 | u05 | desarrollo de subtema | [md](manual-4/sem-1/u05/M4-u05-04__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **330** | `M4-u05-05` | ilustracion | 1 | u05 | desarrollo de subtema | [md](manual-4/sem-1/u05/M4-u05-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **334** | `M4-u05-06` | interfaz | 1 | u05 | desarrollo de subtema | [md](manual-4/sem-1/u05/M4-u05-06__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **339** | `M4-u05-07` | diagrama-flujo | 1 | u05 | desarrollo de subtema | [md](manual-4/sem-1/u05/M4-u05-07__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **345** | `M4-u05-08` | cuadro-comparativo | 1 | u05 | desarrollo de subtema | [md](manual-4/sem-1/u05/M4-u05-08__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **350** | `M4-u05-09` | cuadro-comparativo | 1 | u05 | desarrollo de subtema | [md](manual-4/sem-1/u05/M4-u05-09__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **386** | `M4-sem1-09` | ilustracion | 1 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-09__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **390** | `M4-sem1-10` | infografia | 1 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-10__infografia__contenido-del-manual__pp1.md) | ✓ |
| **393** | `M4-sem1-11` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-11__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **396** | `M4-sem1-12` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-12__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **398** | `M4-sem1-13` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-4/sem-1/sem1/M4-sem1-13__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |

### Semestre 2 — `dist/manual-4-sem-2.pdf`

| Pág PDF | ID | Tipo | pp | Unidad | Rol | Prompt | Imagen |
|---:|---|---|---:|---|---|---|---|
| **1** | `M4-sem2-01` | ilustracion | 1 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-01__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **2** | `M4-sem2-02` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-02__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **5** | `M4-sem2-03` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-03__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **8** | `M4-sem2-04` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-04__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **10** | `M4-sem2-05` | infografia | 1 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-05__infografia__contenido-del-manual__pp1.md) | ✓ |
| **14** | `M4-sem2-06` | linea-tiempo | 1 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-06__linea-tiempo__contenido-del-manual__pp1.md) | ✓ |
| **17** | `M4-sem2-07` | cuadro-comparativo | 1 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-07__cuadro-comparativo__contenido-del-manual__pp1.md) | ✓ |
| **20** | `M4-sem2-08` | grafica | 0.5 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-08__grafica__contenido-del-manual__pp0p5.md) | ✓ |
| **22** | `M4-u06-01` | ilustracion | 1 | u06 | portadilla | [md](manual-4/sem-2/u06/M4-u06-01__ilustracion__portadilla__pp1.md) | ✓ |
| **23** | `M4-u06-02` | mapa-mental | 1 | u06 | mapa mental de unidad | [md](manual-4/sem-2/u06/M4-u06-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **30** | `M4-u06-03` | cuadro-comparativo | 1 | u06 | desarrollo de subtema | [md](manual-4/sem-2/u06/M4-u06-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **37** | `M4-u06-04` | ilustracion | 1 | u06 | desarrollo de subtema | [md](manual-4/sem-2/u06/M4-u06-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **41** | `M4-u06-05` | ilustracion | 1 | u06 | desarrollo de subtema | [md](manual-4/sem-2/u06/M4-u06-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **48** | `M4-u06-06` | cuadro-comparativo | 1 | u06 | desarrollo de subtema | [md](manual-4/sem-2/u06/M4-u06-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **53** | `M4-u06-07` | diagrama-flujo | 1 | u06 | desarrollo de subtema | [md](manual-4/sem-2/u06/M4-u06-07__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **59** | `M4-u06-08` | cuadro-comparativo | 1 | u06 | desarrollo de subtema | [md](manual-4/sem-2/u06/M4-u06-08__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **99** | `M4-u07-01` | ilustracion | 1 | u07 | portadilla | [md](manual-4/sem-2/u07/M4-u07-01__ilustracion__portadilla__pp1.md) | ✓ |
| **101** | `M4-u07-02` | mapa-mental | 1 | u07 | mapa mental de unidad | [md](manual-4/sem-2/u07/M4-u07-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **108** | `M4-u07-03` | cuadro-comparativo | 1 | u07 | desarrollo de subtema | [md](manual-4/sem-2/u07/M4-u07-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **112** | `M4-u07-04` | interfaz | 1 | u07 | desarrollo de subtema | [md](manual-4/sem-2/u07/M4-u07-04__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **117** | `M4-u07-05` | interfaz | 1 | u07 | desarrollo de subtema | [md](manual-4/sem-2/u07/M4-u07-05__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **121** | `M4-u07-06` | cuadro-comparativo | 1 | u07 | desarrollo de subtema | [md](manual-4/sem-2/u07/M4-u07-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **125** | `M4-u07-07` | cuadro-comparativo | 1 | u07 | desarrollo de subtema | [md](manual-4/sem-2/u07/M4-u07-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **130** | `M4-u07-08` | cuadro-comparativo | 1 | u07 | desarrollo de subtema | [md](manual-4/sem-2/u07/M4-u07-08__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **135** | `M4-u07-09` | diagrama-flujo | 1 | u07 | desarrollo de subtema | [md](manual-4/sem-2/u07/M4-u07-09__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **176** | `M4-u08-01` | ilustracion | 1 | u08 | portadilla | [md](manual-4/sem-2/u08/M4-u08-01__ilustracion__portadilla__pp1.md) | ✓ |
| **177** | `M4-u08-02` | mapa-mental | 1 | u08 | mapa mental de unidad | [md](manual-4/sem-2/u08/M4-u08-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **184** | `M4-u08-03` | diagrama-flujo | 1 | u08 | desarrollo de subtema | [md](manual-4/sem-2/u08/M4-u08-03__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **190** | `M4-u08-04` | cuadro-comparativo | 1 | u08 | desarrollo de subtema | [md](manual-4/sem-2/u08/M4-u08-04__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **194** | `M4-u08-05` | interfaz | 1 | u08 | desarrollo de subtema | [md](manual-4/sem-2/u08/M4-u08-05__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **200** | `M4-u08-06` | cuadro-comparativo | 1 | u08 | desarrollo de subtema | [md](manual-4/sem-2/u08/M4-u08-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **205** | `M4-u08-07` | ilustracion | 1 | u08 | desarrollo de subtema | [md](manual-4/sem-2/u08/M4-u08-07__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **235** | `M4-u09-01` | ilustracion | 1 | u09 | portadilla | [md](manual-4/sem-2/u09/M4-u09-01__ilustracion__portadilla__pp1.md) | ✓ |
| **237** | `M4-u09-02` | mapa-mental | 1 | u09 | mapa mental de unidad | [md](manual-4/sem-2/u09/M4-u09-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **245** | `M4-u09-03` | cuadro-comparativo | 1 | u09 | desarrollo de subtema | [md](manual-4/sem-2/u09/M4-u09-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **249** | `M4-u09-04` | ilustracion | 1 | u09 | desarrollo de subtema | [md](manual-4/sem-2/u09/M4-u09-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **255** | `M4-u09-05` | cuadro-comparativo | 1 | u09 | desarrollo de subtema | [md](manual-4/sem-2/u09/M4-u09-05__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **259** | `M4-u09-06` | cuadro-comparativo | 1 | u09 | desarrollo de subtema | [md](manual-4/sem-2/u09/M4-u09-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **264** | `M4-u09-07` | cuadro-comparativo | 1 | u09 | desarrollo de subtema | [md](manual-4/sem-2/u09/M4-u09-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **269** | `M4-u09-08` | ilustracion | 1 | u09 | desarrollo de subtema | [md](manual-4/sem-2/u09/M4-u09-08__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **301** | `M4-u10-01` | ilustracion | 1 | u10 | portadilla | [md](manual-4/sem-2/u10/M4-u10-01__ilustracion__portadilla__pp1.md) | ✓ |
| **302** | `M4-u10-02` | mapa-mental | 1 | u10 | mapa mental de unidad | [md](manual-4/sem-2/u10/M4-u10-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **309** | `M4-u10-03` | cuadro-comparativo | 1 | u10 | desarrollo de subtema | [md](manual-4/sem-2/u10/M4-u10-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **316** | `M4-u10-04` | cuadro-comparativo | 1 | u10 | desarrollo de subtema | [md](manual-4/sem-2/u10/M4-u10-04__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **320** | `M4-u10-05` | ilustracion | 1 | u10 | desarrollo de subtema | [md](manual-4/sem-2/u10/M4-u10-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **325** | `M4-u10-06` | cuadro-comparativo | 1 | u10 | desarrollo de subtema | [md](manual-4/sem-2/u10/M4-u10-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **329** | `M4-u10-07` | cuadro-comparativo | 1 | u10 | desarrollo de subtema | [md](manual-4/sem-2/u10/M4-u10-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **362** | `M4-sem2-09` | ilustracion | 1 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-09__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **367** | `M4-sem2-10` | infografia | 1 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-10__infografia__contenido-del-manual__pp1.md) | ✓ |
| **370** | `M4-sem2-11` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-11__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **373** | `M4-sem2-12` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-12__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **375** | `M4-sem2-13` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-4/sem-2/sem2/M4-sem2-13__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |

## Manual 5

### Semestre 1 — `dist/manual-5-sem-1.pdf`

| Pág PDF | ID | Tipo | pp | Unidad | Rol | Prompt | Imagen |
|---:|---|---|---:|---|---|---|---|
| **1** | `M5-sem1-01` | ilustracion | 1 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-01__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **3** | `M5-sem1-02` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-02__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **6** | `M5-sem1-03` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-03__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **9** | `M5-sem1-04` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-04__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **11** | `M5-sem1-05` | infografia | 1 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-05__infografia__contenido-del-manual__pp1.md) | ✓ |
| **15** | `M5-sem1-06` | linea-tiempo | 1 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-06__linea-tiempo__contenido-del-manual__pp1.md) | ✓ |
| **18** | `M5-sem1-07` | cuadro-comparativo | 1 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-07__cuadro-comparativo__contenido-del-manual__pp1.md) | ✓ |
| **22** | `M5-sem1-08` | grafica | 0.5 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-08__grafica__contenido-del-manual__pp0p5.md) | ✓ |
| **23** | `M5-u01-01` | ilustracion | 1 | u01 | portadilla | [md](manual-5/sem-1/u01/M5-u01-01__ilustracion__portadilla__pp1.md) | ✓ |
| **25** | `M5-u01-02` | mapa-mental | 1 | u01 | mapa mental de unidad | [md](manual-5/sem-1/u01/M5-u01-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **33** | `M5-u01-03` | cuadro-comparativo | 1 | u01 | desarrollo de subtema | [md](manual-5/sem-1/u01/M5-u01-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **37** | `M5-u01-04` | cuadro-comparativo | 1 | u01 | desarrollo de subtema | [md](manual-5/sem-1/u01/M5-u01-04__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **41** | `M5-u01-05` | diagrama-flujo | 1 | u01 | desarrollo de subtema | [md](manual-5/sem-1/u01/M5-u01-05__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **46** | `M5-u01-06` | ilustracion | 1 | u01 | desarrollo de subtema | [md](manual-5/sem-1/u01/M5-u01-06__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **51** | `M5-u01-07` | cuadro-comparativo | 1 | u01 | desarrollo de subtema | [md](manual-5/sem-1/u01/M5-u01-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **56** | `M5-u01-08` | diagrama-flujo | 1 | u01 | desarrollo de subtema | [md](manual-5/sem-1/u01/M5-u01-08__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **62** | `M5-u01-09` | cuadro-comparativo | 1 | u01 | desarrollo de subtema | [md](manual-5/sem-1/u01/M5-u01-09__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **100** | `M5-u02-01` | ilustracion | 1 | u02 | portadilla | [md](manual-5/sem-1/u02/M5-u02-01__ilustracion__portadilla__pp1.md) | ✓ |
| **101** | `M5-u02-02` | mapa-mental | 1 | u02 | mapa mental de unidad | [md](manual-5/sem-1/u02/M5-u02-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **109** | `M5-u02-03` | ilustracion | 1 | u02 | desarrollo de subtema | [md](manual-5/sem-1/u02/M5-u02-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **114** | `M5-u02-04` | ilustracion | 1 | u02 | desarrollo de subtema | [md](manual-5/sem-1/u02/M5-u02-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **119** | `M5-u02-05` | cuadro-comparativo | 1 | u02 | desarrollo de subtema | [md](manual-5/sem-1/u02/M5-u02-05__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **123** | `M5-u02-06` | ilustracion | 1 | u02 | desarrollo de subtema | [md](manual-5/sem-1/u02/M5-u02-06__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **129** | `M5-u02-07` | cuadro-comparativo | 1 | u02 | desarrollo de subtema | [md](manual-5/sem-1/u02/M5-u02-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **133** | `M5-u02-08` | diagrama-flujo | 1 | u02 | desarrollo de subtema | [md](manual-5/sem-1/u02/M5-u02-08__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **171** | `M5-u03-01` | ilustracion | 1 | u03 | portadilla | [md](manual-5/sem-1/u03/M5-u03-01__ilustracion__portadilla__pp1.md) | ✓ |
| **172** | `M5-u03-02` | mapa-mental | 1 | u03 | mapa mental de unidad | [md](manual-5/sem-1/u03/M5-u03-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **179** | `M5-u03-03` | ilustracion | 1 | u03 | desarrollo de subtema | [md](manual-5/sem-1/u03/M5-u03-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **183** | `M5-u03-04` | ilustracion | 1 | u03 | desarrollo de subtema | [md](manual-5/sem-1/u03/M5-u03-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **188** | `M5-u03-05` | ilustracion | 1 | u03 | desarrollo de subtema | [md](manual-5/sem-1/u03/M5-u03-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **193** | `M5-u03-06` | ilustracion | 1 | u03 | desarrollo de subtema | [md](manual-5/sem-1/u03/M5-u03-06__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **197** | `M5-u03-07` | cuadro-comparativo | 1 | u03 | desarrollo de subtema | [md](manual-5/sem-1/u03/M5-u03-07__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **201** | `M5-u03-08` | ilustracion | 1 | u03 | desarrollo de subtema | [md](manual-5/sem-1/u03/M5-u03-08__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **236** | `M5-u04-01` | ilustracion | 1 | u04 | portadilla | [md](manual-5/sem-1/u04/M5-u04-01__ilustracion__portadilla__pp1.md) | ✓ |
| **237** | `M5-u04-02` | mapa-mental | 1 | u04 | mapa mental de unidad | [md](manual-5/sem-1/u04/M5-u04-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **242** | `M5-u04-03` | ilustracion | 1 | u04 | desarrollo de subtema | [md](manual-5/sem-1/u04/M5-u04-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **245** | `M5-u04-04` | ilustracion | 1 | u04 | desarrollo de subtema | [md](manual-5/sem-1/u04/M5-u04-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **249** | `M5-u04-05` | ilustracion | 1 | u04 | desarrollo de subtema | [md](manual-5/sem-1/u04/M5-u04-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **253** | `M5-u04-06` | cuadro-comparativo | 1 | u04 | desarrollo de subtema | [md](manual-5/sem-1/u04/M5-u04-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **256** | `M5-u04-07` | diagrama-flujo | 1 | u04 | desarrollo de subtema | [md](manual-5/sem-1/u04/M5-u04-07__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **260** | `M5-u04-08` | cuadro-comparativo | 1 | u04 | desarrollo de subtema | [md](manual-5/sem-1/u04/M5-u04-08__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **296** | `M5-sem1-09` | ilustracion | 1 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-09__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **301** | `M5-sem1-10` | infografia | 1 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-10__infografia__contenido-del-manual__pp1.md) | ✓ |
| **305** | `M5-sem1-11` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-11__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **307** | `M5-sem1-12` | cuadro-comparativo | 0.5 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-12__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **310** | `M5-sem1-13` | ilustracion | 0.5 | sem1 | contenido del manual | [md](manual-5/sem-1/sem1/M5-sem1-13__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |

### Semestre 2 — `dist/manual-5-sem-2.pdf`

| Pág PDF | ID | Tipo | pp | Unidad | Rol | Prompt | Imagen |
|---:|---|---|---:|---|---|---|---|
| **1** | `M5-sem2-01` | ilustracion | 1 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-01__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **3** | `M5-sem2-02` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-02__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **6** | `M5-sem2-03` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-03__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
| **9** | `M5-sem2-04` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-04__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **11** | `M5-sem2-05` | infografia | 1 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-05__infografia__contenido-del-manual__pp1.md) | ✓ |
| **15** | `M5-sem2-06` | linea-tiempo | 1 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-06__linea-tiempo__contenido-del-manual__pp1.md) | ✓ |
| **18** | `M5-sem2-07` | cuadro-comparativo | 1 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-07__cuadro-comparativo__contenido-del-manual__pp1.md) | ✓ |
| **23** | `M5-sem2-08` | grafica | 0.5 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-08__grafica__contenido-del-manual__pp0p5.md) | ✓ |
| **24** | `M5-u05-01` | ilustracion | 1 | u05 | portadilla | [md](manual-5/sem-2/u05/M5-u05-01__ilustracion__portadilla__pp1.md) | ✓ |
| **26** | `M5-u05-02` | mapa-mental | 1 | u05 | mapa mental de unidad | [md](manual-5/sem-2/u05/M5-u05-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **31** | `M5-u05-03` | cuadro-comparativo | 1 | u05 | desarrollo de subtema | [md](manual-5/sem-2/u05/M5-u05-03__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **34** | `M5-u05-04` | diagrama-flujo | 1 | u05 | desarrollo de subtema | [md](manual-5/sem-2/u05/M5-u05-04__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **39** | `M5-u05-05` | ilustracion | 1 | u05 | desarrollo de subtema | [md](manual-5/sem-2/u05/M5-u05-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **43** | `M5-u05-06` | cuadro-comparativo | 1 | u05 | desarrollo de subtema | [md](manual-5/sem-2/u05/M5-u05-06__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **47** | `M5-u05-07` | ilustracion | 1 | u05 | desarrollo de subtema | [md](manual-5/sem-2/u05/M5-u05-07__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **51** | `M5-u05-08` | ilustracion | 1 | u05 | desarrollo de subtema | [md](manual-5/sem-2/u05/M5-u05-08__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **54** | `M5-u05-09` | ilustracion | 1 | u05 | desarrollo de subtema | [md](manual-5/sem-2/u05/M5-u05-09__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **59** | `M5-u05-10` | ilustracion | 1 | u05 | desarrollo de subtema | [md](manual-5/sem-2/u05/M5-u05-10__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **97** | `M5-u06-01` | ilustracion | 1 | u06 | portadilla | [md](manual-5/sem-2/u06/M5-u06-01__ilustracion__portadilla__pp1.md) | ✓ |
| **97** | `M5-u06-02` | mapa-mental | 1 | u06 | mapa mental de unidad | [md](manual-5/sem-2/u06/M5-u06-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **102** | `M5-u06-03` | ilustracion | 1 | u06 | desarrollo de subtema | [md](manual-5/sem-2/u06/M5-u06-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **106** | `M5-u06-04` | diagrama-flujo | 1 | u06 | desarrollo de subtema | [md](manual-5/sem-2/u06/M5-u06-04__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **110** | `M5-u06-05` | ilustracion | 1 | u06 | desarrollo de subtema | [md](manual-5/sem-2/u06/M5-u06-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **114** | `M5-u06-06` | ilustracion | 1 | u06 | desarrollo de subtema | [md](manual-5/sem-2/u06/M5-u06-06__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **118** | `M5-u06-07` | ilustracion | 1 | u06 | desarrollo de subtema | [md](manual-5/sem-2/u06/M5-u06-07__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **155** | `M5-u07-01` | ilustracion | 1 | u07 | portadilla | [md](manual-5/sem-2/u07/M5-u07-01__ilustracion__portadilla__pp1.md) | ✓ |
| **156** | `M5-u07-02` | mapa-mental | 1 | u07 | mapa mental de unidad | [md](manual-5/sem-2/u07/M5-u07-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **160** | `M5-u07-03` | ilustracion | 1 | u07 | desarrollo de subtema | [md](manual-5/sem-2/u07/M5-u07-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **165** | `M5-u07-04` | ilustracion | 1 | u07 | desarrollo de subtema | [md](manual-5/sem-2/u07/M5-u07-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **169** | `M5-u07-05` | diagrama-flujo | 1 | u07 | desarrollo de subtema | [md](manual-5/sem-2/u07/M5-u07-05__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **174** | `M5-u07-06` | ilustracion | 1 | u07 | desarrollo de subtema | [md](manual-5/sem-2/u07/M5-u07-06__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **179** | `M5-u07-07` | interfaz | 1 | u07 | desarrollo de subtema | [md](manual-5/sem-2/u07/M5-u07-07__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **182** | `M5-u07-08` | cuadro-comparativo | 1 | u07 | desarrollo de subtema | [md](manual-5/sem-2/u07/M5-u07-08__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **218** | `M5-u08-01` | ilustracion | 1 | u08 | portadilla | [md](manual-5/sem-2/u08/M5-u08-01__ilustracion__portadilla__pp1.md) | ✓ |
| **219** | `M5-u08-02` | mapa-mental | 1 | u08 | mapa mental de unidad | [md](manual-5/sem-2/u08/M5-u08-02__mapa-mental__mapa-mental-de-unidad__pp1.md) | ✓ |
| **225** | `M5-u08-03` | ilustracion | 1 | u08 | desarrollo de subtema | [md](manual-5/sem-2/u08/M5-u08-03__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **228** | `M5-u08-04` | ilustracion | 1 | u08 | desarrollo de subtema | [md](manual-5/sem-2/u08/M5-u08-04__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **233** | `M5-u08-05` | ilustracion | 1 | u08 | desarrollo de subtema | [md](manual-5/sem-2/u08/M5-u08-05__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **238** | `M5-u08-06` | ilustracion | 1 | u08 | desarrollo de subtema | [md](manual-5/sem-2/u08/M5-u08-06__ilustracion__desarrollo-de-subtema__pp1.md) | ✓ |
| **243** | `M5-u08-07` | diagrama-flujo | 1 | u08 | desarrollo de subtema | [md](manual-5/sem-2/u08/M5-u08-07__diagrama-flujo__desarrollo-de-subtema__pp1.md) | ✓ |
| **247** | `M5-u08-08` | interfaz | 1 | u08 | desarrollo de subtema | [md](manual-5/sem-2/u08/M5-u08-08__interfaz__desarrollo-de-subtema__pp1.md) | ✓ |
| **253** | `M5-u08-09` | cuadro-comparativo | 1 | u08 | desarrollo de subtema | [md](manual-5/sem-2/u08/M5-u08-09__cuadro-comparativo__desarrollo-de-subtema__pp1.md) | ✓ |
| **284** | `M5-sem2-09` | ilustracion | 1 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-09__ilustracion__contenido-del-manual__pp1.md) | ✓ |
| **290** | `M5-sem2-10` | infografia | 1 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-10__infografia__contenido-del-manual__pp1.md) | ✓ |
| **293** | `M5-sem2-11` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-11__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **296** | `M5-sem2-12` | cuadro-comparativo | 0.5 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-12__cuadro-comparativo__contenido-del-manual__pp0p5.md) | ✓ |
| **299** | `M5-sem2-13` | ilustracion | 0.5 | sem2 | contenido del manual | [md](manual-5/sem-2/sem2/M5-sem2-13__ilustracion__contenido-del-manual__pp0p5.md) | ✓ |
