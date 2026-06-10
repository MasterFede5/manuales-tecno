---
id: M1-u02-06
manual: 1
unidad: u02
semestre: 1
tipo: infografia
paginas_ocupa: 1
fuente_md: manuales/manual-1/unidades/u02/10-tema-2-4.md
fuente_md_linea: 88
imagen_destino: assets/visuales/manual-1/u02/M1-u02-06.jpg
pagina_pdf_estimada: 148
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M1-u02-06`

**Tipo visual:** `infografia` · **Ocupa:** 1 pp · **Página PDF estimada:** 148

**Manual 1 · U02 — Agua · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u02-06` |
| Archivo destino imagen | `assets/visuales/manual-1/u02/M1-u02-06.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-1.pdf` |
| Página PDF estimada | **p. 148** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u02/10-tema-2-4.md:88` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Infografía vertical de la escala de pH de 0 a 14 con franja de colores (rojo intenso a violeta) y 12 ejemplos cotidianos etiquetados a su pH correspondiente: ácido de batería 0, ácido estomacal 1, jugo de limón 2, Coca-Cola 2.5, vinagre 3, café 5, leche 6.5, agua pura 7, sangre 7.4, bicarbonato 9, amoniaco 11, lejía 13. Indicador con flecha del rango aceptable para agua potable (6.5-8.5) en verde.  
> _Nota:_ incluir leyenda con definiciones operativas y la fórmula pH = -log[H+]

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U02 — Agua**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **infografia**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Infografía vertical de la escala de pH de 0 a 14 con franja de colores (rojo intenso a violeta) y 12 ejemplos cotidianos etiquetados a su pH correspondiente: ácido de batería 0, ácido estomacal 1, jugo de limón 2, Coca-Cola 2.5, vinagre 3, café 5, leche 6.5, agua pura 7, sangre 7.4, bicarbonato 9, amoniaco 11, lejía 13. Indicador con flecha del rango aceptable para agua potable (6.5-8.5) en verde.  
- **Nota editorial:** incluir leyenda con definiciones operativas y la fórmula pH = -log[H+]

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
2. Guárdala como `assets/visuales/manual-1/u02/M1-u02-06.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u02-06` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
