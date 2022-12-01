from fastapi import FastAPI, status, Response
from pydantic import BaseModel
from secrets import token_hex

class ShortUrl(BaseModel):
    hash: str
    link: str

app = FastAPI()

hashList = {}

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/new")
def addLink(link: str):
    hash = token_hex(4).upper()
    hashList[hash] = link
    return {"hash": hash}

@app.get("/{hash}", status_code=status.HTTP_301_MOVED_PERMANENTLY)
def hashMatch(hash: str, response: Response):
    link = hashList.get(hash)
    response.headers["Location"] = link
    return {}
