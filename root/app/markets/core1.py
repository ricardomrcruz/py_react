from fastapi import FastAPI, APIRouter, Request, Header
from playwright.async_api import async_playwright
import asyncio
import logging
import sys
import json 
import os

app = FastAPI()
router = APIRouter()

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def scrape_amazon():

    browsers = ["chromium", "firefox", "webkit"]
    async with async_playwright() as p:
        for browser_type in browsers:

            browser = await p[browser_type].launch(args=['--no-sandbox'])
            page = await browser.new_page()
            query = "playstation+5+console"
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

            logging.debug(f"Scraped data: {data}")
            # print(data)
            await browser.close()
            return data
        
def run_scrape_amazon():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(scrape_amazon())
    loop.close()
    return result

@router.get("/run_scraper1")
async def run_scraper1():
    try:
        scraped_data = await asyncio.to_thread(run_scrape_amazon)
        return {"status": "success", "data": scraped_data}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"status": "error", "message": str(e)}

app.include_router(router, prefix="/scraper", tags=["scraper1"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

