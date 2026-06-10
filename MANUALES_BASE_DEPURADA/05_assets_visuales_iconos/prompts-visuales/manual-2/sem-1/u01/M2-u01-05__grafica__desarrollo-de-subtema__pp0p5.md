---
id: M2-u01-05
manual: 2
unidad: u01
semestre: 1
tipo: grafica
paginas_ocupa: 0.5
fuente_md: manuales/manual-2/unidades/u01/10-tema-1-3.md
fuente_md_linea: 67
imagen_destino: assets/visuales/manual-2/u01/M2-u01-05.jpg
pagina_pdf_estimada: 23
pdf_destino: dist/manual-2-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
---

# `M2-u01-05`

**Tipo visual:** `grafica` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 23

**Manual 2 · U01 — Cinemática (Telemetría) · Semestre 1**

> Rol del archivo: _desarrollo de subtema_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u01-05` |
| Archivo destino imagen | `assets/visuales/manual-2/u01/M2-u01-05.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-1.pdf` |
| Página PDF estimada | **p. 23** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u01/10-tema-1-3.md:67` |
| Tipo de placeholder | `grafica` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Tres gráficas paralelas verticales en MRU: 1) x vs t recta ascendente con etiqueta 'pendiente = v', 2) v vs t línea horizontal a v=18 m/s con sombreado bajo curva etiquetado 'área = desplazamiento', 3) a vs t línea horizontal en cero. Eje horizontal común de tiempo de 0 a 1 s. Conexión visual entre las tres con líneas verticales en t=0.5s.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U01 — Cinemática (Telemetría)**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **desarrollo de subtema**
- Tipo de visual: **grafica**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (grafica):**
GRÁFICA CIENTÍFICA limpia: ejes etiquetados con magnitud+unidad, cuadrícula tenue, una o dos series, leyenda compacta arriba derecha.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Tres gráficas paralelas verticales en MRU: 1) x vs t recta ascendente con etiqueta 'pendiente = v', 2) v vs t línea horizontal a v=18 m/s con sombreado bajo curva etiquetado 'área = desplazamiento', 3) a vs t línea horizontal en cero. Eje horizontal común de tiempo de 0 a 1 s. Conexión visual entre las tres con líneas verticales en t=0.5s.

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
2. Guárdala como `assets/visuales/manual-2/u01/M2-u01-05.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u01-05` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
