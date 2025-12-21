import flask
from sqlalchemy import text
from data.model.__init__ import *


Session = get_session()


#check db_session
"""stock = Stocks(
    ticker="AAPL",
    name="Apple Inc.",
    sector="Technology",
    industry="Consumer Electronics",
    description="Apple Inc. designs, manufactures, and markets consumer electronics and software.",
    currency="USD",
    exchange="NASDAQ",
    is_active=True
)

with Session() as session:
    if not session.query(Stocks).filter_by(ticker="AAPL").first():
        session.add(stock)
        session.commit()
    else:
        print("Запись с таким ticker уже существует!")


ans = session.query(Stocks).all()
for stock in ans:
    print(stock)"""