import pytest

# Zadanie 1 
# Testowanie guens_number.py
# 1. OK
# 2. OK
# 3. OK
# 4. OK
# 5. OK
# 6. OK
# 7. OK
# 8. Brak komunikatu o błędzie (należy dodać ewentualność)
# 9. OK
# 10. Nie można podac przedzialu zaczynajacego sie nie od 0 ponieważ uzytkownik moze podac jedynie górną granice.
# 11. Brak komunikatu o błędzie (należy dodać ewentualność)


# Zadanie 2
# Testowanie passwgen.py
# 1. OK
# 2. OK
# 3. OK
# 4. OK
# 5. OK
# 6. OK
# 7. OK
# 8. OK
# 9. Program nie obsługuje błędnych danych wejściowych (np. ujemnej długości hasła, niepoprawnych znaków) nie prosi o podanie prawidłowych.
# 10. Program ignoruje błędne znaki wejściowe przy pytaniach i kontynuuje działanie z domyślną wartością "nie".

# Zadanie 3
def combine_strings(str1,str2):
    return str1 + str2

def test_combine_strings():
    assert combine_strings("Hello", "World") == "HelloWorld"
    assert combine_strings("Python", "0Programming") == "Python0Programming"
    assert combine_strings("", "") == ""
    assert combine_strings("Test", "") == "Test"
    assert combine_strings("", "Test") == "Test"
    

# Zadanie 4
def max_out_of_3(a, b, c):
    if any(not isinstance(i, (int, float)) for i in [a, b, c]):
        return "All inputs must be numbers"
    return max(a, b, c)

def test_max_out_of_3():
    assert max_out_of_3(1, 2, 3) == 3
    assert max_out_of_3(5, 5, 5) == 5
    assert max_out_of_3(-1, -2, -3) == -1
    assert max_out_of_3('a', 1, 'c') == "All inputs must be numbers"
    assert max_out_of_3(10, 20, 30) == 30
    

# Zadanie 5
def all_even(numbers):
    """
    Check if all numbers in the list are even.

    Args:
        numbers (list): A list of numbers to check.

    Returns:
        bool: True if all numbers are even, False otherwise.
    >>> all_even([2, 4, 6])
    True
    >>> all_even([1, 2, 3])
    False
    >>> all_even([])
    True
    >>> all_even([-2, -4, -6])
    True
    >>> all_even([0,0,0])
    True
    """
    return all(num % 2 == 0 for num in numbers)

# Zadanie 6
def x_count_in_list(x,arr):
    """Count occurrences of x in arr.

    Args:
        x (any): The element to count.
        arr (list): The list in which to count occurrences of x.
    
    Returns:
        int: The count of occurrences of x in arr.
        
    >>> x_count_in_list(1, [1, 2, 3, 1])
    2
    >>> x_count_in_list(2, [1, 2, 3, 4])
    1
    >>> x_count_in_list('a', ['a', 1, 'b', 1])
    1
    >>> x_count_in_list(-1, [1, 1, 1])
    0
    >>> x_count_in_list('a', [])
    0
    """
    return arr.count(x)


# Zadanie 7
def nth_fibonacci(n):
    """Calculate the nth Fibonacci number.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
        
    >>> nth_fibonacci(0)
    0
    >>> nth_fibonacci(1)
    1
    >>> nth_fibonacci(2)
    1
    >>> nth_fibonacci(3)
    2
    >>> nth_fibonacci(4)
    3
    >>> nth_fibonacci(9)
    34
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# Zadanie 8
def is_prime(n):
    """Check if a number is prime.
    Args:
        n (int): Number to check if it is prime.
    Returns:
        bool: True if n is prime, False otherwise.
        
    >>> is_prime(0)
    False
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(-1)
    False
    >>> is_prime(97)
    True
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

    
# python -m pytest 152774_lab2.py
# python -m doctest -v 152774_lab2.py