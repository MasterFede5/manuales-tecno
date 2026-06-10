---
id: M2-u09-03
manual: 2
unidad: u09
semestre: 2
tipo: linea-tiempo
paginas_ocupa: 1
fuente_md: manuales/manual-2/unidades/u09/10-tema-9-1.md
fuente_md_linea: 42
imagen_destino: assets/visuales/manual-2/u09/M2-u09-03.jpg
pagina_pdf_estimada: 178
pdf_destino: dist/manual-2-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M2-u09-03`

**Tipo visual:** `linea-tiempo` · **Ocupa:** 1 pp · **Página PDF estimada:** 178

**Manual 2 · U09 — Física Contemporánea · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u09-03` |
| Archivo destino imagen | `assets/visuales/manual-2/u09/M2-u09-03.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-2.pdf` |
| Página PDF estimada | **p. 178** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u09/10-tema-9-1.md:42` |
| Tipo de placeholder | `linea-tiempo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Línea horizontal con cinco hitos atómicos: 1808 DALTON (esfera indivisible), 1897 THOMSON (pudín de pasas con electrones embebidos en gel positivo), 1911 RUTHERFORD (núcleo denso con electrones orbitando lejanos), 1913 BOHR (órbitas circulares con energías cuantizadas, saltos electrónicos con emisión de fotón), 1926 SCHRÖDINGER-HEISENBERG (orbitales como nubes de probabilidad y principio de incertidumbre). Cada hito con dibujo, fecha, autor principal y experimento decisivo.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U09 — Física Contemporánea**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **linea-tiempo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (linea-tiempo):**
LÍNEA DE TIEMPO horizontal con eje cronológico central, hitos como cápsulas con fecha + título + micro-ilustración + frase corta.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Línea horizontal con cinco hitos atómicos: 1808 DALTON (esfera indivisible), 1897 THOMSON (pudín de pasas con electrones embebidos en gel positivo), 1911 RUTHERFORD (núcleo denso con electrones orbitando lejanos), 1913 BOHR (órbitas circulares con energías cuantizadas, saltos electrónicos con emisión de fotón), 1926 SCHRÖDINGER-HEISENBERG (orbitales como nubes de probabilidad y principio de incertidumbre). Cada hito con dibujo, fecha, autor principal y experimento decisivo.

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
2. Guárdala como `assets/visuales/manual-2/u09/M2-u09-03.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u09-03` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
