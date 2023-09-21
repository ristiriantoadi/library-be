from models.default.base import DefaultModel


class Book(DefaultModel):
    title: str
    isbn: str
    author: str
    publicationYear: int
    publisher: str
    category: str
    stock: int
    cover: str
