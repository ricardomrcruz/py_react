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


app = FastAPI(title="API", description="api test", docs_url="/docs")

db = CRUD()


app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# API routes
app.include_router(api_endpoints.router, prefix="/api/v1", tags=["api"])


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse({"request": request}, name="index.html")

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse({"request": request}, name="dashboard.html")


@app.get("/test", response_class=HTMLResponse)
async def index2(request: Request, hx_request: Annotated[str | None, Header()] = None):
    films = [
        {"name": "Blade Runner", "director": "Ridley Scott"},
        {"name": "Inception", "director": "Christopher Nolan"},
        {"name": "The Matrix", "director": "Lana Wachowski"},
        {"name": "Pulp Fiction", "director": "Quentin Tarantino"},
    ]
    context = {"request": request, "films": films}
    if hx_request:
        return templates.TemplateResponse("components/table.html", context)
    return templates.TemplateResponse("index3.html", context)


@app.get("/dropdown-feat", response_class=HTMLResponse)
async def dropdown_feat():
    return """ 
    <div
    class=" border-b border-neutral-800 p-2"
    hx-trigger="mouseleave from:body"
    hx-target="#dropdown"
    hx-swap="innerHTML"
    hx-get="/empty-dropdown">
        <ul class="w-[70%] flex flex-wrap items-center justify-center gap-8 mx-auto">
            <li>
                <a
                href="#"
                class="block py-2 px-3 text-gray-300 rounded md:hover:text-white md:p-0"
                >Market Data</a
                >
            </li>
            <li>
                <a
                href="#"
                class="block py-2 px-3 text-gray-300 rounded md:hover:text-white md:p-0"
                >Upcoming releases</a
                >
            </li>
        </ul>
    </div>
    """


@app.get("/dropdown-about", response_class=HTMLResponse)
async def dropdown_about():
    return """ 
    <div
    class=" border-b border-neutral-800 p-2"
    hx-trigger="mouseleave from:body"
    hx-target="#dropdown"
    hx-swap="innerHTML"
    hx-get="/empty-dropdown">
        <ul class="w-[70%] flex flex-wrap items-center justify-center gap-8 mx-auto">
            <li>
                <a
                href="#"
                class="block py-2 px-3 text-gray-300 rounded md:hover:text-white md:p-0"
                >Who are we?</a
                >
            </li>
            <li>
                <a
                href="#"
                class="block py-2 px-3 text-gray-300 rounded md:hover:text-white md:p-0"
                >Contact Us</a
                >
            </li>
        </ul>
    </div>
    """


@app.get("/empty-dropdown", response_class=HTMLResponse)
async def empty_dropdown():
    return ""
