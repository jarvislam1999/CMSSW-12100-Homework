'''
Test code for Modeling Epidemics

Emma Nechamkin and Anne Rogers
July 2018

Borja Sotomayor
September 2018
'''

import os
import sys
import random

import pytest

import sir
import util

EPS = 0.000000001

# Handle the fact that the grading code may not
# be in the same directory as sir.py
sys.path.append(os.getcwd())

# Get the name of the directory that holds the grading code.
BASE_DIR = os.path.dirname(__file__)
TEST_DATA_DIR = os.path.join(BASE_DIR, "configs")
# I haven't stored this yet


def gen_check_rand_calls(seed, max_num_calls):
    '''
    Generate a function that can be used to check whether the correct
    number of calls were made to the random number generator.


    Inputs:
      seed (int): the seed for the random number generator
      max_num_calls (int): the maximum number of calls to
         random.random() that will need to be verified.

    Returns: function of one variable
    '''

    random.seed(seed)
    rand_vals = [random.random() for i in range(max_num_calls+1)]

    def check(expected_num_calls):
        '''
        Check whether the expected number of calls to random.random()
        were made.

        Inputs:
          expected_num_calls: the number of calls that should have
          been made.

        Returns: boolean that will be True if the check succeeded and
          False otherwise and, if necessary, an error message as a
          string.
        '''
        assert expected_num_calls <= max_num_calls

        # Make a call to random.
        actual_r = random.random()
        expected_r = rand_vals[expected_num_calls]

        # Did the call to random yield the expected value?
        if actual_r == pytest.approx(expected_r):
            return True, None

        for i, r in enumerate(rand_vals):
            if actual_r == pytest.approx(r):
                if i < expected_num_calls:
                    return False, "Not enough calls to random.random()"
                return False, "Too many calls to random.random()"

        return False, "Bug in test code?"

    return check


check_rand_20170217 = gen_check_rand_calls(20170217, 2)

################## Task 1: Count number of infected people #################

def helper_count_infected(city, expected):
    '''
    Purpose: helper function for task 1

    Inputs:
        city: (list) sir.py parameter for starting state
    '''

    n = sir.count_infected(city)

    if n != expected:
        s = "City {} has {} infected people, but count_infected returned {}"
        pytest.fail(s.format(city, expected, n))


def test_count_infected_1():
    '''
    Cities with no infected people
    '''
    helper_count_infected(["S", "S", "S", "S"], 0)
    helper_count_infected(["R", "R", "R", "R"], 0)
    helper_count_infected(["R", "S", "R", "S"], 0)
    helper_count_infected(["R"] * 20, 0)
    helper_count_infected(["S"] * 20, 0)
    helper_count_infected(["R", "S"] * 10, 0)


def test_count_infected_2():
    '''
    Cities with some I1 (but no I0) infected people.
    '''
    helper_count_infected(["I1", "S", "S", "S"], 1)
    helper_count_infected(["S", "I1", "S", "S"], 1)
    helper_count_infected(["S", "S", "I1", "S"], 1)
    helper_count_infected(["S", "S", "S", "I1"], 1)
    helper_count_infected(["I1", "R", "R", "R"], 1)
    helper_count_infected(["R", "I1", "R", "R"], 1)
    helper_count_infected(["R", "R", "I1", "S"], 1)
    helper_count_infected(["R", "R", "R", "I1"], 1)
    helper_count_infected(["S", "I1", "I1", "S"], 2)
    helper_count_infected(["R", "I1", "I1", "R"], 2)
    helper_count_infected(["I1", "S", "S", "I1"], 2)
    helper_count_infected(["I1", "R", "R", "I1"], 2)
    helper_count_infected(["R", "I1", "S", "I1"], 2)
    helper_count_infected(["I1", "I1", "I1", "I1"], 4)
    helper_count_infected(["I1"] * 20, 20)


