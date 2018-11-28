import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/securedoors
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes one parameter: A list of pairs. Each pair contains 
# two strings. The first one is either "entry" or "exit", and the second one
# is a name
#
# The function should not return anything. It should directly print
# the output as specified in the problem statement.
def solve(access_log):
    # Replace pass with your solution
    pass

if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()

    n = int(tokens.pop(0))
    access_log = []
    for i in range(n):
        action = tokens.pop(0)
        name = tokens.pop(0)
        access_log.append( (action, name) )

    solve(access_log)
