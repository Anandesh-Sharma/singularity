from typing import Any, List

class Service:
    async def get(self):
        return {"status": True, "message": "Toyota get has been created"}