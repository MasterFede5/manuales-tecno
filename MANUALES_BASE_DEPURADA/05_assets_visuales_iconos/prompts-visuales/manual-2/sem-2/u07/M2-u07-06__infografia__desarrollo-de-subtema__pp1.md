---
id: M2-u07-06
manual: 2
unidad: u07
semestre: 2
tipo: infografia
paginas_ocupa: 1
fuente_md: manuales/manual-2/unidades/u07/10-tema-7-1.md
fuente_md_linea: 168
imagen_destino: assets/visuales/manual-2/u07/M2-u07-06.jpg
pagina_pdf_estimada: 63
pdf_destino: dist/manual-2-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M2-u07-06`

**Tipo visual:** `infografia` · **Ocupa:** 1 pp · **Página PDF estimada:** 63

**Manual 2 · U07 — Mecánica de Fluidos · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u07-06` |
| Archivo destino imagen | `assets/visuales/manual-2/u07/M2-u07-06.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-2.pdf` |
| Página PDF estimada | **p. 63** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u07/10-tema-7-1.md:168` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Tres bloques cúbicos del mismo tamaño sumergidos en agua. (1) Bloque de plomo: peso 11.3 N, empuje 1 N → se hunde. (2) Bloque de plástico: peso 1 N, empuje 1 N → flota a cualquier profundidad. (3) Corcho: peso 0.2 N, empuje 0.2 N pero sólo con parte sumergida → flota en la superficie. Cada bloque con flechas de peso (W, hacia abajo) y empuje (E, hacia arriba) en proporción correcta.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U07 — Mecánica de Fluidos**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **infografia**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Tres bloques cúbicos del mismo tamaño sumergidos en agua. (1) Bloque de plomo: peso 11.3 N, empuje 1 N → se hunde. (2) Bloque de plástico: peso 1 N, empuje 1 N → flota a cualquier profundidad. (3) Corcho: peso 0.2 N, empuje 0.2 N pero sólo con parte sumergida → flota en la superficie. Cada bloque con flechas de peso (W, hacia abajo) y empuje (E, hacia arriba) en proporción correcta.

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
2. Guárdala como `assets/visuales/manual-2/u07/M2-u07-06.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u07-06` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
