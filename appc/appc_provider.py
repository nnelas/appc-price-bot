from appc.appc_price_repository import AppcPriceRepository
from appc.binance_api_response_mapper import BinanceApiResponseMapper
from appc.binance_api_wrapper import BinanceApiWrapper
from appc.catappult_api_response_mapper import CatappultApiResponseMapper
from appc.catappult_api_wrapper import CatappultApiWrapper


class AppcProvider:
    def __init__(self):
        self.__binance_api_wrapper = BinanceApiWrapper(
            "https://api.binance.com", BinanceApiResponseMapper()
        )
        self.__catappult_api_wrapper = CatappultApiWrapper(
            "https://api.catappult.io", CatappultApiResponseMapper()
        )

    def provide_appc_price_repository(self) -> AppcPriceRepository:
        return AppcPriceRepository(
            self.__binance_api_wrapper, self.__catappult_api_wrapper
        )


appc_provider = AppcProvider()
