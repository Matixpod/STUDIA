import pytest

def combine_strings(str1,str2):
    return str1 + str2

def max_out_of_3(a, b, c):
    if all(isinstance(i, str) for i in [a, b, c]):
        return "All inputs must be numbers"
    return max(a, b, c)

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
    >>> all_even([a, b, c])
    False
    """
    if not all(isinstance(num, (int)) for num in numbers):
        return False
    
    # ! Poprawic
    return all(num % 2 == 0 for num in numbers)


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
    False
    >>> x_count_in_list(-1, [1, 1, 1])
    0
    >>> x_count_in_list('a', [])
    0
    """
    return arr.count(x)

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

# def is_prime(n):
    """Check if a number is prime.
    

    Args:
        n (int): Number to check if it is prime.
    
    Returns:
        bool: True if n is prime, False otherwise.
    """
    # if n > 1:
    #     for i in range(2,)

def test_combine_strings():
    assert combine_strings("Hello", "World") == "HelloWorld"
    assert combine_strings("Python", "0Programming") == "Python0Programming"
    assert combine_strings("", "") == ""
    assert combine_strings("Test", "") == "Test"
    assert combine_strings("", "Test") == "Test"
    
    
    
def test_max_out_of_3():
    assert max_out_of_3(1, 2, 3) == 3
    assert max_out_of_3(5, 5, 5) == 5
    assert max_out_of_3(-1, -2, -3) == -1
    assert max_out_of_3('a', 'v', 'c') == "All inputs must be numbers"
    assert max_out_of_3(10, 20, 30) == 30
    

    
    
    
    
# python -m pytest 152774_lab2.py
# python -m doctest -v 152774_lab2.py