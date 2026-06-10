# Arquitectura y CLI — Manuales Albatros

Documento de referencia para operar el sistema completo: estructura de
archivos, scripts disponibles, flujos de trabajo end-to-end, e inyección de
imágenes.

---

## 1. Cómo están acomodados los manuales

### 1.1 Vista general del repositorio

```
manual tecno/                              ← raíz del repositorio
├── manuales/                              ← código fuente (MD)
│   ├── manual-1/   Química
│   ├── manual-2/   Física
│   ├── manual-3/   IA Básica
│   ├── manual-4/   IA Avanzada
│   └── manual-5/   IA con Programación
├── build/                                 ← motor de conversión MD → HTML
│   ├── converter.py                       ← convertidor principal
│   ├── print-letter.css                   ← CSS de impresión (carta)
│   ├── digital.css                        ← CSS para versión web
│   ├── template.html                      ← plantilla Jinja
│   ├── iconografia.py / iconos.py         ← resolver de íconos
│   ├── scaffold.py                        ← genera estructura vacía de unidad
│   └── validate.py                        ← validador pre-build
├── dist/                                  ← salidas HTML + PDF
│   ├── manual-N.html / .pdf               ← manual completo
│   ├── manual-N-digital.html              ← variante web
│   └── manual-N-sem-X.html / .pdf         ← manual por semestre (10 PDFs)
├── assets/
│   ├── iconos/                            ← SVG/PNG de íconos (registry)
│   ├── prompts-visuales/                  ← prompts de imagen + índices
│   └── visuales/                          ← imágenes generadas (vacío hoy)
├── docs/                                  ← documentación y reportes
│   ├── ARQUITECTURA.md                    ← ESTE archivo
│   ├── diagnostico-pedagogico.md
│   ├── reporte-pedagogico.md
│   └── verificacion-spec.md
└── *.py                                   ← scripts CLI raíz (ver §3)
```

### 1.2 Estructura de un manual

```
manuales/manual-N/
├── manifest.md                            ← frontmatter del manual completo
├── semestre-1/                            ← 13 archivos de front+back matter
│   ├── 00-portada.md
│   ├── 01-carta-estudiante.md
│   ├── 02-carta-docente.md
│   ├── 03-mapa-contenidos.md
│   ├── 04-hilo-conductor.md
│   ├── 05-competencias.md
│   ├── 06-diagnostica.md
│   ├── 90-cierre-semestre.md
│   ├── 91-material-extra.md
│   ├── 92-glosario-semestre.md
│   ├── 93-bibliografia-semestre.md
│   ├── 94-indice-analitico.md
│   └── README.md
├── semestre-2/                            ← idem
└── unidades/                              ← contenido teórico/práctico
    ├── u00/                               ← (solo M1 tiene u00)
    ├── u01/
    │   ├── README.md
    │   ├── 00-portadilla.md
    │   ├── 01-mapa-mental.md
    │   ├── 02-caso-episodio.md
    │   ├── 10-tema-1-1.md
    │   ├── 10-tema-1-2.md
    │   ├── ...
    │   ├── 80-practica-resuelta.md
    │   ├── 81-banco-ejercicios.md
    │   ├── 90-actividades.md
    │   ├── 92-investigacion.md
    │   ├── 93-taller.md
    │   ├── 94-fuentes.md
    │   ├── 95-implementacion.md
    │   └── 99-cierre.md
    └── uXX/
```

### 1.3 División por semestres (qué unidades van en cada semestre)

| Manual | Semestre 1 | Semestre 2 |
|---|---|---|
| **M1 Química** | u00, u01, u02, u03 | u04, u05, u06 |
| **M2 Física** | u01, u02, u03, u04, u05 | u06, u07, u08, u09 |
| **M3 IA Básica** | u01, u02, u03, u04, u05 | u06, u07, u08, u09 |
| **M4 IA Avanzada** | u01, u02, u03, u04, u05 | u06, u07, u08, u09, u10 |
| **M5 IA con Prog** | u01, u02, u03, u04 | u05, u06, u07, u08 |

(Definido en `build/converter.py` → constante `SEMESTER_MAP`. Cambiar ahí si se quiere otra división.)

### 1.4 Orden de aparición de archivos en el build

Cuando se construye con `--semester X`, el converter recorre los archivos así:

