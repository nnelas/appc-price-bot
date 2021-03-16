from dataclasses import dataclass


@dataclass(frozen=True)
class Binance24hStats:
    symbol: str
    price_change_percent: float
    volume: float

    def get_formatted_price_change(self) -> str:
        return f"{self.price_change_percent:0.2f}%"
