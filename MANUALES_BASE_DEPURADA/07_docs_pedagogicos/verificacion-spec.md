# Verificacion contra manual-spec

Generado por `verify_spec.py`. Mide los 10 PDFs semestrales contra la regla vigente: 120 a 140 paginas por manual de contenido.

## Tamano fisico - Carta 8.5x11 in (612x792 pt = 215.9x279.4 mm)

| PDF | Paginas | Tamano detectado | Carta |
|---|---:|---|:-:|
| `manual-1-sem-1.pdf` | 258 | 612.0x792.0 pt (215.9x279.4 mm) | OK |
| `manual-1-sem-2.pdf` | 201 | 612.0x792.0 pt (215.9x279.4 mm) | OK |
| `manual-2-sem-1.pdf` | 321 | 612.0x792.0 pt (215.9x279.4 mm) | OK |
| `manual-2-sem-2.pdf` | 233 | 612.0x792.0 pt (215.9x279.4 mm) | OK |
| `manual-3-sem-1.pdf` | 306 | 612.0x792.0 pt (215.9x279.4 mm) | OK |
| `manual-3-sem-2.pdf` | 255 | 612.0x792.0 pt (215.9x279.4 mm) | OK |
| `manual-4-sem-1.pdf` | 399 | 612.0x792.0 pt (215.9x279.4 mm) | OK |
| `manual-4-sem-2.pdf` | 376 | 612.0x792.0 pt (215.9x279.4 mm) | OK |
| `manual-5-sem-1.pdf` | 311 | 612.0x792.0 pt (215.9x279.4 mm) | OK |
| `manual-5-sem-2.pdf` | 300 | 612.0x792.0 pt (215.9x279.4 mm) | OK |

**Carta exacta:** 612.0 x 792.0 pt (215.9 x 279.4 mm). Tolerancia +/-2 pt.

## Rango de paginas por manual semestral

Regla correcta: cada PDF semestral debe tener entre 120 y 140 paginas de contenido.

| PDF | Paginas | Rango 120-140 | Exceso sobre 140 | Reduccion minima |
|---|---:|:-:|---:|---:|
| `manual-1-sem-1.pdf` | 258 | alto | 118 | 45.7% |
| `manual-1-sem-2.pdf` | 201 | alto | 61 | 30.3% |
| `manual-2-sem-1.pdf` | 321 | alto | 181 | 56.4% |
| `manual-2-sem-2.pdf` | 233 | alto | 93 | 39.9% |
| `manual-3-sem-1.pdf` | 306 | alto | 166 | 54.2% |
| `manual-3-sem-2.pdf` | 255 | alto | 115 | 45.1% |
| `manual-4-sem-1.pdf` | 399 | alto | 259 | 64.9% |
| `manual-4-sem-2.pdf` | 376 | alto | 236 | 62.8% |
| `manual-5-sem-1.pdf` | 311 | alto | 171 | 55.0% |
| `manual-5-sem-2.pdf` | 300 | alto | 160 | 53.3% |

**PDFs esperados:** 10.
**PDFs detectados:** 10.
**Total actual:** 2960 paginas.
**Rango total permitido:** 1200-1400 paginas.
**Exceso minimo sobre el maximo:** 1560 paginas.
**Objetivo recomendado:** 1300 paginas (130 por semestre).
**Reduccion contra objetivo recomendado:** 1660 paginas (56.1%).

## Estructura minima por semestre

Cada `semestre-X/` debe tener al menos:

| Manual | Sem | Archivos esperados | Presentes | Completo |
|---|:-:|---:|---:|:-:|
| M1 | 1 | 12 | 12 | OK |
| M1 | 2 | 12 | 12 | OK |
| M2 | 1 | 12 | 12 | OK |
| M2 | 2 | 12 | 12 | OK |
| M3 | 1 | 12 | 12 | OK |
| M3 | 2 | 12 | 12 | OK |
| M4 | 1 | 12 | 12 | OK |
| M4 | 2 | 12 | 12 | OK |
| M5 | 1 | 12 | 12 | OK |
| M5 | 2 | 12 | 12 | OK |

## Bloques minimos por unidad

Ver `docs/diagnostico-pedagogico.md`: cero unidades con bloques obligatorios faltantes.

## Visuales - descripcion >= 50 caracteres

11 visuales con descripcion corta:
- `manuales/manual-3/unidades/u01/10-tema-1-1.md` -> `Cuadro de las 3 definiciones....`
- `manuales/manual-3/unidades/u01/10-tema-1-2.md` -> `Infografía de los dos inviernos de IA....`
- `manuales/manual-3/unidades/u01/10-tema-1-3.md` -> `Tres círculos concéntricos: ANI, AGI, ASI....`
- `manuales/manual-3/unidades/u01/10-tema-1-5.md` -> `Analogía del aprendiz de cocinero en 3 viñetas....`
- `manuales/manual-2/unidades/u03/10-tema-3-3.md` -> `Gráfica parabólica de Ek vs v....`
- `manuales/manual-2/unidades/u03/10-tema-3-4.md` -> `Dos viñetas ilustrando U_g y U_e....`
- `manuales/manual-2/unidades/u03/10-tema-3-5.md` -> `Conservación en montaña rusa....`
- `manuales/manual-2/unidades/u03/10-tema-3-6.md` -> `Diagrama de conservación de momento en colisión....`
- `manuales/manual-2/unidades/u03/10-tema-3-7.md` -> `Cuadro de colisiones....`
- `manuales/manual-2/unidades/u03/10-tema-3-8.md` -> `Cuatro viñetas con tipos de fricción....`
- `manuales/manual-2/unidades/u04/10-tema-4-8.md` -> `Diagramas de las Leyes....`
