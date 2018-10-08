import sys
import matplotlib.pyplot as plt

def read_data(filename):
    '''
    Reads a data file.

    A data file has two lines:
    - Line 1: A single integer representing the "maximum value".
              This is not necessarily the higher value in the data,
              but rather the maximum value to be used for the purposes
              of computing frequency distributions.
    - Line 2: One or more integers, each separated by a single space.

    Inputs:
        filename (string): Filename of data file

    Returns: (list of ints, int) The list of numbers,
       and the maximum value
    '''
    with open(filename, 'r') as f:
        values = [int(x) for x in f.read().strip().split()]

    max_value = values.pop(0)

    return values, max_value


def save_data(filename, values, max_value):
    '''
    Saves integers to a data file.

    See read_data docstring for file format.

    Inputs:
        filename (string): Filename of data file
        values (list of ints): Integers
        max_value: The maximum value

    Returns: Nothing
    '''

    with open(filename, 'w') as f:
        print(max_value, file=f)
        print(" ".join([str(x) for x in values]), file=f)
            

def plot_frequencies(values):
    '''
    Produces a histogram for a list of integers

    Inputs:
        values (list of ints): Integers

    Returns: Nothing
    '''
    min_value = min(values)-1
    max_value = max(values)+1

    if max_value - min_value < 10:
        bins = 10
    else:
        bins = max_value - min_value

    plt.hist(values, bins=bins, range=(min_value,max_value), align="mid")


def compute_cfd(values, max_value):
    '''
    Compute the CFD of a list of integers.

    Inputs:
        values (list of ints): Integers
        max_value: The maximum value

    Returns: (list of floats) The CFD
    '''

    # YOUR CODE GOES HERE

    return []
    
    
def plot_cfd(values, max_value):
    '''
    Produces a CFD plot for a list of integers

    Inputs:
        values (list of ints): Integers
        max_value (int): The maximum value

    Returns: Nothing
    '''
    cfreq = compute_cfd(values, max_value)
    plt.plot(range(len(cfreq)), cfreq)


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("USAGE: cfd.py NUMBERS_FILE")

    filename = sys.argv[1]

    values, max_value = read_data(filename)
    
    cfreq = compute_cfd(values, max_value)

    print("The CFD is", cfreq)
    


