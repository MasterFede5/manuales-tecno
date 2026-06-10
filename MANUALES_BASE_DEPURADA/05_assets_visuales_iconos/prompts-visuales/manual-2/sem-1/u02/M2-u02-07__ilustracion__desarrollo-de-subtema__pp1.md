---
id: M2-u02-07
manual: 2
unidad: u02
semestre: 1
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-2/unidades/u02/10-tema-2-5.md
fuente_md_linea: 87
imagen_destino: assets/visuales/manual-2/u02/M2-u02-07.jpg
pagina_pdf_estimada: 93
pdf_destino: dist/manual-2-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M2-u02-07`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 93

**Manual 2 · U02 — Dinámica (Fuerzas) · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u02-07` |
| Archivo destino imagen | `assets/visuales/manual-2/u02/M2-u02-07.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-1.pdf` |
| Página PDF estimada | **p. 93** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u02/10-tema-2-5.md:87` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Dos viñetas: izquierda TORCA — llave inglesa apretando tuerca con brazo de palanca r horizontal y fuerza F aplicada perpendicular al final de la llave, vector torca τ representado saliendo del eje, fórmula τ=rF sin θ. Derecha EQUILIBRIO ROTACIONAL — balanza de brazos con masas m1 y m2 a distancias r1 y r2 del pivote, ecuación m1·r1 = m2·r2, anotación 'Arquímedes, siglo III a.C.'.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U02 — Dinámica (Fuerzas)**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Dos viñetas: izquierda TORCA — llave inglesa apretando tuerca con brazo de palanca r horizontal y fuerza F aplicada perpendicular al final de la llave, vector torca τ representado saliendo del eje, fórmula τ=rF sin θ. Derecha EQUILIBRIO ROTACIONAL — balanza de brazos con masas m1 y m2 a distancias r1 y r2 del pivote, ecuación m1·r1 = m2·r2, anotación 'Arquímedes, siglo III a.C.'.

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
2. Guárdala como `assets/visuales/manual-2/u02/M2-u02-07.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u02-07` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
