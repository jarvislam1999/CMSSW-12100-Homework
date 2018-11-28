import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/flowlayout
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes two parameters:
#
#  - max_width: The maximum width of the window
#  - rectangles: A list of pairs. Each pair contains two integers:
#                the width and height of a rectangle
#
# You must return the width and height of the resulting window.
def solve(max_width, rectangles):
    # YOUR CODE HERE
    
    # Replace 0, 0 with the width and height of the resulting window.
    return 0, 0


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()

    width = int(tokens.pop(0))
    while width != 0:
        rectangles = []
        rwidth = int(tokens.pop(0))
        rheight = int(tokens.pop(0))
        while rwidth != -1 and rheight != -1:
            rectangles.append( (rwidth, rheight) )
            rwidth = int(tokens.pop(0))
            rheight = int(tokens.pop(0))
            
        w, h = solve(width, rectangles)
        print("{} x {}".format(w, h))

        width = int(tokens.pop(0))
