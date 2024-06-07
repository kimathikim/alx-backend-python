#!/usr/bin/env python3
'''A type annotated sum_list function'''


def sum_list(input_list: list) -> float:
    '''A type annotated sum_list function'''
    return sum(map(float, input_list))
