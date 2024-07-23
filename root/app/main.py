import os
from fastapi import FastAPI, Request, HTTPException, Header, Form

from sqlalchemy.ext.asyncio import async_sessionmaker, insert
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

@app.post("/register/", response_class=HTMLResponse)
async def register(request:Request, email: str = Form(...), password: str=Form(...)):
    async with AsyncSession(engine) as session:
        hashed_password = auth_handler.get_hash_password(User.password)
        query = insert(User).values(email = User.email, hashed_password = hashed_password )
        await session.execute(query)
        await session.commit()
        
        response= templates.TemplateResponse("seccess.html",
                {"request":request, "success_msg":"Registration Successful!",
                 "path_route":'/', "path_msg":"Click here to login!"})
        return response
    
@app.login("/login/")
async def sign_in(request:Request, response:Response, 
    email:str = Form(...), password: str =Form(...)):
    try:
        async with AsyncSession(engine) as session:
            # find user mail
            query = select(User).values(User.email == email )
            result = await session.execute(query)
            user = result.scalar_one_or_none()
            
            if await auth_handler.authenticate_user(user.email, user.password):
                #if user and password verifies create cookie
                atoken = auth_handler.create_access_token(user.email)
                response = templates.TemplateResponse("success.html",
                    {"request":request, "USERNAME": user.email, "success_msg":"Welcome back!",
                     "path_route": '/private/', "path_msg": "Go to your private page!"})
                
                response.set_cookie(key="Authorization", value=f"{atoken}", httponly=True)
                return response
            else:
                return templates.TemplateResponse("error.html", 
                {"request":request, 'detail':'Incorrect Username or Password', 'status_code':404})
    except Exception as err:
        return templates.TemplateResponse("error.html", 
                {"request":request, 'detail':'Incorrect Username or Password', 'status_code':401})
        

    
    
        
        
        
   
