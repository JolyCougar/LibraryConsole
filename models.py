import os
import json
from typing import Dict


class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str):
        """
        Инициализация книги.

        :param id: Уникальный идентификатор книги.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год выпуска книги.
        :param status: Статус книги (например, "В наличии", "Выдана").
        """

        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """
        Преобразование книги в словарь для сохранения в JSON.

        :return: Словарь, представляющий книгу.
        """

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    def __str__(self) -> str:
        """
        Строковое представление книги

        :return: Строка, содержащая автора и название книги.
        """

        return f"{self.author} {self.title}"

    def __repr__(self) -> str:
        """
        Представление книги для отладки.

        :return: Строка, содержащая автора и название книги.
        """

        return self.__str__()


class LibraryFile:
    def __init__(self, filename: str = "library.json"):
        """
        Инициализация библиотеки с указанием файла.

        :param filename: Имя файла для хранения данных о книгах (по умолчанию "library.json").
        :param self.library: Загрузка уже созданных книг и файла.
        """

        self.filename = filename
        self.library = self.load_books()

    def load_books(self) -> Dict[int, Book]:
        """
        Загрузка книг из JSON файла
        :return: Словарь, где ключи — это ID книг, а значения — объекты Book.
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, mode="r", encoding="utf-8") as file:
                    data_f = json.load(file)
                    return {int(data): Book(**data_f[data]) for data in data_f}
            except (json.JSONDecodeError, FileNotFoundError):
                return {}
        return {}

    def save_books(self) -> None:
        """
        Сохранение книг в файле JSON
        """
        with open(self.filename, mode="w", encoding="utf-8") as file:
            json.dump({book: self.library[book].to_dict() for book in self.library}, file, ensure_ascii=False, indent=4)

    def lib(self) -> Dict[int, Book]:
        """
        Получение библиотеки книг.

        :return: Словарь, где ключи — это ID книг, а значения — объекты Book.
        """

        return self.library
