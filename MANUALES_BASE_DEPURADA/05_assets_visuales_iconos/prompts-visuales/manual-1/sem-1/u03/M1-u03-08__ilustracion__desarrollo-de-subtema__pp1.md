---
id: M1-u03-08
manual: 1
unidad: u03
semestre: 1
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-1/unidades/u03/10-tema-3-6.md
fuente_md_linea: 95
imagen_destino: assets/visuales/manual-1/u03/M1-u03-08.jpg
pagina_pdf_estimada: 216
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M1-u03-08`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 216

**Manual 1 · U03 — Aire · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u03-08` |
| Archivo destino imagen | `assets/visuales/manual-1/u03/M1-u03-08.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-1.pdf` |
| Página PDF estimada | **p. 216** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u03/10-tema-3-6.md:95` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Cuatro paneles ilustrativos: 1) Smog fotoquímico - silueta urbana con sol y flechas mostrando NOx + COV + UV → O3 + haze anaranjado; 2) Inversión térmica - corte vertical con capa fría abajo (azul, llena de humo) y capa caliente arriba (naranja, limpia); 3) Lluvia ácida - chimeneas emiten SO2/NOx, reacciones en nube → H2SO4/HNO3, gotas cayendo sobre bosque deteriorado; 4) Efecto invernadero - Tierra con sol incidente, radiación IR saliente parcialmente reflejada por capa de gases (CO2, CH4) hacia el suelo. Cada panel con etiqueta y reacción química clave.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U03 — Aire**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuatro paneles ilustrativos: 1) Smog fotoquímico - silueta urbana con sol y flechas mostrando NOx + COV + UV → O3 + haze anaranjado; 2) Inversión térmica - corte vertical con capa fría abajo (azul, llena de humo) y capa caliente arriba (naranja, limpia); 3) Lluvia ácida - chimeneas emiten SO2/NOx, reacciones en nube → H2SO4/HNO3, gotas cayendo sobre bosque deteriorado; 4) Efecto invernadero - Tierra con sol incidente, radiación IR saliente parcialmente reflejada por capa de gases (CO2, CH4) hacia el suelo. Cada panel con etiqueta y reacción química clave.

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
2. Guárdala como `assets/visuales/manual-1/u03/M1-u03-08.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u03-08` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
