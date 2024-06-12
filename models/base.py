import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
logger = logging.getLogger(__name__)

username = "collector"
password = "z9JLmSAK9BHMn0Z5IV7UlkdjT9T-R1_JsSXxwadg_KU"
host = "localhost"
database = "collector"

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}?charset=utf8mb4')
session = Session(bind=engine)


class Base(DeclarativeBase):
    pass


def init_db():
    Base.metadata.create_all(bind=engine)
    logger.info("database created")


