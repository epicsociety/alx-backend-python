#!/usr/bin/env python3
"""
Module contains an asynchronous coroutine
"""


import asyncio
import random
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronous coroutine that takes in 2 integer arguments,
    spawn wait_random n times with the specified max_delay,
    Return:  list of all the delays (float values)
    """
    delays_list = []

    for i in range(n):
        delay = await asyncio.gather(task_wait_random(max_delay))
        delays_list.append(delay[0])
    return sorted(delays_list)
