from appCreation import mongoClient

def getByMalId(collection, id):
    try:
        db = mongoClient["scraper"]
        dbCollection = db[collection.capitalize()]
        item = dbCollection.find_one({"mal_id": id})
        if item is None:
            return None
        else:
            item.pop("_id")
            return item
    except Exception as e:
        print(e)
        return "Error"

def getByAnilistId(collection, id):
    try:
        db = mongoClient["scraper"]
        dbCollection = db[collection.capitalize()]
        item = dbCollection.find_one({"ani_id": id})
        if item is None:
            return None
        else:
            item.pop("_id")
            return item
    except Exception as e:
        print(e)
        return "Error"
        
def getByHashedId(collection, id):
    try:
        db = mongoClient["scraper"]
        dbCollection = db[collection.capitalize()]
        item = dbCollection.find_one({"id": id})
        if item is None:
            return None
        else:
            item.pop("_id")
            return item
    except Exception as e:
        print(e)
        return "Error"


