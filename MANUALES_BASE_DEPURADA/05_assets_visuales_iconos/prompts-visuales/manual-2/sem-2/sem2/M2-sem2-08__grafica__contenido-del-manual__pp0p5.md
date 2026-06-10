---
id: M2-sem2-08
manual: 2
unidad: sem2
semestre: 2
tipo: grafica
paginas_ocupa: 0.5
fuente_md: manuales/manual-2/semestre-2/06-diagnostica.md
fuente_md_linea: 77
imagen_destino: assets/visuales/manual-2/sem2/M2-sem2-08.jpg
pagina_pdf_estimada: 10
pdf_destino: dist/manual-2-sem-2.pdf
rol_archivo: contenido del manual
status: pendiente
---

# `M2-sem2-08`

**Tipo visual:** `grafica` · **Ocupa:** 0.5 pp · **Página PDF estimada:** 10

**Manual 2 · SEM2 — Front/Back matter — Semestre 2 · Semestre 2**

> Rol del archivo: _contenido del manual_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-sem2-08` |
| Archivo destino imagen | `assets/visuales/manual-2/sem2/M2-sem2-08.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-2.pdf` |
| Página PDF estimada | **p. 10** |
| Archivo Markdown fuente | `manuales/manual-2/semestre-2/06-diagnostica.md:77` |
| Tipo de placeholder | `grafica` |
| Espacio reservado | 0.5 página(s) |

## Descripción original del manual

> Gráfica de radar de 5 ejes para autoevaluación inicial: 1) Familiaridad con el tema, 2) Confianza para practicar, 3) Acceso a recursos, 4) Motivación inicial, 5) Tiempo disponible. Cada eje numerado de 0 a 5. El estudiante marcará con un punto su nivel actual y al final del semestre se compara con una segunda lectura.  
> _Nota:_ gráfico para que el estudiante mida su evolución durante el semestre

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **SEM2 — Front/Back matter — Semestre 2**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **contenido del manual**
- Tipo de visual: **grafica**
- Ocupación: **0.5** página(s) → media página · 8.5x5.5 in · landscape · `--ar 3:2`

**COMPOSICIÓN REQUERIDA (grafica):**
GRÁFICA CIENTÍFICA limpia: ejes etiquetados con magnitud+unidad, cuadrícula tenue, una o dos series, leyenda compacta arriba derecha.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Gráfica de radar de 5 ejes para autoevaluación inicial: 1) Familiaridad con el tema, 2) Confianza para practicar, 3) Acceso a recursos, 4) Motivación inicial, 5) Tiempo disponible. Cada eje numerado de 0 a 5. El estudiante marcará con un punto su nivel actual y al final del semestre se compara con una segunda lectura.  
- **Nota editorial:** gráfico para que el estudiante mida su evolución durante el semestre

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
2. Guárdala como `assets/visuales/manual-2/sem2/M2-sem2-08.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-sem2-08` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
