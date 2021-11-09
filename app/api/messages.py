from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import MessageOut, MessageIn, RecipientMessages
from app.api import db_manager

messages = APIRouter()


@messages.post('/', response_model=MessageOut, status_code=201)
async def send_message(payload: MessageIn):
    message_id = await db_manager.add_message(payload)

    response = {
        'id': message_id,
        **payload.dict()
    }

    return response


@messages.get('/{recipient}/', response_model=RecipientMessages)
async def get_message(recipient):
    messages = await db_manager.get_recipient_messages(recipient)
    res = {"messages": messages}

    return res
