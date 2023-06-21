from appCreation import fastAPI as app
from functions.statusFunctions import getSearchStatus, getWebsiteStatus

@app.get("/status")
def get_status():
    return {
        "search": getSearchStatus(),
        "website": getWebsiteStatus(),
        "api": "OK"
    }

    