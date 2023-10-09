#!/usr/bin/env python3
"""
Module contains an asynchronous coroutine
"""


import asyncio
from typing import Coroutine
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Coroutine:
    """
    returns asyncio.Task
    Args:
        max_delay: int
    Return: asyncio.Task
    """

    return asyncio.create_task(wait_random(max_delay))
