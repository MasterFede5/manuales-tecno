---
id: M3-u02-11
manual: 3
unidad: u02
semestre: 1
tipo: infografia
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u02/10-tema-2-7.md
fuente_md_linea: 99
imagen_destino: assets/visuales/manual-3/u02/M3-u02-11.jpg
pagina_pdf_estimada: 94
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M3-u02-11`

**Tipo visual:** `infografia` · **Ocupa:** 1 pp · **Página PDF estimada:** 94

**Manual 3 · U02 — Tu primer chat útil · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u02-11` |
| Archivo destino imagen | `assets/visuales/manual-3/u02/M3-u02-11.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 94** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u02/10-tema-2-7.md:99` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Tres limitaciones de LLMs en infografía con personajes ilustrados: 1) ALUCINACIONES — modelo IA con globo de diálogo afirmando 'según el paper de Smith 2019...' (paper que no existe), un humano detrás verificando en Google Scholar. Tip box: 'verifica TODA cita o número crítico'. 2) SESGOS — dos personajes (mujer y hombre) idénticos haciendo la misma pregunta y recibiendo respuestas con tono distinto. Tip: 'cuestiona suposiciones implícitas'. 3) FECHA DE CORTE — calendario con marca a una fecha pasada; modelo IA dice 'no sé qué pasó después de Oct 2023'. Tip: 'usa búsqueda web para datos recientes'.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U02 — Tu primer chat útil**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **infografia**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Tres limitaciones de LLMs en infografía con personajes ilustrados: 1) ALUCINACIONES — modelo IA con globo de diálogo afirmando 'según el paper de Smith 2019...' (paper que no existe), un humano detrás verificando en Google Scholar. Tip box: 'verifica TODA cita o número crítico'. 2) SESGOS — dos personajes (mujer y hombre) idénticos haciendo la misma pregunta y recibiendo respuestas con tono distinto. Tip: 'cuestiona suposiciones implícitas'. 3) FECHA DE CORTE — calendario con marca a una fecha pasada; modelo IA dice 'no sé qué pasó después de Oct 2023'. Tip: 'usa búsqueda web para datos recientes'.

**REGLAS DE CALIDAD:**
- Texto en español de México, ortográfica y científicamente correcto (sin texto deformado IA).
- Fórmulas químicas/físicas/matemáticas con subíndices/superíndices correctos (H₂O, CO₂, E=mc², etc.).
- Sin marcas de agua, sin firmas, sin elementos decorativos no pedidos.
- Espacio para que el maquetador añada leyendas posteriores.
- Si es infografía/mapa-mental/tabla: zonas de texto editables (placeholders rectangulares claros).
- Resultado vector-friendly aunque se entregue como PNG @300 dpi.

**NEGATIVOS:**
sin photoreal, sin estilo Pixar, sin anime, sin elementos cursis, sin firma de artista, sin watermark, sin texto basura, sin manos deformes, sin números inventados, sin alfabetos no latinos.
```

## Cómo inyectar la imagen final

1. Genera la imagen con el prompt de arriba (Midjourney, DALL·E, SD, Flux — manualmente, sin API).
2. Guárdala como `assets/visuales/manual-3/u02/M3-u02-11.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u02-11` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
