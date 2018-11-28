import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/raggedright
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

def solve(lines):
    """
    Parameters:
     - lines: List of strings. Each string is a line of the paragraph.

    Returns: The raggedness score (as defined in the problem statement)
    """

    # YOUR CODE HERE
    len_list = [len(line) for line in lines]
    max_len = max(len_list)
    ragged_sum = 0
    for line in lines:
        ragged_sum += (max_len - len(line)) ** 2




    # Replace 0 with your return value
    return ragged_sum


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    lines = [x.strip() for x in lines]

    rv = solve(lines)
    assert isinstance(rv, int), "solve() must return an integer"

    print(rv)

