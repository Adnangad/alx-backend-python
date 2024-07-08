#!/usr/bin/env python3
"""
This module contains an async function that returns a list.
"""
import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Args:
    n: the number of loops
    max_delay: the number.
    """
    ls = []
    for _ in range(0, n):
        x = await wait_random(max_delay)
        ls.append(x)
    j = n
    while j > 0:
        j = j - 1
        for x in range(0, len(ls) - 1):
            if ls[x + 1] < ls[x]:
                temp = ls[x]
                ls[x] = ls[x + 1]
                ls[x + 1] = temp
    return ls
