#!/usr/bin/env python3
""" returns an index range """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """ function that computes particula pagination parameter """
    return ((page * page_size) - page_size, page * page_size)
