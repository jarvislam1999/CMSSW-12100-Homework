'''
Polling places: test code for find_number_of_booths
'''

import csv
import pytest
import util

from simulate import find_number_of_booths

DATA_DIR = "./data/"

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg= invalid-name, missing-docstring, too-many-arguments, line-too-long


with open(DATA_DIR + "best_num_booths.csv") as f:
    reader = csv.DictReader(f)

    configs = []
    for row in reader:
        config = (row["config_file"],
                  int(row["num_trials"]),
                  float(row["target_wait_time"]),
                  int(row["max_num_booths"]),
                  int(row["num_booths"]),
                  None if row["avg_wait_time"] == "" else float(row["avg_wait_time"])
                 )
        configs.append(config)

def run_test(precincts_file, num_trials, target_wait_time, max_num_booths,
             num_booths, avg_wait_time):
    precincts, seed = util.load_precincts(precincts_file)
    p = precincts[0]

    nb, avg_wt = find_number_of_booths(p, target_wait_time, max_num_booths, num_trials, seed)

    if avg_wait_time == None:
      avg_wait_time = None
    else:
      avg_wait_time = pytest.approx(avg_wait_time)

    assert nb == num_booths
    assert avg_wt == avg_wait_time

@pytest.mark.parametrize("config_file,num_trials,target_wait_time,max_num_booths,num_booths,avg_wait_time", configs)
def test_simulate(config_file, num_trials, target_wait_time, max_num_booths,
                  num_booths, avg_wait_time):
    run_test(DATA_DIR + config_file, num_trials, target_wait_time, max_num_booths,
             num_booths, avg_wait_time)
