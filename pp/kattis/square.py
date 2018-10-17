#!/usr/bin/python

import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/uchicago.mpcs.square
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the exp function.
# Do not modify any other code.


def exp(x,n):
    # This function takes a pair of integers x and y and returns x raised
    # to the power y.  
    #
    # Your solution must be recursive!

    # replace the 1 with an appropriate return value
    return 1


if __name__ == "__main__":
    ### The following code handles the input and output tasks for
    ### this problem.  Do not modify it!

    tokens = sys.stdin.read().split()

    x = int(tokens[0])
    n = int(tokens[1])

    print(exp(x, n))

