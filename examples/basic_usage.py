"""
Пример использования библиотеки
"""
from src.library_sim import Book, Library, run_simulation


def example_basic_usage():
    """Базовый пример использования"""
    print("="*60)
    print("ПРИМЕР ИСПОЛЬЗОВАНИЯ БИБЛИОТЕКИ")
    print("="*60)
    
    # Создание библиотеки
    library = Library("Моя библиотека")
    
    # Показываем статус
    library.print_status()
    
    # Создаем новую книгу
    new_book = Book(
        title="Новая книга",
        author="Я",
        year=2024,
        genre="Научная литература",
        isbn="987-654-321-0"
    )
    
    # Добавляем книгу
    print("\nДобавление книги:")
    library.add_book(new_book)
    
    # Ищем книги
    print("\nПоиск книг Толстого:")
    results = library.search_books(author="Лев Толстой")
    print(f"Найдено книг: {len(results)}")
    for book in results:
        print(f"  - {book}")
    
    # Выдача книги
    print("\nВыдача книги:")
    library.borrow_book("978-5-389-07435-1")  # Война и мир
    
    # Показываем обновленный статус
    library.print_status()
    
    # Поиск по ключевому слову
    print("\nПоиск по ключевому слову 'мир':")
    results = library.search_by_keyword("мир")
    print(f"Найдено книг: {len(results)}")


def example_simulation():
    """Пример запуска симуляции"""
    print("\n" + "="*60)
    print("ЗАПУСК СИМУЛЯЦИИ")
    print("="*60)
    
    # Детерминированная симуляция
    run_simulation(steps=10, seed=42)
    
    print("\n" + "="*60)
    print("СЛУЧАЙНАЯ СИМУЛЯЦИЯ")
    print("="*60)
    
    # Случайная симуляция
    run_simulation(steps=5)


