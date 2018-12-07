#!/usr/bin/python3

import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/uchicago.miles
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the flights() function. 
#
# Your solution must be *recursive*, but the flights() function itself 
# doesn't have to be the recursive function in your solution. Remember 
# that you are welcome to write auxiliary functions in your solutions. 


# The flights() function received four parameters:
#
# - itinerary: A list of strings with the desired itinerary for the mileage run
#              e.g.: [ "chicago", "detroit", "omaha", "pittsburgh", "chicago" ]
#              Remember that, while the problem statements presents examples
#              where the first and last airport are the same, your algorithm
#              must work even if this is not the case. You *can* however
#              assume that, if the first and last airport are not the same,
#              that no airport appears more than once in the list.
#
# - schedules: The flight schedules, stored as a dictionary with keys corresponding 
#              to departure cities. The values for each of these keys are dictionaries 
#              as well. In these nested dictionaries, the keys are arrival cities and 
#              the values are the lists of flights between the specified cities (where
#              each flight is a tuple with a departure and arrival time, as described 
#              in the problem statement). For example, the dictionary corresponding to
#              the schedules specified in the third sample input would be:
#
#              {'chicago': {'detroit': [(1.5, 3.0), (2.75, 4.25), (5.0, 6.0)],
#                           'omaha': [(1.0, 2.0), (3.0, 4.0)],
#                           'pittsburgh': [(2.5, 3.5)]},
#               'detroit': {'chicago': [(1.0, 2.0), (3.0, 4.0)],
#                           'omaha': [(2.0, 3.0), (3.0, 4.0), (4.0, 5.0)],
#                           'pittsburgh': [(2.5, 3.5), (5.0, 6.0)]},
#               'omaha': {'chicago': [(1.0, 2.0), (3.0, 4.0)],
#                         'detroit': [(5.5, 7.5), (8.0, 9.0)],
#                         'pittsburgh': [(1.5, 4.5), (6.0, 9.0), (6.5, 9.5)]},
#               'pittsburgh': {'chicago': [(10.5, 11.5), (11.25, 12.75)],
#                              'detroit': [(1.5, 2.5), (4.0, 5.0)],
#                              'omaha': [(2.0, 3.0), (3.0, 4.0)]}}
#
# - t_min, t_max: The minimum and maximum connection times, as specified in the problem
#                 statement.
#
# The function must return a list of all possible sequences of flights, subject to the
# minimum/maximum connection times, the order of cities you need to visit, and the provided
# schedule of flights. Each sequence of flights is represented by a list where the entries
# are the departure/arrival time tuples for each flight, and ending with the string "done".
# For example, the return value corresponding to the third sample output would be this:
#
#    [ [(1.5, 3.0), (4.0, 5.0), (6.0, 9.0), (10.5, 11.5), 'done'],
#      [(1.5, 3.0), (4.0, 5.0), (6.5, 9.5), (10.5, 11.5), 'done'],
#      [(1.5, 3.0), (4.0, 5.0), (6.5, 9.5), (11.25, 12.75), 'done'] ]
#
# If there are no feasible sequences of flights, the function must return the empty list.
#


def find_path(itinerary, schedules, t_min, t_max, start):
    

def flights(itinerary, schedules, t_min, t_max):
    # your code goes here
    return []


### The following code handles the input and output tasks for
### this problem.  Do not modify it!

if __name__ == "__main__":
    # parse the input
    tokens = sys.stdin.read().split()
    n_airports = int(tokens.pop(0))
    n_flights = int(tokens.pop(0))
    n_itinerary = int(tokens.pop(0))
    t_min = float(tokens.pop(0))
    t_max = float(tokens.pop(0))

    schedules = {}
    for i in range(n_airports):
        airport = tokens.pop(0)
        schedules[airport] = {}

    for i in range(n_flights):
        origin = tokens.pop(0)
        destination = tokens.pop(0)
        leave = float(tokens.pop(0))
        depart = float(tokens.pop(0))

        schedules[origin].setdefault(destination, []).append( (leave, depart) )

    itinerary = []
    for i in range(n_itinerary):
        itinerary.append(tokens.pop(0))

    runs = flights(itinerary, schedules, t_min, t_max)

    if len(runs) == 0:
        print("NO RUNS")
    else:
        for run in runs:
            if len(run) == 0:
                print("Error: flights() returned an empty run.", file=sys.stderr)
                continue

            if run[-1] != "done":
                print("Error: run doesn't end with 'done': {}".format(run), file=sys.stderr)
                continue
        
            if len(run) != len(itinerary):
                print("Error: run has {} flights, should have {}: {}".format(len(run)-1, len(itinerary)-1, run), file=sys.stderr)
                continue

            for i, flight in enumerate(run[:-1]):
                if len(flight) != 2:
                    print("Error: run contains an invalid value: ".format(flight), file=sys.stderr)
                    print("       Runs should contain only pairs of floats, or 'done' as the last element", file=sys.stderr)
                    break

                print(itinerary[i], itinerary[i+1], flight[0], flight[1])

            print("###")
