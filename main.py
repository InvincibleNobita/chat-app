
from typing import Optional

from fastapi import FastAPI
import os
from dotenv import load_dotenv
import pymongo
from bson.objectid import ObjectId
from model.pymongo_model import SimpleModel, DiffHistoryModelV1, DiffHistoryModelV2
from models.user import User
from models.message import Message
from schemas.user import serializeDict,serializeList

load_dotenv()


MONGO_KEY = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_KEY)
db = client["PyAssignment"]

app = FastAPI()

@app.get("/")
def get_messages():
    return serializeList(db.message.find())

@app.post("/signup")
def signup(newUser: User):
    print(newUser)
    db.user.insert_one(dict(newUser))
    return serializeList(db.user.find())

@app.post("/send-chat")
def send_chat(newMessage: Message):
    db.message.insert_one(dict(newMessage))
    return serializeList(db.message.find())


@app.post("/login")
def login(existingUser: User):
    user = serializeList(db.user.find_one({'username':existingUser.username}))
    print(user)
    return {user}


