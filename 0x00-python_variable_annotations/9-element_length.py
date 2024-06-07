#!/usr/bin/env python3
'''A type annotated element_length function'''
from typing import Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    return [(i, len(i)) for i in lst]