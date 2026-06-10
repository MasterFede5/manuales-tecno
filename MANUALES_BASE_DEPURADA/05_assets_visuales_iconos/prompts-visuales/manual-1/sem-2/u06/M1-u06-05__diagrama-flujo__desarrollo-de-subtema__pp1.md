---
id: M1-u06-05
manual: 1
unidad: u06
semestre: 2
tipo: diagrama-flujo
paginas_ocupa: 1
fuente_md: manuales/manual-1/unidades/u06/10-tema-6-3.md
fuente_md_linea: 93
imagen_destino: assets/visuales/manual-1/u06/M1-u06-05.jpg
pagina_pdf_estimada: 152
pdf_destino: dist/manual-1-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M1-u06-05`

**Tipo visual:** `diagrama-flujo` · **Ocupa:** 1 pp · **Página PDF estimada:** 152

**Manual 1 · U06 — Seguridad Industrial · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u06-05` |
| Archivo destino imagen | `assets/visuales/manual-1/u06/M1-u06-05.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-2.pdf` |
| Página PDF estimada | **p. 152** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u06/10-tema-6-3.md:93` |
| Tipo de placeholder | `diagrama-flujo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Diagrama de flujo horizontal del ciclo de residuos peligrosos: GENERACIÓN (icono de matraz con símbolo CRETIB) → SEPARACIÓN POR TIPO (envases coloreados según norma) → ETIQUETADO Y BITÁCORA (etiqueta con fecha y CRETIB) → ALMACENAMIENTO TEMPORAL <6 meses (área señalizada con piso impermeable) → TRANSPORTE POR EMPRESA AUTORIZADA (camión con manifiesto) → DESTINO FINAL (reciclaje, tratamiento, incineración o confinamiento). Bajo cada paso, la NOM mexicana aplicable.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U06 — Seguridad Industrial**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **diagrama-flujo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (diagrama-flujo):**
DIAGRAMA DE FLUJO: cajas redondeadas conectadas por flechas, rombos para decisiones, azul Albatros para procesos, naranja para decisión, sin cruces.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Diagrama de flujo horizontal del ciclo de residuos peligrosos: GENERACIÓN (icono de matraz con símbolo CRETIB) → SEPARACIÓN POR TIPO (envases coloreados según norma) → ETIQUETADO Y BITÁCORA (etiqueta con fecha y CRETIB) → ALMACENAMIENTO TEMPORAL <6 meses (área señalizada con piso impermeable) → TRANSPORTE POR EMPRESA AUTORIZADA (camión con manifiesto) → DESTINO FINAL (reciclaje, tratamiento, incineración o confinamiento). Bajo cada paso, la NOM mexicana aplicable.

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
2. Guárdala como `assets/visuales/manual-1/u06/M1-u06-05.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u06-05` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
