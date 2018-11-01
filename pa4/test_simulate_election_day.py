'''
Polling places: test code for simulate_election_day
'''

import csv
import pytest
import util

from simulate import simulate_election_day

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg= invalid-name, missing-docstring, too-many-arguments, line-too-long
# pylint: disable-msg= missing-docstring, too-many-locals, unused-argument


precinct_files = [("config-single-precinct-0.json", "Single Precinct"),
                  ("config-single-precinct-1.json", "Single Precinct"),
                  ("config-single-precinct-2.json", "Single Precinct"),
                  ("config-single-precinct-3.json", "Single Precinct"),
                  ("config-single-precinct-4.json", "Single Precinct"),
                  ("config-single-precinct-5.json", "Single Precinct"),
                  ("config-multiple-precincts-0.json", "Multiple Precincts"),
                  ("config-multiple-precincts-1.json", "Multiple Precincts"),
                  ("config-multiple-precincts-2.json", "Multiple Precincts")]


DATA_DIR = "./data/"

def fcompare(pname, nvoter, field, got, expected):
    assert got == pytest.approx(expected), "The {} of voter #{} in precint '{}' is incorrect (got {}, expected {})".format(field, nvoter, pname, got, expected)

def run_test(precincts_file):
    precincts, seed = util.load_precincts(precincts_file)
    results_file = precincts_file.replace(".json", ".csv")
    voters = simulate_election_day(precincts, seed)

    with open(results_file) as f:
        reader = csv.DictReader(f)

        results = {}
        for row in reader:
            results.setdefault(row["precinct"], []).append(row)

        for p in precincts:
            pname = p["name"]

            pvoters = voters[pname]
            rvoters = results.get(pname, [])

            assert len(pvoters) == len(rvoters), "Incorrect number of voters for precinct '{}' (got {}, expected {}".format(pname, len(pvoters), len(rvoters))

            i = 0
            for returned_voter, expected_voter in zip(pvoters, rvoters):
                fcompare(pname, i, "arrival time", returned_voter.arrival_time, float(expected_voter["arrival_time"]))
                fcompare(pname, i, "voting duration", returned_voter.voting_duration, float(expected_voter["voting_duration"]))
                fcompare(pname, i, "start time", returned_voter.start_time, float(expected_voter["start_time"]))
                i += 1

@pytest.mark.parametrize("config_file,desc", precinct_files)
def test_simulate(config_file, desc):
    run_test(DATA_DIR + config_file)
