import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/oddmanout
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes one parameter: a list of integer invitation codes 
# (corresponding to a single test case in the problem statement)
#
# You must return the code of the odd man out.
def solve(invitation_codes):
    # Replace 0 with the invitation code of the odd man out
    return 0


if __name__ == "__main__":
    ntests = int(sys.stdin.readline())

    for i in range(ntests):
        nguests = int(sys.stdin.readline())
        codes = sys.stdin.readline().strip()
        codes = [int(x) for x in codes.split()]
        assert len(codes) == nguests

        print("Case #{}: {}".format(i+1, solve(codes)))
