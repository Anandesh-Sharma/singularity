import enum

from sqlalchemy import Enum, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

# from sqlalchemy.types import Enum as SqlAlchemyEnum
# from sqlalchemy.types import Float, Integer, String
from singularity.db.postgres.models import CRUD


class CarType(enum.Enum):
    SEDAN = "SEDAN"
    SUV = "SUV"
    HATCHBACK = "HATCHBACK"


class CarModel(CRUD):
    __tablename__ = "cars"

    name: Mapped[str] = mapped_column(String(30), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(63206), nullable=True)
    tax: Mapped[float] = mapped_column(Float, nullable=True)
    fuel: Mapped[str] = mapped_column(String(10), nullable=False)
    power: Mapped[str] = mapped_column(Float, nullable=False)
    type: Mapped[CarType] = mapped_column(Enum(CarType, name="cartype"), nullable=False)
