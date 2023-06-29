from binance.client import Client
from configparser import ConfigParser
import time
import pandas as pd
import os
from dotenv import load_dotenv


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class DataAcquisition(metaclass=Singleton):
    def __init__(self):
        load_dotenv()
        self.public_key = os.getenv('api_key')
        self.private_key = os.getenv('api_secret')
        self.client = Client(self.public_key, self.private_key)

    def calculate_days(self):
        end_timestamp = int(time.time() * 1000)
        start_timestamp = end_timestamp - (self.days * 86400 * 1000)
        return start_timestamp, end_timestamp

    def path_for_each(self):
        output_path = os.path.join(f"historical_data/{self.symbol}_{self.interval}_{self.days}d.csv")
        self.df.to_csv(output_path)


    def path_for_all(self):
        output_path = os.path.join(f"historical_all_data/{self.symbol}_{self.interval}_{self.days}d.csv")
        self.df.to_csv(output_path)


    def get_symbol_interval(self, symbol, interval, days):
        self.symbol = symbol
        self.interval = interval
        self.days = days
        self.start_timestamp, self.end_timestamp = self.calculate_days()
        klines = self.client.get_historical_klines(self.symbol, self.interval, self.start_timestamp, self.end_timestamp)
        self.df = self.klines_to_df(klines)
        self.path_for_each()
        return self.df



    def get_all_symbols(self, interval, days):
        self.interval, self.days = interval, days
        self.start_timestamp, self.end_timestamp = self.calculate_days()

        exchange_info = self.client.get_exchange_info()
        symbols = [symbol['symbol'] for symbol in exchange_info['symbols']]

        for symbol in symbols:
            klines = self.client.get_historical_klines(symbol, self.interval, self.start_timestamp, self.end_timestamp)
            self.symbol = symbol
            self.df = self.klines_to_df(klines)
            self.path_for_all()

    def klines_to_df(self, klines):
        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                           'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
                                           'taker_buy_quote_asset_volume', 'ignore'])
        df.drop(['close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
                 'taker_buy_quote_asset_volume', 'ignore'], axis=1, inplace=True)
        df['open'] = pd.to_numeric(df['open'])
        df['high'] = pd.to_numeric(df['high'])
        df['low'] = pd.to_numeric(df['low'])
        df['close'] = pd.to_numeric(df['close'])
        df['volume'] = pd.to_numeric(df['volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp to datetime
        df.set_index('timestamp', inplace=True)
        return df

    def read_coin(self, file):
        file_path = os.path.join(f"historical_data/{file}")
        data = pd.read_csv(file_path, parse_dates=['timestamp'])
        data.set_index('timestamp', inplace=True)
        return data

    @classmethod
    def load_config(cls, file='config.ini'):
        config = ConfigParser()
        with open(file, 'r') as f:
            config.read_file(f)
        return config
