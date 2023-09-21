const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({headless : false});
  const page = await browser.newPage();

  await page.goto('https://indianexpress.com/');

  await page.waitForTimeout(5000); 

  // Extract <a> tags inside <h3> elements within the specified div
  const links = await page.$$eval('div.left-part h3 a', (aElements) => {
    return aElements.map((element) => element.href);
  });

  console.log(links);

  await browser.close();
})();
