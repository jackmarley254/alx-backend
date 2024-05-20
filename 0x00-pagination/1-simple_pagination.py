#!/usr/bin/env python3
"""
Defines class Server that paginates a database of popular baby names
"""
import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Calculate the start and end indices of a range given a page number
        and page size.

        Parameters:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            tuple: A tuple containing the start index (int)
            and end index (int) of the range.
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Parameters:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            list: The page of the dataset.
        """
        assert isinstance(page, int) and isinstance(page_size, int), "Pages"
        assert page > 0 and page_size > 0, "Page and page_size "

        dataset = self.dataset()
        start_index, end_index = self.index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
