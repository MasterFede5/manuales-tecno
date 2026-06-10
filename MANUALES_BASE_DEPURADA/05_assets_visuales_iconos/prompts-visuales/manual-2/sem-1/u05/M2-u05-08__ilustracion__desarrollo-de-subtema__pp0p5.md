---
id: M2-u05-08
manual: 2
unidad: u05
semestre: 1
tipo: ilustracion
paginas_ocupa: 0.5
fuente_md: manuales/manual-2/unidades/u05/10-tema-5-6.md
fuente_md_linea: 72
imagen_destino: assets/visuales/manual-2/u05/M2-u05-08.jpg
pagina_pdf_estimada: 281
pdf_destino: dist/manual-2-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M2-u05-08`

**Tipo visual:** `ilustracion` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 281

**Manual 2 · U05 — Ondas y Sonido · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u05-08` |
| Archivo destino imagen | `assets/visuales/manual-2/u05/M2-u05-08.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-1.pdf` |
| Página PDF estimada | **p. 281** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u05/10-tema-5-6.md:72` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Tres viñetas: 1) ONDAS ESTACIONARIAS — cuerda de guitarra con tres modos: fundamental (1 antinodo central), 2do armónico (1 nodo central, 2 antinodos), 3er armónico (2 nodos, 3 antinodos). 2) DOPPLER — coche moviéndose hacia la derecha emitiendo ondas; las ondas hacia adelante están comprimidas (mayor f), las de atrás dilatadas (menor f); observador adelante oye agudo, atrás grave. 3) Sirena de ambulancia con flecha del cambio de frecuencia al pasar.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U05 — Ondas y Sonido**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **ilustracion**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Tres viñetas: 1) ONDAS ESTACIONARIAS — cuerda de guitarra con tres modos: fundamental (1 antinodo central), 2do armónico (1 nodo central, 2 antinodos), 3er armónico (2 nodos, 3 antinodos). 2) DOPPLER — coche moviéndose hacia la derecha emitiendo ondas; las ondas hacia adelante están comprimidas (mayor f), las de atrás dilatadas (menor f); observador adelante oye agudo, atrás grave. 3) Sirena de ambulancia con flecha del cambio de frecuencia al pasar.

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
2. Guárdala como `assets/visuales/manual-2/u05/M2-u05-08.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u05-08` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
