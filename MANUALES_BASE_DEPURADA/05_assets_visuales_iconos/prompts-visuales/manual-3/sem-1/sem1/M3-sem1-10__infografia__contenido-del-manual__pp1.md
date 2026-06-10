---
id: M3-sem1-10
manual: 3
unidad: sem1
semestre: 1
tipo: infografia
paginas_ocupa: 1
fuente_md: manuales/manual-3/semestre-1/91-material-extra.md
fuente_md_linea: 91
imagen_destino: assets/visuales/manual-3/sem1/M3-sem1-10.jpg
pagina_pdf_estimada: 300
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: contenido del manual
status: pendiente
---

# `M3-sem1-10`

**Tipo visual:** `infografia` · **Ocupa:** 1 pp · **Página PDF estimada:** 300

**Manual 3 · SEM1 — Front/Back matter — Semestre 1 · Semestre 1**

> Rol del archivo: _contenido del manual_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-sem1-10` |
| Archivo destino imagen | `assets/visuales/manual-3/sem1/M3-sem1-10.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 300** |
| Archivo Markdown fuente | `manuales/manual-3/semestre-1/91-material-extra.md:91` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Infografía resumen del semestre completo en una sola hoja: panel superior con el case study, panel medio con las 5 unidades del semestre como columnas (cada columna con título, ícono y entregable), panel inferior con los 3 hábitos de estudio Albatros y el portafolio final. Paleta azul Albatros + naranja, listo para colgar en el cuaderno.  
> _Nota:_ resumen visual del semestre — útil como póster del estudiante

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **SEM1 — Front/Back matter — Semestre 1**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **contenido del manual**
- Tipo de visual: **infografia**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Infografía resumen del semestre completo en una sola hoja: panel superior con el case study, panel medio con las 5 unidades del semestre como columnas (cada columna con título, ícono y entregable), panel inferior con los 3 hábitos de estudio Albatros y el portafolio final. Paleta azul Albatros + naranja, listo para colgar en el cuaderno.  
- **Nota editorial:** resumen visual del semestre — útil como póster del estudiante

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
2. Guárdala como `assets/visuales/manual-3/sem1/M3-sem1-10.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-sem1-10` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
