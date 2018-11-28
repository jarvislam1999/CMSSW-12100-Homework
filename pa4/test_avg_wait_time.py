'''
Polling places: test code for avg_wait_time
'''

import csv
import pytest
import util
from simulate import find_avg_wait_time

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg= invalid-name, missing-docstring


DATA_DIR = "./data/"

with open(DATA_DIR + "avg_wait_time.csv") as f:
    reader = csv.DictReader(f)

    configs = []
    for row in reader:
        config = (row["config_file"],
                  int(row["num_trials"]),
                  int(row["num_booths"]),
                  float(row["avg_wait_time"])
                 )
        configs.append(config)

def run_test(precincts_file, num_trials, num_booths, avg_wait_time):
    precincts, seed = util.load_precincts(precincts_file)
    p = precincts[0]

    avg_wt = find_avg_wait_time(p, num_booths, num_trials, initial_seed=seed)

    assert avg_wt == pytest.approx(avg_wait_time)

@pytest.mark.parametrize("precincts_file,num_trials,num_booths,avg_wait_time", configs)
def test_simulate(precincts_file, num_trials, num_booths, avg_wait_time):
    run_test(DATA_DIR + precincts_file, num_trials, num_booths, avg_wait_time)
