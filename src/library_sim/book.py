from typing import Dict, Optional
from abc import ABC, abstractmethod


class Book(ABC):
    """Абстрактный базовый класс книги"""
    
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
        return f"{self.__class__.__name__}('{self.title}', {self.author}, {self.year}, {self.genre}, ISBN: {self.isbn}, статус: {status})"
    
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
        """Выдать книгу - общий метод для всех книг"""
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False
    
    def return_book(self) -> bool:
        """Вернуть книгу - общий метод для всех книг"""
        if self._is_borrowed:
            self._is_borrowed = False
            return True
        return False
    
    @property
    def is_available(self) -> bool:
        """Проверка доступности книги - общее свойство"""
        return not self._is_borrowed
    
    @abstractmethod
    def get_loan_period(self) -> int:
        """Абстрактный метод: получить срок выдачи в днях"""
        pass
    
    @abstractmethod
    def can_be_extended(self) -> bool:
        """Абстрактный метод: можно ли продлить книгу"""
        pass
    
    def to_dict(self) -> Dict:
        """Конвертация в словарь для сохранения"""
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'isbn': self.isbn,
            'is_borrowed': self._is_borrowed,
            'type': self.__class__.__name__
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        """Создание объекта из словаря с учетом типа"""
        book_type = data.get('type', 'RegularBook')
        
        if book_type == 'ReferenceBook':
            return ReferenceBook.from_dict(data)
        elif book_type == 'FictionBook':
            return FictionBook.from_dict(data)
        else:
            return RegularBook.from_dict(data)


class RegularBook(Book):
    """Обычная книга - базовый производный класс"""
    
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        super().__init__(title, author, year, genre, isbn)
    
    def get_loan_period(self) -> int:
        """Срок выдачи обычной книги - 14 дней"""
        return 14
    
    def can_be_extended(self) -> bool:
        """Обычную книгу можно продлить 1 раз"""
        return True
    
    def __repr__(self) -> str:
        """Строковое представление с указанием типа"""
        base_repr = super().__repr__()
        return base_repr.replace("RegularBook", "Обычная книга", 1)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'RegularBook':
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


class ReferenceBook(Book):
    """Справочная/научная книга"""
    
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str,
                 reference_type: str = "справочник"):
        super().__init__(title, author, year, genre, isbn)
        self.reference_type = reference_type  # тип: справочник, энциклопедия, словарь
    
    def get_loan_period(self) -> int:
        """Справочные книги выдаются на 7 дней"""
        return 7
    
    def can_be_extended(self) -> bool:
        """Справочные книги нельзя продлевать"""
        return False
    
    def is_for_library_use_only(self) -> bool:
        """Некоторые справочники только для использования в библиотеке"""
        return self.reference_type in ["энциклопедия", "словарь"]
    
    def __repr__(self) -> str:
        """Строковое представление с указанием типа"""
        base_repr = super().__repr__()
        return base_repr.replace("ReferenceBook", f"{self.reference_type.capitalize()}", 1)
    
    def to_dict(self) -> Dict:
        """Конвертация в словарь с дополнительными полями"""
        data = super().to_dict()
        data['reference_type'] = self.reference_type
        return data
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ReferenceBook':
        """Создание объекта из словаря"""
        book = cls(
            title=data['title'],
            author=data['author'],
            year=data['year'],
            genre=data['genre'],
            isbn=data['isbn'],
            reference_type=data.get('reference_type', 'справочник')
        )
        book._is_borrowed = data.get('is_borrowed', False)
        return book


class FictionBook(Book):
    """
    Художественная литература
    """
    
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str,
                 literary_genre: str = "проза"):
        super().__init__(title, author, year, genre, isbn)
        self.literary_genre = literary_genre  # литературный жанр: проза, поэзия, драма
    
    def get_loan_period(self) -> int:
        """Художественную литературу выдают на 21 день"""
        return 21
    
    def can_be_extended(self) -> bool:
        """Художественную литературу можно продлить 2 раза"""
        return True
    
    def is_popular_genre(self) -> bool:
        """Проверка, является ли жанр популярным"""
        popular_genres = ["фэнтези", "детектив", "роман", "триллер"]
        return self.genre.lower() in popular_genres
    
    def __repr__(self) -> str:
        """Строковое представление с указанием типа"""
        base_repr = super().__repr__()
        return base_repr.replace("FictionBook", f"Худ. {self.literary_genre}", 1)
    
    def to_dict(self) -> Dict:
        """Конвертация в словарь с дополнительными полями"""
        data = super().to_dict()
        data['literary_genre'] = self.literary_genre
        return data
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'FictionBook':
        """Создание объекта из словаря"""
        book = cls(
            title=data['title'],
            author=data['author'],
            year=data['year'],
            genre=data['genre'],
            isbn=data['isbn'],
            literary_genre=data.get('literary_genre', 'проза')
        )
        book._is_borrowed = data.get('is_borrowed', False)
        return book