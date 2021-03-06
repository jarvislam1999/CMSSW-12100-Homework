import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/quickbrownfox
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes one parameter: the phrase (as described in the problem statement)
#
# It must return a list of letters that are missing from the phrase (i.e., that 
# prevent the phrase from being a pangram, as described in the problem statement) 
# The missing letters should be reported in lower case and should be sorted 
# alphabetically.
#
# If the phrase is a pangram, just return an empty list.
def solve(phrase):
    # YOUR CODE HERE
    pphrase = phrase.lower().replace(" ", "").replace("'", "")
    letter_dict = {}
    missing = []
    for l in pphrase:
        letter_dict[l] = True
    for l in range(ord('a'), ord('z')):
        if (chr(l) not in letter_dict):
            missing.append(chr(l))
    if (len(missing) == 0):
        return "pangram"
    else:
        return "missing " + "".join(missing)
    # Replace [] with the list of missing characters
    


if __name__ == "__main__":
    ntests = int(sys.stdin.readline())

    for i in range(ntests):
        phrase = sys.stdin.readline().strip()
        missing = solve(phrase)

        if len(missing) == 0:
            print("pangram")
        else:
            print("missing", "".join(missing))
