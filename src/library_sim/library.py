"""
Класс Library - основная точка входа для работы с библиотекой
"""
from typing import Optional, List
from .book import Book
from .my_collections import BookCollection, IndexDict


class Library:
    """
    Основной класс библиотеки
    Объединяет пользовательские коллекции и логику
    """
    
    def __init__(self, name: str = "Главная библиотека"):
        self.name = name
        
        # Пользовательские коллекции
        self.books = BookCollection()
        self.indexes = IndexDict()
        
        # Инициализация начальными книгами
        self._create_initial_books()
    
    def __repr__(self) -> str:
        return f"Library(name='{self.name}', books={len(self.books)})"
    
    def _create_initial_books(self) -> None:
        """
        Создание начального набора книг
        """
        initial_books = [
            Book("Война и мир", "Лев Толстой", 1869, "Роман", "978-5-389-07435-1"),
            Book("Преступление и наказание", "Федор Достоевский", 1866, "Роман", "978-5-17-090665-5"),
            Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "Фэнтези", "978-5-17-067580-4"),
            Book("1984", "Джордж Оруэлл", 1949, "Антиутопия", "978-5-17-080115-9"),
            Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", "978-5-389-07429-0"),
            Book("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", "978-5-389-04863-5"),
            Book("Анна Каренина", "Лев Толстой", 1877, "Роман", "978-5-699-40438-4"),
            Book("Идиот", "Федор Достоевский", 1869, "Роман", "978-5-17-090678-5"),
        ]
        
        for book in initial_books:
            self.add_book(book, silent=True)
    
    def add_book(self, book: Book, silent: bool = False) -> bool:
        """
        Добавить книгу в библиотеку
        """
        if book.isbn in self.indexes:
            if not silent:
                print(f"Книга с ISBN {book.isbn} уже существует")
            return False
        
        self.books.add(book)
        self.indexes.add_book(book)
        
        if not silent:
            print(f"Добавлена книга: {book.title}")
        
        return True
    
    def remove_book(self, isbn: str) -> bool:
        """
        Удалить книгу по ISBN
        """
        book = self.indexes.get_book_by_isbn(isbn)
        if not book:
            print(f"Книга с ISBN {isbn} не найдена")
            return False
        
        self.books.remove(book)
        self.indexes.remove_book(book)
        
        print(f"Удалена книга: {book.title}")
        return True
    
    def borrow_book(self, isbn: str) -> bool:
        """Выдать книгу"""
        book = self.indexes.get_book_by_isbn(isbn)

        if not book:
            print(f"Книга с ISBN {isbn} не найдена")
            return False
        
        if book.borrow():
            print(f"Выдана книга: {book.title}")
            return True
        else:
            print(f"Книга '{book.title}' уже выдана")
            return False
    
    def return_book(self, isbn: str) -> bool:
        """
        Вернуть книгу
        """
        book = self.indexes.get_book_by_isbn(isbn)
        if not book:
            print(f"Книга с ISBN {isbn} не найдена")
            return False
        
        if book.return_book():
            print(f"Возвращена книга: {book.title}")
            return True
        else:
            print(f"Книга '{book.title}' не была выдана")
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