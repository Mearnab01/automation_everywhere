const puppeteer = require('puppeteer');

const parallel = 4;

const scientists = [
  { name: 'C. V. Raman', url: 'https://en.wikipedia.org/wiki/C._V._Raman' },
  { name: 'A. P. J. Abdul Kalam', url: 'https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam' },
  { name: 'Srinivasa Ramanujan', url: 'https://en.wikipedia.org/wiki/Srinivasa_Ramanujan' },
  { name: 'Homi J. Bhabha', url: 'https://en.wikipedia.org/wiki/Homi_J._Bhabha' },
  { name: 'Satyendra Nath Bose', url: 'https://en.wikipedia.org/wiki/Satyendra_Nath_Bose' },
  { name: 'Vikram Sarabhai', url: 'https://en.wikipedia.org/wiki/Vikram_Sarabhai' },
  { name: 'Aryabhata', url: 'https://en.wikipedia.org/wiki/Aryabhata' },
  { name: 'Chandrasekhar Venkat Raman', url: 'https://en.wikipedia.org/wiki/Chandrasekhar_Venkat_Raman' },
  { name: 'Jagadish Chandra Bose', url: 'https://en.wikipedia.org/wiki/Jagadish_Chandra_Bose' },
  { name: 'Hargobind Khorana', url: 'https://en.wikipedia.org/wiki/Har_Gobind_Khorana' },
];

const screenshotScientists = async (scientists, parallel) => {
  const parallelBatches = Math.ceil(scientists.length / parallel);

  console.log(`\nTaking screenshots of ${scientists.length} Wikipedia articles on Indian scientists.`);
  console.log(`This will be done in ${parallelBatches} batches.`);

  for (let i = 0; i < scientists.length; i += parallel) {
    const browser = await puppeteer.launch({headless: false});
    const context = await browser.createIncognitoBrowserContext();
    const page = await context.newPage();
    page.setJavaScriptEnabled(false);

    let k = i / parallel + 1;
    console.log(`\nBatch ${k} of ${parallelBatches}`);

    const promises = [];
    for (let j = 0; j < parallel; j++) {
      const elem = i + j;
      if (scientists[elem] !== undefined) {
        promises.push(browser.newPage().then(async (page) => {
          await page.setViewport({ width: 1280, height: 800 });
          try {
            await page.goto(scientists[elem].url, { waitUntil: 'domcontentloaded' });
            await page.waitForTimeout(10000); // Wait for 2 seconds after page load
            await page.screenshot({ path: `${elem+1} ${scientists[elem].name}.png` }); // Decrement elem by 1
            console.log(`Screenshot taken for ${scientists[elem].name}`);
          } catch (err) {
            console.log(`Error while taking a screenshot for ${scientists[elem].name}`);
          }
        }));
      }
    }

    await Promise.all(promises);
    await browser.close();

    console.log(`Batch ${k} finished.`);
  }
};

screenshotScientists(scientists, parallel);
