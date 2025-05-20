from abc import ABC, abstractmethod
from typing import Union, Dict, TypeAlias, Literal, final # final od Python 3.8

# PEP 484: Zaawansowane typy
Numeric: TypeAlias = Union[int, float]
OperationSymbol: TypeAlias = Literal['+', '-', '*', '/']

# --- Zasada SRP: Definicja interfejsu operacji (Wzorzec Strategy) ---
class Operation(ABC):
    """
    Abstract base class for an arithmetic operation. (Strategy Interface)
    """
    @abstractmethod
    def execute(self, a: Numeric, b: Numeric) -> Numeric:
        """
        Execute the arithmetic operation.

        Parameters
        ----------
        a : Numeric
            The first operand.
        b : Numeric
            The second operand.

        Returns
        -------
        Numeric
            The result of the operation.
        """
        pass

# --- Zasada SRP: Konkretne implementacje operacji (Konkretne Strategie) ---
@final
class AddOperation(Operation):
    """Adds two numbers."""
    def execute(self, a: Numeric, b: Numeric) -> Numeric:
        return a + b

@final
class SubtractOperation(Operation):
    """Subtracts the second number from the first."""
    def execute(self, a: Numeric, b: Numeric) -> Numeric:
        return a - b

@final
class MultiplyOperation(Operation):
    """Multiplies two numbers."""
    def execute(self, a: Numeric, b: Numeric) -> Numeric:
        return a * b

@final
class DivideOperation(Operation):
    """Divides the first number by the second. Returns a float."""
    def execute(self, a: Numeric, b: Numeric) -> float: # Division always results in float
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return float(a) / float(b) # Ensure float division

# --- Wzorzec Factory (lub mechanizm wyboru strategii) ---
@final
class OperationFactory:
    """
    Factory class to get an operation strategy.
    Follows SRP: its only responsibility is to create/provide operation objects.
    """
    def __init__(self) -> None:
        self._operations: Dict[OperationSymbol, Operation] = {
            '+': AddOperation(),
            '-': SubtractOperation(),
            '*': MultiplyOperation(),
            '/': DivideOperation(),
        }
        # Strategie są bezstanowe, więc możemy je preinstancjonować (Flyweight-like)

    def get_operation(self, operator: OperationSymbol) -> Operation:
        """
        Get the operation object for the given operator symbol.

        Parameters
        ----------
        operator : OperationSymbol
            The symbol representing the desired operation ('+', '-', '*', '/').

        Returns
        -------
        Operation
            The concrete operation strategy.

        Raises
        ------
        ValueError
            If the operator is not supported.
        """
        try:
            return self._operations[operator]
        except KeyError:
            raise ValueError(f"Unsupported operation: {operator}")


# --- Główna klasa Calculator (Orkiestrator) ---
@final
class Calculator:
    """
    A calculator that uses specific operation strategies to perform calculations.
    Follows SRP: its responsibility is to orchestrate the calculation,
    delegating the actual computation to strategy objects.
    """
    def __init__(self, factory: OperationFactory) -> None:
        """
        Initialize the calculator with an operation factory.

        Parameters
        ----------
        factory : OperationFactory
            The factory to obtain operation strategies.
        """
        self._factory = factory
        # Usunęliśmy self.result, ponieważ metody bezpośrednio zwracają wynik.
        # Kalkulator jest teraz bezstanowy w kontekście wyniku ostatniej operacji.

    def calculate(self, a: Numeric, b: Numeric, operator: OperationSymbol) -> Numeric:
        """
        Perform a calculation using the specified operation.

        Parameters
        ----------
        a : Numeric
            The first operand.
        b : Numeric
            The second operand.
        operator : OperationSymbol
            The symbol for the operation to perform.

        Returns
        -------
        Numeric
            The result of the calculation.

        Raises
        ------
        ValueError
            If the operator is unsupported or if division by zero is attempted.
        """
        operation_strategy = self._factory.get_operation(operator)
        return operation_strategy.execute(a, b)