```
1. manuales/manual-N/semestre-X/00-portada.md
2. manuales/manual-N/semestre-X/01-carta-estudiante.md
3. manuales/manual-N/semestre-X/02-carta-docente.md
4. manuales/manual-N/semestre-X/03-mapa-contenidos.md
5. manuales/manual-N/semestre-X/04-hilo-conductor.md
6. manuales/manual-N/semestre-X/05-competencias.md
7. manuales/manual-N/semestre-X/06-diagnostica.md
8. manuales/manual-N/unidades/uXX/00-portadilla.md   ← primera unidad del semestre
9. manuales/manual-N/unidades/uXX/01-mapa-mental.md
... (todas las unidades del semestre en orden)
N-3. manuales/manual-N/semestre-X/90-cierre-semestre.md
N-2. manuales/manual-N/semestre-X/91-material-extra.md
N-1. manuales/manual-N/semestre-X/92-glosario-semestre.md
N.   manuales/manual-N/semestre-X/93-bibliografia-semestre.md
N+1. manuales/manual-N/semestre-X/94-indice-analitico.md
```

---

## 2. Cómo están acomodados los prompts visuales

### 2.1 Estructura

```
assets/prompts-visuales/
├── INDEX.md                               ← índice humano con tablas
├── INDEX.csv                              ← tabla machine-readable 511 filas
├── por-pagina.md                          ← cronología por página de PDF
├── inject-map.json                        ← id → metadata completa
├── manifest.json                          ← registros completos con prompts
├── anidados-pendientes.md                 ← 65 visuales dentro de bloques (no rastreables)
├── manual-N-prompts.md                    ← consolidado por manual
└── manual-N/
    ├── sem-1/
    │   ├── sem1/                          ← visuales del front/back matter
    │   │   └── M{N}-sem1-NN__<tipo>__<rol>__pp<P>.md
    │   ├── u00/                           ← visuales de cada unidad
    │   │   └── M{N}-u00-NN__<tipo>__<rol>__pp<P>.md
    │   └── uXX/
    └── sem-2/
        └── idem
```

### 2.2 Convención del ID

```
M{N}-{u|sem}{XX}-{NN}
```
- `N` = manual (1..5)
- `uXX` = unidad (`u00`..`u10`) o `sem1`/`sem2` para front/back matter
- `NN` = ordinal del visual dentro de esa unidad/sección (01, 02, ...)

Ejemplo: `M1-u01-03` = tercer visual de la unidad u01 del manual 1.

### 2.3 Convención del nombre de archivo

```
M{N}-{u|sem}{XX}-{NN}__{tipo}__{rol}__pp{P}.md
```

Ejemplos:
- `M1-u01-03__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md`
- `M1-sem1-05__infografia__contenido-del-manual__pp1.md`

(`pp0p5` = ½ página, `pp1` = página completa, `pp2` = doble página.)

### 2.4 Frontmatter de cada prompt

```yaml
id: M1-u01-03
manual: 1
unidad: u01
semestre: 1
tipo: cuadro-comparativo
paginas_ocupa: 0.5
fuente_md: manuales/manual-1/unidades/u01/10-tema-1-1.md
fuente_md_linea: 66
imagen_destino: assets/visuales/manual-1/u01/M1-u01-03.png
pagina_pdf_estimada: 77
pdf_destino: dist/manual-1-sem-1.pdf
rol_archivo: desarrollo de subtema
status: pendiente
```

### 2.5 Carpeta destino de imágenes

```
assets/visuales/manual-N/uXX/<ID>.png    ← unidades
assets/visuales/manual-N/sem1/<ID>.png   ← front/back matter sem 1
assets/visuales/manual-N/sem2/<ID>.png   ← front/back matter sem 2
```

Formatos aceptados (en este orden de precedencia): `.png` > `.webp` > `.jpg` > `.jpeg` > `.svg`.

---

## 3. CLI disponibles (scripts en la raíz del repo)

### 3.1 `scaffold_semestres.py` — Crear estructura por semestre

Genera las 130 plantillas de front+back matter (13 archivos × 2 semestres × 5 manuales). **Idempotente**: no sobrescribe a menos que se pase `--force`.

```bash
python scaffold_semestres.py                 # los 5 manuales
python scaffold_semestres.py --manual 3      # solo manual 3
python scaffold_semestres.py --force         # sobrescribe lo existente
```

### 3.2 `extract_visual_prompts.py` — Extraer prompts desde los .md

