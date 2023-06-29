


from binance import Client, ThreadedWebsocketManager

class StreamData:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.websocket_manager = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
        self.price = None

    def start_price_stream(self, symbol):
        self.websocket_manager.start_symbol_ticker_socket(symbol, self.process_price_event)
        self.websocket_manager.start()

    def process_price_event(self, event):
        self.price = float(event['c'])

    def stop_price_stream(self):
        self.websocket_manager.stop_socket(self.websocket_manager.get_socket_key(symbol))
        self.websocket_manager.stop()
