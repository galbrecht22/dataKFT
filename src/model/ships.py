from dataclasses import dataclass


@dataclass
class ShipSchema:
    id: int
    brand: str
    model: str
    length: str
    length_dim: str
    year: str
    price: str
    currency: str