def test_count_infected_3():
    '''
    Cities with some I0 (but no I1) infected people.
    '''
    helper_count_infected(["I0", "S", "S", "S"], 1)
    helper_count_infected(["S", "I0", "S", "S"], 1)
    helper_count_infected(["S", "S", "I0", "S"], 1)
    helper_count_infected(["S", "S", "S", "I0"], 1)
    helper_count_infected(["I0", "R", "R", "R"], 1)
    helper_count_infected(["R", "I0", "R", "R"], 1)
    helper_count_infected(["R", "R", "I0", "S"], 1)
    helper_count_infected(["R", "R", "R", "I0"], 1)
    helper_count_infected(["S", "I0", "I0", "S"], 2)
    helper_count_infected(["R", "I0", "I0", "R"], 2)
    helper_count_infected(["I0", "S", "S", "I0"], 2)
    helper_count_infected(["I0", "R", "R", "I0"], 2)
    helper_count_infected(["R", "I0", "S", "I0"], 2)
    helper_count_infected(["I0", "I0", "I0", "I0"], 4)
    helper_count_infected(["I0"] * 20, 20)


def test_count_infected_4():
    '''
    Cities with both I1 and I0 infected people.
    '''
    helper_count_infected(["I0", "S", "I1", "S"], 2)
    helper_count_infected(["I1", "S", "I0", "S"], 2)
    helper_count_infected(["I0", "I0", "I1", "S"], 3)
    helper_count_infected(["I1", "I1", "I0", "S"], 3)
    helper_count_infected(["I1", "I1", "I0", "I0"], 4)
    helper_count_infected(["I0", "I0", "I1", "I1"], 4)
    helper_count_infected(["I0", "I1", "I0", "I1"], 4)
    helper_count_infected(["I1", "I0", "I1", "I0"], 4)
    helper_count_infected(["I0", "I1"] * 10, 20)


################## Task 2: has_an_infected_neighbor #################
def helper_has_an_infected_neighbor(city, position, expected_result):
    '''
    Purpose: helper function for task 2

    Inputs:
        city: (list) sir.py parameter for starting state
        position: (int) sir.py parameter for location in list
    '''

    actual_infection = sir.has_an_infected_neighbor(city, position)
    if actual_infection != expected_result:
        s = "Expected boolean ({:}) and actual boolean ({:}) do not match."
        pytest.fail(s.format(expected_result, actual_infection))


def test_has_an_infected_neighbor_1():
    '''
    Purpose: tests infected left neighbor
    '''

    # without wrap-around
    helper_has_an_infected_neighbor(
        ['I1', 'S', 'S'], 1, True)

    helper_has_an_infected_neighbor(
        ['I0', 'S', 'S'], 1, True)

    # with wrap-around
    helper_has_an_infected_neighbor(
        ['S', 'S', 'I0'], 0, True)

    helper_has_an_infected_neighbor(
        ['S', 'S', 'I1'], 0, True)


def test_has_an_infected_neighbor_2():
    '''
    Purpose: tests infected right neighbor
    '''

    # without wrap-around
    helper_has_an_infected_neighbor(
        ['R', 'S', 'I0'], 1, True)

    helper_has_an_infected_neighbor(
        ['R', 'S', 'I1'], 1, True)

    # with wrap-around
    helper_has_an_infected_neighbor(
        ['I1', 'S', 'S'], 2, True)

    helper_has_an_infected_neighbor(
        ['I0', 'S', 'S'], 2, True)

def test_has_an_infected_neighbor_3():
    '''
    Purpose: Similar to above tests, but with larger cities
    '''

    # Right infected, no wrap-around
    helper_has_an_infected_neighbor(
        ['R', 'S', 'S', 'I1'], 2, True)

    # Left infected, no wrap-around
    helper_has_an_infected_neighbor(
        ['R', 'I1', 'S', 'S'], 2, True)

    # Right infected, with wrap-around
    helper_has_an_infected_neighbor(
        ['I1', 'S', 'S', 'S'], 3, True)

    # Left infected, with wrap-around
    helper_has_an_infected_neighbor(
        ['S', 'R', 'S', 'I1'], 0, True)


