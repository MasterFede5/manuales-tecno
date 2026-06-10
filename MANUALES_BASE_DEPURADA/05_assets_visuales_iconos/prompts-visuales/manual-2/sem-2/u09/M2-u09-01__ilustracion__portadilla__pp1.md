---
id: M2-u09-01
manual: 2
unidad: u09
semestre: 2
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-2/unidades/u09/00-portadilla.md
fuente_md_linea: 13
imagen_destino: assets/visuales/manual-2/u09/M2-u09-01.jpg
pagina_pdf_estimada: 175
pdf_destino: dist/manual-2-sem-2.pdf
rol_archivo: portadilla
status: pendiente
---

# `M2-u09-01`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 175

**Manual 2 · U09 — Física Contemporánea · Semestre 2**

> Rol del archivo: _portadilla_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u09-01` |
| Archivo destino imagen | `assets/visuales/manual-2/u09/M2-u09-01.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-2.pdf` |
| Página PDF estimada | **p. 175** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u09/00-portadilla.md:13` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Ilustración hero de cuatro elementos: 1) Modelo atómico de Bohr con núcleo y electrones en órbitas circulares y emisión de fotón al cambiar de nivel. 2) Símbolo nuclear con N y P y la fórmula E=mc² destacada. 3) Panel solar fotovoltaico recibiendo rayos del Sol con flechas de electrones saliendo. 4) Coche F1 escolar con celda solar pequeña encima y carga eléctrica conectada al motor. Paleta tecno azul/naranja con destellos amarillos.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U09 — Física Contemporánea**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **portadilla**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Ilustración hero de cuatro elementos: 1) Modelo atómico de Bohr con núcleo y electrones en órbitas circulares y emisión de fotón al cambiar de nivel. 2) Símbolo nuclear con N y P y la fórmula E=mc² destacada. 3) Panel solar fotovoltaico recibiendo rayos del Sol con flechas de electrones saliendo. 4) Coche F1 escolar con celda solar pequeña encima y carga eléctrica conectada al motor. Paleta tecno azul/naranja con destellos amarillos.

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
2. Guárdala como `assets/visuales/manual-2/u09/M2-u09-01.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u09-01` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
