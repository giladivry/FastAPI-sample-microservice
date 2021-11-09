from app.api.models import MessageIn, MessageOut
from app.api.db import messages, database


async def add_message(payload: MessageIn):
    query = messages.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_message(id):
    query = messages.select(messages.c.id == id)
    return await database.fetch_one(query=query)


async def get_recipient_messages(recipient_id):
    query = messages.select(messages.c.recipient == recipient_id)
    return await database.fetch_all(query=query)
