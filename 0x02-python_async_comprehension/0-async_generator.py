#!/usr/bin/env python3
"""
This module contains an async gen function that generats numbers.
"""
import typing
import asyncio
import random


async def async_generator() -> typing.AsyncGenerator[int, None]:
    """
    Yields numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
