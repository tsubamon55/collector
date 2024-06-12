import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

from config import conf

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
logger = logging.getLogger(__name__)

username = conf["db"]["username"]
password = conf["db"]["password"]
host = conf["db"]["host"]
database = conf["db"]["database"]

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}?charset=utf8mb4')
session = Session(bind=engine)


class Base(DeclarativeBase):
    pass


def init_db():
    Base.metadata.create_all(bind=engine)
    logger.info("database created")


