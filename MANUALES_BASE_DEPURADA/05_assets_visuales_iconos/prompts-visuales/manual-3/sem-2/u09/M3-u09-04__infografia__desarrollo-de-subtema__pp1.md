---
id: M3-u09-04
manual: 3
unidad: u09
semestre: 2
tipo: infografia
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u09/10-tema-9-2.md
fuente_md_linea: 40
imagen_destino: assets/visuales/manual-3/u09/M3-u09-04.jpg
pagina_pdf_estimada: 196
pdf_destino: dist/manual-3-sem-2.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M3-u09-04`

**Tipo visual:** `infografia` · **Ocupa:** 1 pp · **Página PDF estimada:** 196

**Manual 3 · U09 — Ética y publicación responsable · Semestre 2**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u09-04` |
| Archivo destino imagen | `assets/visuales/manual-3/u09/M3-u09-04.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-2.pdf` |
| Página PDF estimada | **p. 196** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u09/10-tema-9-2.md:40` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Infografía horizontal 'El viaje de tu prompt' con 5 estaciones en línea: tu dispositivo (icono teclado) → red TLS (icono candado) → servidor del proveedor (icono nube) → revisión humana opcional (icono ojo) → entrenamiento futuro (icono engrane). Bajo cada estación, un cuadro pequeño con la 'palanca' que tienes para protegerte (ej: borrar local, VPN, política de retención, opt-out de revisión humana, opt-out de entrenamiento). Colores Albatros con flujo de izquierda a derecha.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U09 — Ética y publicación responsable**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **infografia**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Infografía horizontal 'El viaje de tu prompt' con 5 estaciones en línea: tu dispositivo (icono teclado) → red TLS (icono candado) → servidor del proveedor (icono nube) → revisión humana opcional (icono ojo) → entrenamiento futuro (icono engrane). Bajo cada estación, un cuadro pequeño con la 'palanca' que tienes para protegerte (ej: borrar local, VPN, política de retención, opt-out de revisión humana, opt-out de entrenamiento). Colores Albatros con flujo de izquierda a derecha.

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
2. Guárdala como `assets/visuales/manual-3/u09/M3-u09-04.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u09-04` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
