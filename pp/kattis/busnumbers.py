import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/busnumbers
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

def solve(numbers):
    """
    Parameters:
     - numbers: List of integers. The list of bus numbers

    Returns: String. The shortest representation of the list of bus numbers
    """

    # YOUR CODE HERE

    # Replace "" with your return value
    return ""


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()
    tokens.reverse()

    n = int(tokens.pop())
    numbers = [int(tokens.pop()) for _ in range(n)]

    numbers_str = solve(numbers)
    assert isinstance(numbers_str, str), "solve() should return a string"
    print(numbers_str)        
