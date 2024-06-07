#!/usr/bin/env python3
'''A type annotated safe_first_element function'''
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[
        typing.Any, None]:
    '''A type annotated safe_first_element function'''
    if lst:
        return lst[0]
    else:
        return None
