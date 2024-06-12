import asyncio

from stream.tradestream import TradeStream


async def main():
    trade_stream = TradeStream()
    await trade_stream.connect()

if __name__ == '__main__':
    asyncio.run(main())
