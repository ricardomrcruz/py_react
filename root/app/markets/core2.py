import asyncio
from playwright.async_api import async_playwright
import sys



async def scrape_amazon(query:str):

    browsers = ["chromium", "firefox", "webkit"]
    async with async_playwright() as p:
        for browser_type in browsers:

            browser = await p[browser_type].launch()
            page = await browser.new_page()
            # query = "playstation+5+console" 
            await page.goto(f"https://www.amazon.fr/s?k={query}")
            await page.screenshot(path=f"py_{browser_type}.png", full_page=True)
            await page.wait_for_timeout(1000)

            all_products = await page.query_selector_all(
                ".s-card-container > .a-spacing-base"
            )
            data = []
            for product in all_products:
                result = dict()
                title_el = await product.query_selector(".a-size-base-plus")
                result["title"] = await title_el.inner_text() if title_el else None
                price_el = await product.query_selector(".a-price")
                result["price"] = await price_el.inner_text() if price_el else None
                rating_el = await product.query_selector(".a-icon-alt")
                result["rating"] = await rating_el.inner_text() if rating_el else None
                img_el = await product.query_selector(".s-image-optimized-rendering")
                result["img"] = await img_el.get_attribute("src") if img_el else None
                data.append(result)

            print(data)
            await browser.close()
    return data

async def main(query:str):
    return await scrape_amazon(query)

if __name__ == "__main__":
    asyncio.run(main("playstation+5+console"))
