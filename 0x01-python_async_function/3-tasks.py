#!/usr/bin/env python3
"""regular function"""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    takes an integer max_delay and returns a asyncio.Task
    """
    T = create_task(wait_random(max_delay))
    return T
