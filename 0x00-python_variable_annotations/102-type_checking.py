#!/usr/bin/env python3
'''Type Checking'''
from typing import Tuple, Any, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into the elements of the input
    tuple by repeating each element multiple times.

    Args:
        lst (Tuple[int, ...]): The input tuple containing integers.
        factor (int, optional): The factor by which each element
        in the input tuple is repeated. Defaults to 2.

    Returns:
        Tuple[int, ...]: A tuple containing the elements of the input
        tuple, where each element is repeated 'factor' times.
        """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
