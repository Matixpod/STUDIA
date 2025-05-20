# validation.py
from pydantic import BaseModel, ValidationError, model_validator
from .types import Number  # Importujesz alias z types.py

class CalculationInput(BaseModel):
    a: Number
    b: Number
    operator: str

    @model_validator(mode='before')
    def check_operator_and_b(cls, values):
        operator = values.get('operator')
        b = values.get('b')
        if operator not in ['+', '-', '*', '/']:
            raise ValueError('Unsupported operation')
        if operator == '/' and b == 0:
            raise ValueError('Cannot divide by zero')
        return values
