import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/plantingtrees
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes a single parameter: a list of integers, each of
# which represents t_i (as described in the problem statement)
def solve(times):
    # YOUR CODE HERE

    # Replace 0 with the earliest day the party can be
    # organized (as described in the problem statement)
    return 0


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()

    n = int(tokens.pop(0))

    times = [int(t) for t in tokens]
    assert len(times) == n

    print(solve(times))
