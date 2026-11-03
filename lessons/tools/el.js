const { chromium } = require('playwright');
(async () => { const [file, sel, out, w, dark] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: +w, height: 900 }, colorScheme: dark ? 'dark' : 'light' });
  await p.goto('file://' + file); await p.waitForTimeout(600); await p.locator(sel).first().screenshot({ path: out }); await b.close(); })();
