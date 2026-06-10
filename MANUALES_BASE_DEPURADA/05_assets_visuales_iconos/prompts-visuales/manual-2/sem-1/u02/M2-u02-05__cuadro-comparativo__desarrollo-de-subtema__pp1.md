---
id: M2-u02-05
manual: 2
unidad: u02
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 1
fuente_md: manuales/manual-2/unidades/u02/10-tema-2-3.md
fuente_md_linea: 103
imagen_destino: assets/visuales/manual-2/u02/M2-u02-05.jpg
pagina_pdf_estimada: 84
pdf_destino: dist/manual-2-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M2-u02-05`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 1 pp · **Página PDF estimada:** 84

**Manual 2 · U02 — Dinámica (Fuerzas) · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u02-05` |
| Archivo destino imagen | `assets/visuales/manual-2/u02/M2-u02-05.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-1.pdf` |
| Página PDF estimada | **p. 84** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u02/10-tema-2-3.md:103` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Cuadro comparativo en dos columnas: MASA (escalar, kg, propiedad intrínseca, balanza, ejemplo: 70 kg) vs PESO (vector fuerza, N, gravitatoria, dinamómetro, cambia con ubicación). Tabla anexa con peso de una persona de 70 kg en distintos cuerpos celestes: Tierra 686 N, Luna 113 N, Marte 259 N, Júpiter 1735 N, Sol 19,180 N. Ilustración del astronauta saltando en la Luna por su menor peso.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U02 — Dinámica (Fuerzas)**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro comparativo en dos columnas: MASA (escalar, kg, propiedad intrínseca, balanza, ejemplo: 70 kg) vs PESO (vector fuerza, N, gravitatoria, dinamómetro, cambia con ubicación). Tabla anexa con peso de una persona de 70 kg en distintos cuerpos celestes: Tierra 686 N, Luna 113 N, Marte 259 N, Júpiter 1735 N, Sol 19,180 N. Ilustración del astronauta saltando en la Luna por su menor peso.

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
2. Guárdala como `assets/visuales/manual-2/u02/M2-u02-05.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u02-05` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
