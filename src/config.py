from dotenv import load_dotenv
import os

load_dotenv()
BYBIT_TESTNET_API_KEY = os.getenv("BYBIT_TESTNET_API_KEY")
BYBIT_TESTNET_API_SECRET = os.getenv("BYBIT_TESTNET_API_SECRET")
SYMBOLS = ["BTCUSDT", "ETHUSDT"]
ORDERBOOK_LIMIT = 300