#!/usr/bin/env python3

'''
More involved type annotations
'''

from typing import Union, Any, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''
    return dictionary key
    '''
    if key in dct:
        return dct[key]
    else:
        return default
