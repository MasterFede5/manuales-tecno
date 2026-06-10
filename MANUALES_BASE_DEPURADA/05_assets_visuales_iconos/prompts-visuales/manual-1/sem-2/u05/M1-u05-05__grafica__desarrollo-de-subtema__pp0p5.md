---
id: M1-u05-05
manual: 1
unidad: u05
semestre: 2
tipo: grafica
paginas_ocupa: 0.5
fuente_md: manuales/manual-1/unidades/u05/10-tema-5-3.md
fuente_md_linea: 106
imagen_destino: assets/visuales/manual-1/u05/M1-u05-05.jpg
pagina_pdf_estimada: 83
pdf_destino: dist/manual-1-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M1-u05-05`

**Tipo visual:** `grafica` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 83

**Manual 1 · U05 — Energía y Reacciones Químicas · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u05-05` |
| Archivo destino imagen | `assets/visuales/manual-1/u05/M1-u05-05.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-2.pdf` |
| Página PDF estimada | **p. 83** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u05/10-tema-5-3.md:106` |
| Tipo de placeholder | `grafica` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Tres gráficas paralelas de las leyes de los gases: 1) Boyle (P vs V a T cte, hipérbola descendente con etiqueta T1 < T2 < T3), 2) Charles (V vs T en Kelvin, líneas rectas que parten de origen extrapoladas hasta -273.15°C cero absoluto), 3) Gay-Lussac (P vs T a V cte). Cada una con un ejemplo cotidiano ilustrado: jeringa comprimiéndose, globo expandiéndose con calor, olla a presión.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U05 — Energía y Reacciones Químicas**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **grafica**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (grafica):**
GRÁFICA CIENTÍFICA limpia: ejes etiquetados con magnitud+unidad, cuadrícula tenue, una o dos series, leyenda compacta arriba derecha.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Tres gráficas paralelas de las leyes de los gases: 1) Boyle (P vs V a T cte, hipérbola descendente con etiqueta T1 < T2 < T3), 2) Charles (V vs T en Kelvin, líneas rectas que parten de origen extrapoladas hasta -273.15°C cero absoluto), 3) Gay-Lussac (P vs T a V cte). Cada una con un ejemplo cotidiano ilustrado: jeringa comprimiéndose, globo expandiéndose con calor, olla a presión.

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
2. Guárdala como `assets/visuales/manual-1/u05/M1-u05-05.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u05-05` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
