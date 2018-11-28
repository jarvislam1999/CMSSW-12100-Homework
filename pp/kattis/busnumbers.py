import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/busnumbers
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

def solve(numbers):
    """
    Parameters:
     - numbers: List of integers. The list of bus numbers

    Returns: String. The shortest representation of the list of bus numbers
    """

    # YOUR CODE HERE
    dict_number = {}
    list_number = []

    for num in numbers:
        dict_number[num] = True
    for num in numbers:
        lower_index = num
        higher_index = num
        if (dict_number[num]):
            while(lower_index - 1 in dict_number):
                lower_index -= 1
                dict_number[lower_index] = False
            while(higher_index + 1 in dict_number):
                higher_index += 1
                dict_number[higher_index] = False
            if(higher_index - lower_index == 0):
                list_number.append(num)
            elif (higher_index - lower_index == 1):
                list_number.append(lower_index)
                list_number.append(higher_index)
            else:
                list_number.append(str(lower_index) + "-" + str(higher_index))
        dict_number[num] = False
    return list_number

    # Replace "" with your return value
    return ""


if __name__ == "__main__":
    tokens = sys.stdin.read().strip().split()
    tokens.reverse()

    n = int(tokens.pop())
    numbers = [int(tokens.pop()) for _ in range(n)]

    numbers_str = solve(numbers)
    assert isinstance(numbers_str, str), "solve() should return a string"
    print(numbers_str)        
