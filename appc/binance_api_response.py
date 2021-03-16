from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional

from appc.binance_24h_stats import Binance24hStats


@dataclass(frozen=True)
class BinanceApiResponse:
    status: HTTPStatus
    binance_24h_stats: Optional[Binance24hStats] = None
