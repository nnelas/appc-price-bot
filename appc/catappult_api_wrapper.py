from http import HTTPStatus

import requests

from appc.catappult_api_response import CatappultApiResponse
from appc.catappult_api_response_mapper import CatappultApiResponseMapper


class CatappultApiWrapper:
    def __init__(
        self,
        base_host: str,
        catappult_api_response_mapper: CatappultApiResponseMapper,
        timeout: int = 5,
    ):
        self.__base_host = base_host
        self.__timeout = timeout
        self.__catappult_api_response_mapper = catappult_api_response_mapper

    def get_current_price(self, symbol: str, to: str) -> CatappultApiResponse:
        try:
            url = (
                self.__base_host
                + "/broker/8.20180518/exchanges/"
                + symbol
                + "/convert/1"
            )
            params = {"to": to}
            response = requests.get(url, params=params, timeout=self.__timeout)
            return self.__catappult_api_response_mapper.map(response)
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.ReadTimeout,
        ):
            return CatappultApiResponse(HTTPStatus.INTERNAL_SERVER_ERROR)
