from app.db.models import Product
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select


class CRUD:
    async def get_all(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(Product).order_by(Product.id)

            result = await session.execute(statement)

            return result.scalars()

    async def add(
        self, async_session: async_sessionmaker[AsyncSession], product: Product
    ):
        async with async_session() as session:
            session.add(product)
            await session.commit()

            return product

    async def get_product_by(
        self, async_session: async_sessionmaker[AsyncSession], product_id: str
    ):
        async with async_session() as session:
            statement = select(Product).filter(Product.id == product_id)

            result = await session.execute(statement)
            return result.scalars().one()

    async def update_product_by(
        self, async_session: async_sessionmaker[AsyncSession], product_id, data
    ):
        async with async_session() as session:
            statement = select(Product).filter(Product.id == product_id)

            result = await session.execute(statement)

            product = result.scalars().one()

            product.title = data["title"]
            product.price = data["price"]
            product.img = data["img"]
            product.description = data["description"]
            product.url = data["url"]
            product.rating = data["rating"]
            product.state = data["state"]
            # product.categories = data["categories"]

            await session.commit()

            return product

    async def delete(
        self, async_session: async_sessionmaker[AsyncSession], product: Product
    ):
        async with async_session() as session:
            await session.delete(product)
            await session.commit()

        return {}
