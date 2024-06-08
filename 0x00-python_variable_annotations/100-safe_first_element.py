#!/usr/bin/env python3
'''
first eeelement of a sequence
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    it Retrieves the first element of a sequence if it exists
    '''
    if lst:
        return lst[0]
    else:
        return None

