#!/usr/bin/python

import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/uchicago.mpcs.minesweeper
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.  Do not
# modify any other code.

# This function takes a one parameter: a list of lists of integers
# (representing a matrix, i.e., the minefield).  A 1 means that 
# the spot contains a mine and a zero indicates that it
# does not.  You must return a list of lists of integers representing
# a field of the same dimensions, but where each spot
# should contain either -1, meaning that the spot holds a mine, or a
# value that is >= 0, which is a count of the number of mines in
# adjacent spots.

def solve(field):
	# Your code here
	field1 = []
	for i in range(len(field)):
		field1.append([0] * len(field[0]))

	mine = []
	for i in range(len(field)):
		for j in range(len(field[0])):
			if field[i][j] == 1:
				if ( i - 1 < 0):
					rlower = 0
				else:
					rlower = i - 1
				if ( i + 1 > len(field) - 1):
					rupper = len(field)
				else:
					rupper = i + 2
				if ( j - 1 < 0):
					clower = 0
				else:
					clower = j - 1
				if ( j + 1 > len(field[0]) - 1):
					cupper = len(field[0])
				else:
					cupper = j + 2
				for x in range(rlower, rupper):
					for y in range(clower, cupper):
						field1[x][y] += 1
				mine.append([i, j])
	for m in mine:
		if (field[m[0]][m[1]] == 1):
			field1[m[0]][m[1]] = -1

	# Replace [] with a list of lists representing the solved minefield
	return field1

def result_to_str(field):
	result_str = ""
	for row in field:
		s = ""
		for v in row:
			if v == -1:
				s += "X"
			elif v == 0:
				s += "-"
			else:
				s += str(v)
		result_str += s + "\n"

	return result_str

if __name__ == "__main__":
	tokens = sys.stdin.read().strip().split()

	x = int(tokens.pop(0))
	y = int(tokens.pop(0))

	field = []

	for i in range(x):
		row = []
		for j in range(y):
			row.append(int(tokens.pop(0)))
		field.append(row)

	result = solve(field)
	print(result_to_str(result))

		  
