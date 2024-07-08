#!/usr/bin/env python3
"""
This module uses a task function.
"""
import typing
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    ls = []
    for _ in range(0, n):
        x = await task_wait_random(max_delay)
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
