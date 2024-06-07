#!/usr/bin/env python3
'''A type annotated to_kv function'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''A type annotated to_kv function'''
    return (k, v * v)
