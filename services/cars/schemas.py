import enum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class CarType(enum.Enum):
    SUV = "suv"
    Sedan = "sedan"
    Hatchback = "hatchback"


class Car(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: Annotated[str, Field(min_length=2, max_length=30, examples=["Pineapple"])]
    description: str | None = Annotated[
        str, Field(min_length=1, max_length=63206, examples=["This is the description"])
    ]
    price: float = Annotated[float, Field(gt=0, examples=[100.02, 200.40, 300.50])]
    tax: float | None = None
    fuel: str
    power: float
    type: CarType


class CarRead(BaseModel):
    name: str
    description: str | None
    price: int
    tax: float | None
    fuel: str
    power: float
    type: CarType
