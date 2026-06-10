---
id: M5-u03-04
manual: 5
unidad: u03
semestre: 1
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-5/unidades/u03/10-tema-3-2.md
fuente_md_linea: 79
imagen_destino: assets/visuales/manual-5/u03/M5-u03-04.jpg
pagina_pdf_estimada: 183
pdf_destino: dist/manual-5-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M5-u03-04`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 183

**Manual 5 · U03 — Visualización (Matplotlib/Seaborn) · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M5-u03-04` |
| Archivo destino imagen | `assets/visuales/manual-5/u03/M5-u03-04.jpg` |
| PDF en el que aparece | `dist/manual-5-sem-1.pdf` |
| Página PDF estimada | **p. 183** |
| Archivo Markdown fuente | `manuales/manual-5/unidades/u03/10-tema-3-2.md:79` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Ilustración a tamaño página comparativa. Lado izquierdo: histograma con campana clara, anotaciones de bins, frecuencia, media (línea roja punteada), forma de distribución. Lado derecho: boxplot vertical con etiquetas: mínimo, Q1, mediana, Q3, máximo, outliers. Bajo ambos, los mismos datos representados en una tablita y un texto explicando 'mismo dataset, dos lentes'. Estilo blueprint educativo Albatros.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial con Programación** — De Python al primer modelo de Machine Learning y APIs de IA
- Unidad: **U03 — Visualización (Matplotlib/Seaborn)**
- Case study: *Predictor de rendimiento escolar — pipeline ML completo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Ilustración a tamaño página comparativa. Lado izquierdo: histograma con campana clara, anotaciones de bins, frecuencia, media (línea roja punteada), forma de distribución. Lado derecho: boxplot vertical con etiquetas: mínimo, Q1, mediana, Q3, máximo, outliers. Bajo ambos, los mismos datos representados en una tablita y un texto explicando 'mismo dataset, dos lentes'. Estilo blueprint educativo Albatros.

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
2. Guárdala como `assets/visuales/manual-5/u03/M5-u03-04.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 5
   python print_to_pdf.py --manual 5 --all-semesters
   ```

4. Verifica que `M5-u03-04` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
