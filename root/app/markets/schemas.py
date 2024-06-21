from pydantic import BaseModel, EmailStr


class Product(BaseModel):
    title: str
    price: int
    img: str
    description: str | None = None
    url: str
    rating: str | None = None
    state: str | None = None

    class Config:
        orm_mode = True


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

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str



