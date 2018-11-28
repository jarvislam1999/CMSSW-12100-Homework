import sys

# This is the provided within_bounds function.
# Do not modify it!
def within_bounds(x, lb, ub):
    return (lb <= x and x <= ub)

# Implement a function called within_range here
# Your implementation must include a call to within_bounds


if __name__ == "__main__":
    # parse the input
    (x,c,r) = [float(item.strip()) for item  in sys.stdin.read().split()]

    # Replace True with a call to your within_range function
    # You must use variables x, c, r in your function call.
    rv = True

    print(rv)
