#!/usr/bin/env python3
'''
Let's duck type as an iterable object
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Computes the length
    '''
    return [(i, len(i)) for i in lst]
