import peewee
from env import *

db = peewee.PostgresqlDatabase(DBNAME, host=HOST, user=USER, password=PSWD, port=PORT)

def get_db():
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()
