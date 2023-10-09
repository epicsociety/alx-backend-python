#!/usr/bin/env python3
"""
Module contains an asynchronous coroutine
"""


import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay)
    Args:
        int n
        int max_delay as arguments
    Return: total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
