"""
Класс Library - основная точка входа для работы с библиотекой
"""
from typing import Optional, List
from .book import Book, RegularBook, ReferenceBook, FictionBook
from .my_collections import BookCollection, IndexDict


class Library:
    """
    Основной класс библиотеки
    """
    
    def __init__(self, name: str = "Главная библиотека"):
        self.name = name
        self.books = BookCollection()
        self.indexes = IndexDict()
        self._create_initial_books()
    
    def _create_initial_books(self) -> None:
        """Создание начального набора книг разных типов"""
        initial_books = [
            # Обычные книги
            RegularBook("Война и мир", "Лев Толстой", 1869, "роман", "978-5-389-07435-1"),
            RegularBook("Преступление и наказание", "Федор Достоевский", 1866, "роман", "978-5-17-090665-5"),
            
            # Справочные книги
            ReferenceBook("Толковый словарь", "Владимир Даль", 1880, "словарь", "978-5-17-090689-1", "словарь"),
            ReferenceBook("Большая энциклопедия", "Коллектив авторов", 2005, "энциклопедия", "978-5-17-080185-2", "энциклопедия"),
            
            # Художественная литература
            FictionBook("Мастер и Маргарита", "Михаил Булгаков", 1967, "фэнтези", "978-5-17-067580-4", "проза"),
            FictionBook("1984", "Джордж Оруэлл", 1949, "антиутопия", "978-5-17-080115-9", "проза"),
            FictionBook("Гарри Поттер", "Джоан Роулинг", 1997, "фэнтези", "978-5-389-07429-0", "проза"),
        ]
        
        for book in initial_books:
            self.add_book(book, silent=True)
    
    def add_book(self, book: Book, silent: bool = False) -> bool:
        """Добавить книгу в библиотеку"""
        if book.isbn in self.indexes:
            if not silent:
                print(f"Книга с ISBN {book.isbn} уже существует")
            return False
        
        # Особые проверки для ReferenceBook
        if isinstance(book, ReferenceBook) and book.is_for_library_use_only():
            if not silent:
                print(f"Информация: {book.reference_type.capitalize()} '{book.title}' - только для использования в библиотеке")
        
        self.books.add(book)
        self.indexes.add_book(book)
        
        if not silent:
            print(f"Добавлена книга: {book}")
        
        return True
    
    def borrow_book(self, isbn: str) -> bool:
        """Выдать книгу с учетом ее типа"""
        book = self.indexes.get_book_by_isbn(isbn)
        if not book:
            print(f"Книга с ISBN {isbn} не найдена")
            return False
        
        # Проверка для справочников
        if isinstance(book, ReferenceBook) and book.is_for_library_use_only():
            print(f"Ошибка: {book.reference_type.capitalize()} '{book.title}' нельзя выдать на дом")
            return False
        
        if book.borrow():
            print(f"Выдана книга: {book.title}")
            print(f"Срок возврата: {book.get_loan_period()} дней")
            print(f"Можно продлить: {'да' if book.can_be_extended() else 'нет'}")
            return True
        else:
            print(f"Предупреждение: Книга '{book.title}' уже выдана")
            return False
    
    def get_books_by_type(self, book_type: type) -> List[Book]:
        """Получить книги определенного типа"""
        return [book for book in self.books if isinstance(book, book_type)]
    
    def print_books_by_type(self) -> None:
        """Вывести книги сгруппированные по типам"""
        print("\nКниги по типам:")
        print("-" * 50)
        
        regular_books = self.get_books_by_type(RegularBook)
        if regular_books:
            print("\nОбычные книги:")
            for book in regular_books:
                print(f"  - {book.title}")
        
        reference_books = self.get_books_by_type(ReferenceBook)
        if reference_books:
            print("\nСправочные книги:")
            for book in reference_books:
                print(f"  - {book.title} ({book.reference_type})")
        
        fiction_books = self.get_books_by_type(FictionBook)
        if fiction_books:
            print("\nХудожественная литература:")
            for book in fiction_books:
                print(f"  - {book.title} ({book.literary_genre})")
    
    def remove_book(self, isbn: str) -> bool:
        """Удалить книгу по ISBN"""
        book = self.indexes.get_book_by_isbn(isbn)
        if not book:
            print(f"Книга с ISBN {isbn} не найдена")
            return False
        
        self.books.remove(book)
        self.indexes.remove_book(book)
        print(f"Удалена книга: {book.title}")
        return True
    
    def return_book(self, isbn: str) -> bool:
        """Вернуть книгу"""
        book = self.indexes.get_book_by_isbn(isbn)
        if not book:
            print(f"Книга с ISBN {isbn} не найдена")
            return False
        
        if book.return_book():
            print(f"Возвращена книга: {book.title}")
            return True
        else:
            print(f"Предупреждение: Книга '{book.title}' не была выдана")
            return False
    
    def search_books(self, author: str = None, year: int = None, genre: str = None) -> BookCollection:
        """Поиск книг по параметрам"""
        results = []
        
        if author:
            results.extend(self.indexes.search_by_author(author))
        
        if year:
            if results:
                results = [book for book in results if book.year == year]
            else:
                results.extend(self.indexes.search_by_year(year))
        
        if genre:
            if results:
                results = [book for book in results if book.genre == genre]
            else:
                results.extend(self.indexes.search_by_genre(genre))
        
        return BookCollection(results)
    
    def search_by_keyword(self, keyword: str) -> BookCollection:
        """Поиск по ключевому слову"""
        return self.books.search_by_keyword(keyword)
    
    def get_book(self, isbn: str) -> Optional[Book]:
        """Получить книгу по ISBN"""
        return self.indexes.get_book_by_isbn(isbn)
    
    def print_status(self) -> None:
        """Вывести статус библиотеки"""
        total = len(self.books)
        available = len(self.books.get_available_books())
        borrowed = len(self.books.get_borrowed_books())
        
        print("\n" + "="*50)
        print(f"СТАТУС БИБЛИОТЕКИ '{self.name}':")
        print(f"Всего книг: {total}")
        print(f"Доступно: {available}")
        print(f"Выдано: {borrowed}")
        print("="*50)