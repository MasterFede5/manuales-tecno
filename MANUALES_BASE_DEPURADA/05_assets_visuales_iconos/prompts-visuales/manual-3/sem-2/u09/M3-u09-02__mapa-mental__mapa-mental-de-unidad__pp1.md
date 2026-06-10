---
id: M3-u09-02
manual: 3
unidad: u09
semestre: 2
tipo: mapa-mental
paginas_ocupa: 1
fuente_md: manuales/manual-3/unidades/u09/01-mapa-mental.md
fuente_md_linea: 9
imagen_destino: assets/visuales/manual-3/u09/M3-u09-02.jpg
pagina_pdf_estimada: 190
pdf_destino: dist/manual-3-sem-2.pdf
rol_archivo: mapa mental de unidad
status: pendiente
---

# `M3-u09-02`

**Tipo visual:** `mapa-mental` · **Ocupa:** 1 pp · **Página PDF estimada:** 190

**Manual 3 · U09 — Ética y publicación responsable · Semestre 2**

> Rol del archivo: _mapa mental de unidad_

## Trazabilidad

| Campo | Valor |
|---|---|
| ID estable | `M3-u09-02` |
| Archivo destino imagen | `assets/visuales/manual-3/u09/M3-u09-02.jpg` |
| PDF en el que aparece | `dist/manual-3-sem-2.pdf` |
| Página PDF estimada | **p. 190** |
| Archivo Markdown fuente | `manuales/manual-3/unidades/u09/01-mapa-mental.md:9` |
| Tipo de placeholder | `mapa-mental` |
| Espacio reservado | 1 página(s) |

## Descripción original del manual

> Mapa mental con nodo central 'Ética, sesgo y uso responsable' del que salen 6 ramas principales en colores distintos: 1) Sesgos en datos y resultados (sub-nodos: sesgo de selección, sesgo histórico, sesgo de confirmación, mitigación, auditoría). 2) Privacidad y datos personales (PII, datos sensibles, LFPDPPP, GDPR, derechos ARCO, opt-out de entrenamiento). 3) Derechos de autor (obras derivadas, fair use, atribución, licencias Creative Commons, output IA y autoría). 4) Deepfakes y desinformación (síntesis de voz/rostro, detección, marcas de agua, C2PA, daño reputacional). 5) Impacto laboral y educativo (automatización vs aumento, reskilling, plagio académico, evaluación auténtica). 6) Ley de IA en México y UE (AI Act, niveles de riesgo, NOMs, sandbox regulatorio, autoridad). Cada rama con palabras clave en burbujas y un ícono pequeño. Estilo limpio para impresión B/N.

## Prompt visual super-específico

```text
**ESTILO Y MARCA (obligatorio):**
Ilustración editorial educativa estilo Albatros. Paleta dual estricta: azul profundo `#0E3A8A` como primario y naranja vibrante `#F39C12` como acento (verde `#1E8449` solo si es rama Tecno; gris `#4A4A4A` y blanco puro para texto y fondo). Trazos limpios outline + duotone, sin photoreal, sin estilo cartoon infantil. Tipografía sans-serif moderna legible. Fondo blanco con generoso whitespace. Impresión carta a 300 dpi, reproducible en B/N.

**CONTEXTO DE USO:**
- Manual: **Inteligencia Artificial Básica** — Alfabetización en IA Generativa
- Unidad: **U09 — Ética y publicación responsable**
- Case study: *Mi tutor IA personal — capa por capa de un asistente educativo*
- Rol del archivo: **mapa mental de unidad**
- Tipo de visual: **mapa-mental**
- Ocupación: **1** página(s) → página completa carta · 8.5x11 in · portrait · `--ar 17:22`

**COMPOSICIÓN REQUERIDA (mapa-mental):**
MAPA MENTAL radial: nodo central grande, 4-7 ramas curvas a sub-nodos, cada rama en color sólido distinto dentro de paleta Albatros; hojas con micro-ilustración.

**CONTENIDO ESPECÍFICO (respeta literalmente, no inventes):**
Mapa mental con nodo central 'Ética, sesgo y uso responsable' del que salen 6 ramas principales en colores distintos: 1) Sesgos en datos y resultados (sub-nodos: sesgo de selección, sesgo histórico, sesgo de confirmación, mitigación, auditoría). 2) Privacidad y datos personales (PII, datos sensibles, LFPDPPP, GDPR, derechos ARCO, opt-out de entrenamiento). 3) Derechos de autor (obras derivadas, fair use, atribución, licencias Creative Commons, output IA y autoría). 4) Deepfakes y desinformación (síntesis de voz/rostro, detección, marcas de agua, C2PA, daño reputacional). 5) Impacto laboral y educativo (automatización vs aumento, reskilling, plagio académico, evaluación auténtica). 6) Ley de IA en México y UE (AI Act, niveles de riesgo, NOMs, sandbox regulatorio, autoridad). Cada rama con palabras clave en burbujas y un ícono pequeño. Estilo limpio para impresión B/N.

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
2. Guárdala como `assets/visuales/manual-3/u09/M3-u09-02.jpg` (JPG @300 dpi, calidad alta).
3. Re-build del manual:

   ```bash
   python build_semestres.py 3
   python print_to_pdf.py --manual 3 --all-semesters
   ```

4. Verifica que `M3-u09-02` ya no esté en estado `pendiente` corriendo:

   ```bash
   python organize_prompts.py
   ```
