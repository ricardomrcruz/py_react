from fastapi import FastAPI, HTTPException, APIRouter
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
from pydantic import BaseModel


router = APIRouter()

session = async_sessionmaker(bind=engine, expire_on_commit=False)

db = CRUD()


@router.get("/products", response_model=List[Product])
async def get_all_products():
    products = await db.get_all(session)

    if products is None:
        return []

    return products


@router.post("/products", status_code=HTTPStatus.CREATED)
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


@router.get("/product/{product_id}")
async def get_product_by_id(product_id):

    product = await db.get_product_by(session, product_id)

    return product


@router.patch("/product/{product_id}")
async def update_product(product_id: str, data: CreateProductModel):
    product = await db.update_product_by(
        session,
        product_id,
        data={
            "title": data.title,
            "price": data.price,
            "img": data.img,
            "description": data.description,
            "rating": data.rating,
            "url": data.url,
            "state": data.state,
        },
    )

    return product


@router.delete("/product/{product_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_product(product_id):
    product = await db.get_product_by(session, product_id)

    result = await db.delete(session, product)
    return result
