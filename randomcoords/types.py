from typing import Optional, TypedDict, List, Dict


class RandomCoordsApiError(Exception):
    def __init__(self, message: str, status_code: int, url: str):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.url = url


class RegionsResponse(TypedDict):
    type: str
    results: int
    data: List[Dict[str, str]]


class CountriesResponse(TypedDict):
    type: str
    results: int
    data: List[Dict[str, str]]


class Coordinate(TypedDict):
    uid: str
    id: str
    country: str
    city: str
    iso2: str
    coordinates: List[float]
    state: Optional[str]


class RegionCoordinatesResponse(TypedDict):
    id: str
    name: str
    type: str
    results: int
    data: List[Coordinate]


class CountryCoordinate(TypedDict):
    uid: str
    city: str
    state: Optional[str]
    coordinates: List[float]


class CountryCoordinatesResponse(TypedDict):
    id: str
    name: str
    type: str
    iso2: str
    regions: List[str]
    results: int
    data: List[CountryCoordinate]


class Config(TypedDict, total=False):
    api_token: str
    base_url: str
    timeout: float


class CoordinatesOptions(TypedDict, total=False):
    limit: int
