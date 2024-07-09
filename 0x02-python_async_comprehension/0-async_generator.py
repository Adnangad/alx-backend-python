#!/usr/bin/env python3
"""
This module contains an async gen function that generats numbers.
"""
import asyncio
import random


async def async_generator():
    """
    Yields numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
