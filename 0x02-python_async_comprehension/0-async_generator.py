#!/usr/bin/env python3
"""coroutine"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """
    a coroutine function that takes no arguments
    """

    for item in range(10):
        await asyncio.sleep(1)
        yield(random.random() * 10)
