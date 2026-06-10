from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "05_assets_visuales_iconos" / "visuales" / "manual-2" / "u01"


BLUE = "#0E3A8A"
CYAN = "#0E7490"
ORANGE = "#F39C12"
GREEN = "#15803D"
INK = "#172033"
MUTED = "#5B6472"
SOFT = "#F7FAFC"
LINE = "#D8DEE9"


def t(value: object) -> str:
    return escape(str(value), quote=True)


def header(title: str, subtitle: str, width: int, height: int) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <style>
      .title {{ font-family: Arial, sans-serif; font-size: 56px; font-weight: 800; fill: {BLUE}; }}
      .subtitle {{ font-family: Arial, sans-serif; font-size: 30px; font-weight: 600; fill: {MUTED}; }}
      .h {{ font-family: Arial, sans-serif; font-size: 34px; font-weight: 800; fill: {BLUE}; }}
      .body {{ font-family: Arial, sans-serif; font-size: 27px; font-weight: 600; fill: {INK}; }}
      .small {{ font-family: Arial, sans-serif; font-size: 23px; font-weight: 600; fill: {MUTED}; }}
      .formula {{ font-family: Arial, sans-serif; font-size: 35px; font-weight: 800; fill: {ORANGE}; }}
      .label {{ font-family: Arial, sans-serif; font-size: 25px; font-weight: 800; fill: white; }}
    </style>
  </defs>
  <rect width="100%" height="100%" fill="white"/>
  <rect x="0" y="0" width="{width}" height="18" fill="{ORANGE}"/>
  <text x="54" y="76" class="title">{t(title)}</text>
  <text x="56" y="120" class="subtitle">{t(subtitle)}</text>
"""


def footer(width: int, height: int) -> str:
    return f"""
  <text x="{width - 56}" y="{height - 35}" text-anchor="end" class="small">Colegio Nuevo Tecno · Física · Unidad 1</text>
</svg>
"""


def box(x: int, y: int, w: int, h: int, title: str, lines: list[str], formula: str = "", color: str = CYAN) -> str:
    line_svg = []
    yy = y + 92
    for line in lines:
        line_svg.append(f'<text x="{x + 28}" y="{yy}" class="body">{t(line)}</text>')
        yy += 36
    formula_svg = f'<text x="{x + 28}" y="{y + h - 34}" class="formula">{t(formula)}</text>' if formula else ""
    return f"""
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{SOFT}" stroke="{LINE}" stroke-width="3"/>
  <rect x="{x}" y="{y}" width="{w}" height="58" rx="18" fill="{color}"/>
  <text x="{x + 28}" y="{y + 40}" class="label">{t(title)}</text>
  {''.join(line_svg)}
  {formula_svg}
"""


def arrow(x1: int, y1: int, x2: int, y2: int, color: str = ORANGE) -> str:
    return f"""
  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="9" stroke-linecap="round"/>
  <polygon points="{x2},{y2} {x2-26},{y2-15} {x2-26},{y2+15}" fill="{color}"/>
"""


def write(name: str, svg: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(svg, encoding="utf-8", newline="\n")


def visual_02() -> str:
    width, height = 1536, 1024
    svg = header("Tipos de movimiento en cinemática", "Elige el modelo según trayectoria, velocidad y aceleración", width, height)
    svg += box(70, 175, 420, 250, "MRU", ["Línea recta", "Velocidad constante", "Aceleración = 0"], "x = x0 + vt", BLUE)
    svg += box(518, 175, 420, 250, "MRUA", ["Línea recta", "Aceleración constante", "La velocidad cambia"], "v = v0 + at", CYAN)
    svg += box(966, 175, 420, 250, "Caída libre", ["Movimiento vertical", "La aceleración es g", "No depende de la masa"], "g = 9.8 m/s²", GREEN)
    svg += box(180, 515, 520, 270, "Movimiento parabólico", ["Trayectoria curva", "Eje x: velocidad constante", "Eje y: aceleración g"], "x = vxt · t", ORANGE)
    svg += box(820, 515, 520, 270, "Movimiento circular", ["Trayectoria circular", "Rapidez puede ser constante", "Aceleración hacia el centro"], "ac = v² / r", BLUE)
    svg += arrow(705, 425, 770, 425)
    svg += f"""
  <rect x="215" y="842" width="1106" height="92" rx="18" fill="#FFF8E8" stroke="{ORANGE}" stroke-width="3"/>
  <text x="768" y="884" text-anchor="middle" class="h">Pregunta guía</text>
  <text x="768" y="922" text-anchor="middle" class="body">¿El coche va en línea recta, acelera, cae, se curva o gira?</text>
