const { chromium } = require('playwright');
(async () => {
  const [file, out, w, dark] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: +w || 1280, height: 900 }, colorScheme: dark ? 'dark' : 'light' });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + file); await p.waitForTimeout(800);
  const ow = await p.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
  await p.screenshot({ path: out, fullPage: true }); console.log('errors', errs, 'overflow', ow); await b.close();
})();
