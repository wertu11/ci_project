import pytest
from calculator import add

# проверка положительных чисел
def test_add_positive():
    assert add(2, 3) == 5

# проверка отрицательного и положительного числа
def test_add_mixed():
    assert add(-1, 1) == 0

# проверка нулей
def test_add_zeros():
    assert add(0, 0) == 0

# параметризованный тест (проверяет сразу 3 набора данных, включая дроби)
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (-10, -5, -15),
    (1.5, 2.5, 4.0)
])
def test_add_complex(a, b, expected):
    assert add(a, b) == expected