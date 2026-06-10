const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const inputArg = process.argv[2];
const pagesArg = Number(process.argv[3] || 6);

if (!inputArg) {
  console.error('Uso: node auditar_render_html.js <manual.html> [paginas]');
  process.exit(1);
}

const htmlPath = path.resolve(inputArg);

if (!fs.existsSync(htmlPath)) {
  console.error(`No existe el HTML: ${htmlPath}`);
  process.exit(1);
}

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

  const report = await page.evaluate((pageLimit) => {
    const pageEls = [...document.querySelectorAll('.page')];
    const firstPages = pageEls.slice(0, pageLimit).map((pageEl, index) => {
      const rect = pageEl.getBoundingClientRect();
      const footer = pageEl.querySelector('.footer');
      const footerRect = footer?.getBoundingClientRect();
      const imgs = [...pageEl.querySelectorAll('img')].map((img) => {
        const r = img.getBoundingClientRect();
        return {
          src: img.getAttribute('src'),
          visualId: img.closest('[data-visual-id]')?.getAttribute('data-visual-id') || '',
          naturalWidth: img.naturalWidth,
          naturalHeight: img.naturalHeight,
          renderedWidth: Math.round(r.width),
          renderedHeight: Math.round(r.height),
          renderedArea: Math.round(r.width * r.height),
        };
      });
      const children = [...pageEl.children].map((child) => {
        const r = child.getBoundingClientRect();
        return {
          tag: child.tagName.toLowerCase(),
          cls: child.className || '',
          top: Math.round(r.top - rect.top),
          bottom: Math.round(r.bottom - rect.top),
          height: Math.round(r.height),
          text: (child.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 140),
        };
      });
      return {
        page: index + 1,
        title: pageEl.querySelector('h1,h2')?.textContent?.trim().replace(/\s+/g, ' ') || '',
        className: pageEl.className,
        textLength: (pageEl.innerText || '').length,
        footerTop: footerRect ? Math.round(footerRect.top - rect.top) : null,
        imgs,
        children,
      };
    });
    const images = [...document.images].map((img) => {
      const r = img.getBoundingClientRect();
      const pageEl = img.closest('.page');
      const pageIndex = pageEl ? [...document.querySelectorAll('.page')].indexOf(pageEl) + 1 : 0;
      const area = r.width * r.height;
      return {
        page: pageIndex,
        src: img.getAttribute('src'),
        visualId: img.closest('[data-visual-id]')?.getAttribute('data-visual-id') || '',
        naturalWidth: img.naturalWidth,
        naturalHeight: img.naturalHeight,
        renderedWidth: Math.round(r.width),
        renderedHeight: Math.round(r.height),
        renderedArea: Math.round(area),
        complete: img.complete && img.naturalWidth > 0,
      };
    });
    return {
      pages: pageEls.length,
      firstPages,
      brokenImages: images.filter((img) => !img.complete),
      tinyImages: images.filter((img) => img.complete && img.renderedArea < 90000),
      images,
    };
  }, pagesArg);

  console.log(JSON.stringify(report, null, 2));
  await browser.close();
})();
