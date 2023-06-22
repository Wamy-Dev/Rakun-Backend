from appCreation import fastAPI as app
from functions.statusFunctions import getSearchStatus, getWebsiteStatus
from typing import Literal
from api_analytics.fastapi import Analytics
from functions.getFunctions import getByMalId, getByAnilistId, getByHashedId
from fastapi import HTTPException
from fastapi.responses import FileResponse
app.add_middleware(Analytics, api_key='54494a91-1dee-4eb9-86d1-709d0971bec5')

@app.get("/favicon.ico", tags=["Basics"])
def favicon():
    return FileResponse("static/favicon.ico")

@app.get("/status", tags=["Basics"])
def get_status():
    return {
        "search": getSearchStatus(),
        "website": getWebsiteStatus(),
        "api": "OK"
    }

@app.get("/get/mal/{collection}/{mal_id}" , tags=["Items"], summary="Get an item by its MAL ID. Make sure to use the correct collection.")
def get_by_mal_id(collection: Literal["anime", "eroanime", "manga", "eromanga"], mal_id: int):
    data = getByMalId(collection, mal_id)
    if data is None:
        raise HTTPException(status_code=404, detail={
            "status": "NOK",
            "message": "Item not found. Make sure you are using the correct collection and have the correct MAL ID."
        })
    elif data == "Error":
        raise HTTPException(status_code=500, detail={
            "status": "NOK",
            "message": "Item not found. Make sure you are using the correct collection and have the correct MAL ID."
        })
    else:
        raise HTTPException(status_code=200, detail={
            "status": "OK",
            "message": "Successfully got item by MAL ID.",
            "data": data
        })

@app.get("/get/anilist/{collection}/{anilist_id}" , tags=["Items"], summary="Get an item by its ANILIST ID. Make sure to use the correct collection.")
def get_by_anilist_id(collection: Literal["anime", "eroanime", "manga", "eromanga"], anilist_id: int):
    data = getByAnilistId(collection, anilist_id)
    if data is None:
        raise HTTPException(status_code=404, detail={
            "status": "NOK",
            "message": "Item not found. Make sure you are using the correct collection and have the correct ANILIST ID."
        })
    elif data == "Error":
        raise HTTPException(status_code=500, detail={
            "status": "NOK",
            "message": "Item not found. Make sure you are using the correct collection and have the correct ANILIST ID."
        })
    else:
        raise HTTPException(status_code=200, detail={
            "status": "OK",
            "message": "Successfully got item by ANILIST ID.",
            "data": data
        })

@app.get("/get/id/{collection}/{id}" , tags=["Items"], summary="Get an item by its hashed ID. Make sure to use the correct collection.", description="The ID is the hashed ID in md5 of the MAL name of the item + the type of the item (title-cased). For example the ID of the anime `Boku no Hero Academia` is `Boku no Hero AcademiaAnime` then hashed to md5 gives this id -> `2bfbcac5fc33577c29656bd102c2db1a`. This likely is not useful for you, but it is how to search engine shows the pages, and is the static url for the page.")
def get_by_hashed_id(collection: Literal["anime", "eroanime", "manga", "eromanga"], id: str):
    data = getByHashedId(collection, id)
    if data is None:
        raise HTTPException(status_code=404, detail={
            "status": "NOK",
            "message": "Item not found. Make sure you are using the correct collection and have the correct HASHED ID."
        })
    elif data == "Error":
        raise HTTPException(status_code=500, detail={
            "status": "NOK",
            "message": "Item not found. Make sure you are using the correct collection and have the correct HASHED ID."
        })
    else:
        raise HTTPException(status_code=200, detail={
            "status": "OK",
            "message": "Successfully got item by HASHED ID.",
            "data": data
        })

