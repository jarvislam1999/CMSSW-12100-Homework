import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/engineeringenglish
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes a single parameter: a list of strings, each corresponding
# to a line of input. You must return a list of strings where the strings
# have been converted as described in the problem statement.
def solve(lines):
    # YOUR CODE 
    word_dict= {}
    word_list = []
    for line in lines:
    	word_list.extend(line.lower().split())
    for word in range(0, len(word_list) -1):
    	if (word_list[word] in word_dict):
    		word_list[word] = '.'
    	else:
    		word_dict[word_list[word]] = True

    # Replace [] with the list of processed strings
    return " ".join(word_list)


if __name__ == "__main__":
    lines = [s.strip() for s in sys.stdin.readlines()]

    print("\n".join(solve(lines)))
