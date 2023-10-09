#!/usr/bin/env python3
"""
Module contains an asynchronous coroutine
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument,
    waits for a random delay between 0 and max_delay seconds,
    and returns it
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
