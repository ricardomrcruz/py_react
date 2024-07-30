from fastapi import FastAPI, HTTPException
from .scraper import scrape_amazon

app = FastAPI()

@app.post("/scrape")
def scrape(query: str):
    try:
        result = scrape_amazon(query)
        return {"data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))