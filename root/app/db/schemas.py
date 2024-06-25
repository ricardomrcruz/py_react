from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class Product(BaseModel):
    
    title: str
    price: int
    img: str
    description: str | None = None
    url: str
    rating: str | None = None
    state: str | None = None
    date_created: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
      

class Category(BaseModel):
    name: str

class ProductByCategory(BaseModel):
    product_id: int
    category_id: int


class Market(BaseModel):
    base_urls: str


class UserResearch(BaseModel):
    title: str
    Results: list[str] = []


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str | None = None


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str | None = None

    model_config = ConfigDict(
        from_attributes=True
    )


class UserLogin(BaseModel):
    username: str
    password: str