def test_has_an_infected_neighbor_4():
    '''
    Purpose: tests non-infected neighbors
    '''

    helper_has_an_infected_neighbor(
        ['S', 'S', 'S'], 0, False)

    helper_has_an_infected_neighbor(
        ['R', 'S', 'R'], 1, False)

    helper_has_an_infected_neighbor(
        ['S', 'S', 'R'], 0, False)

    helper_has_an_infected_neighbor(
        ['I0', 'S', 'S', 'R'], 2, False)


def test_has_an_infected_neighbor_5():
    '''
    Purpose: tests both neighbors infected.
    '''

    helper_has_an_infected_neighbor(
        ['S', 'I0', 'I1'], 0, True)

    helper_has_an_infected_neighbor(
        ['I1', 'S', 'I0'], 1, True)

    helper_has_an_infected_neighbor(
        ['I0', 'I1', 'S'], 2, True)

def test_has_an_infected_neighbor_6():
    '''
    Purpose: check larger city
    '''

    city = ["S"] * 100
    city[27] = "I0"
    city[42] = "I1"
    city[99] = "R"

    helper_has_an_infected_neighbor(city, 26, True)
    helper_has_an_infected_neighbor(city, 43, True)
    helper_has_an_infected_neighbor(city, 0, False)


################## Task 3: determine infection ##################

def helper_gets_infected_at_position(city, position, infection_rate,
                                           expected_infection, num_rand_calls):
    '''
    Purpose: helper function for task 2

    Inputs:
        city: (list) sir.py parameter for starting state
        position: (int) sir.py parameter for location in list
        infection_rate: (float) sir.py parameter r
        expected_infection: (bool) expected value
        num_rand_calls: (int) expected number of calls to
          random.random()
    '''

    # use the same seed for all the tests
    random.seed(20170217)

    actual_infection = sir.gets_infected_at_position(city,
                                                           position,
                                                           infection_rate)
    if actual_infection != expected_infection:
        s = "Expected boolean ({:}) and actual boolean ({:}) do not match."
        pytest.fail(s.format(expected_infection, actual_infection))

    (check, msg) = check_rand_20170217(num_rand_calls)

    if not check:
        pytest.fail(msg)


def test_gets_infected_at_position_1():
    '''
    Purpose: Left neighbor is infected, susceptible person gets
    infected
    '''
    helper_gets_infected_at_position(
        ['S', 'S', 'I1'], 0, 0.5, True, 1)

def test_gets_infected_at_position_2():
    '''
    Purpose: Left neighbor is infected, susceptible person does not
    get infected
    '''
    helper_gets_infected_at_position(
        ['S', 'S', 'I1'], 0, 0.2, False, 1)


def test_gets_infected_at_position_3():
    '''
    Purpose: Right neighbor is infected, susceptible person gets infected
    '''
    helper_gets_infected_at_position(
        ['S', 'I1', 'S'], 0, 1.0, True, 1)


def test_gets_infected_at_position_4():
    '''
    Purpose: Right neighbor is infected, susceptible person does not
    get infected
    '''
    helper_gets_infected_at_position(
        ['S', 'I1', 'S'], 0, 0.2, False, 1)


def test_gets_infected_at_position_5():
    '''
    Purpose: Both neighbors are infected, susceptible person gets infected
    '''
    helper_gets_infected_at_position(
        ['S', 'I1', 'I1'], 0, 1.0, True, 1)


def test_gets_infected_at_position_6():
    '''
    Purpose: Both neighbors are infected, susceptible person does not
    gets infected
    '''
    helper_gets_infected_at_position(
        ['S', 'I1', 'I1'], 0, 0.2, False, 1)


def test_gets_infected_at_position_7():
    '''
    Purpose: No infected neighbors, does not get infected
             (and should not make a call to random.random())
    '''
    helper_gets_infected_at_position(
        ['S', 'R', 'S'], 0, 1.0, False, 0)


def test_gets_infected_at_position_8():
    '''
    Purpose: tests that the function works for multiple list lengths.
    '''
    helper_gets_infected_at_position(
        ['I1', 'S', 'S', 'S'], 2, 1.0, False, 0)


