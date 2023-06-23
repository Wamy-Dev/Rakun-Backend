import requests

def getSearchStatus():
    try:
        req = requests.get('https://search.rakun.app/health')
        if req.status_code == 200:
            return "OK"
        else:
            return "NOK"
    except:
        return "NOK"
def getWebsiteStatus():
    try:
        req = requests.get('https://rakun.app')
        if req.status_code == 200:
            return "OK"   
        else:
            return "NOK"
    except:
        return "NOK"
