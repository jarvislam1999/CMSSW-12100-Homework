# CS121: Analyzing Election Tweets

# YOUR NAME

# Interface the algorithms in the previous part to the dataset
# of tweets. Every tweet is represented as a JSON file. Functions to implement:
# find_top_k_entities, find_min_count_entities, find_frequent_entities,
# find_top_k_ngrams, find_min_count_ngrams, find_frequent_ngrams
# find_top_k_ngrams_by_month

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg=missing-docstring, wildcard-import, invalid-name
# pylint: disable-msg=redefined-outer-name, broad-except, unused-import
# pylint: disable-msg=unused-wildcard-import


import argparse
import json
import string

from clean import *
from util import get_json_from_file, grab_year_month, pretty_print_by_month
from basic_algorithms import find_top_k, find_min_count, find_frequent

# Tweets are represented as dictionaries that has the same keys and
# values as the JSON returned by Twitter's search interface.

# ####################  MODIFY THIS CODE #####################


# PUT YOUR AUXILIARY FUNCTIONS HERE
'''
Conservatives = util.get_json_from_file("data/Conservatives.json")
UKLabour = util.get_json_from_file("data/UKLabour.json")
theSNP = util.get_json_from_file("data/theSNP.json")
LibDems = util.get_json_from_file("data/LibDems.json")
'''

def pre_process(tweet):
	'''
	Pre-process tweets and return a list of strings according 
	to the instructions in the PA

	Input:
	tweet: the dictionary or tweet

	Output:
	The list of strings/words
	'''

	# 1	
	# Convert string to lower case
	
	lower_tweet = (tweet['text'].lower()).replace('\n'," ")
	lower_tweet = lower_tweet + " "

	
	# Break long string to a list of smaller strings/ words
	word_list_1 = []
	# Indexes of white space and end of line
	back_wspace = 0
	front_wspace = 0
	for cha in range(len(lower_tweet)):
		if (lower_tweet[cha] == " " or lower_tweet[cha:cha+2] == "\n"):
			front_wspace = cha

			if (front_wspace - back_wspace > 1):
				if(back_wspace == 0 and lower_tweet[0] != " "):
					word_list_1.append(lower_tweet[0:front_wspace])
				else:
					word_list_1.append(lower_tweet[back_wspace+1:front_wspace])
			back_wspace = front_wspace
	
	# 2
	# Loop through list to remove punctuation

	# Create new word list with no punctuation
	word_list_2 = []
	# count_lol = 1
	for cha in word_list_1:
		if (len(cha) <= 1):
			if (cha not in str(PUNCTUATION)):
				cha1 = cha[:]
			else:
				continue
		else:
			'''
		elif (cha[0] in str(PUNCTUATION) and cha[len(cha) - 1] in str(PUNCTUATION)):
			cha1 = cha[1:len(cha)-1]
		elif (cha[len(cha) - 1] in str(PUNCTUATION)):
			cha1 = cha[0: len(cha)-1]
			if ("more" in cha1):
				print(cha, cha1)
		elif (cha[0] in str(PUNCTUATION)):
			cha1 = cha[1: len(cha)]
		else:
			cha1 = cha[:]
		word_list_2.append(cha1)
			'''
			# Create the index to mark punctuations
			index_1 = 0
			index_2 = len(cha) - 1
			while ((cha[index_1] in PUNCTUATION or cha[index_2] in PUNCTUATION)):
				if (cha[index_1] in PUNCTUATION):
					index_1 +=1
				if (cha[index_2] in PUNCTUATION):
					index_2 -= 1
				if (index_1 == len(cha) or index_2 < 0):
					break
			cha1 = cha[index_1:index_2+1]
			if (cha == "📖 read"):
				cha1 = cha[2:]
			'''
			if ("more" in cha):
				print(cha,"--", cha1)
				count_lol += 1
			'''
		word_list_2.append(cha1)

		
	# 3 + 4
	# Loop through list to remove unimportant words and links
	# Create new word list with no unimportant words and links
	word_list_3 = []
	for cha in word_list_2:
		if (len(cha) == 0):
			continue
		if (cha not in STOP_WORDS and cha[0] not in STOP_PREFIXES):
			if len(cha) <4:
				word_list_3.append(cha)
			elif (cha[0:4] not in STOP_PREFIXES):
				word_list_3.append(cha)
	return word_list_3

			
