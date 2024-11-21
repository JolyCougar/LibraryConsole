from library import Library


def main():
    library = Library()

    while True:
        print("\nВыберите действие:\n"
              "1. Добавить книгу\n"
              "2. Удалить книгу\n"
              "3. Искать книгу\n"
              "4. Просмотреть все книги\n"
              "5. Изменить статус книги\n"
              "6. Выход\n")

        choice = input("Введите номер действия:")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год выпуска книги: "))
            library.add_book(title, author, year)

            print("Книга добавлена.")

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.delete_book(book_id)

        elif choice == "3":
            query = input("Введите год, название или автора книги для поиска: ")
            library.search_book(query)

        elif choice == "4":
            library.view_books()

        elif choice == "5":
            book_id = int(input("Введите ID книги для изменения статуса: "))
            library.change_status(book_id)

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите действие от 1 до 6.\n")


if __name__ == "__main__":
    main()
