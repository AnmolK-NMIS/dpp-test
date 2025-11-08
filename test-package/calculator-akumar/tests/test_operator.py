import pytest
from calculator.operator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 2) == -4

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)
