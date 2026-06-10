from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path("MANUALES_BASE_DEPURADA/05_assets_visuales_iconos/visuales")
OUT = Path("MANUALES_BASE_DEPURADA/07_docs_pedagogicos/u01_contact_sheet_5_manuales.jpg")


def main() -> None:
    manuals = [f"manual-{i}" for i in range(1, 6)]
    thumb_w, thumb_h = 180, 120
    label_h = 28
    cols = 10
    manual_images = []
    rows = 0

    for manual in manuals:
        files = sorted((ROOT / manual / "u01").glob("*.jpg"))
        manual_images.append((manual, files))
        rows += (len(files) + cols - 1) // cols + 1

    sheet_w = cols * thumb_w
    sheet_h = rows * (thumb_h + label_h) + 20
    sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(sheet)
    y = 10

    for manual, files in manual_images:
        draw.rectangle([0, y, sheet_w, y + 24], fill=(14, 58, 138))
        draw.text((8, y + 5), f"{manual} / u01 / {len(files)} imagenes", fill="white")
        y += 30

        for idx, img_path in enumerate(files):
            x = (idx % cols) * thumb_w
            row = idx // cols
            yy = y + row * (thumb_h + label_h)

            try:
                img = Image.open(img_path).convert("RGB")
                img.thumbnail((thumb_w - 8, thumb_h - 8), Image.LANCZOS)
                px = x + (thumb_w - img.width) // 2
                py = yy + 4 + (thumb_h - 8 - img.height) // 2
                sheet.paste(img, (px, py))
            except Exception:
                draw.text((x + 4, yy + 20), "ERROR", fill="red")

            draw.rectangle([x, yy, x + thumb_w - 1, yy + thumb_h + label_h - 1], outline=(170, 180, 195))
            draw.text((x + 4, yy + thumb_h + 4), img_path.stem, fill=(23, 32, 51))

        y += ((len(files) + cols - 1) // cols) * (thumb_h + label_h) + 8

    OUT.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(OUT, quality=92)
    print(OUT)


if __name__ == "__main__":
    main()
