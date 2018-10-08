'''
Epidemic modeling

YOUR NAME

Functions for running epidemiological simulation
'''

import random
import os.path
import sys

import util

# A few constants to simplify debugging
TEST_SEED = 20170217
INFECTION_RATE_LIST = [0, 0.25, 0.5, 0.75, 1.0]

def count_infected(city):
	'''
	Purpose: Count the number of infected people

	Inputs:
		city (list): the state of all people in the simulation
			at the start of the day

	Returns (int): number of infected people in the city
	'''

	# YOUR CODE HERE

	# Output number of infected people variable, initialized
	infectedcount = 0

	#For loop to count number of infected people in city
	for person in city:
		if (person == "I0" or person == "I1"):
			infectedcount = infectedcount +1

	# REPLACE 0 WITH THE APPROPRIATE RETURN VALUE
	return infectedcount


def has_an_infected_neighbor(city, position):
	'''
	Purpose: determine whether a person has an infected neighbor

	Inputs:
		city (list): the state of all people in the simulation
			at the start of the day
		position (int): the position of the person to check
	Returns:
		True, if the person has an infected neighbor, False otherwise.
	'''
	assert city[position] == "S"

	# YOUR CODE HERE
	
	# Final boolean output variable, initialized
	infectedneighbor = False

	# Check for infected neighbor, additional if statement to account the last 
	if position == len(city)-1:
		if (city[0] == "I0" or city[0]=="I1" or city[position-1] == "I0" or city[position-1]== "I1"):
			infectedneighbor = True
	else:
		if (city[position+1] == "I0" or city[position+1]=="I1" or city[position-1] == "I0" or city[position-1]== "I1"):
			infectedneighbor = True

	# REPLACE False WITH THE APPROPRIATE RETURN VALUE
	return infectedneighbor


def gets_infected_at_position(city, position, infection_rate):
	'''
	Purpose: Determine whether the person at position gets infected.

	Inputs:
		city (list): the state of all people in the simulation
			at the start of the day
		position (int): the position of the person to check
		infection_rate (float): the chance of getting infected if one of your
			neighbors is infected

	Returns:
		 True, if the person should be infected, False otherwise.
	'''

	# YOUR CODE HERE

	# Final boolean output variable, initialized
	get_infected = False

	# Check for infected neighbor before continue
	if has_an_infected_neighbor(city, position):
		if city[position] == "S":
			#Assign immunity level randomly
			immunity_level = random.random()
			#Determine if one gets infected
			if immunity_level < infection_rate:
				get_infected = True


	# REPLACE False WITH THE APPROPRIATE RETURN VALUE
	return get_infected


def simulate_one_day(city, infection_rate):
	'''
	Purpose: to move the simulation forward a single day.

	Inputs:
		city (list of strings): the starting state of the
			simulation, i.e., what disease state each person is. A
			starting state of ['S', 'I', 'R'] means that person 0
			starts the day susceptible to disease, person 1 starts the
			day infected by the disease, and person 2 has starts the
			day protected from disease

		t (int): the duration of the infected state (i.e., how many
			days it will take someone in state 'I' to turn into state
			'R')

		infection_rate (float): the chance of getting infected if one of your
			neighbors is infected

	Returns:
		tuple (new_city, new_timing) of
		  new_city (list): disease state of the city after one day
		  new_timing (list): timings for the city after one day
	'''

	# YOUR CODE HERE

	#Initialize output list 
	new_city = []

	#Putting values into new list
	for i in range(0, len(city)):
		if city[i] == "S":
			if gets_infected_at_position(city, i, infection_rate):
				new_city.append("I1")
			else:
				new_city.append(city[i])
		elif city[i] == "I1":
			new_city.append("I0")
		elif city[i] == "I0":
			new_city.append("R")
		else:
			new_city.append(city[i])

	# REPLACE [] WITH THE APPROPRIATE RETURN VALUE
	return new_city
# I only put in the result as a list instead of a tuple because this is what worked for the test

def run_simulation(starting_state, random_seed, max_num_days, infection_rate):
	'''
	Purpose: to run the entire simulation.

	Inputs:
		starting_state (list of strings): the starting states of all
			members of the simulation
		random_seed (int): the random seed to use for the simulation
		d (int): the maximum days of the simulation
		infection_rate (float): the chance of getting infected if one of your
			neighbors is infected

	Returns:
		tuple (city, d) of
			city (list): the final state of the simulation
			d (int): days of the simulation
	'''

	assert max_num_days >= 0

	# YOUR CODE HERE

	# Final city initialized
	city = []
	# Days of the simulation initialized
	d = 0

	#Setting the seed
	random.seed(random_seed)

	# Simulate the first day
	city = simulate_one_day(starting_state, infection_rate)
	d= d+1

	#Simulate until conditions met
	while (d < max_num_days and count_infected(city) != 0):
		city = simulate_one_day(city, infection_rate)
		d = d+1

	return city, d