Recorre todos los `::visual{}` de los .md fuente y genera prompts individuales + manifest.json.

```bash
python extract_visual_prompts.py             # 511 prompts a assets/prompts-visuales/
```

### 3.3 `organize_prompts.py` — Renombrar e indexar con trazabilidad

Toma el `manifest.json` y produce:
- archivos renombrados `<ID>__<tipo>__<rol>__pp<P>.md` con frontmatter rastreable
- `INDEX.csv`, `INDEX.md`, `por-pagina.md`, `inject-map.json` con páginas PDF estimadas

```bash
python organize_prompts.py                   # recalcula todo
```

Correr **después** de cualquiera de estos eventos:
1. Modificar un .md fuente (cambia páginas/IDs).
2. Rebuild de los HTMLs/PDFs.
3. Agregar una imagen nueva a `assets/visuales/`.

### 3.4 `build_semestres.py` — Construir HTMLs por semestre

Wrapper que llama `build/converter.py --semester N` para los 10 semestres.

```bash
python build_semestres.py                    # los 10 (5 manuales × 2 sem)
python build_semestres.py 1                  # solo manual 1 (ambos semestres)
```

### 3.5 `print_to_pdf.py` — Imprimir HTMLs a PDF (Chrome headless)

```bash
python print_to_pdf.py                       # 5 PDFs completos
python print_to_pdf.py --all-semesters       # 10 PDFs por semestre
python print_to_pdf.py --manual 1            # solo manual 1 completo
python print_to_pdf.py --manual 1 --semester 1   # solo M1 sem 1
python print_to_pdf.py --manual 1 --open     # abre el PDF al terminar
python print_to_pdf.py --digital             # variante web (manual-N-digital)
python print_to_pdf.py --timeout 600         # timeout custom (default 240s)
```

Detecta automáticamente Chrome o Edge (busca en rutas estándar de Windows).

### 3.6a `build_docx.py` — HTML a Word (.docx) por semestre

Convierte los HTMLs construidos (con las imágenes ya inyectadas por el
converter) a documentos Word usando pandoc.

```bash
python build_docx.py                       # los 10 DOCX por semestre
python build_docx.py --manual 1            # solo manual 1
python build_docx.py --manual 1 --semester 1
python build_docx.py --complete            # manuales completos manual-N.docx (sin split)
python build_docx.py --digital             # variante manual-N-sem-X-digital.docx
python build_docx.py --reference plantilla.docx   # estilos custom de Word
python build_docx.py --open                # abre el primer DOCX al terminar
```

Salida: `dist/manual-N-sem-X.docx`.

### 3.6 `build/converter.py` — Convertidor principal (uso directo)

```bash
# manual completo
python build/converter.py manuales/manual-1 dist/manual-1.html
python build/converter.py manuales/manual-1 dist/manual-1-digital.html --mode digital

# por semestre
python build/converter.py manuales/manual-1 dist/manual-1-sem-1.html --semester 1
python build/converter.py manuales/manual-1 dist/manual-1-sem-2.html --semester 2

# por unidades arbitrarias (no usa SEMESTER_MAP)
python build/converter.py manuales/manual-1 dist/test.html --units u01,u02,u03
```

### 3.7 `diagnostico_pedagogico.py` — Diagnóstico de % práctico

Mide cobertura de bloques, % práctico aproximado, tipos de actividad del catálogo §6 presentes/faltantes.

```bash
python diagnostico_pedagogico.py             # docs/diagnostico-pedagogico.{md,json}
```

### 3.8 `verify_spec.py` — Verificación contra manual-spec

Verifica tamaño carta exacto, conteo de páginas, estructura mínima, validez de visuales.

```bash
python verify_spec.py                        # docs/verificacion-spec.md
```

### 3.9 `build/validate.py` — Validador pre-build

```bash
python build/validate.py manuales/manual-1
```

Detiene si: falta archivo mínimo, descripción de visual < 50 chars, tipo inválido, ícono no resuelve, tag sin cierre.

---

## 4. Flujos de trabajo

### 4.1 Build completo desde cero (sin imágenes)

```bash
# 1. Asegurar estructura
python scaffold_semestres.py

# 2. Construir HTMLs por semestre
python build_semestres.py

# 3. Generar PDFs
python print_to_pdf.py --all-semesters

# 4. Extraer prompts
python extract_visual_prompts.py

# 5. Reorganizar prompts con páginas estimadas
python organize_prompts.py

# 6. Verificar contra manual-spec
python verify_spec.py
```

