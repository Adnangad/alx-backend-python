#!/usr/bin/env python3
"""
This module contains a fnction that implements an async comprehension
"""
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Returns a list.
    """
    rez = [i async for i in async_generator()]
    return rez
