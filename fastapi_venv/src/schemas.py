import pydantic

class CreateHash(pydantic.BaseModel):
    link: pydantic.HttpUrl

class Token(pydantic.BaseModel):
    access_token: str
    token_type: str