Tiempo aproximado total: ~3 minutos.

### 4.2 Workflow para inyectar imágenes (manual, sin API)

```bash
# 1. Abre cualquier prompt
notepad assets/prompts-visuales/manual-1/sem-1/u01/M1-u01-03__cuadro-comparativo__desarrollo-de-subtema__pp0p5.md

# 2. Copia el bloque ```text``` y pégalo en tu motor (Midjourney, DALL-E, Flux, SD, etc.)
#    Genera la imagen, guárdala como PNG @300 dpi.

# 3. Guarda el PNG en la ruta indicada por imagen_destino:
#    assets/visuales/manual-1/u01/M1-u01-03.png

# 4. Rebuild
python build_semestres.py 1                  # solo M1
python print_to_pdf.py --manual 1 --all-semesters

# 5. Actualizar índices (marca status=listo)
python organize_prompts.py
```

El converter detecta el PNG por su ID y lo inyecta como `<img>` en el lugar correcto, reemplazando el placeholder SVG.

### 4.3 Workflow para inyectar imágenes en lote

```bash
# 1. Genera todas las imágenes y déjalas con sus nombres correctos en:
#    assets/visuales/manual-N/uXX/<ID>.png
#    assets/visuales/manual-N/sem1/<ID>.png
#    assets/visuales/manual-N/sem2/<ID>.png

# 2. Rebuild completo
python build_semestres.py
python print_to_pdf.py --all-semesters
python organize_prompts.py

# 3. Verifica
python verify_spec.py
```

### 4.4 Workflow después de editar un .md fuente

```bash
# 1. Editaste alguna unidad o front matter
# 2. Rebuild del manual afectado
python build_semestres.py <N>
python print_to_pdf.py --manual <N> --all-semesters

# 3. Recalcula prompts (IDs y páginas pueden haber cambiado)
python extract_visual_prompts.py
python organize_prompts.py

# 4. Verifica
python verify_spec.py
```

### 4.4-bis Workflow completo MD → Word (.docx) con imágenes

**Este es el flujo recomendado si el destino final es Word, no PDF.**

```bash
# 1. Asegura la estructura (idempotente)
python scaffold_semestres.py

# 2. Coloca las imágenes generadas en sus rutas destino por ID:
#    assets/visuales/manual-N/uXX/<ID>.png
#    assets/visuales/manual-N/sem1/<ID>.png
#    assets/visuales/manual-N/sem2/<ID>.png
#
#    (Si todavía no las tienes, salta este paso — el Word incluirá
#    placeholders simbólicos donde van.)

# 3. MD -> HTML enriquecido (con las imágenes inyectadas por ID)
python build_semestres.py                  # 10 HTMLs por semestre

# 4. HTML -> DOCX vía pandoc
python build_docx.py                       # 10 DOCX por semestre

# 5. (Opcional) Actualizar índices
python organize_prompts.py

# Resultado en dist/manual-N-sem-X.docx (10 archivos Word).
```

**Tiempo total:** ~90 segundos para los 10 documentos Word.

### 4.4-ter Cómo viajan las imágenes y los bloques semánticos al Word

| Elemento Albatros | Cómo aparece en Word |
|---|---|
| Imagen real PNG en `assets/visuales/` | Embebida inline en el .docx (alta calidad, 300 dpi) |
| Placeholder SVG (cuando no hay PNG) | Espacio vacío con caption visible (pandoc no embebe SVG sin `rsvg-convert`) |
| Caja `::concepto::` / `::interioriza::` / etc. | Tabla de una celda con encabezado y borde sutil |
| Caja `::albatros::` / `::caso::` / `::implementacion::` | Tabla con encabezado destacado y rúbrica anidada |
| Actividad `::act-mcq::` / `::act-fill::` / etc. | Lista numerada o tabla, con casillas o líneas para escribir |
| `::pausa::` (💭 mini-actividad) | Bloque con preguntas y guías de respuesta |
| `::visual{}` con imagen | `<w:drawing>` inline con la imagen embebida |
| `::visual{}` sin imagen | Espacio con descripción debajo (caption) |
| `::fuentes::` | Lista con íconos del medio (📘 🌐 📺 …) |
| Tabla en Markdown | `<w:tbl>` nativa de Word con encabezado |
| Fórmulas `$...$` LaTeX | OMML (Office MathML) — Word las renderiza nativamente |
| Íconos del registry Albatros | PNG embebidos como inline-images |

