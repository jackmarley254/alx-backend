#!/usr/bin/env python3
"""function named index_range that takes two integer arguments
page and page_size."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
