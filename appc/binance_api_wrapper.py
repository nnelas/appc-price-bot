from http import HTTPStatus

import requests

from appc.binance_api_response import BinanceApiResponse
from appc.binance_api_response_mapper import BinanceApiResponseMapper


class BinanceApiWrapper:
    def __init__(
        self,
        base_host: str,
        binance_api_response_mapper: BinanceApiResponseMapper,
        timeout: int = 5,
    ):
        self.__base_host = base_host
        self.__binance_api_response_mapper = binance_api_response_mapper
        self.__timeout = timeout

    def get_24h_ticker_stats(self, symbol: str) -> BinanceApiResponse:
        try:
            url = self.__base_host + "/api/v3/ticker/24hr"
            params = {"symbol": symbol}
            response = requests.get(url, params=params, timeout=self.__timeout)
            return self.__binance_api_response_mapper.map(response)
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.ReadTimeout,
        ):
            return BinanceApiResponse(HTTPStatus.INTERNAL_SERVER_ERROR)
