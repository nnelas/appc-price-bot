from http import HTTPStatus
from typing import Optional

from appc.binance_24h_stats import Binance24hStats
from appc.binance_api_wrapper import BinanceApiWrapper
from appc.catappult_api_wrapper import CatappultApiWrapper


class AppcPriceRepository:
    def __init__(
        self,
        binance_api: BinanceApiWrapper,
        catappult_api: CatappultApiWrapper,
    ):
        self.__binance_api = binance_api
        self.__catappult_api = catappult_api

    def get_last_24h_stats(self) -> Optional[Binance24hStats]:
        response = self.__binance_api.get_24h_ticker_stats("APPCBTC")
        if response.status == HTTPStatus.OK:
            return response.binance_24h_stats
        return None

    def get_last_price(self, to: str) -> Optional[float]:
        response = self.__catappult_api.get_current_price("APPC", to)
        if response.status == HTTPStatus.OK:
            return response.current_price
        return None
