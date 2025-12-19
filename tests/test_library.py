"""
Тесты для класса Library
"""
import pytest
from src.library_sim.book import Book
from src.library_sim.library import Library


class TestLibrary:
    """Тестирование класса Library"""
    
    def setup_method(self):
        """Настройка теста"""
        self.library = Library("Тестовая библиотека")
    
    def test_library_creation(self):
        """Тест создания библиотеки"""
        assert self.library.name == "Тестовая библиотека"
        assert len(self.library.books) > 0
        assert len(self.library.indexes) > 0
    
    def test_add_book(self):
        """Тест добавления книги"""
        new_book = Book("Новая книга", "Новый автор", 2023, "Новый жанр", "999-999")
        
        # Успешное добавление
        result = self.library.add_book(new_book)
        assert result == True
        assert len(self.library.books) == 9  # 8 начальных + 1 новая
        
        # Попытка добавить книгу с тем же ISBN
        duplicate_book = Book("Другая книга", "Другой автор", 2023, "Другой жанр", "999-999")
        result = self.library.add_book(duplicate_book)
        assert result == False
    
    def test_borrow_return_book(self):
        """Тест выдачи и возврата книги"""
        # Получаем первую книгу
        first_book_isbn = list(self.library.indexes)[0]
        
        # Выдача книги
        result = self.library.borrow_book(first_book_isbn)
        assert result == True
        
        # Проверяем, что книга стала выданной
        book = self.library.get_book(first_book_isbn)
        assert book.is_available == False
        
        # Попытка повторной выдачи
        result = self.library.borrow_book(first_book_isbn)
        assert result == False
        
        # Возврат книги
        result = self.library.return_book(first_book_isbn)
        assert result == True
        assert book.is_available == True
    
    def test_search_books(self):
        """Тест поиска книг"""
        # Поиск по автору (должен найти книги Толстого)
        results = self.library.search_books(author="Лев Толстой")
        assert len(results) >= 2  # Война и мир + Анна Каренина
        
        # Поиск по жанру
        results = self.library.search_books(genre="Фэнтези")
        assert len(results) >= 2  # Мастер и Маргарита + Гарри Поттер
        
        # Поиск по году
        results = self.library.search_books(year=1869)
        assert len(results) >= 2  # Война и мир + Идиот
        
        # Комбинированный поиск
        results = self.library.search_books(author="Лев Толстой", genre="Роман")
        assert len(results) >= 2
    
    def test_search_by_keyword(self):
        """Тест поиска по ключевому слову"""
        results = self.library.search_by_keyword("война")
        assert len(results) >= 1  # Война и мир
        
        results = self.library.search_by_keyword("преступление")
        assert len(results) >= 1  # Преступление и наказание