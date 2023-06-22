from pymongo import MongoClient
from fastapi import FastAPI
from appConfig import MONGO_URI

def createMongo():
    client = MongoClient(MONGO_URI)
    return client

mongoClient = createMongo()

def createFastAPI():
    tags_metadata = [
        {
            "name": "Items",
            "description": "Items are the main functions of Rakun. They are the things you can search for. They contain metadata as well as the links you want.",
        },
        {
            "name": "Basics",
            "description": "These are the basic endpoints of the API. General endpoints.",
        }
    ]
    app = FastAPI(
        title="Rakun API",
        description='''
        This is the API for Rakun.

        You can find Rakun at https://rakun.app and https://search.rakun.app
        ''',
        openapi_tags=tags_metadata,
    )
    return app

fastAPI = createFastAPI()
