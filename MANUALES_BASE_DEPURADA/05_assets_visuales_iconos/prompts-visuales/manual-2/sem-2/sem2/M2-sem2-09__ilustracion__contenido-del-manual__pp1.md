---
id: M2-sem2-09
manual: 2
unidad: sem2
semestre: 2
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-2/semestre-2/90-cierre-semestre.md
fuente_md_linea: 57
imagen_destino: assets/visuales/manual-2/sem2/M2-sem2-09.jpg
pagina_pdf_estimada: 227
pdf_destino: dist/manual-2-sem-2.pdf
rol_archivo: contenido del manual
status: pendiente
---

# `M2-sem2-09`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 227

**Manual 2 · SEM2 — Front/Back matter — Semestre 2 · Semestre 2**

> Rol del archivo: _contenido del manual_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-sem2-09` |
| Archivo destino imagen | `assets/visuales/manual-2/sem2/M2-sem2-09.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-2.pdf` |
| Página PDF estimada | **p. 227** |
| Archivo Markdown fuente | `manuales/manual-2/semestre-2/90-cierre-semestre.md:57` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Ilustración de cierre cálida: un estudiante revisando su portafolio terminado con varias hojas y evidencias del case study sobre la mesa, mirada satisfecha, fondo de salón de clases o espacio personal. Al pie de la ilustración, un cohete pequeño apuntando hacia arriba (símbolo del siguiente semestre). Paleta azul Albatros + naranja, outline + duotone.  
> _Nota:_ pieza emocional de cierre del semestre

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **SEM2 — Front/Back matter — Semestre 2**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **contenido del manual**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Ilustración de cierre cálida: un estudiante revisando su portafolio terminado con varias hojas y evidencias del case study sobre la mesa, mirada satisfecha, fondo de salón de clases o espacio personal. Al pie de la ilustración, un cohete pequeño apuntando hacia arriba (símbolo del siguiente semestre). Paleta azul Albatros + naranja, outline + duotone.  
- **Nota editorial:** pieza emocional de cierre del semestre

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
2. Guárdala como `assets/visuales/manual-2/sem2/M2-sem2-09.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-sem2-09` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