"""
    return svg + footer(width, height)


def visual_05() -> str:
    width, height = 1536, 1024
    svg = header("MRU: movimiento rectilíneo uniforme", "La velocidad permanece constante y la aceleración es cero", width, height)
    svg += f"""
  <line x1="130" y1="760" x2="1370" y2="760" stroke="{LINE}" stroke-width="6"/>
  <circle cx="220" cy="760" r="24" fill="{BLUE}"/><text x="220" y="815" text-anchor="middle" class="small">0 s</text>
  <circle cx="510" cy="760" r="24" fill="{BLUE}"/><text x="510" y="815" text-anchor="middle" class="small">1 s</text>
  <circle cx="800" cy="760" r="24" fill="{BLUE}"/><text x="800" y="815" text-anchor="middle" class="small">2 s</text>
  <circle cx="1090" cy="760" r="24" fill="{BLUE}"/><text x="1090" y="815" text-anchor="middle" class="small">3 s</text>
  <text x="760" y="890" text-anchor="middle" class="formula">Distancias iguales en tiempos iguales</text>
"""
    svg += box(80, 175, 430, 330, "Gráfica x-t", ["Recta ascendente", "La pendiente es v", "Más inclinada = más rápida"], "v = Δx / Δt", BLUE)
    svg += box(548, 175, 430, 330, "Gráfica v-t", ["Línea horizontal", "Velocidad constante", "Área = desplazamiento"], "Δx = v · t", CYAN)
    svg += box(1016, 175, 430, 330, "Gráfica a-t", ["Línea en cero", "No cambia la velocidad", "No hay aceleración"], "a = 0", GREEN)
    return svg + footer(width, height)


def visual_06() -> str:
    width, height = 1536, 1024
    svg = header("MRUA: velocidad que cambia", "La aceleración es constante y modifica la velocidad cada segundo", width, height)
    svg += box(80, 175, 430, 330, "Posición x-t", ["Curva parabólica", "El avance por segundo crece", "Si frena, la curva cambia"], "x = x0 + v0t + 1/2at²", BLUE)
    svg += box(548, 175, 430, 330, "Velocidad v-t", ["Recta inclinada", "La pendiente es a", "Área = desplazamiento"], "v = v0 + at", CYAN)
    svg += box(1016, 175, 430, 330, "Aceleración a-t", ["Línea horizontal", "Valor constante", "Puede ser positiva o negativa"], "a = Δv / Δt", GREEN)
    svg += f"""
  <rect x="160" y="615" width="1216" height="180" rx="24" fill="#FFF8E8" stroke="{ORANGE}" stroke-width="4"/>
  <text x="768" y="675" text-anchor="middle" class="h">Lectura para el prototipo F1</text>
  <text x="768" y="724" text-anchor="middle" class="body">Si cada marca de pista queda más separada, el coche acelera.</text>
  <text x="768" y="768" text-anchor="middle" class="body">Si cada marca queda menos separada, el coche frena.</text>
"""
    return svg + footer(width, height)


def visual_07() -> str:
    width, height = 1536, 1024
    svg = header("Caída libre y tiro vertical", "La gravedad acelera en dirección vertical", width, height)
    svg += box(90, 180, 610, 360, "Caída libre", ["El objeto se suelta", "v0 = 0 si parte del reposo", "La rapidez aumenta hacia abajo", "La masa no cambia g"], "y = y0 + 1/2gt²", BLUE)
    svg += box(846, 180, 610, 360, "Tiro vertical", ["El objeto sube con v0", "La gravedad lo frena al subir", "En la altura máxima v = 0", "Luego baja acelerando"], "v = v0 - gt", CYAN)
    svg += f"""
  <line x1="760" y1="230" x2="760" y2="795" stroke="{LINE}" stroke-width="5"/>
  <circle cx="760" cy="300" r="18" fill="{ORANGE}"/>
  <circle cx="760" cy="410" r="22" fill="{ORANGE}"/>
  <circle cx="760" cy="560" r="26" fill="{ORANGE}"/>
  <circle cx="760" cy="745" r="30" fill="{ORANGE}"/>
  <text x="760" y="875" text-anchor="middle" class="formula">g = 9.8 m/s² hacia abajo</text>
