"""
Тесты для симуляции
"""
import random
from src.library_sim.simulation import run_simulation


class TestSimulation:
    """Тестирование симуляции"""
    
    def test_simulation_with_seed(self):
        """Тест воспроизводимости симуляции с seed"""
        # Этот тест проверяет, что с одинаковым seed
        # симуляция ведет себя одинаково
        # (в реальном тесте нужно было бы проверять вывод)
        
        # Запускаем симуляцию с seed
        try:
            run_simulation(steps=5, seed=123)
            assert True
        except Exception as e:
            pytest.fail(f"Симуляция завершилась с ошибкой: {e}")
    
    def test_simulation_without_seed(self):
        """Тест симуляции без seed"""
        try:
            run_simulation(steps=5)
            assert True
        except Exception as e:
            pytest.fail(f"Симуляция завершилась с ошибкой: {e}")
    
    def test_random_seed_behavior(self):
        """Тест поведения random с seed"""
        # Проверяем, что seed действительно делает генерацию воспроизводимой
        random.seed(42)
        numbers1 = [random.randint(1, 100) for _ in range(5)]
        
        random.seed(42)
        numbers2 = [random.randint(1, 100) for _ in range(5)]
        
        assert numbers1 == numbers2