---
id: M3-sem1-07
manual: 3
unidad: sem1
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 1
fuente_md: manuales/manual-3/semestre-1/05-competencias.md
fuente_md_linea: 39
imagen_destino: assets/visuales/manual-3/sem1/M3-sem1-07.jpg
pagina_pdf_estimada: 12
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: contenido del manual
status: pendiente
---

# `M3-sem1-07`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 1 pp · **Página PDF estimada:** 12

**Manual 3 · SEM1 — Front/Back matter — Semestre 1 · Semestre 1**

> Rol del archivo: _contenido del manual_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-sem1-07` |
| Archivo destino imagen | `assets/visuales/manual-3/sem1/M3-sem1-07.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 12** |
| Archivo Markdown fuente | `manuales/manual-3/semestre-1/05-competencias.md:39` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Tabla extendida del índice de competencias del semestre con columnas: ID, descripción corta, verbo Bloom, % del manual dedicado, página del primer reactivo, página de la evidencia integradora. Encabezado azul Albatros, zebra sutil, ícono Bloom en la columna del verbo.  
> _Nota:_ cuadro maestro para revisión de la coordinación académica

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **SEM1 — Front/Back matter — Semestre 1**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **contenido del manual**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Tabla extendida del índice de competencias del semestre con columnas: ID, descripción corta, verbo Bloom, % del manual dedicado, página del primer reactivo, página de la evidencia integradora. Encabezado azul Albatros, zebra sutil, ícono Bloom en la columna del verbo.  
- **Nota editorial:** cuadro maestro para revisión de la coordinación académica

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
2. Guárdala como `assets/visuales/manual-3/sem1/M3-sem1-07.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-sem1-07` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
