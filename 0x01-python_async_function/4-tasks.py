#!/usr/bin/env python3

'''
Let's execute multiple coroutines at the same time with async
'''

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    will Call wait_random n times
    '''

    result = []

    delays = [task_wait_random(max_delay) for time in range(n)]

    for sort in asyncio.as_completed(delays):
        val = await sort
        result.append(val)
    return result
