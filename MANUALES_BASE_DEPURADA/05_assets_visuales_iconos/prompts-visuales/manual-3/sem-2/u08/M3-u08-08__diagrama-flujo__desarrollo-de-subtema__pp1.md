---
id: M3-u08-08
manual: 3
unidad: u08
semestre: 2
tipo: diagrama-flujo
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u08/10-tema-8-6.md
fuente_md_linea: 38
imagen_destino: assets/visuales/manual-3/u08/M3-u08-08.jpg
pagina_pdf_estimada: 153
pdf_destino: dist/manual-3-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M3-u08-08`

**Tipo visual:** `diagrama-flujo` · **Ocupa:** 1 pp · **Página PDF estimada:** 153

**Manual 3 · U08 — Producción de contenido educativo · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u08-08` |
| Archivo destino imagen | `assets/visuales/manual-3/u08/M3-u08-08.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-2.pdf` |
| Página PDF estimada | **p. 153** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u08/10-tema-8-6.md:38` |
| Tipo de placeholder | `diagrama-flujo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Pipeline horizontal de 7 estaciones: 1) IDEA en globo de pensamiento (5 min). 2) TEXTO en ChatGPT/Claude generando guion + 3 posts (15 min). 3) IMAGEN en DALL·E generando 6 visuales (15 min). 4) VOZ en ElevenLabs narrando (10 min). 5) VIDEO en CapCut ensamblando con subtítulos (20 min). 6) DISEÑO en Canva produciendo carrusel para Instagram (15 min). 7) PUBLICACIÓN simultánea en YouTube/TikTok/Instagram/LinkedIn (10 min). Tiempo total: 90 min. Cada estación con icono de herramienta y tiempo en minutos.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U08 — Producción de contenido educativo**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **diagrama-flujo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (diagrama-flujo):**
DIAGRAMA DE FLUJO: cajas redondeadas conectadas por flechas, rombos para decisiones, azul Albatros para procesos, naranja para decisión, sin cruces.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Pipeline horizontal de 7 estaciones: 1) IDEA en globo de pensamiento (5 min). 2) TEXTO en ChatGPT/Claude generando guion + 3 posts (15 min). 3) IMAGEN en DALL·E generando 6 visuales (15 min). 4) VOZ en ElevenLabs narrando (10 min). 5) VIDEO en CapCut ensamblando con subtítulos (20 min). 6) DISEÑO en Canva produciendo carrusel para Instagram (15 min). 7) PUBLICACIÓN simultánea en YouTube/TikTok/Instagram/LinkedIn (10 min). Tiempo total: 90 min. Cada estación con icono de herramienta y tiempo en minutos.

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
2. Guárdala como `assets/visuales/manual-3/u08/M3-u08-08.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u08-08` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
