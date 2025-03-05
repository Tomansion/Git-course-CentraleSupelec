from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The difference of the two numbers.
    """
    return a - b


def Multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Mutlpity two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The multiplication of the two numbers.
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divide two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The division of the two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
