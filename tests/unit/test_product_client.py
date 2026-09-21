from unittest.mock import Mock
from src.clients.product_client import ProductClient
from src.models.product import Product

def test_get_products_calls_base_client():
    base_client = Mock()
    expected_response = Mock()
    base_client.get.return_value = expected_response

    client = ProductClient(base_client)

    response = client.get_products()

    base_client.get.assert_called_once_with("/products")

    assert response is expected_response

def test_create_product_calls_base_client():
    base_client = Mock()
    expected_response = Mock()
    base_client.post.return_value = expected_response

    client = ProductClient(base_client)

    payload = {
        "title" : "Test Product",
        "price" : 99.99,
        "stock" : 10
    }

    response = client.create_product(payload)

    base_client.post.assert_called_once_with(
        "/products/add",
        payload
    )

    assert response is expected_response

def test_update_product_calls_base_client():
    base_client = Mock()
    expected_response = Mock()
    base_client.put.return_value = expected_response

    client = ProductClient(base_client)

    payload  = {
        "title" : "Update Product",
        "price" : 149.99
    }

    response = client.update_product(1, payload)

    base_client.put.assert_called_once_with(
        "/products/1",
        payload
    )

    assert response is expected_response

def test_delete_product_calls_base_client():
    base_client = Mock()
    expected_response = Mock()
    base_client.delete.return_value = expected_response

    client = ProductClient(base_client)

    response  = client.delete_product(1)

    base_client.delete.assert_called_once_with(
        "/products/1"
    )

    assert response is expected_response

def test_get_produtc_transform_json_into_product():
    base_client = Mock()
    response = Mock()

    response.json.return_value = {
        "id" : 1,
        "title" : "Example Product",
        "price" : 99.99,
        "stock" : 20
    }

    base_client.get.return_value = response

    client = ProductClient(base_client)
    product = client.get_product(1)

    base_client.get.assert_called_once_with("/products/1")
    assert isinstance(product, Product)

def test_get_product_maps_json_fields_correctly():
    base_client = Mock()
    response = Mock()

    response.json.return_value = {
        "id" : 42,
        "title" : "Test Product",
        "price" : 149.99,
        "stock" : 35
    }

    base_client.get.return_value = response

    client = ProductClient(base_client)

    product = client.get_product(42)

    assert product.id == 42
    assert product.title == "Test Product"
    assert product.price == 149.99
    assert product.stock == 35