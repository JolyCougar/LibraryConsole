from models import LibraryFile, Book


class Library:
    def __init__(self):
        """ Инициализация библиотеки """
        self.library = LibraryFile()

    def add_book(self, title_book: str, author_book: str, year_book: int) -> None:
        """
        Добавление новой книги в библиотеку

        :param title_book: Название книги.
        :param author_book: Автор книги.
        :param year_book: Год выпуска книги.
        """
        if len(self.library.lib()) == 0:
            count = 1
        else:
            count = max(self.library.lib()) + 1
        self.library.lib()[count] = Book(count, title_book, author_book, year_book, "В наличии")
        self.library.save_books()

    def delete_book(self, book_id: int) -> None:
        """
        Удаление книги из библиотеки

        :param book_id: Уникальный идентификатор книги для удаления.
        """
        try:
            self.library.lib().pop(book_id)
            self.library.save_books()
        except KeyError:
            print("Книги с таким ID не найдено")

    def search_book(self, query: str) -> None:
        """
        Поиск книги по ID, названию или автору.

        :param query: Запрос для поиска (может быть год, название или автор книги).
        """
        result = None
        for book in self.library.lib().values():
            if query.isdigit():
                if book.year == int(query):
                    result = book
                    print(f"Ваша книга найдена!\n ID книги {book.id}\n Ее автор: {book.author},\n "
                          f"название {book.title},\n год: {book.year},\n состояние: {book.status}\n")
            else:
                if book.title == query or book.author == query:
                    result = book
                    print(f"Ваша книга найдена!\n ID книги {book.id}\n Ее автор: {book.author},\n "
                          f"название {book.title},\n год: {book.year},\n состояние: {book.status}\n")
            if not result:
                print("К сожалению ваша книга не найдена! =(")

    def view_books(self) -> None:
        """
        Просмотр всех книг в библиотеке
        """
        if self.library:
            for x in self.library.lib().values():
                print(f"Книга ID: {x.id},\n Автор: {x.author},\n Название: {x.title},\n "
                      f"Год выпуска: {x.year},\n Статус: {x.status}\n")
        else:
            print("Библиотека пустая, Добавьте новые книги!")

    def change_status(self, book_id: int) -> None:
        """
        Смена статуса книги

        :param book_id: Уникальный идентификатор книги для удаления.
        """
        try:
            book = self.library.lib()[book_id]
            if book.status == "Выдана":
                book.status = "В наличии"
            else:
                book.status = "Выдана"
            print(f"Состояние книги с ID {book_id} успешно изменено")
            self.library.save_books()
        except KeyError:
            print("Книги с таким ID не найдено проверьте ID и попробуйте снова")