def test_gets_infected_at_position_9():
    '''
    Purpose: tests that the function works at multiple list positions.
        (middle position)
    '''
    # unhealthy person w/ infected 1st neighbors
    helper_gets_infected_at_position(
        ['I1', 'S', 'S'], 1, 0.5, True, 1)

    # healthy person w/ infected neighbors
    helper_gets_infected_at_position(
        ['I1', 'S', 'S'], 1, 0.2, False, 1)

    # unhealthy person w/ infected 2nd neighbors
    helper_gets_infected_at_position(
        ['R', 'S', 'I0'], 1, 0.5, True, 1)

    # healthy person w/ infected neighbors
    helper_gets_infected_at_position(
        ['R', 'S', 'I0'], 1, 0.2, False, 1)

    # unhealthy person w/ infected neighbors
    helper_gets_infected_at_position(
        ['I1', 'S', 'I0'], 1, 0.5, True, 1)

    # healthy person w/ infected neighbors
    helper_gets_infected_at_position(
        ['I1', 'S', 'I0'], 1, 0.2, False, 1)


def test_gets_infected_at_position_10():
    '''
    Purpose: tests that the function works at multiple list positions.
        (end position)
    '''
    # unhealthy person w/ infected 1st neighbor
    helper_gets_infected_at_position(
        ['R', 'I1', 'S'], 2, 0.5, True, 1)

    # healthy person w/ infected 1st neighbors
    helper_gets_infected_at_position(
        ['R', 'I1', 'S'], 2, 0.2, False, 1)

    # unhealthy person w/ infected 2nd neighbor
    helper_gets_infected_at_position(
        ['I1', 'S', 'S'], 2, 0.5, True, 1)

    # healthy person w/ infected 1st neighbors
    helper_gets_infected_at_position(
        ['I1', 'S', 'S'], 2, 0.2, False, 1)

    # unhealthy person w/ infected neighbors
    helper_gets_infected_at_position(
        ['I1', 'I1', 'S'], 2, 0.5, True, 1)

    # healthy person w/ infected neighbors
    helper_gets_infected_at_position(
        ['I1', 'I1', 'S'], 2, 0.2, False, 1)


def test_gets_infected_at_position_11():
    '''
    Purpose: test uninfected neighbors
    '''

    helper_gets_infected_at_position(
        ['S', 'S', 'S'], 0, 1.0, False, 0)

    helper_gets_infected_at_position(
        ['S', 'S', 'S'], 1, 1.0, False, 0)

    helper_gets_infected_at_position(
        ['S', 'S', 'S'], 2, 1.0, False, 0)


################## Task 4: Move simulation forward one day #################

def helper_simulate_one_day(city, infection_rate,
                            expected_city):
    '''
    Purpose: helper function for task 4

    Inputs:
        city: (list) sir.py parameter for starting state
        infection_rate: (float) sir.py parameter r
        expected_city: (list) expected value
    '''
    new_city = sir.simulate_one_day(city, infection_rate)
    if new_city != expected_city:
        s = "Expected new state ({}) and actual new state ({}) do not match."
        pytest.fail(s.format(expected_city, new_city))


def test_simulate_one_day_1():
    '''
    Purpose: check that I1 is correctly changed to I0
    '''
    random.seed(20170217)
    helper_simulate_one_day(['I1', 'I1', 'I1'], 0.0,
                            ['I0', 'I0', 'I0'])


def test_simulate_one_day_2():
    '''
    Purpose: checks that I0 is correctly changed to R
    '''
    random.seed(20170217)
    helper_simulate_one_day(['I0', 'I0', 'I0'], 0.0,
                            ['R', 'R', 'R'])


def test_simulate_one_day_3():
    '''
    Purpose: checks that R is not changed
    '''
    random.seed(20170217)
    helper_simulate_one_day(['R', 'R', 'R'], 0.0,
                            ['R', 'R', 'R'])


def test_simulate_one_day_4():
    '''
    Purpose: Check that a susceptible person does not become infected
    '''
    random.seed(20170217)
    helper_simulate_one_day(['I1', 'I1', 'S'], 0.2,
                            ['I0', 'I0', 'S'])


