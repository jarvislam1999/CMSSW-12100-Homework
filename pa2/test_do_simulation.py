'''
Schelling Model of Housing Segregation

Test code for do_simulation
'''

import os
import sys
import pytest


# Handle the fact that the grading code may not
# be in the same directory as schelling.py
sys.path.append(os.getcwd())

#pylint: disable-msg=wrong-import-position
from schelling import do_simulation
import utility

# Get the test files from the same directory as
# this file.
BASE_DIR = os.path.dirname(__file__)

def count_homeowners(grid):
    '''
    Count the number of occupied homes:

    Inputs:
        grid: (list of lists of strings) the grid

    Returns: integer
    '''

    num_homeowners = 0
    for row in grid:
        for home in row:
            if home != "O":
                num_homeowners += 1
    return num_homeowners


#pylint: disable-msg=too-many-arguments
#pylint: disable-msg=too-many-locals
def helper(input_filename, expected_filename, R, M_threshold,
           B_threshold, max_num_steps, expected_num_relocations):
    '''
    Do one simulation with the specified parameters (R, threshold,
    max_num_steps) starting from the specified input file.  Match
    actual grid generated with the expected grid and match expected
    steps and actual steps.

    Inputs:
        input_filename: (string) name of the input grid file
        expected_filename: (string) name of the expected grid file.
        R: (int) radius for the neighborhood
        M_threshold: lower bound for similarity score for maroon homeowners
        B_threshold: lower bound for similarity score for blue homeowners
        max_steps: (int) maximum number of steps to do
        expected_num_relocations: (int) expected number of relocations
            performed during the simulation
    '''

    input_filename = os.path.join(BASE_DIR, input_filename)
    actual_grid = utility.read_grid(input_filename)
    expected_num_homeowners = count_homeowners(actual_grid)
    opens = utility.find_opens(actual_grid)

    actual_num_relocations = do_simulation(actual_grid, R, M_threshold, B_threshold,
                                     max_num_steps, opens)
    actual_num_homeowners = count_homeowners(actual_grid)

    expected_filename = os.path.join(BASE_DIR, expected_filename)
    expected_grid = utility.read_grid(expected_filename)

    if actual_num_relocations != expected_num_relocations:
        s = ("actual and expected values number of relocations do not match\n"
             "  got {:d}, expected {:d}")
        s = s.format(actual_num_relocations, expected_num_relocations)
        pytest.fail(s)

    if actual_num_homeowners != expected_num_homeowners:
        if actual_num_homeowners <= expected_num_homeowners:
            s = "Homeowners are fleeing the city!\n"
        else:
            s = ("The city is gaining homeowners.\n")
        s += ("  Actual number of homeowners: {:d}\n"
              "  Expected number of homeowners: {:d}\n")
        s = s.format(actual_num_homeowners, expected_num_homeowners)

        pytest.fail(s)

    mismatch = utility.find_mismatch(actual_grid, expected_grid)
    if mismatch:
        (i, j) = mismatch
        s = ("actual and expected grid values do not match "
             "at location ({:d}, {:d})\n")
        s = s.format(i, j)
        s = s + "  got {}, expected {}".format(actual_grid[i][j],
                                               expected_grid[i][j])
        pytest.fail(s)


def test_0():
    ''' Check stopping condition #1 '''
    input_fn = "tests/a18-sample-grid.txt"
    output_fn = "tests/a18-sample-grid-1-33-33-0-final.txt"
    helper(input_fn, output_fn, 1, 0.33, 0.33, 0, 0)

def test_1():
    ''' Check stopping condition #2 '''
    input_fn = "tests/a18-sample-grid.txt"
    output_fn = "tests/a18-sample-grid-1-33-33-3-final.txt"
    helper(input_fn, output_fn, 1, 0.33, 0.33, 3, 2)

def test_2():
    ''' Check choosing among acceptable locations. '''
    input_fn = "tests/a18-sample-grid.txt"
    output_fn = "tests/a18-sample-grid-1-60-40-1-final.txt"
    helper(input_fn, output_fn, 1, 0.6, 0.40, 1, 5)

def test_3():
    ''' Check choosing among acceptable locations. '''
    input_fn = "tests/a18-sample-grid.txt"
    output_fn = "tests/a18-sample-grid-1-60-40-2-final.txt"
    helper(input_fn, output_fn, 1, 0.6, 0.40, 2, 6)

def test_4():
    ''' Check case where there are no suitable homes. '''
    input_fn = "tests/grid-sea-of-red.txt"
    output_fn = "tests/grid-sea-of-red-1-40-70-1-final.txt"
    helper(input_fn, output_fn, 1, 0.4, 0.7, 1, 0)

def test_5():
    '''
    Check case where possible new location is in the homeowner's
    current neighborhood.
    '''

    input_fn = "tests/a18-sample-grid.txt"
    output_fn = "tests/a18-sample-grid-1-75-25-1-final.txt"
    helper(input_fn, output_fn, 1, 0.75, 0.25, 1, 6)

def test_6():
    ''' Check that the different thresholds are recognized. '''
    input_fn = "tests/a18-sample-grid.txt"
    output_fn = "tests/a18-sample-grid-1-30-50-1-final.txt"
    helper(input_fn, output_fn, 1, 0.30, 0.50, 1, 5)

def test_7():
    ''' Check that the different thresholds are recognized. '''
    input_fn = "tests/a18-sample-grid.txt"
    output_fn = "tests/a18-sample-grid-1-50-30-1-final.txt"
    helper(input_fn, output_fn, 1, 0.50, 0.30, 1, 2)

def test_8():
    ''' Check sample grid with R of 2. '''
    input_fn = "tests/a18-sample-grid.txt"
    output_fn = "tests/a18-sample-grid-2-44-70-7-final.txt"
    helper(input_fn, output_fn, 2, 0.44, 0.7, 7, 0)

def test_9():
    ''' Check choosing among equidistant locations. '''
    input_fn = "tests/grid-ties.txt"
    output_fn = "tests/grid-ties-2-33-70-2-final.txt"
    helper(input_fn, output_fn, 2, 0.33, 0.70, 2, 4)

def test_10():
    ''' Check whether more recently vacant homes are preferred. '''
    input_fn = "tests/grid-ten.txt"
    output_fn = "tests/grid-ten-2-40-65-2-final.txt"
    helper(input_fn, output_fn, 2, 0.40, 0.65, 2, 21)

def test_11():
    ''' Check 4 steps of a medium-size grid. '''
    input_fn = "tests/grid-ten.txt"
    output_fn = "tests/grid-ten-2-32-62-4-final.txt"
    helper(input_fn, output_fn, 2, 0.32, 0.62, 4, 23)

def test_12():
    ''' Check a larger R. '''
    input_fn = "tests/grid-ten.txt"
    output_fn = "tests/grid-ten-3-32-62-4-final.txt"
    helper(input_fn, output_fn, 3, 0.32, 0.62, 4, 1)


@pytest.mark.timeout(30)
@pytest.mark.large
def test_13():
    ''' Check a large grid. '''
    input_fn = "tests/large-grid.txt"
    output_fn = "tests/large-grid-2-33-70-20-final.txt"
    helper(input_fn, output_fn, 2, 0.33, 0.7, 20, 188)
