const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const [inputArg, outputArg] = process.argv.slice(2);

if (!inputArg || !outputArg) {
  console.error('Uso: node export_html_to_pdf.js <entrada.html> <salida.pdf>');
  process.exit(1);
}

const inputPath = path.resolve(inputArg);
const outputPath = path.resolve(outputArg);

if (!fs.existsSync(inputPath)) {
  console.error(`No existe el HTML de entrada: ${inputPath}`);
  process.exit(1);
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1600 } });
  await page.goto('file:///' + inputPath.replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(async () => {
    const images = [...document.images];
    await Promise.all(images.map((img) => {
      if (img.complete) return Promise.resolve();
      return new Promise((resolve) => {
        img.addEventListener('load', resolve, { once: true });
        img.addEventListener('error', resolve, { once: true });
      });
    }));
    if (document.fonts?.ready) await document.fonts.ready;
  });

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  await page.pdf({
    path: outputPath,
    printBackground: true,
    preferCSSPageSize: true,
  });

  const sizeMb = fs.statSync(outputPath).size / (1024 * 1024);
  console.log(JSON.stringify({
    input: inputPath,
    output: outputPath,
    sizeMb: Number(sizeMb.toFixed(2)),
  }, null, 2));

  await browser.close();
})();
