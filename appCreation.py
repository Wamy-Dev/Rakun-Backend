from pymongo import MongoClient
from fastapi import FastAPI

def createMongo():
    client = MongoClient('mongodb+srv://Rakun:Rakun@rakuntest.vwblngb.mongodb.net/test')
    return client

mongoClient = createMongo()

def createFastAPI():
    app = FastAPI()
    return app

fastAPI = createFastAPI()
