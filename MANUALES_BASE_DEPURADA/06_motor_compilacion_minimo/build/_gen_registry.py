#!/usr/bin/env python3
"""Generador del registry.json — fuente única de verdad de íconos Albatros.

Edita las tuplas ICONS_BY_CATEGORY de abajo, luego corre:
    python build/_gen_registry.py
y se regenera assets/iconos/registry.json
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# (suffix, alias, emoji, concepto-visual)
ICONS_BY_CATEGORY = {
    "bloques": [
        ("concepto",        ["concepto", "definicion", "libro-abierto"],          "📘", "Libro abierto con marcador"),
        ("interioriza",     ["interioriza", "foco", "idea", "lampara"],           "💡", "Foco encendido con rayos"),
        ("pausa",           ["pausa", "pensar", "burbuja-pensamiento"],           "💭", "Burbuja de pensamiento"),
        ("practica",        ["practica", "pluma", "escribir"],                    "📝", "Pluma sobre hoja"),
        ("caso",            ["caso", "brujula"],                                  "🧭", "Brújula apuntando al norte"),
        ("implementacion",  ["implementacion", "cohete", "lanzar"],               "🚀", "Cohete despegando"),
        ("albatros",        ["albatros", "diana", "target"],                      "🎯", "Diana con flecha clavada"),
        ("tecno",           ["tecno", "engranaje", "tuerca"],                     "🔧", "Engranaje con llave"),
        ("investiga",       ["investiga", "investigacion", "lupa-docs"],          "🔎", "Lupa sobre documento"),
        ("fuentes",         ["fuentes", "biblioteca", "libros-pila"],             "📚", "Pila de libros"),
    ],
    "actividades": [
        ("fill",       ["fill", "rellenar", "lineas-respuesta"],   "✏️",  "Lápiz sobre líneas"),
        ("mcq",        ["mcq", "opcion-multiple", "casillas"],     "🔘",  "Casillas con check"),
        ("table",      ["table", "tabla", "celdas-vacias"],        "📊",  "Cuadrícula con celdas"),
        ("calc",       ["calc", "calculadora", "cuadricula-calc"], "🧮",  "Calculadora con cuadrícula"),
        ("match",      ["match", "relacion", "cadena", "flechas"], "🔗",  "Cadena con flechas"),
        ("puzzle",     ["puzzle", "crucigrama", "rompecabezas"],   "🧩",  "Pieza de puzzle"),
        ("mindmap",    ["mindmap", "mapa-mental-act"],             "🧠",  "Cerebro con ramas"),
        ("label",      ["label", "etiqueta", "diagrama-etiquetar"],"🏷️", "Etiqueta numerada"),
        ("case",       ["case", "carpeta", "expediente"],          "📂",  "Carpeta abierta"),
        ("challenge",  ["challenge", "reto-act", "trofeo"],        "🏆",  "Trofeo con cohete"),
        ("tf",         ["tf", "verdadero-falso", "check-cruz"],    "✅",  "Check + cruz"),
        ("order",      ["order", "ordenar", "pasos"],              "🔢",  "Lista numerada con pasos"),
    ],
    "fuentes": [
        ("libro",     ["libro", "book"],                  "📘", "Libro cerrado de costado"),
        ("web",       ["web", "internet", "globo"],       "🌐", "Globo terráqueo + cursor"),
        ("ocw",       ["ocw", "academia", "birrete"],     "🎓", "Birrete académico"),
        ("video",     ["video", "play", "claqueta"],      "📺", "Claqueta + play"),
        ("articulo",  ["articulo", "periodico", "news"],  "📰", "Periódico doblado"),
        ("mexicana",  ["mexicana", "mx", "mexico"],       "🇲🇽", "Silueta MX con bandera"),
    ],
    "albatros-tipos": [
        ("experimento",          ["experimento", "matraz", "lab"],        "🧪", "Matraz con burbujas"),
        ("debate",               ["debate", "burbujas-opuestas"],         "🗣️", "Dos burbujas opuestas"),
        ("taller",               ["taller", "martillo-llave"],            "🛠️", "Martillo + llave inglesa"),
        ("caso",                 ["albatros-caso", "expediente-lupa"],    "📁", "Expediente con lupa"),
        ("reto",                 ["reto", "bandera-meta"],                "🏁", "Bandera de meta"),
        ("simulacion",           ["simulacion", "monitor-engranaje"],     "🖥️", "Monitor con engranaje"),
        ("investigacion-corta",  ["investigacion-corta", "lupa-hoja"],    "🔬", "Microscopio / lupa con hoja"),
    ],
    "tecno-tipos": [
        ("maker",      ["maker", "impresora-3d"],         "🖨️", "Impresora 3D"),
        ("circuito",   ["circuito", "placa", "pcb"],      "🔌", "Placa con componentes"),
        ("codigo",     ["codigo", "code", "llaves"],      "💻", "Llaves { } de código"),
        ("dato",       ["dato", "data", "db"],            "🗄️", "Cilindro de base de datos"),
        ("iot",        ["iot", "nube-dispositivos"],      "📡", "Nube + dispositivos conectados"),
        ("prototipo",  ["prototipo", "wireframe"],        "📐", "Objeto en wireframe"),
    ],
    "visuales": [
        ("infografia",        ["infografia", "info"],                 "📊", "Hoja con barras + texto"),
        ("mapa-mental",       ["mapa-mental-vis", "ramas"],           "🧠", "Nodo central + ramas"),
        ("cuadro-comp",       ["cuadro-comp", "comparativo"],         "📋", "Dos columnas"),
        ("linea-tiempo",      ["linea-tiempo", "timeline"],           "📅", "Línea con hitos"),
        ("diagrama-flujo",    ["diagrama-flujo", "flowchart"],        "🔄", "Cajas conectadas"),
        ("ilustracion",       ["ilustracion", "marco-paisaje"],       "🖼️", "Marco con paisaje"),
        ("interfaz",          ["interfaz", "ui", "ventana"],          "🖥️", "Ventana con menús"),
        ("tabla-grande",      ["tabla-grande", "grid"],               "📑", "Tabla amplia"),
        ("grafica",           ["grafica", "chart"],                   "📈", "Gráfica de líneas"),
    ],
    "pedagogico": [
        ("bloom-recordar",    ["bloom-recordar"],         "🧠", "Bombillo + memoria"),
        ("bloom-comprender",  ["bloom-comprender"],       "👁️", "Ojos sobre libro"),
        ("bloom-aplicar",     ["bloom-aplicar"],          "🛠️", "Engranaje en mano"),
        ("bloom-analizar",    ["bloom-analizar"],         "🔍", "Lupa sobre gráfica"),
        ("bloom-evaluar",     ["bloom-evaluar"],          "⚖️", "Balanza"),
        ("bloom-crear",       ["bloom-crear"],            "✨", "Lápiz + chispa"),
        ("nivel-1",           ["nivel-1", "basico"],      "⭐", "1 estrella"),
        ("nivel-2",           ["nivel-2", "intermedio"],  "🌟", "2 estrellas"),
        ("nivel-3",           ["nivel-3", "avanzado"],    "💫", "3 estrellas"),
    ],
    "flujo": [
        ("diagnostica",     ["diagnostica", "diagnostico"], "📋", "Clipboard con check"),
        ("examen",          ["examen", "test", "prueba"],   "📝", "Hoja + lápiz + reloj"),
        ("glosario",        ["glosario", "abc"],            "🔤", "Libro con letras ABC"),
        ("bibliografia",    ["bibliografia", "estante"],    "📚", "Estante de libros"),
        ("indice",          ["indice", "lista-alfabetica"], "🔖", "Hoja con lista alfabética"),
    ],
    "manuales": [
        ("1-quimica",         ["quimica", "manual-1"],       "🧪", "Matraz + molécula H₂O"),
        ("2-fisica",          ["fisica", "manual-2"],        "⚛️", "Átomo + coche F1 estilizado"),
        ("3-ia-basica",       ["ia-basica", "manual-3"],     "🤖", "Chatbot conversando"),
        ("4-ia-avanzada",     ["ia-avanzada", "manual-4"],   "🧠", "Nodo + agentes conectados"),
        ("5-ia-programacion", ["ia-prog", "manual-5"],       "💻", "Terminal con prompt"),
    ],
    "decorativos": [
        ("tip",          ["tip", "consejo"],            "💡", "Foco con destellos"),
        ("warning",      ["warning", "alerta", "cuidado"], "⚠️", "Triángulo con signo de !"),
        ("success",      ["success", "ok", "correcto"], "✅", "Check verde"),
        ("error",        ["error", "incorrecto"],       "❌", "Cruz roja"),
        ("tiempo",       ["tiempo", "duracion", "reloj"], "⏱️", "Cronómetro"),
        ("grupo",        ["grupo", "equipo"],           "👥", "3 personas en grupo"),
        ("individual",   ["individual", "solo"],        "👤", "1 persona sola"),
        ("rubrica",      ["rubrica", "evaluacion-est"], "🌟", "Estrellas + check"),
    ],
}

LOGOS = [
    ("color",  ["albatros-color"],  "Logo Albatros completo a color"),
    ("mono",   ["albatros-mono"],   "Logo Albatros monocromo azul"),
    ("white",  ["albatros-white"],  "Logo Albatros blanco"),
    ("mini",   ["albatros-mini"],   "Logo Albatros mini cuadrado 64×64"),
    ("tecno",  ["albatros-tecno"],  "Logo Albatros + engranaje (variante Tecno)"),
]

PREFIX_BY_CAT = {
    "bloques": "bloque",
    "actividades": "act",
    "fuentes": "fuente",
    "albatros-tipos": "tipo-albatros",
    "tecno-tipos": "tipo-tecno",
    "visuales": "visual",
    "pedagogico": "",   # ya viene en el suffix (bloom-*, nivel-*)
    "flujo": "flujo",
    "manuales": "manual",
    "decorativos": "decor",
}


def build_registry() -> dict:
    icons: dict = {}

    for cat, items in ICONS_BY_CATEGORY.items():
        prefix = PREFIX_BY_CAT[cat]
        for suffix, aliases, emoji, concepto in items:
            key = f"{prefix}-{suffix}" if prefix else suffix
            file_id = f"ico-{key}"
            icons[key] = {
                "id": file_id,
                "categoria": cat,
                "alias": aliases,
                "emoji": emoji,
                "concepto": concepto,
                "svg":      f"{cat}/{file_id}.svg",
                "svg_mono": f"{cat}/{file_id}-mono.svg",
                "png":      f"{cat}/{file_id}.png",
                "estado":   "pendiente",
                "color_primario": "#0E3A8A",
                "color_acento":   "#F39C12",
            }

    # Logos (categoría especial)
    for suffix, aliases, concepto in LOGOS:
        key = f"logo-{suffix}"
        icons[key] = {
            "id": key,
            "categoria": "logo",
            "alias": aliases,
            "emoji": "🛡️",
            "concepto": concepto,
            "svg":      f"logo/{key}.svg",
            "svg_mono": f"logo/{key}-mono.svg",
            "png":      f"logo/{key}.png",
            "estado":   "pendiente",
            "color_primario": "#0E3A8A",
            "color_acento":   "#F39C12",
        }

    return {
        "version": "1.0",
        "estilo": "outline + duotone",
        "tamano_base": "256x256",
        "paleta": {
            "primario": "#0E3A8A",
            "acento":   "#F39C12",
            "tecno":    "#1E8449",
            "neutro":   "#5C6F7A",
            "crema":    "#FFF8E7",
            "blanco":   "#FFFFFF",
        },
        "total": len(icons),
        "icons": icons,
    }


def main():
    out = Path(__file__).parent.parent / "assets" / "iconos" / "registry.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    reg = build_registry()
    out.write_text(json.dumps(reg, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✓ Registry generado: {out}")
    print(f"  Total: {reg['total']} íconos en {len(set(v['categoria'] for v in reg['icons'].values()))} categorías")


if __name__ == "__main__":
    main()
