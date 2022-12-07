import uvicorn

from models import ShortUrl
from database import db

db.connect()
db.create_tables([ShortUrl])
db.close()

if __name__ == "__main__":
    uvicorn.run("routes:app", host="0.0.0.0", port=8000, reload=True)
