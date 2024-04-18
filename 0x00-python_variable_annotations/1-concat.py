#!/usr/bin/env python3
'''type annotation module'''


def concat(str1: str, str2: str) -> str:
    '''takes a string str1 and a string str2 as arguments
    and returns a concatenated string'''
    return "{}{}".format(str1, str2)
