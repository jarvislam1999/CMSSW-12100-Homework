import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/permutationencryption
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


def encrypt(message, permutations):
    """
    Parameters:
     - message: String. The message to encrypt.
     - permutations: List of integers. The integers that form the permutation.

    Returns: String. The encrypted message.
    """

    # Your code here.

    # Replace "" with a suitable return value.
    return ""


### The following code handles the input and output tasks for
### this problem.  Do not modify it!

if __name__ == "__main__":
    tokens = sys.stdin.readline().split()

    while int(tokens[0]) != 0:
        n = int(tokens[0])
        permutations = [int(x) for x in tokens[1:]]
        assert(len(permutations) == n)

        message = sys.stdin.readline().strip()
    
        print("'{}'".format(encrypt(message, permutations)))
        
        tokens = sys.stdin.readline().split()
    
