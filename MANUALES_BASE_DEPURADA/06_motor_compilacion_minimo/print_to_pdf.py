"""
Genera PDFs imprimibles de los manuales Albatros directamente con
Chrome / Edge headless, sin pasar por la UI del navegador (que se cuelga
con HTMLs grandes y muchos page-break-inside: avoid).

Uso:
    python print_to_pdf.py                # los 5 manuales (versión impresa)
    python print_to_pdf.py --manual 1     # solo manual 1
    python print_to_pdf.py --digital      # variante -digital.html (web friendly)
    python print_to_pdf.py --manual 1 --open  # abre el PDF al terminar

Salida en dist/manual-N.pdf
"""
from __future__ import annotations
import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_browser() -> str:
    for c in CHROME_CANDIDATES:
        if Path(c).exists():
            return c
    # last resort, PATH lookup
    for name in ("chrome.exe", "msedge.exe", "chrome", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    raise RuntimeError("No se encontró Chrome ni Edge instalado.")


def file_url(p: Path) -> str:
    # ruta absoluta a URL file:/// respetando espacios y acentos
    abs_path = str(p.resolve()).replace("\\", "/")
    # quote para espacios/acentos
    from urllib.parse import quote
    return "file:///" + quote(abs_path, safe="/:")


def print_pdf(browser: str, html_path: Path, pdf_path: Path, timeout: int = 180) -> None:
    if not html_path.exists():
        raise FileNotFoundError(html_path)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    url = file_url(html_path)
    # tmp user-data-dir para no interferir con sesión real del usuario
    import tempfile
    user_data_dir = Path(tempfile.mkdtemp(prefix="albatros-print-"))
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-extensions",
        "--disable-features=Translate,BackForwardCache",
        "--hide-scrollbars",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=60000",  # ms para que cargue fuentes/imágenes
        f"--user-data-dir={user_data_dir}",
        f"--print-to-pdf={pdf_path}",
        url,
    ]
    print(f"  -> {pdf_path.name}", flush=True)
    t0 = time.time()
    try:
        res = subprocess.run(
            cmd,
            timeout=timeout,
            capture_output=True,
        )
    finally:
        shutil.rmtree(user_data_dir, ignore_errors=True)
    elapsed = time.time() - t0
    if res.returncode != 0 or not pdf_path.exists():
        err_txt = (res.stderr or b"").decode("utf-8", errors="replace")
        print("STDERR:", err_txt[-2000:], file=sys.stderr)
        raise RuntimeError(
            f"Chrome/Edge falló (exit={res.returncode}) tras {elapsed:.1f}s. "
            f"Ver stderr arriba."
        )
    size_mb = pdf_path.stat().st_size / (1024 * 1024)
    print(f"     OK  {size_mb:.1f} MB  ({elapsed:.1f}s)", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manual", type=int, choices=[1, 2, 3, 4, 5],
                    help="solo este manual (default: los 5)")
    ap.add_argument("--semester", type=int, choices=[1, 2],
                    help="solo este semestre (1 o 2) - usa manual-N-sem-X.html")
    ap.add_argument("--all-semesters", action="store_true",
                    help="generar PDFs de los 10 archivos manual-N-sem-X.html")
    ap.add_argument("--digital", action="store_true",
                    help="usar variante manual-N-digital.html (web friendly)")
    ap.add_argument("--variant", default="",
                    help="sufijo de variante antes de -digital, por ejemplo: 40-60")
    ap.add_argument("--open", action="store_true",
                    help="abrir el PDF al terminar (solo si se especifica --manual)")
    ap.add_argument("--timeout", type=int, default=240,
                    help="timeout por manual en segundos (default 240)")
    args = ap.parse_args()

    browser = find_browser()
    print(f"Navegador: {browser}", flush=True)

    variant_suffix = f"-{args.variant.strip('-')}" if args.variant else ""
    suffix = f"{variant_suffix}{'-digital' if args.digital else ''}"
    manuales = [args.manual] if args.manual else [1, 2, 3, 4, 5]

    # Construir lista de targets (html, pdf, label)
    targets: list[tuple[Path, Path, str]] = []
    if args.all_semesters or args.semester:
        sems = [args.semester] if args.semester else [1, 2]
        for n in manuales:
            for s in sems:
                html = DIST / f"manual-{n}-sem-{s}{suffix}.html"
                pdf = DIST / f"manual-{n}-sem-{s}{suffix}.pdf"
                targets.append((html, pdf, f"Manual {n} - Semestre {s}"))
    else:
        for n in manuales:
            html = DIST / f"manual-{n}{suffix}.html"
            pdf = DIST / f"manual-{n}{suffix}.pdf"
            targets.append((html, pdf, f"Manual {n}"))

    failures: list[str] = []
    for html, pdf, label in targets:
        print(f"\n{label} {'(digital)' if args.digital else '(impresión)'}", flush=True)
        try:
            print_pdf(browser, html, pdf, timeout=args.timeout)
        except Exception as e:
            print(f"  ERROR {label}: {e}", file=sys.stderr)
            failures.append(label)
            continue
        if args.open and len(targets) == 1:
            os.startfile(str(pdf))  # noqa: S606

    if failures:
        print("Fallos:", ", ".join(failures), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
