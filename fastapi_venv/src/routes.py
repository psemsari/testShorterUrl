from fastapi import FastAPI, status, Response, security, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import get_db
import schemas
import crud
import env

app = FastAPI()
oauth2_scheme = security.OAuth2PasswordBearer(tokenUrl="token")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/token")
def login(form_data: security.OAuth2PasswordRequestForm = Depends()):
    if not env.ADMIN == form_data.username or not env.ADMINPW == form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": form_data.username, "token_type": "bearer"}

@app.post("/new", dependencies=[Depends(get_db)])
def addLink(link: schemas.CreateHash):
    hash = crud.get_hash_by_link(link)
    if not hash:
        hash = crud.create_hash(link)
    return {"hash": hash}

@app.delete("/{hash}", dependencies=[Depends(get_db)])
def deleteShortURL(hash: str, token: str = Depends(oauth2_scheme)):
    crud.delete_by_hash(hash)
    return {"deleted": hash, "token": token}

@app.get("/{hash}", status_code=status.HTTP_301_MOVED_PERMANENTLY, dependencies=[Depends(get_db)])
def hashMatch(response: Response, hash: str):
    link = crud.get_link_by_hash(hash)
    if not link:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    response.headers["Location"] = link
    return {}
