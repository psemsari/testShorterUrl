from models import *
from secrets import token_hex

def get_hash_by_link(link: str):
    query = ShortUrl.get_or_none(ShortUrl.link == link)
    return query.hash if query else query

def get_link_by_hash(hash: str):
    query = ShortUrl.get_or_none(ShortUrl.hash == hash)
    return query.link if query else query

def create_hash(link: str):
    hash = token_hex(4).upper()
    ShortUrl.create(hash=hash, link=link)
    return (hash)
