---
id: M1-u01-04
manual: 1
unidad: u01
semestre: 1
tipo: linea-tiempo
paginas_ocupa: 1
fuente_md: manuales/manual-1/unidades/u01/10-tema-1-2.md
fuente_md_linea: 43
imagen_destino: assets/visuales/manual-1/u01/M1-u01-04.jpg
pagina_pdf_estimada: 74
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M1-u01-04`

**Tipo visual:** `linea-tiempo` · **Ocupa:** 1 pp · **Página PDF estimada:** 74

**Manual 1 · U01 — Temas Básicos de la Materia · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u01-04` |
| Archivo destino imagen | `assets/visuales/manual-1/u01/M1-u01-04.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-1.pdf` |
| Página PDF estimada | **p. 74** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u01/10-tema-1-2.md:43` |
| Tipo de placeholder | `linea-tiempo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Línea de tiempo horizontal con los cinco modelos atómicos: Dalton 1803 (esfera maciza), Thomson 1897 (budín de pasas con electrones incrustados), Rutherford 1911 (núcleo central con electrones orbitando), Bohr 1913 (electrones en órbitas cuantizadas con saltos), Schrödinger 1926 (orbitales como nubes de probabilidad). Cada modelo con ilustración miniaturizada, fecha, autor y una frase de su aporte clave.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U01 — Temas Básicos de la Materia**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **linea-tiempo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (linea-tiempo):**
LÍNEA DE TIEMPO horizontal con eje cronológico central, hitos como cápsulas con fecha + título + micro-ilustración + frase corta.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Línea de tiempo horizontal con los cinco modelos atómicos: Dalton 1803 (esfera maciza), Thomson 1897 (budín de pasas con electrones incrustados), Rutherford 1911 (núcleo central con electrones orbitando), Bohr 1913 (electrones en órbitas cuantizadas con saltos), Schrödinger 1926 (orbitales como nubes de probabilidad). Cada modelo con ilustración miniaturizada, fecha, autor y una frase de su aporte clave.

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
2. Guárdala como `assets/visuales/manual-1/u01/M1-u01-04.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u01-04` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
