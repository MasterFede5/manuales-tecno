---
id: M5-u02-05
manual: 5
unidad: u02
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 1
fuente_md: manuales/manual-5/unidades/u02/10-tema-2-3.md
fuente_md_linea: 118
imagen_destino: assets/visuales/manual-5/u02/M5-u02-05.jpg
pagina_pdf_estimada: 119
pdf_destino: dist/manual-5-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M5-u02-05`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 1 pp · **Página PDF estimada:** 119

**Manual 5 · U02 — Limpieza con NumPy/Pandas · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M5-u02-05` |
| Archivo destino imagen | `assets/visuales/manual-5/u02/M5-u02-05.jpg` |
| PDF en el que aparece | `dist/manual-5-sem-1.pdf` |
| Página PDF estimada | **p. 119** |
| Archivo Markdown fuente | `manuales/manual-5/unidades/u02/10-tema-2-3.md:118` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Cuadro a tamaño página con los 3 formatos en filas (CSV, Excel, JSON). Columnas: función pandas · ejemplo · parámetros clave (encoding, sep, sheet, orient) · librería extra requerida · cuándo usar · cuándo NO. Bajo el cuadro, snippet visual de los 3 formatos con sus 'caras' típicas (CSV: texto con comas, Excel: tabla con celdas, JSON: estructura con llaves). Estilo blueprint Albatros.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial con Programación** — De Python al primer modelo de Machine Learning y APIs de IA
- Unidad: **U02 — Limpieza con NumPy/Pandas**
- Case study: *Predictor de rendimiento escolar — pipeline ML completo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro a tamaño página con los 3 formatos en filas (CSV, Excel, JSON). Columnas: función pandas · ejemplo · parámetros clave (encoding, sep, sheet, orient) · librería extra requerida · cuándo usar · cuándo NO. Bajo el cuadro, snippet visual de los 3 formatos con sus 'caras' típicas (CSV: texto con comas, Excel: tabla con celdas, JSON: estructura con llaves). Estilo blueprint Albatros.

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
2. Guárdala como `assets/visuales/manual-5/u02/M5-u02-05.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 5
   python print_to_pdf.py --manual 5 --all-semesters
   ```

4. Verifica que `M5-u02-05` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
