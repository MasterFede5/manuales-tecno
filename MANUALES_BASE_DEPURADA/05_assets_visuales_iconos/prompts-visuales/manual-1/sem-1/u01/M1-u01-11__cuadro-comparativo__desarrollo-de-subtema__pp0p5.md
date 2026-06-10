---
id: M1-u01-11
manual: 1
unidad: u01
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 0.5
fuente_md: manuales/manual-1/unidades/u01/10-tema-1-6.md
fuente_md_linea: 136
imagen_destino: assets/visuales/manual-1/u01/M1-u01-11.jpg
pagina_pdf_estimada: 93
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M1-u01-11`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 93

**Manual 1 · U01 — Temas Básicos de la Materia · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u01-11` |
| Archivo destino imagen | `assets/visuales/manual-1/u01/M1-u01-11.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-1.pdf` |
| Página PDF estimada | **p. 93** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u01/10-tema-1-6.md:136` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Cuadro comparativo de las cuatro fuerzas intermoleculares: dispersión de London (presente en todas las moléculas, energía 0.05-40 kJ/mol, ejemplo CH4), dipolo-dipolo (moléculas polares, 5-25 kJ/mol, ejemplo HCl), puente de hidrógeno (H unido a F, O o N, 10-40 kJ/mol, ejemplo H2O), ion-dipolo (iones disueltos, 40-600 kJ/mol, ejemplo NaCl en agua). Cada fila con esquema visual de la interacción y aplicación cotidiana.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U01 — Temas Básicos de la Materia**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro comparativo de las cuatro fuerzas intermoleculares: dispersión de London (presente en todas las moléculas, energía 0.05-40 kJ/mol, ejemplo CH4), dipolo-dipolo (moléculas polares, 5-25 kJ/mol, ejemplo HCl), puente de hidrógeno (H unido a F, O o N, 10-40 kJ/mol, ejemplo H2O), ion-dipolo (iones disueltos, 40-600 kJ/mol, ejemplo NaCl en agua). Cada fila con esquema visual de la interacción y aplicación cotidiana.

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
2. Guárdala como `assets/visuales/manual-1/u01/M1-u01-11.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u01-11` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
