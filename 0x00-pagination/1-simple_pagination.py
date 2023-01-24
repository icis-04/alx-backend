#!/usr/bin/env python3
import csv
import math
from typing import Tuple, List,Callable


def index_range(page: int, page_size: int) -> Tuple[int]:
    """ function that computes particula pagination parameter """
    return ((page * page_size) - page_size, page * page_size)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """Gets a slice of a list dataset"""
            assert type(page) == int and type(page_size) == int
            assert page > 0 and page_size > 0
            start, end = index_range(page, page_size)
            result: Callable = self.dataset()
            if start > len(result) or end > len(result):
                return []
            else:
                return result[start:end]
