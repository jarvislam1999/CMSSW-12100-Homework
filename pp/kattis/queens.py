#!/usr/bin/python

import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/queens
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.  Do not
# modify any other code.

# This function takes a single parameter: a list of tuples, which
# represent the locations of queens on the board.  Your function
# should return True if the queens are placed legally.

def solve(queens):    
    # YOUR CODE HERE

    # Replace True with the correct return value
    return True

if __name__ == "__main__":

    tokens = sys.stdin.read().split()

    n = int(tokens.pop(0))

    queens = []
    for i in range(n):
        queens.append( (int(tokens.pop(0)), int(tokens.pop(0))) )

    if solve(queens):
        print("CORRECT")
    else:
        print("INCORRECT")

