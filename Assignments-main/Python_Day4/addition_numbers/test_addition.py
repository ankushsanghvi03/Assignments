import pytest
from addition import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5

def test_add_positive_and_negative():
    assert add(2, -3) == -1

def test_add_floats():
    assert add(2.5, 3.1) == 5.6

def test_subtract():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_multiply():
    assert multiply(2, 3) == 6

def test_multiply_zero():
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
