const puppeteer = require('puppeteer');
const fs = require('fs/promises');
const path = require('path');

const outputPath = path.join(__dirname, 'fetchData'); // Path to the fetchData directory

async function enterFormData(url, searchQuery, outputFilename) {
    try {
        const browser = await puppeteer.launch({ headless: false }); // Launch Puppeteer in non-headless mode
        const page = await browser.newPage();
        await page.goto(url);

        await page.focus('textarea[name="q"]');
        await page.keyboard.type(searchQuery);
        await page.keyboard.press('Enter');

        await page.waitForNavigation({ waitUntil: 'networkidle2' });

        // Capture a screenshot of the search results page
        const screenshotPath = path.join(outputPath, outputFilename);
        await page.screenshot({ path: screenshotPath, fullPage: true });

        await browser.close();

        console.log(`Search Query: ${searchQuery} fetched successfully and screenshot saved as ${outputFilename}`);
    } catch (error) {
        console.error(error);
    }
}

const url = "https://www.google.com/";
const searchQuery = "Avengers Endgame";
const outputFilename = "formData.png";

enterFormData(url, searchQuery, outputFilename);
