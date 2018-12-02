import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/blackfriday
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


def solve(rolls):
    """
    Parameters:
     - rolls: List of integers. The outcome of each participant's die roll.

    Returns: Integer, or None.
             The index of the participat that has the highest unique outcome.
             If no such participant exists, return None.
    """

    # Your code here.
    roll = sorted(rolls, reverse = True)
    if roll[0] != roll[1]:
        return roll[0]
    for i in range(1, len(roll) - 2):
        if (roll[i] != roll[i+1]):
            return roll[i+1]

    # Replace "None" with a suitable return value.
    return None


### The following code handles the input and output tasks for
### this problem.  Do not modify it!

if __name__ == "__main__":
    tokens = sys.stdin.read().split()

    n = int(tokens.pop(0))
    rolls = [int(tokens.pop(0)) for i in range(n)]

    rv = solve(rolls)
    if rv is None:
        print("none")
    else:
        print(rv)
    
