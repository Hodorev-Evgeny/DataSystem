import sqlalchemy
import datetime
from sqlalchemy.orm import declarative_base
from .db_session import *


Session = get_session()
Base = declarative_base()


class Stocks(Base):
    __tablename__ = 'stocks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    ticker = sqlalchemy.Column(sqlalchemy.VARCHAR(10), unique=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=False)
    sector = sqlalchemy.Column(sqlalchemy.VARCHAR(100), nullable=False)
    industry = sqlalchemy.Column(sqlalchemy.VARCHAR(100), nullable=False)
    description = sqlalchemy.Column(sqlalchemy.TEXT, nullable=False)
    currency = sqlalchemy.Column(sqlalchemy.VARCHAR(10), nullable=False)
    exchange = sqlalchemy.Column(sqlalchemy.VARCHAR(50), nullable=False)
    is_active = sqlalchemy.Column(sqlalchemy.BOOLEAN, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=False, default=datetime.datetime.now(datetime.UTC))
    updated_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=False, default=datetime.datetime.now(datetime.UTC))

    def __repr__(self):
        return (f"<Stocks(id={self.id}, ticker='{self.ticker}', name='{self.name}', "
                f"sector='{self.sector}', exchange='{self.exchange}')>")