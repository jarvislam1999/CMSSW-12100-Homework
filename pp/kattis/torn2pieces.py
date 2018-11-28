import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/torn2pieces
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


def solve(pieces, start, end):
    """
    Parameters:
     - pieces: List of lists of strings. Each list of strings represents a 
               piece of the map. For example, [["A","B"],["B","A","D"]] 
               represents two pieces, one for station "A" (which is connected
               to "B") and one for station "B" (which is connected to "A" and "D")
     - start, end: A starting and ending station.

    Returns: List of strings, or None.
             If a route exists between the starting and ending station, return
             a list with the stations in that route.
             If no such route exists, return None.
    """

    # Your code here.

    # Replace "None" with a suitable return value.
    return None


### The following code handles the input and output tasks for
### this problem.  Do not modify it!

if __name__ == "__main__":
    npieces = int(sys.stdin.readline())

    pieces = []
    for i in range(npieces):
        piece = sys.stdin.readline().strip().split()
        pieces.append(piece)

    start, end = sys.stdin.readline().strip().split()

    route = solve(pieces, start, end)
    if route is None:
        print("no route found")
    else:
        print(" ".join(route))

