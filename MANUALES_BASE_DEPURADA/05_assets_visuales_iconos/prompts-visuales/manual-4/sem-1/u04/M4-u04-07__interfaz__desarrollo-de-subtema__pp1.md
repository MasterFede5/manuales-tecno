---
id: M4-u04-07
manual: 4
unidad: u04
semestre: 1
tipo: interfaz
paginas_ocupa: 1
fuente_md: manuales/manual-4/unidades/u04/10-tema-4-4.md
fuente_md_linea: 133
imagen_destino: assets/visuales/manual-4/u04/M4-u04-07.jpg
pagina_pdf_estimada: 262
pdf_destino: dist/manual-4-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M4-u04-07`

**Tipo visual:** `interfaz` · **Ocupa:** 1 pp · **Página PDF estimada:** 262

**Manual 4 · U04 — RAG sobre reglamento · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M4-u04-07` |
| Archivo destino imagen | `assets/visuales/manual-4/u04/M4-u04-07.jpg` |
| PDF en el que aparece | `dist/manual-4-sem-1.pdf` |
| Página PDF estimada | **p. 262** |
| Archivo Markdown fuente | `manuales/manual-4/unidades/u04/10-tema-4-4.md:133` |
| Tipo de placeholder | `interfaz` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Captura a tamaño página de Dify mostrando un workflow visual con 7 nodos conectados (Input → Document Loader → Splitter → Embedder → Vector Store → Retriever → LLM → Output), cada nodo con icono y etiqueta. Panel lateral derecho mostrando configuración del nodo seleccionado (Embedder con dropdown de modelo, dimensiones, batch size). Toolbar superior con botones Test, Deploy, Version. Anotaciones laterales numeradas explicando cada zona de la UI. Mensaje 'el flujo se construye visual'. Estilo screenshot real Albatros.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Avanzada** — Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza
- Unidad: **U04 — RAG sobre reglamento**
- Case study: *Asistente Institucional Albatros — IA con herramientas reales*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **interfaz**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (interfaz):**
MOCKUP DE INTERFAZ: marco de navegador o ventana de app con barra superior, sidebar opcional, área principal con contenido relevante, UI minimalista.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Captura a tamaño página de Dify mostrando un workflow visual con 7 nodos conectados (Input → Document Loader → Splitter → Embedder → Vector Store → Retriever → LLM → Output), cada nodo con icono y etiqueta. Panel lateral derecho mostrando configuración del nodo seleccionado (Embedder con dropdown de modelo, dimensiones, batch size). Toolbar superior con botones Test, Deploy, Version. Anotaciones laterales numeradas explicando cada zona de la UI. Mensaje 'el flujo se construye visual'. Estilo screenshot real Albatros.

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
2. Guárdala como `assets/visuales/manual-4/u04/M4-u04-07.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 4
   python print_to_pdf.py --manual 4 --all-semesters
   ```

4. Verifica que `M4-u04-07` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
