#!/usr/bin/env python3
"""Andamiaje (scaffold) de carpetas y stubs por unidad.

Lee el manifest.md de cada manual y crea:
  manuales/manual-N/unidades/uNN/
con los archivos mínimos exigidos por manual-spec §11.5 y un stub por subtema.

Uso:
  python build/scaffold.py manuales/manual-1
  python build/scaffold.py manuales/                # los 5
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
import yaml

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


UNIT_HEADER_RE = re.compile(
    r"^##\s*U(\d+)\s*[—\-]\s*([^(]+?)\s*\((\d+)\s*pp\)",
    re.MULTILINE,
)
SUBTEMA_RE = re.compile(
    r"\|\s*(\d+\.\d+(?:\.\d+)?)\s+([^|]+?)\s*\|\s*(\d+)\s*\|"
)


def parse_frontmatter(text: str):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            try:
                fm = yaml.safe_load(text[3:end].strip()) or {}
            except Exception:
                fm = {}
            return fm, text[end + 4:].lstrip()
    return {}, text


def parse_manifest(path: Path):
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    headers = list(UNIT_HEADER_RE.finditer(body))
    units = []
    for i, m in enumerate(headers):
        u_num = int(m.group(1))
        title = m.group(2).strip()
        pp = int(m.group(3))
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(body)
        section = body[start:end]
        # Extrae subtemas con número decimal
        subtemas = []
        for sm in SUBTEMA_RE.finditer(section):
            num = sm.group(1)
            t = sm.group(2).strip()
            spp = int(sm.group(3))
            subtemas.append((num, t, spp))
        # Episodio
        ep_match = re.search(r"\*\*Caso E\d+:\*\*\s*([^\n]+)", section)
        episodio = ep_match.group(1).strip() if ep_match else ""
        units.append({
            "num": u_num, "title": title, "pp": pp,
            "subtemas": subtemas, "episodio": episodio,
        })
    return fm, units


def fm_yaml(d: dict) -> str:
    """Serializa frontmatter YAML estable y legible."""
    return yaml.safe_dump(d, allow_unicode=True, sort_keys=False).rstrip()


def stub_readme(meta: dict, unit: dict) -> str:
    case = meta.get("case_study", {})
    rows = "\n".join(
        f"| {s[0]} | {s[1]} | {s[2]} |" for s in unit["subtemas"]
    ) or "| — | (subtemas integrativos) | — |"
    return f"""# Unidad {unit['num']:02d} — {unit['title']}

**Páginas objetivo:** {unit['pp']}
**Manual:** {meta.get('titulo', '')}
**Case study:** {case.get('nombre', '')}
**Episodio en esta unidad:** {unit['episodio']}

## Subtemas

| ID | Título | pp |
|---|---|---:|
{rows}

## Archivos esperados

- `00-portadilla.md` — portadilla con título e ilustración
- `01-mapa-mental.md` — mapa mental de la unidad
- `02-caso-episodio.md` — episodio del case study
- `10-tema-X-Y.md` — un archivo por subtema
- `80-practica-resuelta.md` — práctica resuelta paso a paso
- `90-actividades.md` — actividades del catálogo (mín. 3 tipos)
- `92-investigacion.md` — apartado de investigación independiente
- `94-fuentes.md` — fuentes recomendadas (mín. 5)
- `95-implementacion.md` — proyecto integrador
- `99-cierre.md` — cierre y autoevaluación

## Recordatorios (manual-spec §4)

- Cada subtema lleva: ::concepto:: + ::interioriza:: + desarrollo + ::pausa::
- Mínimo 1 ::albatros:: y 1 ::investiga:: por unidad
- Visuales con `descripcion` ≥ 50 caracteres
- No emojis a mano. Usar íconos auto-inyectados o la sintaxis inline `ico:NAME`.
"""


def stub_subtema(unit: dict, st_num: str, st_title: str, st_pp: int) -> str:
    fm = fm_yaml({
        "unidad": unit["num"],
        "subtema": st_num,
        "titulo": st_title,
        "paginas_objetivo": st_pp,
        "competencias": [st_num],
        "visuals": [{
            "tipo": "ilustracion",
            "descripcion": f"Ilustración explicativa del subtema {st_num} {st_title}, mostrando los conceptos clave con etiquetas y ejemplo concreto.",
            "paginas": 0.5,
        }],
        "caso": unit.get("episodio", ""),
    })
    return f"""---
{fm}
---

# {st_num} {st_title}

[STUB — completar] Pregunta detonadora que arranca este subtema.

::concepto{{titulo="{st_title}"}}
**{st_title}** se define como… [completar definición formal]
::/concepto

::interioriza{{titulo="¿Por qué te importa?"}}
[Analogía o ejemplo cotidiano que conecte con la vida del estudiante.]
::/interioriza

