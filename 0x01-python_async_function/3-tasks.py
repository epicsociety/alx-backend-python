#!/usr/bin/env python3
"""
Module contains an asynchronous coroutine
"""


import asyncio
from typing import Coroutine
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Coroutine:
    """
    Utilizes create_task method from asyncio class
    Args:
        max_delay: int
    Return: asyncio.Task
    """

    return asyncio.create_task(wait_random(max_delay))
