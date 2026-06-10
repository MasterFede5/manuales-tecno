---
id: M1-sem1-01
manual: 1
unidad: sem1
semestre: 1
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-1/semestre-1/00-portada.md
fuente_md_linea: 18
imagen_destino: assets/visuales/manual-1/sem1/M1-sem1-01.jpg
pagina_pdf_estimada: 1
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: contenido del manual
status: pendiente
---

# `M1-sem1-01`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 1

**Manual 1 · SEM1 — Front/Back matter — Semestre 1 · Semestre 1**

> Rol del archivo: _contenido del manual_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-sem1-01` |
| Archivo destino imagen | `assets/visuales/manual-1/sem1/M1-sem1-01.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-1.pdf` |
| Página PDF estimada | **p. 1** |
| Archivo Markdown fuente | `manuales/manual-1/semestre-1/00-portada.md:18` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Ilustración hero de portada para el Semestre 1 del Manual 1: Química Albatros. Composición editorial vertical con el logo Albatros en la esquina superior derecha, título grande del manual, subtítulo, barra cromática azul Albatros + matraces verdes, y al centro un escenario evocador del case study 'Agua escolar saludable' que conecta visualmente las unidades del semestre (Lenguaje del Químico, Temas Básicos de la Materia, Agua, Aire). Tono editorial, sin photoreal, paleta azul Albatros con acento naranja.  
> _Nota:_ hero de portada del semestre — eje narrativo del case study

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **SEM1 — Front/Back matter — Semestre 1**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **contenido del manual**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Ilustración hero de portada para el Semestre 1 del Manual 1: Química Albatros. Composición editorial vertical con el logo Albatros en la esquina superior derecha, título grande del manual, subtítulo, barra cromática azul Albatros + matraces verdes, y al centro un escenario evocador del case study 'Agua escolar saludable' que conecta visualmente las unidades del semestre (Lenguaje del Químico, Temas Básicos de la Materia, Agua, Aire). Tono editorial, sin photoreal, paleta azul Albatros con acento naranja.  
- **Nota editorial:** hero de portada del semestre — eje narrativo del case study

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
2. Guárdala como `assets/visuales/manual-1/sem1/M1-sem1-01.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-sem1-01` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
