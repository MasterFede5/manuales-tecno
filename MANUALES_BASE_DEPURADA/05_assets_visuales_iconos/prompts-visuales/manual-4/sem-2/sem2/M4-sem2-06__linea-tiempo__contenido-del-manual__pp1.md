---
id: M4-sem2-06
manual: 4
unidad: sem2
semestre: 2
tipo: linea-tiempo
paginas_ocupa: 1
fuente_md: manuales/manual-4/semestre-2/04-hilo-conductor.md
fuente_md_linea: 31
imagen_destino: assets/visuales/manual-4/sem2/M4-sem2-06.jpg
pagina_pdf_estimada: 14
pdf_destino: dist/manual-4-sem-2.pdf
rol_archivo: contenido del manual
status: pendiente
---

# `M4-sem2-06`

**Tipo visual:** `linea-tiempo` · **Ocupa:** 1 pp · **Página PDF estimada:** 14

**Manual 4 · SEM2 — Front/Back matter — Semestre 2 · Semestre 2**

> Rol del archivo: _contenido del manual_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M4-sem2-06` |
| Archivo destino imagen | `assets/visuales/manual-4/sem2/M4-sem2-06.jpg` |
| PDF en el que aparece | `dist/manual-4-sem-2.pdf` |
| Página PDF estimada | **p. 14** |
| Archivo Markdown fuente | `manuales/manual-4/semestre-2/04-hilo-conductor.md:31` |
| Tipo de placeholder | `linea-tiempo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Línea de tiempo horizontal del semestre 2: en el extremo izquierdo, el problema inicial del case study 'Asistente Institucional Albatros'; en el centro, 5 hitos correspondientes a los episodios de cada unidad (u06, u07, u08, u09, u10); en el extremo derecho, el entregable final del portafolio del semestre. Cada hito con fecha tentativa (semana N), título corto y micro-ilustración temática.  
> _Nota:_ visión panorámica del hilo conductor del semestre

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Avanzada** — Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza
- Unidad: **SEM2 — Front/Back matter — Semestre 2**
- Case study: *Asistente Institucional Albatros — IA con herramientas reales*
- Rol del archivo: **contenido del manual**
- Tipo de visual: **linea-tiempo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (linea-tiempo):**
LÍNEA DE TIEMPO horizontal con eje cronológico central, hitos como cápsulas con fecha + título + micro-ilustración + frase corta.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Línea de tiempo horizontal del semestre 2: en el extremo izquierdo, el problema inicial del case study 'Asistente Institucional Albatros'; en el centro, 5 hitos correspondientes a los episodios de cada unidad (u06, u07, u08, u09, u10); en el extremo derecho, el entregable final del portafolio del semestre. Cada hito con fecha tentativa (semana N), título corto y micro-ilustración temática.  
- **Nota editorial:** visión panorámica del hilo conductor del semestre

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
2. Guárdala como `assets/visuales/manual-4/sem2/M4-sem2-06.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 4
   python print_to_pdf.py --manual 4 --all-semesters
   ```

4. Verifica que `M4-sem2-06` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
