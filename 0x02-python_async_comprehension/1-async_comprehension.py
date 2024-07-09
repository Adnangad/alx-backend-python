#!/usr/bin/env python3
"""
This module contains a fnction that implements an async comprehension
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns a list.
    """
    rez: List[float] = [i async for i in async_generator()]
    return rez
