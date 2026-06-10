---
id: M3-u01-06
manual: 3
unidad: u01
semestre: 1
tipo: infografia
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u01/10-tema-1-4.md
fuente_md_linea: 111
imagen_destino: assets/visuales/manual-3/u01/M3-u01-06.jpg
pagina_pdf_estimada: 29
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M3-u01-06`

**Tipo visual:** `infografia` · **Ocupa:** 1 pp · **Página PDF estimada:** 29

**Manual 3 · U01 — Fundamentos e Historia de la IA · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u01-06` |
| Archivo destino imagen | `assets/visuales/manual-3/u01/M3-u01-06.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 29** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u01/10-tema-1-4.md:111` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Cuatro círculos concéntricos: 1) IA (más grande) con ejemplos: sistemas expertos, lógica simbólica, planificación, ML, DL. 2) MACHINE LEARNING — Random Forest, regresión, SVM, K-means, Naive Bayes. 3) DEEP LEARNING — CNNs (visión), RNNs (secuencias), GANs (imágenes), Diffusion (DALL·E, Sora), Transformers. 4) LLMs (más pequeño) — GPT-4, Claude, Gemini, Llama, Mistral, DeepSeek. Cada círculo en color creciente y con flechas indicando que cada uno es subconjunto del anterior. Notación matemática IA ⊃ ML ⊃ DL ⊃ LLMs visible.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U01 — Fundamentos e Historia de la IA**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **infografia**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuatro círculos concéntricos: 1) IA (más grande) con ejemplos: sistemas expertos, lógica simbólica, planificación, ML, DL. 2) MACHINE LEARNING — Random Forest, regresión, SVM, K-means, Naive Bayes. 3) DEEP LEARNING — CNNs (visión), RNNs (secuencias), GANs (imágenes), Diffusion (DALL·E, Sora), Transformers. 4) LLMs (más pequeño) — GPT-4, Claude, Gemini, Llama, Mistral, DeepSeek. Cada círculo en color creciente y con flechas indicando que cada uno es subconjunto del anterior. Notación matemática IA ⊃ ML ⊃ DL ⊃ LLMs visible.

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
2. Guárdala como `assets/visuales/manual-3/u01/M3-u01-06.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u01-06` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
