# Semestre 2 — Manual 4: Inteligencia Artificial Avanzada

**Unidades de este semestre:** U06 (Agentes con herramientas), U07 (Versión local soberana), U08 (Conexión vía MCP), U09 (Material educativo certificable), U10 (Implementación, costos y gobernanza)

## Front matter (en orden)

1. `00-portada.md` — Portada e identidad del semestre
2. `01-carta-estudiante.md` — Carta al estudiante
3. `02-carta-docente.md` — Carta al docente
4. `03-mapa-contenidos.md` — Mapa de contenidos del semestre
5. `04-hilo-conductor.md` — Hilo conductor (case study) en este semestre
6. `05-competencias.md` — Índice de competencias del semestre
7. `06-diagnostica.md` — Evaluación diagnóstica inicial

## Unidades

Las unidades viven en `manuales/manual-4/unidades/` — este semestre incluye
las carpetas `u06`, `u07`, `u08`, `u09`, `u10`.

## Cierre y material extra

8. `90-cierre-semestre.md` — Cierre del semestre + proyecto integrador
9. `91-material-extra.md` — Material extra opcional (tips, retos, lecturas cruzadas)
10. `92-glosario-semestre.md` — Glosario de términos del semestre
11. `93-bibliografia-semestre.md` — Bibliografía y bitácora de fuentes
12. `94-indice-analitico.md` — Índice analítico personal

## Build

```bash
python build/converter.py manuales/manual-4 dist/manual-4-sem-2.html --semester 2
python print_to_pdf.py --manual 4 --semester 2
```
