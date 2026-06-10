---
id: M2-u02-08
manual: 2
unidad: u02
semestre: 1
tipo: grafica
paginas_ocupa: 0.5
fuente_md: manuales/manual-2/unidades/u02/10-tema-2-6.md
fuente_md_linea: 84
imagen_destino: assets/visuales/manual-2/u02/M2-u02-08.jpg
pagina_pdf_estimada: 98
pdf_destino: dist/manual-2-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M2-u02-08`

**Tipo visual:** `grafica` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 98

**Manual 2 · U02 — Dinámica (Fuerzas) · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u02-08` |
| Archivo destino imagen | `assets/visuales/manual-2/u02/M2-u02-08.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-1.pdf` |
| Página PDF estimada | **p. 98** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u02/10-tema-2-6.md:84` |
| Tipo de placeholder | `grafica` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Gráfica F vs x para un resorte: línea recta con pendiente positiva en el rango elástico (Ley de Hooke F=kx), zona elástica marcada en verde con anotación 'el resorte regresa', luego curva que se desvía marcando el límite elástico (zona amarilla 'deformación plástica' donde queda permanente), finalmente ruptura en zona roja. Anexo con tres ilustraciones de resorte: en reposo, comprimido con flecha de fuerza opuesta, y estirado.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U02 — Dinámica (Fuerzas)**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **grafica**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (grafica):**
GRÁFICA CIENTÍFICA limpia: ejes etiquetados con magnitud+unidad, cuadrícula tenue, una o dos series, leyenda compacta arriba derecha.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Gráfica F vs x para un resorte: línea recta con pendiente positiva en el rango elástico (Ley de Hooke F=kx), zona elástica marcada en verde con anotación 'el resorte regresa', luego curva que se desvía marcando el límite elástico (zona amarilla 'deformación plástica' donde queda permanente), finalmente ruptura en zona roja. Anexo con tres ilustraciones de resorte: en reposo, comprimido con flecha de fuerza opuesta, y estirado.

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
2. Guárdala como `assets/visuales/manual-2/u02/M2-u02-08.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u02-08` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
