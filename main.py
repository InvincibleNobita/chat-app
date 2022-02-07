
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
import os
from dotenv import load_dotenv
import pymongo
from bson.objectid import ObjectId
from model.pymongo_model import SimpleModel, DiffHistoryModelV1, DiffHistoryModelV2
from models.user import User
from models.message import Message
from schemas.user import serializeDict,serializeList

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

load_dotenv()


MONGO_KEY = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_KEY)
db = client["PyAssignment"]

app = FastAPI()

# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
#     )


@app.get("/")
def get_messages(token: str = Depends(oauth2_scheme)):
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
# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")

#     return {"access_token": user.username, "token_type": "bearer"}


