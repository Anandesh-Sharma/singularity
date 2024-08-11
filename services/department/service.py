class Service:
    def post(self, payload: str):
        return {
            "status": True,
            "message": "hello from post method of department service",
        }
