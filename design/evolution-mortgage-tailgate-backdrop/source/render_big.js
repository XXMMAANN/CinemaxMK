// usage: node render_big.js <svg file> <out.png> <width px> <height px>   (tiles fullPage screenshots, no size cap)
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [,, svgFile, out, W, H] = process.argv; const w = +W, h = +H;
  let svg = fs.readFileSync(svgFile, 'utf8').replace(/width="[^"]+" height="[^"]+"/, `width="${w}" height="${h}"`);
  const html = `<!doctype html><html><body style="margin:0;width:${w}px;height:${h}px;overflow:hidden">${svg}</body></html>`;
  const tmp = path.resolve(out + '.html'); fs.writeFileSync(tmp, html);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 4000, height: 3000 }, deviceScaleFactor: 1 });
  await p.goto('file://' + tmp); await p.waitForTimeout(500);
  const T = 6000; let n = 0;
  for (let y = 0; y < h; y += T) for (let x = 0; x < w; x += T) {
    const cw = Math.min(T, w - x), ch = Math.min(T, h - y);
    await p.screenshot({ path: `${out}.tile_${x}_${y}.png`, fullPage: true, clip: { x, y, width: cw, height: ch } }); n++;
  }
  await b.close(); fs.unlinkSync(tmp); console.log('tiles', n);
})();