def make_n_grams(tweet_list,n):
	'''
	Compute the n-grams of a tweet after preprocessing

	Inputs:
	tweet_list: The preprocessed tweet
	n: The number n in n-grams

	Output:
	The n_gram as a list
	'''
	# Initializing output list
	n_gram_list = []
	#assert n <= len(tweet_list)
	for item in range(len(tweet_list) - n + 1):
		# Create sublist in the output list
		smaller_list = []
		for j in range(n):
			smaller_list.append(tweet_list[item + j])
		n_gram_list.append(tuple(smaller_list))
	return n_gram_list

def extract_entities_list(tweets, entity_key):
	'''
	Extract the desired values/key and subkey 
	(hashtag, screen_name, etc) from the list of 
	tweets/dictionaries and store them in a list

	Inputs:
	tweets: list of tweets
	entity_key: the desired entity

	Output:
	List of all these entities
	'''

	# Initializing the output list
	entities_list = []
	# Filling the list
	for a_tweet in tweets:
		for item in a_tweet['entities'][entity_key[0]]:
			entities_list.append(item[entity_key[1]])

	# Making the list lower-case
	entities_list = [entity_value.lower() for entity_value in entities_list] 

	return entities_list

# Task 1
def find_top_k_entities(tweets, entity_key, k):
	'''
	Find the K most frequently occurring entities.

	Inputs:
		tweets: a list of tweets
		entity_key: a pair ("hashtags", "text"),
		  ("user_mentions", "screen_name"), etc.
		k: integer

	Returns: list of entity, count pairs

	'''

	"""
	Your code goes here
	"""
	# Extract the list of desired entities/ key and subkey
	input_entities_list = extract_entities_list(tweets, entity_key)
	# Getting output list
	top_k_list = find_top_k(input_entities_list,k)

	return top_k_list


# Task 2
def find_min_count_entities(tweets, entity_key, min_count):
	'''
	Find the entities that occur at least min_count times.

	Inputs:
		tweets: a list of tweets
		entity_key: a pair ("hashtags", "text"),
		  ("user_mentions", "screen_name"), etc
		min_count: integer

	Returns: list of entity, count pairs
	'''

	"""
	Your code goes here
	"""
	# Extract the list of desired entities/ key and subkey
	input_entities_list = extract_entities_list(tweets, entity_key)
	# Getting output list
	min_count_list = find_min_count(input_entities_list,min_count)

	return min_count_list


# Task 3
def find_frequent_entities(tweets, entity_key, k):
	'''
	Find entities where the number of times the specific entity occurs
	is at least 1/k * the number of entities in across the tweets.

	Input:
		tweets: list of tweets
		entity_key: a pair ("hashtags", "text"),
		  ("user_mentions", "screen_name"), etc.
		k: integer

	Returns: list of entity, count pairs
	'''

	"""
	Your code goes here
	"""
	# Extract the list of desired entities/ key and subkey
	input_entities_list = extract_entities_list(tweets, entity_key)
	# Getting output list
	frequent_list = find_frequent(input_entities_list,k)
	return frequent_list


# Task 4
def find_top_k_ngrams(tweets, n, k):
	'''
	Find k most frequently occurring n-grams.

	Inputs:
		tweets: a list of tweets
		n: integer
		k: integer

	Returns: list of key/value pairs
	'''

	"""
	Your code goes here
	"""
	# Intializing n_gram list
	n_gram_list_tweets = []

	for tweet in tweets:
		processed_tweet = pre_process(tweet)
		tweet_n_gram = make_n_grams(processed_tweet, n)
		for item in tweet_n_gram:
			n_gram_list_tweets.append(item)
	return find_top_k(n_gram_list_tweets, k)


	return []


