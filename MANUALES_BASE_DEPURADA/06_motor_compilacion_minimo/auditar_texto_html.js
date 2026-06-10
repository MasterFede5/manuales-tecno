const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const inputArg = process.argv[2];

if (!inputArg) {
  console.error('Uso: node auditar_texto_html.js <manual.html>');
  process.exit(1);
}

const htmlPath = path.resolve(inputArg);

if (!fs.existsSync(htmlPath)) {
  console.error(`No existe el HTML: ${htmlPath}`);
  process.exit(1);
}

const promptPatterns = [
  /\bprompt\b/i,
  /Midjourney/i,
  /DALL/i,
  /Stable Diffusion/i,
  /\bFlux\b/i,
  /super-espec/i,
];

const accentChecks = [
  ['Fisica', 'Física'],
  ['fisica', 'física'],
  ['Formula', 'Fórmula'],
  ['formula', 'fórmula'],
  ['Calculo', 'Cálculo'],
  ['calculo', 'cálculo'],
  ['Energia', 'Energía'],
  ['energia', 'energía'],
  ['Aceleracion', 'Aceleración'],
  ['aceleracion', 'aceleración'],
  ['Posicion', 'Posición'],
  ['posicion', 'posición'],
  ['Dinamica', 'Dinámica'],
  ['dinamica', 'dinámica'],
  ['Termodinamica', 'Termodinámica'],
  ['termodinamica', 'termodinámica'],
  ['Mecanica', 'Mecánica'],
  ['mecanica', 'mecánica'],
  ['Conclusion', 'Conclusión'],
  ['conclusion', 'conclusión'],
  ['Bibliografia', 'Bibliografía'],
  ['bibliografia', 'bibliografía'],
  ['Indice', 'Índice'],
  ['indice', 'índice'],
  ['Comprension', 'Comprensión'],
  ['comprension', 'comprensión'],
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 1700 } });
  await page.goto('file:///' + htmlPath.replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  const report = await page.evaluate(({ promptSources, accentPairs }) => {
    const text = document.body.innerText;
    const promptHits = promptSources
      .map((source) => new RegExp(source.source, source.flags))
      .filter((pattern) => pattern.test(text))
      .map((pattern) => pattern.toString());
    const accentHits = [];
    for (const [bad, good] of accentPairs) {
      const pattern = new RegExp(`\\b${bad}\\b`, 'g');
      const matches = text.match(pattern);
      if (matches) accentHits.push({ bad, good, count: matches.length });
    }
    return {
      pages: document.querySelectorAll('.page').length,
      images: document.images.length,
      links: document.querySelectorAll('a[href]').length,
      mojibake: /Ã|Â|�/.test(text),
      promptHits,
      accentHits,
      visibleChars: text.length,
    };
  }, {
    promptSources: promptPatterns.map((pattern) => ({ source: pattern.source, flags: pattern.flags })),
    accentPairs: accentChecks,
  });
  console.log(JSON.stringify(report, null, 2));
  await browser.close();
})();
