from db.config import async_session
from data_access_layers.book_dal import BookDAL


async def get_book_dal():
    async with async_session() as session:
        async with session.begin():
            yield BookDAL(session)
