from fastapi import FastAPI, Request, Header, Form, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from typing import List
from app.db.repositories import CRUD
from app.db.database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.router.api_v1 import endpoints as api_endpoints
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from app.router import htmx_components
from app.auth import AuthHandler, RequiresLoginException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User as Userdb, Product as DBProduct
from app.db.database import engine
from app.db.schemas import User, UserOut
from datetime import datetime, timezone
import logging

app = FastAPI(title="API", description="api test", docs_url="/docs")

db = CRUD()
session = async_sessionmaker(bind=engine, expire_on_commit=False)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")
auth_handler = AuthHandler()


# redirection from exception to index
@app.exception_handler(RequiresLoginException)
async def exception_handler(request: Request, exc: RequiresLoginException) -> Response:
    return RedirectResponse(url="/")


@app.middleware("http")
async def create_auth_header(request: Request, call_next):
    """
    Checks if there are cookies set for authorization. If so, contruct
    the authorization header and modify the request (unless the header
    already exists!)
    """
    if "Authorization" not in request.headers and "Authorization" in request.cookies:
        access_token = request.cookies["Authorization"]

        request.headers.__dict__["_list"].append(
            (
                "authorization".encode(),
                f"Bearer{access_token}".encode(),
            )
        )
    elif (
        "Authorization" not in request.headers
        and "Authorization" not in request.cookies
    ):
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
app.include_router(htmx_components.router, tags=["htmx"])


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse({"request": request}, name="index.html")


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    # blocked access without cookie
    auth_token = request.cookies.get("Authorization")
    if not auth_token:
        return RedirectResponse(url="/signin", status_code=302)

    welcome = request.cookies.get("welcome", "")

    response = templates.TemplateResponse(
        {
            "request": request,
            "USERNAME": request.cookies.get("username", "User"),
            "success_login": welcome,
        },
        name="dashboard.html",
    )
    response.delete_cookie("welcome")
    return response


@app.get("/users", response_model=List[UserOut])
async def get_all_users():
    async with AsyncSession(engine) as session:
        result = await session.execute(select(Userdb))
        return result.scalars().all()


@app.get("/signin", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse({"request": request}, name="login.html")


@app.post("/register/", response_class=HTMLResponse)
async def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    verify_password: str = Form(...),
):
    async with AsyncSession(engine) as session:

        # if verify_password != password:
        #     logger.info(f"Error. Passwords dont verify eachother.")
        #     return """
        #     Passwords dont verify. 
        #     """, 400
        
        hashed_password = auth_handler.get_hash_password(password)
        current_time = datetime.now(timezone.utc)
        query = insert(Userdb).values(
            username=username,
            email=email,
            hashed_password=hashed_password,
            is_active=True,
            is_admin=False,
            updated_at=current_time,
        )
        await session.execute(query)
        await session.commit()

        response = templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "success_msg": "Registration Successful!",
                "path_route": "/",
                "path_msg": "Click here to login!",
            },
        )
        return response


@app.post("/login/")
async def sign_in(
    request: Request,
    response: Response,
    email: str = Form(...),
    password: str = Form(...),
):
    try:
        async with AsyncSession(engine) as session:
            logger.info(f"Attempting to find user with email: {email}")
            # find user mail
            query = select(Userdb).where(Userdb.email == email)
            result = await session.execute(query)
            user = result.scalar_one_or_none()

            if not user:
                logger.info(f"No user found with email: {email}")
                return templates.TemplateResponse(
                    "login.html",
                    {
                        "request": request,
                        "detail": "User not found",
                        "status_code": 404,
                    },
                )

            logger.info(f"User found: {user.email}")

            authenticated_user = await auth_handler.authenticate_user(email, password)
            if authenticated_user:
                # if user and password verifies create cookie
                atoken = auth_handler.create_access_token(user.email)
                logger.info(
                    f"Authentication successful for user: {user.email}. Redirecting to index."
                )
                response = RedirectResponse(url="/dashboard", status_code=303)
                response.set_cookie(
                    key="Authorization", value=f"{atoken}", httponly=True
                )
                response.set_cookie(key="welcome", value="Welcome back to Mark3ts")
                return response
            else:
                logger.info(f"Incorrect password for user: {email}")
                return templates.TemplateResponse(
                    "index.html",
                    {
                        "request": request,
                        "detail": "Incorrect Username or Password",
                        "status_code": 404,
                    },
                )
    except Exception as err:
        logger.error(f"An unexpected error occurred: {str(err)}")
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "detail": "Incorrect Username or Password",
                "status_code": 401,
            },
        )


@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    response = templates.TemplateResponse({"request": request}, name="index.html")
    response.delete_cookie("Authorization")
    return response
