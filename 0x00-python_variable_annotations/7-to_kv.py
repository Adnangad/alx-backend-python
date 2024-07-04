#!/usr/bin/env python3
"""
This module returns a tuple from given args.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
    k: str
    v: an int or float
    """
    a = (k, v * v)
    return a
