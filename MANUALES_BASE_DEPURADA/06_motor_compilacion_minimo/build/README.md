# Build — Manuales Albatros (doc-as-code)

Pipeline para convertir el contenido `.md` de un manual en un HTML imprimible
tamaño carta (8.5″×11″). Implementa la skill `manual-html-build`.

## Requisitos

- Python 3.10+
- `pip install markdown jinja2 pyyaml`

## Estructura

```
build/
├── converter.py        ← script principal MD → HTML
├── print-letter.css    ← estilos imprimibles tamaño carta
├── digital.css         ← estilos para versión digital interactiva
├── template.html       ← shell HTML (Jinja2)
├── example/
│   └── example.md      ← demo con todos los bloques y actividades
└── README.md           ← este archivo
```

## Uso

### Construir un manual completo

```bash
python build/converter.py manuales/manual-1 dist/manual-1.html
```

Lee:
- `manuales/manual-1/manifest.md`
- Cualquier `.md` suelto en la raíz
- Todas las `unidades/u01/`, `u02/`, … en orden

Escribe el HTML resultante en `dist/manual-1.html`.

### Modo digital (con interactividad)

```bash
python build/converter.py manuales/manual-1 dist/manual-1-digital.html --mode digital
```

### Construir un solo archivo (demo)

Para probar con el ejemplo:

```bash
mkdir -p manuales/_demo/unidades/u01
cp build/example/example.md manuales/_demo/unidades/u01/10-tema-1-1.md
python build/converter.py manuales/_demo dist/demo.html
```

### Generar PDF imprimible

Usar Chromium headless en el HTML imprimible:

```bash
chrome --headless --disable-gpu \
  --print-to-pdf=dist/manual-1.pdf \
  --no-pdf-header-footer \
  --print-to-pdf-no-header \
  dist/manual-1.html
```

O bien `playwright`:

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_page()
    page.goto('file://' + os.path.abspath('dist/manual-1.html'))
    page.pdf(path='dist/manual-1.pdf', format='Letter')
    b.close()
```

## Bloques que el converter renderiza

### Bloques semánticos
- `::concepto::` → caja azul Albatros con definición formal
- `::interioriza::` → caja crema con analogía / ejemplo cotidiano
- `::pausa::` → caja amarilla 💭 con líneas de respuesta
- `::practica::` → caja gris con pasos numerados
- `::caso::` → episodio del case study, banda lateral degradada
- `::implementacion::` → caja destacada 🚀 con rúbrica
- `::albatros::` → 🎯 Actividad Albatros (tipo, tiempo, entregable)
- `::investiga::` → 🔎 Apartado de Investigación (medios propios)
- `::fuentes::` → 📚 Fuentes recomendadas curadas
- `::visual::` → placeholder de infografía/mapa con dimensión

### Catálogo de actividades
- `::act-fill::` líneas continuas para escribir
- `::act-mcq::` opción múltiple con casillas
- `::act-table::` tabla a completar
- `::act-calc::` cuadrícula 5 mm para cálculo
- `::act-match::` relación de columnas
- `::act-tf::` verdadero / falso justificado
- `::act-order::` ordenar pasos
- `::act-case::` caso para resolver con líneas
- `::act-puzzle::` crucigrama / sopa
- `::act-mindmap::` mapa mental abierto
- `::act-label::` diagrama para etiquetar
- `::act-challenge::` 🚀 reto Albatros

## Sintaxis general

```
::tipo{atributo="valor" otro=valor}::
contenido en Markdown estándar (negritas, listas, tablas, etc.)
::/tipo::
```

Los atributos con espacios deben ir entre comillas. Cada apertura
`::tipo::` debe cerrarse con `::/tipo::` exactamente del mismo nombre.

## Validación

El script imprime un resumen al terminar:

```
✓ Construido: dist/manual-1.html  (modo: print, archivos: 47)
```

Para validar el conteo de páginas, abrir el HTML en Chrome → Print
preview → confirmar:
- Tamaño: **US Letter** (8.5" × 11")
- Páginas totales en rango **350–450**

(Pendiente: validador automático de páginas con headless Chromium.)

## Vinculación con las skills

Este pipeline implementa la skill `manual-html-build` y consume MD producido
bajo `manual-md-author`, respetando las restricciones de `manual-spec`.
Antes de ejecutar el build, asegurarse de que el contenido MD pasa la
validación previa de `manual-md-author` §9.
