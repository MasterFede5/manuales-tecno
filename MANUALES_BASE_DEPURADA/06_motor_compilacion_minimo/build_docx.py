"""
Convierte los HTMLs construidos por build/converter.py a documentos Word (.docx)
usando pandoc (vía pypandoc).

Flujo recomendado para la entrega 40/60:
  1) python build_semestres_40_60.py      # MD -> HTML semestral 40/60
  2) python build_docx.py --variant 40-60 # HTML -> DOCX editable

Importante:
- Las imágenes que el converter ya inyectó en el HTML por ID (desde
  assets/visuales/) viajan al DOCX como imágenes embebidas reales.
- En la variante 40/60 los visuales finales deben ser JPG profesionales;
  no se esperan placeholders SVG en la entrega.
- Las cajas semánticas Albatros (::concepto::, ::albatros::, ::pausa::,
  etc.) se convirtieron a <aside>/<section> con clases CSS. Pandoc las
  preserva como bloques estilizados en Word (no cajas con borde, pero sí
  con encabezado distinguible).

Uso:
  python build_docx.py                      # los 10 (5 manuales x 2 sem)
  python build_docx.py --manual 1           # solo manual 1 (ambos sem)
  python build_docx.py --manual 1 --semester 1
  python build_docx.py --complete           # manuales completos (no por sem)
  python build_docx.py --variant 40-60      # variante semestral 40/60
  python build_docx.py --digital            # usar -digital.html
  python build_docx.py --open               # abrir el primer DOCX al terminar
"""
from __future__ import annotations
import argparse
import os
import re
import sys
import time
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"


def ensure_pandoc():
    import pypandoc
    try:
        return pypandoc.get_pandoc_version()
    except OSError:
        print("Descargando pandoc...", flush=True)
        pypandoc.download_pandoc()
        return pypandoc.get_pandoc_version()


def convert(html: Path, docx: Path, reference_docx: Path | None = None) -> None:
    import pypandoc
    if not html.exists():
        raise FileNotFoundError(html)
    docx.parent.mkdir(parents=True, exist_ok=True)
    extra_args = [
        # resource-path permite que pandoc resuelva las rutas relativas/file://
        # de las imágenes inyectadas por el converter Albatros.
        f"--resource-path={ROOT}",
        f"--resource-path={DIST}",
        f"--resource-path={ROOT / 'assets' / 'visuales'}",
        f"--resource-path={ROOT / 'assets' / 'iconos'}",
        "--embed-resources",          # embebe imágenes en el .docx
        "--standalone",
        "--from", "html",
        "--to", "docx",
    ]
    if reference_docx and reference_docx.exists():
        extra_args.extend(["--reference-doc", str(reference_docx)])
    print(f"  -> {docx.name}", flush=True)
    t0 = time.time()
    source_html = html
    tmp_name: str | None = None
    raw = html.read_text(encoding="utf-8", errors="replace")
    cleaned = re.sub(r'<link[^>]+https://cdn\.jsdelivr\.net/[^>]+>\s*', "", raw)
    cleaned = re.sub(r'<script\b[^>]*>.*?</script>\s*', "", cleaned, flags=re.S)
    cleaned = re.sub(r'<div class="print-page-(?:header|footer)">.*?</div>\s*', "", cleaned, flags=re.S)
    cleaned = re.sub(
        r"<h[1-6]\b[^>]*>",
        lambda m: re.sub(r"\s+id=(['\"]).*?\1", "", m.group(0)),
        cleaned,
    )
    if cleaned != raw:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
        with tmp:
            tmp.write(cleaned)
            tmp_name = tmp.name
        source_html = Path(tmp_name)
    try:
        pypandoc.convert_file(
            str(source_html),
            "docx",
            outputfile=str(docx),
            extra_args=extra_args,
        )
    except Exception as e:
        # pandoc a veces falla con file:// absolutas Windows; intentar plan B
        # convirtiendo a markdown intermedio y luego a docx no es ideal — mejor
        # reportar el error.
        raise RuntimeError(f"pandoc falló al convertir {html.name}: {e}") from e
    if tmp_name:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
    if not docx.exists():
        raise RuntimeError(f"pandoc no produjo {docx}")
    elapsed = time.time() - t0
    size_mb = docx.stat().st_size / (1024 * 1024)
    print(f"     OK  {size_mb:.1f} MB  ({elapsed:.1f}s)", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manual", type=int, choices=[1, 2, 3, 4, 5])
    ap.add_argument("--semester", type=int, choices=[1, 2])
    ap.add_argument("--complete", action="store_true",
                    help="convertir los manuales completos manual-N.html (sin split)")
    ap.add_argument("--digital", action="store_true",
                    help="usar variante -digital.html")
    ap.add_argument("--variant", default="",
                    help="sufijo de variante antes de -digital, por ejemplo: 40-60")
    ap.add_argument("--open", action="store_true")
    ap.add_argument("--reference", type=str, default=None,
                    help="plantilla .docx con estilos Albatros (reference-doc)")
    args = ap.parse_args()

    version = ensure_pandoc()
    print(f"pandoc {version}", flush=True)

    variant_suffix = f"-{args.variant.strip('-')}" if args.variant else ""
    suffix = f"{variant_suffix}{'-digital' if args.digital else ''}"
    manuales = [args.manual] if args.manual else [1, 2, 3, 4, 5]
    sems = [args.semester] if args.semester else [1, 2]
    reference = Path(args.reference) if args.reference else None

    targets: list[tuple[Path, Path, str]] = []
    if args.complete:
        for n in manuales:
            h = DIST / f"manual-{n}{suffix}.html"
            d = DIST / f"manual-{n}{suffix}.docx"
            targets.append((h, d, f"Manual {n}"))
    else:
        for n in manuales:
            for s in sems:
                h = DIST / f"manual-{n}-sem-{s}{suffix}.html"
                d = DIST / f"manual-{n}-sem-{s}{suffix}.docx"
                targets.append((h, d, f"Manual {n} - Semestre {s}"))

    ok_count = 0
    fail = []
    for h, d, label in targets:
        print(f"\n{label}", flush=True)
        if not h.exists():
            hint = "python build_semestres_40_60.py" if args.variant == "40-60" else "python build_semestres.py"
            print(f"  WARN: {h.name} no existe. Corre antes '{hint}'.", file=sys.stderr)
            fail.append(label)
            continue
        try:
            convert(h, d, reference)
            ok_count += 1
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            fail.append(label)

    print(f"\n=== {ok_count}/{len(targets)} convertidos ===")
    if fail:
        print("Fallos:", ", ".join(fail))
        sys.exit(1)

    if args.open and ok_count and targets:
        first = next((d for _, d, _ in targets if d.exists()), None)
        if first:
            os.startfile(str(first))  # noqa: S606


if __name__ == "__main__":
    main()
