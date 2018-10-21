# -*- coding: utf-8 -*-
"""Utility functions

This module defines utility functions and
variables that will be useful for you throughout
the assignment. There are various printing, loading
and comparison functions defined below.
"""

from datetime import datetime as dt
from datetime import date
import sys
import json

# DO NOT REMOVE THIS LINE OF CODE
# pylint: disable-msg=unused-argument, too-few-public-methods
# pylint: disable-msg=invalid-name, len-as-condition, too-many-locals


def cmp_to_key(mycmp):
    '''
    Convert a cmp= function into a key= function
    From: https://docs.python.org/3/howto/sorting.html
    '''

    class KeyComparison:
        '''
        Comparison key class
        '''
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return KeyComparison


def cmp_count_tuples(t0, t1):
    '''
    Compare pairs using the second value as the primary key and the
    first value as the secondary key.  Order the primary key in
    non-increasing order and the secondary key in non-decreasing
    order.

    Inputs:
        t0: pair
        t1: pair

    Returns: -1, 0, 1

    Sample uses:
        cmp(("A", 3), ("B", 2)) => -1

        cmp(("A", 2), ("B", 3)) => 1

        cmp(("A", 3), ("B", 3)) => -1

        cmp(("A", 3), ("A", 3))
    '''
    (key0, val0) = t0
    (key1, val1) = t1
    if val0 > val1:
        return -1
    elif val0 < val1:
        return 1
    elif key0 < key1:
        return -1
    elif key0 > key1:
        return 1
    return 0


def sort_count_pairs(l):
    '''
    Sort pairs using the second value as the primary sort key and the
    first value as the seconary sort key.

    Inputs:
       l: list of pairs.

    Returns: list of key/value pairs
    '''
    return sorted(l, key=cmp_to_key(cmp_count_tuples))


def grab_year_month(date_str):
    '''
    Extract the year and month from a twitter date string.

    Input:
       date_str: string in the format used by twitter for
          dates.
    Returns: (integer year, integer month)
    '''
    d = dt.strptime(date_str, "%a %b %d %H:%M:%S %z %Y")
    return (d.year, d.month)


def pretty_print_by_month(results):
    '''
    Print result of find_top_k_ngrams_per_month in
    a readable format.

    Input:
        results: list of the form:
           [((year, month), list of ngrams),
            ((year, month), list of ngrams),
            ...
            ((year, month), list of ngrams)]
    '''
    fill_width = 16

    # Convert dates and ngrams to strings and find the longest ngram
    # string.
    longest = 0
    massaged = []
    for ((year, month), tuples) in results:
        # Convert year and month integers to
        # Month Year as strings
        d = date(year, month, 1)
        d_str = (d.strftime("%B %Y") + ":").ljust(fill_width, " ")

        # Convert ngrams to strings.
        row = []
        for (ngram, count) in tuples:
            s = " ".join(ngram)
            row.append((s, count))
            longest = max(longest, len(s))

        massaged.append((d, d_str, row))

    # Add two for padding
    longest = longest + 2

    # print result
    for (_, date_str, ngrams) in sorted(massaged):
        if len(ngrams) == 0:
            print(date_str)
        else:
            print(date_str, ngrams[0][0].ljust(longest, " "), ngrams[0][1])
            for (ngram, count) in ngrams[1:]:
                print(" " * fill_width, ngram.ljust(longest, " "), count)
        print()


def get_json_from_file(filename):
    '''
    Read data from a JSON file.
    '''

    try:
        return json.load(open(filename))
    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
