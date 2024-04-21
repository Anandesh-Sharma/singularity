import sys

sys.path.append("/Users/hash/work/personal/singularity")
# import asyncio

from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from core.db.postgres.models import CRUD

# base = declarative_base()


class Item(CRUD):
    __tablename__ = "items"

    name: Mapped[str] = mapped_column(String(30), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(63206), nullable=True)
    tax: Mapped[float] = mapped_column(Float, nullable=True)
