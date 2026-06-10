#!/usr/bin/env python3
"""Validador pre-build de manuales Albatros.

Aplica las reglas duras de manual-spec, manual-md-author y manual-iconografia.

Uso:
  python build/validate.py manuales/manual-1
  python build/validate.py manuales/                # valida los 5
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
import yaml

sys.path.insert(0, str(Path(__file__).parent))
import iconografia as ico

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# Catálogos de tipos válidos
ALBATROS_TIPOS = {
    "experimento", "debate", "taller", "caso", "reto",
    "simulacion", "investigacion-corta",
}
TECNO_TIPOS = {
    "maker", "circuito", "codigo", "dato", "iot", "prototipo",
}
VISUAL_TIPOS = {
    "infografia", "mapa-mental", "cuadro-comparativo", "linea-tiempo",
    "diagrama-flujo", "ilustracion", "interfaz", "tabla-grande", "grafica",
}

# Archivos mínimos por unidad (manual-spec §11.5)
ARCHIVOS_MIN_UNIDAD = {
    "README.md", "00-portadilla.md", "01-mapa-mental.md",
    "02-caso-episodio.md", "80-practica-resuelta.md",
    "90-actividades.md", "92-investigacion.md", "94-fuentes.md",
    "95-implementacion.md", "99-cierre.md",
}

ATTR_RE = re.compile(r'(\w+)\s*=\s*(?:"([^"]*)"|(\S+))')
BLOCK_OPEN_RE = re.compile(r"^::(?P<tag>[\w-]+)(\{[^}]*\})?(?:::)?\s*$",
                            re.MULTILINE)
BLOCK_CLOSE_RE = re.compile(r"^::/(?P<tag>[\w-]+)(?:::)?\s*$", re.MULTILINE)
INLINE_ICO_RE = re.compile(r"\{\{ico:([\w/-]+)\}\}")


def parse_attrs(s: str) -> dict:
    if not s:
        return {}
    s = s.strip("{}")
    return {m.group(1): (m.group(2) or m.group(3)) for m in ATTR_RE.finditer(s)}


def parse_frontmatter(text: str):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            try:
                fm = yaml.safe_load(text[3:end].strip()) or {}
            except Exception:
                fm = {}
            return fm, text[end + 4:].lstrip()
    return None, text


def validate_md(path: Path) -> list[str]:
    errs: list[str] = []
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    rel = str(path).replace("\\", "/").rsplit("manuales/", 1)[-1]

    if fm is None:
        # README.md y archivos sin frontmatter explícito son docs, no contenido
        if path.name == "README.md":
            return errs
        errs.append(f"{rel}: falta frontmatter YAML")
        body = text

    # Apertura/cierre balanceado (excluyendo ::visual:: que es self-closing)
    SELF_CLOSING = {"visual"}
    opens = [
        m.group("tag") for m in BLOCK_OPEN_RE.finditer(body)
        if m.group("tag") not in SELF_CLOSING
    ]
    closes = [m.group("tag") for m in BLOCK_CLOSE_RE.finditer(body)]
    for t in set(opens) | set(closes):
        if opens.count(t) != closes.count(t):
            errs.append(
                f"{rel}: apertura/cierre desbalanceado de ::{t}:: "
                f"({opens.count(t)} aperturas, {closes.count(t)} cierres)"
            )
            break

    # ::visual::
    for m in re.finditer(r"::visual(\{[^}]*\})", body):
        attrs = parse_attrs(m.group(1))
        tipo = attrs.get("tipo")
        desc = attrs.get("descripcion", "")
        if not tipo:
            errs.append(f"{rel}: ::visual:: sin atributo `tipo`")
        elif tipo not in VISUAL_TIPOS:
            errs.append(f"{rel}: ::visual:: tipo='{tipo}' no está en el catálogo")
        if not desc:
            errs.append(f"{rel}: ::visual:: sin `descripcion`")
        elif len(desc) < 50:
            errs.append(
                f"{rel}: ::visual:: `descripcion` con {len(desc)} chars (< 50): "
                f"'{desc[:40]}…'"
            )
        if "paginas" not in attrs:
            errs.append(f"{rel}: ::visual:: sin atributo `paginas`")

    # ::albatros::
    for m in re.finditer(r"::albatros(\{[^}]*\})", body):
        attrs = parse_attrs(m.group(1))
        tipo = attrs.get("tipo")
        if not tipo:
            errs.append(f"{rel}: ::albatros:: sin atributo `tipo`")
        elif tipo not in ALBATROS_TIPOS:
            errs.append(
                f"{rel}: ::albatros:: tipo='{tipo}' no está en {sorted(ALBATROS_TIPOS)}"
            )
        if not attrs.get("titulo"):
            errs.append(f"{rel}: ::albatros:: sin `titulo`")

    # ::tecno::
    for m in re.finditer(r"::tecno(\{[^}]*\})", body):
        attrs = parse_attrs(m.group(1))
        tipo = attrs.get("tipo")
        if not tipo:
            errs.append(f"{rel}: ::tecno:: sin atributo `tipo`")
        elif tipo not in TECNO_TIPOS:
            errs.append(
                f"{rel}: ::tecno:: tipo='{tipo}' no está en {sorted(TECNO_TIPOS)}"
            )
        if not attrs.get("titulo"):
            errs.append(f"{rel}: ::tecno:: sin `titulo`")

    # {{ico:NAME}} — todos deben resolver
    for m in INLINE_ICO_RE.finditer(body):
        name = m.group(1)
        if not ico.resolve(name):
            errs.append(f"{rel}: {{{{ico:{name}}}}} no se resuelve en el registry")

    return errs


def validate_manual(manual_dir: Path) -> list[str]:
    errs: list[str] = []
    name = manual_dir.name

    manifest = manual_dir / "manifest.md"
    if not manifest.exists():
        errs.append(f"{name}: falta manifest.md")
        return errs

    fm, _ = parse_frontmatter(manifest.read_text(encoding="utf-8"))
    if not fm:
        errs.append(f"{name}/manifest.md: falta frontmatter")
        return errs

    n_units = fm.get("unidades", 0)

    unidades_dir = manual_dir / "unidades"
    if not unidades_dir.exists():
        errs.append(f"{name}: falta carpeta unidades/")
        return errs

    existing = sorted(
        d.name for d in unidades_dir.iterdir()
        if d.is_dir() and re.match(r"^u\d{2}$", d.name)
    )
    if len(existing) != n_units:
        errs.append(
            f"{name}: manifest declara {n_units} unidades, "
            f"hay {len(existing)} carpetas uNN/ ({', '.join(existing) or '∅'})"
        )

    # Cada unidad tiene archivos mínimos
    for udir in unidades_dir.iterdir():
        if not udir.is_dir():
            continue
        archivos = {f.name for f in udir.iterdir() if f.is_file()}
        faltan = ARCHIVOS_MIN_UNIDAD - archivos
        if faltan:
            errs.append(
                f"{name}/unidades/{udir.name}: faltan {sorted(faltan)}"
            )

    # Validar todos los .md
    for md_file in unidades_dir.rglob("*.md"):
        errs.extend(validate_md(md_file))
    for md_file in manual_dir.glob("*.md"):
        errs.extend(validate_md(md_file))

    return errs


def main():
    p = argparse.ArgumentParser(description="Validador de manuales Albatros")
    p.add_argument("path", help="manuales/manual-N o manuales/")
    p.add_argument("--quiet", action="store_true", help="No imprimir resumen si OK")
    args = p.parse_args()

    base = Path(args.path)
    all_errs: list[str] = []
    targets: list[Path] = []
    if (base / "manifest.md").exists():
        targets = [base]
    else:
        targets = sorted(d for d in base.glob("manual-*") if d.is_dir())

    if not targets:
        print(f"⚠ No se encontraron manuales en {base}")
        return 1

    for t in targets:
        errs = validate_manual(t)
        all_errs.extend(errs)

    if not all_errs:
        if not args.quiet:
            print(f"✓ Validación OK · {len(targets)} manual(es) · cero errores")
        return 0

    print(f"✗ {len(all_errs)} error(es) en {len(targets)} manual(es):\n")
    for e in all_errs[:80]:
        print(f"  · {e}")
    if len(all_errs) > 80:
        print(f"  … y {len(all_errs) - 80} más")
    return 1


if __name__ == "__main__":
    sys.exit(main())
