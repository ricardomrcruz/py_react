from playwright.async_api import async_playwright
import asyncio


query = "playstation+5+console"


async def main():
    browsers = ["chromium", "firefox", "webkit"]
    async with async_playwright() as p:
        for browser_type in browsers:
            browser = await p[browser_type].launch()
            page = await browser.new_page()
            await page.goto("https://www.amazon.fr/s?k={query}")
            page.screenshot(path=f"py_{browser_type}.png", full_page=True)
            await page.wait_for_timeout(1000)
            await browser.close()

            all_products = await page.query_selector_all(
                ".s-card-container > .a-spacing-base"
            )
            data = []
            for product in all_products:
                result = dict()
                title_el = await product.query_selector(".a-size-mini")
                result["title"] = await title_el.inner_text() if title_el else None
                price_el = await product.query_selector(".a-price")
                result["price"] = await price_el.inner_text() if price_el else None
                rating_el = await product.query_selector(".a-icon-alt")
                result["rating"] = await rating_el.inner_text() if rating_el else None
                img_el = await product.query_selector(".a-img")
                result["img"] = await img_el.inner_text() if img_el else None


asyncio.run(main())
