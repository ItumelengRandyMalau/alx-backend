#!/usr/bin/env python3
"""
Server class to paginate a database of popular baby names.
"""
import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the appropriate page of the dataset.
        """
        # Validate input using assert
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset_len = len(self.dataset())
        start_index, end_index = index_range(page, page_size)

        if start_index >= dataset_len:
            return []
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int,
            page_size: int) -> Dict[str, Union[int, List[List], None]]:
        """
        Returns a dictionary of pagination information.
        """
        data = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if index_range(page, page_size)[1] < total_rows else None

        total_pages = math.ceil(total_rows / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
