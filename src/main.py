"""
Основной файл для запуска из src
"""
import sys
import os

# Добавляем путь к examples
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.app import app


def main():
    print("ЛАБОРАТОРНАЯ РАБОТА №4: СИСТЕМА БИБЛИОТЕКИ")
    print("="*60 + "\n")

    app()
    
    


if __name__ == "__main__":
    main()