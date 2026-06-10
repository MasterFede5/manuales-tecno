---
id: M3-u02-09
manual: 3
unidad: u02
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u02/10-tema-2-6.md
fuente_md_linea: 39
imagen_destino: assets/visuales/manual-3/u02/M3-u02-09.jpg
pagina_pdf_estimada: 87
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M3-u02-09`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 1 pp · **Página PDF estimada:** 87

**Manual 3 · U02 — Tu primer chat útil · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u02-09` |
| Archivo destino imagen | `assets/visuales/manual-3/u02/M3-u02-09.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 87** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u02/10-tema-2-6.md:39` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Cuadro comparativo de 4 plataformas en formato tabla: Columnas: ChatGPT Plus / Claude Pro / Gemini Advanced / Copilot Pro. Filas: 1) Modelo base — GPT-5 + o3 / Opus 4.7 + Sonnet / Gemini 2.0 Pro / GPT-4 con Microsoft. 2) Contexto — 128K-256K / 1M / 2M / 128K. 3) Multimodal — sí, GPT-4o / sí, Sonnet 4.6 / sí, nativo / sí. 4) Búsqueda web — sí / sí (limitada) / sí, Google / sí, Bing. 5) Integración — GPTs Store / Projects + Artifacts / Workspace nativa / Office 365 nativa. 6) Función distintiva — Voice avanzada + GPTs / Artifacts + 1M contexto / Workspace + 2M / Office Apps. 7) Precio — $20/mes / $20/mes / $20/mes / $20/mes. 8) Caso ideal — Generalista, plugins, voz / Redacción larga, código, docs / Vives en Google / Vives en Microsoft.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U02 — Tu primer chat útil**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro comparativo de 4 plataformas en formato tabla: Columnas: ChatGPT Plus / Claude Pro / Gemini Advanced / Copilot Pro. Filas: 1) Modelo base — GPT-5 + o3 / Opus 4.7 + Sonnet / Gemini 2.0 Pro / GPT-4 con Microsoft. 2) Contexto — 128K-256K / 1M / 2M / 128K. 3) Multimodal — sí, GPT-4o / sí, Sonnet 4.6 / sí, nativo / sí. 4) Búsqueda web — sí / sí (limitada) / sí, Google / sí, Bing. 5) Integración — GPTs Store / Projects + Artifacts / Workspace nativa / Office 365 nativa. 6) Función distintiva — Voice avanzada + GPTs / Artifacts + 1M contexto / Workspace + 2M / Office Apps. 7) Precio — $20/mes / $20/mes / $20/mes / $20/mes. 8) Caso ideal — Generalista, plugins, voz / Redacción larga, código, docs / Vives en Google / Vives en Microsoft.

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
2. Guárdala como `assets/visuales/manual-3/u02/M3-u02-09.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u02-09` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
