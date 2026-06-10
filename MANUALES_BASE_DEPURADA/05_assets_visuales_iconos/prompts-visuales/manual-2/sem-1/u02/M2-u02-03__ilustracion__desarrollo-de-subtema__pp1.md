---
id: M2-u02-03
manual: 2
unidad: u02
semestre: 1
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-2/unidades/u02/10-tema-2-1.md
fuente_md_linea: 92
imagen_destino: assets/visuales/manual-2/u02/M2-u02-03.jpg
pagina_pdf_estimada: 76
pdf_destino: dist/manual-2-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M2-u02-03`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 76

**Manual 2 · U02 — Dinámica (Fuerzas) · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u02-03` |
| Archivo destino imagen | `assets/visuales/manual-2/u02/M2-u02-03.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-1.pdf` |
| Página PDF estimada | **p. 76** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u02/10-tema-2-1.md:92` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Diagrama de cuerpo libre del coche F1 dibujado de perfil: silueta del coche en el centro con cinco vectores etiquetados saliendo de su centro de masa: F_cc empuje del CO2 (flecha grande horizontal hacia adelante), W peso (flecha vertical hacia abajo), N normal (flecha vertical hacia arriba, igual magnitud que W), F_r fricción (flecha pequeña hacia atrás), F_a resistencia aire (flecha pequeña también hacia atrás). Anexo lateral con descomposición de un vector arbitrario en F_x y F_y.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U02 — Dinámica (Fuerzas)**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Diagrama de cuerpo libre del coche F1 dibujado de perfil: silueta del coche en el centro con cinco vectores etiquetados saliendo de su centro de masa: F_cc empuje del CO2 (flecha grande horizontal hacia adelante), W peso (flecha vertical hacia abajo), N normal (flecha vertical hacia arriba, igual magnitud que W), F_r fricción (flecha pequeña hacia atrás), F_a resistencia aire (flecha pequeña también hacia atrás). Anexo lateral con descomposición de un vector arbitrario en F_x y F_y.

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
2. Guárdala como `assets/visuales/manual-2/u02/M2-u02-03.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u02-03` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
