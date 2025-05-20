import pytest
from advanced_calculator.calculator import Calculator, OperationFactory
from advanced_calculator.validation import CalculationInput
from pydantic import ValidationError

def test_addition():
    calc = Calculator(OperationFactory())
    assert calc.calculate(2, 3, '+') == 5

def test_subtraction():
    calc = Calculator(OperationFactory())
    assert calc.calculate(5, 3, '-') == 2

def test_multiplication():
    calc = Calculator(OperationFactory())
    assert calc.calculate(4, 3, '*') == 12

def test_division():
    calc = Calculator(OperationFactory())
    assert calc.calculate(10, 2, '/') == 5.0

def test_division_float_result():
    calc = Calculator(OperationFactory())
    assert calc.calculate(7, 2, '/') == 3.5

def test_division_by_zero():
    calc = Calculator(OperationFactory())
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.calculate(10, 0, '/')

def test_unsupported_operator():
    calc = Calculator(OperationFactory())
    with pytest.raises(ValueError, match="Unsupported operation"):
        calc.calculate(10, 5, '%')

def test_validation_correct_input():
    # Model powinien się utworzyć bez błędu
    model = CalculationInput(a=1, b=2, operator='+')
    assert model.a == 1
    assert model.b == 2
    assert model.operator == '+'

def test_validation_unsupported_operator():
    with pytest.raises(ValidationError, match="Unsupported operation"):
        CalculationInput(a=1, b=2, operator='%')

def test_validation_divide_by_zero():
    with pytest.raises(ValidationError, match="Cannot divide by zero"):
        CalculationInput(a=1, b=0, operator='/')
