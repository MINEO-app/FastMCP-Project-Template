"""Tool functions for the FastMCP Calculator service.

This module contains the mathematical operations exposed as tools in the MCP server.
Each tool is designed to work with floating-point numbers and return the result.
"""


def add(a: float, b: float) -> float:
    """Add two numbers together.

    Performs arithmetic addition of two numeric values.
    Supports both integers and floating-point numbers.

    Args:
        a: The first addend. Can be any real number.
        b: The second addend. Can be any real number.

    Returns:
        The sum of a and b (a + b).

    Example:
        >>> add(2.0, 3.0)
        5.0
        >>> add(-1.0, 1.0)
        0.0
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first.

    Performs arithmetic subtraction of the second operand from the first.
    Supports both integers and floating-point numbers.

    Args:
        a: The minuend (the number to subtract from). Can be any real number.
        b: The subtrahend (the number to subtract). Can be any real number.

    Returns:
        The result of a - b.

    Example:
        >>> subtract(10.0, 4.0)
        6.0
        >>> subtract(5.0, 9.0)
        -4.0
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers together.

    Performs arithmetic multiplication of two numeric values.
    Supports both integers and floating-point numbers.

    Args:
        a: The first factor. Can be any real number.
        b: The second factor. Can be any real number.

    Returns:
        The product of a and b (a * b).

    Example:
        >>> multiply(4.0, 5.0)
        20.0
        >>> multiply(-2.0, 3.0)
        -6.0
    """
    return a * b
