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

    empty_list = []
    m = int((len(message) ** 0.5) // 1) + (1 if ((len(message) ** 0.5) % 1 != 0) else 0)
    message1 = message + "*" * (m ** 2 - len(message))

    for i in range(m):
        for j in range(m - 1, -1, -1):
            if message1[4 * j + i] != "*":
                empty_list.append(message1[4*j + i])
    # Replace "" with your return value
    return "".join(empty_list)


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()
    tokens.reverse()

    m = int(tokens.pop())

    for i in range(m):
        message = tokens.pop()
        secret_message = solve(message)
        assert isinstance(secret_message, str), "solve() should return a string"
        print(secret_message)        
