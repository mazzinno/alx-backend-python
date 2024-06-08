#!/usr/bin/env python3

'''
Complex types - functions
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Returning a function
    '''
    def multiplier_func(number: float) -> float:
        return number * multiplier
    return multiplier_func
