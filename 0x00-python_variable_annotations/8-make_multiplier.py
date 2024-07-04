#!/usr/bin/env python3
"""
This module contains a function that returns a callable object.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
    multiplier: the float to be multiplied.
    Returns:
    A function that multiplies its input by the multiplier.
    """
    def multiply(x: float) -> float:
        """
        Args:
        x: the float to be multiplied
        Returns:
        The result of x multiplied by multiplier.
        """
        return x * multiplier
    return multiply
