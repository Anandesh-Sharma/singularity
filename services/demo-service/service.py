from typing import List

from core.service import Base

from .model import Item as ItemModel
from .schemas import Item, ItemRead


class Service(Base):
    async def post(self, item: Item) -> ItemRead:
        item = ItemModel(
            name=item.name, description=item.description, price=item.price, tax=item.tax
        )

        await item.create()
        return item

    async def get(self, id: str) -> List[ItemRead]:
        # item = await ItemModel.read(id)
        items = await ItemModel.read_all(name="MatchBox")
        return items

    async def delete(self, id: str) -> ItemRead:
        item = await ItemModel.read(id)
        await item.delete()
        return item
