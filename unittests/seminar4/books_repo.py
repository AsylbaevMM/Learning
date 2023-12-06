from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Book:
    id: int
    title: str
    author: str


class BookRepository:
    def __init__(self, books: list[Book] = None):
        self._books = books
        if books is None:
            self._books = []

    def find_by_id(self, book_id: int) -> Book:
        return [*filter(lambda x: x.id == book_id, self._books)][0]

    def find_all(self) -> list[Book]:
        return deepcopy(self._books)