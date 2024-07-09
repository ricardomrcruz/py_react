import os
from fastapi import FastAPI, Request, HTTPException, Header
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import Optional, List, Annotated
from http import HTTPStatus
from app.db.repositories import CRUD
from app.db.database import engine
from app.db.models import Product as DBProduct
from app.db.create_db import create_db
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.router.api_v1 import endpoints as api_endpoints
from fastapi.responses import HTMLResponse


app = FastAPI(title="API", description="api test", docs_url="/")

db = CRUD()


app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# API routes
app.include_router(api_endpoints.router, prefix="/api/v1", tags=["api"])


@app.get("/index", response_class=HTMLResponse)
async def index(request: Request, hx_request: Annotated[str | None, Header()] = None):
    films = [
        {"name": "Blade Runner", "director": "Ridley Scott"},
        {"name": "Inception", "director": "Christopher Nolan"},
        {"name": "The Matrix", "director": "Lana Wachowski"},
        {"name": "Pulp Fiction", "director": "Quentin Tarantino"},
    ]
    context = {"request": request, "films": films}
    if hx_request:
        return templates.TemplateResponse("table.html", context)
    return templates.TemplateResponse("index.html", context)
