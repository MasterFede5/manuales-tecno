---
id: M4-u01-10
manual: 4
unidad: u01
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 1
fuente_md: manuales/manual-4/unidades/u01/10-tema-1-8.md
fuente_md_linea: 85
imagen_destino: assets/visuales/manual-4/u01/M4-u01-10.jpg
pagina_pdf_estimada: 62
pdf_destino: dist/manual-4-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M4-u01-10`

**Tipo visual:** `cuadro-comparativo` · **Ocupa:** 1 pp · **Página PDF estimada:** 62

**Manual 4 · U01 — Prompts versionados · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M4-u01-10` |
| Archivo destino imagen | `assets/visuales/manual-4/u01/M4-u01-10.jpg` |
| PDF en el que aparece | `dist/manual-4-sem-1.pdf` |
| Página PDF estimada | **p. 62** |
| Archivo Markdown fuente | `manuales/manual-4/unidades/u01/10-tema-1-8.md:85` |
| Tipo de placeholder | `cuadro-comparativo` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Cuadro 'Pirámide de evaluación de prompts' tamaño página completa con 4 niveles apilados ascendentemente. Nivel 1 (base, ancho): Smoke test con 3-5 ejemplos manuales, frecuencia 'cada cambio', costo cero, señal 'no se rompió'. Nivel 2: Golden set con 20-50 ejemplos versionados, frecuencia 'pre-merge', costo bajo, señal 'mejora sobre baseline'. Nivel 3: A/B canary al 5%, frecuencia 'pre-rollout', costo medio, señal 'mejor en producción real'. Nivel 4 (cima, angosto): Evaluación humana con rúbrica, frecuencia 'cada release', costo alto, señal 'calidad subjetiva'. Cada nivel con icono distintivo. Estilo profesional Albatros.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Avanzada** — Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza
- Unidad: **U01 — Prompts versionados**
- Case study: *Asistente Institucional Albatros — IA con herramientas reales*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **cuadro-comparativo**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (cuadro-comparativo):**
CUADRO COMPARATIVO tipo tabla de 2-4 columnas con encabezado en azul Albatros; bordes finos; iconos en cabecera; alternancia zebra sutil.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Cuadro 'Pirámide de evaluación de prompts' tamaño página completa con 4 niveles apilados ascendentemente. Nivel 1 (base, ancho): Smoke test con 3-5 ejemplos manuales, frecuencia 'cada cambio', costo cero, señal 'no se rompió'. Nivel 2: Golden set con 20-50 ejemplos versionados, frecuencia 'pre-merge', costo bajo, señal 'mejora sobre baseline'. Nivel 3: A/B canary al 5%, frecuencia 'pre-rollout', costo medio, señal 'mejor en producción real'. Nivel 4 (cima, angosto): Evaluación humana con rúbrica, frecuencia 'cada release', costo alto, señal 'calidad subjetiva'. Cada nivel con icono distintivo. Estilo profesional Albatros.

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
2. Guárdala como `assets/visuales/manual-4/u01/M4-u01-10.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 4
   python print_to_pdf.py --manual 4 --all-semesters
   ```

4. Verifica que `M4-u01-10` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
