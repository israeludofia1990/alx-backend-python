#!/usr/bin/env python3
'''Duck typing - first element of a sequence'''
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a list if it exists, otherwise return None.

    This function safely returns the first element of a given list.
    If the list is empty or None, it returns None instead of raising an error.

    Args:
        lst (list): A list of elements of any type.

    Returns:
        Any or None: The first element of the list if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
