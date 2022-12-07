from secrets import token_hex

from models import *
from schemas import CreateHash

def get_hash_by_link(link: str):
    query = ShortUrl.get_or_none(ShortUrl.link == link)
    return query.hash if query else query

def get_link_by_hash(hash: str):
    query = ShortUrl.get_or_none(ShortUrl.hash == hash)
    return query.link if query else query

def create_hash(data: CreateHash):
    hash = token_hex(4).upper()
    ShortUrl.create(hash=hash, link=data.link)
    return (hash)

def delete_by_hash(hash: str):
    query: ShortUrl = ShortUrl.get_or_none(ShortUrl.hash == hash)
    if query:
        query.delete_instance()
    return
