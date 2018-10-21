# CS121: Analyzing Election Tweets

# JARVIS LAM

# Algorithms for efficiently counting and sorting distinct
# `entities`, or unique values, are widely used in data
# analysis. Functions to implement: count_items, find_top_k,
# find_min_count, find_frequent

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg=missing-docstring

from util import sort_count_pairs


def count_items(items):
	'''
	Counts each distinct item (entity) in a list of items

	Inputs:
		items: list of items (must be hashable/comparable)

	Returns: list (item, number of occurrences).
	'''

	# YOUR CODE GOES HERE

	# Initializing dictionary to store count for distinct items
	count_dict = {}
	# Loop through input list and fill dictionary
	for i in items:
		if i not in count_dict:
			count_dict[i] = 0
		count_dict[i] += 1

	# Initializing output list
	count_list = []
	# Putting data from dictionary to the list
	for i in count_dict:
		count_list.append((i, count_dict[i]))


	# REPLACE RETURN VALUE WITH AN APPROPRIATE VALUE
	return count_list


def find_top_k(items, k):
	'''
	Find the K most frequently occurring items

	Inputs:
		items: list of items (must be hashable/comparable)
		k: a non-negative integer

	Returns: sorted list of the top K tuples

	'''

	# Error checking (DO NOT MODIFY)
	if k < 0:
		raise ValueError("In find_top_k, k must be a non-negative integer")

	# Runs the helper function for you (DO NOT MODIFY)
	item_counts = count_items(items)

	# YOUR CODE GOES HERE

	# Initializing output list
	top_k_list = []
	# Initializing sorted list
	sorted_item_counts = sort_count_pairs(item_counts)

	if len(sorted_item_counts) <= k:
		return sorted_item_counts
	for num in range(k):
		top_k_list.append(sorted_item_counts[num])

	# REPLACE RETURN VALUE WITH AN APPROPRIATE VALUE
	return top_k_list


def find_min_count(items, min_count):
	'''
	Find the items that occur at least min_count times

	Inputs:
		items: a list of items  (must be hashable/comparable)
		min_count: integer

	Returns: sorted list of tuples
	'''

	# Runs the helper function for you (DO NOT MODIFY)
	item_counts = count_items(items)
	if (len(items) == 0):
		return []
	print(item_counts)
	# YOUR CODE HERE

	# Sort item_counts
	sorted_item_counts = sort_count_pairs(item_counts)
	# Initializing output list
	min_count_list = []

	# Filling the output list
	index = 1
	print(sorted_item_counts)
	count_until_min = sorted_item_counts[index - 1][1]
	while (count_until_min >= min_count and index <= len(sorted_item_counts)):
		min_count_list.append(sorted_item_counts[index - 1])
		index += 1
		if (index <= len(sorted_item_counts)):
			count_until_min = sorted_item_counts[index - 1][1]
	# REPLACE RETURN VALUE WITH AN APPROPRIATE VALUE
	return min_count_list


def find_frequent(items, k):
	'''
	Find items where the number of times the item occurs is at least
	1/k * len(items).

	Input:
		items: a list of items  (must be hashable/comparable)
		k: integer

	Returns: sorted list of tuples
	'''

	counter = {}

	for item in items:

		if len(counter) > k - 1:
			raise ValueError(
				"The number of elements stored in counter" +
				" should not exceed (k-1)=" + str(k-1))

		# YOUR CODE HERE
		# WRITE THE APPROPRIATE UPDATE LOGIC FOR COUNTER

	return sort_count_pairs(counter.items())
