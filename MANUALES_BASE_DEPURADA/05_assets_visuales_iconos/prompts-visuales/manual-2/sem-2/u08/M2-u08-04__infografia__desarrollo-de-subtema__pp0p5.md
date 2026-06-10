---
id: M2-u08-04
manual: 2
unidad: u08
semestre: 2
tipo: infografia
paginas_ocupa: 0.5
fuente_md: manuales/manual-2/unidades/u08/10-tema-8-1.md
fuente_md_linea: 90
imagen_destino: assets/visuales/manual-2/u08/M2-u08-04.jpg
pagina_pdf_estimada: 118
pdf_destino: dist/manual-2-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M2-u08-04`

**Tipo visual:** `infografia` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 118

**Manual 2 · U08 — Óptica · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u08-04` |
| Archivo destino imagen | `assets/visuales/manual-2/u08/M2-u08-04.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-2.pdf` |
| Página PDF estimada | **p. 118** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u08/10-tema-8-1.md:90` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Reflexión total interna en fibra óptica: corte longitudinal de un cable de fibra mostrando núcleo central con n₁ alto y revestimiento exterior con n₂ menor; rayo de luz entrando por un extremo y rebotando en zigzag dentro del núcleo gracias a θ > θ_c, sin perderse al exterior. Anotación: ángulo crítico, fórmula sinθ_c=n₂/n₁; recuadro pequeño con cable submarino transatlántico y mapa de internet global.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U08 — Óptica**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **infografia**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Reflexión total interna en fibra óptica: corte longitudinal de un cable de fibra mostrando núcleo central con n₁ alto y revestimiento exterior con n₂ menor; rayo de luz entrando por un extremo y rebotando en zigzag dentro del núcleo gracias a θ > θ_c, sin perderse al exterior. Anotación: ángulo crítico, fórmula sinθ_c=n₂/n₁; recuadro pequeño con cable submarino transatlántico y mapa de internet global.

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
2. Guárdala como `assets/visuales/manual-2/u08/M2-u08-04.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u08-04` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
