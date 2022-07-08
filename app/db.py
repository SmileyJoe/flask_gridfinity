from tinydb import TinyDB
from pathlib import Path

DIR_DB = 'app/db'
MODELS = DIR_DB + '/models.json'
TAGS = DIR_DB + '/tags.json'

@staticmethod
def setup():
    path = Path(DIR_DB)
    path.mkdir(parents=True,exist_ok=True)

@staticmethod
def models():
    return TinyDB(MODELS)

@staticmethod
def tags():
    return TinyDB(TAGS)