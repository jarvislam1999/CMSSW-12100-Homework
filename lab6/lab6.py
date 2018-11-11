import numpy as np
import sys

# import linear regression and apply beta from PA #5.
sys.path.append("../pa5")
from model import linear_regression

def read_file(filename):
    '''
    Read data from the specified file.  Split the lines and convert
    float strings into floats.  Assumes the first row contains labels
    for the columns.

    Inputs:
      filename: name of the file to be read

    Returns:
      (list of strings, 2D array)
    '''
    with open(filename) as f:
        labels = f.readline().strip().split(',')
        data = np.loadtxt(f, delimiter=',', dtype=np.float64)
        return labels, data

def var(y):
    # replace 0.0 with proper return value
    return 0.0


def task2(b):
    ### Replace 0.0 with code to extract the desired slice
    print("rows 0, 1, and 2.")
    print(0.0)
    print()
    print("rows 0, 1, and 5")
    print(0.0)
    print()
    print("columns 0, 1, and 2")
    print(0.0)
    print()
    print("columns 0, 1, and 3")
    print(0.0)
    print()
    print("columns 0, 1, and 2 from rows 2 and 3.")
    print(0.0)
    print()

def go():
    city_col_names, city_data = read_file("../pa5/data/city/data.csv")

    graffiti = city_data[:,0]
    garbage = city_data[:,3]

    print("Task 1")
    print("GRAFFITI:", var(graffiti))
    print("GARBAGE:", var(garbage))
    print()
    print()


    print("Task 2")
    b = (np.arange(24)**2).reshape(6,4)
    task2(b)


    print("Task 3")
    ### REPLACE 0.0 with appropriate call to linear regression
    print("Rodents, Garbage => Crime", 0.0)
    print()
    print()


    print("Task 4")
    ### REPLACE 0.0 with appropriate call to linear regression
    print("Graffiti => Crime:", 0.0)
    print()
    print()

if __name__ == "__main__":
    go()
