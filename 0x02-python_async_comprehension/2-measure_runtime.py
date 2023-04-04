#!/usr/bin/env python3
"""coroutine"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    a measure_runtime coroutine that will execute
    async_comprehension four times in parallel using asyncio.gather
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension())
    end = time.perf_counter()
    total_time = end - start
    return total_time
