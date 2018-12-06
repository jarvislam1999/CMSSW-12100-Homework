import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/ferryloading4
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


def solve(l, cars):
    """
    Parameters:
     - l: Integer. The length of the ferry.
     - cars: List of tuples. Each tuple represents a car. The first element of the
             tuple is the length of the car, and the second element is "left" or "right"
             (the bank at which the car arrives). Cars appear in the list in the order
             in which they arrive.

    Returns: Integer. The number of times the ferry has to cross the river.
    """

    # Your code here.
    left = []
    right = []
    for car in cars:
        if (car[1] == 'left'):
            left.append(car[0])
        else:
            right.append(car[0])
    bank = True
    count = 0
    while (len(left) != 0 or len(right) != 0):
        cl = l * 100
        i = 0
        if (bank):
            while (i < len(left) and cl >= left[i] ):
                cl -= left[i]
                i += 1
            left = left[i:]
        else:
            while (i < len(right) and cl >= right[i]):
                cl -= right[i]
                i += 1
            right = right[i:]
        count += 1
        bank = not bank

    # Replace 0 with a suitable return value.
    return count


### The following code handles the input and output tasks for
### this problem.  Do not modify it!

if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    tokens.reverse()

    ntests = int(tokens.pop())

    for i in range(ntests):
        l = int(tokens.pop())
        m = int(tokens.pop())
        cars = []
        for j in range(m):
            cars.append( (int(tokens.pop()), tokens.pop()) )

        print(solve(l, cars))


