# Semestre 2 — Manual 3: Inteligencia Artificial Básica

**Unidades de este semestre:** U06 (IA automatiza tu semana), U07 (Tu GPT/Gem propio), U08 (Producción de contenido educativo), U09 (Ética y publicación responsable)

## Front matter (en orden)

1. `00-portada.md` — Portada e identidad del semestre
2. `01-carta-estudiante.md` — Carta al estudiante
3. `02-carta-docente.md` — Carta al docente
4. `03-mapa-contenidos.md` — Mapa de contenidos del semestre
5. `04-hilo-conductor.md` — Hilo conductor (case study) en este semestre
6. `05-competencias.md` — Índice de competencias del semestre
7. `06-diagnostica.md` — Evaluación diagnóstica inicial

## Unidades

Las unidades viven en `manuales/manual-3/unidades/` — este semestre incluye
las carpetas `u06`, `u07`, `u08`, `u09`.

## Cierre y material extra

8. `90-cierre-semestre.md` — Cierre del semestre + proyecto integrador
9. `91-material-extra.md` — Material extra opcional (tips, retos, lecturas cruzadas)
10. `92-glosario-semestre.md` — Glosario de términos del semestre
11. `93-bibliografia-semestre.md` — Bibliografía y bitácora de fuentes
12. `94-indice-analitico.md` — Índice analítico personal

## Build

```bash
python build/converter.py manuales/manual-3 dist/manual-3-sem-2.html --semester 2
python print_to_pdf.py --manual 3 --semester 2
```
