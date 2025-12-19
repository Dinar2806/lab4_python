"""
Тесты для пользовательских коллекций
"""
import pytest
from src.library_sim.book import Book
from library_sim.my_collections import BookCollection, IndexDict


class TestBookCollection:
    """Тестирование BookCollection"""
    
    def setup_method(self):
        """Настройка теста"""
        self.book1 = Book("Книга 1", "Автор 1", 2020, "Жанр 1", "111")
        self.book2 = Book("Книга 2", "Автор 2", 2021, "Жанр 2", "222")
        self.book3 = Book("Книга 3", "Автор 3", 2022, "Жанр 3", "333")
        self.collection = BookCollection([self.book1, self.book2, self.book3])
    
    def test_len(self):
        """Тест метода __len__"""
        assert len(self.collection) == 3
    
    def test_getitem_index(self):
        """Тест доступа по индексу"""
        assert self.collection[0] == self.book1
        assert self.collection[1] == self.book2
        assert self.collection[2] == self.book3
    
    def test_getitem_slice(self):
        """Тест срезов"""
        sliced = self.collection[1:3]
        assert len(sliced) == 2
        assert sliced[0] == self.book2
        assert sliced[1] == self.book3
    
    def test_iteration(self):
        """Тест итерации"""
        books = list(self.collection)
        assert books == [self.book1, self.book2, self.book3]
    
    def test_contains(self):
        """Тест метода __contains__"""
        assert self.book1 in self.collection
        new_book = Book("Новая", "Автор", 2023, "Жанр", "999")
        assert new_book not in self.collection
    
    def test_add_remove(self):
        """Тест добавления и удаления"""
        new_book = Book("Новая", "Автор", 2023, "Жанр", "999")
        
        # Добавление
        self.collection.add(new_book)
        assert len(self.collection) == 4
        assert new_book in self.collection
        
        # Удаление
        result = self.collection.remove(new_book)
        assert result == True
        assert len(self.collection) == 3
        assert new_book not in self.collection
    
    def test_search_by_keyword(self):
        """Тест поиска по ключевому слову"""
        # Поиск по названию
        results = self.collection.search_by_keyword("Книга")
        assert len(results) == 3
        
        # Поиск по автору
        results = self.collection.search_by_keyword("Автор 1")
        assert len(results) == 1
        assert results[0] == self.book1


class TestIndexDict:
    """Тестирование IndexDict"""
    
    def setup_method(self):
        """Настройка теста"""
        self.book1 = Book("Книга 1", "Автор А", 2020, "Жанр X", "111")
        self.book2 = Book("Книга 2", "Автор Б", 2020, "Жанр Y", "222")
        self.book3 = Book("Книга 3", "Автор А", 2021, "Жанр X", "333")
        self.index = IndexDict()
    
    def test_add_book(self):
        """Тест добавления книги в индексы"""
        self.index.add_book(self.book1)
        
        assert len(self.index) == 1
        assert "111" in self.index
        assert self.index.get_book_by_isbn("111") == self.book1
        
        # Проверка индекса по автору
        assert len(self.index.search_by_author("Автор А")) == 1
        
        # Проверка индекса по году
        assert len(self.index.search_by_year(2020)) == 1
    
    def test_remove_book(self):
        """Тест удаления книги из индексов"""
        self.index.add_book(self.book1)
        self.index.add_book(self.book2)
        
        assert len(self.index) == 2
        
        # Удаление
        result = self.index.remove_book(self.book1)
        assert result == True
        assert len(self.index) == 1
        assert "111" not in self.index
        
        # Попытка удалить несуществующую
        result = self.index.remove_book(self.book3)
        assert result == False
    
    def test_search_functions(self):
        """Тест функций поиска"""
        self.index.add_book(self.book1)
        self.index.add_book(self.book2)
        self.index.add_book(self.book3)
        
        # Поиск по автору
        author_results = self.index.search_by_author("Автор А")
        assert len(author_results) == 2
        
        # Поиск по году
        year_results = self.index.search_by_year(2020)
        assert len(year_results) == 2
        
        # Поиск по жанру
        genre_results = self.index.search_by_genre("Жанр X")
        assert len(genre_results) == 2