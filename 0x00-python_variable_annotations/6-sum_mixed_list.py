#!/usr/bin/env python3
'''
imixed list
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Computes the sum - list of integers and floating-point numbers
    '''
    return float(sum(mxd_lst))
