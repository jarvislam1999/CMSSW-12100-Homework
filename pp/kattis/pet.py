import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/pet
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes a single parameters containing a list
# with exactly five entries (one per contestant). Each entry 
# is a list with exactly four integers (the scores for that
# contestant)
def solve(contestant_scores):
    # YOUR CODE HERE

    # Replace 1 with the winning contestant (remember that
    # contestants are 1-indexed, not 0-indexed) and replace 0
    # with the score of the winning contestant.
    return 1, 0


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()

    scores = [ [int(tokens.pop(0)) for i in range(4)] for j in range(5) ]

    pet, score = solve(scores)

    print(pet, score)
