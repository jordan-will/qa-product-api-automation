from requests import Response

from src.clients.base_client import BaseClient
from src.models.product import Product


class ProductClient:
    def __init__(self, base_client: BaseClient) -> None:
        self.base_client = base_client

    def get_products(self) -> Response:
        return self.base_client.get("/products")

    def get_product(self, product_id: int) -> Product:
        response = self.base_client.get(f"/products/{product_id}")
        data = response.json()

        return Product(
            id=data["id"],
            title=data["title"],
            price=data["price"],
            stock=data["stock"],
        )

    def create_product(self, data: dict) -> Response:
        return self.base_client.post(
            "/products/add",
            data,
        )

    def update_product(
        self,
        product_id: int,
        data: dict,
    ) -> Response:
        return self.base_client.put(
            f"/products/{product_id}",
            data,
        )

    def delete_product(self, product_id: int) -> Response:
        return self.base_client.delete(
            f"/products/{product_id}"
        )