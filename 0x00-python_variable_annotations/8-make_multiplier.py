#!/usr/bin/env python3
'''Complex types - functions'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by the
    specified multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns it multiplied by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies the input by the outer function's multiplier.

        Args:
            x (float): The input float to be multiplied.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_function
