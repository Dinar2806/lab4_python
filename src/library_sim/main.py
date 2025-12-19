"""
Основной файл для запуска из src
"""
import sys
import os

# Добавляем путь к examples
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from examples.basic_usage import example_basic_usage, example_simulation


def main():
    """Основная функция"""
    print("ЛАБОРАТОРНАЯ РАБОТА №4: СИСТЕМА БИБЛИОТЕКИ")
    print("="*60)
    
    example_basic_usage()
    example_simulation()


if __name__ == "__main__":
    main()