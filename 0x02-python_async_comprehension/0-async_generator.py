#!/usr/bin/env python3
'''Async Generator'''
import asyncio
from typing import Generato
import random


async def async_generator() -> Generator[float, None, None]:
    '''coroutine called async_generator that takes no arguments.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
