from singularity.service import Base

from .model import CarModel
from .schemas import Car, CarRead


class Service(Base):
    async def post(self, car: Car) -> CarRead:
        new_car = CarModel(**car.model_dump())
        await new_car.create()
        return new_car

    async def get(self, id: str) -> CarRead:
        car = await CarModel.read(id)
        return car

    async def delete(self, id: str) -> CarRead:
        car = await CarModel.read(id)
        await car.delete()
        return car
