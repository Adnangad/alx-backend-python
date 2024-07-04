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
    return lambda x: x * multiplier
