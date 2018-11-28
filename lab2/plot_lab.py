import math
import pylab
import numpy


def sinc(x):
    ''' Compute the sampling (or sine cardinal) function'''
    if x != 0:
        return math.sin(x) / x
    else:
        return 1


def plot_sinc():
    ''' Plot the sinc function '''

    # Compute Xs using range or numpy.arange
    # Compute Ys using a loop
    # Call plot
    # Call show
    # remove the next line
    pass
