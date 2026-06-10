---
id: M1-u01-13
manual: 1
unidad: u01
semestre: 1
tipo: infografia
paginas_ocupa: 0.5
fuente_md: manuales/manual-1/unidades/u01/10-tema-1-8.md
fuente_md_linea: 110
imagen_destino: assets/visuales/manual-1/u01/M1-u01-13.jpg
pagina_pdf_estimada: 103
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M1-u01-13`

**Tipo visual:** `infografia` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 103

**Manual 1 · U01 — Temas Básicos de la Materia · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u01-13` |
| Archivo destino imagen | `assets/visuales/manual-1/u01/M1-u01-13.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-1.pdf` |
| Página PDF estimada | **p. 103** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u01/10-tema-1-8.md:110` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Infografía del concepto de mol comparando escalas: a la izquierda, una cucharadita de sal con leyenda '5 g de NaCl ≈ 5 × 10²² unidades fórmula'; al centro, un vaso con 18 mL de agua con leyenda '18 g de H₂O = 1 mol = 6.022 × 10²³ moléculas'; a la derecha, un globo con 22.4 L de gas con leyenda '1 mol de cualquier gas ideal a CNTP'. En la parte inferior, el triángulo del mol con sus tres conversiones (m, n, N) y un ejemplo aplicado al sorbo del bebedero.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U01 — Temas Básicos de la Materia**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **infografia**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Infografía del concepto de mol comparando escalas: a la izquierda, una cucharadita de sal con leyenda '5 g de NaCl ≈ 5 × 10²² unidades fórmula'; al centro, un vaso con 18 mL de agua con leyenda '18 g de H₂O = 1 mol = 6.022 × 10²³ moléculas'; a la derecha, un globo con 22.4 L de gas con leyenda '1 mol de cualquier gas ideal a CNTP'. En la parte inferior, el triángulo del mol con sus tres conversiones (m, n, N) y un ejemplo aplicado al sorbo del bebedero.

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
2. Guárdala como `assets/visuales/manual-1/u01/M1-u01-13.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u01-13` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
