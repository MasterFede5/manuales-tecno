const { chromium } = require('playwright');
const path = require('path');

const root = path.resolve(__dirname, '..');
const htmlPath = path.join(
  root,
  '01_fuente_principal_markdown',
  'manuales',
  'manual-1',
  'semestre-1',
  'manual-1-quimica-semestre-1-reintento.html'
);

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
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1000, height: 1300 } });
  await page.goto('file:///' + htmlPath.replace(/\\/g, '/'));
  await page.emulateMedia({ media: 'print' });
  const report = await page.evaluate((selectors) => {
    const pages = [...document.querySelectorAll('.page')];
    const issues = [];
    pages.forEach((pageEl, index) => {
      const pageRect = pageEl.getBoundingClientRect();
      const footer = pageEl.querySelector('.footer');
      const footerTop = footer ? footer.getBoundingClientRect().top : pageRect.bottom - 34;
      const safeBottom = footerTop - 8;
      const pageBottom = pageRect.bottom - 2;
      const pageTitle = pageEl.querySelector('h2')?.textContent?.trim() || '(sin titulo)';
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
    return {
      pages: pages.length,
      issues,
    };
  }, targets);
  console.log(JSON.stringify(report, null, 2));
  await browser.close();
})();
