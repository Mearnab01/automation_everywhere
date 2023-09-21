const puppeteer = require('puppeteer');

const parallel = 4;

const scientists = [
  { name: 'C. V. Raman', url: 'https://en.wikipedia.org/wiki/C._V._Raman' },
  { name: 'A. P. J. Abdul Kalam', url: 'https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam' },
  // Add more scientist entries as needed
];

const takeScreenshots = async () => {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
  
    for (const scientist of scientists) {
      await page.setViewport({ width: 1280, height: 800 });
  
      try {
        await page.goto(scientist.url);
        await page.screenshot({ path: `${scientist.name}.png` });
        console.log(`Took a screenshot of ${scientist.name}`);
      } catch (error) {
        console.error(`Failed to take a screenshot of ${scientist.name}: ${error.message}`);
      }
    }
  
    await browser.close();
  };
  
  takeScreenshots();