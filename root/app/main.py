from fastapi import FastAPI, HTTPException
from typing import Optional, List, Annotated
from pydantic import BaseModel

# from app.db.schemas import User, Product, Category, ProductByCategory, Market, UserResearch, UserCreate, User

app = FastAPI()


@app.get("/")
def index():
    return {"name": "First Data"}
