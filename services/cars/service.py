from core.service import Base
from services.cars.model import CarModel
from services.cars.schemas import Car, CarRead


class Service(Base):
    async def post(self, car: Car) -> CarRead:
        new_car = CarModel(
            name=car.name, description=car.description, price=car.price, tax=car.tax
        )
        await new_car.create()
        return new_car

    async def get(self, id: str) -> CarRead:
        car = await CarModel.read(id)
        return car

    async def delete(self, id: str) -> CarRead:
        car = await CarModel.read(id)
        await car.delete()
        return car
