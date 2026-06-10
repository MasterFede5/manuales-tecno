---
id: M1-u03-02
manual: 1
unidad: u03
semestre: 1
tipo: mapa-mental
paginas_ocupa: 1
fuente_md: manuales/manual-1/unidades/u03/01-mapa-mental.md
fuente_md_linea: 9
imagen_destino: assets/visuales/manual-1/u03/M1-u03-02.jpg
pagina_pdf_estimada: 193
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: mapa mental de unidad
status: pendiente
---

# `M1-u03-02`

**Tipo visual:** `mapa-mental` · **Ocupa:** 1 pp · **Página PDF estimada:** 193

**Manual 1 · U03 — Aire · Semestre 1**

> Rol del archivo: _mapa mental de unidad_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M1-u03-02` |
| Archivo destino imagen | `assets/visuales/manual-1/u03/M1-u03-02.jpg` |
| PDF en el que aparece | `dist/manual-1-sem-1.pdf` |
| Página PDF estimada | **p. 193** |
| Archivo Markdown fuente | `manuales/manual-1/unidades/u03/01-mapa-mental.md:9` |
| Tipo de placeholder | `mapa-mental` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Mapa mental con nodo central AIRE y seis ramas: 1) COMPOSICIÓN (N2 78%, O2 21%, Ar, CO2, vapor); 2) REACCIONES DEL O2 (combustión completa, incompleta, óxidos básicos vs ácidos); 3) REDOX (oxidación, reducción, balanceo por tanteo y método ion-electrón); 4) CICLOS (carbono, nitrógeno, oxígeno con flechas entre atmósfera, biósfera, hidrósfera); 5) CONTAMINANTES (NOx, SOx, CO, partículas PM2.5, ozono troposférico); 6) FENÓMENOS (smog fotoquímico, inversión térmica, lluvia ácida, efecto invernadero).

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Química Albatros** — Materia, Agua, Aire, Alimentos y Energía
- Unidad: **U03 — Aire**
- Case study: *Agua escolar saludable — bebedero del patio contaminado*
- Rol del archivo: **mapa mental de unidad**
- Tipo de visual: **mapa-mental**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (mapa-mental):**
MAPA MENTAL radial: nodo central grande, 4-7 ramas curvas a sub-nodos, cada rama en color sólido distinto dentro de paleta Albatros; hojas con micro-ilustración.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Mapa mental con nodo central AIRE y seis ramas: 1) COMPOSICIÓN (N2 78%, O2 21%, Ar, CO2, vapor); 2) REACCIONES DEL O2 (combustión completa, incompleta, óxidos básicos vs ácidos); 3) REDOX (oxidación, reducción, balanceo por tanteo y método ion-electrón); 4) CICLOS (carbono, nitrógeno, oxígeno con flechas entre atmósfera, biósfera, hidrósfera); 5) CONTAMINANTES (NOx, SOx, CO, partículas PM2.5, ozono troposférico); 6) FENÓMENOS (smog fotoquímico, inversión térmica, lluvia ácida, efecto invernadero).

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
2. Guárdala como `assets/visuales/manual-1/u03/M1-u03-02.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 1
   python print_to_pdf.py --manual 1 --all-semesters
   ```

4. Verifica que `M1-u03-02` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
