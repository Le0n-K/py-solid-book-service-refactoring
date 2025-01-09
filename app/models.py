class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def __str__(self):
        return self.title

    @staticmethod
    def validate_book(title: str, content: str):
        if not title or not content:
            raise ValueError("Both title and content must be provided and non-empty.")

    def save(self):
        self.validate_book(self.title, self.content)
        return self
