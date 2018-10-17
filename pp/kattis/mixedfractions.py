import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/mixedfractions
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

def solve(numerator, denominator):
    """
    Parameters:
     - numerator, denominator: Integers. As defined in the problem statement.

    Returns: Tuple of three integers. This tuple will be the mixed fraction:
             the first element is the whole number, and the next two numbers
             are the numerator and denominator of the mixed fraction.
    """
    
    # YOUR CODE HERE

    # Replace 0, 0, 0 with the appropriate return values
    return 0, 0, 0


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()
    tokens.reverse()

    while True:
        numerator = int(tokens.pop())
        denominator = int(tokens.pop())

        if numerator == 0 and denominator == 0:
            break

        x = solve(numerator, denominator)

        assert isinstance(x, tuple), "solve() must return a tuple"
        assert len(x) == 3, "solve() must return a tuple of three integers"
        assert all([isinstance(y, int) for y in x]), "solve() returned a tuple containing a non-integer" 

        a, b, c = x

        print("{} {} / {}".format(a,b,c))

