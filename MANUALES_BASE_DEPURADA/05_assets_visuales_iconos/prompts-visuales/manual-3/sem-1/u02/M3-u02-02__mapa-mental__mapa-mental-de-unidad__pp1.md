---
id: M3-u02-02
manual: 3
unidad: u02
semestre: 1
tipo: mapa-mental
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u02/01-mapa-mental.md
fuente_md_linea: 9
imagen_destino: assets/visuales/manual-3/u02/M3-u02-02.jpg
pagina_pdf_estimada: 68
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: mapa mental de unidad
status: pendiente
---

# `M3-u02-02`

**Tipo visual:** `mapa-mental` · **Ocupa:** 1 pp · **Página PDF estimada:** 68

**Manual 3 · U02 — Tu primer chat útil · Semestre 1**

> Rol del archivo: _mapa mental de unidad_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u02-02` |
| Archivo destino imagen | `assets/visuales/manual-3/u02/M3-u02-02.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 68** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u02/01-mapa-mental.md:9` |
| Tipo de placeholder | `mapa-mental` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Mapa mental con nodo central ASISTENTE CONVERSACIONAL y siete ramas: 1) ANATOMÍA — tokens, contexto, ventana de contexto, memoria, system prompt. 2) ChatGPT — modelos GPT-4o/5/o3, voice mode, GPTs, Canvas, plugins. 3) CLAUDE — artifacts, projects, styles, computer use, Claude Code. 4) GEMINI — multimodal nativo, integración Workspace, NotebookLM, 2M contexto. 5) COPILOT — integración Office 365, Copilot Studio, Microsoft 365 Chat. 6) COMPARATIVA — fortalezas/debilidades por caso de uso, costo. 7) LIMITACIONES — alucinaciones, sesgo, fecha de corte, jailbreaks. En el centro inferior, ícono del tutor IA personal en construcción.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U02 — Tu primer chat útil**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **mapa mental de unidad**
- Tipo de visual: **mapa-mental**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (mapa-mental):**
MAPA MENTAL radial: nodo central grande, 4-7 ramas curvas a sub-nodos, cada rama en color sólido distinto dentro de paleta Albatros; hojas con micro-ilustración.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Mapa mental con nodo central ASISTENTE CONVERSACIONAL y siete ramas: 1) ANATOMÍA — tokens, contexto, ventana de contexto, memoria, system prompt. 2) ChatGPT — modelos GPT-4o/5/o3, voice mode, GPTs, Canvas, plugins. 3) CLAUDE — artifacts, projects, styles, computer use, Claude Code. 4) GEMINI — multimodal nativo, integración Workspace, NotebookLM, 2M contexto. 5) COPILOT — integración Office 365, Copilot Studio, Microsoft 365 Chat. 6) COMPARATIVA — fortalezas/debilidades por caso de uso, costo. 7) LIMITACIONES — alucinaciones, sesgo, fecha de corte, jailbreaks. En el centro inferior, ícono del tutor IA personal en construcción.

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
2. Guárdala como `assets/visuales/manual-3/u02/M3-u02-02.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u02-02` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
