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
    if (len(l) == 0):
        return True
    middle = len(l) // 2
    if (l[middle] < l[0] or l[middle] > l[len(l) - 1]):
        return False
    return all([is_ascending(l[:middle]), is_ascending(l[middle + 1:])])

    # replace True with a suitable return value
    # return True

def is_descending(l):
    # replace True with a suitable return value
    if (len(l) == 0):
        return True
    middle = len(l) // 2
    if (l[middle] > l[0] or l[middle] < l[len(l) - 1]):
        return False
    return all([is_descending(l[:middle]), is_descending(l[middle + 1:])])
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
