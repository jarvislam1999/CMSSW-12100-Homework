import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/torn2pieces
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


def station_link(pieces):
    l_dict = {}
    for p in pieces:
        for s in p: 
            if (s not in l_dict):
                l_dict[s] = []
            if (s not in l_dict[p[0]] and s != p[0]):
                l_dict[p[0]].append(s)
            if (p[0] not in l_dict[s] and s != p[0]):
                l_dict[s].append(p[0])
        
    return l_dict


def path_recursive(d, start, end):
    if (len(d[start]) == 0):
        return (False, 0)
    for s in d[start]:
        if (s == end):
            return (True, [end])
        d[s].remove(start)
        v = path_recursive(d, s, end)
        if (v[0] == True):
            return (True, [s] + v[1])
    return (False, 0)


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
    d = station_link(pieces)
    
    if (start not in d or end not in d):
        return None

    v = path_recursive(d, start, end)
    if (v[0] == True):
        return [start] + v[1]
    else:
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

