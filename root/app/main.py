from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import Optional, List, Annotated
from pydantic import BaseModel
from app.db.repositories import CRUD
from app.db.database import engine
from app.db.models import Product
from app.db.create_db import create_db
from app.db.schemas import User, Product, Category, ProductByCategory, Market, UserResearch, UserCreate, User
from http import HTTPStatus

app = FastAPI(title="API", description="api test", docs_url="/")

session = async_sessionmaker(bind=engine, expire_on_commit=False)

db = CRUD()

@app.get("/products" ,response_model=List[Product])
async def get_all_products():
    products = await db.get_all(session)
     
    if products is None:
        return []

    return products

@app.post("/products")
async def create_product():
    pass

@app.get("/product/{product_id}")
async def get_product_by_id(product_id):
    pass

@app.patch("/product/{product_id}")
async def update_product_by_id(product_id):
    pass

@app.delete("/product/{product_id}")
async def delete_product_by_id():
    pass
