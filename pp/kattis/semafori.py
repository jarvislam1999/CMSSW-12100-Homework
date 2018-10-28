import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/semafori
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

def solve(l, lights):
    """
    Parameters:
     - l: Integer. The length of the road.
     - lights: List of tuples. Each tuple represents one traffic light and it
               contains three integers D, R, and G as defined in the problem statement.

    Returns: Integer. The time to reach the end of the road.
    """

    # YOUR CODE HERE
    second = 0
    position = 1
    color = 1
    '''
    while (light < len(lights)):
        second += lights[light][0] - position
    '''

    for light in lights:
        second += light[0] - position 
        color = second % (light[1] + light[2])
        if (color < light[1]):
            second += light[1] - color
        position = light[0]

    return second + l - position
    # Replace the 0 with your return value


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()
    tokens.reverse()

    n = int(tokens.pop())
    l = int(tokens.pop())

    lights = []
    for i in range(n):
        d = int(tokens.pop())
        r = int(tokens.pop())
        g = int(tokens.pop())

        lights.append( (d, r, g) )

    rv = solve(l, lights)
    assert isinstance(rv, int), "solve() must return an integer"

    print(rv)

