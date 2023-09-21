const puppeteer = require('puppeteer');
const fs = require('fs/promises');
const path = require('path');

const outputPath = path.join(__dirname, 'fetchData'); // Path to the fetchData directory

async function start(url, outputFile, captureScreenshot = false) {
    try {
        const browser = await puppeteer.launch({ headless: false });
        const page = await browser.newPage();
        await page.goto(url);


        const pdfPath = path.join(outputPath, outputFile + '.pdf');
        await page.pdf({ path: pdfPath, format: 'A4' });
        console.log(`PDF generated as ${outputFile}.pdf`);

        if (captureScreenshot) {
            const screenshotPath = path.join(outputPath, outputFile + '.png');
            await page.screenshot({ path: screenshotPath, fullPage: true });
            console.log(`Screenshot captured as ${outputFile}.png`);
        }

        await browser.close();
    } catch (err) {
        console.error('An error occurred:', err);
    }
}

const url = "https://www.google.com/";
const outputFile = "index3";

// Set captureScreenshot to true if you want to capture a screenshot
start(url, outputFile, false);
