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
from app.router import htmx_components 


app = FastAPI(title="API", description="api test", docs_url="/docs")

db = CRUD()


app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# API routes
app.include_router(api_endpoints.router, prefix="/api/v1", tags=["api"])
app.include_router(htmx_components.router)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse({"request": request}, name="index.html")

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse({"request": request}, name="dashboard.html")

@app.get("/signin", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse({"request": request}, name="login.html")





