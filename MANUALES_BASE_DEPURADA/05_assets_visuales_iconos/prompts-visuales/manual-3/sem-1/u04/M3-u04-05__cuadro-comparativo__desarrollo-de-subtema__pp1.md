---
id: M3-u04-05
manual: 3
unidad: u04
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u04/10-tema-4-2.md
fuente_md_linea: 80
imagen_destino: assets/visuales/manual-3/u04/M3-u04-05.jpg
pagina_pdf_estimada: 196
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M3-u04-05`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 1 pp · **Página PDF estimada:** 196

**Manual 3 · U04 — Voz, imagen y video con IA · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u04-05` |
| Archivo destino imagen | `assets/visuales/manual-3/u04/M3-u04-05.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 196** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u04/10-tema-4-2.md:80` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Cuadro comparativo de 6 plataformas de video IA 2025 en formato tabla: 1) SORA (OpenAI) — text-to-video, calidad líder cinematográfica, duración 60s en Pro, costo $20-200/mes. 2) VEO 2/3 (Google) — text-to-video con audio sincronizado, integración Workspace, $20/mes. 3) RUNWAY GEN-3 — image-to-video y edición, ecosistema completo, $15-95/mes. 4) PIKA LABS — text-to-video conceptual, vía Discord, $0-58/mes. 5) HEYGEN — avatares hablando con tu guion, clonación de tu rostro, $24/mes. 6) SYNTHESIA — avatares corporate multilingüe, $30/mes. Filas con tipo principal, duración máx, calidad, caso de uso ideal.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U04 — Voz, imagen y video con IA**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro comparativo de 6 plataformas de video IA 2025 en formato tabla: 1) SORA (OpenAI) — text-to-video, calidad líder cinematográfica, duración 60s en Pro, costo $20-200/mes. 2) VEO 2/3 (Google) — text-to-video con audio sincronizado, integración Workspace, $20/mes. 3) RUNWAY GEN-3 — image-to-video y edición, ecosistema completo, $15-95/mes. 4) PIKA LABS — text-to-video conceptual, vía Discord, $0-58/mes. 5) HEYGEN — avatares hablando con tu guion, clonación de tu rostro, $24/mes. 6) SYNTHESIA — avatares corporate multilingüe, $30/mes. Filas con tipo principal, duración máx, calidad, caso de uso ideal.

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
2. Guárdala como `assets/visuales/manual-3/u04/M3-u04-05.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u04-05` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
