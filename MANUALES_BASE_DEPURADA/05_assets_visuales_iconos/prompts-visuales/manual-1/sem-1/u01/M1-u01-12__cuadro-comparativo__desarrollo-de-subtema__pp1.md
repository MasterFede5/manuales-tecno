---
id: M1-u01-12
manual: 1
unidad: u01
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 1
fuente_md: manuales/manual-1/unidades/u01/10-tema-1-7.md
fuente_md_linea: 168
imagen_destino: assets/visuales/manual-1/u01/M1-u01-12.jpg
pagina_pdf_estimada: 99
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M1-u01-12`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 1 pp · **Página PDF estimada:** 99

**Manual 1 · U01 — Temas Básicos de la Materia · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u01-12` |
| Archivo destino imagen | `assets/visuales/manual-1/u01/M1-u01-12.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-1.pdf` |
| Página PDF estimada | **p. 99** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u01/10-tema-1-7.md:168` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Cuadro comparativo de los tres sistemas de nomenclatura aplicados a 8 compuestos comunes (NaCl, CaO, Fe₂O₃, H₂SO₄, NaOH, HClO, NaClO, CaCO₃) con columnas para fórmula, nomenclatura sistemática IUPAC, Stock con número romano y tradicional con sufijos. Marca con fondo amarillo los compuestos presentes en el agua del bebedero (cloruro de sodio, hipoclorito, carbonato de calcio).  
> _Nota:_ incluir nota al pie sobre el sistema preferido por la IUPAC moderna

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
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro comparativo de los tres sistemas de nomenclatura aplicados a 8 compuestos comunes (NaCl, CaO, Fe₂O₃, H₂SO₄, NaOH, HClO, NaClO, CaCO₃) con columnas para fórmula, nomenclatura sistemática IUPAC, Stock con número romano y tradicional con sufijos. Marca con fondo amarillo los compuestos presentes en el agua del bebedero (cloruro de sodio, hipoclorito, carbonato de calcio).  
- **Nota editorial:** incluir nota al pie sobre el sistema preferido por la IUPAC moderna

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
2. Guárdala como `assets/visuales/manual-1/u01/M1-u01-12.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u01-12` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
