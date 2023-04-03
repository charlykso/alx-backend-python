#!/usr/bin/env python3
"""alter wait_n  function"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
      The code is nearly identical to wait_n
      except task_wait_random is being called.
     """
    delays = []
    for x in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
    delays = sorted(delays)
    return delays
