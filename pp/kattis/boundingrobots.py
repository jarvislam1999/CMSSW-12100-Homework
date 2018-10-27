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
	rx = 0
	ry = 0
	ax = 0
	ay = 0
	for step in moves:
		if (step[0] == 'u'):
			ry += step[1]
			if (ay + step[1] <= w - 1):
				ay += step[1]
			else:
				ay = w - 1
		if (step[0] == 'd'):
			ry -= step[1]
			if (ay - step[1] >= 0):
				ay -= step[1]
			else:
				ay = 0
		if (step[0] == 'r'):
			rx += step[1]
			if (ax + step[1] <= l - 1):
				ax += step[1]
			else:
				ax = l - 1
		if (step[0] == 'l'):
			rx -= step[1]
			if (ax + step[1] >= 0):
				ax -= step[1]
			else:
				ax = 0


	# Replace the 0's with the values for rx, ry, ax, ay
	return rx, ry, ax, ay


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

