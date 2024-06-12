from models.base import Base, engine
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class TradeModel(Base):
    __tablename__ = 'public_trade'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel: Mapped[str] = mapped_column(String(15))
    price: Mapped[float] = mapped_column(Float)
    side: Mapped[str] = mapped_column(String(15))
    size: Mapped[float] = mapped_column(Float)
    symbol: Mapped[str] = mapped_column(String(15))
    timestamp: Mapped[DateTime] = mapped_column(DateTime)


Base.metadata.create_all(bind=engine)
