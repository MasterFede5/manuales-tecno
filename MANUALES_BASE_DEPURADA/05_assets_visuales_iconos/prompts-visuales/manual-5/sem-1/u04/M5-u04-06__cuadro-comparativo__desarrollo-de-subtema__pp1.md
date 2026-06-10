---
id: M5-u04-06
manual: 5
unidad: u04
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 1
fuente_md: manuales/manual-5/unidades/u04/10-tema-4-4.md
fuente_md_linea: 73
imagen_destino: assets/visuales/manual-5/u04/M5-u04-06.jpg
pagina_pdf_estimada: 253
pdf_destino: dist/manual-5-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M5-u04-06`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 1 pp · **Página PDF estimada:** 253

**Manual 5 · U04 — ML clásico (scikit-learn) · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M5-u04-06` |
| Archivo destino imagen | `assets/visuales/manual-5/u04/M5-u04-06.jpg` |
| PDF en el que aparece | `dist/manual-5-sem-1.pdf` |
| Página PDF estimada | **p. 253** |
| Archivo Markdown fuente | `manuales/manual-5/unidades/u04/10-tema-4-4.md:73` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Galería visual a tamaño página de 6 scatter plots: 1) r=+1 puntos en diagonal perfecta. 2) r=+0.7 nube clara ascendente. 3) r=+0.3 nube ligeramente ascendente. 4) r=0 nube circular. 5) r=-0.3 nube ligeramente descendente. 6) r=-1 perfecto descendente. Cada uno etiquetado con fortaleza. Bajo todo, regla de interpretación 0-1. Estilo blueprint educativo Albatros.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial con Programación** — De Python al primer modelo de Machine Learning y APIs de IA
- Unidad: **U04 — ML clásico (scikit-learn)**
- Case study: *Predictor de rendimiento escolar — pipeline ML completo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Galería visual a tamaño página de 6 scatter plots: 1) r=+1 puntos en diagonal perfecta. 2) r=+0.7 nube clara ascendente. 3) r=+0.3 nube ligeramente ascendente. 4) r=0 nube circular. 5) r=-0.3 nube ligeramente descendente. 6) r=-1 perfecto descendente. Cada uno etiquetado con fortaleza. Bajo todo, regla de interpretación 0-1. Estilo blueprint educativo Albatros.

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
2. Guárdala como `assets/visuales/manual-5/u04/M5-u04-06.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 5
   python print_to_pdf.py --manual 5 --all-semesters
   ```

4. Verifica que `M5-u04-06` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
