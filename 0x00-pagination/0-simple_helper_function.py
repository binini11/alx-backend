#!/usr/bin/env python3
"""
This module provides a function to calculate the start and end index for a given page and page size.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.

    Parameters:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index

