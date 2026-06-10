---
id: M1-sem1-06
manual: 1
unidad: sem1
semestre: 1
tipo: linea-tiempo
paginas_ocupa: 1
fuente_md: manuales/manual-1/semestre-1/04-hilo-conductor.md
fuente_md_linea: 30
imagen_destino: assets/visuales/manual-1/sem1/M1-sem1-06.jpg
pagina_pdf_estimada: 8
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: contenido del manual
status: pendiente
---

# `M1-sem1-06`

**Tipo visual:** `linea-tiempo` · **Ocupa:** 1 pp · **Página PDF estimada:** 8

**Manual 1 · SEM1 — Front/Back matter — Semestre 1 · Semestre 1**

> Rol del archivo: _contenido del manual_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-sem1-06` |
| Archivo destino imagen | `assets/visuales/manual-1/sem1/M1-sem1-06.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-1.pdf` |
| Página PDF estimada | **p. 8** |
| Archivo Markdown fuente | `manuales/manual-1/semestre-1/04-hilo-conductor.md:30` |
| Tipo de placeholder | `linea-tiempo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Línea de tiempo horizontal del semestre 1: en el extremo izquierdo, el problema inicial del case study 'Agua escolar saludable'; en el centro, 4 hitos correspondientes a los episodios de cada unidad (u00, u01, u02, u03); en el extremo derecho, el entregable final del portafolio del semestre. Cada hito con fecha tentativa (semana N), título corto y micro-ilustración temática.  
> _Nota:_ visión panorámica del hilo conductor del semestre

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **SEM1 — Front/Back matter — Semestre 1**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **contenido del manual**
- Tipo de visual: **linea-tiempo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (linea-tiempo):**
LÍNEA DE TIEMPO horizontal con eje cronológico central, hitos como cápsulas con fecha + título + micro-ilustración + frase corta.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Línea de tiempo horizontal del semestre 1: en el extremo izquierdo, el problema inicial del case study 'Agua escolar saludable'; en el centro, 4 hitos correspondientes a los episodios de cada unidad (u00, u01, u02, u03); en el extremo derecho, el entregable final del portafolio del semestre. Cada hito con fecha tentativa (semana N), título corto y micro-ilustración temática.  
- **Nota editorial:** visión panorámica del hilo conductor del semestre

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
2. Guárdala como `assets/visuales/manual-1/sem1/M1-sem1-06.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-sem1-06` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
