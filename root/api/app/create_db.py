import asyncio
from db.database import Base, init_db
from db.models import Product, Category, User  # import your models

async def create_db():
    engine = await init_db()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(create_db())