from pydantic import BaseModel

class CreateHash(BaseModel):
    link: str
