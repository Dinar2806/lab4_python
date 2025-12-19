"""
Тесты для класса Book
"""
import pytest
from src.library_sim.book import Book


class TestBook:
    """Тестирование класса Book"""
    
    def test_book_creation(self):
        """Тест создания книги"""
        book = Book("Тест", "Автор", 2023, "Жанр", "123-456")
        assert book.title == "Тест"
        assert book.author == "Автор"
        assert book.year == 2023
        assert book.genre == "Жанр"
        assert book.isbn == "123-456"
        assert book.is_available == True
    
    def test_book_repr(self):
        """Тест строкового представления"""
        book = Book("Тест", "Автор", 2023, "Жанр", "123-456")
        assert "Книга" in repr(book)
        assert "Тест" in repr(book)
        assert "Автор" in repr(book)
    
    def test_book_contains(self):
        """Тест магического метода __contains__"""
        book = Book("Война и мир", "Лев Толстой", 1869, "Роман", "978-5-389-07435-1")
        assert "война" in book
        assert "ВОЙНА" in book
        assert "Толстой" in book
        assert "1869" in book
        assert "роман" in book
        assert "несуществующее" not in book
    
    def test_book_borrow_return(self):
        """Тест выдачи и возврата книги"""
        book = Book("Тест", "Автор", 2023, "Жанр", "123-456")
        
        # Выдача
        assert book.borrow() == True
        assert book.is_available == False
        
        # Повторная выдача
        assert book.borrow() == False
        
        # Возврат
        assert book.return_book() == True
        assert book.is_available == True
        
        # Повторный возврат
        assert book.return_book() == False
    
    def test_book_equality(self):
        """Тест сравнения книг"""
        book1 = Book("Книга 1", "Автор", 2023, "Жанр", "123-456")
        book2 = Book("Книга 2", "Автор", 2023, "Жанр", "123-456")  # Тот же ISBN
        book3 = Book("Книга 1", "Автор", 2023, "Жанр", "789-012")  # Другой ISBN
        
        assert book1 == book2  # Равны по ISBN
        assert book1 != book3  # Разные ISBN