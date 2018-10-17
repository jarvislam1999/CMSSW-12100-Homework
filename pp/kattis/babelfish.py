import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/babelfish
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes two parameters: 
#
#  - A list of pairs. Each pair contains two strings in this order:
#    an English word and its equivalent foreign word 
#  - A list of words to translate
#
# You must return a list of translated words.
def solve(word_pairs, words):
    # Replace [] with the list of translated words
    return []


if __name__ == "__main__":
    line = sys.stdin.readline().strip()

    word_pairs = []
    while line != "":
        word_pairs.append(line.split())
        line = sys.stdin.readline().strip()

    words = []
    for line in sys.stdin:
        words.append(line.strip())

    translated = solve(word_pairs, words)

    for w in translated:
        print(w)
