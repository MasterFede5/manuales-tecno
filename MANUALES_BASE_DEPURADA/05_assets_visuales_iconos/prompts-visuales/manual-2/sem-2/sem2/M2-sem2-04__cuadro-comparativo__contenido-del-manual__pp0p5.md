---
id: M2-sem2-04
manual: 2
unidad: sem2
semestre: 2
tipo: cuadro-comparativo
paginas_ocupa: 0.5
fuente_md: manuales/manual-2/semestre-2/02-carta-docente.md
fuente_md_linea: 56
imagen_destino: assets/visuales/manual-2/sem2/M2-sem2-04.jpg
pagina_pdf_estimada: 4
pdf_destino: dist/manual-2-sem-2.pdf
rol_archivo: contenido del manual
status: pendiente
---

# `M2-sem2-04`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 4

**Manual 2 · SEM2 — Front/Back matter — Semestre 2 · Semestre 2**

> Rol del archivo: _contenido del manual_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-sem2-04` |
| Archivo destino imagen | `assets/visuales/manual-2/sem2/M2-sem2-04.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-2.pdf` |
| Página PDF estimada | **p. 4** |
| Archivo Markdown fuente | `manuales/manual-2/semestre-2/02-carta-docente.md:56` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Cuadro comparativo de 3 columnas: 'Enfoque tradicional' vs 'Enfoque Albatros' vs 'Beneficio esperado'. Filas: rol del docente, papel del estudiante, fuente de evidencia, evaluación, ritmo de avance, integración del caso real. Encabezado azul Albatros con texto blanco, zebra sutil en filas.  
> _Nota:_ ayuda visual para que el docente identifique los cambios metodológicos

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **SEM2 — Front/Back matter — Semestre 2**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **contenido del manual**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro comparativo de 3 columnas: 'Enfoque tradicional' vs 'Enfoque Albatros' vs 'Beneficio esperado'. Filas: rol del docente, papel del estudiante, fuente de evidencia, evaluación, ritmo de avance, integración del caso real. Encabezado azul Albatros con texto blanco, zebra sutil en filas.  
- **Nota editorial:** ayuda visual para que el docente identifique los cambios metodológicos

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
2. Guárdala como `assets/visuales/manual-2/sem2/M2-sem2-04.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-sem2-04` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
