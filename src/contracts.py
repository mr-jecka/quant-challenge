from dataclasses import dataclass
from typing import Dict, Any
from strategy import BaseDeltaStrategy


@dataclass
class FetchOrderbookCommand:
    """Команда для получения снимка ордербука."""
    symbol: str
    limit: int


@dataclass
class CalculateDeltaCommand:
    """Команда для вычисления дельты между снимками."""
    snapshot_prev: Dict
    snapshot_new: Dict


@dataclass
class RunStrategyCommand:
    """Команда для запуска стратегии."""
    symbol: str
    delta: float
    price: float = 0.0


class BybitOrderbookHandler:
    """Обработчик для получения снимков ордербука."""
    def __init__(self, client):
        self.client = client

    async def handle(self, request: FetchOrderbookCommand) -> Dict:
        return await self.client.fetch_orderbook(request)


class DeltaHandler:
    """Обработчик для вычисления дельты."""
    def __init__(self, client):
        self.client = client

    async def handle(self, request: CalculateDeltaCommand) -> float:
        return await self.client.calculate_delta(request)


class StrategyHandler:
    """Обработчик для выполнения стратегии."""
    def __init__(self, strategy: BaseDeltaStrategy):
        self.strategy = strategy

    async def handle(self, request: RunStrategyCommand) -> Dict[str, Any]:
        return self.strategy.execute(request.symbol, request.delta, request.price)