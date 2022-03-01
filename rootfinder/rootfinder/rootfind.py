"""Calculate the roots of a quadratic equation."""

from typing import Tuple
from typing import Union


def calculate_quadratic_equation_roots(
    a: float, b: float, c: float
) -> Tuple[Union[float, complex], Union[float, complex]]:
    """Calculate the roots of a quadratic equation."""
    #  Use the source code example on page 21 of the
    # "Doing Math with Python" to implement this function.
    D = (b * b - 4 * a * c) ** 0.5
    # Your function should take as input the values
    # of a, b, and c and return the values of x_one
    # and x_two as a two-tuple of values.
    x_one = (-b + D) / (2 * a)
    x_two = (-b - D) / (2 * a)
    return x_one, x_two
    # The return values of this function can either
    # be a complex number (i.e., involving an imaginary
    # number and designated with j) or a floating-point
    # value (i.e., not involving an imaginary number and
    # instead only a decimal value)
