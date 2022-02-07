from pydantic import BaseModel

class Message(BaseModel):
    body: str
    username: str
    #date: 