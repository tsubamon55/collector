from sqlalchemy import desc

from models.base import session
from models.trademodel import TradeModel


trades = session.query(TradeModel).all()
chunk = []
chain = []
side_now = "BUY"

print(trades)

for trade in trades:
    if trade.side == side_now:
        chunk.append(trade)
    else:
        if len(chunk) == 1:
            chain.append([0, 0])
        else:
            amount = 0
            for c in chunk:
                amount += c.size
            chain.append([chunk[0].price - chunk[-1].price, amount])
        chunk = [trade]
        side_now = trade.side
print(chain)

