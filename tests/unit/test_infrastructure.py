from config.settings import BASE_URL, TIMEOUT
from src.clients.base_client import BaseClient
from src.clients.product_client import ProductClient


def test_settings_fixture(settings_fixture):
    assert settings_fixture["base_url"] == BASE_URL
    assert settings_fixture["timeout"] == TIMEOUT


def test_base_client_fixture(base_client):
    assert isinstance(base_client, BaseClient)
    assert base_client.base_url == BASE_URL
    assert base_client.timeout == TIMEOUT


def test_product_client_fixture(product_client):
    assert isinstance(product_client, ProductClient)
    assert isinstance(product_client.base_client, BaseClient)


def test_products_data_fixture(products_data):
    assert isinstance(products_data, list)
    assert len(products_data) > 0

    for product in products_data:
        assert isinstance(product, dict)
        assert "id" in product
        assert "title" in product
        assert "price" in product
        assert "stock" in product


def test_valid_product_payload_fixture(valid_product_payload):
    assert valid_product_payload["title"] == "QA Automation Product"
    assert valid_product_payload["price"] == 99.99
    assert valid_product_payload["stock"] == 100