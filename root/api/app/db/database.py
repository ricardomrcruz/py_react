from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import text
from dotenv import load_dotenv
import os

load_dotenv()

class Base(DeclarativeBase):
    pass

async def init_db() -> AsyncEngine:
    engine = create_async_engine(os.getenv("DATABASE_URL"), echo=True)
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))
    print("Database connection successful")
    return engine


engine = None
async_session_maker = None