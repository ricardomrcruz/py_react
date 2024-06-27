from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
import uuid


class Product(BaseModel):

    id: uuid.UUID
    title: str
    price: int
    img: str
    description: str | None = None
    url: str
    rating: str | None = None
    state: str | None = None
    date_created: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateProductModel(BaseModel):

    title: str
    price: int
    img: str
    description: str | None = None
    url: str
    rating: str | None = None
    state: str | None = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "title": "Sample title",
                "price": 20,
                "img": "https://fastly.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U",
                "description": "",
                "rating": "5 in 5",
                "url": "https://www.amazon.com/Lenovo-IdeaPad-Celeron-Storage-Graphics/dp/B0CK66T68X",
                "state": "New",
            }
        },
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

    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    username: str
    password: str
