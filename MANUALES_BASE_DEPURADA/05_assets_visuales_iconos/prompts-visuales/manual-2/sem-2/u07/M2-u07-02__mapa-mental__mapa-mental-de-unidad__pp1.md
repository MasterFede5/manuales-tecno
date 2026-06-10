---
id: M2-u07-02
manual: 2
unidad: u07
semestre: 2
tipo: mapa-mental
paginas_ocupa: 1
fuente_md: manuales/manual-2/unidades/u07/01-mapa-mental.md
fuente_md_linea: 9
imagen_destino: assets/visuales/manual-2/u07/M2-u07-02.jpg
pagina_pdf_estimada: 53
pdf_destino: dist/manual-2-sem-2.pdf
rol_archivo: mapa mental de unidad
status: pendiente
---

# `M2-u07-02`

**Tipo visual:** `mapa-mental` · **Ocupa:** 1 pp · **Página PDF estimada:** 53

**Manual 2 · U07 — Mecánica de Fluidos · Semestre 2**

> Rol del archivo: _mapa mental de unidad_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M2-u07-02` |
| Archivo destino imagen | `assets/visuales/manual-2/u07/M2-u07-02.jpg` |
| PDF en el que aparece | `dist/manual-2-sem-2.pdf` |
| Página PDF estimada | **p. 53** |
| Archivo Markdown fuente | `manuales/manual-2/unidades/u07/01-mapa-mental.md:9` |
| Tipo de placeholder | `mapa-mental` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Mapa mental con nodo central FLUIDOS y dos grandes ramas: 1) FLUIDOS EN REPOSO — sub-ramas: densidad (ρ=m/V), presión hidrostática (P=ρgh), principio de Pascal (prensa hidráulica), principio de Arquímedes (E=ρ_f·V_d·g), capilaridad y tensión superficial. 2) FLUIDOS EN MOVIMIENTO — sub-ramas: caudal (Q=Av), ecuación de continuidad (A1v1=A2v2), ecuación de Bernoulli (P+½ρv²+ρgh=cte), viscosidad y régimen turbulento (Reynolds). En el centro inferior, ícono del coche F1 conectado a Bernoulli con flecha 'downforce'.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Física Albatros** — Mecánica, Termodinámica, Ondas, Electromagnetismo y Física Contemporánea
- Unidad: **U07 — Mecánica de Fluidos**
- Case study: *Equipo F1 Albatros — diseño y telemetría de un coche escolar*
- Rol del archivo: **mapa mental de unidad**
- Tipo de visual: **mapa-mental**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (mapa-mental):**
MAPA MENTAL radial: nodo central grande, 4-7 ramas curvas a sub-nodos, cada rama en color sólido distinto dentro de paleta Albatros; hojas con micro-ilustración.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Mapa mental con nodo central FLUIDOS y dos grandes ramas: 1) FLUIDOS EN REPOSO — sub-ramas: densidad (ρ=m/V), presión hidrostática (P=ρgh), principio de Pascal (prensa hidráulica), principio de Arquímedes (E=ρ_f·V_d·g), capilaridad y tensión superficial. 2) FLUIDOS EN MOVIMIENTO — sub-ramas: caudal (Q=Av), ecuación de continuidad (A1v1=A2v2), ecuación de Bernoulli (P+½ρv²+ρgh=cte), viscosidad y régimen turbulento (Reynolds). En el centro inferior, ícono del coche F1 conectado a Bernoulli con flecha 'downforce'.

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
2. Guárdala como `assets/visuales/manual-2/u07/M2-u07-02.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 2
   python print_to_pdf.py --manual 2 --all-semesters
   ```

4. Verifica que `M2-u07-02` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
