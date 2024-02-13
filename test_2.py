class Book:
    def __init__(self, title=None, author=None, year=None):
        self.author = author
        self.year = year
        self.title = title

    def display(self):
        if self.author is None and self.year is None:
            return print(f'{self.title:<30}')
        elif self.author is None:
            return print(f'{self.title:<30}{"":<20}{self.year:>5}')
        elif self.year is None:
            return print(f'{self.title:<30}{self.author:<20}')
        else:
            return print(f'{self.title:<30}{self.author:<20}{self.year:>5}')


class Library:
    def __init__(self, name_library, *books: Book):
        self.list_book = list(books)
        self.name = name_library

    def list(self):
        print(self.name)
        self.print_table()
        for book in self.list_book:
            book.display()

    def filter(self, title=None, author=None, year=None):
        result = []
        for i in self.list_book:
            if (title is None or i.title == title) and (author is None or i.author == author) and (
                    year is None or i.author == author):
                result.append(i)

        return result

    def add_book(self, new_book):
        self.list_book.append(new_book)

    def delete_book(self, name_book):
        self.list_book.remove(name_book)

    @staticmethod
    def print_table():
        print(f"{'Название':<30}{'Автор':<20}{'Год':>5}")

    @staticmethod
    def as_table(book):
        Library.print_table()
        for i in book:
            i.display()


book_1 = Book('Чистый код', 'Дядя Боб', year=2017)

book_2 = Book('От 2 до 5', 'Корней Чуковский', 1958)

book_3 = Book('Идеальный программист', 'Дядя Боб', 2018)

book_4 = Book('Рецепты татарской кухни', year=2018)

library = Library('Домашняя библиотека')

library.add_book(book_1)

library.add_book(book_2)

library.add_book(book_3)

library.add_book(book_4)

library.list()

