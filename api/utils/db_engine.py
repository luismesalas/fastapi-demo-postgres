import os

from sqlmodel import create_engine

from api.decorators.singleton import singleton


@singleton
class DBEngine(object):
    def __init__(self):
        self.__engine = create_engine(f"postgresql://{os.getenv('PG_USER')}:{os.getenv('PG_PASS')}@"
                                      f"{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DB')}")

    def get_db_engine(self):
        return self.__engine
