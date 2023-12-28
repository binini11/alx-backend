#!/usr/bin/env python3
"""
write a function named index_range that takeds two intger arguments page asn page_size.
the function should return a tuple of size two cintaining a stat index aand an end index
cronpinding to the range id indexes to return in a list for those particular pagination parameters

page numbers are 1-indexed the first page is page 1.
"""

from typing import Tuple

def index_range(page: int,  page_size: int) -> Tuple[int, int]:
    """
    start index and an end index corrospongid to the range if
    """
    #if page is 1,start at 0 and end at page_size
    #if page is 2,start at((page-1) * page_size) and 
    #end at (page_size * page)
    #if page is 3,start at ((page-1) * (page_size) and 
    #end at (page_size * page)

    return ((page - 1) * page_size, page_size * page)
