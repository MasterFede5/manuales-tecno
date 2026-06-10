---
id: M4-sem2-05
manual: 4
unidad: sem2
semestre: 2
tipo: infografia
paginas_ocupa: 1
fuente_md: manuales/manual-4/semestre-2/03-mapa-contenidos.md
fuente_md_linea: 18
imagen_destino: assets/visuales/manual-4/sem2/M4-sem2-05.jpg
pagina_pdf_estimada: 10
pdf_destino: dist/manual-4-sem-2.pdf
rol_archivo: contenido del manual
status: pendiente
---

# `M4-sem2-05`

**Tipo visual:** `infografia` · **Ocupa:** 1 pp · **Página PDF estimada:** 10

**Manual 4 · SEM2 — Front/Back matter — Semestre 2 · Semestre 2**

> Rol del archivo: _contenido del manual_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M4-sem2-05` |
| Archivo destino imagen | `assets/visuales/manual-4/sem2/M4-sem2-05.jpg` |
| PDF en el que aparece | `dist/manual-4-sem-2.pdf` |
| Página PDF estimada | **p. 10** |
| Archivo Markdown fuente | `manuales/manual-4/semestre-2/03-mapa-contenidos.md:18` |
| Tipo de placeholder | `infografia` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Infografía vertical tipo mapa visual del semestre 2 del manual Inteligencia Artificial Avanzada: en la parte superior, el título del case study 'Asistente Institucional Albatros'. Debajo, una columna de 5 estaciones conectadas verticalmente, una por unidad (u06, u07, u08, u09, u10), cada estación con su número, título, ícono temático y la herramienta que aporta al caso. Al pie, un entregable de portafolio final del semestre. Paleta azul Albatros + naranja en conectores.  
> _Nota:_ mapa visual del semestre — pieza central del front matter

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Avanzada** — Usuario de Poder · Especificaciones, Artifacts, Agentes y Gobernanza
- Unidad: **SEM2 — Front/Back matter — Semestre 2**
- Case study: *Asistente Institucional Albatros — IA con herramientas reales*
- Rol del archivo: **contenido del manual**
- Tipo de visual: **infografia**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (infografia):**
INFOGRAFÍA vertical organizada en 3-5 secciones jerárquicas con títulos y micro-iconos; numeración visible; íconos outline+duotone consistentes.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Infografía vertical tipo mapa visual del semestre 2 del manual Inteligencia Artificial Avanzada: en la parte superior, el título del case study 'Asistente Institucional Albatros'. Debajo, una columna de 5 estaciones conectadas verticalmente, una por unidad (u06, u07, u08, u09, u10), cada estación con su número, título, ícono temático y la herramienta que aporta al caso. Al pie, un entregable de portafolio final del semestre. Paleta azul Albatros + naranja en conectores.  
- **Nota editorial:** mapa visual del semestre — pieza central del front matter

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
2. Guárdala como `assets/visuales/manual-4/sem2/M4-sem2-05.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 4
   python print_to_pdf.py --manual 4 --all-semesters
   ```

4. Verifica que `M4-sem2-05` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
