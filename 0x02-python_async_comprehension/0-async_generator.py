#!/usr/bin/env python3
'''
will loop 10 times, each time asynchronously wait 1 second
'''
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    '''
    coroutine will loop 10 times.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
