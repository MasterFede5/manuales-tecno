---
id: M4-u01-07
manual: 4
unidad: u01
semestre: 1
tipo: diagrama-flujo
paginas_ocupa: 1
fuente_md: manuales/manual-4/unidades/u01/10-tema-1-5.md
fuente_md_linea: 97
imagen_destino: assets/visuales/manual-4/u01/M4-u01-07.jpg
pagina_pdf_estimada: 48
pdf_destino: dist/manual-4-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M4-u01-07`

**Tipo visual:** `diagrama-flujo` · **Ocupa:** 1 pp · **Página PDF estimada:** 48

**Manual 4 · U01 — Prompts versionados · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M4-u01-07` |
| Archivo destino imagen | `assets/visuales/manual-4/u01/M4-u01-07.jpg` |
| PDF en el que aparece | `dist/manual-4-sem-1.pdf` |
| Página PDF estimada | **p. 48** |
| Archivo Markdown fuente | `manuales/manual-4/unidades/u01/10-tema-1-5.md:97` |
| Tipo de placeholder | `diagrama-flujo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Diagrama de pipeline de 5 prompts encadenados a tamaño página completa. Caja 1 'Extracción' (input cuadro de texto, output JSON estructurado). Caja 2 'Estructura' (input JSON, output outline). Caja 3 'Redacción' (input outline, output borrador). Caja 4 'Revisión de tono' (input borrador, output comunicado revisado con marcas). Caja 5 'Formato final' (input revisado, output HTML/PDF con membrete). Flechas etiquetadas con el tipo de paso de contexto. Bajo el pipeline, una pequeña etiqueta de versión 'pipeline-comunicado-v2.1'. Estilo limpio.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Avanzada** — Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza
- Unidad: **U01 — Prompts versionados**
- Case study: *Asistente Institucional Albatros — IA con herramientas reales*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **diagrama-flujo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (diagrama-flujo):**
DIAGRAMA DE FLUJO: cajas redondeadas conectadas por flechas, rombos para decisiones, azul Albatros para procesos, naranja para decisión, sin cruces.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Diagrama de pipeline de 5 prompts encadenados a tamaño página completa. Caja 1 'Extracción' (input cuadro de texto, output JSON estructurado). Caja 2 'Estructura' (input JSON, output outline). Caja 3 'Redacción' (input outline, output borrador). Caja 4 'Revisión de tono' (input borrador, output comunicado revisado con marcas). Caja 5 'Formato final' (input revisado, output HTML/PDF con membrete). Flechas etiquetadas con el tipo de paso de contexto. Bajo el pipeline, una pequeña etiqueta de versión 'pipeline-comunicado-v2.1'. Estilo limpio.

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
2. Guárdala como `assets/visuales/manual-4/u01/M4-u01-07.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 4
   python print_to_pdf.py --manual 4 --all-semesters
   ```

4. Verifica que `M4-u01-07` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
