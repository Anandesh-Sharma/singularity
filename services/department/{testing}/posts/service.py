class Service:
    def post(self, testing: int, title: str, content: str):
        return {
            "status": True,
            "title": title,
            "content": content,
        }
