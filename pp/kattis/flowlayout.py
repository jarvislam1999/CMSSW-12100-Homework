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
	max_length = 0
	max_depth = 0
	depth = 0
	plus_variable = 0
	i = 0

	while (i <= len(rectangles) - 1):
		if (plus_variable + rectangles[i][0] <= max_width):
			plus_variable += rectangles[i][0]
			if (rectangles[i][1] > max_depth):
				max_depth = rectangles[i][1]
			i += 1
		if (i > len(rectangles) - 1):
			if (plus_variable > max_length):
				max_length = plus_variable
			depth += max_depth
			break
		if (plus_variable + rectangles[i][0] > max_width):
			if (plus_variable > max_length):
				max_length = plus_variable
			depth += max_depth
			plus_variable = 0
			max_depth = 0
			
	return str(max_length) + ' x ' + str(depth)







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