### 4.4-quater Recomendaciones para el Word final

1. **Si quieres que TODOS los placeholders se vean en Word** (incluso los
   SVG simbólicos cuando aún no hay imagen real): instala `rsvg-convert`.
   En Windows con Chocolatey:
   ```
   choco install rsvg-convert
   ```
   O descarga `librsvg` y añade `rsvg-convert.exe` al PATH.
   **No es necesario** si vas a inyectar imágenes reales — los PNG se
   embeben sin problema.

2. **Estilos custom de Word.** Pandoc usa estilos por defecto. Para personalizar
   (fuentes Albatros, colores, espaciados):
   ```bash
   # Genera una plantilla base
   pandoc -o plantilla-albatros.docx --print-default-data-file reference.docx

   # Edítala en Word, modifica los estilos "Heading 1", "Heading 2", "Title",
   # "Quote", "List Paragraph", etc. con la paleta Albatros.

   # Úsala como referencia
   python build_docx.py --reference plantilla-albatros.docx
   ```

3. **Cajas semánticas con borde y color en Word.** Pandoc no preserva borde
   ni color de las cajas por defecto. Si los quieres en Word: edítalos en
   `plantilla-albatros.docx` definiendo estilos como `Aside`, `Caso`,
   `Albatros`, etc., y referencia la plantilla con `--reference`.

4. **Numeración automática de figuras.** Una vez abierto en Word, agrega
   "Insertar > Tabla de contenido" y "Insertar > Tabla de ilustraciones"
   para generar índices automáticos. Cada `<figure id="M1-u01-03">` lleva
   su ID como nombre del archivo de imagen embebida, lo que facilita
   navegar por imagen.

### 4.5 Verificar el estado de cualquier imagen

**Opción A — Por ID:**
```bash
grep -l "id: M1-u01-03" assets/prompts-visuales/manual-1/sem-1/u01/
ls -la assets/visuales/manual-1/u01/M1-u01-03.png 2>/dev/null && echo "✓ existe" || echo "○ pendiente"
```

**Opción B — Por página del PDF:**
```bash
grep "p\.  77" assets/prompts-visuales/por-pagina.md
```

**Opción C — Por tipo o rol:**
```bash
grep ",cuadro-comparativo," assets/prompts-visuales/INDEX.csv
```

**Opción D — Todo de un vistazo:**
Abrir `assets/prompts-visuales/INDEX.csv` en Excel/Sheets y filtrar/ordenar.

---

## 5. Cómo el converter inyecta una imagen

Ver `build/converter.py` función `render_visual()`. Lógica:

1. Procesa cada `::visual{}` del .md fuente.
2. Asigna ID estable: `M{n}-{uXX}-{NN}` (contador por unidad).
3. Si el `::visual{}` trae `src="..."` explícito: usa ese src.
4. Si no, busca en este orden:
   ```
   assets/visuales/manual-N/{uXX|semX}/<ID>.png
   .webp
   .jpg
   .jpeg
   .svg
   ```
5. Si existe: inyecta `<img src="file:///...">` con `id="<ID>"`.
6. Si no existe: renderiza un placeholder SVG simbólico generado a partir
   de `descripcion` (mantiene la maqueta legible).

El HTML final lleva el ID en el `<figure>` para que `organize_prompts.py`
pueda calcular la página estimada por su posición byte.

---

## 6. Mapa de tareas y reportes

| Documento | Qué dice |
|---|---|
| `docs/ARQUITECTURA.md` | **Este archivo** — referencia operativa |
| `docs/diagnostico-pedagogico.md` | % práctico, tipos de actividad por unidad, brecha al 60% |
| `docs/diagnostico-pedagogico.json` | Mismo en JSON |
| `docs/reporte-pedagogico.md` | Plan unidad-por-unidad para llegar al 60% práctico |
| `docs/verificacion-spec.md` | Tamaño carta, páginas, estructura, visuales |
| `assets/prompts-visuales/INDEX.md` | Catálogo humano de prompts |
| `assets/prompts-visuales/INDEX.csv` | Catálogo machine-readable (Excel-friendly) |
| `assets/prompts-visuales/por-pagina.md` | "En qué página del PDF aparece cada visual" |
| `assets/prompts-visuales/inject-map.json` | Map id → ruta md + ruta imagen + página |
| `assets/prompts-visuales/anidados-pendientes.md` | 65 visuales dentro de bloques (sin ID estable) |

