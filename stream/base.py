import websockets
import ssl
import certifi
import json

SSL_CONTEXT = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
SSL_CONTEXT.load_verify_locations(certifi.where())


class BaseWebsocketClient(object):

    def __init__(self, uri):
        self.uri = uri

    async def connect(self):
        async with websockets.connect(self.uri, ssl=SSL_CONTEXT) as ws:
            await self.on_open(ws)
            while True:
                msg = await ws.recv()
                await self.onmessage(Message(msg))

    async def on_open(self, ws):
        pass

    async def onmessage(self, message):
        pass


class Message(object):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    def json(self):
        message_json = json.loads(self.message)
        return message_json


