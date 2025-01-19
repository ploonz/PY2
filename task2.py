BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен относиться к типу int")
        if not id_ > 0:
            raise ValueError("Идентификатор не может быть отрицательным")
        self.id_ = id_
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть строкой")
        if not len(name) >= 0:
            raise ValueError("Книга должна иметь название")
        self.name=name
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно относитья к типу int")
        if not pages >= 0:
            raise ValueError("Кол-во страниц не может быть отрицательным")
        self.pages=pages


# TODO написать класс Library
class Library:
    def __init__(self, books: list[Book]=[]):
        if not isinstance(books, list):
            raise TypeError("Список книг должен иметь тип данных \"список\"")
        self.books = books
    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return len(self.books)+1
    def get_index_by_book_id(self,id:int):
        for index,item in enumerate(self.books):
            if id == item.id_:
                return index



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
