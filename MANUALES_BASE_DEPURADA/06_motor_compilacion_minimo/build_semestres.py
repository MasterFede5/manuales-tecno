"""
Construye los HTMLs por semestre de los 5 manuales:
  dist/manual-N-sem-1.html  (semestre 1)
  dist/manual-N-sem-2.html  (semestre 2)

Es un wrapper simple sobre build/converter.py.
"""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CONVERTER = ROOT / "build" / "converter.py"


def main():
    only_manual = None
    if len(sys.argv) > 1:
        only_manual = int(sys.argv[1])

    targets = [only_manual] if only_manual else [1, 2, 3, 4, 5]
    for n in targets:
        src = ROOT / "manuales" / f"manual-{n}"
        for sem in (1, 2):
            out = ROOT / "dist" / f"manual-{n}-sem-{sem}.html"
            cmd = [sys.executable, str(CONVERTER), str(src), str(out), "--semester", str(sem)]
            print(f"\n--- Manual {n} · Semestre {sem} ---")
            res = subprocess.run(cmd, capture_output=False)
            if res.returncode != 0:
                print(f"FAILED manual {n} sem {sem}", file=sys.stderr)


if __name__ == "__main__":
    main()
