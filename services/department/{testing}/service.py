class Service:
    def get(self, testing: int, skip: int = 0, limit: int = 10):
        return {
            "status": True,
            "testing": testing,
            "skip": skip,
            "limit": limit,
        }
