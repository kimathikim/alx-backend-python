#!/usr/bin/env python3
'''A type annotated make_multiplier function'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''A type annotated make_multiplier function'''
    def multiply(n: float) -> float:
        '''A type annotated multiply function'''
        return n * multiplier
    return multiply
