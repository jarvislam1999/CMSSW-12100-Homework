import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/uchicago.mpcs.tricky
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


# This functions takes two parameters. Each is a list
# of strings representing the cards that each player
# will play in the game (each string has a single
# character: "A", "2", ..., "9", "J", "Q", or "K")
#
# If player one wins, you must return the string "PLAYER 1 WINS"
#
# If player two wins, you must return the string "PLAYER 2 WINS"
#
# If the game ends in a tie, you must return the string "TIE"
def solve(p1_cards, p2_cards):
    # Write your solution here, and don't forget to update
    # the return statement to return the correct value.
    return "TIE"


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()

    n = int(tokens.pop(0))

    p1_cards = [tokens.pop(0) for i in range(n)]
    p2_cards = [tokens.pop(0) for i in range(n)]

    print(solve(p1_cards, p2_cards))

