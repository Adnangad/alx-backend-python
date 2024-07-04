#!/usr/bin/env python3
"""
This module contains a module.
"""
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
    lst: a list.
    """
    return [(i, len(i)) for i in lst]
