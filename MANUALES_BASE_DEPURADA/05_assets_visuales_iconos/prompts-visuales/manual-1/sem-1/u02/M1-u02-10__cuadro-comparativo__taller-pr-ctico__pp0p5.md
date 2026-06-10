---
id: M1-u02-10
manual: 1
unidad: u02
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 0.5
fuente_md: manuales/manual-1/unidades/u02/93-taller.md
fuente_md_linea: 35
imagen_destino: assets/visuales/manual-1/u02/M1-u02-10.jpg
pagina_pdf_estimada: 185
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: taller práctico
status: pendiente
---

# `M1-u02-10`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 185

**Manual 1 · U02 — Agua · Semestre 1**

> Rol del archivo: _taller práctico_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u02-10` |
| Archivo destino imagen | `assets/visuales/manual-1/u02/M1-u02-10.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-1.pdf` |
| Página PDF estimada | **p. 185** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u02/93-taller.md:35` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Cuadro comparativo de las tres estaciones del taller (pH, dureza, cloro). Filas: instrumento, reactivos, técnica, fórmula clave, rango NOM-127, observaciones. Cada estación con icono distintivo (potenciómetro, bureta, gota colorimétrica).

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U02 — Agua**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **taller práctico**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro comparativo de las tres estaciones del taller (pH, dureza, cloro). Filas: instrumento, reactivos, técnica, fórmula clave, rango NOM-127, observaciones. Cada estación con icono distintivo (potenciómetro, bureta, gota colorimétrica).

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
2. Guárdala como `assets/visuales/manual-1/u02/M1-u02-10.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u02-10` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
