class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def __init__(self):
        """
        Initialize the calculator with a result set to zero.
        """
        self.result = 0

    def add(self, a, b):
        """
        Add two numbers.

        Parameters
        ----------
        a : float or int
            The first number.
        b : float or int
            The second number.

        Returns
        -------
        float or int
            The result of a + b.
        """
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        """
        Subtract one number from another.

        Parameters
        ----------
        a : float or int
            The number to subtract from.
        b : float or int
            The number to subtract.

        Returns
        -------
        float or int
            The result of a - b.
        """
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Parameters
        ----------
        a : float or int
            The first number.
        b : float or int
            The second number.

        Returns
        -------
        float or int
            The result of a * b.
        """
        self.result = a * b
        return self.result

    def divide(self, a, b):
        """
        Divide one number by another.

        Parameters
        ----------
        a : float or int
            The dividend.
        b : float or int
            The divisor.

        Returns
        -------
        float
            The result of a / b.

        Raises
        ------
        ValueError
            If b is equal to zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result