def test_simulate_one_day_5():
    '''
    Purpose: Check that a susceptible person becomes infected
    '''
    random.seed(20170217)
    helper_simulate_one_day(['I1', 'I1', 'S'], 0.5,
                            ['I0', 'I0', 'I1'])


def test_simulate_one_day_6():
    '''
    Purpose: Check that a susceptible person becomes infected,
             even when its neighbors recover in that same day.
    '''
    random.seed(20170217)
    helper_simulate_one_day(['I0', 'I0', 'S'], 0.5,
                            ['R', 'R', 'I1'])


def test_simulate_one_day_7():
    '''
    Purpose: Check that two susceptible persons become infected.
    '''
    random.seed(20170217)
    helper_simulate_one_day(['S', 'I0', 'S'], 0.9,
                            ['I1', 'R', 'I1'])


def test_simulate_one_day_8():
    '''
    Purpose: Check that, out of the two susceptible persons, only one
             of them becomes infected.
    '''
    random.seed(20170217)
    helper_simulate_one_day(['S', 'I0', 'S'], 0.3,
                            ['S', 'R', 'I1'])


def test_simulate_one_day_9():
    '''
    Purpose: Check that none of the susceptible persons become infected
    '''
    random.seed(20170217)
    helper_simulate_one_day(['S', 'S', 'S'], 1.0,
                            ['S', 'S', 'S'])


################## Task 5: run simulation over many days d  ##################


def helper_run_simulation(filename, expected_state, expected_num_days):
    '''
    Purpose: helper function for task 5

    Inputs:
        filename: (str) json file to open
        expected_state: (list) expected value
        expected_num_days: (int) expected value
    '''
    starting_state, random_seed, d, r, _ = \
        util.get_config(filename)

    # helper function for testing
    (actual_state, actual_num_days) = sir.run_simulation(
        starting_state, random_seed, d, r)
    if actual_state != expected_state:
        s = "Actual ({:}) and expected ({:}) final states do not match"
        pytest.fail(s.format(actual_state, expected_state))
    if actual_num_days != expected_num_days:
        s = "Actual ({:f}) and expected ({:f}) number of days do not match"
        pytest.fail(s.format(actual_num_days, expected_num_days))


def test_run_simulation_1():
    '''
    Purpose: tests basic functionality.
    '''
    test_file = TEST_DATA_DIR + '/3.json'
    helper_run_simulation(test_file,
                          ['S', 'R', 'R'], 3)


def test_run_simulation_2():
    '''
    Purpose: tests basic functionality.
    '''
    test_file = TEST_DATA_DIR + '/4.json'
    helper_run_simulation(test_file,
                          ['S', 'S', 'R'], 2)


def test_run_simulation_3():
    '''
    Purpose: tests basic functionality.
    '''
    test_file = TEST_DATA_DIR + '/5.json'
    helper_run_simulation(test_file,
                          ['R', 'S', 'R', 'R', 'S'], 2)


def test_run_simulation_4():
    '''
    Purpose: tests stopping conditions for all protected.
    '''
    test_file = TEST_DATA_DIR + '/6.json'
    helper_run_simulation(test_file,
                          ['R', 'R', 'R'], 2)


def test_run_simulation_5():
    '''
    Purpose: tests stopping conditions for no infected.
    '''
    test_file = TEST_DATA_DIR + '/7.json'
    helper_run_simulation(test_file,
                          ['R', 'S', 'S'], 1)

def test_run_simulation_6():
    '''
    Purpose: tests stopping condition for max number of days,
             where are still infected persons what con infect others
    '''
    test_file = TEST_DATA_DIR + '/8.json'
    helper_run_simulation(test_file,
                          ['R', 'R', 'R', 'I0', 'I1', 'S', 'S'], 3)


################## Task 6: Testing infection spread ##########################

def helper_compute_average_num_infected(filename, expected_average):
    '''
    Purpose: helper function for task 5

    Inputs:
        filename: (str) json file to open
        expected_average: (float) expected value
    '''
    starting_state, random_seed, max_num_days, infection_rate, num_trials = \
        util.get_config(filename)

    # helper function for testing
    actual_average = sir.compute_average_num_infected(
        starting_state, random_seed, max_num_days, infection_rate, num_trials)
    if actual_average != pytest.approx(expected_average):
        s = "Actual ({:}) and expected ({:}) averages do not match"
        pytest.fail(s.format(actual_average, expected_average))


