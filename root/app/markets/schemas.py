from pydantic import BaseModel


class Product(BaseModel):
    id: int
    title: str 
    price: int
    img: str 
    description: str 
    url: str

    class Config:
        validate_assignement = True


class Category(BaseModel):
    id: int
    name: str


class ProductByCategory(BaseModel):
    id: int
    product_id: Product.id
    category_id: Category.id







