from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import Optional, List, Annotated
from pydantic import BaseModel
from db.repositories import CRUD
from db.database import engine

# from app.db.schemas import User, Product, Category, ProductByCategory, Market, UserResearch, UserCreate, User

app = FastAPI(title="API", description="api test", docs_url="/")


session = async_sessionmaker()
db = CRUD()


@app.get("/products")
async def get_all_products():
    products = db.get_all()


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
