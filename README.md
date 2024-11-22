# LibraryConsole

Это консольное приложение для управления библиотекой книг.
Оно позволяет добавлять, удалять, искать и просматривать книги,
а также изменять их статус (например, "В наличии" или "Выдана").
Также приложение сохраняет добавленные книги в файл формата JSON,
и загружает его при запуске,подгружая добавленные ранее кники<br>

## Функционал

Приложение предоставляет следующие функции:

- **Добавить книгу**: Позволяет пользователю ввести название, автора и год выпуска книги, после чего книга добавляется в библиотеку.
- **Удалить книгу**: Удаляет книгу из библиотеки по уникальному идентификатору (ID).
- **Искать книгу**: Позволяет искать книгу по ID, названию или автору. Если книга найдена, отображаются ее детали.
- **Просмотреть все книги**: Выводит список всех книг в библиотеке с их деталями, включая ID, автора, название, год выпуска и статус.
- **Изменить статус книги**: Позволяет изменять статус книги (например, с "В наличии" на "Выдана" и наоборот) по уникальному идентификатору.
- **Выход**: Завершает работу приложения.


## Установка используя скомпилированные файлы:
1. [Скачать файлы](https://github.com/JolyCougar/LibraryConsole/releases/tag/pre_release) для вашей системы(Windows или Linux)
2. Для Windows достаточно распаковать архив и запустить
3. Для Linux необходимо расспаковать архив, запустить терминал пройти в директорию куда вы расспаковали архив и запустить файл **!Обязательно через терминал иначе ничего не произойдет!**

## Установка используя исходный код:
1. Скачать и установить Python с [оффициального сайта](https://www.python.org/downloads/release/python-3122/) (если он не установлен)<br>
  1.2. Для этого в конце страницы в пункте "Files" выбираем и скачиваем файл в соответствии с вашей Операционной системой.<br>
  1.3. Запускаем скачанный файл и следуем указаниям мастера по установке.<br>
2. Скачиваем приложение:<br>
  2.1(а). Если у вас установлен [Git](https://git-scm.com/downloads) в терминале вводим команду `git clone https://github.com/JolyCougar/LibraryConsole.git`<br>
  2.1(б). Если у вас не установлен Git, то можно скачать файлы с [репозитория](https://github.com/JolyCougar/LibraryConsole/archive/refs/heads/main.zip) архивом<br>
3. Если вы использвали п.п. 2.1(б). ,тогда распакуйте архив в удобную для вас директорию.<br>
4. Дальше запускаем терминал(командная строка) и переходим(в зависимости от вашей Операционной системы) в директорию с проектом.<br>
   <br>Например(Windows) :<br>
   `
   cd c:/LibraryConsole
   `<br>
   <br>Пример(Linux):<br>
   `
   cd Загрузки/LibraryConsole
   `<br>
   
5. Дальше вводим команду:<br>
   Windows: `python ./main.py`<br>
   Linux: `python3 ./main.py`<br>
6. Приложение запущенно<br>
7. Для завершенния работы приложения выберете пунк 6 в меню приложения
