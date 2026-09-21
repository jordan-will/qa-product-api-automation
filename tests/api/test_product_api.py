from src.validators.response_validator import(
    validate_json_structure,
    validate_required_fields,
    validate_status_code
)

from src.validators.product_validator import validate_product

def test_get_products_returns_valid_prodduct_list(product_client):
    response = product_client.get_products()

    validate_status_code(response, 200)

    data = response.json()

    validate_json_structure(data, dict)

    validate_required_fields(
        data,
        ["products", "total", "skip", "limit"]
    )

    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0

def test_get_products_return_valid_products(product_client):
    response = product_client.get_products()

    validate_status_code(response, 200)

    data = response.json()

    validate_required_fields(
        data,
        ["products"]
    )

    validate_json_structure(
        data["products"],
        list
    )

    assert len(data["products"]) > 0

    for product in data["products"]:
        validate_product(product)

def test_target_product_returns_valid_products(product_client):
    product = product_client.get_product(1)

    assert product.id == 1
    assert isinstance(product.title, str)
    assert isinstance(product.price, float)
    assert isinstance(product.stock, int)

    assert product.price > 0
    assert product.stock >= 0

def test_get_nonexistent_product_returns_not_found(product_client):
    response = product_client.base_client.get("/products/99999")

    validate_status_code(response, 404)

def test_create_product_returns_created_product(
        product_client,
        valid_product_payload
): 
    response = product_client.create_product(
        valid_product_payload
    )

    validate_status_code(response, 201)

    data = response.json()

    validate_product(data)

    assert data["title"] == valid_product_payload["title"]
    assert data["price"] == valid_product_payload["price"]
    assert data["stock"] == valid_product_payload["stock"]

def test_update_product_returns_updated_product(product_client):
    payload = {
        "title" : "Update QA Product",
        "price" : 149.99
    }

    response = product_client.update_product(
        1,
        payload
    )

    data = response.json()

    validate_product(data)

    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["price"] == payload["price"]

def test_delete_product_returns_deleted_product(product_client):
    response = product_client.delete_product(1)

    validate_status_code(response, 200)

    data = response.json()

    validate_product(data)

    assert data["id"] == 1
    assert data["isDeleted"] is True
    assert "deletedOn" in data