"""
    return svg + footer(width, height)


def visual_08() -> str:
    width, height = 1536, 1024
    svg = header("Movimiento parabólico", "Dos movimientos al mismo tiempo: horizontal y vertical", width, height)
    svg += f"""
  <path d="M160 790 C410 390, 820 310, 1280 790" fill="none" stroke="{ORANGE}" stroke-width="10"/>
  <line x1="150" y1="790" x2="1320" y2="790" stroke="{LINE}" stroke-width="5"/>
  <line x1="160" y1="810" x2="160" y2="220" stroke="{LINE}" stroke-width="5"/>
  <text x="1290" y="850" class="small">x</text>
  <text x="105" y="240" class="small">y</text>
  <circle cx="160" cy="790" r="18" fill="{BLUE}"/>
  <circle cx="500" cy="490" r="18" fill="{BLUE}"/>
  <circle cx="860" cy="490" r="18" fill="{BLUE}"/>
  <circle cx="1280" cy="790" r="18" fill="{BLUE}"/>
"""
    svg += box(90, 150, 500, 210, "Eje horizontal", ["No hay aceleración horizontal", "La velocidad vx se conserva"], "x = vx · t", BLUE)
    svg += box(946, 150, 500, 210, "Eje vertical", ["La gravedad actúa hacia abajo", "La velocidad vy cambia"], "y = y0 + v0yt - 1/2gt²", GREEN)
    svg += f"""
  <rect x="390" y="870" width="756" height="70" rx="18" fill="#FFF8E8" stroke="{ORANGE}" stroke-width="3"/>
  <text x="768" y="916" text-anchor="middle" class="body">La parábola aparece al combinar x constante con y acelerado.</text>
"""
    return svg + footer(width, height)


def visual_09() -> str:
    width, height = 1536, 1024
    svg = header("Movimiento circular uniforme", "La rapidez puede ser constante, pero la dirección cambia", width, height)
    svg += f"""
  <circle cx="500" cy="520" r="245" fill="none" stroke="{BLUE}" stroke-width="10"/>
  <circle cx="500" cy="520" r="16" fill="{INK}"/>
  <circle cx="745" cy="520" r="32" fill="{ORANGE}"/>
  <line x1="745" y1="520" x2="500" y2="520" stroke="{GREEN}" stroke-width="8" marker-end="url(#none)"/>
  <line x1="745" y1="520" x2="745" y2="330" stroke="{CYAN}" stroke-width="8"/>
  <text x="606" y="492" class="body">r</text>
  <text x="760" y="350" class="body">v tangencial</text>
  <text x="570" y="565" class="body">ac hacia el centro</text>
"""
    svg += box(900, 210, 430, 230, "Idea clave", ["La rapidez puede no cambiar", "La dirección sí cambia", "Por eso existe aceleración"], "", BLUE)
    svg += box(900, 500, 430, 230, "Fórmulas", ["ac: aceleración centrípeta", "v: rapidez tangencial", "r: radio de giro"], "ac = v² / r", ORANGE)
    svg += f"""
  <text x="768" y="900" text-anchor="middle" class="formula">Girar exige fuerza y aceleración hacia el centro.</text>
"""
    return svg + footer(width, height)


def main() -> None:
    write("M2-u01-02.svg", visual_02())
    write("M2-u01-05.svg", visual_05())
    write("M2-u01-06.svg", visual_06())
    write("M2-u01-07.svg", visual_07())
    write("M2-u01-08.svg", visual_08())
    write("M2-u01-09.svg", visual_09())
    print("Visuales U1 legibles generados en", OUT)


if __name__ == "__main__":
    main()
