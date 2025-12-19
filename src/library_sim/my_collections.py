"""
Пользовательские коллекции: BookCollection и IndexDict
"""
from typing import List, Dict, Any, Union, Optional
from collections import defaultdict


class BookCollection:
    """
    Пользовательская списковая коллекция книг
    Поддерживает индексацию, срезы, итерацию
    """
    
    def __init__(self, books: List['Book'] = None):
        self._books = books if books else []
    
    def __len__(self) -> int:
        """Количество книг в коллекции"""
        return len(self._books)
    
    def __getitem__(self, index: Union[int, slice]) -> Union['Book', 'BookCollection']:
        """Доступ по индексу или срезу"""
        if isinstance(index, slice):
            return BookCollection(self._books[index])
        return self._books[index]
    
    def __iter__(self):
        """Итерация по книгам"""
        return iter(self._books)
    
    def __repr__(self) -> str:
        """Строковое представление"""
        return f"BookCollection({len(self)} книг)"
    
    def __contains__(self, book: 'Book') -> bool:
        """Проверка наличия книги"""
        return book in self._books
    
    def add(self, book: 'Book') -> None:
        """Добавить книгу"""
        self._books.append(book)
    
    def remove(self, book: 'Book') -> bool:
        """Удалить книгу"""
        if book in self._books:
            self._books.remove(book)
            return True
        return False
    
    def get_available_books(self) -> List['Book']:
        """Получить доступные книги"""
        return [book for book in self._books if book.is_available]
    
    def get_borrowed_books(self) -> List['Book']:
        """Получить выданные книги"""
        return [book for book in self._books if not book.is_available]
    
    def search_by_keyword(self, keyword: str) -> 'BookCollection':
        """Поиск книг по ключевому слову"""
        results = [book for book in self._books if keyword in book]
        return BookCollection(results)
    
    def clear(self) -> None:
        """Очистить коллекцию"""
        self._books.clear()


class IndexDict:
    """
    Пользовательская словарная коллекция для индексации книг
    """
    
    def __init__(self):
        self._indexes = {
            'isbn': {},  # ISBN -> Book
            'author': defaultdict(list),  # Author -> List[Book]
            'year': defaultdict(list),    # Year -> List[Book]
            'genre': defaultdict(list)    # Genre -> List[Book]
        }
        self._change_log = []
    
    def __getitem__(self, key: str) -> Dict:
        """Доступ к индексу по имени"""
        if key not in self._indexes:
            raise KeyError(f"Доступные индексы: {list(self._indexes.keys())}")
        return self._indexes[key]
    
    def __setitem__(self, key: str, value: Any):
        """Установка значения с логированием"""
        self._indexes[key] = value
        self._log_change(f"Изменен индекс '{key}'")
    
    def __len__(self) -> int:
        """Количество индексированных книг"""
        return len(self._indexes['isbn'])
    
    def __contains__(self, isbn: str) -> bool:
        """Проверка наличия книги по ISBN"""
        return isbn in self._indexes['isbn']
    
    def __iter__(self):
        """Итерация по ISBNам"""
        return iter(self._indexes['isbn'])
    
    def _log_change(self, message: str):
        """Логирование изменений"""
        self._change_log.append(message)
    
    def add_book(self, book: 'Book') -> None:
        """Добавить книгу во все индексы"""
        # ISBN (уникальный)
        self._indexes['isbn'][book.isbn] = book
        self._log_change(f"Добавлена книга: {book.title} (ISBN: {book.isbn})")
        
        # Автор
        self._indexes['author'][book.author].append(book)
        
        # Год
        self._indexes['year'][book.year].append(book)
        
        # Жанр
        self._indexes['genre'][book.genre].append(book)
    
    def remove_book(self, book: 'Book') -> bool:
        """Удалить книгу из всех индексов"""
        if book.isbn not in self._indexes['isbn']:
            return False
        
        # Удаление из всех индексов
        del self._indexes['isbn'][book.isbn]
        
        if book in self._indexes['author'][book.author]:
            self._indexes['author'][book.author].remove(book)
        
        if book in self._indexes['year'][book.year]:
            self._indexes['year'][book.year].remove(book)
        
        if book in self._indexes['genre'][book.genre]:
            self._indexes['genre'][book.genre].remove(book)
        
        self._log_change(f"Удалена книга: {book.title} (ISBN: {book.isbn})")
        return True
    
    def search_by_author(self, author: str) -> List['Book']:
        """Поиск книг по автору"""
        return self._indexes['author'].get(author, [])
    
    def search_by_year(self, year: int) -> List['Book']:
        """Поиск книг по году"""
        return self._indexes['year'].get(year, [])
    
    def search_by_genre(self, genre: str) -> List['Book']:
        """Поиск книг по жанру"""
        return self._indexes['genre'].get(genre, [])
    
    def get_book_by_isbn(self, isbn: str) -> Optional['Book']:
        """Получить книгу по ISBN"""
        return self._indexes['isbn'].get(isbn)
    
    def get_change_log(self) -> List[str]:
        """Получить лог изменений"""
        return self._change_log.copy()