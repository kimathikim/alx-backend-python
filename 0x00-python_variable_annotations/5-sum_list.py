#!/usr/bin/env python3
'''A type annotated sum_list function'''
import typing


def sum_list(input_list: typing.List[float]) -> float:
    '''A type annotated sum_list function'''
    return sum(map(float, input_list))
