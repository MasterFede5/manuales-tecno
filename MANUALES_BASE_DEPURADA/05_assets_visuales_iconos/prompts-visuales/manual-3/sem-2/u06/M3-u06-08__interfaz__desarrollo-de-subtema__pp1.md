---
id: M3-u06-08
manual: 3
unidad: u06
semestre: 2
tipo: interfaz
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u06/10-tema-6-6.md
fuente_md_linea: 80
imagen_destino: assets/visuales/manual-3/u06/M3-u06-08.jpg
pagina_pdf_estimada: 41
pdf_destino: dist/manual-3-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M3-u06-08`

**Tipo visual:** `interfaz` · **Ocupa:** 1 pp · **Página PDF estimada:** 41

**Manual 3 · U06 — IA automatiza tu semana · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u06-08` |
| Archivo destino imagen | `assets/visuales/manual-3/u06/M3-u06-08.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-2.pdf` |
| Página PDF estimada | **p. 41** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u06/10-tema-6-6.md:80` |
| Tipo de placeholder | `interfaz` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Captura de Otter durante reunión Zoom activa: panel lateral derecho. Arriba: 'Live Transcription' con líneas de texto identificando speakers (María: ..., Carlos: ...). En medio: 'Action items' destacados en amarillo (Carlos enviará reporte el viernes; María agendará follow-up). Abajo: 'Summary' auto-generado de bullets clave. Botón 'Search transcript' permite buscar texto. Compartir con equipo opcional.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U06 — IA automatiza tu semana**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **interfaz**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (interfaz):**
MOCKUP DE INTERFAZ: marco de navegador o ventana de app con barra superior, sidebar opcional, área principal con contenido relevante, UI minimalista.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Captura de Otter durante reunión Zoom activa: panel lateral derecho. Arriba: 'Live Transcription' con líneas de texto identificando speakers (María: ..., Carlos: ...). En medio: 'Action items' destacados en amarillo (Carlos enviará reporte el viernes; María agendará follow-up). Abajo: 'Summary' auto-generado de bullets clave. Botón 'Search transcript' permite buscar texto. Compartir con equipo opcional.

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
2. Guárdala como `assets/visuales/manual-3/u06/M3-u06-08.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u06-08` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
