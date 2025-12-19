"""
Класс Book и связанные компоненты
"""
from typing import Dict, Optional


class Book:
    """Класс книги с магическими методами"""
    
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
        self._is_borrowed = False
    
    def __repr__(self) -> str:
        """Строковое представление книги"""
        status = "выдана" if self._is_borrowed else "в наличии"
        return f"Книга('{self.title}', {self.author}, {self.year}, {self.genre}, ISBN: {self.isbn}, статус: {status})"
    
    def __contains__(self, keyword: str) -> bool:
        """Магический метод для поиска по ключевому слову"""
        return (keyword.lower() in self.title.lower() or 
                keyword.lower() in self.author.lower() or 
                keyword.lower() in self.genre.lower() or
                keyword.lower() in str(self.year))
    
    def __eq__(self, other: object) -> bool:
        """Сравнение книг по ISBN"""
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn
    
    def __hash__(self) -> int:
        """Хэш для использования в словарях"""
        return hash(self.isbn)
    
    def borrow(self) -> bool:
        """Выдать книгу"""
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False
    
    def return_book(self) -> bool:
        """Вернуть книгу"""
        if self._is_borrowed:
            self._is_borrowed = False
            return True
        return False
    
    @property
    def is_available(self) -> bool:
        """Проверка доступности книги"""
        return not self._is_borrowed
    
    def to_dict(self) -> Dict:
        """Конвертация в словарь для сохранения"""
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'isbn': self.isbn,
            'is_borrowed': self._is_borrowed
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        """Создание объекта из словаря"""
        book = cls(
            title=data['title'],
            author=data['author'],
            year=data['year'],
            genre=data['genre'],
            isbn=data['isbn']
        )
        book._is_borrowed = data.get('is_borrowed', False)
        return book