#!/usr/bin/env python3
'''More involved type annotations'''
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping[Any, Any]): The dictionary to search.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None]): The default value to return if the key
                                  is not found.

    Returns:
        Union[Any, T]: The value from the dictionary if the key is found,
                       otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
