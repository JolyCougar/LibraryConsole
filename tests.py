import unittest
import os
import json
from unittest import mock
from library import Library
from models import Book



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
        """Тестирование удаления несуществующей книги."""
        with mock.patch('builtins.print') as mocked_print:
            self.library.delete_book(999)
            mocked_print.assert_called_once_with("Книги с таким ID не найдено")
