"""
Модуль для псевдослучайной симуляции работы библиотеки
"""
import random
from typing import Optional
from .book import Book
from .library import Library


def run_simulation(steps: int = 20, seed: Optional[int] = None) -> None:
    """
    Запуск псевдослучайной симуляции работы библиотеки
    
    Args:
        steps: Количество шагов симуляции
        seed: Seed для генератора случайных чисел
    """
    # Настройка случайного генератора
    if seed is not None:
        random.seed(seed)
        print(f"\n🌱 Начало симуляции с seed={seed}")
    else:
        print(f"\n🎲 Начало случайной симуляции")
    
    # Создание библиотеки
    library = Library(name="Симуляционная библиотека")
    
    # Список возможных событий (минимум 5 разных типов)
    events = [
        "add_book",           # Добавление новой книги
        "remove_random_book", # Удаление случайной книги
        "borrow_random_book", # Выдача случайной книги
        "return_random_book", # Возврат случайной книги
        "search_by_author",   # Поиск по автору
        "search_by_genre",    # Поиск по жанру
        "search_by_year",     # Поиск по году
        "try_nonexistent",    # Попытка получить несуществующую книгу
    ]
    
    # Данные для событий
    new_books_data = [
        ("Собачье сердце", "Михаил Булгаков", 1925, "Сатира", "978-5-389-06535-9"),
        ("Улисс", "Джеймс Джойс", 1922, "Модернизм", "978-5-389-03948-0"),
        ("О дивный новый мир", "Олдос Хаксли", 1932, "Антиутопия", "978-5-17-090689-1"),
        ("Властелин колец", "Дж. Р. Р. Толкин", 1954, "Фэнтези", "978-5-17-080185-2"),
        ("Шерлок Холмс", "Артур Конан Дойл", 1892, "Детектив", "978-5-389-03215-3"),
    ]
    
    authors = ["Лев Толстой", "Федор Достоевский", "Джордж Оруэлл", "Джоан Роулинг", 
               "Михаил Булгаков", "Антуан де Сент-Экзюпери"]
    genres = ["Роман", "Фэнтези", "Антиутопия", "Сказка", "Детектив", "Приключения"]
    
    print("\n" + "="*60)
    print("НАЧАЛО СИМУЛЯЦИИ БИБЛИОТЕКИ")
    print("="*60)
    
    for step in range(1, steps + 1):
        print(f"\n🔹 Шаг {step}/{steps}: ", end="")
        
        # Выбор случайного события
        event = random.choice(events)
        
        if event == "add_book":
            # Добавление новой книги
            if new_books_data:
                title, author, year, genre, isbn = random.choice(new_books_data)
                new_book = Book(title, author, year, genre, isbn)
                library.add_book(new_book)
                new_books_data.remove((title, author, year, genre, isbn))
            else:
                print("Нет новых книг для добавления")
                
        elif event == "remove_random_book":
            # Удаление случайной книги
            if len(library.books) > 0:
                book_to_remove = random.choice(list(library.books))
                library.remove_book(book_to_remove.isbn)
            else:
                print("Нет книг для удаления")
                
        elif event == "borrow_random_book":
            # Выдача случайной книги
            available_books = library.books.get_available_books()
            if available_books:
                book_to_borrow = random.choice(available_books)
                library.borrow_book(book_to_borrow.isbn)
            else:
                print("Нет доступных книг для выдачи")
                
        elif event == "return_random_book":
            # Возврат случайной книги
            borrowed_books = library.books.get_borrowed_books()
            if borrowed_books:
                book_to_return = random.choice(borrowed_books)
                library.return_book(book_to_return.isbn)
            else:
                print("Нет выданных книг для возврата")
                
        elif event == "search_by_author":
            # Поиск по автору
            author = random.choice(authors)
            results = library.search_books(author=author)
            print(f"Поиск книг автора '{author}': найдено {len(results)} книг")
            
        elif event == "search_by_genre":
            # Поиск по жанру
            genre = random.choice(genres)
            results = library.search_books(genre=genre)
            print(f"Поиск книг жанра '{genre}': найдено {len(results)} книг")
            
        elif event == "search_by_year":
            # Поиск по году
            year = random.choice([1869, 1949, 1997, 1967, 1925])
            results = library.search_books(year=year)
            print(f"Поиск книг {year} года: найдено {len(results)} книг")
            
        elif event == "try_nonexistent":
            # Попытка получить несуществующую книгу
            fake_isbn = "000-0-00-000000-0"
            print(f"Попытка выдать книгу с несуществующим ISBN {fake_isbn}")
            library.borrow_book(fake_isbn)
    
    print("\n" + "="*60)
    print("ЗАВЕРШЕНИЕ СИМУЛЯЦИИ")
    print("="*60)
    
    # Финальный статус
    library.print_status()


if __name__ == "__main__":
    # Запуск симуляции при прямом вызове модуля
    print("Запуск тестовой симуляции...")
    run_simulation(steps=15, seed=42)