#!/usr/bin/env python3
import math


class Server:
    # ...

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Get a page of the dataset and return a dictionary
        containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        dataset = self.get_page(page, page_size)
        total_pages = int(math.ceil(len(self.dataset()) / page_size))
        next_page = None
        prev_page = None

        if page < total_pages:
            next_page = page + 1
        if page > 1:
            prev_page = page - 1

        return {
            'page_size': len(dataset),
            'page': page,
            'data': dataset,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
