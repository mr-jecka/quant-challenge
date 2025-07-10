from typing import Dict
from contracts import Handler
from bybit import BybitClient
from contracts import FetchOrderbookCommand, CalculateDeltaCommand, RunStrategyCommand


class BybitOrderbookHandler(Handler):
    def __init__(self, client: BybitClient):
        self.client = client

    async def handle(self, cmd: FetchOrderbookCommand) -> Dict:
        return await self.client.fetch_orderbook_snapshot(cmd.symbol, cmd.limit)


class DeltaHandler(Handler):
    async def handle(self, cmd: CalculateDeltaCommand) -> float:
        return await self.client.calculate_delta(cmd.snapshot_prev, cmd.snapshot_new)


class StrategyHandler(Handler):
    def __init__(self, strategy):
        self.strategy = strategy

    async def handle(self, cmd: RunStrategyCommand) -> Dict:
        return self.strategy.evaluate(cmd.symbol, cmd.delta)