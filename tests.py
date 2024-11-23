import unittest
import os
import json
from unittest import mock
from library import Library
from models import Book, LibraryFile


class TestBook(unittest.TestCase):
    def setUp(self):
        """ Создание экземпляра книги для тестов."""
        self.book = Book(id=1, title="Test Title", author="Test Author", year=2023, status="В наличии")

    def test_initialization(self):
        """ Тестирование инициализации книги. """
        self.assertEqual(self.book.id, 1)
        self.assertEqual(self.book.title, "Test Title")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.year, 2023)
        self.assertEqual(self.book.status, "В наличии")

    def test_to_dict(self):
        """ Тестирование метода to_dict."""
        expected_dict = {
            "id": 1,
            "title": "Test Title",
            "author": "Test Author",
            "year": 2023,
            "status": "В наличии"
        }
        self.assertEqual(self.book.to_dict(), expected_dict)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создание экземпляра библиотеки для тестов."""
        self.library = Library()
        self.library.library.library = {}
        self.test_filename = "test.json"
        self.library.library.filename = self.test_filename

    def tearDown(self):
        """Удаление тестового файла после тестов."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_book(self):
        """ Тест на добавление книги и проверка на то что книга сохранилась в файле JSON """
        self.library.add_book(title_book="Test_title",
                              author_book="Test_author",
                              year_book=2024)
        self.assertEqual(len(self.library.library.lib()), 1)
        book = self.library.library.lib()[1]
        self.assertEqual(book.title, "Test_title")
        self.assertEqual(book.author, "Test_author")
        self.assertEqual(book.year, 2024)
        self.assertEqual(book.status, "В наличии")

        self.assertTrue(os.path.exists(self.test_filename))

        with open(self.test_filename, mode="r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertIn("1", data)
            self.assertEqual(data["1"]["title"], "Test_title")
            self.assertEqual(data["1"]["author"], "Test_author")
            self.assertEqual(data["1"]["year"], 2024)
            self.assertEqual(data["1"]["status"], "В наличии")

    def test_delete_book(self):
        """ Тестирование удаления книги """
        self.library.add_book(title_book="Test_title",
                              author_book="Test_author",
                              year_book=2024)
        self.assertEqual(len(self.library.library.lib()), 1)
        self.library.delete_book(1)
        self.assertEqual(len(self.library.library.lib()), 0)
        with open(self.test_filename, mode="r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertNotIn("1", data)

    def test_delete_nonexistent_book(self):
        """ Тестирование удаления несуществующей книги. """
        with mock.patch('builtins.print') as mocked_print:
            self.library.delete_book(999)
            mocked_print.assert_called_once_with("Книги с таким ID не найдено")

    def test_search_book_by_author(self):
        """ Тестирование поиска книги по автору. """
        self.library.add_book("Tests_title", "Tests_author", 1949)
        with mock.patch('builtins.print') as mocked_print:
            self.library.search_book("Tests_author")
            mocked_print.assert_called_once_with(f"Ваша книга найдена!\n ID книги 1\n Ее автор: Tests_author,\n "
                                                 f"название Tests_title,\n год: 1949,\n состояние: В наличии\n")

    def test_search_nonexistent_book(self):
        """ Тестирование поиска несуществующей книги. """
        self.library.add_book("Tests_title", "Tests_author", 1949)
        with mock.patch('builtins.print') as mocked_print:
            self.library.search_book("Неизвестная книга")
            mocked_print.assert_called_once_with("К сожалению ваша книга не найдена! =(")

    def test_search_book_with_empty_library(self):
        """ Тестирование поиска книги с пустой библиотекой. """
        with mock.patch('builtins.print') as mocked_print:
            self.library.search_book("Неизвестная книга")
            mocked_print.assert_called_once_with('В библиотеке нет не одной книги')

    def test_view_books(self):
        """ Тестирование просмотра всех книг в библиотеке. """
        self.library.add_book("Test_title_1", "Test_author_1", 2021)
        self.library.add_book("Test_title_2", "Test_author_2", 2022)

        with mock.patch('builtins.print') as mocked_print:
            self.library.view_books()
            mocked_print.assert_any_call("Книга ID: 1,\n Автор: Test_author_1,\n Название: Test_title_1,\n "
                                         "Год выпуска: 2021,\n Статус: В наличии\n")
            mocked_print.assert_any_call("Книга ID: 2,\n Автор: Test_author_2,\n Название: Test_title_2,\n "
                                         "Год выпуска: 2022,\n Статус: В наличии\n")

    def test_view_books_with_empty_library(self):
        """ Тестирование просмотра всех книг в пустой библиотеке. """
        with mock.patch('builtins.print') as mocked_print:
            self.library.view_books()
            mocked_print.assert_any_call("Библиотека пустая, Добавьте новые книги!")

    def test_change_status(self):
        """ Тестирование изменения статуса книги. """
        self.library.add_book("Test_title", "Test_author", 2024)
        self.library.change_status(1)
        book = self.library.library.lib()[1]
        self.assertEqual(book.status, "Выдана")

        self.library.change_status(1)
        book = self.library.library.lib()[1]
        self.assertEqual(book.status, "В наличии")

    def test_change_status_nonexistent_book(self):
        """ Тестирование изменения статуса несуществующей книги. """
        with mock.patch('builtins.print') as mocked_print:
            self.library.change_status(999)
            mocked_print.assert_called_once_with("Книги с таким ID не найдено проверьте ID и попробуйте снова")


class TestLibraryFile(unittest.TestCase):
    def setUp(self):
        """ Создание экземпляра библиотеки для тестов. """
        self.test_filename = "test_library.json"
        self.library_file = LibraryFile(filename=self.test_filename)
        self.library_file.library = {}

    def tearDown(self):
        """ Удаление тестового файла после тестов. """
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_load_books(self):
        """ Тестирование загрузки книг из файла JSON. """
        test_data = {
            "1": {"id": "1", "title": "Test Title", "author": "Test Author", "year": 2023, "status": "В наличии"}
        }
        with open(self.test_filename, mode="w", encoding="utf-8") as file:
            json.dump(test_data, file, ensure_ascii=False, indent=4)

        library_file = LibraryFile(filename=self.test_filename)
        self.assertEqual(len(library_file.lib()), 1)
        book = library_file.lib()[1]
        self.assertEqual(book.title, "Test Title")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.status, "В наличии")

    def test_save_books(self):
        """ Тестирование сохранения книг в файл JSON. """
        self.library_file.library[1] = Book(1, "Test Title", "Test Author", 2023, "В наличии")
        self.library_file.save_books()

        with open(self.test_filename, mode="r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertIn("1", data)
            self.assertEqual(data["1"]["title"], "Test Title")
            self.assertEqual(data["1"]["author"], "Test Author")
            self.assertEqual(data["1"]["year"], 2023)
            self.assertEqual(data["1"]["status"], "В наличии")

    def test_lib(self):
        """ Тестирование метода lib. """
        self.library_file.library[1] = Book(1, "Test Title", "Test Author", 2023, "В наличии")
        self.assertEqual(len(self.library_file.lib()), 1)
        self.assertEqual(self.library_file.lib()[1].title, "Test Title")
        self.assertEqual(self.library_file.lib()[1].author, "Test Author")
