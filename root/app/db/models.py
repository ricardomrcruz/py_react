from typing import List
from sqlalchemy import Text, Integer, String, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship, datetime
from app.db import Base


product_category_table = Table(
    "product_category",
    Base.metadata,
    mapped_column("product_id", Integer, ForeignKey("products.id")),
    mapped_column("category_id", Integer, ForeignKey("categories_id")),
)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    price: Mapped[int] = mapped_column(Integer)
    img: Mapped[str] = mapped_column(String)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    url: Mapped[str] = mapped_column(String)
    rating: Mapped[str | None] = mapped_column(String, nullable=True)
    date_created: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    categories: Mapped[List["Category"]] = relationship(
        secondary=product_category_table, back_populates="products"
    )

    def __repr__(self) -> str:
        return f"<Product {self.title} at {self.date_created}>"


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, unique=True)
    products: Mapped[List[Product]] = relationship(
        secondary=product_category_table, back_populates="categories"
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    full_name: Mapped[str | None] = mapped_column(String, nullable=True)
