import requests
from requests import Response

from config.settings import BASE_URL, TIMEOUT


class BaseClient:
    def __init__(
        self,
        base_url: str = BASE_URL,
        timeout: int = TIMEOUT,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, endpoint: str) -> Response:
        return requests.get(
            self._build_url(endpoint),
            timeout=self.timeout,
        )

    def post(self, endpoint: str, data: dict) -> Response:
        return requests.post(
            self._build_url(endpoint),
            json=data,
            timeout=self.timeout,
        )

    def put(self, endpoint: str, data: dict) -> Response:
        return requests.put(
            self._build_url(endpoint),
            json=data,
            timeout=self.timeout,
        )

    def delete(self, endpoint: str) -> Response:
        return requests.delete(
            self._build_url(endpoint),
            timeout=self.timeout,
        )

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"