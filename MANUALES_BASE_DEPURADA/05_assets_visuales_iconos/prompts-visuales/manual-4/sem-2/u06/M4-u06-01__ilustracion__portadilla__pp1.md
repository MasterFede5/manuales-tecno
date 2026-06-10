---
id: M4-u06-01
manual: 4
unidad: u06
semestre: 2
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-4/unidades/u06/00-portadilla.md
fuente_md_linea: 13
imagen_destino: assets/visuales/manual-4/u06/M4-u06-01.jpg
pagina_pdf_estimada: 22
pdf_destino: dist/manual-4-sem-2.pdf
rol_archivo: portadilla
status: pendiente
---

# `M4-u06-01`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 22

**Manual 4 · U06 — Agentes con herramientas · Semestre 2**

> Rol del archivo: _portadilla_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M4-u06-01` |
| Archivo destino imagen | `assets/visuales/manual-4/u06/M4-u06-01.jpg` |
| PDF en el que aparece | `dist/manual-4-sem-2.pdf` |
| Página PDF estimada | **p. 22** |
| Archivo Markdown fuente | `manuales/manual-4/unidades/u06/00-portadilla.md:13` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Ilustración hero de portadilla para la Unidad 6: en el centro un círculo azul Albatros etiquetado 'Agente' con icono de cerebro. A su alrededor, en órbita, 6 herramientas (search, RAG, calendar, email, code, browse) que el agente decide invocar según el problema. Una flecha externa entra como 'objetivo' y otra sale como 'resultado'. Línea punteada en otra órbita: 'memoria' y 'observabilidad'. Mensaje: 'el agente no es un workflow más complejo; es un cambio de paradigma'. Paleta azul Albatros.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Avanzada** — Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza
- Unidad: **U06 — Agentes con herramientas**
- Case study: *Asistente Institucional Albatros — IA con herramientas reales*
- Rol del archivo: **portadilla**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Ilustración hero de portadilla para la Unidad 6: en el centro un círculo azul Albatros etiquetado 'Agente' con icono de cerebro. A su alrededor, en órbita, 6 herramientas (search, RAG, calendar, email, code, browse) que el agente decide invocar según el problema. Una flecha externa entra como 'objetivo' y otra sale como 'resultado'. Línea punteada en otra órbita: 'memoria' y 'observabilidad'. Mensaje: 'el agente no es un workflow más complejo; es un cambio de paradigma'. Paleta azul Albatros.

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
2. Guárdala como `assets/visuales/manual-4/u06/M4-u06-01.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 4
   python print_to_pdf.py --manual 4 --all-semesters
   ```

4. Verifica que `M4-u06-01` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
