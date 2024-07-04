#!/usr/bin/python3
"""
This module contains a function that returns a callable object.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
    multiplier: the float to be multiplied.
    """
    def multiply(x: float) -> float:
        """
        Args:
        x: the arg to be multiplied
        """
        return x * x
    return multiply
