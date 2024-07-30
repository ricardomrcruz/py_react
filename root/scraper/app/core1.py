import asyncio
from playwright.async_api import async_playwright
import json

async def scrape_amazon(query: str):
    try:
        async with async_playwright() as p:
             # browser = await p.chromium.launch(executable_path=r"G:\Program Files\Google\Chrome\Application\chrome.exe")
            browser = await p.chromium.launch(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            page = await browser.new_page()
            await page.goto(f"https://www.amazon.fr/s?k={query}")
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
                img_el = await product.query_selector(".s-image")
                result["img"] = await img_el.get_attribute("src") if img_el else None
                data.append(result)

            await browser.close()
        return data
    except Exception as e:
        print(f"Error in scrape_amazon: {str(e)}", file=sys.stderr)
        raise

if __name__ == "__main__":
    try:
        import sys
        query = sys.argv[1]
        result = asyncio.run(scrape_amazon(query))
        print(json.dumps(result))
    except Exception as e:
        print(f"Error in main: {str(e)}", file=sys.stderr)
        sys.exit(1)