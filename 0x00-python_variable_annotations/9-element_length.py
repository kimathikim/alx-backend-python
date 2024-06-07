#!/usr/bin/env python3
'''A type annotated element_length function'''
import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]) -> typing.List[
        typing.Tuple[typing.Sequence, int]]:
    '''A type annotated element_length function'''
    return [(i, len(i)) for i in lst]
