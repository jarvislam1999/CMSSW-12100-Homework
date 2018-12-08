#!/usr/bin/python
import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/uchicago.mpcs.ninetyone
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the m91 function.
# Do not modify any other code.

def m91(n):
    # This function takes an integer and returns an integer.
    if (n > 100):
    	return n -10
    if (n <= 100):
    	return m91(m91(n + 11))
    # replace the 1 with a suitable return value
    #return 1


### The following code handles the input and output tasks for
### this problem.  Do not modify it!

if __name__ == "__main__":
    n = int(sys.stdin.read())

    print(m91(n))

