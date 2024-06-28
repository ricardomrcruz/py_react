from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import Optional, List, Annotated
from pydantic import BaseModel
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
from http import HTTPStatus
import uuid

app = FastAPI(title="API", description="api test", docs_url="/")

session = async_sessionmaker(bind=engine, expire_on_commit=False)

db = CRUD()


@app.get("/products", response_model=List[Product])
async def get_all_products():
    products = await db.get_all(session)

    if products is None:
        return []

    return products


@app.post("/products", status_code=HTTPStatus.CREATED)
async def create_product(product_data: CreateProductModel):
    new_product = DBProduct(
        title=product_data.title,
        price=product_data.price,
        img=product_data.img,
        description=product_data.description,
        url=product_data.url,
        rating=product_data.rating,
        state=product_data.state,
    )

    product = await db.add(session, new_product)

    return product


@app.get("/product/{product_id}")
async def get_product_by_id(product_id):
    product = await db.get_product_by(session, product_id)

    if product is None:
        return "Product non existent."

    return product


@app.patch("/product/{product_id}")
async def update_product(product_id: str, data: CreateProductModel):
    product = await db.update_product_by(session, product_id, data=data)

    return product

@app.delete("/product/{product_id}")
async def delete_product_by_id():
    pass
