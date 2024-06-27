from app.db.database import Base, engine
from app.db.models import Product, Category, User
import asyncio


async def create_db():
    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()


# decomment to create db
# asyncio.run(create_db())
