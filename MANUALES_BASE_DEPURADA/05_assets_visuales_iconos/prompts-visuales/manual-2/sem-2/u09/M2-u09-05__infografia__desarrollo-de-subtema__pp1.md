---
id: M2-u09-05
manual: 2
unidad: u09
semestre: 2
tipo: infografia
paginas_ocupa: 1
fuente_md: manuales/manual-2/unidades/u09/10-tema-9-1.md
fuente_md_linea: 74
imagen_destino: assets/visuales/manual-2/u09/M2-u09-05.jpg
pagina_pdf_estimada: 180
pdf_destino: dist/manual-2-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M2-u09-05`

**Tipo visual:** `infografia` · **Ocupa:** 1 pp · **Página PDF estimada:** 180

**Manual 2 · U09 — Física Contemporánea · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u09-05` |
| Archivo destino imagen | `assets/visuales/manual-2/u09/M2-u09-05.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-2.pdf` |
| Página PDF estimada | **p. 180** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u09/10-tema-9-1.md:74` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Niveles de energía del átomo de hidrógeno según Bohr: cinco niveles concéntricos n=1 (más interno, -13.6 eV), n=2 (-3.4 eV), n=3 (-1.51 eV), n=4 (-0.85 eV), n=5 (-0.54 eV). Flechas de saltos electrónicos: a n=1 → serie LYMAN (UV), a n=2 → serie BALMER (visible: H_α rojo 656 nm, H_β verde-azul, H_γ violeta), a n=3 → serie PASCHEN (IR). Abajo, el espectro de emisión real del hidrógeno con líneas brillantes en las posiciones predichas.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U09 — Física Contemporánea**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **infografia**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Niveles de energía del átomo de hidrógeno según Bohr: cinco niveles concéntricos n=1 (más interno, -13.6 eV), n=2 (-3.4 eV), n=3 (-1.51 eV), n=4 (-0.85 eV), n=5 (-0.54 eV). Flechas de saltos electrónicos: a n=1 → serie LYMAN (UV), a n=2 → serie BALMER (visible: H_α rojo 656 nm, H_β verde-azul, H_γ violeta), a n=3 → serie PASCHEN (IR). Abajo, el espectro de emisión real del hidrógeno con líneas brillantes en las posiciones predichas.

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
2. Guárdala como `assets/visuales/manual-2/u09/M2-u09-05.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u09-05` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
