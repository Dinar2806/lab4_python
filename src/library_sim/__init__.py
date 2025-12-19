"""
Library Simulation System
Лабораторная работа №4: Симуляция с пользовательскими коллекциями
"""

__version__ = "0.1.0"
__author__ = "Student"

from .book import Book
from .my_collections import BookCollection, IndexDict
from .library import Library
from .simulation import run_simulation

__all__ = [
    'Book',
    'BookCollection', 
    'IndexDict',
    'Library',
    'run_simulation'
]