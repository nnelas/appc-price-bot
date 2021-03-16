from http import HTTPStatus

import requests

from appc.binance_24h_stats import Binance24hStats
from appc.binance_api_response import BinanceApiResponse


class BinanceApiResponseMapper:
    def __init__(self):
        pass

    def map(self, response: requests.Response) -> BinanceApiResponse:
        if response.status_code == HTTPStatus.OK:
            stats = Binance24hStats(
                symbol=response.json()["symbol"],
                price_change_percent=float(response.json()["priceChangePercent"]),
                volume=float(response.json()["volume"]),
            )
            return BinanceApiResponse(HTTPStatus.OK, stats)
        return BinanceApiResponse(HTTPStatus.BAD_REQUEST)
