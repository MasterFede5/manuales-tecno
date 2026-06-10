---
id: M4-u09-07
manual: 4
unidad: u09
semestre: 2
tipo: cuadro-comparativo
paginas_ocupa: 1
fuente_md: manuales/manual-4/unidades/u09/10-tema-9-5.md
fuente_md_linea: 60
imagen_destino: assets/visuales/manual-4/u09/M4-u09-07.jpg
pagina_pdf_estimada: 264
pdf_destino: dist/manual-4-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M4-u09-07`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 1 pp · **Página PDF estimada:** 264

**Manual 4 · U09 — Material educativo certificable · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M4-u09-07` |
| Archivo destino imagen | `assets/visuales/manual-4/u09/M4-u09-07.jpg` |
| PDF en el que aparece | `dist/manual-4-sem-2.pdf` |
| Página PDF estimada | **p. 264** |
| Archivo Markdown fuente | `manuales/manual-4/unidades/u09/10-tema-9-5.md:60` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Cuadro a tamaño página de 8 tipos de contenido legal en filas. Columnas: nivel de riesgo (con código de color), si IA puede ayudar, qué porcentaje, validación humana requerida, disclaimer obligatorio sí/no, frecuencia de revisión. Bajo el cuadro, plantilla de disclaimer estándar y advertencia destacada: 'la IA NO sustituye asesoría legal. Es herramienta de aceleración, no sustitución'. Estilo Albatros con tono serio.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Avanzada** — Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza
- Unidad: **U09 — Material educativo certificable**
- Case study: *Asistente Institucional Albatros — IA con herramientas reales*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro a tamaño página de 8 tipos de contenido legal en filas. Columnas: nivel de riesgo (con código de color), si IA puede ayudar, qué porcentaje, validación humana requerida, disclaimer obligatorio sí/no, frecuencia de revisión. Bajo el cuadro, plantilla de disclaimer estándar y advertencia destacada: 'la IA NO sustituye asesoría legal. Es herramienta de aceleración, no sustitución'. Estilo Albatros con tono serio.

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
2. Guárdala como `assets/visuales/manual-4/u09/M4-u09-07.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 4
   python print_to_pdf.py --manual 4 --all-semesters
   ```

4. Verifica que `M4-u09-07` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
