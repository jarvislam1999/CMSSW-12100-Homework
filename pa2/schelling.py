'''
Schelling Model of Housing Segregation

Program for simulating of a variant of Schelling's model of
housing segregation.  This program takes five parameters:

	filename -- name of a file containing a sample city grid

	R - The radius of the neighborhood: home at Location (i, j) is in
		the neighborhood of the home at Location (k,l)
		if k-R <= i <= k+R and l-R <= j <= l+R

	M threshold - minimum acceptable threshold for ratio of the number
				of similar neighbors to the number of occupied homes
				in a neighborhood for maroon homeowners.

	B threshold - minimum acceptable threshold for ratio of the number
				of similar neighbors to the number of occupied homes
				in a neighborhood for blue homeowners.

	max_steps - the maximum number of passes to make over the city
				during a simulation.

Sample:
  python3 schelling.py --grid_file=tests/a18-sample-grid.txt --r=1 --m_threshold=0.44 --b_threshold=0.70 --max_steps=2
'''

import os
import sys
import click
import utility


def is_satisfied(grid, R, location, M_threshold, B_threshold):
	'''
	Determine whether or not the homeowner at a specific location is satisfied
	using a neighborhood of radius R and specified M and B thresholds.

	Inputs:
		grid: the grid
		R: radius for the neighborhood
		location: a grid location
		M_threshold: lower bound for similarity score for maroon homeowners
		B_threshold: lower bound for similarity score for blue homeowners

	Returns: Boolean
	'''

	assert utility.is_grid(grid), ("The grid argument has the wrong type.  "
								   "It should be a list of lists of strings "
								   "with the same number of rows and columns")
	# Storing the location tuple into row and column
	lrow = location[0]
	lcol = location[1]
	assert grid[lrow][lcol] != "O"
	assert R <= len(grid)
	# We recommend adding an assertion to check that the location does
	# not contain an open (unoccupied) home.

	# YOUR CODE HERE

	# Initializing output variable
	B_count = 0
	M_count = 0
	occupied_count = 0
	
	r_low = lrow - R
	r_upp = lrow + R +1
	c_low = lcol - R
	c_upp = lcol + R +1

	if (r_low < 0):
		r_low = 0
	if (r_upp > len(grid)):
		r_upp = len(grid)
	if (c_low < 0):
		c_low = 0
	if (c_upp > len(grid)):
		c_upp = len(grid)	

	for r in range(r_low, r_upp):
		for c in range(c_low, c_upp):
			if (grid[r][c] == "B"):
				B_count += 1
			if (grid[r][c] == "M"):
				M_count += 1
			if (grid[r][c] != "O"):
				occupied_count += 1

	B_percent = B_count/occupied_count	
	M_percent = M_count/occupied_count	

	if (grid[lrow][lcol] == "B"):
		if B_percent >= B_threshold:
			return True
	if (grid[lrow][lcol] == "M"):
		if M_percent >= M_threshold:
			return True
	# Replace False with correct return value
	return False


# PUT YOUR AUXILIARY FUNCTIONS HERE

# Determine the distance between two locations
def distance(location1,location2):
	squared_distance = (location2[0] - location1[0]) ** 2 + (location2[1] - location1[1]) ** 2
	return squared_distance ** 0.5

# Compute R-1 direct neighbors
def R1_direct_neighbor(grid,location):
	assert utility.is_grid(grid)

	border_count = 0
	if (len(grid) == 1):
		return 0
	if (location[0] == 0 or location[0] == len(grid) - 1):
		border_count += 1

# DO NOT REMOVE THE COMMENT BELOW
#pylint: disable-msg=too-many-arguments
def do_simulation(grid, R, M_threshold, B_threshold, max_steps, opens):
	'''
	Do a full simulation.

	Inputs:
		grid: (list of lists of strings) the grid
		R: (int) radius for the neighborhood
		M_threshold: (float) satisfaction threshold for maroon homeowners
		B_threshold: (float) satisfaction threshold for blue homeowners
		max_steps: (int) maximum number of steps to do
		opens: (list of tuples) a list of open locations

	Returns:
		The total number of relocations completed.
	'''

	assert utility.is_grid(grid), ("The grid argument has the wrong type.  "
								   "It should be a list of lists of strings "
								   "with the same number of rows and columns")

	# YOUR CODE HERE
	# REPLACE -1 with an appropriate return value
	return -1


@click.command(name="schelling")
@click.option('--grid_file', type=click.Path(exists=True))
@click.option('--r', type=int, default=1, help="neighborhood radius")
@click.option('--m_threshold', type=float, default=0.44, help="M threshold")
@click.option('--b_threshold', type=float, default=0.70, help="B threshold")
@click.option('--max_steps', type=int, default=1)
def run(grid_file, r, m_threshold, b_threshold, max_steps):
	'''
	Put it all together: do the simulation and process the results.
	'''

	if grid_file is None:
		print("No parameters specified...just loading the code")
		return

	grid = utility.read_grid(grid_file)

	if len(grid) < 20:
		print("Initial state of city:")
		for row in grid:
			print(row)
		print()

	opens = utility.find_opens(grid)
	num_relocations = do_simulation(grid, r, m_threshold, b_threshold,
									max_steps, opens)
	print("Number of relocations done: " + str(num_relocations))

	if len(grid) < 20:
		print()
		print("Final state of the city:")
		for row in grid:
			print(row)

if __name__ == "__main__":
	run() # pylint: disable=no-value-for-parameter