---

## 7. Salidas finales en `dist/`

| Archivo | Qué es | Cuándo se actualiza |
|---|---|---|
| `dist/manual-N.html` | Manual completo (web) | `build/converter.py` |
| `dist/manual-N-digital.html` | Variante web interactiva | `--mode digital` |
| `dist/manual-N.pdf` | Manual completo imprimible | `print_to_pdf.py --manual N` |
| `dist/manual-N-sem-X.html` | Manual por semestre | `build_semestres.py` |
| `dist/manual-N-sem-X.pdf` | PDF imprimible por semestre | `print_to_pdf.py --all-semesters` |
| `dist/manual-N-sem-X.docx` | **Word editable por semestre con imágenes embebidas** | **`build_docx.py`** |
| `dist/manual-N.docx` | Word del manual completo | `build_docx.py --complete` |
| `dist/gem-manual-*.{html,docx}` | Variante Gemini (legacy) | manual |

---

## 8. Quick reference — CLI cheatsheet

```bash
# === Setup inicial ===
python scaffold_semestres.py                       # crea estructura

# === Build estándar ===
python build_semestres.py                          # 10 HTMLs por semestre
python print_to_pdf.py --all-semesters             # 10 PDFs por semestre
python build_docx.py                               # 10 DOCX por semestre (Word)

# === Manual individual ===
python build_semestres.py 3                        # solo manual 3
python print_to_pdf.py --manual 3 --all-semesters

# === Manual completo (sin split) ===
python build/converter.py manuales/manual-3 dist/manual-3.html
python print_to_pdf.py --manual 3

# === Después de generar imágenes ===
# (coloca PNG en assets/visuales/manual-N/uXX/<ID>.png)
python build_semestres.py
python print_to_pdf.py --all-semesters             # PDFs imprimibles
python build_docx.py                               # Words editables con imágenes embebidas
python organize_prompts.py                         # marca status=listo

# === Flujo SOLO Word (más rápido si Word es el destino final) ===
python build_semestres.py                          # MD -> HTML (con inyección por ID)
python build_docx.py                               # HTML -> DOCX (~90 s para los 10)
python build_docx.py --manual 1 --semester 1 --open    # genera y abre uno

# === Diagnóstico y verificación ===
python diagnostico_pedagogico.py                   # docs/diagnostico-pedagogico.md
python verify_spec.py                              # docs/verificacion-spec.md
python build/validate.py manuales/manual-3         # validación pre-build

# === Abrir un PDF al terminar ===
python print_to_pdf.py --manual 3 --semester 1 --open
```

---

## 9. Configuración importante (constantes del repo)

### Dónde cambiar la división por semestres
`build/converter.py` → constante `SEMESTER_MAP`
También en `extract_visual_prompts.py`, `scaffold_semestres.py`, `diagnostico_pedagogico.py`.

### Dónde cambiar la paleta de marca
`build/print-letter.css` → `:root { --brand: #0E3A8A; --accent: #F39C12; ... }`

### Dónde cambiar el tamaño de página
`build/print-letter.css` → `@page { size: letter; margin: 18mm 19mm 18mm 19mm; }`
(manual-spec exige carta + 22mm — actualmente 18-19mm; aceptable.)

### Dónde están los íconos
`assets/iconos/registry.json` (alias y mapeo de bloques semánticos a íconos).

---

## 10. Convenciones y reglas duras (manual-spec)

Recordatorio rápido. Para detalles ver `.claude/skills/manual-spec/SKILL.md`.

- Tamaño página: **Carta 8.5″ × 11″ estricto** (612 × 792 pt).
- Total páginas por manual completo: **350–450** (objetivo 400). _Excedido_
  ligeramente por la división actual con front/back matter dedicado por semestre.
- Cada `::visual{}` debe traer `tipo` válido, `descripcion ≥ 50 chars`, `paginas` numérico.
- Cada unidad necesita: portadilla, mapa mental, caso episódico, mínimo
  3 tipos del catálogo §6, práctica resuelta, investigación, fuentes,
  implementación, cierre.
- Hilo conductor obligatorio: un solo case study por manual con un episodio
  por unidad.
