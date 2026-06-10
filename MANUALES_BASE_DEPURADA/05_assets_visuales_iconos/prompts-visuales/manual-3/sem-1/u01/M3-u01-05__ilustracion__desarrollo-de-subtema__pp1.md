---
id: M3-u01-05
manual: 3
unidad: u01
semestre: 1
tipo: ilustracion
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u01/10-tema-1-3.md
fuente_md_linea: 70
imagen_destino: assets/visuales/manual-3/u01/M3-u01-05.jpg
pagina_pdf_estimada: 26
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M3-u01-05`

**Tipo visual:** `ilustracion` · **Ocupa:** 1 pp · **Página PDF estimada:** 26

**Manual 3 · U01 — Fundamentos e Historia de la IA · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u01-05` |
| Archivo destino imagen | `assets/visuales/manual-3/u01/M3-u01-05.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 26** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u01/10-tema-1-3.md:70` |
| Tipo de placeholder | `ilustracion` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Tres círculos concéntricos crecientes representando los niveles de IA: 1) ANI (IA ESTRECHA) círculo interior sólido con ejemplos: ChatGPT, AlphaGo, Siri, Tesla autopilot, recomendador Netflix. Etiqueta 'EXISTE HOY 2025'. 2) AGI (IA GENERAL) círculo medio punteado con un humano genérico al centro y leyenda 'aprende cualquier tarea humana'. Etiqueta 'PROBABLE 2030-2050'. 3) ASI (SÚPER-IA) círculo exterior teórico con leyenda 'supera al humano en TODOS los dominios'. Etiqueta '¿LLEGARÁ?'. Cada nivel con una flecha hacia el siguiente con el desafío técnico que falta superar.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U01 — Fundamentos e Historia de la IA**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **ilustracion**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (ilustracion):**
ESCENA LIBRE editorial; composición balanceada; foco narrativo claro; un solo punto focal con elementos secundarios apoyando.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Tres círculos concéntricos crecientes representando los niveles de IA: 1) ANI (IA ESTRECHA) círculo interior sólido con ejemplos: ChatGPT, AlphaGo, Siri, Tesla autopilot, recomendador Netflix. Etiqueta 'EXISTE HOY 2025'. 2) AGI (IA GENERAL) círculo medio punteado con un humano genérico al centro y leyenda 'aprende cualquier tarea humana'. Etiqueta 'PROBABLE 2030-2050'. 3) ASI (SÚPER-IA) círculo exterior teórico con leyenda 'supera al humano en TODOS los dominios'. Etiqueta '¿LLEGARÁ?'. Cada nivel con una flecha hacia el siguiente con el desafío técnico que falta superar.

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
2. Guárdala como `assets/visuales/manual-3/u01/M3-u01-05.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u01-05` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
