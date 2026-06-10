---
id: M1-u04-07
manual: 1
unidad: u04
semestre: 2
tipo: infografia
paginas_ocupa: 1
fuente_md: manuales/manual-1/unidades/u04/10-tema-4-5.md
fuente_md_linea: 126
imagen_destino: assets/visuales/manual-1/u04/M1-u04-07.jpg
pagina_pdf_estimada: 33
pdf_destino: dist/manual-1-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M1-u04-07`

**Tipo visual:** `infografia` · **Ocupa:** 1 pp · **Página PDF estimada:** 33

**Manual 1 · U04 — Alimentos · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u04-07` |
| Archivo destino imagen | `assets/visuales/manual-1/u04/M1-u04-07.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-2.pdf` |
| Página PDF estimada | **p. 33** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u04/10-tema-4-5.md:126` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Infografía de cuatro reacciones culinarias clave en cuadrantes: 1) Maillard arriba-izquierda (filete asado, café, pan tostado con flecha aminoacido + azúcar + calor → compuestos pardos aromáticos), 2) Caramelización arriba-derecha (caramelo, flan con flecha azúcar + calor → marrón dulce), 3) Fermentación abajo-izquierda (pulque, queso, pan con flechas glucosa → etanol+CO2 o ácido láctico), 4) Oxidación enzimática abajo-derecha (manzana cortada con flecha polifenoles + O2 + enzima → melanina marrón).

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U04 — Alimentos**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **infografia**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Infografía de cuatro reacciones culinarias clave en cuadrantes: 1) Maillard arriba-izquierda (filete asado, café, pan tostado con flecha aminoacido + azúcar + calor → compuestos pardos aromáticos), 2) Caramelización arriba-derecha (caramelo, flan con flecha azúcar + calor → marrón dulce), 3) Fermentación abajo-izquierda (pulque, queso, pan con flechas glucosa → etanol+CO2 o ácido láctico), 4) Oxidación enzimática abajo-derecha (manzana cortada con flecha polifenoles + O2 + enzima → melanina marrón).

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
2. Guárdala como `assets/visuales/manual-1/u04/M1-u04-07.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u04-07` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
