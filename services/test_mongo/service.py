from typing import Any, List

from singularity.service import Base

from .model import TestModel


class Service(Base):
    async def get(
        self, name: str, page: int, size: int
    ) -> TestModel | List[TestModel] | None | List:
        # return await TestModel.get(id)
        return await TestModel.list({"name": name}, page=page, size=size)

    async def post(self):
        person = await TestModel(
            name="Anandesh",
            age=25,
            address="Kathmandu",
            email="anandeshsharma@gmail.com",
            phone="9841234567",
        ).insert()

        return {
            "status": True,
            "message": f"test has been created with id {person.id}",
        }

    async def delete(self, id: str) -> Any:
        data = await TestModel.find({"_id": id})
        print(data)
        await data.delete()
        return {"status": True, "message": "Test has been deleted"}
