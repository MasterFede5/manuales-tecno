---
id: M4-u07-04
manual: 4
unidad: u07
semestre: 2
tipo: interfaz
paginas_ocupa: 1
fuente_md: manuales/manual-4/unidades/u07/10-tema-7-2.md
fuente_md_linea: 118
imagen_destino: assets/visuales/manual-4/u07/M4-u07-04.jpg
pagina_pdf_estimada: 112
pdf_destino: dist/manual-4-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M4-u07-04`

**Tipo visual:** `interfaz` · **Ocupa:** 1 pp · **Página PDF estimada:** 112

**Manual 4 · U07 — Versión local soberana · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M4-u07-04` |
| Archivo destino imagen | `assets/visuales/manual-4/u07/M4-u07-04.jpg` |
| PDF en el que aparece | `dist/manual-4-sem-2.pdf` |
| Página PDF estimada | **p. 112** |
| Archivo Markdown fuente | `manuales/manual-4/unidades/u07/10-tema-7-2.md:118` |
| Tipo de placeholder | `interfaz` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Captura de terminal a tamaño página con 4 paneles: panel 1 muestra `curl install` con output. Panel 2 muestra `ollama pull llama3.1` con barra de progreso. Panel 3 muestra `ollama run llama3.1` con conversación interactiva (pregunta del usuario y respuesta del modelo en español). Panel 4 muestra `ollama list` con tabla de modelos. Anotaciones laterales: 'instala', 'descarga', 'corre', 'gestiona'. Estilo screenshot real terminal Albatros.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Avanzada** — Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza
- Unidad: **U07 — Versión local soberana**
- Case study: *Asistente Institucional Albatros — IA con herramientas reales*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **interfaz**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (interfaz):**
MOCKUP DE INTERFAZ: marco de navegador o ventana de app con barra superior, sidebar opcional, área principal con contenido relevante, UI minimalista.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Captura de terminal a tamaño página con 4 paneles: panel 1 muestra `curl install` con output. Panel 2 muestra `ollama pull llama3.1` con barra de progreso. Panel 3 muestra `ollama run llama3.1` con conversación interactiva (pregunta del usuario y respuesta del modelo en español). Panel 4 muestra `ollama list` con tabla de modelos. Anotaciones laterales: 'instala', 'descarga', 'corre', 'gestiona'. Estilo screenshot real terminal Albatros.

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
2. Guárdala como `assets/visuales/manual-4/u07/M4-u07-04.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 4
   python print_to_pdf.py --manual 4 --all-semesters
   ```

4. Verifica que `M4-u07-04` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
