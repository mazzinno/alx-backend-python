#!/usr/bin/env python3
'''
now More involved type annotations
'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''
    it Retrieves a value from a dict using a given key
    '''
    if key in dct:
        return dct[key]
    else:
        return default

