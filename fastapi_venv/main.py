from fastapi import FastAPI, status, Response, Depends

from database import db
from models import ShortUrl

import crud

db.connect()
db.create_tables([ShortUrl])
db.close()

app = FastAPI()

hashList = {}

def get_db():
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/new", dependencies=[Depends(get_db)])
def addLink(link: str):
    hash = crud.get_hash_by_link(link)
    if not hash:
        hash = crud.create_hash(link)
    return {"hash": hash}

@app.get("/{hash}", status_code=status.HTTP_301_MOVED_PERMANENTLY, dependencies=[Depends(get_db)])
def hashMatch(response: Response, hash: str):
    if len(hash) == 8:
        link = crud.get_link_by_hash(hash)
        response.headers["Location"] = link
        return {}
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error" : "Not found"}
