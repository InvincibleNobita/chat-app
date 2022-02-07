from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
import pymongo
from bson.objectid import ObjectId
from model.pymongo_model import SimpleModel, DiffHistoryModelV1, DiffHistoryModelV2

MONGO_KEY = os.getenv('MONGO_KEY')
client = pymongo.MongoClient(MONGO_KEY)
db = client["myFirstDatabase"]
class User(SimpleModel):
    collection = db.user 
#print(os.environ['MONGO_URI'])
#conn=MongoClient(os.environ['MONGO_URI'])