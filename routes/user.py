from fastapi import APIRouter

from models.user import User

#from config.db import conn
from schemas.user import serializeDict, serializeList

user = APIRouter()

@user.get('/')
def get_all_user():
    return {"hh":'hh'}