def test_compute_average_num_infected_1():
    '''
    Purpose: test case that can be hand-computed.
    '''
    test_file = TEST_DATA_DIR + '/9.json'
    helper_compute_average_num_infected(test_file, 4.0)


def test_compute_average_num_infected_2():
    '''
    Purpose: test basic functionality.
    '''
    test_file = TEST_DATA_DIR + '/10.json'
    helper_compute_average_num_infected(test_file, 4.6)


def test_compute_average_num_infected_3():
    '''
    Purpose: test basic functionality.
    '''
    test_file = TEST_DATA_DIR + '/11.json'
    helper_compute_average_num_infected(test_file, 23.03)


def test_compute_average_num_infected_4():
    '''
    Purpose: test edge case - 1 trial
    '''
    test_file = TEST_DATA_DIR + '/12.json'
    helper_compute_average_num_infected(test_file, 8.0)


################## Task 6: Testing parameter sweep ###########################


def helper_infection_rate_param_sweep(filename, expected_avg_list,
                                      infection_rate_list=None):
    '''
    Purpose: helper function for task 6

    Inputs:
        filename: (str) json file to open
        expected_avg_list: (list) expected value
        infection_rate_list: (list) optional input parameter
    '''
    starting_state, random_seed, max_num_days, _, num_trials = \
        util.get_config(filename)

    if infection_rate_list is None:
        infection_rate_list = [0, 0.25, 0.5, 0.75, 1.0]
    # helper function for testing
    actual_avg_list = sir.infection_rate_param_sweep(
        starting_state, random_seed, max_num_days,
        infection_rate_list, num_trials)
    if actual_avg_list != pytest.approx(expected_avg_list):
        s = "Actual ({:}) and expected ({:}) final states do not match"
        pytest.fail(s.format(actual_avg_list, expected_avg_list))


def test_infection_rate_param_sweep_1():
    '''
    Purpose: can be computed by hand.
    '''
    test_file = TEST_DATA_DIR + '/13.json'
    helper_infection_rate_param_sweep(test_file,
                                      [2.0, 2.4, 3.5, 4.3, 5.0])


def test_infection_rate_param_sweep_2():
    '''
    Purpose: can be computed by hand.
    '''
    test_file = TEST_DATA_DIR + '/14.json'
    helper_infection_rate_param_sweep(test_file,
                                      [2.0, 2.4, 3.7, 4.6, 5.0])

def test_infection_rate_param_sweep_3():
    '''
    Purpose: can be computed by hand.
    '''
    test_file = TEST_DATA_DIR + '/15.json'
    helper_infection_rate_param_sweep(test_file,
                                      [2.0, 2.45, 2.77, 2.945, 3.0])


def test_infection_rate_param_sweep_4():
    '''
    Purpose: cannot be computed by hand.
    '''
    test_file = TEST_DATA_DIR + '/16.json'
    helper_infection_rate_param_sweep(test_file,
                                      [16.0, 21.824, 29.252, 35.078, 37.0])


def test_infection_rate_param_sweep_5():
    '''
    Purpose: cannot be computed by hand.
    '''
    test_file = TEST_DATA_DIR + '/17.json'
    helper_infection_rate_param_sweep(test_file,
                                      [38.0, 72.7, 106.2, 180.0, 397.0])


def test_infection_rate_param_sweep_6():
    '''
    Purpose: checks corner case.
    '''
    test_file = TEST_DATA_DIR + '/1.json'
    helper_infection_rate_param_sweep(test_file,
                                      [], infection_rate_list=[])


def test_infection_rate_param_sweep_7():
    '''
    Purpose: checks corner case.
    '''
    test_file = TEST_DATA_DIR + '/1.json'
    helper_infection_rate_param_sweep(test_file,
                                      [3.0], infection_rate_list=[1.0])
