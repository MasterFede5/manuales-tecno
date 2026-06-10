#!/usr/bin/env python3
"""CLI del sistema de iconografía Albatros.

Subcomandos:
  list      lista todos los íconos (filtrable por categoría)
  find      busca por palabra clave en alias / concepto / id
  show      muestra ficha completa de un ícono
  pending   imprime los pendientes en formato Markdown (lista para diseñador)
  validate  comprueba que los archivos SVG/PNG existan en assets/iconos/
  mark      marca un ícono como producido (estado = listo)
  csv       exporta el registry como CSV
"""
from __future__ import annotations
import argparse
import csv
import json
import sys
from pathlib import Path

# Permite importar iconografia.py al estar en el mismo directorio
sys.path.insert(0, str(Path(__file__).parent))
from iconografia import load_registry, resolve, _REG_PATH

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def cmd_list(args):
    reg = load_registry()
    by_cat: dict = {}
    for k, v in reg["icons"].items():
        by_cat.setdefault(v["categoria"], []).append((k, v))
    for cat, items in sorted(by_cat.items()):
        if args.categoria and args.categoria != cat:
            continue
        print(f"\n[{cat}]  ({len(items)} íconos)")
        print("-" * 60)
        for k, v in sorted(items):
            mark = "✓" if v.get("estado") == "listo" else "·"
            print(f"  {mark}  {v['id']:<38}  {v['emoji']}  {v['concepto']}")


def cmd_find(args):
    reg = load_registry()
    q = args.query.lower()
    found = []
    for k, v in reg["icons"].items():
        if (q in k.lower()
            or q in v.get("concepto", "").lower()
            or q in v.get("id", "").lower()
            or any(q in a.lower() for a in v.get("alias", []))):
            found.append(v)
    if not found:
        print(f"⚠ Sin resultados para '{args.query}'")
        return 1
    print(f"# {len(found)} resultado(s) para '{args.query}'\n")
    for v in found:
        print(f"  {v['id']:<38}  {v['emoji']}  {v['concepto']}")
        print(f"    alias: {', '.join(v['alias'])}")


def cmd_show(args):
    icon = resolve(args.query)
    if not icon:
        print(f"⚠ No se resolvió '{args.query}'")
        return 1
    print(json.dumps(icon, indent=2, ensure_ascii=False))


def cmd_pending(args):
    reg = load_registry()
    by_cat: dict = {}
    for k, v in reg["icons"].items():
        if v.get("estado") != "listo":
            by_cat.setdefault(v["categoria"], []).append(v)
    total = sum(len(x) for x in by_cat.values())
    out_lines = [
        f"# Íconos pendientes — Albatros ({total})",
        "",
        f"_Generado desde {_REG_PATH}_",
        "",
        "Estilo: outline + duotone · 256×256 px · paleta `#0E3A8A` / `#F39C12` (`#1E8449` rama Tecno)",
        "",
    ]
    for cat in sorted(by_cat):
        items = sorted(by_cat[cat], key=lambda x: x["id"])
        out_lines.append(f"## {cat}  ({len(items)})\n")
        out_lines.append("| Estado | ID | Concepto visual | Alias |")
        out_lines.append("|---|---|---|---|")
        for v in items:
            alias = ", ".join(v["alias"][:3]) if v.get("alias") else "—"
            out_lines.append(
                f"| ☐ | `{v['id']}` | {v['emoji']} {v['concepto']} | {alias} |"
            )
        out_lines.append("")
    text = "\n".join(out_lines)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"✓ Lista escrita en {args.out}  ({total} íconos)")
    else:
        print(text)


def cmd_validate(args):
    reg = load_registry()
    base = _REG_PATH.parent  # assets/iconos/
    listos, faltan = [], []
    for k, v in reg["icons"].items():
        svg = base / v["svg"]
        if svg.exists():
            listos.append(v["id"])
        else:
            faltan.append(v["id"])
    print(f"Total registrados : {len(reg['icons'])}")
    print(f"Producidos        : {len(listos)}")
    print(f"Pendientes        : {len(faltan)}")
    if faltan and args.verbose:
        for f in faltan:
            print(f"  · {f}")


def cmd_mark(args):
    reg = load_registry()
    icon = resolve(args.query)
    if not icon:
        print(f"⚠ No se resolvió '{args.query}'")
        return 1
    # Encuentra clave real
    key = None
    for k, v in reg["icons"].items():
        if v["id"] == icon["id"]:
            key = k
            break
    if not key:
        return 1
    reg["icons"][key]["estado"] = "listo" if args.estado == "listo" else "pendiente"
    _REG_PATH.write_text(json.dumps(reg, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✓ {icon['id']} → estado: {reg['icons'][key]['estado']}")


def cmd_csv(args):
    reg = load_registry()
    rows = []
    for k, v in reg["icons"].items():
        rows.append({
            "id": v["id"],
            "categoria": v["categoria"],
            "alias": "|".join(v["alias"]),
            "emoji": v["emoji"],
            "concepto": v["concepto"],
            "svg": v["svg"],
            "estado": v["estado"],
        })
    out = args.out or "iconos.csv"
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"✓ CSV exportado: {out}  ({len(rows)} filas)")


def main():
    p = argparse.ArgumentParser(prog="iconos", description="Iconografía Albatros — CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("list", help="Listar todos los íconos")
    pl.add_argument("--categoria", help="Filtrar por categoría")
    pl.set_defaults(func=cmd_list)

    pf = sub.add_parser("find", help="Buscar por palabra")
    pf.add_argument("query")
    pf.set_defaults(func=cmd_find)

    ps = sub.add_parser("show", help="Ficha completa de un ícono")
    ps.add_argument("query")
    ps.set_defaults(func=cmd_show)

    pp = sub.add_parser("pending", help="Lista en Markdown de pendientes")
    pp.add_argument("--out", help="Archivo de salida (.md)")
    pp.set_defaults(func=cmd_pending)

    pv = sub.add_parser("validate", help="Comprobar archivos vs registro")
    pv.add_argument("--verbose", action="store_true")
    pv.set_defaults(func=cmd_validate)

    pm = sub.add_parser("mark", help="Marcar como listo o pendiente")
    pm.add_argument("query")
    pm.add_argument("estado", choices=["listo", "pendiente"])
    pm.set_defaults(func=cmd_mark)

    pc = sub.add_parser("csv", help="Exportar como CSV")
    pc.add_argument("--out", help="archivo CSV destino")
    pc.set_defaults(func=cmd_csv)

    args = p.parse_args()
    rc = args.func(args) or 0
    sys.exit(rc)


if __name__ == "__main__":
    main()
