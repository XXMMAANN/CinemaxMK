// usage: node render.js <input.html|svg> <out.png|-> <cssWidth> <cssHeight> [scale=1] [pdfOut] [pdfWidthIn] [pdfHeightIn]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [,, input, out, w, h, scale = '1', pdfOut, pdfW, pdfH] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +scale });
  await page.goto('file://' + path.resolve(input), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts ? document.fonts.ready : null);
  await page.waitForTimeout(400);
  if (out !== '-') await page.screenshot({ path: out, fullPage: false });
  if (pdfOut) await page.pdf({ path: pdfOut, width: pdfW + 'in', height: pdfH + 'in', printBackground: true, margin: {top:0,right:0,bottom:0,left:0} });
  await browser.close();
  console.log('rendered', out, pdfOut || '');
})().catch(e => { console.error(e); process.exit(1); });
