---
id: M3-sem1-02
manual: 3
unidad: sem1
semestre: 1
tipo: ilustracion
paginas_ocupa: 0.5
fuente_md: manuales/manual-3/semestre-1/00-portada.md
fuente_md_linea: 26
imagen_destino: assets/visuales/manual-3/sem1/M3-sem1-02.jpg
pagina_pdf_estimada: 2
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: contenido del manual
status: pendiente
---

# `M3-sem1-02`

**Tipo visual:** `ilustracion` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 2

**Manual 3 · SEM1 — Front/Back matter — Semestre 1 · Semestre 1**

> Rol del archivo: _contenido del manual_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-sem1-02` |
| Archivo destino imagen | `assets/visuales/manual-3/sem1/M3-sem1-02.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 2** |
| Archivo Markdown fuente | `manuales/manual-3/semestre-1/00-portada.md:26` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Pieza de créditos editoriales: logo Albatros centrado en azul Albatros sobre fondo blanco, debajo el texto 'Grupo Cultural Albatros · Edición Tecno · 2026', y al pie tres líneas finas naranja como ornamento. Composición simple, simétrica, tipografía sans-serif moderna.  
> _Nota:_ página de créditos institucionales

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **SEM1 — Front/Back matter — Semestre 1**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **contenido del manual**
- Tipo de visual: **ilustracion**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Pieza de créditos editoriales: logo Albatros centrado en azul Albatros sobre fondo blanco, debajo el texto 'Grupo Cultural Albatros · Edición Tecno · 2026', y al pie tres líneas finas naranja como ornamento. Composición simple, simétrica, tipografía sans-serif moderna.  
- **Nota editorial:** página de créditos institucionales

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
2. Guárdala como `assets/visuales/manual-3/sem1/M3-sem1-02.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-sem1-02` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
