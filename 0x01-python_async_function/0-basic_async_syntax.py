#!/usr/bin/env python3
"""
This module contains a function thatreturns a value after a delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    x: float = random.uniform(0, max_delay + 1)
    await asyncio.sleep(x)
    return x
