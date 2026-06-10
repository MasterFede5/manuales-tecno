---
id: M1-u05-06
manual: 1
unidad: u05
semestre: 2
tipo: ilustracion
paginas_ocupa: 0.5
fuente_md: manuales/manual-1/unidades/u05/10-tema-5-4.md
fuente_md_linea: 105
imagen_destino: assets/visuales/manual-1/u05/M1-u05-06.jpg
pagina_pdf_estimada: 88
pdf_destino: dist/manual-1-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M1-u05-06`

**Tipo visual:** `ilustracion` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 88

**Manual 1 · U05 — Energía y Reacciones Químicas · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u05-06` |
| Archivo destino imagen | `assets/visuales/manual-1/u05/M1-u05-06.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-2.pdf` |
| Página PDF estimada | **p. 88** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u05/10-tema-5-4.md:105` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Dos diagramas de energía contrapuestos lado a lado: izquierda reacción exotérmica con perfil descendente desde reactivos arriba, pasando por barrera de E_a, hasta productos abajo, con flecha que muestra ΔH negativo y calor saliendo al entorno representado por flechas radiantes. Derecha reacción endotérmica con perfil ascendente, ΔH positivo, calor entrando del entorno. Cada una con ejemplo: combustión de gas vs disolución de bicarbonato.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U05 — Energía y Reacciones Químicas**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **ilustracion**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Dos diagramas de energía contrapuestos lado a lado: izquierda reacción exotérmica con perfil descendente desde reactivos arriba, pasando por barrera de E_a, hasta productos abajo, con flecha que muestra ΔH negativo y calor saliendo al entorno representado por flechas radiantes. Derecha reacción endotérmica con perfil ascendente, ΔH positivo, calor entrando del entorno. Cada una con ejemplo: combustión de gas vs disolución de bicarbonato.

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
2. Guárdala como `assets/visuales/manual-1/u05/M1-u05-06.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u05-06` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
