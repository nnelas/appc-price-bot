from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional


@dataclass(frozen=True)
class CatappultApiResponse:
    status: HTTPStatus
    current_price: Optional[float] = None
