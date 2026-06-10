---
id: M3-u03-05
manual: 3
unidad: u03
semestre: 1
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u03/10-tema-3-2.md
fuente_md_linea: 92
imagen_destino: assets/visuales/manual-3/u03/M3-u03-05.jpg
pagina_pdf_estimada: 139
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M3-u03-05`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 139

**Manual 3 · U03 — Prompts que sí funcionan · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u03-05` |
| Archivo destino imagen | `assets/visuales/manual-3/u03/M3-u03-05.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 139** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u03/10-tema-3-2.md:92` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Tres técnicas en columnas paralelas comparando aplicación a la misma pregunta de matemáticas: 1) ZERO-SHOT — pregunta directa, respuesta inmediata (a veces incorrecta en problemas complejos). 2) FEW-SHOT — usuario da 2 ejemplos resueltos primero, luego pregunta nueva; modelo imita el patrón paso a paso. 3) CHAIN-OF-THOUGHT — usuario añade 'piensa paso a paso'; modelo escribe razonamiento explícito antes de la respuesta final. Resultados: zero-shot 60% precisión, few-shot 75%, CoT 85% en problemas matemáticos.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U03 — Prompts que sí funcionan**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Tres técnicas en columnas paralelas comparando aplicación a la misma pregunta de matemáticas: 1) ZERO-SHOT — pregunta directa, respuesta inmediata (a veces incorrecta en problemas complejos). 2) FEW-SHOT — usuario da 2 ejemplos resueltos primero, luego pregunta nueva; modelo imita el patrón paso a paso. 3) CHAIN-OF-THOUGHT — usuario añade 'piensa paso a paso'; modelo escribe razonamiento explícito antes de la respuesta final. Resultados: zero-shot 60% precisión, few-shot 75%, CoT 85% en problemas matemáticos.

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
2. Guárdala como `assets/visuales/manual-3/u03/M3-u03-05.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u03-05` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
