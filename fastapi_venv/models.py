from peewee import *

from database import db

class BaseModel(Model):
    class Meta:
        database = db

class ShortUrl(BaseModel):
    hash = CharField(unique=True, index=True, max_length=8, primary_key=True)
    link = CharField()
    clicked = IntegerField(default = 0)