[Desarrollo teórico — {max(st_pp - 1, 1)} a {st_pp} páginas]

[Texto principal del subtema. Cada concepto técnico nuevo: definir + dar ejemplo. Máx. 1 término nuevo por párrafo.]

::pausa{{titulo="💭 Pausa para pensar"}}
1. [Pregunta 1]
   ____________________________________________________________
2. [Pregunta 2]
   ____________________________________________________________
3. [Pregunta 3]
   ____________________________________________________________
::/pausa

::visual{{tipo="ilustracion" descripcion="Ilustración explicativa del subtema {st_num} {st_title}, con elementos etiquetados y un ejemplo aplicado al contexto del case study." paginas=0.5}}

[Frase puente al siguiente subtema.]
"""


def stub_portadilla(unit: dict, meta: dict) -> str:
    fm = fm_yaml({
        "unidad": unit["num"],
        "seccion": "portadilla",
        "paginas_objetivo": 1,
    })
    return f"""---
{fm}
---

# Unidad {unit['num']:02d}

## {unit['title']}

> [Frase detonadora de la unidad — completar]

::visual{{tipo="ilustracion" descripcion="Ilustración hero de portadilla para la Unidad {unit['num']} ({unit['title']}). Debe transmitir el tema central de manera atractiva e invitar al estudio." paginas=1}}
"""


def stub_mapa_mental(unit: dict) -> str:
    fm = fm_yaml({"unidad": unit["num"], "seccion": "mapa-mental", "paginas_objetivo": 1})
    bullets = "\n".join(f"- {s[0]} {s[1]}" for s in unit["subtemas"])
    return f"""---
{fm}
---

## Mapa mental — Unidad {unit['num']:02d}

::visual{{tipo="mapa-mental" descripcion="Mapa mental de la Unidad {unit['num']} con nodo central '{unit['title']}' y ramas para cada subtema, con jerarquía visual clara y palabras clave." paginas=1}}

### Nodos esperados
{bullets}
"""


def stub_caso_episodio(unit: dict, meta: dict) -> str:
    fm = fm_yaml({"unidad": unit["num"], "seccion": "caso-episodio", "paginas_objetivo": 1})
    case = meta.get("case_study", {})
    return f"""---
{fm}
---

::caso{{episodio={unit['num']}}}
**Caso Albatros — Episodio {unit['num']}: {unit['episodio']}**

[Recapitula brevemente lo del episodio anterior y plantea el nuevo reto del case study "{case.get('nombre', '')}" para esta unidad. 1–2 párrafos.]

[Cierra con una pregunta gancho que vincule con el primer subtema.]
::/caso
"""


def stub_practica(unit: dict) -> str:
    fm = fm_yaml({"unidad": unit["num"], "seccion": "practica-resuelta", "paginas_objetivo": 1})
    return f"""---
{fm}
---

## Práctica resuelta — Unidad {unit['num']:02d}

::practica{{titulo="[Título de la práctica]"}}
**Problema.** [Enunciado claro y aplicado al case study]

**Paso 1 — Datos.** …
**Paso 2 — Estrategia.** …
**Paso 3 — Cálculo / razonamiento.** …
**Paso 4 — Respuesta.** …
**Paso 5 — Verificación.** …
::/practica
"""


def stub_actividades(unit: dict) -> str:
    fm = fm_yaml({"unidad": unit["num"], "seccion": "actividades", "paginas_objetivo": 4})
    return f"""---
{fm}
---

## Actividades — Unidad {unit['num']:02d}

[Mínimo 3 tipos del catálogo. Plantillas listas para personalizar:]

::act-mcq{{titulo="Repaso conceptual"}}
1. [Pregunta]
   - [ ] opción A
   - [ ] opción B
   - [x] opción C (correcta)
   - [ ] opción D
::/act-mcq

::act-table{{titulo="Completa la tabla"}}
| Columna 1 | Columna 2 | Columna 3 |
|---|---|---|
|  |  |  |
|  |  |  |
::/act-table

::act-match{{titulo="Relaciona columnas"}}
| A | B |
|---|---|
| 1. … | a) … |
| 2. … | b) … |
::/act-match

::albatros{{titulo="[Título de la actividad Albatros]" tipo="experimento" tiempo="45 min"}}
**Pregunta detonadora.** …
**Lo que harás.** [pasos]
**Materiales.** …
**Entregable.** …
::/albatros
"""


def stub_investigacion(unit: dict) -> str:
    fm = fm_yaml({"unidad": unit["num"], "seccion": "investigacion", "paginas_objetivo": 1})
    return f"""---
{fm}
---

::investiga{{titulo="[Pregunta de investigación]" tiempo="2 h"}}
**Pregunta de investigación.** …

