"""
Модуль для псевдослучайной симуляции работы библиотеки
"""
import random
from typing import Optional
from .book import RegularBook, ReferenceBook, FictionBook
from .library import Library


def run_simulation(steps: int = 20, seed: Optional[int] = None) -> None:
    """
    Запуск псевдослучайной симуляции работы библиотеки
    """
    if seed is not None:
        random.seed(seed)
        print(f"\nНачало симуляции с seed={seed}")
    else:
        print(f"\nНачало случайной симуляции")
    
    library = Library(name="Симуляционная библиотека")
    
    # События согласно требованиям + демонстрация наследования
    events = [
        "add_book",              # 1. Добавление новой книги
        "remove_random_book",    # 2. Удаление случайной книги
        "search_by_author",      # 3. Поиск по автору
        "search_by_genre",       # 3. Поиск по жанру
        "search_by_year",        # 3. Поиск по году
        "update_index",          # 4. Обновление индекса
        "try_nonexistent",       # 5. Попытка получить несуществующую книгу
        "demonstrate_inheritance", # Дополнительно: демонстрация наследования
    ]
    
    # Данные для добавления книг (всех типов)
    new_books_data = [
        # RegularBook
        ("Собачье сердце", "Михаил Булгаков", 1925, "сатира", "978-5-389-06535-9", "regular"),
        ("Улисс", "Джеймс Джойс", 1922, "модернизм", "978-5-389-03948-0", "regular"),
        
        # ReferenceBook
        ("Энциклопедия науки", "Коллектив авторов", 2020, "энциклопедия", "978-5-17-090699-0", "reference"),
        ("Словарь русского языка", "Сергей Ожегов", 1990, "словарь", "978-5-17-080195-1", "reference"),
        
        # FictionBook
        ("О дивный новый мир", "Олдос Хаксли", 1932, "антиутопия", "978-5-17-090689-1", "fiction"),
        ("Властелин колец", "Дж. Р. Р. Толкин", 1954, "фэнтези", "978-5-17-080185-2", "fiction"),
    ]
    
    authors = ["Лев Толстой", "Михаил Булгаков", "Джордж Оруэлл", "Джоан Роулинг"]
    genres = ["роман", "фэнтези", "антиутопия", "сатира", "энциклопедия", "словарь"]
    years = [1869, 1925, 1949, 1967, 1997, 2020]
    
    print("\n" + "="*60)
    print("НАЧАЛО СИМУЛЯЦИИ БИБЛИОТЕКИ")
    print("="*60)
    
    for step in range(1, steps + 1):
        
        
        event = random.choice(events)
        print("\nСобытие: " + event)


        print(f"Шаг {step}/{steps}: ", end="")
        
        if event == "add_book":
            """1. ДОБАВЛЕНИЕ НОВОЙ КНИГИ"""
            if new_books_data:
                title, author, year, genre, isbn, book_type = random.choice(new_books_data)
                
                # Создаем книгу нужного типа (демонстрация наследования)
                if book_type == "reference":
                    ref_type = random.choice(["справочник", "энциклопедия", "словарь"])
                    new_book = ReferenceBook(title, author, year, genre, isbn, ref_type)
                elif book_type == "fiction":
                    lit_genre = random.choice(["проза", "поэзия", "драма"])
                    new_book = FictionBook(title, author, year, genre, isbn, lit_genre)
                else:
                    new_book = RegularBook(title, author, year, genre, isbn)
                
                library.add_book(new_book)
                new_books_data.remove((title, author, year, genre, isbn, book_type))
            else:
                print("Нет новых книг для добавления")
                
        elif event == "remove_random_book":
            """2. УДАЛЕНИЕ СЛУЧАЙНОЙ КНИГИ"""
            if len(library.books) > 0:
                book_to_remove = random.choice(list(library.books))
                library.remove_book(book_to_remove.isbn)
            else:
                print("Нет книг для удаления")
                
        elif event == "search_by_author":
            """3. ПОИСК ПО АВТОРУ"""
            author = random.choice(authors)
            results = library.search_books(author=author)
            print(f"Поиск книг автора '{author}': найдено {len(results)} книг")
            if results:
                for i, book in enumerate(results[:2], 1):
                    print(f"  {i}. {book.title} ({book.__class__.__name__})")
                    
        elif event == "search_by_genre":
            """3. ПОИСК ПО ЖАНРУ"""
            genre = random.choice(genres)
            results = library.search_books(genre=genre)
            print(f"Поиск книг жанра '{genre}': найдено {len(results)} книг")
            if results:
                for i, book in enumerate(results[:2], 1):
                    print(f"  {i}. {book.title} ({book.author})")
                    
        elif event == "search_by_year":
            """3. ПОИСК ПО ГОДУ"""
            year = random.choice(years)
            results = library.search_books(year=year)
            print(f"Поиск книг {year} года: найдено {len(results)} книг")
            if results:
                for i, book in enumerate(results[:2], 1):
                    print(f"  {i}. {book.title} ({book.genre})")
                    
        elif event == "update_index":
            """4. ОБНОВЛЕНИЕ ИНДЕКСА"""
            print("Обновление индексов библиотеки...")
            # Показываем статистику индексов
            indexes = library.indexes
            stats = {
                'Всего книг в индексе ISBN': len(indexes['isbn']),
                'Уникальных авторов': len(indexes['author']),
                'Уникальных годов издания': len(indexes['year']),
                'Уникальных жанров': len(indexes['genre']),
            }
            
            print("Статистика индексов:")
            for key, value in stats.items():
                print(f"  {key}: {value}")
            
            # Показываем последние изменения
            change_log = indexes.get_change_log()
            if change_log:
                print(f"Последние изменения ({min(3, len(change_log))} из {len(change_log)}):")
                for change in change_log[-3:]:
                    print(f"  - {change}")
                    
        elif event == "try_nonexistent":
            """5. ПОПЫТКА ПОЛУЧИТЬ НЕСУЩЕСТВУЮЩУЮ КНИГУ"""
            fake_isbns = ["000-0-00-000000-0", "999-9-99-999999-9", "123-4-56-789012-3"]
            fake_isbn = random.choice(fake_isbns)
            print(f"Попытка выдать книгу с несуществующим ISBN {fake_isbn}")
            library.borrow_book(fake_isbn)
            
        elif event == "demonstrate_inheritance":
            """ДОПОЛНИТЕЛЬНО: ДЕМОНСТРАЦИЯ НАСЛЕДОВАНИЯ"""
            print("Демонстрация наследования (разные типы книг):")
            
            # Показываем книги по типам
            regular_books = library.get_books_by_type(RegularBook)
            reference_books = library.get_books_by_type(ReferenceBook)
            fiction_books = library.get_books_by_type(FictionBook)
            
            if regular_books:
                book = random.choice(regular_books)
                print(f"  Обычная книга: {book.title}")
                print(f"    Срок выдачи: {book.get_loan_period()} дней, Можно продлить: {'да' if book.can_be_extended() else 'нет'}")
            
            if reference_books:
                book = random.choice(reference_books)
                print(f"  Справочник: {book.title}")
                print(f"    Срок выдачи: {book.get_loan_period()} дней, Можно продлить: {'да' if book.can_be_extended() else 'нет'}")
                print(f"    Только в библиотеке: {'да' if book.is_for_library_use_only() else 'нет'}")
            
            if fiction_books:
                book = random.choice(fiction_books)
                print(f"  Художественная: {book.title}")
                print(f"    Срок выдачи: {book.get_loan_period()} дней, Можно продлить: {'да' if book.can_be_extended() else 'нет'}")
                print(f"    Популярный жанр: {'да' if book.is_popular_genre() else 'нет'}")
    
    print("\n" + "="*60)
    print("ЗАВЕРШЕНИЕ СИМУЛЯЦИИ")
    print("="*60)
    
    # Финальный статус
    library.print_status()
    
    # Дополнительно: показываем итоговую статистику по типам
    print("\nИтоговая статистика по типам книг:")
    print("-" * 40)
    regular_count = len(library.get_books_by_type(RegularBook))
    reference_count = len(library.get_books_by_type(ReferenceBook))
    fiction_count = len(library.get_books_by_type(FictionBook))
    
    print(f"Обычные книги: {regular_count}")
    print(f"Справочные книги: {reference_count}")
    print(f"Художественная литература: {fiction_count}")
    print(f"Всего: {regular_count + reference_count + fiction_count}")


if __name__ == "__main__":
    print("Запуск тестовой симуляции...")
    run_simulation(steps=15, seed=42)