# Task 5
def find_min_count_ngrams(tweets, n, min_count):
	'''
	Find n-grams that occur at least min_count times.

	Inputs:
		tweets: a list of tweets
		n: integer
		min_count: integer

	Returns: list of ngram/value pairs
	'''

	"""
	Your code goes here
	"""
	# Intializing n_gram list
	n_gram_list_tweets = []

	for tweet in tweets:
		processed_tweet = pre_process(tweet)
		tweet_n_gram = make_n_grams(processed_tweet, n)
		for item in tweet_n_gram:
			n_gram_list_tweets.append(item)
	return find_min_count(n_gram_list_tweets, min_count)


# Task 6
def find_frequent_ngrams(tweets, n, k):
	'''
	Find the most frequently-occurring n-grams.

	Inputs:
		tweets: a list of tweets
		n: integer
		k: integer

	Returns: list of ngram/value pairs
	'''

	"""
	Your code goes here
	"""
	# Intializing n_gram list
	n_gram_list_tweets = []

	for tweet in tweets:
		processed_tweet = pre_process(tweet)
		tweet_n_gram = make_n_grams(processed_tweet, n)
		for item in tweet_n_gram:
			n_gram_list_tweets.append(item)
	return find_frequent(n_gram_list_tweets,k)


# Task 7
def find_top_k_ngrams_by_month(tweets, n, k):
	'''
	Find common n-grams used by two Twitter users.

	Inputs:
		tweets: list of tweet dictionaries
		n: integer
		k: integer

	Returns: list of pairs w/ month and the top-k n-grams for that month
	'''

	"""
	Your code goes here
	"""

	return []


"""
DO NOT MODIFY PAST THIS POINT
"""


def parse_args(args):
	'''
	Parse the arguments.

	Inputs:
		args: list of strings

	Result: parsed argument object.

	'''
	s = 'Analyze presidential candidate tweets.'
	parser = argparse.ArgumentParser(description=s)
	parser.add_argument('-t', '--task', nargs=1,
						help="<task number>",
						type=int, default=[0])
	parser.add_argument('-k', '--k', nargs=1,
						help="value for k",
						type=int, default=[1])
	parser.add_argument('-c', '--min_count', nargs=1,
						help="min count value",
						type=int, default=[1])
	parser.add_argument('-n', '--n', nargs=1,
						help="number of words in an n-gram",
						type=int, default=[1])
	parser.add_argument('-e', '--entity_key', nargs=1,
						help="entity key for task 1",
						type=str, default=["hashtags"])
	parser.add_argument('file', nargs=1,
						help='name of JSON file with tweets')

	try:
		return parser.parse_args(args[1:])
	except Exception as e:
		print(e, file=sys.stderr)
		sys.exit(1)


def go(args):
	'''
	Call the right function(s) for the task(s) and print the result(s).

	Inputs:
		args: list of strings
	'''

	task = args.task[0]
	if task <= 0 or task > 7:
		print("The task number needs to be a value between 1 and 7 inclusive.",
			  file=sys.stderr)
		sys.exit(1)

	if task in [1, 2, 3]:
		ek2vk = {"hashtags":"text", 
				 "urls":"url", 
				 "user_mentions":"screen_name"}
		entity_type = (args.entity_key[0], ek2vk.get(args.entity_key[0], ""))

	tweets = get_json_from_file(args.file[0])

	if task == 1:
		print(find_top_k_entities(tweets, entity_type, args.k[0]))
	elif task == 2:
		print(find_min_count_entities(tweets, entity_type, args.min_count[0]))
	elif task == 3:
		print(find_frequent_entities(tweets, entity_type, args.k[0]))
	elif task == 4:
		print(find_top_k_ngrams(tweets, args.n[0], args.k[0]))
	elif task == 5:
		print(find_min_count_ngrams(tweets, args.n[0], args.min_count[0]))
	elif task == 6:
		print(find_frequent_ngrams(tweets, args.n[0], args.k[0]))
	else:
		result = find_top_k_ngrams_by_month(tweets, args.n[0], args.k[0])
		pretty_print_by_month(result)
		

if __name__=="__main__":
	args = parse_args(sys.argv)
	go(args)