**Lo que debes encontrar.**
- …
- …

**Cómo presentarlo.** …

**Criterios de evaluación.** …
::/investiga
"""


def stub_fuentes(unit: dict, meta: dict) -> str:
    fm = fm_yaml({"unidad": unit["num"], "seccion": "fuentes", "paginas_objetivo": 1})
    return f"""---
{fm}
---

::fuentes{{titulo="Fuentes recomendadas — Unidad {unit['num']:02d}"}}
- 📘 **Libro** · …
- 🌐 **Web** · …
- 🎓 **OCW** · …
- 📺 **Video** · …
- 📰 **Artículo** · …
- 🇲🇽 **México** · …
::/fuentes
"""


def stub_implementacion(unit: dict) -> str:
    fm = fm_yaml({"unidad": unit["num"], "seccion": "implementacion", "paginas_objetivo": 3})
    return f"""---
{fm}
---

::implementacion{{titulo="Implementación Albatros — Unidad {unit['num']:02d}"}}
**Objetivo.** …

**Materiales / recursos.** …

**Pasos.**
1. …
2. …
3. …

**Entregable.** …

**Rúbrica.**
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
|  |  |  |  |
::/implementacion
"""


def stub_cierre(unit: dict) -> str:
    fm = fm_yaml({"unidad": unit["num"], "seccion": "cierre", "paginas_objetivo": 1})
    return f"""---
{fm}
---

## Cierre y autoevaluación — Unidad {unit['num']:02d}

[Síntesis breve de lo aprendido + conexión con la siguiente unidad]

### Autoevaluación (rúbrica de 5 niveles)

| Criterio | 1 — Inicial | 2 | 3 — Suficiente | 4 | 5 — Excelente |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
"""


def write_if_absent(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True


def scaffold_unit(manual_dir: Path, meta: dict, unit: dict) -> int:
    folder = manual_dir / "unidades" / f"u{unit['num']:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    created = 0

    placeholders = [
        ("README.md",                  stub_readme(meta, unit)),
        ("00-portadilla.md",           stub_portadilla(unit, meta)),
        ("01-mapa-mental.md",          stub_mapa_mental(unit)),
        ("02-caso-episodio.md",        stub_caso_episodio(unit, meta)),
        ("80-practica-resuelta.md",    stub_practica(unit)),
        ("90-actividades.md",          stub_actividades(unit)),
        ("92-investigacion.md",        stub_investigacion(unit)),
        ("94-fuentes.md",              stub_fuentes(unit, meta)),
        ("95-implementacion.md",       stub_implementacion(unit)),
        ("99-cierre.md",               stub_cierre(unit)),
    ]
    for name, content in placeholders:
        if write_if_absent(folder / name, content):
            created += 1

    for st_num, st_title, st_pp in unit["subtemas"]:
        st_id = st_num.replace(".", "-")
        if write_if_absent(folder / f"10-tema-{st_id}.md",
                           stub_subtema(unit, st_num, st_title, st_pp)):
            created += 1
    return created


def scaffold_manual(manual_dir: Path) -> tuple[int, int]:
    if not (manual_dir / "manifest.md").exists():
        print(f"⚠ Sin manifest.md en {manual_dir.name}")
        return 0, 0
    fm, units = parse_manifest(manual_dir / "manifest.md")
    n_units = fm.get("unidades", len(units))
    if not units:
        print(f"⚠ No se detectaron unidades en {manual_dir.name}/manifest.md")
        return 0, 0
    if len(units) != n_units:
        print(f"⚠ {manual_dir.name}: manifest declara {n_units} unidades, "
              f"se encontraron {len(units)} encabezados ## UN —")

    total_created = 0
    print(f"\n[{manual_dir.name}]  {fm.get('titulo', '')}")
    for u in units:
        n = scaffold_unit(manual_dir, fm, u)
        total_created += n
        marca = "+" if n > 0 else "·"
        print(f"  {marca} u{u['num']:02d}/  ({len(u['subtemas'])} subtemas, +{n} archivos)")
    return len(units), total_created


def main():
    p = argparse.ArgumentParser(description="Scaffold de manuales Albatros")
    p.add_argument("path", help="manuales/manual-N o manuales/")
    args = p.parse_args()

    base = Path(args.path)
    if (base / "manifest.md").exists():
        targets = [base]
    else:
        targets = sorted(d for d in base.glob("manual-*") if d.is_dir())

    if not targets:
        print(f"⚠ No se encontraron manuales en {base}")
        return 1

    grand_total = 0
    for t in targets:
        n_units, created = scaffold_manual(t)
        grand_total += created

    print(f"\n✓ Andamiaje completado · {grand_total} archivos creados en {len(targets)} manual(es)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
