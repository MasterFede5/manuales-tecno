---
id: M4-u01-08
manual: 4
unidad: u01
semestre: 1
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-4/unidades/u01/10-tema-1-6.md
fuente_md_linea: 79
imagen_destino: assets/visuales/manual-4/u01/M4-u01-08.jpg
pagina_pdf_estimada: 54
pdf_destino: dist/manual-4-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M4-u01-08`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 54

**Manual 4 · U01 — Prompts versionados · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M4-u01-08` |
| Archivo destino imagen | `assets/visuales/manual-4/u01/M4-u01-08.jpg` |
| PDF en el que aparece | `dist/manual-4-sem-1.pdf` |
| Página PDF estimada | **p. 54** |
| Archivo Markdown fuente | `manuales/manual-4/unidades/u01/10-tema-1-6.md:79` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Ilustración 'curaduría de ejemplos few-shot' tamaño media página: cuadrícula de 12 ejemplos candidatos representados como tarjetas, cada una etiquetada con su tipo (típico, raro, ambiguo, borde, ruido). Una mano selecciona 3 marcadas con check verde (1 típico claro, 1 ambiguo de tono, 1 caso de borde). Las 9 restantes quedan en gris semitranspariente. Subtítulo: '3 ejemplos diversos > 30 ejemplos similares'. Estilo limpio Albatros.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Avanzada** — Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza
- Unidad: **U01 — Prompts versionados**
- Case study: *Asistente Institucional Albatros — IA con herramientas reales*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Ilustración 'curaduría de ejemplos few-shot' tamaño media página: cuadrícula de 12 ejemplos candidatos representados como tarjetas, cada una etiquetada con su tipo (típico, raro, ambiguo, borde, ruido). Una mano selecciona 3 marcadas con check verde (1 típico claro, 1 ambiguo de tono, 1 caso de borde). Las 9 restantes quedan en gris semitranspariente. Subtítulo: '3 ejemplos diversos > 30 ejemplos similares'. Estilo limpio Albatros.

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
2. Guárdala como `assets/visuales/manual-4/u01/M4-u01-08.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 4
   python print_to_pdf.py --manual 4 --all-semesters
   ```

4. Verifica que `M4-u01-08` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
