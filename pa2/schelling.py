# NAME: JARVIS LAM
# CS 12100

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
	'''
	Determine the distance between two locations on any grids. 

	Inputs:
		location1: a tuple containing the row and column of the first location in a grid
		location2: a tuple containing the row and column of the second location in a grid

	Returns: a real number which is the Euclidean distance between the two locations
	'''
	# Squared distance according to Euclidean geometry
	squared_distance = (location2[0] - location1[0]) ** 2 + (location2[1] - location1[1]) ** 2
	return squared_distance ** 0.5

# Compute R-1 direct neighbors
def R1_direct_neighbor(grid,location):
	'''
	Determine the R-1 direct neighbors of a particular location on the grid.

	Inputs:
		grid: the grid
		location: a grid location tuple

	Returns: the number of R-1 direct neighbors of a particular location on the grid
	'''	
	assert utility.is_grid(grid)

	lrow = location[0]
	lcol = location[1]
	occupied_count = 0
	
	r_low = lrow - 1
	r_upp = lrow + 2
	c_low = lcol - 1
	c_upp = lcol + 2

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
			if (grid[r][c] != "O"):
				occupied_count += 1
	return occupied_count

# Swap the values between two locations
def swap_value(grid, location1, location2):
	middle_man = grid[location1[0]][location1[1]]
	grid[location1[0]][location1[1]] = grid[location2[0]][location2[1]]
	grid[location2[0]][location2[1]] = middle_man
	return None

# Evaluate and return the best swapping location of a particular location
def evaluate_open_spot(grid, R, location, M_threshold, B_threshold, opens):
	assert grid[location[0]][location[1]] != "O"
	assert is_satisfied(grid, R, location, M_threshold, B_threshold) == False
	
	location_list = []
	second_location_list = []
	third_location_list = []
	distance_list = []
	R1_neighbor_list = []
	open_spot_list = utility.find_opens(grid)
	for loc in open_spot_list:
		swap_value(grid, location, loc)
		if is_satisfied(grid, R, loc, M_threshold, B_threshold): 
			location_list.append(loc)
			distance_list.append(distance(location,loc))
		swap_value(grid, location, loc)
	if (len(location_list) == 0):
		return location
	elif (len(location_list) == 1):
		return location_list[0]
	else:
		for loc in location_list:
			if (distance(location,loc) == min(distance_list)):
				second_location_list.append(loc)
				R1_neighbor_list.append(R1_direct_neighbor(grid, loc))
		if (len(second_location_list) == 1):
			return second_location_list[0]
		elif (len(second_location_list) > 1):
			for loc in second_location_list:
				if (R1_direct_neighbor(grid, loc) == max(R1_neighbor_list)):
					third_location_list.append(loc)
			if (len(third_location_list) == 1):
				return third_location_list[0]
			elif (len(third_location_list) > 1):
				for loc1 in reversed(third_location_list):
					for loc2 in opens:
						if (loc1 == loc2):
							return loc1
	return None


def simulate_one_step(grid, R, M_threshold, B_threshold, opens):
	relocation_count = 0
	for ro in range(0,len(grid)):
		for co in range(0,len(grid)):
			current_loc = (ro,co)
			if (grid[ro][co] != "O"):
				if (is_satisfied(grid, R, current_loc, M_threshold, B_threshold) == False):
					desired_loc = evaluate_open_spot(grid, R, current_loc, M_threshold, B_threshold, opens)
					swap_value(grid, current_loc, desired_loc)
					if (desired_loc != current_loc):
						for loc3 in range(0,len(opens)):
							if (opens[loc3] == desired_loc):
								opens.append(current_loc)
								del(opens[loc3])
						relocation_count += 1
	return relocation_count





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
	count_steps = 0
	count_relocation = 0
	relocation_one_step = 10
	while ((count_steps < max_steps) and (relocation_one_step != 0)):
		relocation_one_step = 0
		relocation_one_step = simulate_one_step(grid, R, M_threshold, B_threshold, opens)
		count_relocation += relocation_one_step
		count_steps += 1
	# REPLACE -1 with an appropriate return value
	return count_relocation

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
