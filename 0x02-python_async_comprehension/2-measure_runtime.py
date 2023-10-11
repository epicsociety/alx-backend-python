#!/usr/bin/env python3
"""
Implementation of Async Comprehension
"""


import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel
    using asyncio.gather
    args: None
    return: sum(float)
    """
    start_time = asyncio.get_event_loop().time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
