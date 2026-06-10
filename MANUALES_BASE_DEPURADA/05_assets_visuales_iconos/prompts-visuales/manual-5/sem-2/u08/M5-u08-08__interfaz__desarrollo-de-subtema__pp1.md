---
id: M5-u08-08
manual: 5
unidad: u08
semestre: 2
tipo: interfaz
paginas_ocupa: 1
fuente_md: manuales/manual-5/unidades/u08/10-tema-8-6.md
fuente_md_linea: 102
imagen_destino: assets/visuales/manual-5/u08/M5-u08-08.jpg
pagina_pdf_estimada: 247
pdf_destino: dist/manual-5-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M5-u08-08`

**Tipo visual:** `interfaz` · **Ocupa:** 1 pp · **Página PDF estimada:** 247

**Manual 5 · U08 — Publicación y despliegue · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M5-u08-08` |
| Archivo destino imagen | `assets/visuales/manual-5/u08/M5-u08-08.jpg` |
| PDF en el que aparece | `dist/manual-5-sem-2.pdf` |
| Página PDF estimada | **p. 247** |
| Archivo Markdown fuente | `manuales/manual-5/unidades/u08/10-tema-8-6.md:102` |
| Tipo de placeholder | `interfaz` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Captura app Streamlit a tamaño página: header 'Predictor Albatros', 3 sliders horizontales (horas, asistencia, cal_ant), botón naranja 'Predecir y explicar', resultado con métrica grande (pred=6.5) y caja de texto con explicación IA. Paleta azul Albatros institucional.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial con Programación** — De Python al primer modelo de Machine Learning y APIs de IA
- Unidad: **U08 — Publicación y despliegue**
- Case study: *Predictor de rendimiento escolar — pipeline ML completo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **interfaz**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (interfaz):**
MOCKUP DE INTERFAZ: marco de navegador o ventana de app con barra superior, sidebar opcional, área principal con contenido relevante, UI minimalista.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Captura app Streamlit a tamaño página: header 'Predictor Albatros', 3 sliders horizontales (horas, asistencia, cal_ant), botón naranja 'Predecir y explicar', resultado con métrica grande (pred=6.5) y caja de texto con explicación IA. Paleta azul Albatros institucional.

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
2. Guárdala como `assets/visuales/manual-5/u08/M5-u08-08.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 5
   python print_to_pdf.py --manual 5 --all-semesters
   ```

4. Verifica que `M5-u08-08` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
