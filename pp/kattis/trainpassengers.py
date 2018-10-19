import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/trainpassengers
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

def solve(C, stations):
    """
    Parameters:
     - C: Integer. The capacity of the train.
     - stations: List of tuples. Each tuple represents a station the train stopped in.
                 The tuple contains three integers: the number of people that left the 
                 train, entered the train, and had to stay at a station

    Returns: Boolean. True if the measurements are consistent, False otherwise
    """
    
    # YOUR CODE HERE

    # Replace True with your return value
    return True


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()
    tokens.reverse()

    C = int(tokens.pop())
    n = int(tokens.pop())

    stations = []
    for i in range(n):
        left = int(tokens.pop())
        entered = int(tokens.pop())
        stayed = int(tokens.pop())

        stations.append( (left, entered, stayed) )

    rv = solve(C, stations)
    assert isinstance(rv, bool), "solve() must return a boolean"

    if rv:
        print("possible")
    else:
        print("impossible")
