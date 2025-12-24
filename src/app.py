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
    run_simulation(seed=42)
    
    print("\n" + "="*60)
    print("СЛУЧАЙНАЯ СИМУЛЯЦИЯ")
    print("="*60)
    
    # Случайная симуляция
    run_simulation(steps=5)



def start_simulation(steps: int = 20, seed: int | None = None):
    """Запуск симуляции"""
    print("\n" + "="*60)
    print("ЗАПУСК СИМУЛЯЦИИ")
    print("="*60)
    
    run_simulation(steps=steps, seed=seed)
    

def app():
    print("Выберите тип симуляции библиотеки")
    print("="*60)
    print("1. Базовый пример использования\n" \
    "2. Пример симуляции\n" \
    "3. Симуляция с входными данными\n")

    type = input("Тип симуляции: ")

    match type:
        case "1":
            example_basic_usage()

        case "2":
            example_simulation()

        case "3":
            print("Введите входные данные: ")
            steps = int(input("Количество шагов симуляции: "))
            print("\n")
            seed = int(input("Сид: "))
            print("\n")  

            run_simulation(steps=steps, seed=seed)