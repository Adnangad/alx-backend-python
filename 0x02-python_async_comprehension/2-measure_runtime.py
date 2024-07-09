#!/usr/bin/env python3
"""
Module that calculates the measure time for 4 parallel operations.
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures the time it takes to complete 4 async_comp routines
    """
    start: float = time.time()
    batch = asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension())
    rez_1, rez_2, rez_3, rez_4 = await batch
    end: float = time.time()
    time_taken: float = end - start
    return time_taken
