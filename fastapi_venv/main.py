from fastapi import FastAPI, status, Response, Path
from pydantic import BaseModel
from secrets import token_hex

class ShortUrl(BaseModel):
    hash: str
    link: str

app = FastAPI()

hashList = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/new")
async def addLink(link: str):
    hash = token_hex(4).upper()
    hashList[hash] = link
    return {"hash": hash}

@app.get("/{hash}", status_code=status.HTTP_301_MOVED_PERMANENTLY)
async def hashMatch(response: Response, hash: str):
    if len(hash) == 8:
        link = hashList.get(hash)
        response.headers["Location"] = link
        return {}
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error" : "Not found"}
