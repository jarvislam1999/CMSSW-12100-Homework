import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/secretmessage
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

import math

def solve(message):
    """
    Parameters:
     - message: String. The message.

    Returns: String. The secret message
    """
    # YOUR CODE HERE

    # Replace "" with your return value
    return ""


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()
    tokens.reverse()

    m = int(tokens.pop())

    for i in range(m):
        message = tokens.pop()
        secret_message = solve(message)
        assert isinstance(secret_message, str), "solve() should return a string"
        print(secret_message)        
