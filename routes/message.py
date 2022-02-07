from fastapi import APIRouter

from models.message import Message

#from config.db import conn
from schemas.message import serializeDict, serializeList

message = APIRouter()

@message.get('/')
def get_all_message():
    pass