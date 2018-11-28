import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/hittingtargets
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

def solve(targets, x, y):
    """
    Parameters:
     - targets: A list of dictionaries. All dictionaries have a "type"
                key which will contain either "rectangle" or "circle".
                
                If "type" is "rectangle", then the dictionary will have
                four additional keys "x1", "y1", "x2", "y2", as defined
                in the problem statement.

                If "type" is "circle", then the dictionary will have three
                additional keys "x", "y", and "r", as defined in the problem
                statement.
      - x, y: Integers. The coordinates of a single shot.

    Returns: Integer. The number of targets hit by the shot at (x,y)
    """

    # YOUR CODE HERE

    # Replace 0 with your return value
    return 0


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()
    tokens.reverse()

    m = int(tokens.pop())

    targets = []
    for i in range(m):
        target_type = tokens.pop()
        assert(target_type == "rectangle" or target_type == "circle")
        if target_type == "rectangle":
            target = {
                      "type": "rectangle",
                      "x1":  int(tokens.pop()),
                      "y1":  int(tokens.pop()),
                      "x2":  int(tokens.pop()),
                      "y2":  int(tokens.pop())
                     }
        elif target_type == "circle":
            target = {
                      "type": "circle",
                      "x":  int(tokens.pop()),
                      "y":  int(tokens.pop()),
                      "r":  int(tokens.pop())
                     }
        targets.append(target)

    nshots = int(tokens.pop())
    shots = []
    for i in range(nshots):
        shots.append( (int(tokens.pop()), int(tokens.pop())) )

    for x, y in shots:
        nhits = solve(targets, x, y)
        assert isinstance(nhits, int), "solve() should return an integer"
        print(nhits)
        
