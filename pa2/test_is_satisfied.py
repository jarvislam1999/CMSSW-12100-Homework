'''
Schelling Model of Housing Segregation

Automatically added to test code for is_satisfied

Handle the fact that the test code may not be in the same directory as
schelling.py
'''

import os
import sys
import pytest

sys.path.append(os.getcwd())

#pylint: disable-msg=wrong-import-position
import utility
import schelling

EPS = 0.000001

#pylint: disable-msg=too-many-arguments
def helper_test_is_satisfied(filename, R, location, M_threshold,
                             B_threshold, expected):
    '''
    Check result of calling is_satisfied on the specified
    location with in an R-neighborhood with the specified threshold.

    Inputs:
        filename: (string) name of the input grid file
        R: (integer) neighborhood parameter
        location: (pair of integers) location in the grid to be tested
        M_threshold: lower bound for similarity score for maroon homeowners
        B_threshold: lower bound for similarity score for blue homeowners
        expected: (float) expected result.
    '''
    grid = utility.read_grid(filename)

    actual = schelling.is_satisfied(grid, R, location, M_threshold, B_threshold)
    if actual != expected:

        s = "Actual value ({}) is not equal to the expected value ({}).\n"
        s = s + "    @ location {} with R-{:d} neighborhoods.\n"
        pytest.fail(s.format(actual, expected, location, R))

# Generated code

def test_0():
    ''' Check boundary neighborhood: top right corner. '''
    filename = "tests/a18-sample-grid.txt"
    helper_test_is_satisfied(filename, 0, (0, 4), 0.8, 0.9, True)

def test_1():
    ''' Check boundary neighborhood: top right corner. '''
    filename = "tests/a18-sample-grid.txt"
    helper_test_is_satisfied(filename, 1, (0, 4), 0.7, 0.8, False)

def test_2():
    ''' Check boundary neighborhood: top right corner. '''
    filename = "tests/a18-sample-grid.txt"
    helper_test_is_satisfied(filename, 2, (0, 4), 0.5, 0.55, True)

def test_3():
    ''' Check boundary neighborhood: lower left corner. '''
    filename = "tests/a18-sample-grid.txt"
    helper_test_is_satisfied(filename, 0, (4, 0), 0.9, 0.95, True)

def test_4():
    ''' Check boundary neighborhood: lower left corner. '''
    filename = "tests/a18-sample-grid.txt"
    helper_test_is_satisfied(filename, 1, (4, 0), 0.8, 0.85, True)

def test_5():
    '''
    Check boundary neighborhood: lower left corner and difference
    between M and B thresholds.
    '''
    filename = "tests/a18-sample-grid.txt"
    helper_test_is_satisfied(filename, 2, (4, 0), 0.4, 0.5, True)

def test_6():
    ''' Check interior R-0 neighborhood.'''
    filename = "tests/a18-sample-grid.txt"
    helper_test_is_satisfied(filename, 0, (1, 1), 0.3, 0.7, True)

def test_7():
    ''' Check neighborhood that is complete when R is 1. '''
    filename = "tests/a18-sample-grid.txt"
    helper_test_is_satisfied(filename, 1, (1, 1), 0.2, 0.25, True)

def test_8():
    ''' Check neighborhood that is not complete when R is 2.'''
    filename = "tests/a18-sample-grid.txt"
    helper_test_is_satisfied(filename, 2, (1, 1), 0.9, 0.9, False)

def test_9():
    ''' Check larger neighborhood.'''
    filename = "tests/a18-sample-grid.txt"
    helper_test_is_satisfied(filename, 2, (2, 3), 0.5, 0.6, True)

def test_10():
    '''
    Check interior neighborhood with location that has no other neighbors.
    '''
    filename = "tests/grid-no-neighbors.txt"
    helper_test_is_satisfied(filename, 1, (2, 2), 0.2, 0.7, True)

def test_11():
    '''
    Check neighborhood with location
    that has no other neighbors.
    '''
    filename = "tests/grid-no-neighbors.txt"
    helper_test_is_satisfied(filename, 1, (4, 4), 0.5, 0.7, True)

def test_12():
    '''
    Check boundary neighborhood (lower right corner) with location
    that has a few neighbors.
    '''
    filename = "tests/grid-no-neighbors.txt"
    helper_test_is_satisfied(filename, 2, (4, 4), 0.3, 0.4, False)
