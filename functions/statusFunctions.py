import requests

def getSearchStatus():
    req = requests.get('https://search.rakun.app/health')
    if req.status_code == 200:
        return "OK"
    else:
        return "NOK"
def getWebsiteStatus():
    req = requests.get('https://rakun.app')
    if req.status_code == 200:
        return "OK"   
    else:
        return "NOK"
