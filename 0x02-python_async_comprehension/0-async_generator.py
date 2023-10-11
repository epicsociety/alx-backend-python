#!/usr/bin/env python3
"""
Implementation of Async Comprehension
"""


from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[int, None, None]:
    """
    oop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    args: None
    Return: None
    Yield an int
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
