from unittest.mock import Mock, patch
from src.clients.base_client import BaseClient


@patch("src.clients.base_client.requests.get")
def test_get_calls_requests_with_correct_url_and_timeout(mock_get):
    expected_response = Mock()
    mock_get.return_value = expected_response

    client = BaseClient(
        base_url="https://example.com",
        timeout=5
    )

    response = client.get("/products")

    mock_get.assert_called_once_with(
        "https://example.com/products",
        timeout=5
    )

    assert response is expected_response

@patch("src.clients.base_client.requests.post")
def test_post_calls_requests_with_correct_url_payload_and_timeout(
    mock_post
):
    expected_response = Mock()
    mock_post.return_value = expected_response

    client = BaseClient(
        base_url="https://example.com",
        timeout=5
    )

    payload = {
        "title" : "Test Product",
        "price" : 99.99,
        "stock" : 10 
    }

    response = client.post("/products/add", payload)

    mock_post.assert_called_once_with(
        "https://example.com/products/add",
        json=payload,
        timeout=5
    )

    assert response is expected_response

@patch("src.clients.base_client.requests.put")
def test_put_calls_requests_with_correct_url_payload_and_time(
    mock_put
): 
    expected_response = Mock()
    mock_put.return_value = expected_response

    client = BaseClient(
        base_url="https://example.com",
        timeout=5
    )

    payload = {
        "title" : "Updated product",
        "price" : 149.99
    }

    response = client.put("/products/1", payload)

    mock_put.assert_called_once_with(
        "https://example.com/products/1",
        json=payload,
        timeout=5
    )

    assert response is expected_response


@patch("src.clients.base_client.requests.delete")
def test_delete_calls_requests_with_correct_url_and_time(
    mock_delete
): 
    expected_response = Mock()
    mock_delete.return_value = expected_response

    client = BaseClient(
        base_url="https://example.com",
        timeout=5
    )

    response = client.delete("/products/1")

    mock_delete.assert_called_once_with(
        "https://example.com/products/1",
        timeout=5
    ) 

    assert response is expected_response