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
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from app.router import htmx_components
from app.auth import AuthHandler, RequiresLoginException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User
from app.db.database import engine


app = FastAPI(title="API", description="api test", docs_url="/docs")

db = CRUD()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")
auth_handler = AuthHandler()


# redirection from exception to index
@app.exception_handler(RequiresLoginException)
async def exception_handler(request: Request, exc: RequiresLoginException) -> Response:
    return RedirectResponse(url="/")


@app.middleware("http")
async def create_auth_header(request:Request, call_next):
    '''
    Checks if there are cookies set for authorization. If so, contruct 
    the authorization header and modify the request (unless the header 
    already exists!)
    '''
    if ("Authorization" not in request.headers
        and "Authorization" in request.cookies):
        access_token = request.cookies["Authorization"]
        
        request.headers.__dict__["_list"].append(
            (
                "authorization".encode(),
                f"Bearer{access_token}".encode(),
                                       
            )
        )
    elif ("Authorization" not in request.headers
        and "Authorization" not in request.cookies):
        request.headers.__dict__["_list"].append(
            (
                "authorization".encode(),
                f"Bearer 1234".encode(),
                                       
            )
        )
        
    response = await call_next(request)
    return response
        


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

# @app.post("/register/", response_class=HTMLResponse)
# async def register(request:Request, email: str = Form(...), password: str=Form(...)):
#     try:
#         async with AsyncSession(engine) as session:
#         query = insert(User).where(User.email == email)
#         result = await session.execute(query)
#         user = result.scalar_one_or_none()
#     catch:
        
   
