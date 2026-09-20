import json
from pathlib import Path

import pytest

from config.settings import BASE_URL, TIMEOUT
from src.clients.base_client import BaseClient
from src.clients.product_client import ProductClient


@pytest.fixture(scope="session")
def settings_fixture() -> dict:
    return {
        "base_url": BASE_URL,
        "timeout": TIMEOUT,
    }


@pytest.fixture(scope="session")
def base_client(settings_fixture: dict) -> BaseClient:
    return BaseClient(
        base_url=settings_fixture["base_url"],
        timeout=settings_fixture["timeout"],
    )


@pytest.fixture(scope="session")
def product_client(base_client: BaseClient) -> ProductClient:
    return ProductClient(base_client)


@pytest.fixture(scope="session")
def products_data() -> list[dict]:
    data_path = Path(__file__).parent / "data" / "products.json"

    with data_path.open(encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def valid_product_payload() -> dict:
    return {
        "title": "QA Automation Product",
        "price": 99.99,
        "stock": 100,
    }