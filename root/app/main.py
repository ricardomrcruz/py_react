from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import Optional, List, Annotated
from http import HTTPStatus
from app.db.repositories import CRUD
from app.db.database import engine
from app.db.models import Product as DBProduct
from app.db.create_db import create_db
from app.db.schemas import (
    User,
    Product,
    CreateProductModel,
    Category,
    ProductByCategory,
    Market,
    UserResearch,
    UserCreate,
    User,
)
import uuid
from pydantic import BaseModel


app = FastAPI(title="API", description="api test", docs_url="/")

session = async_sessionmaker(bind=engine, expire_on_commit=False)

db = CRUD()
