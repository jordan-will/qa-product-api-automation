from dataclasses import dataclass


@dataclass
class Product:
    id: int
    title: str
    price: float
    stock: int