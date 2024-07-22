from typing import List
from sqlalchemy import Text, Integer, String, Boolean, ForeignKey, Table, Column, func, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base
from datetime import datetime
import uuid


class Product(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String, index=True)
    price: Mapped[int] = mapped_column(Integer)
    img: Mapped[str] = mapped_column(String)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    url: Mapped[str] = mapped_column(String)
    rating: Mapped[str | None] = mapped_column(String, nullable=True)
    state: Mapped[str | None] = mapped_column(String, nullable=True)
    date_created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    category_id: Mapped[int | None] = mapped_column(
        ForeignKey("categories.id"), nullable=True
    )
    category: Mapped["Category | None "] = relationship(
        "Category", back_populates="products"
    )

    def __repr__(self) -> str:
        return f"<Product {self.title} at {self.date_created}>"


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, unique=True)
    products: Mapped[List[Product]] = relationship("Product", back_populates="category")


product_category_table = Table(
    "product_category",
    Base.metadata,
    Column("product_id", UUID(as_uuid=True), ForeignKey("products.id")),
    Column("category_id", Integer, ForeignKey("categories.id")),
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    full_name: Mapped[str | None] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=True) 
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self) -> str:
        return f"<User {self.username}"
    

