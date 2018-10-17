import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/boundingrobots
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

def solve(w, l, moves):
    """
    Parameters:
     - w, l: Integers. The width and length of the room.
     - moves: List of tuples. Each tuple contains a string ("u","d","l", or "r")
              specifying the direction of the move, and an integer, specifying
              the number of meters to move in that direction.

    Returns: A tuple with four integers (rx, ry, ax, ay). rx, ry are the coordinates
             the robot thinks it is at. ax, ay are the coordinates the robot is actually at.
    """
    
    # YOUR CODE HERE

    # Replace the 0's with the values for rx, ry, ax, ay
    return 0, 0, 0, 0


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()
    tokens.reverse()

    while True:
        w = int(tokens.pop())
        l = int(tokens.pop())

        if w==0 and l==0:
            break

        n = int(tokens.pop())
    
        moves = []
        for i in range(n):
            move_type = tokens.pop()
            assert move_type in ("u","d","l","r"), "Invalid move type: {}".format(move_type)

            meters = int(tokens.pop())

            moves.append( (move_type, meters) )

        rv = solve(w, l, moves)
        assert isinstance(rv, tuple), "solve() must return a tuple"
        assert len(rv) == 4, "solve() must return a tuple of three integers"
        assert all([isinstance(x, int) for x in rv]), "solve() returned a tuple containing a non-integer" 

        rx, ry, ax, ay = rv
        print("Robot thinks {} {}".format(rx, ry))
        print("Actually at {} {}".format(ax, ay))
        print()

