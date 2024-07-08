#!/usr/bin/env python3
"""
This module contains a function that measures the runtime of operations
"""
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Args:
    n: the number
    max_delay: the number to be used as an arg
    """
    ls = asyncio.run(wait_n(n, max_delay))
    rez = sum(ls) / n
    return rez
