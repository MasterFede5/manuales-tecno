const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const inputArg = process.argv[2];

if (!inputArg) {
  console.error('Uso: node auditar_overflow_html.js <manual.html>');
  process.exit(1);
}

const htmlPath = path.resolve(inputArg);

if (!fs.existsSync(htmlPath)) {
  console.error(`No existe el HTML: ${htmlPath}`);
  process.exit(1);
}

const targets = [
  '.development-card',
  '.exercise-development',
  '.classification-task',
  '.mini-table',
  '.bank-item',
  '.concept',
  '.formula-card',
  '.question',
  '.note',
  '.appendix-card',
  '.route-card',
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 1700 } });
  await page.goto('file:///' + htmlPath.replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(async () => {
    if (document.fonts?.ready) await document.fonts.ready;
    await Promise.all([...document.images].map((img) => {
      if (img.complete) return Promise.resolve();
      return new Promise((resolve) => {
        img.addEventListener('load', resolve, { once: true });
        img.addEventListener('error', resolve, { once: true });
      });
    }));
  });

  const report = await page.evaluate((selectors) => {
    const pages = [...document.querySelectorAll('.page')];
    const issues = [];
    pages.forEach((pageEl, index) => {
      const pageRect = pageEl.getBoundingClientRect();
      const footer = pageEl.querySelector('.footer');
      const footerTop = footer ? footer.getBoundingClientRect().top : pageRect.bottom - 30;
      const safeBottom = footerTop - 8;
      const pageBottom = pageRect.bottom - 2;
      const pageTitle = pageEl.querySelector('h1,h2')?.textContent?.trim() || '(sin titulo)';
      const scrollOverflow = pageEl.scrollHeight - pageEl.clientHeight;
      if (scrollOverflow > 2) {
        issues.push({
          page: index + 1,
          title: pageTitle,
          type: 'page-overflow',
          detail: `scrollHeight excede ${Math.round(scrollOverflow)} px`,
        });
      }
      selectors.forEach((selector) => {
        pageEl.querySelectorAll(selector).forEach((el) => {
          const rect = el.getBoundingClientRect();
          if (rect.height < 1) return;
          if (rect.bottom > pageBottom || rect.bottom > safeBottom) {
            const label = el.querySelector('h3,strong')?.textContent?.trim() || el.textContent.trim().slice(0, 80);
            issues.push({
              page: index + 1,
              title: pageTitle,
              type: selector,
              bottom: Math.round(rect.bottom - pageRect.top),
              safeBottom: Math.round(safeBottom - pageRect.top),
              detail: label,
            });
          }
        });
      });
    });
    const images = [...document.images];
    return {
      file: location.pathname,
      pages: pages.length,
      images: images.length,
      brokenImages: images.filter((img) => !img.complete || img.naturalWidth === 0).length,
      landscapePages: pages.filter((page) => page.classList.contains('landscape')).length,
      issues,
    };
  }, targets);

  console.log(JSON.stringify(report, null, 2));
  await browser.close();
})();
