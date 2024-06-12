#!/usr/bin/env python3

'''
execute multiple coroutines at the same time with async
'''

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    This Call wait_random n times
    '''
    result = []

    # List of wait_random done n times
    delays = [wait_random(max_delay) for time in range(n)]

    # Loop delays in order of completion
    for sort in asyncio.as_completed(delays):
        val = await sort
        result.append(val)
    return result
