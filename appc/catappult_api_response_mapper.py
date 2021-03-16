from http import HTTPStatus

import requests

from appc.catappult_api_response import CatappultApiResponse


class CatappultApiResponseMapper:
    def __init__(self):
        pass

    def map(self, response: requests.Response) -> CatappultApiResponse:
        if response.status_code == HTTPStatus.OK:
            return CatappultApiResponse(HTTPStatus.OK, float(response.json()["value"]))
        return CatappultApiResponse(HTTPStatus.BAD_REQUEST)
