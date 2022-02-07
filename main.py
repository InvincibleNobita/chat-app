from concurrent.futures import process
from typing import Optional

from fastapi import FastAPI

from routes.user import user
from routes.message import message



app = FastAPI()
app.include_router(user)
app.include_router(message)

#print(MONGO_URI)
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/signup")
def signup(username: str, password: str):

    return {"User created succeessfullyy"}

@app.post("/login")
def login(username: str, password: str):

    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
