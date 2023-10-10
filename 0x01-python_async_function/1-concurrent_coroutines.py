#!/usr/bin/env python3
"""
Module contains an asynchronous coroutine
"""


import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronous coroutine that takes in 2 integer arguments,
    spawn wait_random n times with the specified max_delay,
    Return:  list of all the delays (float values)
    """
    delays_list = []

    for i in range(n):
        delay = await asyncio.gather(wait_random(max_delay))
        delays_list.append(delay[0])
    return sorted(delays_list)