def compute_average_num_infected(
		starting_state, random_seed, max_num_days, infection_rate, num_trials):
	'''
	Purpose: to conduct N trials with one infection probability and calculate
		how many people on average get infected over time

	Inputs:
		starting_state (list of strings): the starting states of all
			members of the simulation
		random_seed (int): the random seed to set the simulation to for
			every single time the simulation runs. This is what the FIRST s
			simulation will use, and then will be incremented every time the
			simulation runs
		max_num_days (int): the maximum days of the simulation
		infection_rate (float): the chance of getting infected if one of your
			neighbors is infected
		num_trials (int): the number of trials to run

	Returns:
		(int): the average number of people infected over time
	'''

	assert num_trials > 0

	# YOUR CODE HERE

	# List to get the average from
	list_count_infected = []

	#Filling this list with number of infected people
	for i in range(0, num_trials):
		infected_city = run_simulation(starting_state, random_seed, max_num_days, infection_rate)
		#print(infected_city)
		infected_count = 0
		for j in range(0,len(infected_city[0])):
			#print(infected_city[0][j])
			if (infected_city[0][j] == "I0" or infected_city[0][j] == "I1" or infected_city[0][j] == "R"):
				infected_count= infected_count+1
		list_count_infected.append(infected_count)
		#print(infected_count)
		random_seed = random_seed +1
	sum_infected = 0
	for i in list_count_infected:
		sum_infected = sum_infected +i
	mean_infected = sum_infected/len(list_count_infected)

	return mean_infected

def infection_rate_param_sweep(
		starting_state, random_seed, d, infection_rate_list, num_trials):
	'''
	Purpose: run trials where the starting state and random_seed are
		constant, but the infection rate is changing

	Inputs:
		starting_state (list of strings): the starting states of all
			members of the simulation
		randostarting_state, random_seed, max_num_days, infection_ratem_seed (int): the random seed to set the simulation to for
			every single time the simulation runs. This is what the FIRST s
			simulation will use, and then will be incremented every time the
			simulation runs
		max_num_days (int): the maximum days of the simulation
		num_trials (int): the number of trials to run
		infection_rate_list (list of floats): a list of the chance of getting
			infected if one of your neighbors is infected per trial

	Returns:
		infected_number_list (list of ints): the number of people infected
			indexed by trial
	'''

	# YOUR CODE HERE
	list_infection_rate_average = []
	for rate_infected in infection_rate_list:
		infection_average = compute_average_num_infected(starting_state, random_seed, d, rate_infected, num_trials)
		list_infection_rate_average.append(infection_average)

	# REPLACE [] WITH THE APPROPRIATE RETURN VALUES
	return list_infection_rate_average


################ Do not change the code below this line #######################


def run():
	'''
	Process the command-line arguments and do the work.
	'''
	usage = ("usage: python simulation.py <data_filename>")

	if len(sys.argv) != 2:
		print(usage)
		return

	input_filename = sys.argv[1]
	if not os.path.isfile(input_filename):
		print(usage)
		print("error: file not found: {}".format(input_filename))
		return

	# check that state number is valid -- no key error
	try:
		starting_state, random_seed, max_num_days, \
			infection_rate, num_trials = util.get_config(input_filename)
	except KeyError:
		print(usage)
		return

	print("Running initial simulation...")
	(final_state, sim_days) = run_simulation(
		starting_state, random_seed, max_num_days, infection_rate)
	print("The starting state of the simulation was {}.".format(
		starting_state))
	print("The final state of the simulation is {}.". format(
		final_state))
	print("The simulation ended after day {}.".format(sim_days))

	print("Running multiple trials...")
	avg_infected = compute_average_num_infected(
		starting_state, random_seed, max_num_days, infection_rate, num_trials)
	print("Over {} trial(s), on average, {:3.1f} people were infected".format(
		num_trials, avg_infected))

	print("Varying infection parameter...")
	infected_list = infection_rate_param_sweep(
		starting_state, random_seed, max_num_days,
		INFECTION_RATE_LIST, num_trials)
	printstr = "Rate | Infected"
	for rate, infected_number in zip(INFECTION_RATE_LIST, infected_list):
		printstr += "\n{:4.1f} | {:2.2f}".format(rate, infected_number)
	print(printstr)

if __name__ == "__main__":
	run()
