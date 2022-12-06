from peewee import *
from env import *

db = PostgresqlDatabase("ShorterUrl", host=HOST, user=USER, password=PSWD, port=PORT)
