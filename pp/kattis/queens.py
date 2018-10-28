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
    row = {}
    column = {}
    for queen in queens:
        if (queen[0] in row):
            return False
        if (queen[1] in column):
            return False
        row[queen[0]] = True
        column[queen[1]] = True
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if(abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1])):
                return False
                

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

