#!/usr/bin/env python3
"""
This module sums the elements in a mixed int and float list.
"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """
    Args:
    mxd_lst: a list of floats.
    """
    a = 0.00
    for i in mxd_lst:
        a = a + i
    return a
