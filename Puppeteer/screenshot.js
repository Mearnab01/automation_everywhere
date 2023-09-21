//How to take ss
const puppeteer = require('puppeteer');

async function start() {
    try {
        const browser = await puppeteer.launch({ headless: false }); 
        const page = await browser.newPage();
        
        await page.goto("https://www.youtube.com/results?search_query=puppeteer+tutorial", {
            waitUntil: "domcontentloaded"
        });

        await page.waitForTimeout(10000);

        await page.screenshot({ path: "ss_youtube.png", fullPage: true });

        await browser.close(); 
        console.log("Screenshot taken successfully.");
    } catch (error) {
        console.error("An error occurred:", error);
    }
}

start();
