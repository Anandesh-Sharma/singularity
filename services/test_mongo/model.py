from singularity.db.mongo import BaseModel


class TestModel(BaseModel):
    name: str
    age: int
    address: str
    email: str
    phone: str

    class Settings:
        indexes = ["name", "email"]
