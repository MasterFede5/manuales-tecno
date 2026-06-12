const { chromium } = require("playwright");
const path = require("path");
const htmlPath = path.resolve(process.argv[2]);
const outDir = path.resolve(process.argv[3]);
const pagesToShot = process.argv[4].split(",").map(Number);
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1100, height: 1500 } });
  await page.goto("file:///" + htmlPath.replace(/\\/g, "/"), { waitUntil: "networkidle" });
  const sections = await page.$$("section.page");
  for (const n of pagesToShot) {
    const el = sections[n - 1];
    if (!el) continue;
    await el.scrollIntoViewIfNeeded();
    await el.screenshot({ path: path.join(outDir, "pagina-" + n + ".png") });
    console.log("capturada p." + n);
  }
  await browser.close();
})();