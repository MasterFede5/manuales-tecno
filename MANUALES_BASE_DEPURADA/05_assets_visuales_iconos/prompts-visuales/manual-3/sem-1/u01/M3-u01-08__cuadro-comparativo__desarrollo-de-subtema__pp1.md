---
id: M3-u01-08
manual: 3
unidad: u01
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u01/10-tema-1-6.md
fuente_md_linea: 75
imagen_destino: assets/visuales/manual-3/u01/M3-u01-08.jpg
pagina_pdf_estimada: 35
pdf_destino: dist/manual-3-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M3-u01-08`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 1 pp · **Página PDF estimada:** 35

**Manual 3 · U01 — Fundamentos e Historia de la IA · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u01-08` |
| Archivo destino imagen | `assets/visuales/manual-3/u01/M3-u01-08.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-1.pdf` |
| Página PDF estimada | **p. 35** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u01/10-tema-1-6.md:75` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Cuadro comparativo de 8 LLMs principales 2025 en formato tabla con columnas: 1) MODELO. 2) EMPRESA. 3) PARÁMETROS estimados. 4) CONTEXTO en tokens (1M, 2M, 200K, etc.). 5) MULTIMODAL sí/no. 6) PRICING por millón de tokens entrada/salida USD. 7) CASO DE USO IDEAL. Filas: GPT-4o (OpenAI, ~1.7T, 128K, sí, $5/$15, multimodal general), GPT-5 (OpenAI, oculto, 256K, sí, $10/$30, frontier), Claude Opus 4.7 (Anthropic, oculto, 1M, sí, $15/$75, redacción larga), Claude Sonnet 4.6 (Anthropic, oculto, 200K, sí, $3/$15, balanceado), Gemini 2.0 Pro (Google, oculto, 2M, sí, $7/$21, integración Google), Llama 4 (Meta, 405B, 128K, no, GRATIS abierto, autohospedaje), Mistral Large 2 (Mistral, ~123B, 128K, no, $3/$9, multilingüe europeo), DeepSeek V3 (DeepSeek, ~671B MoE, 128K, no, $0.27/$1.1, costo bajo). Última columna con casos de uso de una línea.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U01 — Fundamentos e Historia de la IA**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro comparativo de 8 LLMs principales 2025 en formato tabla con columnas: 1) MODELO. 2) EMPRESA. 3) PARÁMETROS estimados. 4) CONTEXTO en tokens (1M, 2M, 200K, etc.). 5) MULTIMODAL sí/no. 6) PRICING por millón de tokens entrada/salida USD. 7) CASO DE USO IDEAL. Filas: GPT-4o (OpenAI, ~1.7T, 128K, sí, $5/$15, multimodal general), GPT-5 (OpenAI, oculto, 256K, sí, $10/$30, frontier), Claude Opus 4.7 (Anthropic, oculto, 1M, sí, $15/$75, redacción larga), Claude Sonnet 4.6 (Anthropic, oculto, 200K, sí, $3/$15, balanceado), Gemini 2.0 Pro (Google, oculto, 2M, sí, $7/$21, integración Google), Llama 4 (Meta, 405B, 128K, no, GRATIS abierto, autohospedaje), Mistral Large 2 (Mistral, ~123B, 128K, no, $3/$9, multilingüe europeo), DeepSeek V3 (DeepSeek, ~671B MoE, 128K, no, $0.27/$1.1, costo bajo). Última columna con casos de uso de una línea.

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
2. Guárdala como `assets/visuales/manual-3/u01/M3-u01-08.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u01-08` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
