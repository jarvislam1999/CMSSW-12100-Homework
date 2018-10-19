import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/uchicagoplacement.martingale
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


# This functions takes three parameters. 
#
#  - initial_cash: The amount of cash the player starts with 
#                  (m_1 in the problem statement)
#  - initial_bet: The initial bet amount (b_1 in the problem statement)
#  - coin_flips: A list of integers, representing the sequence
#                of coin flips (1: heads, 0:tails)
#
# Your function must return an integer with the amount of money 
# that the player has at the end of the game. Note that if the
# player has no money at the end of the game, you must return
# the integer zero (not the string "BROKE")
def solve(initial_money, initial_bet, cointosses):
    # Write your solution here, and don't forget to update
    # the return statement to return the correct value.
    return 0


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()

    initial_money = int(tokens.pop(0))
    initial_bet = int(tokens.pop(0))

    n = int(tokens.pop(0))
    cointosses = [int(tokens.pop(0)) for i in range(n)]

    money = solve(initial_money, initial_bet, cointosses)

    if money == 0:
        print("BROKE")
    else:
        print(money)

