from playwright.async_api import async_playwright
import asyncio

async def main():
    browsers = ['chromium','firefox','webkit']
    async with async_playwright() as p:
        for browser_type in browsers:
            browser = await p[browser_type].launch()