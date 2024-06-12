import json
import logging
from datetime import datetime

from controller.base_stream import BaseWebsocketClient
from models.base import session
from models.trademodel import TradeModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
logger = logging.getLogger(__name__)


class TradeStream(BaseWebsocketClient):
    def __init__(self):
        super().__init__(uri="wss://api.coin.z.com/ws/public/v1")

    async def on_open(self, ws):
        message = {
            "command": "subscribe",
            "channel": "trades",
            "symbol": "BTC_JPY"
        }
        await ws.send(json.dumps(message))
        logger.info(f"connected | message: {message}")

    async def onmessage(self, message):
        message_json = message.json()
        timestamp = datetime.fromisoformat(message_json["timestamp"].replace("Z", "+00:00"))
        session.add(TradeModel(
            symbol=message_json["symbol"], price=float(message_json["price"]), side=message_json["side"],
            timestamp=timestamp, channel=message_json["channel"],
            size=float(message_json["size"]),
        ))
        session.commit()
        logger.info(message_json)
