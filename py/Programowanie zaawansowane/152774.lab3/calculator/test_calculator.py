import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6

def test_multiply(calc):
    assert calc.multiply(6, 7) == 42

def test_divide(calc):
    assert calc.divide(8, 2) == 4

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)
