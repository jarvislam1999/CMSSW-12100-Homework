import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/lineup
#
# Make sure you read the problem before editing this code.
#
# You should focus on implementing the is_ascending and is_descending
# functions.  Both functions will take a list and return a boolean.
# is_ascending should return True when the list is in ascending order.
# is_descending should return True when the list is in descending order.


def is_ascending(l):
    # replace True with a suitable return value
    return True

def is_descending(l):
    # replace True with a suitable return value
    return True


### The following code handles the input and output tasks for
### this problem.  Do not modify it!

if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()

    n = int(tokens.pop(0))

    assert(len(tokens) == n)

    asc = is_ascending(tokens)
    desc = is_descending(tokens)

    if asc and not desc:
        print("INCREASING")
    elif not asc and desc:
        print("DECREASING")
    else:
        print("NEITHER")
